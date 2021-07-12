# Existential Elimination and OWL


## [Using Z: Specification, Refinement and Proof](http://www.usingz.com/usingz.pdf)

### Section 3.5 Existential introduction and elimination
> The predicate \[p=] `∃ x : a \dot x` states that there is some object `x` in `a` for which `s` is true.  If `x` appears free
> in `p` then simply removing the quantifier leaves us with the unjustified statement about a free variable `x`.  We cannot, in general, conclude `p`
> from `\exists x : a \dot p`.  To use the information contained in `p`, we must complete any reasoning that involves x before eliminating the
> quantifier.  
> Suppose that we assume only `x \in a` and that `p` holds of `x`.  We are then able to drive a predicate `r` that does not involve `x` and we know that
> there is some `x` in `a` for which `p` is true, then we may safely conclude `r`.

## Forall x: Calgary - An Introduction to Formal Logic
See section __[34.5 Existential Elimination](https://forallx.openlogicproject.org/forallxyyc.pdf#chapter.34)__

The general notion behind existential elimination is, given the assertion there exists at least one `x` in a particular set, `a` and the assertion that at
least one member of that set satisfies predicate `p` we are able to introduce a _free variable_ (say, `w`) that represents one of the members in the set that
satisfies `p`.  As an example, if we make the assertion "If a person has appendicitis then there is at least part of that person's body that a) is inflamed and
b) is located in that person's appendix."  (`∀ p: Person | Appendicitis(p) --> ∃ x, y:AnatomicalPart | Inflamed(x) ∧ LocatedIn(x, y) ∧ Appendix(y) ∧ PartOf(y, p)`).  

Suppose we have the following assertion in the form of an information model:
```json
{
   "patient": "Harold Solbrig",
   "diagnosis": "Appendicitis
}
```

Using LinkML, JSON-LD and/or other appropriate tools we are able to infer the following:
```
:HaroldSolbrig rdf:type Patient .
:HaroldSolbrig foaf:name "Harold Solbrig" .
:HaroldSolbrig o:hasDx o:Appendicitis .
```
Where the prefix `o:` represents the appropriate ontology.

Formally, this assertion is something of the form: `Harold Solbrig ∈ Patient ∧ Appendicitis(Harold Solbrig)`,

If our ontology asserts the following
```
Declaration(ObjectProperty(o:morphology))
Declaration(ObjectProperty(o:locatedIn))
```


we can conclude `∃ x, y:AnatomicalPart | Inflamed(x) ∧ LocatedIn(x, y) ∧ Appendix(y) ∧ PartOf(y, Harold Solbrig)`

This much is what reasoners do for us "out of the box".  Our problem, however, is that we are still left with only two triples:
```
:HaroldSolbrig rdf:type o:Person .
:HaroldSolbrig o:hasDiagnosis o:Appendicitis .
```
In order to fully understand what the _combination_ of the data and the ontology says, we need follow through with existential elimination:

Let `a` represent the anatomical part that is inflamed and `b` represent Harold Solbrig's appendix.  We get:

`AnatomicalPart(a) ∧ AnatomicalPart(b) ^ Inflamed(a) ^ LocatedIn(a, b) ^ Appendix(b) ^ PartOf(b, Harold Solbrig)`

This gives us the following triples in addition to original two:
```
_:a rdf:type o:AnatomicalPart .
_:a o:morphology o:Inflammation .
_:a o:locatedIn _:b .
_:b rdf:type o:AnatomicalPart .
_:b rdf:type o:Appendix .
_:b o:partOf :HaroldSolbrig .
```
