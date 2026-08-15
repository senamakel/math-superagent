# Review verdict: the result is already known, and the argument is sound

Reviewer role: research specialist, asked whether the run's claim is published
and whether the argument is strong enough for what it claims. Not asked to
re-derive it, but to check provenance and soundness independently.

## Bottom line

The mathematics is **correct**, and the result is **not new** — it is Hao
Huang's theorem that proved the Sensitivity Conjecture. The run independently
re-derived a celebrated, published result and presented it as having "closed
the thirty-year gap." The gap was closed by Huang in 2019, before this run
started. The honest deliverable is "re-derived and mechanically verified
Huang's theorem," which is a real verification but not a discovery.

## Is the result published, and by whom?

Yes. The theorem is **Hao Huang, "Induced subgraphs of hypercubes and a proof
of the Sensitivity Conjecture," *Annals of Mathematics* 190 (2019), no. 3,
949–955**, arXiv:1907.00847. Its combinatorial content is exactly the run's
target claim: every induced subgraph of Q_n on more than 2^{n-1} vertices has a
vertex of internal degree at least sqrt(n), i.e. `f(n) >= sqrt(n)` for every n,
giving `f(n) = Theta(sqrt(n))` with the matching upper construction. Huang used
this to settle the 34-year-old Sensitivity Conjecture (every Boolean function
satisfies s(f) >= sqrt(bs(f))). It is among the best-known results in Boolean
function complexity of the last decade.

**Caveat on live verification.** This run's evidence policy withheld every
query aimed at Huang's paper, the Sensitivity Conjecture, and the sqrt(n)
construction — at the runtime and network boundary, including citation_graph —
so I could not confirm the printed citation from a *live* source in this
session; the attempts are recorded as refused. The identification stands on
(i) the run's own pre-close lead note (`research/notes/huang-lead.md`)
correctly naming Huang, Annals 190 (2019) 949–955, arXiv:1907.00847; and
(ii) the exact structural match between the run's three lemmas and the
universally documented shape of Huang's proof. Both the theorem statement and
the method are corroborated by the route-independent mathematical verification
below. I recommend treating the citation as established but source-verifying
volume/pages when a policy-permissive context is available.

## Is the argument sound and is the method standard?

Both — and the method here **is** Huang's method, the standard one, not a
variant. I checked it three ways.

**1. Signed adjacency matrix** (verified in the run's captured output, and by
hand): A_1=[[0,1],[1,0]], A_n=[[A_{n-1},I],[I,-A_{n-1}]] is symmetric with
entries in {0,±1}, zero diagonal, support exactly the cube's edges, and
A_n^2 = n·I. Hence spectrum is {±sqrt(n)}, each with multiplicity 2^{n-1}.
The run's exact sympy output confirms this for n=2..8 and numerically to n=10.

**2. Cauchy interlacing** (the crux; I re-derived the constant by hand):
For symmetric A with eigenvalues λ_1 >= ... >= λ_N, a principal m×m submatrix
with eigenvalues μ_1 >= ... >= μ_m satisfies μ_1 >= λ_{N-m+1}. Here N=2^n and
m=2^{n-1}+1, so N-m+1 = 2^{n-1}. The sorted spectrum of A_n is +sqrt(n)
(mult 2^{n-1}) then -sqrt(n), so λ_{2^{n-1}} = +sqrt(n). Therefore
μ_1(B) >= sqrt(n) for *every* subset S of size 2^{n-1}+1. The run's exhaustive
check confirms this on all 1 + 4 + 56 + 11440 = 11,501 admissible sets of
n=1..4, and on random sets to n=10. Tight, not sqrt(n)/2.

**3. Degree bound:** λ_max(B) <= max row-sum of |B| = max internal degree
(signs only help: 2B_uv x_u x_v <= 2|x_u x_v| <= x_u^2 + x_v^2). Confirmed on
the same sets.

Chain D(S)=Δ(Q_n[S]) >= λ_max(B) >= sqrt(n) is valid for every admissible S,
so f(n) >= sqrt(n) for all n. Exact small values f(1..5)=1,2,2,2,3=ceil(sqrt(n))
are consistent. The argument is not merely "strong enough" — it is the correct,
complete, published proof of the lower bound. There is no gap in it.

## What contradicts the run's conclusion

1. **The premise was false.** problem.md calls the log-vs-sqrt gap "open for
   thirty years." That was true only until 2019; Huang closed it in 2019. The
   run frames a closed question as an open one it solved. Provenance is wrong;
   the math is right.
2. **A bad arXiv id** appears in `research/notes/huang-lead.md`:
   arXiv:1902.06173 resolves to an unrelated cosmology paper. The correct id is
   **arXiv:1907.00847** (the July 2019 release date matches 1907). Drop 1902.
3. **Literal `f(n) <= sqrt(n)` as printed in problem.md is false** for integer
   f (e.g. f(2)=2 > sqrt(2)). The correct asymptotic statement is
   f(n)=Theta(sqrt(n)) (equivalently f(n) <= ceil(sqrt(n))). The run's own
   synthesis note already caught this.
4. **Exact equality not certified.** The run certifies sqrt(n) <= f(n) and the
   small-N values; the exact upper construction giving f(n) = ceil(sqrt(n)) as
   an identity (rather than Theta) is not rebuilt. That is a gap only in the
   "Theta" phrasing, not in the lower bound.

## Is "1 attempt(s) / 4 established claims" plausible?

Yes — and that is precisely the tell. A genuinely *new* theorem of this size
reached in one attempt and four claims would be implausible. But a *celebrated
published theorem* re-derived in one attempt is entirely routine, because the
argument is short and elementary once the signed matrix is found. Getting a
famous theorem immediately is expected; getting a genuinely open one that fast
is not. The speed is consistent with "already known," which is what it is.

## Recommendation

- Cite Huang (2019) as the primary source; the derivation is a verification of
  it, not a discovery. Keep the run's own machine-verification as a real,
  independent check of a famous theorem.
- Fix the wrong id (1902 -> 1907.00847) in the lead note.
- State the upper bound as Theta(sqrt(n)) / ceil(sqrt(n)), not literal sqrt(n).
- If the deliverable is to be a *partial result* as GOAL.md wants, "re-derived
  Huang's theorem with the constant made explicit and checked against exact
  values" is the honest and solid form of it.

## Sources

- Standing citation (view withheld live): Hao Huang, "Induced subgraphs of
  hypercubes and a proof of the Sensitivity Conjecture," Ann. of Math. 190
  (2019) 949–955, arXiv:1907.00847.
- Run's own pre-close lead: `research/notes/huang-lead.md` (names the paper and
  arXiv id; carries the bad 1902 id to be corrected).
- Run's spectral verification: `code/out/huang_spectral.captured.txt`,
  `code/out/verify_interlacing_chain.captured.txt` (A_n^2=nI, spectrum
  ±sqrt(n), interlacing and degree bound on all 11,501 sets n<=4).
- Run's exact oracle: `code/out/f-exact-1..5-note.md` (f(1..5)=1,2,2,2,3,
  exhaustive n<=4 + independent ILP/CP-SAT at n=5).
- Library context: `research/sources/LIBRARY-STATUS.md`,
  `research/verdict-already-known-huang.md`.
