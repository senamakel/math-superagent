# Li & Zhao, "Non-Wieferich property of prime ideals and a conjecture of Erdős"

Source: arXiv:2601.12753, 19 Jan 2026. Full text: `research/sources/li-zhao-2026-non-wieferich-erdos-body.full.md` (PDF capture, held in full, 931 lines). This note replaces an earlier self-contradictory draft that both reported the body as absent and as present; the body IS in the library and is digested in `research/summaries/li-zhao-2026-non-wieferich-erdos-body.md`.

## What the body establishes

**Theorem 1.2 (generalisation of Dupuy–Weirich, number-field case).** Let `(β) = p_1^{g_1}⋯p_h^{g_h}` with each `p_i` unramified and `N(p_i) = p_i` (residue degree 1), and `α` relatively prime to `β`, not a root of unity. Then `lim_{m→∞} f_{α,m}(b) = 1/#D` for all digit `b ∈ D`, where `f_{α,m}` is the Cesàro average over `n` of the frequency of digit `b` in the first `m` digits of the β-adic expansion of `α^n`.

**The Erdős-relevant case is covered, and its hypotheses hold here.** Taking `K=ℚ, α=2, β=3`: the ideal `(3)` is unramified with `N((3)) = 3 = p` (residue degree 1), and 2 is coprime to 3. So Theorem 1.2 applies unconditionally: the ternary digits of `2^n` are asymptotically equidistributed **in the Cesàro average over n** — the same conclusion as Dupuy–Weirich Theorem 3, restated and generalised.

**Theorem 1.3:** if `(β)` has a ramified prime-ideal factor, still get a block-complexity result `C(α)` on β-adic expansions of `α^n`.

**Notation.** `f_{α,m}(b)` is a Cesàro average over `n` (`1/N Σ_{n≤N}`), not a statement about any single `n`.

## What it does NOT do

Like Dupuy–Weirich and the probabilistic heuristic, the equidistribution is an **average/density** statement. It does not pin down the digits of any particular `2^n`, does not rule out a counterexample `n > 8`, and says nothing about which integers lie in the digit-`{0,1}` set. It is background, not a proof route.

```claim
id: LI-ZHAO-EQUIDISTRIBUTION-DW-GEN
statement: (Theorem 1.2) For α, β relatively prime in a number field with
  prime-ideal factors of (β) unramified and residue degree 1 (N(p_i)=p_i), α not
  a root of unity, the digits of the β-adic expansions of α^n are asymptotically
  equidistributed (Cesàro average over n) at frequency 1/#D, generalising
  Dupuy–Weirich. The K=Q, α=2, β=3 case is covered: (3) unramified, N((3))=3,
  residue degree 1, so ternary digits of 2^n equidistribute in the average.
hypotheses: (β) unramified residue-degree-1 prime-ideal factors; α coprime to β,
  not a root of unity.
holds-here: yes -- the K=Q, α=2, β=3 case satisfies all hypotheses
  unconditionally (verified against the held full body, Theorem 1.2).
status: asserted-by-source (proved in the paper; statement verified against the
  held body, proof not re-derived here).
bearing: the strongest recent statement in the digit-uniformity line; a Cesàro
  average over n, so it does not constrain any particular 2^n and cannot prove
  the Erdős conjecture. Background on digit distribution, consistent with the
  heuristic.
anchor: research/sources/li-zhao-2026-non-wieferich-erdos-body.full.md
```

## Status

Sourced, full body held. Resolves the earlier `holds-here: unchecked` on the
Erdős-relevant ℤ case: the hypotheses DO hold, so the claim is now `holds-here:
yes` (still asserted-by-source on the proof).
