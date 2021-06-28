# Notes on [Terminology Binding](https://www.cs.man.ac.uk/~rector/papers/Terminology-binding-final-revision-embedded-single-rector%20copy.pdf)

This contains an excellent introduction on the purpose of ontology and its relationship to information models.

This paper focuses on the use of _single_ data structures and their ability to faithfully record "accurate statements" about the world in
a way that does not compromise (change) the meaning of the intended statements when they are re-interpreted.  It is interesting to note that
the upper box (oval) in Figure 1 represents a combination of what we refer to as the "T-Box" (general statements about classes and categories)
and the "A-Box" (assertions about individuals).   The "T-Box" is where the shared community meaning is maintained.  One should also note that
the "T-Box" is the aspect of data and communication that is almost always underspecified.  In a clinical community, the statement "All diabetes are
metabolic diseases" is so obvious as to be considered insulting if anyone chooses to state it.  As information is disseminated over time, space and/or
culture, this sort of statement becomes essential to the understanding of the second statement about John.

* Time -- "diabetes" and "metabolic diseases" represent categories that reflect our best understanding of the nature of this particular type of
  disease as of today.  This may (and will) change over time, leading to statements in the future of the form "John had a disease that, in 2007,
  was called 'diabetes' which, at that point in time, was considered to be a type of 'metabolic disease' which, at that point in time included..."
* Space and culture -- the phrases "diabetes", "brittle", "metabolic" and even "disease" itself are specific to the anglo-european perspective of
  medicine.  It may be necessary to translate both the _language_ of the utterances and, as with the time dimension, add cultural references to
  aid in its interpretation by practitioners of Traditional Chinese Medicine etc.

One should also note an _extremely_ important transition that is only briefly touched upon in this document, that being how one gets from
a an instance of a "valid specification"[1] as shown in the square box to its corresponding interpretation, "John has diabetes & it is brittle".

We have proposed dividing this transformation into the following steps:
1. Transform the data structure instance into a directed graph, with the arcs represented by labels and the nodes by a combination of
   terminal values or nested graphs.  XML, JSON and YAML data structures are already in this form.  SQL requires some secondary processing
   as exemplified by the R2RML specification.
