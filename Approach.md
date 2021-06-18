# Research Question
A novel approach has recently been proposed for addressing what has been referred to as the "TermInfo Problem".  The "Terminfo Problem"
has focused on how clinical data records can be classified, compared and translated when information is represented in different levels of
granularity.  While some tools exist and some work has been done in the area of classfication and comparison https://github.com/hsolbrig/SNOMEDToOWL,
(CSIRO OntoServer), (quick literature search), the translation portion of the problem has remained relatively unaddressed.

We are proposing an approach to the translation problem that utilizes the notion of "proxy individuals" -- placeholders that 
represent the "unsaid" components of a data record, and can be used by a description logic (DL) reasoner to assemble any
desired combination of pre- and post-coordinated output. Using the following pipeline:

```
Data Record A --> (JSON-LD Context) --> RDF data set --> (DL Reasoner) --> Augmented RDF Data Set --> (ShExMap) --> (JSON-LD Context 2) --> Data Record B
                                                            ^  ^
                                                            |  |
                                        OWL Ontology -------+  |
                                                               |
                                        Proxy Individuals -----+
```

Our focus will be on the following aspects in the above pipeline:

1) How do we algorithmically produce the necessary set of `Proxy Individuals`
2) What needs to be added to the `OWL Ontology` to support the complete reasoning process (e.g. property chains, more complete definitions, ...)?
3) Will this approach be computationally tractable with existing DL reasoners and, if so, what type of reasoner is needed?

If it turns out that the answer to 3) above is "no", we may begin to look at what would be needed to create a scalable process.


## Background
Considerably thought and effort has gone in the definition of "value sets" -- enumerations of values, concept codes, URIs
or more complex structures that identify the set of possible answers for a field on a form, a column in a database, or an attribute 
in a transaction.   

The value set problem space encompasses the following components:

1) Definition and distribution -- how do we identify and maintain the the set possible values for a particular field?
2) Representation -- how should a specific value from a value set be represented in a database or computerized transaction?
3) Searching and classification -- how do we combine specific value set entries with their associated definitions and 
   classifications in order formulate queries?
4) Mapping and transformation -- how do we go about converting a specific value (or collection of specific values) from 
   a data record as it occurs in one model into a (near) equivalent (set of) values in a data record represented in a different
   data model?
   
While our work will draw on all four of these components, our primary focus will be on problem 4).  

We will constrain our work to value sets that derived from the collection of resource that are called "ontologies" and, within
that collection, on resources that use a formal description-logic definitions that are amenable to representation in the 
Web Ontology Language (OWL).

## Approach
We will begin by briefly examining some of current approaches to defining value sets in the terms of the target ontology, zeroing
in on some of the approaches used to define value sets in the NCI Thesaurus, in the HL7 FHIR models and in the Value Set
Authority Center (VSAC).

We will then draw on the ISO/IEC 11179-3 Metamodel and its implementation in the LinkML modeling language to help tease
apart the set of possible "value meanings" of a given field (Data Element in the 11179 model) from the set of "permissible values" --
the set of codes that can occur in the data element itself. 

We will then select a small set of representative examples -- drawing on the current FHIR specification, a
Stan Huff's CIMI slides (Suspected Lung Cancer), the CCDH Analyte-Type issue, a generic laterality example (Simple Fracture of the
Left Femur) and, possibly, a medication prescription example.

Using these examples, we will use the appropriate set of ontologies, which will include SNOMED-CT, the NCIt or Mondo and whatever
other ontologies may be needed.  

We will use Protege to examine and edit each of these ontologies, providing whatever additional DL statements that may be necessary.
[SoloOntology](https://github.com/hsolbrig/soloexample/blob/main/data/SoloOntology.owl) has a small example of one such set

We will then use small prototypes to arrive at a first approximation of the algorithm needed to produce the accompanying 
"proxy individuals" (see: [SoloCodeSets](https://github.com/hsolbrig/soloexample/blob/main/data/SoloCodesets.owl) for a
first cut at an example). Note that we may need to draw on the value set definitions themselves to support this task.  Also
note that the development of the proxy individuals may turn out to be as important an ontology engineering exercise as the
creation of the ontology itself.

Once we have an approximation, we will use FunOwl in combination with the source ontologies and other material to produce 
first approximations of complete proxy value set spaces.  

We will then use these approximations, the original ontology and sample data records in RDF to test the relative performance of
the reasoning process.  For our first cut at this we intend to use very coarse measurements, starting with the amount of time
it takes to (incrementally) classify the ontology itself, the ontology + the proxy individuals and, finally, the ontology + the
proxy individuals + sample data records.

We will then summarize our findings in the form of a poster and, if time permits, a paper.


## Definitions
* __composite concept__ -
* __ontology__ -
* __postcoordination__ - establishing a composite class in a data record.  
* __precoordination__ - defining a single "composite class" in a an ontology.  As an example, the SNOMED CT ontology defines
[Chronic osteomyelitis of left tibia (disorder)](http://snomed.info/id/1077591000119101) -- a single class that incorporates the
  components:
  * morphology - inflammation
  * finding site - tibia
  * pathological process - infectious process
    (We'll fill this out together)
