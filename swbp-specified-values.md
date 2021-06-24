# Notes on [https://www.w3.org/TR/swbp-specified-values/]()

This is an early paper that eventually led to the publication of the
more extensive and complete [Whats in a code](https://www.cs.man.ac.uk/~rector/papers/Whats-in-a-code/Whats-in-a-code-rector-corrected.pdf).

It defines a rather helpful graphic notation (Q: did anyone ever implement this as a protege plugin?)

It makes a couple of assertions that we will want to explore and test:
1. "The representation is in OWL-DL, and DL reasoners should eventually be expected to make correct inferences with individuals used in this way. However, neither FaCT nor Racer (the two most widespread open source reasoners in use today) perform all the expected inferences reliably."
2. "There is no way to represent alternative partitionings of the same feature space. Because individuals cannot overlap, if Health_Value is defined as equivalent to enumeration of one list of distinct values, it cannot also be equivalent to a different list of distinct values. To do so would cause the reasoner to indicate a contradiction. (i.e that Health_Value was "unsatisfiable".)"

We should upload the links on the page (see note on funowl below, however) and see which reasoners are able to deal with individuals today.

We should also a) demonstrate that 2 is indeed true and (assuming it is), do the maths to show why, because I have a hunch that it will matter in our upcoming work.

On Pattern 2, the authors assert that `:has_health_status` must be functional.  Why is this?  Do we need to add functional and other assertions to the properties in our reference ontologies to make our approach work?
See: [OWL 2 Object Property Axioms](https://www.w3.org/TR/2012/REC-owl2-direct-semantics-20121211/#Object_Property_Expression_Axioms) for details

Important quote that we will need to toy with as to whether and why it holds:

"... a convention for creating anonymous instances in the database is required. (Logicians call such anonymous instances "skolem constants".) In practice, this can usually be ignored."

In particular, our approach is to, instead, use "proxy" (we need to come up with the appropriate phrase) individuals.  One of the things that we will need to address in the next steps/discussion
of the paper is what ramifications and limits come from a "token" individual -- if John's _left arm_ is broken and Sally's _left arm_ is broken, what are the implications if we represent this fact
using exactly __ONE__ individual to represent both John and Sally's left arm.  If, in fact, if the predicate that connected John to his Left Arm _was_ functional, it seems like we would be
unintentionally asserting that John and Sally are the same person.
