# Hieronymi, Ma, Oei, Schaeffer, Schulz, Shallit — *Decidability for Sturmian Words* (LMCS 20:3, 2024)

Source: https://arxiv.org/pdf/2102.08207 — [[hieronymi-decidability-sturmian-words-ar5iv.full]]

## What this source establishes

A logical-computability paper: the first-order theory of Presburger arithmetic
plus a Sturmian word predicate is decidable; Sturmian words are uniformly
ω-automatic in Ostrowski numeration; the decision tool "Pecan" automatically
reproves classical Sturmian theorems and finds new results on antisquares and
antipalindromes in characteristic Sturmian words.

Relevant structural facts:
- Sturmian words are ω-automatic w.r.t. the Ostrowski numeration of their
  slope; addition is ω-automatic in Ostrowski systems (Baranwal–Schaeffer–Shallit).
- The characteristic Sturmian word's factors and special factors are
  first-order expressible; φ(n) = presence of blocks, antisquares, etc. is
  decidable in principle.

## What it implies for PE1006

**Does not help the computation.** The paper is about *decidability* (the
existence of a decision procedure, with non-elementary worst-case cost — it
explicitly says the general procedure is "truly formidable"), not about
*feasible evaluation* of a specific numeric sum. Ψ(10^18) mod M is one concrete
quantity; the O(log) universal-Euclidean route (fhq/OI-wiki/LOJ138) is the
feasible primitive, and this paper neither provides it nor improves on it.

Verdict: tier-3 background. Records that Sturmian-word questions over Presburger
arithmetic are decidable in principle (so no *impossibility* obstruction exists),
but nothing here is load-bearing for obtaining Ψ's residue.

## Claims anchored here

None.