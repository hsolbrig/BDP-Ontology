# Proposal

We propose to separate what has been called the "Information Model" into two distinct components:

1) The _Logical Bindings_ -- a set of assertions about individuals stated in the terms of an underlying Ontology
2) The _Data Model_ -- a grammar that specifies set of rules about what must, may and cannot be represented in a model
instance along with the rules that define how information is translated between the _Logical Bindings_ and the _Data Model_.
   These rules define how specific strings and quantities should be represented as well as how individual / individual
   relationships should appear.
   
## Heading
### Individuals (Continuants)
The individuals that appear in the _Logical Bindings_ can be divided into the following types:

#### Distinguished Individuals
Distinguished Individuals are individuals that have unique well established names.  Examples include:
* Planets, continents, nations, states, cities 
* Differentiated roles such as "the president of the United States", "the capital of the state of Idaho"

Whether a given individual is "distinguished" or simply independent depends on the UOD.  As an example, the state of
Montana should (although it currently doesn't) appear as an individual in SNOMED CT, as they have chosen to enumerate
this sort of thing.

#### Independent Continuant Individuals
Individuals whose existence does not inhere in another individual.  Individual people, things, body parts,
etc. fall into this category.  This is one of the categories that is of greatest interest in our proposals.  Some
of the members in this category will be assigned a unique identifier.  Examples include people, patients,
specimens, physicians, etc.  A large chunk of these individuals, however, will not (ref: Ceusters for an alternative).

Examples in this category include anatomical parts, etc.

The focus of this proposal is on this broad category of things.


#### Dependent individuals
The color of someone's hair.  

### Processes (Occurrents)


## Approach
In order to understand what we are doing, let us start with simple clinical assertion:

On September 22, 2020, Joe Smith was diagnosed by Dr. Samantha Hawkly as having appendicitis.

We have the following named individuals:
* Joe Smith -- we'll identify him as :Joe
* Dr. Samantha Hawkly -- :DrH

The anonymous individuals that we have to address include:
* Joe's appendix
* The state of Joe's appendix at this point in time (ostensibly inflamed)
* Dr. Hawkly's diagnosis

One approach 
