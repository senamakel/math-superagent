# Claim: decidable first-order properties of k-automatic sequences (Goč–Henshall–Shallit)

```claim
id: ghs-automatic-decision-procedure
statement: Let x be a k-automatic sequence over a finite alphabet (n-th term a
finite-state function of the base-k representation of n). Any property of x
expressible using quantifiers, logical operations, integer variables, addition,
subtraction, indexing into x, and comparison of integers or of elements of x is
algorithmically decidable: one builds the automaton recognising the base-k
representations satisfying the predicate and checks emptiness/universality/cycle
reachability mechanically. Consequently (1) deciding whether two k-automatic
sequences are shifts of each other is decidable; (2) the sequence b(n) = n mod 2
derived from a k-automatic x, and more generally digit-induced transforms, are
automatic; (3) the Thue–Morse word t has an unbordered factor of length n iff the
base-2 representation of n is not of the form 1(01*0)*10*1 (open problem of
Currie and Saari, solved mechanically); (4) the Rudin–Shapiro sequence has an
unbordered factor of every length; (5) the paperfolding sequence's unbordered-
factor lengths are recognised by an explicit small automaton.
hypotheses: x k-automatic; the property is first-order over (N, +) with indexing
into x.
holds-here: false for the Fibonacci word S itself — it is Fibonacci-automatic
(Zeckendorf), not k-automatic, so this theorem does not apply directly (that is
exactly the gap the Fibonacci-specific decision algorithms of Mousavi–Schaeffer–
Shallit and the Ostrowski-numeration methods of Hieronymi et al. fill).
status: sourced
bearing: General anchor for the run's mechanical-proving/formalisation direction:
states what can be decided mechanically about automatic sequences, complements
the held Fibonacci-specific and Sturmian-specific decision papers, and grounds
the refutation that Zeckendorf-automatic digit-DP needs a Cobham-type base-
conversion theorem (the Fibonacci word is not k-automatic; 10 and phi are
multiplicatively independent — see cobham-bes-frougny-multiplicatively-
independent-conversion). Does not change the PE1006 solution route
(mechanical/floor-sum, not decision procedures).
anchor: research/sources/goc-henshall-shallit-automatic-theorem-proving.full.md
(arXiv:1203.3758; CIAA 2012, LNCS 7381, pp. 180-191; Thms 1-6)
```

## What the source says

**Goč, Henshall & Shallit, "Automatic Theorem-Proving in Combinatorics on Words"**
(`research/sources/goc-henshall-shallit-automatic-theorem-proving.full.md`,
https://arxiv.org/pdf/1203.3758). The founding paper of the Walnut-style
mechanical-proving school. Theorem 1 is the general decidability statement for
first-order properties of k-automatic sequences; Theorems 2–3 give the shift-
decision and digit-transform results; Theorems 4–6 apply it to unbordered
factor lengths in Thue–Morse (solving Currie–Saari's open problem),
Rudin–Shapiro, and paperfolding.

Related held decision papers (Fibonacci- and Sturmian-specific):
`research/sources/mousavi-schaeffer-shallit-fibonacci-automatic-ar5iv.full.md`
(WALNUT; Fibonacci-automatic words), `research/sources/hieronymi-decidability-
sturmian-words-ar5iv.full.md` (Pecan; Sturmian words via Ostrowski numeration),
`research/sources/cobham-bes-frougny-mult-dep-linear-numeration-2002-irif.full.md`
(Cobham for Pisot bases; blocks base conversion between 10 and phi).