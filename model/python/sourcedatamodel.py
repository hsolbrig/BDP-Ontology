# Auto generated from SourceDataModel.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-07-19 16:08
# Schema: diabetes
#
# id: https://ontologies-r.us/diabetes
# description: Data structures to represent the model from Dr. Alan Rector's Terminology Binding paper
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
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
from linkml_runtime.linkml_model.types import Datetime, String
from linkml_runtime.utils.metamodelcore import XSDDateTime

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
DBDX = CurieNamespace('dbdx', 'https://ontologies-r.us/diabetes/')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCT = CurieNamespace('sct', 'http://snomed.info/id/')
SCTI = CurieNamespace('scti', 'http://ontologies-r.us/individuals/sct/')
DEFAULT_ = DBDX


# Types

# Class references
class PersonId(extended_str):
    pass


class PatientId(PersonId):
    pass


class ClinicianId(PersonId):
    pass


class DiagnosisRecordRecordid(extended_str):
    pass


class DiabeticDataStructure1Recordid(DiagnosisRecordRecordid):
    pass


class DiabeticDataStructure2Recordid(DiagnosisRecordRecordid):
    pass


@dataclass
class Person(YAMLRoot):
    """
    A placeholder for a person identifier
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBDX.Person
    class_class_curie: ClassVar[str] = "dbdx:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = DBDX.Person

    id: Union[str, PersonId] = None
    name: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class Patient(Person):
    """
    A person undergoing diagnosis or care
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBDX.Patient
    class_class_curie: ClassVar[str] = "dbdx:Patient"
    class_name: ClassVar[str] = "Patient"
    class_model_uri: ClassVar[URIRef] = DBDX.Patient

    id: Union[str, PatientId] = None
    name: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PatientId):
            self.id = PatientId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Clinician(Person):
    """
    A person providing care
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBDX.Clinician
    class_class_curie: ClassVar[str] = "dbdx:Clinician"
    class_name: ClassVar[str] = "Clinician"
    class_model_uri: ClassVar[URIRef] = DBDX.Clinician

    id: Union[str, ClinicianId] = None
    name: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ClinicianId):
            self.id = ClinicianId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class DiagnosisRecord(YAMLRoot):
    """
    A simplified diagnosis record
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBDX.DiagnosisRecord
    class_class_curie: ClassVar[str] = "dbdx:DiagnosisRecord"
    class_name: ClassVar[str] = "DiagnosisRecord"
    class_model_uri: ClassVar[URIRef] = DBDX.DiagnosisRecord

    recordid: Union[str, DiagnosisRecordRecordid] = None
    patient: Union[str, PatientId] = None
    source: Union[str, ClinicianId] = None
    date: Union[str, XSDDateTime] = None
    topic: Union[str, "DiagnosisTopics"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.recordid):
            self.MissingRequiredField("recordid")
        if not isinstance(self.recordid, DiagnosisRecordRecordid):
            self.recordid = DiagnosisRecordRecordid(self.recordid)

        if self._is_empty(self.patient):
            self.MissingRequiredField("patient")
        if not isinstance(self.patient, PatientId):
            self.patient = PatientId(self.patient)

        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, ClinicianId):
            self.source = ClinicianId(self.source)

        if self._is_empty(self.date):
            self.MissingRequiredField("date")
        if not isinstance(self.date, XSDDateTime):
            self.date = XSDDateTime(self.date)

        if self._is_empty(self.topic):
            self.MissingRequiredField("topic")
        if not isinstance(self.topic, DiagnosisTopics):
            self.topic = DiagnosisTopics(self.topic)

        super().__post_init__(**kwargs)


@dataclass
class DiabeticDataStructure1(DiagnosisRecord):
    """
    A model of a post-coordinated diabetes data structure
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBDX.DiabeticDataStructure1
    class_class_curie: ClassVar[str] = "dbdx:DiabeticDataStructure1"
    class_name: ClassVar[str] = "DiabeticDataStructure1"
    class_model_uri: ClassVar[URIRef] = DBDX.DiabeticDataStructure1

    recordid: Union[str, DiabeticDataStructure1Recordid] = None
    patient: Union[str, PatientId] = None
    source: Union[str, ClinicianId] = None
    date: Union[str, XSDDateTime] = None
    brittleness: Union[str, "DiabeticBrittleness"] = None
    topic: Union[str, "DiabetesDiagnosisTopics"] = None
    diagnosis: Optional[Union[str, "DiabetesDiagnosisTopics"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.recordid):
            self.MissingRequiredField("recordid")
        if not isinstance(self.recordid, DiabeticDataStructure1Recordid):
            self.recordid = DiabeticDataStructure1Recordid(self.recordid)

        if self._is_empty(self.brittleness):
            self.MissingRequiredField("brittleness")
        if not isinstance(self.brittleness, DiabeticBrittleness):
            self.brittleness = DiabeticBrittleness(self.brittleness)

        if self._is_empty(self.topic):
            self.MissingRequiredField("topic")
        if not isinstance(self.topic, DiabetesDiagnosisTopics):
            self.topic = DiabetesDiagnosisTopics(self.topic)

        if self.diagnosis is not None and not isinstance(self.diagnosis, DiabetesDiagnosisTopics):
            self.diagnosis = DiabetesDiagnosisTopics(self.diagnosis)

        super().__post_init__(**kwargs)


@dataclass
class DiabeticDataStructure2(DiagnosisRecord):
    """
    A model of a pre-coordinated diabetes data structure
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBDX.DiabeticDataStructure2
    class_class_curie: ClassVar[str] = "dbdx:DiabeticDataStructure2"
    class_name: ClassVar[str] = "DiabeticDataStructure2"
    class_model_uri: ClassVar[URIRef] = DBDX.DiabeticDataStructure2

    recordid: Union[str, DiabeticDataStructure2Recordid] = None
    patient: Union[str, PatientId] = None
    source: Union[str, ClinicianId] = None
    date: Union[str, XSDDateTime] = None
    topic: Union[str, "DiagnosisTopics"] = None
    diagnosis: Union[str, "PrecoordinatedDiagnoses"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.recordid):
            self.MissingRequiredField("recordid")
        if not isinstance(self.recordid, DiabeticDataStructure2Recordid):
            self.recordid = DiabeticDataStructure2Recordid(self.recordid)

        if self._is_empty(self.diagnosis):
            self.MissingRequiredField("diagnosis")
        if not isinstance(self.diagnosis, PrecoordinatedDiagnoses):
            self.diagnosis = PrecoordinatedDiagnoses(self.diagnosis)

        super().__post_init__(**kwargs)