2. Map the arcs and nodes of the directed graph to RDF using the approach exemplified in JSON-LD.  Note that _this_ is the step that associates
   arcs with their corresponding meanings in terms of the T-Box (e.g. "diagnosis-code" --> URI for "hasDiagnosis" in the appropriate ontology[2].
   perhaps: [Associated finding](http://snomed.info/id/246090004)?  and the same things with the nodes [Diabetes mellitus type 1](http://snomed.info/id/46635009).

   This is a good time to note that separable statements in the data are going to require the same granularity in the ontology.  While SNOMED CT has codes
   for "Brittle type 1 and type 2 diabetes mellitus" as well as a generic qualifier, [Brittle course](http://snomed.info/id/255299009), the qualifier is not
   connected with the diabetes codes, meaning that the data record in our example has no useful mapping.  We can produce:
   ```
   ObjectPropertyAssertion( sct:246090004 :Joe  :JoesDX )
   ClassAssertion( sct:46635009 :JoesDx )
   ObjectPropertyAssertion( sct:263502005 :JoesDX sct:255299009 )
   ```
   The above example states that Joe "(has) Associated Finding" Joe's Diagnosis and Joe's Diagnosis is an instance of DM Type 1 which has a clinical course of Brittle.
   In order for things to work in the approach that we are describing we would need to:
   1) add a clinical course arc to Brittle DM Type 1 and...
   2) Figure out how to crosss the "role group" speed bump.[3]



As with the [swbp-specified-values paper](swbp-specified-values.md), however, it wanders off into a very
strange place where, instead of simply asserting that codes represent individuals (e.g.  John's type 2 diabetes diagnosis),
it instead starts positing the notion of an individual named "code_for_diabetes_type_2" and assertions that
the individual, "code_for_diabetes_type_2", is a "subcode_of" "code for diabetes".

## 2.2 Details and consequences for selecting codes
The assertion that the information model is about data structures and symbols is quite important.  Similar assertions can be
found in the ISO/IEC 11179-3 "four quadrant" model, where meaning occupies the upper half and syntax the lower.  One might also
look at the slightly dated but markedly prescient [ISO Technical Report 9007 - Information processing systems -- Concepts and
terminology for the conceptual schema and the information base](https://cdn.standards.iteh.ai/samples/16549/67afa4ce8dec4142b58aaf09a7fdd77b/ISO-TR-9007-1987.pdf)

The paper notes that "To say in the ontology that diabetes is a metabolic disorder is not to say simply that all the cases of diabetes happen to fall in the set of metabolic disorders in the way that we might say, for example, that all the red-haired boys in the school are taking geometry. "
This is another way of saying that diabetes is _necessarily_ a metabolic disorder, by definition.  Note, however, that these
assertions are always in a given context (UOD) and, the term "necessarily" doesn't mean that the world MUST be this way, but simply that
our rules say that we won't call it "diabetes" unless it is also something we've called a "metabolic disorder".  See OntoClean, as described in
[Guarino and Welty](https://en.wikipedia.org/wiki/OntoClean)

This section also continues to enforce a conceptual mistake made earlier.  While correctly asserting that "Codes and data structures do not “mean” anything on their own; they are merely valid or invalid. ...
However, if the two data structures are interpreted (See Fig 1) in terms of the meanings that they encode about the world –i.e. at the level of the ontology – then we can ask if they are logically equivalent – if they mean the same thing. ", the
document proceeds to act as if the "codes" embedded in data structures have inherent meaning, leading to the "code_for_.." names.

A key thing to realize is that how we _encode_ information in a data record is a matter of fiat.  Using the example in this paper,
one might have "valid" (i.e. conformant) records where one specifies that the character "1" represents DM type 1 and "2" DM type 2, and
that "brittle" is recorded as a "Y" or a "N".  Another record could say that the string "DM type 1" represents type 1 and a third might
combine the two fields leading to "I" for non-brittle DM 1, "II" for non-brittle 2, "Ib" for "brittle type 1", etc.  The choice is arbitrary.

As a matter of convenience, it is often useful to arrive at some sort of rule. If, for example, you are using SNOMED CT to define the intended
meaning, it might be convenient to use a formula.  As an example one might decide to use the SNOMED CT identifier for the referenced meaning
as the string in the field, thus "46635009" for DM Type 1, "44054006" for DM Type 2, "255299009" for brittle, etc.  Another rule might be to use
the official URI ("http://snomed.info/id/255299009 for "brittle"), a CURIE (SCT:255299009) or even some sort of compound structure, as exemplified by
the [FHIR Coding data structure](https://hl7.org/fhir/datatypes.html#Coding).

While there are obvious benefits to the rule based approach and, in fact, one would be hard pressed to come up with another approach that would work once the number
of possible choices exceeds a couple of dozen, it does have some serious drawbacks, including:
1) the codes for the intended meaning must be present in the ontology from which the codes come from.
2) the source ontology must be "well behaved" (cite Cimino's Desiderada).  It must not allow meanings to "drift", remove codes, or (shudder) assign completely new meanings to existing codes.
3) the use of actual codes effectively "locks" one into a selected ontology, raising hurdles if one needs to assign meanings in different contexts or migrate from one to another ontology
4) the use of codes make it easy to forget that all we are doing is specifying an _encoding_, and the referents of the codes are still in the ontology space

People have attempted to work around the first issue above by allowing ontology level grammar to be embedded in data records.  As an example, [Using SNOMED CT with FHIR](https://www.hl7.org/fhir/snomedct.html) states:
> "The following SNOMED CT artifacts are valid in the code element for the http://snomed.info/sct namespace: Concept IDs and SNOMED CT Expressions (using SNOMED CT Compositional Grammar ). SNOMED CT Terms and Description Identifiers are not valid as codes in FHIR, nor are other alternative identifiers associated with SNOMED CT Concepts. "

While this capability might allow very knowledgeable people to _enter_ data, at the moment we've got enough issues comparing, assembling and dissassembling data without dealing with this component.  In addition, compositional grammars such as that in SNOMED CT are used to define _categories_ (or _classes_), not
assertions about individuals. Later in this series of documents we make the argument that the intended meaning of "code" needs to be framed in the language of the "A-Box" (e.g. "Joe has a fracture that is located on _his_ left tibia", not "Joe belongs to the class of people who have fractures, at
least one of which is located on an instance of a tibia having laterality of left"),  allowing this sort of "T-Box" grammer into the data record only makes things worse.

Work-arounds for the second drawback take the form of attempts to include the state of the ontology at a given point of time as part of the code itself.  The "system" and "version" attributes of the [FHIR Coding datatype](https://hl7.org/fhir/datatypes.html#Coding) exemplify this problem.  
Because there _are_ (or at least _were_) classification systems that re-used codes (ICD-9 in particular), countless hours have been spent on how one might go about saying, to effect, "the definition of the ICD-9 code [250.01](http://www.icd9data.com/2015/Volume1/240-279/249-259/250/250.01.htm)
according to the 2015 edition of ICD-9-CM." while, at the same time, maintaining the ability to search for, compare, etc. _any_ instance of "250.01" no matter the year  -- the alternative having to have a large collection of codes ("250.01 2003 edition", "250.01 2004 edition", ...) to support
any comparison.

It should also be noted that (as noted in Cimino's Desiderata), meaning can also appear in the set of possible choices.  As an example, suppose that one were to define the possible codes for a field that represented, say, urine color by asserting that it is any code that whose corresponding
meaning is a subclass of the [Color](http://snomed.info/id/263714004) class in SNOMED CT. Today, this gives us 20 choices, including [Pink](http://snomed.info/id/371243003) and [Pale Pink](http://snomed.info/id/1004165009).  (TBD: Work on this example)

Work-arounds for the third issue are exemplified in the [FHIR CodeableConcept](https://hl7.org/fhir/datatypes.html#CodeableConcept) datatype, which allows for the possibility of:
> "The concept may be coded multiple times in different code systems (or even multiple times in the same code systems, where multiple forms are possible, such as with SNOMED CT)."

This solution attempts to address _both_ the third and fourth drawbacks described above. Once one forgets that, while algorithmic, there is still a needed step to associate a "code", be it "1", "A", "DM type I" or a complex monster like  
{"system": "http://snomed.info/sct", "version": "20210101", "code": "44054006", "display": "Diabetes Mellitus II"} with its intended meaning.  The fact that there may be an exact or even approximate match for the code "1" in more than one ontology does not
require a different code for each match.  One can say that "When '1' was entered in the diagnosis field, its intended meaning can be found in the 20210101 SNOMED CT as the concept with code 44054006, in the 2015 ICD-9-CM with code 250.11, in MONDO with curie ..., etc.
Furthermore, it makes little sense to record these mappings in each and every data record. Not only does this add to the bulk and complexity of the records themselves, but it violates the basic "DRY"  (Do not Repeate Yourself) principle.  The basic question arises about
what one would do if one record contained "44054006" in SNOMED and "250.11" in ICD-9 while a second had "4405406", "250.1**2**". Is this a systemic error? an accidental error?  Something else.

TBD: Discuss fourth issue separately.


## Section 5
### Section 5.1 Model of Meaning - the "Ontology"

Functional syntax for [Model of Meaning](data/ModelOfMeaning.owl)

One will note that the model of meaning is completely decoupled from both the  
model of codes and the information model. It would have been interesting to see what the authors would
have done with a slightly more inclusive model that included, say, the notion of a "Person" or "Patient".
Would they have accepted something in the form of `ClassAssertion( o:Person :Joe)`?  In an information model,
one would expect `:Joe` to have some sort of unique identifier, which, formally, we would use to create the
appropriate URI for Joe.  As an example, if the data record asserted: `"id": "p12345"` for Joe, we might
use this to assemple a URI of a form such as "http://memorial.hospital.org/patient/p12345" and refer to it
as `:p12345` instead of our placeholder, `:Joe`.

What I wouldn't expect the authors to do, however, is to create an infrastructure similar to what is described
in this paper to allow `ObjectPropertyAssertion( bdptc:sub_code_of bdptc:code_for_patient :p12345 )`.

Notes:
1. We need to make sure that the last assertion is as the authors intended.  This is kind of an
   interesting assertion -- that every instance of a `diabetic brittleness state` is also an instance
   of either `brittle` or `well_controlled`.  Why is this necesary?  Will it still be necessary in our
   new model?

### Section 5.2 The Model of codes - the coding system
Functional syntax for [Model of Codes](data/ModelOfCodes.owl)

An important thing to note about this entry is that, even though the codes represent _individuals_, there is no
`rdf:type` relationship between the individuals and the categories that they represent.  These are modeled as pure  
 information model artifacts -- instances of the class `Code`, and have NO tie to

_This_ is the section that we will be replacing with our proxy individuals.

Notes:
1. Need to double check the individual model -- is "VALUE" necessary here?  If so, how do we put it in.
2. There is a typo in figure 6a -- should be `is_subcode_of VALUE code_for_diabetic_brittleness`**_value**

### Section 5.3 The information model proper
Functional syntax for [InformationModel](data/InformationModel.owl)

"For purposes of illustration, we shall concentrate only on qualities and omit causation." -- is this just
convenience or does this actually sidestep a key point

Notes:
1. a functional property is used to assert that an individual can be associated with at most one instance
    of the property.   The maths for it say that, if (x, a) and (x, b) are in property P then a = b.  Note, btw,
    that this is considerably weaker than what one might expect in a DB -- you have to be really careful to declare,
    say, "code_for_brittle" and "code_for_not_brittle" as different individuals, otherwise things will still work.
    As a general question, is this really a good use for an ontology -- shouldn't ShEx supplant this?

2. We note that `Coded_Attribute` is not formally defined.  We will use the
    textual description to add it in.  Also, has_attr is missing. Also note that "Topic_attr, "Diagnosis_attr" are
    misnamed -- we changed Topic --> Topic_attr, etc.

### Section 5.4 Constraining the codes to placeholders
Functional syntax for in Figure 8 is added to [Model of Codes](data/ModelOfCodes.owl)

### Section 5.5 Code Binding Interface
Figure 9 is represented in the [Code Binding Interface](data/CodeBindingInterface.owl)

## Additional notes
To get to the heart of the matter, if you were putting together an information model that, say,
asserts relationships between different people, the following elements would make perfect sense:

```
ClassAssertion( o:Person :Peter)
ClassAssertion( o:Person :John)
DataPropertyAssertion( o:name :John "John")
DataPropertyAssertion( o:age :John "17"^^xsd:integer)
ObjectPropertyAssertion( o:parentOf :John :Peter)
```

When dealing with collections of individuals (e.g. John, Peter), there is no reason to introduce any notion of
"code_for_individual" -- all we need to do is to supply the identifier of an _actual_ individual into the slot. The
same thing holds for controlled vocabularies (as exemplified in the swbp paper example one).  Suppose that, in our
"universe of discourse", we wanted to know which US state, if any, an individual resided in.  This could be easily
realized using the example we encountered in SWBP pattern 1:
```
Declaration( Class (st:State) )
Declaration( Objectproperty (st:residence) )
ObjectPropertyRange ( st:residence st:State )
ClassAssertion( st:State o:Alabama )
ClassAssertion( st:State o:Alaska )
ClassAssertion( st:State o:Arizona )
ClassAssertion( st:State o:Wyoming )
DifferentIndividuals( st:Alabama st:Alaska st:Arizona st:Wyoming )
EquivalentClasses( st:State ObjectOneOf(st:Alabama st:Alaska st:Arizona st:Wyoming ) )
```


Furthermore, if our model included people and hobbies, the entries below could
represent the fact that "Peter's Favorite Hobby" is woodworking:
```
ClassAssertion( o:WoodWorking :PetersFavoriteHobby )
ObjectPropertyAssertion( o:hasHobby :PetersFavoriteHobby )
```

An important thing to note, however, is that we had to stretch a bit to
come up with a unique name for the instance of wordworking that is unique
to Peter.  This highlights one of the primary motivations for the concept of
"Anonymous Individuals".  While we _could_ come up with a unique name for
everything that occurred in our model, it would quickly become quite tedious if,
say, Peter had four different hobbies.  At some point we'd have to resort to
a formulaic approach such as ":PetersFirstHobby", or ":PetersGardeningHobby" --
names that exist solely for the purpose of differentiation.  In the end
we end up with something of the form:
```
ClassAssertion( o:WoodWorking _:a1 )
ObjectPropertyAssertion( o:hasHobby :Peter _:a1 )
ClassAssertion( o:Gardening _:a2 )
ObjectPropertyAssertion( o:hasHobby :Peter _:a2 )
ClassAssertion( o:Photography _:a3 )
ObjectPropertyAssertion( o:hasHobby :Peter _:a3 )
ClassAssertion( o:Embalming _:a4 )
ObjectPropertyAssertion( o:hasHobby :Peter _:a4 )
```

Where we use the ontology to state that, in our world (Unverse of Discourse):
1. Hobby and Material both represent sets of individuals
2. utilizes represents the set of relationships between something and instances of Materials
3. hasHobby represents the set of relationships between something and instances of Hobbies
4. Every instance of a Hobby utilizes at least one instance of a Material
5. Every instance of Woodworking (in our definition) is an instance of a hobby
6. Every instance of Wood is an instance of a Material
7. Every instance of woodworking utilizes at least one instance (piece) of wood
8. The woodworking hobby is (can be) called "Wood Working"
9. Every instance of something that has a hobby that is an instance of wood working is an instance of a WoodWorker

This pattern continues for every hobby we choose to define
```
Declaration( Class( o:Hobby ) )
Declaration( Class( o:Material ) )
Declaration( ObjectProperty( o:utilizes ) )
ObjectPropertyRange( o:utilizes o:Material )
Declaration( ObjectProperty( o:hasHobby) )
ObjectPropertyRange( o:hasHobby o:Hobby )
SubClassOf( o:Hobby ObjectSomeValuesFrom( o:utilizes o:Material) )
Declaration( Class( o:Hobbyist) )
EquivalentClasses( o:Hobbyist ObjectSomeValuesFrom( o:hasHobby ))

Declaration( Class( o:WoodWorking ) )
SubClassOf( o:WoodWorking o:Hobby )
Declaration( Class( o:Wood ) )
SubClassOf( o:Material o:Wood )
SubClassOf( o:WoodWorking ObjectSomeValuesFrom( o:utilizes o:Wood))
AnnotationPropertyAssertion( rdfs:label o:WoodWorking "Wood Working" )
Declaration( Class (o:WoodWorker ) )
SubClassOf( o:WoodWorker ObjectSomeValuesFrom (o:hasHobby o:WoodWorking) )
SubClassOf( o:Hobbyist ObjectSomeValuesFrom (o:hasHobby ) )

Declaration( Class( o:Gardening ) )
SubClassOf( o:Gardening o:Hobby)
    ...
```
The _combination_ of the ontology and the assertions:

```
ClassAssertion( o:WoodWorking _:a1 )
ObjectPropertyAssertion( o:hasHobby :John _:a1 )
```
Allow us to conclude, amongst other things, that:
1. Somewhere there is at least one piece of wood that is utilized by Peter's hobby
2. That John is an instance of a WoodWorker
3. That John is an instance of a Hobbyist

Now suppose that Sally has a hobby that we haven't defined in our ontology.  Perhaps
she has a strange fascination with watching squirrels fall off of utility poles, so
she strolls the neighborhood with a large tub of lard.  The following assertions
might be used to describe this:
```
ObjectPropertyAssertion( o:hasHobby :Sally :SallysWeirdHobby )
ObjectPropertyAssertion( o:utilizes :SallysWeirdHobby :SallysTubOLard )
```
Working in the _opposite_ direction as above, we can use these statements to conclude
1. Sally's weird hobby is an instance of a Hobby
2. Sally's tub o' lard is an instance of a Material
3. Sally is an instance of a Hobbyist

[1]: We prefer the word "conformant", meaning that it is syntactically correct.  "Validity" broaches areas in which we
have no interest such as whether the content of the structure is actually correct -- that John, in fact _does_ have diabetes, acceptable -- the
document contains all the information necessary to be considered a "valid" medical record, etc.

[2]: It is interesting to note that, while SNOMED CT uses a relatively small collection of predicates in the _definition_ of their model,
it isn't clear how these would be applied in the instance situation.   Looking, in particular, for the property that represents the notion of
"has diagnosis" or, perhaps more strongly "has disease" (the distinction being subtle but important...) one starts with descendants of
[Concept model attribute](http://snomed.info/id/410662002).  It may be that SNOMED CT simply lacks the sort of predicates that can be used
to associated patient instances with instances of diagnoses and the like

[3]: Add a whole section on Role Groups in SNOMED CT.  We may also want to map this same thing to MONDO?








[Section 5.4 Constraining the codes to placeholders]: #section-54-constraining-the-codes-to-placeholders

