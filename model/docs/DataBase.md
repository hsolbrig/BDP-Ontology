
# Class: DataBase


A collection of Patients / Clinicians and both forms of DiabeticDataStructures

URI: [dbdx:DataBase](https://ontologies-r.us/diabetes/DataBase)


[![img](images/DataBase.svg)](images/DataBase.svg)

## Attributes


### Own

 * [➞patients](dataBase__patients.md)  <sub>0..\*</sub>
     * Description: Reference Patients
     * Range: [Patient](Patient.md)
 * [➞clinicians](dataBase__clinicians.md)  <sub>0..\*</sub>
     * Description: Reference Clinicians
     * Range: [Clinician](Clinician.md)
 * [➞post_coord_dxs](dataBase__post_coord_dxs.md)  <sub>0..\*</sub>
     * Description: Post coordinated diagnoses
     * Range: [DiabeticDataStructure1](DiabeticDataStructure1.md)
 * [➞pre_coord_dxs](dataBase__pre_coord_dxs.md)  <sub>0..\*</sub>
     * Description: Pre coordinated diagnoses
     * Range: [DiabeticDataStructure2](DiabeticDataStructure2.md)
