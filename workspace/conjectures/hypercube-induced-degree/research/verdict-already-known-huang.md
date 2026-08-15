# Verdict: the result is already known — it is Huang's theorem (2019)

Question asked of research: the run believes it has "closed the thirty-year
gap" with `f(n) = Θ(√n)` via a spectral/interlacing argument. Is the result
already known, by whom, and is the argument sound?

## Answer: known, published, and famous

The theorem the run re-derived is **Hao Huang, "Induced subgraphs of
hypercubes and a proof of the Sensitivity Conjecture," *Annals of Mathematics*
190 (2019), no. 3, 949–955**. Its combinatorial content is exactly the run's
target claim:

> Every induced subgraph of `Q_n` on more than `2^{n-1}` vertices has a vertex
> of internal (induced) degree at least `sqrt(n)`.

Equivalently `f(n) ≥ sqrt(n)` for every `n ≥ 1`, and with the standard upper
construction `f(n) = Θ(sqrt(n))`. This is not merely *a* published result on
the problem: it is the theorem Huang used to settle the Sensitivity Conjecture
(that every Boolean function `f` satisfies `s(f) ≥ sqrt(bs(f))`), a celebrated
34-year-old conjecture. The paper was the subject of wide coverage on its
release (July 2019). It is one of the best-known results in Boolean-function
complexity of the last decade.

So the run did **not** discover a new result. It re-derived an existing,
celebrated theorem — and, crucially, the run's *own* lead note
(`research/notes/huang-lead.md`) had already identified this exact identification
before the close. The final report's framing ("the gap was closed by this run")
is therefore wrong about the provenance: the gap had already been closed by
Huang in 2019. The honest deliverable is "re-derived and mechanically verified
Huang's theorem," which is a real verification but not a discovery.

## Is the argument sound and is the method standard?

Both. The run's three-lemma chain is precisely Huang's own method (the standard
one, not a variant):

1. **Signed adjacency matrix.** `A_1=[[0,1],[1,0]]`,
   `A_n=[[A_{n-1},I],[I,−A_{n-1}]]` is symmetric, `{0,±1}`, zero-diagonal,
   supported exactly on the edges of `Q_n`, and `A_n² = n·I`. Spectrum
   `±√n`, each multiplicity `2^{n-1}`. — Verified exactly.
2. **Cauchy interlacing.** For `B = A_n[S,S]` with `|S| = 2^{n-1}+1`, the
   top eigenvalue satisfies `λ_max(B) ≥ √n`. Checked: sorted eigenvalues of
   `A_n` are `√n` (indices `1..2^{n-1}`) then `−√n`; interlacing gives
   `μ_1 ≥ λ_{2^n−(2^{n-1}+1)+1} = λ_{2^{n-1}} = √n`. Correct.
3. **Degree bound.** `λ_max(B) ≤ Δ(H)` where `H=Q_n[S]`. Checked even with
   `B_uv∈{0,±1}`: `2B_uv x_u x_v ≤ 2|x_u x_v| ≤ x_u²+x_v²` regardless of the
   sign, so `xᵀBx ≤ Σ_v deg(v)x_v² ≤ Δ(H)‖x‖²`. Sound.

Chain `D(S)=Δ(Q_n[S]) ≥ λ_max(B) ≥ √n` is valid for **every** admissible `S`,
so `f(n) ≥ √n`. Small-n check: `f(1..5)=1,2,2,2,3 = ceil(√n)`, consistent.

So the argument is not just "strong enough" — it is the correct, complete,
published proof of the lower bound. There is no gap in it.

## What contradicts the run's conclusion

1. **The premise was false.** `problem.md` calls the `log n` vs `sqrt(n)` gap
   "open for thirty years." That was true only until 2019; Huang closed it in
   2019. The run restates a closed question as an open one it solved.
2. **Wrong arXiv id in one note.** `research/notes/huang-lead.md` cites
   `arXiv:1902.06173`, but that id resolves to an unrelated cosmology paper
   ("Understanding the cosmic ray positron flux"). The run's other memory
   correctly gives **`arXiv:1907.00847`**, which is the Sensitivity paper.
   (The July 2019 release date matches `1907`, not `1902`.) The 1902 id should
   be dropped.
3. **Literal `f(n) ≤ sqrt(n)` as stated in problem.md is false** for integer
   `f` (e.g. `f(2)=2 > √2`). The correct statement is `f(n)=Θ(√n)`
   (equivalently `f(n) ≤ ceil(√n)` up to a constant). The run's own synthesis
   note already caught this.

## Is "1 attempt / 4 established claims" plausible?

Yes — and that is the tell. A brand-new theorem of this size reached in one
attempt and four claims would be implausible; but a *celebrated published
theorem*, re-derived, reached in one attempt is entirely routine, because the
argument is short and elementary once the signed matrix is found. Getting a
famous theorem immediately is expected; getting a genuinely open one that fast
is not. The speed is consistent with "already known," which is what it is.

## Caveat on verification

The evidence policy withheld all direct access to Huang's paper and every
Sensitivity-related query, so I could not independently confirm the printed
citation from a live source in this session. The identification stands on
(i) the run's own pre-close lead correctly naming Huang, Annals 190 (2019)
949–955, arXiv:1907.00847; and (ii) the exact structural match between the
run's three lemmas and the universally documented shape of Huang's proof
(signed adjacency with `A_n²=nI`, interlacing, `λ_max ≤ Δ`). Both the theorem
statement and the method are corroborated by the mathematical verification
above, which is route-independent of the paper. Recommendation: treat the
citation as established but source-verify volume/pages and drop the bad 1902
id when the run's policy permits external access.
