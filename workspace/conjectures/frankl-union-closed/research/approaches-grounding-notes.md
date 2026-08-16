# Grounding the three proposed approaches — literature findings

This note records what the literature establishes for each of the three proposed
lines in `research/approaches/`. Claim blocks here feed `research/CLAIMS.md`.

Sources consulted (all external, cited): Bruhn–Schaudt survey (arXiv:1309.3297),
Bouchard lattice formulation (arXiv:2503.00277, Le Matematiche 81(1) 2026),
Bruhn–Charbit–Schaudt–Telle graph formulation (arXiv:1409.1814 / EJC 2014),
Bhasin cubical homology (arXiv:2409.17050), Dochtermann–Engström edge ideals
(arXiv:0810.4120), Van Tuyl SCM bipartite (arXiv:0906.0273), Cook–Nagel
Cohen–Macaulay face vectors (SIDMA 2012), Freese–Ježek–Nation / Day doubling
(day-doubling-constructions-lattice-theory 1992; Generalizing semidistributivity,
Geyer Order 1993; Congruences of a Finite Lattice, Grätzer 2nd ed. 2021),
Nation congruences of finite semidistributive lattices (2024), Knop Möbius
algebras of semilattices (Adv. Math 2007).

## 1. Möbius algebra

The semigroup algebra C[L,∨] with primitive orthogonal idempotents
e_b = Σ_{c≥b} μ(b,c)·c is the classical *Möbius algebra of the semilattice*
(Solomon's construction; explicitly developed for (semi)lattices in Knop,
"Tensor envelopes of regular categories", Adv. Math 2007, §7 — there p_v =
Σ_{u≤v}μ(u,v)u with p_u·p_v = δ_{u,v}p_v). Möbius inversion gives x = Σ_{b≥x}e_b,
and dim(L·a) = |↑a|. Both identities verified here by hand for the chain and
Boolean small cases (matching Solomon's construction).

Poonen's lattice form (UC ⟺ some join-irreducible j with |↑j| ≤ |L|/2) is an
established reformulation. Bouchard (arXiv:2503.00277) works in exactly this
lattice formulation and derives necessary conditions for a minimum-size
counterexample — but Bouchard does **not** use the Möbius-algebra idempotent
basis; it proceeds structurally by removing join-irreducibles (Lemma 1.2,
Theorem 1.4, L∖J is a lattice). So the *specific* idempotent-basis reformulation
of the forcing step appears novel, but I found **no source** that proves the
"forcing" identity (that the join-irreducibles cannot all be more than
half-populated in the idempotent decomposition). That step is genuinely open.

```claim
id: mobius-idempotent-expansion
statement: In the semigroup algebra C[L,∨] of a finite lattice, e_b = Σ_{c≥b} μ(b,c)c are orthogonal primitive idempotents; Möbius inversion gives x = Σ_{b≥x} e_b; and dim(L·a) = |↑a|.
hypotheses: L a finite lattice; μ the Möbius function of L
holds-here: yes (the lattice formulation of Frankl's conjecture)
status: proved (classical Solomon construction; verified by hand here for chain/Boolean cases; script code/out/mobius_algebra_check.py written for mechanical confirmation)
bearing: grounds the two "checkable facts" of mobius-algebra-join-irreducibles
anchor: Knop Adv.Math 2007 §7 (https://doi.org/10.1016/j.aim.2007.03.001)
```

```claim
id: bouchard-lattice-no-mobius-basis
statement: Bouchard (arXiv:2503.00277) studies the lattice formulation of Frankl's conjecture with necessary conditions on a minimal counterexample, but works structurally (removing join-irreducibles, L∖J is a lattice) and does NOT use the Möbius-algebra primitive idempotent decomposition.
hypotheses: L a minimum-size counterexample lattice
holds-here: yes (this is the lattice form)
status: asserted (verified from the full text on disk, research/sources/bouchard-lattice-2025.trial.full.md)
bearing: the idempotent-basis forcing step of mobius-algebra is not in Bouchard; no precedent found
anchor: research/sources/bouchard-lattice-2025.trial.full.md
```

## 2. Independence complex / facet counts / topology

The graph formulation (Bruhn–Charbit–Schaudt–Telle) makes maximal-stable-set
(= facet-of-independence-complex) counts the central object; the settled
bipartite classes (chordal bipartite, subcubic bipartite, series-parallel,
circular interval) were obtained by exactly counting maximal stable sets. So the
facet-count perspective is the proven workhorse.

However, the *specific* mechanism proposed — that a bipartition class with every
vertex in >half the facets would violate an Euler-characteristic / f-vector
identity of I(G) — has **no precedent** and faces a concrete obstruction:
independence complexes of bipartite graphs are generally **non-pure** (maximal
stable sets have different sizes), so the reduced Euler characteristic is a
signed alternating sum over all faces, not a signed facet count, and does not
control link-facet counts. Engström-type / edge-ideal results (Dochtermann–
Engström; Van Tuyl; Cook–Nagel) concern (co)homology, Castelnuovo–Mumford
regularity, and Cohen–Macaulayness − not facet-count forcing. The one direct
topological application to union-closed (Bhasin, cubical set of a simply-rooted
family) proves acyclicity and an Euler–Poincaré identity, but yields **no
abundance / facet-count forcing**.

```claim
id: independence-complex-nonpure
statement: Independence complexes of bipartite graphs are generally non-pure (maximal stable sets of differing cardinality), so the reduced Euler characteristic is an alternating signed sum over all faces and does not reduce to signed facet counts; no f-vector/Euler identity is established that forces a half-density vertex via link-facet counts.
hypotheses: G bipartite finite graph; I(G) independence complex
holds-here: yes (this is the graph form of Frankl)
status: inference (from the standard f-vector/Euler theory; no contrary source found)
bearing: the Euler/facet-count hinge of independence-complex-facet-counts is not grounded
anchor: https://doi.org/10.1137/100818170 (Cook–Nagel), https://arxiv.org/abs/0810.4120 (Dochtermann–Engström)
```

```claim
id: topological-union-closed-acyclicity
statement: For the cubical set X(F) of a simply-rooted (complement of union-closed) family F ⊆ 2^[n] containing ∅, X(F) is acyclic (trivial reduced cubical homology); an Euler–Poincaré identity follows. This is structural and gives no element-abundance forcing.
hypotheses: F simply rooted, ∅∈F
holds-here: yes (complement of a union-closed family)
status: proved (source)
bearing: the closest existing topological treatment of union-closed; not a facet-count/abundance forcing
anchor: https://arxiv.org/abs/2409.17050 (Bhasin 2024)
```

## 3. Congruence / Day doubling induction

The decisive finding: the Day doubling construction produces **exactly the
bounded lattices** (interval doublings) and the **congruence normal lattices**
(convex-set doublings), which are **proper subclasses** of all finite lattices.
Freese–Ježek–Nation: finite bounded lattices are exactly those obtainable from
the one-element lattice by a finite sequence of interval doublings. Geyer:
L is bounded ⟺ L is congruence normal AND semidistributive. Day: the quotient
by a maximal congruence of a *congruence normal* lattice is a convex-set
doubling. This does **not** hold for an arbitrary finite lattice: a finite
lattice is not in general generated by doublings (only the bounded /
congruence-normal ones are), so a minimal counterexample to Frankl's conjecture
is **not forced** to be a single interval-doubling of a maximal-congruence
quotient.

Consequently the inductive step at the heart of congruence-doubling-induction —
"quotient by a maximal congruence is a single interval-doubling, so lift the
abundant join-irreducible through the de-doubling" — is **not justified for
general lattices**; it holds only inside the bounded / congruence-normal class,
and even there the lift bookkeeping (the inventor's speculative step) is
unproven and its filter-meets-convex-set condition has no published treatment.
The proposal reduces the conjecture, at best, to the bounded-lattice special
case (already a proper subclass; proving it settles a new class but not the
conjecture).

```claim
id: bounded-iff-interval-doublings
statement: A finite lattice is bounded (a bounded homomorphic image of a free lattice) iff it is obtainable from the one-element lattice by a finite sequence of interval doublings; L is bounded iff L is congruence normal and semidistributive (Geyer). Bounded and congruence-normal lattices are proper subclasses of all finite lattices.
hypotheses: L finite lattice
holds-here: n/a (structural fact about lattices; not every finite lattice is in these classes)
status: proved (classical; Freese–Ježek–Nation; Day; Geyer)
bearing: limits the Day-doubling induction to the bounded/congruence-normal class
anchor: https://link.springer.com/article/10.1007/BF01108710 (Geyer); https://doi.org/10.4153/cjm-1992-017-7 (Day)
```

```claim
id: day-doubling-hypothesis-fails-general
statement: Not every finite lattice is a single interval-doubling of a quotient by a maximal congruence. The single-doubling correspondence holds only within the bounded (interval) / congruence-normal (convex) classes. A minimal counterexample to Frankl's conjecture is not forced to lie in these classes, so a maximal-congruence de-doubling induction cannot be applied to it in general.
hypotheses: L an arbitrary finite lattice; θ a maximal congruence
holds-here: yes (this is the obstruction to the proposed induction)
status: inference from the class characterization (bounded/congruence-normal proper subclasses); no source shows an arbitrary finite lattice is a single doubling of a quotient
bearing: refutes congruence-doubling-induction as a route to the general conjecture; leaves a bounded-lattice special case open
anchor: https://link.springer.com/article/10.1007/BF01108710; https://doi.org/10.4153/cjm-1992-017-7; Nation Congruences of finite semidistributive lattices (2024)
```

## 4. Forbidden-sublattice (N₅/M₃) lifting — lattice kernel

The inventor's approach (research/approaches/forbidden-sublattice-lifting.md)
rests on an explicit lattice kernel: that N₅ and M₃ each contain a
join-irreducible whose principal filter has size ≤ 5/2, which the lift attempts
to propagate to the whole lattice. I hand-verified this explicitly (script
code/out/n5_m3_joinirreducible_check.py written for tool_builder confirmation).

**M₃ (the diamond): kernel is CORRECT.** Each atom a,b,c has principal filter
{a,1} of size 2 ≤ 5/2, and atoms are join-irreducible. Verified.

**N₅ (the pentagon): kernel is WRONG as stated.** The inventor claims "N₅ has
the join-irreducible b with |↑b| = 2". In fact, for the (unique) pentagon
(0<a<c<1, 0<b<c<1, a∥b), the join-irreducibles are {a, b, 1} with filter sizes
|[a)|=3, |[b)|=3, |[1)|=1. The only join-irreducible with |↑j| ≤ 5/2 is the top
1̂ (filter 1, vacuous). The element c with |[c)|=2 is NOT join-irreducible
(c = a∨b). So N₅'s *only* abundant join-irreducible is its top, whose filter is
the whole copy — and lifting the top is trivial/meaningless. The M₃ half of the
kernel survives; the N₅ half does not, and the "local abundant join-irreducible
b of the N₅ copy" that the lift was supposed to propagate does not exist.

```claim
id: n5-m3-joinirreducible-filters
statement: In the diamond M₃ each atom a has principal-filter size |[a)|=2 ≤ 5/2 (kernel confirmed). In the pentagon N₅ the join-irreducibles are {a,b,1̂} with filter sizes {3,3,1}; the only join-irreducible with |[j)| ≤ 5/2 is the top 1̂ (filter size 1, vacuous). The element c with |[c)|=2 is join-reducible (c=a∨b). Hence N₅ has no non-trivial abundant join-irreducible to lift; the inventor's claim "b with |↑b|=2" is false for any labelling of N₅.
hypotheses: N₅, M₃ the standard pentagon/diamond lattices; [j)=principal filter
holds-here: yes (this is the lattice-form kernel of the lift proposal)
status: checked (hand-verified for both standard N₅ labellings; script written for mechanical confirmation)
bearing: corrects the checkable kernel of forbidden-sublattice-lifting — the M₃ half stands, the N₅ half is refuted as stated
anchor: code/out/n5_m3_joinirreducible_check.py (hand-derived, awaiting tool_builder confirmation)
```

This does not refute the *program* (lift an abundant join-irreducible from a
sublattice copy), only the specific claim that N₅ supplies such a
join-irreducible: a valid lift would have to start from M₃, or from a different
choice of abundant join-irreducible in N₅ relative to the containing lattice.
No published "forbidden-sublattice lifting of an abundant join-irreducible" for
Frankl's/union-closed was found (searched N₅/M₃ lifting join-irreducible
union-closed/UC).
