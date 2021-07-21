
# Class: Patient


A person undergoing diagnosis or care

URI: [dbdx:Patient](https://ontologies-r.us/diabetes/Patient)


[![img](images/Patient.svg)](images/Patient.svg)

## Parents

 *  is_a: [Person](Person.md) - A placeholder for a person identifier

## Referenced by class

 *  **None** *[➞patients](dataBase__patients.md)*  <sub>0..\*</sub>  **[Patient](Patient.md)**
 *  **None** *[➞patient](diagnosisRecord__patient.md)*  <sub>1..1</sub>  **[Patient](Patient.md)**

## Attributes


### Inherited from Person:

 * [➞id](person__id.md)  <sub>1..1</sub>
     * Description: An identifier assigned to the patient by this particular model.
     * Range: [String](types/String.md)
 * [➞name](person__name.md)  <sub>1..1</sub>
     * Description: A person's name
     * Range: [String](types/String.md)
