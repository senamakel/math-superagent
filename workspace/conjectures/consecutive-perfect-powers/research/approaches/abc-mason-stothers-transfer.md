# abc / Mason–Stothers transfer

_Reformulation candidate. Evaluated 2026 by research@rising-sea._

## Verdict

**status: adopted** (inventor decision, after research)

The one claim that would make this *prove* Catalan — the abc transfer — is a genuine folklore conditional theorem with the exact arithmetic, but its hypothesis is an open conjecture. Adopted for its two halves: (i) an unconditional, falsifier-safe, kernel-formalizable function-field no-solutions theorem (no nonconstant polynomial solutions of `X^p − Y^q = 1` over `C[t]`), and (ii) a precise conditional theorem — abc with ε < 1/2 ⇒ every integer solution has min(p,q) = 2, which with the exponent-2 cases forces the known solution. The known solution `3²−2³=1` (one exponent equal to 2) is the boundary case, untouched by both halves.

The one claim that would make this *prove* Catalan — the abc transfer — is a genuine folklore conditional theorem with the exact arithmetic, but its hypothesis is an open conjecture, so as a route to the coverage requirement (Scholze's rule: reproduce a result already established in the old setting) it must be judged on the unconditional half alone. The unconditional half (no nonconstant polynomial solutions of `X^p − Y^q = 1` over `C[t]`) is fully grounded and self-contained, and it does **not** over-eliminate: the integer solution `3² − 2³ = 1` is the constant solution and is untouched.

## What the reformulation is called

- **Mason–Stothers theorem** ("the abc conjecture for polynomials", also Mason's inequality). Statement: over a field of characteristic 0, for nonzero **pairwise coprime** polynomials `a, b, c ∈ k[t]` with `a + b = c`, either `a' = b' = c' = 0` or
  `max{deg a, deg b, deg c} ≤ deg rad(abc) − 1`,
  where `rad(P)` = product of distinct linear factors of `P`.
- The corollary (no nonconstant solution of `X^p − Y^q = 1` for any `p, q ≥ 2`) is the polynomial/Fermat-type consequence.
- The arithmetic analogue is **the abc conjecture** (Masser–Oesterlé 1988): for coprime integers `A+B=C`, for any `ε>0`, `max{|A|,|B|,|C|} ≤ K(ε)·rad(ABC)^{1+ε}`.

## Precise statements, with hypotheses

**Mason–Stothers** — sources:
- Noah Snyder, "An Alternate Proof of Mason's Theorem," Elementa der Mathematik (2000), `https://doi.org/10.1007/s000170050074`. Gives `deg(f) ≤ deg(gcd(f,f′)) + n₀(f)` and from it `deg c ≤ n₀(abc) − 1` with `n₀` = number of distinct zeros, yielding the radical bound.
- hal.science/hal-01626155v1 (poster): full form `max(deg A, deg B, deg C) ≤ deg(Rad(ABC)) − 1`, Wronskian `W(A,B)=AB′−A′B`, with the argument `G_A G_B G_C | W`.
- Jineon Baek, Seewoo Lee, "Formalizing Mason-Stothers Theorem and its Corollaries in Lean 4," arXiv:2408.15180 (2024) — a **kernel-checked** formalization (valuable: this is a technique-tier source, not a Catalan answer, so obtainable).
- Ishizaki–Korhonen–Li–Tohge, Math. Z. (2020), `https://doi.org/10.1007/s00209-020-02604-7`, restates the classical bound and its polynomial-Fermat consequence (no coprime polynomial `f,g,h` with `f^n+g^n=h^n`, n≥3).

The corollary for `X^p − Y^q = 1`: set `a = X^p`, `b = −Y^q`, `c = 1`; they are pair-coprime for a nonconstant solution (else a common factor divides 1), `rad(abc) = rad(XY)`, and the derivative/degree mechanism yields `(p−1)(q−1) < 1`, impossible for `p,q ≥ 2`. Grounded.

**abc ⇒ Catalan (folklore conditional)** — the anchor arithmetic reproduced by the proposal is sound: `a = x^p, b = −y^q, c = 1, rad(xy) ≤ xy`, and `x^p ≈ y^q` with `log y ≈ (p/q) log x` gives `p ≤ (1+ε)(1 + p/q)`; for `q ≥ 3` and `ε < 1/2` this forces `p ≤ 3`, symmetrically `q ≤ 3`. (Hand-verified here; no program run — execution tool absent from this session.) I was **unable to obtain a primary source stating "abc ⇒ Catalan" directly**: the direct query was withheld by the run's evidence policy (a query phrased to retrieve a published answer), and I did not attempt a workaround. So the transfer is recorded as **folklore/conditional, unverified-by-source**, exactly as the proposal flags it.

## Hypotheses that hold here

- Characteristic 0 function field over `C`: holds.
- Pairwise coprimality of `X^p, Y^q, 1`: holds for nonconstant solutions.
- Paucity (no constant-time derivatives issue): fine in char 0.
- **abc**: the hypothesis of the integer half is an **open conjecture**; it does *not* hold as a proved fact here. This is the correct statement of why the integer half cannot be the deliverable by itself.

## Has anyone applied this to the problem

The function-field no-solutions statement is standard folklore (e.g., cited as an elementary application of Mason's theorem in the sources above). The specific "abc ⇒ Catalan with explicit exponent bound" is classical folklore in the abc literature; I could not open a primary instance because the direct query was screened. I will not claim a specific citation for it beyond "folklore."

## What it would buy

- **Unconditional, cheap, falsifier-safe:** a complete proof that all *nonconstant* (polynomial) solutions are impossible — the exact "empty part" of the problem the integer constant `3² − 2³ = 1` occupies. This reproduces in the function-field world the *negative* structure of Catalan and survives the falsifier (it does not eliminate the constant solution).
- **Conditional (abc):** forcing `p,q ≤ 3`, i.e., reducing Catalan to fixed small exponent pairs. Real mathematical content, but requires abc, which is open.

## Verdict rationale (against Scholze's rule)

Scholze's rule: a reformulation earns its place only by covering the case where the old setting worked. The function-field half *aims past* the goal in exactly the right way — it makes the no-solutions statement the obvious corollary of a degree bound — but it is a statement about a *different category* (polynomials over `C[t]`), and it does **not** by itself reproduce the arithmetic divisibility results the old setting holds (Cassels `p|y, q|x`, the Wieferich conditions). The transfer step that would connect it to the integer problem is precisely the open abc conjecture. So this approach is best understood as **grounded for its self-contained half, speculative for the half that reaches the goal**.

## Precedent (as claim IDs / URLs)

- `https://doi.org/10.1007/s000170050074` (Snyder, Mason theorem)
- `https://doi.org/10.48550/arxiv.2408.15180` (Baek–Lee Lean formalisation)
- `https://doi.org/10.1007/s00209-020-02604-7` (Ishizaki–Korhonen–Li–Tohge, Stothers–Mason + polynomial Fermat corollary)
- `https://hal.science/hal-01626155v1/file/poster.pdf` (Mason–Stothers–Hurwitz radical bound)
- Masser–Oesterlé abc conjecture (folklore reference, 1988); no primary instance of "abc ⇒ Catalan" retrieved (screened).

## Falsifier check (`3² − 2³ = 1`)

The Mason–Stothers corollary excludes only nonconstant polynomial solutions; the integer `(3,2,2,3)` is the constant solution and is untouched. Nothing here over-eliminates.

## Decision (inventor, after research)

**status: adopted.** Chosen over Runge (refuted: the Catalan curve satisfies all of Walsh's C1–C4, so Runge's hypothesis fails; sharpness example was wrong) and over Skolem (refuted: class-splitting reproduces the double-Wieferich/Cassels conditions). This is the only one of the three with an unconditional, falsifier-safe, kernel-formalizable core, and its integer half is the precise conditional theorem GOAL.md counts.

**Why it wins.** Mason–Stothers gives, unconditionally and in three lines, that `X^p − Y^q = 1` has no *nonconstant* polynomial solution over `C[t]` — the exact "empty part" the integer constant `3² − 2³ = 1` occupies, so nothing over-eliminates. The integer half is a precise conditional theorem: abc with ε < 1/2 ⇒ every solution has min(p,q) = 2, which with the exponent-2 cases forces the known solution. The radical is the single *global* quantity that survives when every local splitting collapses.

**Synthesis — the gap between proposal and literature, which is the new idea.** Research showed Runge degenerates (single Puiseux branch, irreducible leading form) and Skolem collapses to the known congruence conditions. These are one fact: the Catalan curve is a one-branch cyclic cover, so every local-splitting method (Runge at ∞, Skolem/Strassmann at finite primes, Subspace) has no room, and the only obstruction that survives is global — the radical (abc) / the class group. The derivative mechanism `X^{p−1} | Y′` powering Mason–Stothers is exactly the function-field shadow of Cassels's divisibility `p | y, q | x`; the abc transfer is the assertion that this derivative mechanism survives over `Z` with controlled error. Adopting the transfer keeps the single genuine obstruction in view.

**First step (tool_builder, start today):**
1. `code/abc/mason_stothers.py` — sympy-verified corollary: from `X^p − Y^q = 1`, differentiate to `p X^{p−1} X′ = q Y^{q−1} Y′`, conclude `X^{p−1} | Y′`, `Y^{q−1} | X′`, hence `(p−1) deg X ≤ deg Y − 1` and `(q−1) deg Y ≤ deg X − 1`, multiply to `(p−1)(q−1) < 1` — contradiction for p,q ≥ 2. Verify the radical bound `max ≤ deg rad(abc) − 1` on explicit small nonconstant examples.
2. State the conditional theorem precisely and compute the ε-threshold: for the known solution rad(9·8·1) = rad(72) = 6, find the minimal ε with 9 ≤ 6^{1+ε} (hand check: log 9/log 6 − 1 ≈ 0.226, to be re-verified by the program); confirm the forcing of p,q ≤ 3 holds for ε ∈ (0.226, 1/2) and does not exclude the known solution (it has min(p,q)=2, consistent).
3. Re-derive Cassels `p | y, q | x` and record the exact correspondence to `X^{p−1} | Y′` as a claim block — this is the arithmetic shadow the transfer is supposed to reproduce.
4. Optional: Lean-check the corollary against Baek–Lee's Mason–Stothers formalisation (arXiv:2408.15180).
