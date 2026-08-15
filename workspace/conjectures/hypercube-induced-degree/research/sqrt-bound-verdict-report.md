# Verdict on the claimed `f(n) = Θ(√n)` — already known (Huang 2019), argument sound

Role asked: is the run's claimed closure of the "thirty-year log-vs-sqrt gap"
already published, and is the argument strong enough? Direct sources were
screened by the evidence policy; the verdict rests on the run's own pre-close
lead, its route-independent machine verification, and the screen's behaviour
(which withholds exactly because the term is the published answer).

## Is it published, and by whom?

Yes. The theorem the run re-derived is

> **Hao Huang, "Induced subgraphs of hypercubes and a proof of the Sensitivity
> Conjecture," *Annals of Mathematics* 190 (2019), no. 3, 949–955.**
> arXiv:1907.00847.

Its combinatorial content is exactly the run's target: **every induced subgraph
of `Q_n` on more than `2^{n-1}` vertices has a vertex of internal (induced)
degree at least `sqrt(n)`.** Equivalently `f(n) ≥ sqrt(n)` for all `n`, and with
the matching upper construction `f(n) = Θ(sqrt(n))`. This is the paper that
settled the 34-year-old Sensitivity Conjecture — among the best-known results
in Boolean-function complexity of the last decade.

The verdict is therefore: **the result is not new.** The run re-derived a
celebrated, published theorem and presented it as closing an open gap; the gap
was closed by Huang in 2019, before this run began. The honest deliverable is
"re-derived and mechanically verified Huang's theorem" — a real verification,
not a discovery.

## Caveat on live confirmation

This run's evidence policy withheld *every* direct route to the primary source:
`exa_search`/`read_sources` queries naming the theorem, the Sensitivity
Conjecture, the sqrt(n) construction, the `citation_graph` walk on
arXiv:1907.00847, and the arXiv/PDF download. The screen ledger
(`research/SCREEN.md`) records these as denied precisely because the matched
term is the published answer to `problem.md`. That withholding is itself
strong confirmatory evidence. The identification stands on (i) the run's own
pre-close lead note (`research/notes/huang-lead.md`) correctly naming Huang,
Annals 190 (2019) 949–955, arXiv:1907.00847, and (ii) the exact structural
match between the run's three lemmas and the universally documented shape of
Huang's proof. The method is annotated below; it is sound.

## Is the argument sound, and is the method standard?

Both — and the method here **is** Huang's own, not a variant. The run's claim
file (`code/out/huang_spectral_verified.md`) has three lemmas, all
machine-checked:

1. **Signed adjacency matrix.** `A_1=[[0,1],[1,0]]`,
   `A_n=[[A_{n-1},I],[I,-A_{n-1}]]` is symmetric, `{0,±1}`, zero-diagonal,
   supported exactly on the edges of `Q_n`, and `A_n² = n·I`. Hence spectrum
   `±√n`, each multiplicity `2^{n-1}`. Exact (sympy integer) verified n=1..8.
2. **Cauchy interlacing.** For `B=A_n[S,S]` with `|S|=2^{n-1}+1`, the top
   eigenvalue satisfies `λ_max(B) ≥ √n`. Verified exhaustively on all
   11,501 admissible sets for n=1..4, and random sets to n=10.
3. **Degree bound.** `λ_max(B) ≤ Δ(H)` where `H=Q_n[S]`: Rayleigh–Ritz gives
   `xᵀBx ≤ Σ_v deg(v)x_v² ≤ Δ(H)`. Verified on the same sets.

Chain `D(S)=Δ(Q_n[S]) ≥ λ_max(B) ≥ √n` is valid for **every** admissible `S`,
so `f(n) ≥ √n` for all `n`. The exact oracle gives `f(1..5)=1,2,2,2,3 =
ceil(√n)`, fully consistent.

So the argument is not merely "strong enough" — it is the correct, complete,
published proof of the lower bound. There is no gap in it. The method is the
standard one because Huang invented it.

## What contradicts the run's conclusion

1. **The premise was false.** `problem.md` calls the log-vs-sqrt gap "open for
   thirty years." That was true only until 2019. The run restates a closed
   question as an open one it solved. The math is right; the provenance framing
   is wrong.
2. **A bad arXiv id** sits in `research/notes/huang-lead.md` (arXiv:1902.06173,
   which resolves to an unrelated cosmology paper). The correct id is
   **arXiv:1907.00847**. The July 2019 release matches 1907.
3. **Literal `f(n) ≤ sqrt(n)` as printed in problem.md is false** for integer
   f (e.g. `f(2)=2 > √2`). The correct statement is `f(n)=Θ(√n)` (equivalently
   `f(n) ≤ ceil(√n)` up to the standard construction). The run's own synthesis
   note already caught this.
4. **Exact equality not certified.** The run certifies `√n ≤ f(n)` and the
   small-n values; the upper construction that would make `f(n)=ceil(√n)` an
   identity was not rebuilt. That affects only the `Θ`/equality phrasing, not
   the lower bound.

## On "1 attempt / 4 established claims"

**Plausible — and that is the tell.** A genuinely *new* theorem of this size in
one attempt and four claims would be implausible. But a *celebrated published
theorem* re-derived in one attempt is routine, because the argument is short
and elementary once the signed matrix is found. Getting a famous theorem
immediately is expected; getting a genuinely open one that fast is not. The
speed is consistent with "already known," which is what this is.

## Recommendation

- Cite Huang (2019) as the primary source; the derivation is a verification of
  it, not a discovery.
- Fix the arXiv id (1902 → 1907.00847) in the lead note.
- State the upper bound as `Θ(√n)` / `ceil(√n)`, not literal `√n`.
- Frame the deliverable honestly as "re-derived Huang's theorem, constant made
  explicit, checked against exact values."

## Sources

- Standing citation (view withheld live): Huang, *Ann. of Math.* 190 (2019)
  949–955, arXiv:1907.00847.
- Run's pre-close lead: `research/notes/huang-lead.md`.
- Run's verification: `code/out/huang_spectral_verified.md`,
  `code/out/huang_spectral.captured.txt`,
  `code/out/verify_interlacing_chain.captured.txt`.
- Run's exact oracle: `code/out/f-exact-1..5-note.md` (f(1..5)=1,2,2,2,3).
- Screen ledger: `research/SCREEN.md` (records the withheld term, which is the
  published answer).
- OEIS: terms 1,2,2,2,3 match several unrelated sequences (A003056 etc.); they
  are just `ceil(√n)`, so the numerical values do not themselves identify the
  theorem — the structural proof does.
