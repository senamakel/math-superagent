# Laterveer & Ounaïes, *Constraints on hypothetical counterexamples to the CA conjecture* (arXiv:1204.0450)

Full text: [[laterveer_ounaies_constraints_2012]]

Provenance of the **minimal-counterexample structure** recorded in ROOT.md/CLAIMS.md. Elementary (Gauss–Lucas, Newton, Rolle, symmetric polynomials) constraints on how degenerate a counterexample can be. "This note is the fruit of a failed attempt to prove the conjecture for N=12."

## Structural constraints (all char-0, monic, proven here/in [DdJ])

```claim
id: shared-root-set-not-2
statement: [DdJ Prop 6] Let f be CA of degree N≥1 and α_i a common root of f and f^(i).
  The cardinality of {α_1,…,α_{N−1}} cannot be two. Corollaries: if f^(2)=(N)(N−1)(z−a)^{N−2}
  then f=(z−a)^N; a root of multiplicity ≥ N−1 forces f=(z−a)^N; a non-trivial CA
  polynomial has at least 3 distinct roots.
hypotheses: char 0
holds-here: yes
status: proved (Prop 1 here; the ∉-2 fact is [DdJ])
bearing: a candidate structural target (forcing coincidences among shared roots) must
  respect this: exactly-2 distinct shared roots is already ruled out.
anchor: research/sources/laterveer_ounaies_constraints_2012.full.md (§1, Prop 1)
falsifies: a held counterexample with exactly 2 distinct shared roots.
```

```claim
id: multiplicity-near-n
statement: If f is monic CA of degree N≥4 and f^(3)(z) = N!/(N−3)! (z−a)^{N−3}, then
  f=(z−a)^N. Also: if f has a root of multiplicity ≥ N−2, then f=(z−a)^N (Prop 3, N≥3).
  These are "almost pure power" rigidity results (via Rolle/Gauss–Lucas + an inequality
  argument that is specifically real/char-0).
hypotheses: char 0
holds-here: yes
status: proved (Prop 2, Prop 3)
bearing: a counterexample cannot have any root of multiplicity ≥ N−2 — a strong bound
  on multiplicity patterns, directly usable in the run's multiplicity-structure target.
anchor: research/sources/laterveer_ounaies_constraints_2012.full.md (§1, Prop 2–3)
falsifies: a held counterexample violating these bounds.
```

```claim
id: at-least-five-distinct-roots
statement: A non-trivial CA polynomial of degree N≥5 has at least five distinct roots, so
  N≥6, and at least 4 distinct roots in its open Gauss–Lucas hull. CA holds if f has
  at most 4 distinct roots (Prop 5).
hypotheses: char 0, monic degree N
holds-here: yes
status: proved (Prop 4 [N≥4, ≥4 distinct roots], Prop 5 [N≥5, ≥5 distinct roots])
follows-from: shared-root-set-not-2, multiplicity-near-n
bearing: ANY counterexample is quite non-degenerate: ≥5 distinct roots. Refuting CA for
  degree n therefore reduces to deg-n polys with ≥5 distinct roots — a tight constraint
  on the search space and on the variety dimension.
anchor: research/sources/laterveer_ounaies_constraints_2012.full.md (§1, Prop 4–5)
falsifies: a held counterexample with ≤4 distinct roots.
```

## Degree p+1 / p^r+1 (p-adic valuation; §2)

```claim
id: p1-counterexample-constraints
statement: For N = p+1 (p prime), let c be the root of f^(N−1). Then f'(c) ≠ 0 and there
  are at least 2 indices 2 ≤ l_1 < l_2 ≤ N−2 with f^(l_1)(c)=f^(l_2)(c)=0 (Prop 7). A
  degree-(p+1) CA polynomial all of whose roots are rational satisfies CA (Prop 8).
  General lemmas: a root of multiplicity m of f (0≤m≤i) is at most a simple root of f^(i)
  (Lemma 3, [9]); v_p((p^r choose i))-type valuations (Lemma 4, [5]).
hypotheses: degree p+1; char 0
holds-here: yes (p+1 is a special-degree case the run may use as a testbed)
status: proved (Prop 7, Prop 8; the valuation lemmas cited)
bearing: The p-adic-valuation method's elementary form. N=12=11+1 is the settled case;
  its nearest open relative is degree p+1 for larger p via these shared-root-at-c
  constraints.
anchor: research/sources/laterveer_ounaies_constraints_2012.full.md (§2)
falsifies: a degree-(p+1) rational-rooted counterexample.
```

## What it does not settle
No new degree is settled here (it is explicitly a failed N=12 attempt). All constraints hold in char-0 only; they use real/complex analysis (Gauss–Lucas, monotonicity of φ(t)) so they are exactly the sort of step with no char-p analogue — consistent with the char-p counterexamples existing.
