# Embedding logic symbols in Markdown
From: https://stackoverflow.com/questions/11256433/how-to-show-math-equations-in-general-githubs-markdownnot-githubs-blog#47798853

We get to: https://www.w3schools.com/html/html_symbols.asp

Some of the logic symbols we will need:

* Existential quantifier:  &exist; : `&exist;`
* Universal quantifier: &forall; : `&forall;`
* Member of: &isin; : `&isin;`
* Not member of: &notin; : `&notin;`
* Contains: &ni; : `&ni;`
* Left Arrow: &larr; : `&larr;`
* Right Arrow: &rarr; : `&rarr;`
* Double Arrow: &harr; : `&harr;`
* Greek Mu: &mu; : `&mu;`
* Dot: &sdot; : `&sdot;`  (find something better)
* And: &and; :`&and;`
* Or: &or; : `&or;`

There are also unnamed symbols that can be drawn from (fill in symbol ref)
* &#x2660; : `&#x2660;`

---
ObjectSomeValueFrom(is_caused_by, Damage)
Diabetes is a member of the set {w is_caused_by(w, Damage) is True} 


joe's diabetes is_caused_by some 
    (Damage
     and (has_locus some Pancreatic_islet_cells))

&exist; x | x &isin; Damage &and; (&exist; y: Pancreatic_islet_cells | has_locus(x, y)) &and; caused_by(x, y)

has_locus(x, y) 
lives_in(x, y)

lives_in(Rochester, Harold) --> True
lives_in(Rochester, Renee) --> False

lives_in = {(Rochester, Harold), (Baltimore, Renee), (Baltimore, Karl), ...}

lives_in(Rochester, Harold) --> True
(Rochester, Harold) &isin; lives_in

has_locus ::= {(dm, pancreatic_cell), (heart_disease, heart), (kidney_disease, kidney)}

	{ x | ∃ y : ( x, y ) ∈ is_caused_by}
is_caused_by == { x | ∃ y: is_caused_by(x, y)  and Y member of Damage}
Let W be one of the y's such that is_caused_by(Joe's Diabetes, y) and y is a member of Damage.
Joe's_Diabetes is_caused_by W
