
# diabetes schema


Data structures to represent the model from Dr. Alan Rector's Terminology Binding paper


### Classes

 * [DataBase](DataBase.md) - A collection of Patients / Clinicians and both forms of DiabeticDataStructures
 * [DiagnosisRecord](DiagnosisRecord.md) - A simplified diagnosis record
     * [DiabeticDataStructure1](DiabeticDataStructure1.md) - A model of a post-coordinated diabetes data structure
     * [DiabeticDataStructure2](DiabeticDataStructure2.md) - A model of a pre-coordinated diabetes data structure
 * [Person](Person.md) - A placeholder for a person identifier
     * [Clinician](Clinician.md) - A person providing care
     * [Patient](Patient.md) - A person undergoing diagnosis or care

### Mixins


### Slots

 * [➞clinicians](dataBase__clinicians.md) - Reference Clinicians
 * [➞patients](dataBase__patients.md) - Reference Patients
 * [➞post_coord_dxs](dataBase__post_coord_dxs.md) - Post coordinated diagnoses
 * [➞pre_coord_dxs](dataBase__pre_coord_dxs.md) - Pre coordinated diagnoses
 * [➞brittleness](diabeticDataStructure1__brittleness.md) - How well managed the diabetes is
 * [➞diagnosis](diabeticDataStructure1__diagnosis.md) - The code for diabetes or any kind of diabetes
 * [➞diagnosis](diabeticDataStructure2__diagnosis.md) - The code for diabetes or any kind of diabetes
 * [➞date](diagnosisRecord__date.md) - The date and time that the assertion was made
 * [➞patient](diagnosisRecord__patient.md) - The patient to whom the diagnosis applies
 * [➞recordid](diagnosisRecord__recordid.md) - The id of a formal diagnostic event
 * [➞source](diagnosisRecord__source.md) - The clinician who asserted the diagnosis
 * [➞topic](diagnosisRecord__topic.md) - The topic of the diagnostic record
     * [DiabeticDataStructure1➞topic](DiabeticDataStructure1_topic.md) - Exact code for diabetes mellitus
 * [➞id](person__id.md) - An identifier assigned to the patient by this particular model.
 * [➞name](person__name.md) - A person's name

### Enums

 * [DiabetesDiagnosisTopics](DiabetesDiagnosisTopics.md) - Specific diabetes codes
 * [DiabetesTopic](DiabetesTopic.md) - Valid topic of codes for diabetes
 * [DiabeticBrittleness](DiabeticBrittleness.md) - A diabetic brittleness assessment
 * [DiagnosisTopics](DiagnosisTopics.md) - Any topic of a diagnosis record
 * [PrecoordinatedDiagnoses](PrecoordinatedDiagnoses.md) - A complete code that represents the type and brittless state of diabetes as one element

### Subsets


### Types


#### Built in

 * **Bool**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
