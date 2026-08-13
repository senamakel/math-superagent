# Chase 2024 — A random analogue of Gilbreath's conjecture

**Full text:** `research/sources/chase-2024-random-analogue-gilbreath.full.md` [[chase-2024-random-analogue-gilbreath.full]]
**Source:** Math. Ann. 388 (2024) 2611–2625 = arXiv:2005.00530, doi 10.1007/s00208-023-02579-w. Open access. Zachary Chase.

## What it establishes

Proves the (precise form of) the postulate that "2 followed by increasing odd numbers with small random gaps" is eventually Gilbreath. This is the historical first rigorous random-analogue theorem (predecessor of CHT 2026).

- **Theorem 1.** Let f increasing, 2≤f(n), f(M) ≤ (1/100)·loglog M/logloglog M for M large. Random seq: a_1=2, a_2=3, a_{n+1}=a_n+2u_n, u_n uniform on {0,..,f(n)−1} independent. Then a.s. some M_0 with: for all M≥M_0, after M iterations the first term is 1.
- **Theorem 2 (the heart).** For M large, 2≤C≤(1/100)loglog M/logloglog M: for a length-M sequence uniform on {0,..,C−1}, w.p. ≥ 1−e^{−e^{∜⁵√log M}}... (precisely ≥1−e^{−e^{(log M)^{1/20}}}), after e^{(log M)^{1/5}} iterations everything is 0 or 1.
- **Lemma 3.2 (the {0,d}-block consumption lemma).** Let a_1..a_i nonneg, d=max a_j, L = length of longest {0,d}-block containing a d. If L ≤ i−1, then after L iterations the largest number is ≤ d−1. This is precisely the run's "consumption" statement: a {0,d}-block of length L shrinks the maximum by one every L rows.
- **Lemma 3.5 / Corollary 3.6 (parity).** f_i(a_1..a_{i+1}) ≡ Σ_{j∈J_i} a_j mod 2 with J_i⊆[i+1] containing 1 and i+1; so the parity of the ultimate iterate depends linearly on the first and last initial parities, so independent uniform data iterate to even with prob between 1/3 and 2/3, and long runs of even values are exponentially unlikely. (This is the parity formula CHT generalises as Lemma 3.10.)
- **Section 6:** proof adapts to any distribution with positive weight on each of 0..C−1, not just uniform.
- **Proth myth retraction (Sect. 7):** the claim "Proth claimed to prove GC and was wrong" is baseless; H.C. Williams, its apparent originator, retracted ("I can find no support for my assertion... Apologies for seeming to have started a myth", email 2020). Corrects the citation: Proth discussed GC only in Nouv. Corresp. Math. 4 (1878) 236–240; the C.R. 85 (1877) "Théorèmes sur les nombres premiers" is actually Pepin's paper, and C.R. 87 (1877) does not discuss GC at all.

## Hypotheses held here?

Theorems 1–2 are statements about *random* initial data with f(n) extremely slowly growing (≤ loglog n/logloglogn/100). The primes are deterministic and conjecturally only Cramér-random with gaps ~ log n, far above this f; so the theorem does NOT apply to the primes directly — it is heuristic support for the Cramér-type picture, superseded by CHT 2026 Theorem 1.3 for the more realistic f(n)=o(n). Confirms the "small random gaps suffices" postulate at the level of the 2/{0,1}/(0,2) regime.

## Bearing on this run

- **Lemma 3.2 is the run's consumption lemma at the {0,d} level** — matches Odlyzko's block lemma and the run's `odlyzko-block-lemma-exact` (a {0,d}-block of length L bounds how fast the max can drop). Good independent re-derivation of the consumption side.
- Theorem 1's mechanism (leading odd term dropping by 2 each step while second term is 2) is exactly the run's `{0,2}`-regeneration mechanism that CHT later generalises: once everything is 0 or 2 (after halving 0/1), a leading odd ≥3 shrinks by 2 per 2-valued step toward 1 and stays 1 forever.
- Exotic {0,3}-type examples (0s and 3s, or the Sierpinski {0,3} example) are the reason small-gaps/randomness is *necessary* — echoed in the run's `two-separation-hypothesis` and Eppstein anti-Gilbreath.
- Confirms `proth-myth-retracted` and `chase-2024-arxiv-id` claims independently.

## Claims

```claim
id: chase-2024-theorem1
statement: For f increasing, 2≤f(n), f(M)≤(1/100)loglogM/logloglogM, the random sequence a_1=2,a_2=3,a_{n+1}=a_n+2u_n (u_n uniform independent on {0,..,f(n)−1}) is almost surely eventually Gilbreath (first term of every late row is 1).
hypotheses: random initial data with f growing ≤ logloglog(log...); Cramér-type small gap model.
holds-here: primes are deterministic & gaps ~log n exceed this f; heuristic support only, superseded by CHT 2026.
status: proved in source; not checked here.
bearing: establishes small-random-gaps suffices in a weak random model; first rigorous random analogue.
anchor: research/sources/chase-2024-random-analogue-gilbreath.full.md
```

```claim
id: chase-2024-block-consumption03
statement: If a_1..a_i are nonneg with d=max and L = length of longest {0,d}-block containing a d, then after L iterations the max is ≤ d−1 (Lemma 3.2).
hypotheses: none beyond the {0,d}-block structure.
holds-here: yes — the run's consumption (block shrinks max one level per its length).
status: proved in source (elementary induction); consistent with Odlyzko block lemma.
bearing: independent source for the consumption half of regeneration.
anchor: research/sources/chase-2024-random-analogue-gilbreath.full.md
```
