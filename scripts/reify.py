import argparse
import os
import sys
from io import TextIOWrapper
from typing import List, Dict, Tuple, Optional, cast, Union, Set

from argparse import ArgumentParser
from funowl import Class, ObjectIntersectionOf, ObjectSomeValuesFrom, EquivalentClasses, Declaration, NamedIndividual, \
    AnnotationValue, AnnotationAssertion, AnnotationSubject, SubClassOf, ClassExpression, ClassAssertion, \
    ObjectPropertyAssertion, Individual, IRI, Prefix
from funowl.converters.functional_converter import to_python
from funowl.ontology_document import IN_FUNCTIONAL, Ontology, OntologyDocument, Import
from rdflib import URIRef, Graph, RDFS, Namespace, OWL

cwd = os.path.dirname(__file__)

URIRef_or_STR = Union[URIRef, str]

# SNOMED CT Namespace
SCT = Namespace("http://snomed.info/id/")
role_group = SCT['609096000']

EX = Namespace("http://example.org/person/")

# Namespace for proxy nodes
PROXY = Namespace("http://ontologies-r.us/bdp/proxy#")

# Ontology name -- defn is the root type
ONT = "Ontology(<http://ontologies-r.us/bdp/proxy#>\n{defn})"


class IndividualFactory:
    def __init__(self, source_ontology: OntologyDocument, reference_code: URIRef_or_STR, skip_role_groups: bool = False,
                 single_individuals: bool = False) -> None:
        """
        Factory for realizing an instance of a T-Box into an individual
        :param source_ontology: T-Box
        :param reference_code: Class to be realized
        :param skip_role_groups:  True means skip over SNOMED-CT role groups
        :param single_individuals: True means create only ONE individual per class
        """

        # Set up the input T-Box
        source_ontology.prefixDeclarations.append(Prefix('p', PROXY))
        source_ontology.prefixDeclarations.append(Prefix('ex', EX))
        source_ontology.prefixDeclarations.append(Prefix('sct', SCT))
        self.source_graph = Graph()
        source_ontology.to_rdf(self.source_graph, emit_functional_definitions=True)
        self.source_axioms = source_ontology.ontology.axioms

        # Establish the starting node
        self.reference_uri = reference_code if isinstance(reference_code, URIRef) else \
            IRI(str(reference_code)).full_uri(self.source_graph)
        reference_local_name = self._local_name(self.reference_uri)

        # Create the output A-Box
        self.target_ontology = OntologyDocument(ontology=Ontology(PROXY[reference_local_name]))
        self.target_axioms = self.target_ontology.ontology.axioms
        self.target_ontology.ontology.imports(source_ontology.ontology)
        for prefix in source_ontology.prefixDeclarations:
            self.target_ontology.prefixDeclarations.append(prefix)
        self.target_ontology.ontology.imports(source_ontology)

        self.skip_role_groups = skip_role_groups
        self.single_individuals = single_individuals

        # Instances of a given class
        self.individuals: Dict[URIRef, List[URIRef]] = {}

        # Recursion detection
        self.realized: Set[Tuple[str, str]] = set()

    def _local_name(self, uri: URIRef) -> str:
        """ Return the local name associated with uri """
        str_uri = str(uri)
        if "://" not in str_uri:
            return str_uri.rsplit(':', 1)[1] if ':' in str_uri else str_uri
        prefix_len = 0
        for _, prefix in self.source_graph.namespaces():
            if str_uri.startswith(prefix):
                prefix_len = max(len(prefix), prefix_len)
        if prefix_len == 0:
            if '#' in str_uri:
                return str_uri.rsplit('#', 1)[1]
            else:
                return str_uri.rsplit('/', 1)[1]
        else:
            return str_uri[prefix_len:]

    def _full_uri_for(self, uri: Union[str, URIRef_or_STR, IRI]) -> URIRef:
        if '://' in str(uri):
            return URIRef(str(uri))
        else:
            if not isinstance(uri, IRI):
                uri = IRI(uri)
            return uri.full_uri(self.source_graph)

    def _individual_uri_and_name_for(self, cls: Optional[Class] = None) -> Tuple[URIRef, str]:
        """
        Create an individual URIRef_or_STR and name for an instance of cls
        :param cls: Class to be instantiated
        :return: URIRef_or_STR and label for individual
        """
        if not cls:
            cls = OWL.Thing
            cls_name = "Thing"
        else:
            if '://' not in str(cls):
                cls = cls.full_uri(self.source_graph)
            cls_name = str(self.source_graph.label(cls, "Thing"))
        if not self.single_individuals:
            entry_num = len(self.individuals.setdefault(cls, [])) + 1
        else:
            self.individuals.setdefault(cls, [])
            entry_num = 1
        ind_uri = cast(URIRef, PROXY[self._local_name(cls) + f"_{entry_num}"])
        self.individuals[cls].append(ind_uri)
        ind_name = "Instance " + \
                   (str(entry_num) + ' ' if entry_num > 1 else '') + "of " + cls_name[0].lower() + cls_name[1:]
        return ind_uri, ind_name

    def new_individual(self, cls: Optional[Class]) -> Individual:
        """
        Create a new individual that represents an instance cls (or owl:Thing if class is not supplied)
        :param cls: Class
        :return: Named Individual

        This creates a declaration and label. It does NOT add the type entry
        """
        ind_uri, ind_name = self._individual_uri_and_name_for(cls)
        nind = NamedIndividual(ind_uri)
        self.target_axioms.append(Declaration(nind))
        self.target_axioms.append(AnnotationAssertion(RDFS.label, AnnotationSubject(nind), AnnotationValue(ind_name)))
        return cast(Individual, nind)

    def proc_object_some_values_from(self, osvf: ObjectSomeValuesFrom, subject: Individual) -> None:
        """
        This is the workhorse of this process.  Create a new individual that reflects the internal class expression
        and add an assertion connecting ind with the new individual
        :param osvf: SomeValuesFrom statement
        :param subject: subject
        """
        predicate = osvf.objectPropertyExpression
        skip_rg = self.skip_role_groups and self._full_uri_for(IRI(predicate)) == role_group
        if skip_rg:
            obj = subject
        else:
            # If we've got any bare classes, create an instance of them
            obj = self.new_individual(osvf.classExpression if isinstance(osvf.classExpression, Class) else None)
        self.proc_class_expression(osvf.classExpression, obj)
        if not skip_rg:
            self.target_axioms.append(ObjectPropertyAssertion(predicate, subject, obj))

    def proc_intersection_of(self, io: ObjectIntersectionOf, ind: Individual) -> None:
        for ce in io.classExpressions:
            if isinstance(ce, Class):
                self.realize_against(ind, ce)
            elif isinstance(ce, ObjectSomeValuesFrom):
                self.proc_object_some_values_from(ce, ind)
            else:
                print(f"Unprocessed intersection of entry: {type(ce).__name__}")

    def proc_class_expression(self, ce: ClassExpression, ind: Individual) -> None:
        if isinstance(ce, ObjectIntersectionOf):
            self.proc_intersection_of(ce, ind)
        elif isinstance(ce, ObjectSomeValuesFrom):
            self.proc_object_some_values_from(ce, ind)
        elif isinstance(ce, Class):
            self.realize_against(ind, ce)
        else:
            print(f"Unrecognized class expression: {type(ce).__name__}")

    def proc_subclass_of(self, sco: SubClassOf, ind: Individual) -> None:
        """
         Process a subclassof expression
        :param sco: Subclassof definition
        :param ind: Individual being defined
        """
        self.proc_class_expression(sco.superClassExpression, ind)

    def proc_equivalent_classes(self, ec: EquivalentClasses, ind: Individual) -> None:
        """
        Process an equivalent classes expression
        :param ec: expression to process
        :param ind: individual claimed to be a member of the definition
        """
        for ce in ec.classExpressions:
            if isinstance(ce, Class):
                self.realize_against(ind, ce)
            else:
                self.proc_class_expression(ce, ind)

    def realize_against(self, ind: Individual, cls: Union[URIRef_or_STR, Class]) -> None:
        """
        Realize ind against the definition of cls
        :param ind: individual to be realized
        :param cls: class to realize it against
        """
        cls_uri = self._full_uri_for(cls)
        k = (str(cls_uri), str(ind))
        if k not in self.realized:
            self.realized.add(k)
            self.target_axioms.append(ClassAssertion(cls, ind))
            for func_stmt in self.source_graph.objects(cls_uri, IN_FUNCTIONAL):
                if func_stmt.startswith('EquivalentClasses('):
                    o = to_python(ONT.format(defn=func_stmt))
                    self.proc_equivalent_classes(o.ontology.axioms[0], ind)
                elif func_stmt.startswith('SubClassOf('):
                    o = to_python(ONT.format(defn=func_stmt))
                    self.proc_subclass_of(o.ontology.axioms[0], ind)
                elif not func_stmt.startswith('Annotation') and not func_stmt.startswith('Declaration('):
                    raise NotImplementedError(f"Unimplemented class definition type: {func_stmt}")

    def create_instance_for(self, cls: Union[URIRef, URIRef_or_STR, Class]) -> Individual:
        """ Create and define an instance of cls
        :param cls: class to be instantiated
        :return: URIRef_or_STR of the individual that represents this class
        """
        ind = self.new_individual(cls if isinstance(cls, Class) else Class(cls))
        self.realize_against(ind, cls)
        return ind

    def create_instances(self) -> Individual:
        """ Create the outermost instance """
        return self.create_instance_for(self.reference_uri)


