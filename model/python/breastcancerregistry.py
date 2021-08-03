# Auto generated from BreastCancerRegistry.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-08-02 15:53
# Schema: bcr
#
# id: http://example.org/bdpontology/bcr
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_model.types import Date, Integer, String
from linkml_runtime.utils.metamodelcore import XSDDate

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BCR = CurieNamespace('bcr', 'https://example.org/bdpontology/bcr/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SIO = CurieNamespace('sio', 'http://semanticscience.org/resource/SIO_')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = BCR


# Types

# Class references
class PersonId(extended_str):
    pass


@dataclass
class Person(YAMLRoot):
    """
    An entry in the repository person/patient table
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BCR.Person
    class_class_curie: ClassVar[str] = "bcr:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = BCR.Person

    id: Union[str, PersonId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            raise ValueError("id must be supplied")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Entry(YAMLRoot):
    """
    An entry in a breast cancer registry
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BCR.Entry
    class_class_curie: ClassVar[str] = "bcr:Entry"
    class_name: ClassVar[str] = "Entry"
    class_model_uri: ClassVar[URIRef] = BCR.Entry

    id: Optional[Union[str, PersonId]] = None
    entryDate: Optional[Union[str, XSDDate]] = None
    age: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self.entryDate is not None and not isinstance(self.entryDate, XSDDate):
            self.entryDate = XSDDate(self.entryDate)

        if self.age is not None and not isinstance(self.age, int):
            self.age = int(self.age)

        super().__post_init__(**kwargs)


# Enumerations


# Slots

