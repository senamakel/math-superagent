# Marić, *Fast Formal Proof of the Erdős–Szekeres conjecture for convex polygons with at most 6 points*, J. Automated Reasoning 62(3) (2019) 301–329

<!-- source: https://link.springer.com/article/10.1007/s10817-017-9423-7 (DOI 10.1007/s10817-017-9423-7) -->

**Filip Marić.** The Springer article page is paywalled: what is held is the article landing page with the full abstract and complete reference list (JAR 62(3):301–329, DOI 10.1007/s10817-017-9423-7). The mathematics beyond the abstract is NOT in hand — see the gap note at the bottom. JAR 62(3):301–329.

## What it establishes

- The conjectured value for m=6, i.e. **ES(6) = 17**, was first verified by Szekeres & Peters (2006) via huge computer enumeration ("more than 3000 GHz hours").
- Marić re-proves the m=6 case (every set of 17 points in general position contains a convex 6-gon) with a **formally verified** proof:
  - changing the problem representation (SAT encoding),
  - symmetry breaking,
  - modern SAT solvers,
  - and **formalizing the whole proof inside the Isabelle/HOL proof assistant**.
- Result: the proof that took >3000 GHz-hours is reduced to **~1 GHz-hour (~half an hour on an ordinary PC)**, and it is machine-checked in Isabelle/HOL.

```claim
id: maric-es6-formal
statement: ES(6) = 17 is formally verified in Isabelle/HOL (Filip Marić, J. Automated Reasoning 62(3) 2019): every set of 17 points in general position contains a convex 6-gon, proved by a SAT encoding with symmetry breaking whose unsatisfiability is machine-checked; runtime ~1 GHz-hour vs >3000 GHz-hours for Szekeres–Peters.
hypotheses: planar point set, no three collinear (general position); m=6.
holds-here: yes — exact statement of the m=6 case the run must reproduce on the way to any ES(7) argument; also the model for this run's Lean formalization of ES(6).
status: asserted-by-source (peer-reviewed formal-verification paper; the Isabelle/HOL proof is the evidence, not reproduced by this run).
bearing: GOAL item 5 (Lean 4 formal statement of ES(n) and the conjecture) and item 3 (oracle reproducing ES(6)=17). Establishes the benchmark: a verified SAT/Isabelle route to the m=6 bound, with runtime and encoding known.
anchor: research/summaries/maric - Fast Formal Proof ES for convex polygons at most 6 points - JAR 2017.md
```

## Why it matters here

Marić's is the **canonical formal-verification reference** for this exact problem at m=6, cited by Subercaseaux et al. (ITP 2024, already held) as the pioneering SAT reduction formalized in Isabelle/HOL. It is directly relevant to this run's Lean goal and to the oracle reproduction of ES(6)=17.

**Distinct from** Suk (2^{n+o(n)} upper bound, arXiv:1604.08657 — already held) and from the monotone-subsequence "Erdős–Szekeres theorem", which is a different theorem.
