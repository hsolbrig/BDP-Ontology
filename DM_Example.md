# Working through the Diabetes example from [Rector's binding paper](https://www.cs.man.ac.uk/~rector/papers/Terminology-binding-final-revision-embedded-single-rector%20copy.pdf)

We begin by observing that this paper only indirectly references the key semantics document - the [Model of Meaning](data/ModelOfMeaning.owl).

While the [Model of Codes](data/ModelOfCodes.owl) is derived from the model of meaning, there are no direct links.  In this document we propose
an alternative approach:
1) Define a source and a target information model using data modeling tool.  For our purposes, we will use LinkML.
2) Define the _semantics_ of the source and target information model in OWL.  In this context, "semantics" is used to define what is being
_asserted_ by information model statements.
3) Use the definitions in step 2 to determine what additional information can be inferred from the semantics of record
that is "acceptable" or "consistent" with the source information model.
4) Use this additional information to determine what could be asserted in the "semantics" of the target information model.



## Define a source and target information model




## Example from Rectors binding Paper

### Step 1: convert a data record to an RDF statement
Joe Johnson, Patient 12345 is diagnosed w/ [Brittle Type 1 Diabetes](http://snomed.info/id/290002008) as defined in
SNOMED-CT
```json
{
  "patient_id": "A12345",
  "name": "Joe Johnson",
  "dx": "sct:290002008"
}
```
JSON-LD Context
```json
{
  "@context": {
    "sct": "http://snomed.info/id/",
    "o": "http://ontologies-r.us/bdp/diabetes#",
    "@base": "http://example.org/bdp#",
    "patient_id": "@id",
    "name": "o:name",
    "dx": {
      "@type": "@id",
      "@id": "o:hasDiagnosis"
    }
  }
}
```
The context above makes the following assertions:
1) [CURIEs](https://www.w3.org/TR/curie/) that begin with "sct:" map to
SNOMED-CT
2) Curies that begin with "o:" map to our toy diabetes ontology
3) Identifiers that aren't full URI's or CURIES are assumed to be in "http://example.org/#bdp"
4) The JSON key, "patient_id" is the subject of this set of triples
5) The JSON key, "name", maps to "name" as defined in our ontology
6) The JSON key, "dx", maps to "hasDiagnosis in our ontology" and the
value of the DX is a URI (@id)
   
When we apply the above context (see: https://tinyurl.com/hj8e66ww)
We get the following RDF:
```text
<http://example.org/A12345> <http://ontologies-r.us/bdp/diabetes#hasDiagnosis> <http://snomed.info/id/290002008> .
<http://example.org/A12345> <http://ontologies-r.us/bdp/diabetes#name> "Joe Johnson" .
```

### Step 2: Transform the output RDF statements into an OWL "Ontology"
(Borrowing from http://hl7.org/fhir/allergyintolerance-example.ttl.html:)


```text
@prefix : <http://example.org/bdp#> .
@prefix o: <http://ontologies-r.us/bdp/diabetes#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix sct: <http://snomed.info/id/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://example.org/A12345> <http://ontologies-r.us/bdp/diabetes#hasDiagnosis> <http://snomed.info/id/290002008> .
<http://example.org/A12345> <http://ontologies-r.us/bdp/diabetes#name> "Joe Johnson" .

<http://example.org/o> a owl:Ontology .
```
