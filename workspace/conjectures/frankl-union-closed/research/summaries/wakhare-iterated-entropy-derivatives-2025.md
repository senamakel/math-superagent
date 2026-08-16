# Iterated Entropy Derivatives and Binary Entropy Inequalities

Tanay Wakhare. arXiv:2312.14743v2; **published** J. Approximation Theory 307 (2025) 106143. (Peer-reviewed survey of the entropy-inequality line.)

**Full text (read, intro + Thms):** `research/sources/wakhare-iterated-entropy-derivatives-2025.html.full.md` (73KB)

## What it establishes (primary source, read)

**The current-best-constant statement, corrected.** The paper states "the current best constant is ≈ 0.38237 [Liu24], though the method suffers natural limitations. The survey [Cam23] summarizes recent progress and barriers, but new ideas will be needed to prove the full conjecture." Reference [Liu24] is **Jingbo Liu, "Improving the lower bound…via conditionally iid coupling", Proc. 58th Annual Conf. on Information Sciences and Systems (CISS), IEEE, 2024, pp.1-6** — i.e. the ≈0.38237 is Liu's conditional bound, now an IEEE conference publication. This resolves a small numeric discrepancy in the library: the "0.38237" in a 2025 journal is **not a new record beyond Liu**; it is Liu's own CISS-2024 value (the library's Liu ≈0.38271 is the more precise form of the same conditional bound). No published source in the library or in Wakhare exceeds it unconditionally.

**Conjecture 1 (the real-k entropy inequality).** Let k ≥ 1 real, 0<α_k<1 the unique solution of α_k = 1/(1+α_k)^(k−1) in (0,1). Then α_k·H(xᵏ) ≥ x^(k−1)·H(x) for 0≤x≤1, equality at x=0, 1/(1+α_k), 1. **k=2 is Gilmer's/Boppana's inequality, the engine of the iid-entropy (3−√5)/2 barrier.** Lemma 16: α_k is unique with 1/k < α_k < 1; Lemma 17: α_k = (log k)/k + O(log log k/k).

**The structural fact: real-rootedness reduction (Theorem 3).** If the "entropy polynomial" p_{k,r}(x) (defined (1.4), degree k²+kr−r) has exactly two real roots in (0,1), then Conjecture 1 holds for exponent k/r. If this holds for all coprime k>r≥1, Conjecture 1 holds for all real k≥1. So the whole real-k entropy-inequality line reduces to a **polynomial-root-counting statement** — exactly the shape this run's sat_solver/symbolic machinery can attack. Conjecture 2 holds (by quick calc) for k=3,r=2 and for k=3/2 (fractional).

**Theorem 4.** Three closed forms for (d/dx)^(k+1) x^(k−r)·H(x^r): an infinite series; a finite sum with generalized binomials (rv+k choose k); and a generalized-Stirling-number form (Hsu–Shiue). These are the computational workhorse for checking the real-k inequality.

**Information-theoretic reading.** With X₁..X_k ~ Ber(x), A_j = AND of first j bits: H(xᵏ) = H(A_k), x^(k−1)H(x) = H(A_k | A_{k−1}). So Conjecture 1 is a **strong data-processing inequality** for AND, comparing entropy of AND of k bits with conditional entropy of the k-th given the first k−1.

**Why it matters for this run:** (a) fixes the "0.38237" attribution (Liu CISS 2024, not a newer record); (b) the k>r polynomial-root route is a concrete, finite, sat-solver-able formulation of "prove the entropy inequality for fractional k" — the exact shape the live `attack-coupling-half` needs; (c) Ho (arXiv:2601.19327, also in this library) has since proved Conjecture 1 for all real k>1 by a different (calculus) route and formalized it in Lean 4, so the root-counting conjecture is confirmed by a second method — the two make a strong cross-check.

```claim
id: wakhare-0-38237-is-liu-ciss
statement: The "≈0.38237 current best constant" in a 2025 J. Approximation Theory survey is Liu's conditionally-IID bound (CISS 2024, IEEE), not a record beyond Liu's ≈0.38271 (which is the same bound's precise form). No published source exceeds it unconditionally.
hypotheses: none.
holds-here: true
status: sourced
bearing: resolves the numeric discrepancy in the library; confirms Liu is the frontier and there is no hidden post-Liu published record.
anchor: Wakhare arXiv:2312.14743 (JMAA 2025), Intro; ref [Liu24] = CISS 2024.
```

```claim
id: wakhare-realroot-reduction
statement: The real-k entropy inequality α_k H(x^k) ≥ x^(k−1)H(x) for all k≥1 follows if each entropy polynomial p_{k,r} has exactly two real roots in (0,1) (Theorem 3); k=2 is Boppana's/Gilmer's inequality underlying the (3−√5)/2 barrier.
hypotheses: k,r integers, k>r≥1; Conjecture 2.
holds-here: true
status: proved (as a reduction; the root conjecture itself open)
bearing: reduces a continuum of entropy inequalities to finite polynomial-root checking; a concrete route for sat_solver/symbolic work; Ho's 2026 result independently proves the target.
anchor: Wakhare arXiv:2312.14743, Conjectures 1-2, Theorem 3.
```

## Notes
- Independently cross-checks Ho (arXiv:2601.19327): Wakhare's real-rootedness program and Ho's calculus proof both prove Conjecture 1 for real k; Ho additionally gives the Lean 4 formalization. Taken together, not a proof of UC, but a fully-settled family of entropy inequalities that UC's iid-entropy attack rests on.
