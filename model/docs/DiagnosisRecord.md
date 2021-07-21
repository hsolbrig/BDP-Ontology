
# Class: DiagnosisRecord


A simplified diagnosis record

URI: [dbdx:DiagnosisRecord](https://ontologies-r.us/diabetes/DiagnosisRecord)


[![img](images/DiagnosisRecord.svg)](images/DiagnosisRecord.svg)

## Children

 * [DiabeticDataStructure1](DiabeticDataStructure1.md) - A model of a post-coordinated diabetes data structure
 * [DiabeticDataStructure2](DiabeticDataStructure2.md) - A model of a pre-coordinated diabetes data structure

## Referenced by class


## Attributes


### Own

 * [➞recordid](diagnosisRecord__recordid.md)  <sub>1..1</sub>
     * Description: The id of a formal diagnostic event
     * Range: [String](types/String.md)
 * [➞patient](diagnosisRecord__patient.md)  <sub>1..1</sub>
     * Description: The patient to whom the diagnosis applies
     * Range: [Patient](Patient.md)
 * [➞source](diagnosisRecord__source.md)  <sub>1..1</sub>
     * Description: The clinician who asserted the diagnosis
     * Range: [Clinician](Clinician.md)
 * [➞date](diagnosisRecord__date.md)  <sub>1..1</sub>
     * Description: The date and time that the assertion was made
     * Range: [Datetime](types/Datetime.md)
 * [➞topic](diagnosisRecord__topic.md)  <sub>1..1</sub>
     * Description: The topic of the diagnostic record
     * Range: [DiagnosisTopics](DiagnosisTopics.md)
