# LEAD — 2026 public critique claiming a counterexample to Lemma 5.4 of Ghosh arXiv:2402.18717v3

Status: **THIRD-HAND, UNVERIFIED LEAD — record so nobody cites it as established.**
Provenance chain resolved this cycle: the critique text originates in a
social-media post by user "sensho" (tweetlook.com/sensho, quoting "a little
fable-driven math psychosis…"), and was copied verbatim by a Digg tech-news
item dated 2026-07-22 (`https://digg.com/tech/4yiyu023`). Contemporaneous 2026
context (e.g. the unsolved-math-100 GitHub repo) references "Claude Fable 5" as
**an AI model name** — the same week saw an AI-assisted announcement of a
Jacobian-conjecture counterexample — so the "fable" who "found" the Lemma 5.4
obstruction is reported to be an AI model's output, **not a named
mathematician**. No mathematician has vouched for it; no arXiv note, no
follow-up; no response from Ghosh. Treat the content below as
**reported-hearsay**, each claim to be checked exactly against the held source
text before any use.

## What the critique reportedly claims

- The newer 2026 Ghosh claim (arXiv:2501.09272v2) builds on the earlier
  arXiv:2402.18717v3 ("A finiteness result towards the Casas-Alvero
  conjecture"), and the critique claims a **counterexample to a core lemma,
  Lemma 5.4 of 2402.18717v3**.
- Reported counterexample: `Q = h₂·F₁ − T·h₁·F₂` with n=5, i=3,
  (j₁,j₂,jᵢ) = (1,2,5); deg_T(Q) = 3 and
  `[T³]Q(1,1,1,−1/3) = −13/9 ≠ 0`.
- The Digg item itself concedes this "does not fully disprove the conjecture"
  — the target is the lemma, not CA.

## What the held library actually contains (verified this cycle)

- Lemma 5.4 in full, verbatim, at
  `research/sources/ghosh2024_finiteness_html.full.md` lines 578–636
  (statement ~578, proof 580–636): the `≺_T` monomial partial order on
  `R = K[x_1,…,x_{n−1},T]` ordered by T-degree, `Dom(f)` = sum of maximal
  monomials, and the claim that for any nonzero R-linear combination
  `Σ_{j∈S} c_j F_j` there exist `c̃_j` with equality of the combination and
  `Dom(Σ c_j F_j) = Dom(Σ Dom(c̃_j) Dom(F_j))`. Its proof (5.3)-(5.4) uses the
  regular-sequence property of the h_j and skew-symmetric r^1_{jl}.
- The lemma's use later in the paper: it drives the non-zero-divisor argument
  for h_i in `R/(F_1,…,F_{i-1})` (5.5–5.13) and is the load-bearing step of
  Prop 5.3 (the regular-sequence property of the H_l), which in turn is the
  engine of the finiteness theorem of 2402.18717.
- The claimed proof arXiv:2501.09272v2 (full text held at
  `research/sources/ghosh2025_proof_html.full.md`) cites 2402.18717 and its
  framework, so a genuine failure of Lemma 5.4 would propagate.

## What would settle this lead (each is a separate task for the run)

1. **Exact check (tool_builder):** instantiate the reported Q and the lemma's
   setup in sympy/PARI over Q with n=5, i=3, (j₁,j₂,jᵢ)=(1,2,5), compute
   deg_T(Q) and the T³ coefficient at (1,1,1,−1/3), and — more decisively —
   run the lemma's conclusion search: does there exist c̃₁,c̃₂ with
   `Q = c̃₁F₁ + c̃₂F₂` and the Dom identity, or is the reported obstruction
   real? Also test whether the lemma's *proof step* (5.3) fails for this Q.
2. **Find the original thread** (the Digg item's source) — librarian or
   research, via the Digg page and the phrase "fable Casas-Alvero". If the
   original comment is reachable, record whose claim it is and whether any
   mathematician engaged.
3. **Watch for a Ghosh response** — if Ghosh addresses it (arXiv revision,
   v4 of 2402.18717 or a v3 of 2501.09272), the status claim
   `ca-status-2025` / `ghosh-v2-version-record` must be updated.

## Recorded claims this does NOT change yet

None of the 8 held claims bearing on the Ghosh status
(`ca-status-2025`, `ghosh-v2-version-record`, `ghosh-char0-break-4-18`,
`ghosh-finiteness`, `ghosh-dim-bound`, `ghosh-complete-intersection`,
`dobrowolski-2017-withdrawn`, `battiston-withdrawn`) is falsified by a
third-hand report. If the exact check (item 1) confirms the obstruction, the
new fact is: *the foundation paper of the claimed proof has a documented
counterexample to a core lemma* — which would move the Ghosh claim from
"unverified preprint" to the same class as Battiston/Dobrowolski (gap found),
and GOAL.md's priority question would have a concrete new answer. Until then:
CA open, Ghosh unverified, this lead unverified.