@dataclass
class DataBase(YAMLRoot):
    """
    A collection of Patients / Clinicians and both forms of DiabeticDataStructures
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DBDX.DataBase
    class_class_curie: ClassVar[str] = "dbdx:DataBase"
    class_name: ClassVar[str] = "DataBase"
    class_model_uri: ClassVar[URIRef] = DBDX.DataBase

    patients: Optional[Union[Dict[Union[str, PatientId], Union[dict, Patient]], List[Union[dict, Patient]]]] = empty_dict()
    clinicians: Optional[Union[Dict[Union[str, ClinicianId], Union[dict, Clinician]], List[Union[dict, Clinician]]]] = empty_dict()
    post_coord_dxs: Optional[Union[Dict[Union[str, DiabeticDataStructure1Recordid], Union[dict, DiabeticDataStructure1]], List[Union[dict, DiabeticDataStructure1]]]] = empty_dict()
    pre_coord_dxs: Optional[Union[Dict[Union[str, DiabeticDataStructure2Recordid], Union[dict, DiabeticDataStructure2]], List[Union[dict, DiabeticDataStructure2]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="patients", slot_type=Patient, key_name="id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="clinicians", slot_type=Clinician, key_name="id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="post_coord_dxs", slot_type=DiabeticDataStructure1, key_name="recordid", keyed=True)

        self._normalize_inlined_as_dict(slot_name="pre_coord_dxs", slot_type=DiabeticDataStructure2, key_name="recordid", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations
class DiagnosisTopics(EnumDefinitionImpl):
    """
    Any topic of a diagnosis record
    """
    _defn = EnumDefinition(
        name="DiagnosisTopics",
        description="Any topic of a diagnosis record",
        code_set=DBDX.sct_dx_codes,
        pv_formula=PvFormulaOptions.CODE,
    )

class DiabetesTopic(EnumDefinitionImpl):
    """
    Valid topic of codes for diabetes
    """
    _defn = EnumDefinition(
        name="DiabetesTopic",
        description="Valid topic of codes for diabetes",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "73211009",
                PermissibleValue(text="73211009",
                                 description="Diabetes mellitus (disorder)",
                                 meaning=SCTI["73211009"]) )

class DiabetesDiagnosisTopics(EnumDefinitionImpl):
    """
    Specific diabetes codes
    """
    _defn = EnumDefinition(
        name="DiabetesDiagnosisTopics",
        description="Specific diabetes codes",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "46635009",
                PermissibleValue(text="46635009",
                                 description="Diabetes mellitus type 1 (disorder)",
                                 meaning=SCTI["46635009"]) )
        setattr(cls, "44054006",
                PermissibleValue(text="44054006",
                                 description="Diabetes mellitus type 2 (disorder)",
                                 meaning=SCTI["44054006"]) )

class DiabeticBrittleness(EnumDefinitionImpl):
    """
    A diabetic brittleness assessment
    """
    _defn = EnumDefinition(
        name="DiabeticBrittleness",
        description="A diabetic brittleness assessment",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "True",
                PermissibleValue(text="True",
                                 description="Brittle diabetes mellitus (finding)",
                                 meaning=SCTI["11530004"]) )
        setattr(cls, "False",
                PermissibleValue(text="False",
                                 description="Diabetic - good control (finding)",
                                 meaning=SCTI["170763003"]) )

class PrecoordinatedDiagnoses(EnumDefinitionImpl):
    """
    A complete code that represents the type and brittless state of diabetes as one element
    """
    brittle_dm_1 = PermissibleValue(text="brittle_dm_1",
                                               description="Brittle diabetes mellitus type 1",
                                               meaning=SCTI["290002008"])
    brittle_dm_2 = PermissibleValue(text="brittle_dm_2",
                                               description="Brittle diabetes mellitus type 2",
                                               meaning=SCTI["445353002"])
    controlled_dm_1 = PermissibleValue(text="controlled_dm_1",
                                                     description="Well Controlled diabetes mellitus type 1",
                                                     meaning=SCTI["444074000"])
    controlled_dm_2 = PermissibleValue(text="controlled_dm_2",
                                                     description="Well controlled diabetes mellitus type 2",
                                                     meaning=SCTI["444110003"])
    dm_1 = PermissibleValue(text="dm_1",
                               description="Diabetes mellitus type 1 - controlled state unknown",
                               meaning=DBDX.dm1_unk)
    dm_2 = PermissibleValue(text="dm_2",
                               description="Diabetes mellitus type 2 - controlled state unknown",
                               meaning=DBDX.dm2_unk)

    _defn = EnumDefinition(
        name="PrecoordinatedDiagnoses",
        description="A complete code that represents the type and brittless state of diabetes as one element",
    )

# Slots

