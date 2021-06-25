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