def realize(code: Union[str, URIRef], input_ontology_file: Union[str, TextIOWrapper], output_ontology_file: str,
            subject: Union[str, URIRef] = EX.Joe, predicate: Union[str, URIRef_or_STR] = EX.hasDiagnosis,
            skip_role_groups: bool = False, single_individuals: bool = False) -> bool:
    """
    Realize subject, predicate, code as an A-box against the input ontology file
    :param code: CURIE or URIRef_or_STR of code to reconcile
    :param input_ontology_file: name, URIRef_or_STR or file handle of input ontology
    :param output_ontology_file: output file name.  If omitted, prints to sys.stdout
    :param subject: CURIE or URIRef_or_STR of data subject
    :param predicate: CURIE or URIRef_or_STR of data predicate
    :param skip_role_groups: True means ignore SNOMED CT Role groups
    :param single_individuals: True means only emit one individual per type
    :return: success indicator
    """
    input_ontology = to_python(input_ontology_file)
    factory = IndividualFactory(input_ontology, code, skip_role_groups, single_individuals)
    rval = factory.create_instances()
    factory.target_axioms.append(ObjectPropertyAssertion(predicate, subject, rval))
    output = str(factory.target_ontology.to_functional())
    if output_ontology_file:
        with open(output_ontology_file, 'w') as oo:
            oo.write(output)
        print(f"\n{os.path.relpath(os.path.abspath(output_ontology_file), cwd)} written")
    else:
        print(output)
    return True


def genargs() -> ArgumentParser:
    """
    Generate an input string parser
    :return: parser
    """
    parser = ArgumentParser(description="Reify an individual against an ontology")
    parser.add_argument("ontology", help="Ontology to use for reconciliation", type=argparse.FileType('r'))
    parser.add_argument("concept", help="Start concept CURIE or URI")
    parser.add_argument("-o", "--output", help="Reconciliation output. Default: sys.stdout")
    parser.add_argument("-s", "--subject", help="Data level subject. Default: EX:Joe", default=str(EX.Joe))
    parser.add_argument("-p", "--predicate", help="Data level predicate.  Default: Ex.hasDiagnisis",
                        default=str(EX.hasDiagnosis))
    parser.add_argument("--skip_role_groups", help="Don't emit role groups as separate objects", action="store_true")
    parser.add_argument("--single_individuals", help="Only emit one individual per class", action="store_true")
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    opts = genargs().parse_args(argv)
    return realize(opts.concept, opts.ontology, opts.output, opts.subject, opts.predicate, opts.skip_role_groups,
                   opts.single_individuals)

if __name__ == '__main__':
    sys.exit(main())
