# [Description Logics for Databases](https://www.inf.unibz.it/~franconi/dl/course/dlhb/dlhb-16.pdf)
Notes on chapter 16 in the Description Logic Handbook.  Chapter by Borgida, Lenzerina and Rosati.


## 16.1 Introduction
Databases _also_maintain models of a UoD.  
> The main difference between databases and knowledge bases is that while the  former concentrate on manipulating
> _large and perisistent_ models of relatively simpole data, the latter provide more supprt for _inference_...

Need to take a peek at [Borgida, 1995]

Authors argue that ER models (which, we can extend these days to UML, FHIR and LinkML) "describe the UofD about which
the database will be knowledgable."  Calls them _semantic modeling languages_ .  While the OMG

_logical schema_ -- describes the structure, types, interconnections and constraints. 

Reference to the "so-called 'closed world assumption'" -- we may want to pursue this. My own take on this matter is that,
just _like_ knowledge bases, people understand when and where CWA applies.  It isn't a characteristic that is 
inherent in databases, but rather, when it does occur, is often not formally documented.  As an example, if we have
a database that allows 0..2 "parent" links from a person record to another person record, it is clearly NOT the intent
of the designers a Person record less than 2 links is intended to say that these people were cloned.  Maybe not a focus
for this particular paper, but suffice it that the semantics of a missing data does NOT typically fall into the CWA
situation.

"Databases do not allow the representation of disjunctive data" -- while this sounds plausible at first glance, there is 
nothing inherent in databases that prevent disjunctive interpretations.  If one's UofD includes disjunctions, this can 
(and frequently _is_) modeled in databases.  An example that immediately comes to mind is an old HL7 model of 
"prescriptions", where the target of a prescription can reference a regimin of medication, an assistive device 
(e.g. "crutches"), a behavior (climb stairs 3 times per day), etc.  

__As with much of this material, the authors are conflating the _representation_ of information with the interpretation
of said representations__ -- as an example, they assert "if there no information about an attribute, it is given 
the _null_ value". (p464) A data model describes the (potentially infinite) set of possible states of the data itself.
At a really basic level, it asserts the possible of "1"'s and "0"'s are to be treated as conformant to the rules of the
model.  This is wrapped in layers of abstraction that involves representations of character strings, numbers, tables,
links, etc. but, in the end, a data model does NOT include semantics.  Semantics derive from the _mapping_ from possible
bit combinations _to_ a model of interpretation. 

If one has determined that the meaning of a sequence of 8 bits in the
record is intended to represent the age of a person in years using (big endian) signed binary notation, one might assert
that the valid states for these 8 bits is (11111111, 00000001-01111111), where "11111111" indicates that the age is 
asserted to be UNKNOWN and the remaining configurations represent the nearest age in years rounded up.  

Page 468 (published book) asserts:
> The semantics of an ER schema can be given by specifying which database states are consistent with the information 
> structure represented by the schema"

This is more than a bit confusing, as 
> A database state is considered acceptable if it satisfies all integrity constraints that are part of the schema.


