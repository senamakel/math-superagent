# The Gilbreath-polynomial route (Gatti 2023; author confirmed)

> Authored by **Riccardo Gatti** (INBB / Eldor Lab, Bologna). The library's
> earlier claim `gilbreath-polynomials-imply-gc` said "Alkan et al.? — authors
> not confirmed". The author **is Riccardo Gatti** (confirmed from the MDPI
> article page, the Preprints.org title and multiple search digests).

## Status of the claim

**UPDATED (librarian 2026): direct page text now captured.** The PDF endpoint
still 403s, but the article page text was obtained via the library `read_sources`
route (`gatti-2023-gilbreath-polynomials-mdpi.captured.md`), so the claim is no
longer "sourced-by-search-digest only": the full definitional chain (G_n
criterion, max K / min K, Gilbreath polynomials, Equation (6)) and the author's
own concession are on record. **The claim itself is unchanged in strength**:
the implication `p_n − 2^{n−1} ≤ P_{n−1}(1) ⟹ GC_n` reduces to
`p_n ≤ max K(p_1..p_{n−1})`, which is exactly Gatti's Theorem 4 from the 2020
preprint — already refuted here as an invalid proof (`gatti-2020-theorem4-proof-invalid`),
and the MDPI paper itself concedes "bounds for p_n are not good enough to
prove (7)". The 403 endpoints (MDPI page+PDF, Preprints v4) are still recorded
as stubborn; no arXiv mirror is known.

What the digest (two independent searches) does establish, reliably:

- The main theorem: "GC is implied by `p_n − 2^{n−1} ⩽ P_{n−1}(1)`, where
  `P_{n−1}(1)` is the (n−1)-th Gilbreath polynomial at 1", with the polynomial
  built from the first n primes via `u_n = 2^{m+n−1} + P_m(n)`.
- A finite sequence S is a *Gilbreath sequence* iff `s_1` has one parity and
  `s_2..s_n` the other, and `min K(s_1..s_m) ≤ s_{m+1} ≤ max K(s_1..s_m)` for all m.
- `max K_S = s_1·(n−1)! + s_2·(n−2)! + ... + s_n·0! + 1` and `min K_S = 2s_n − max K_S`
  (weighted-factorial bounds).
- Two OEIS sequences: A347924 (Gilbreath polynomial coefficients, triangle by
  rows) and A347925 (denominators).
- Author affiliation: National Laboratory of Molecular Biology and Stem Cell
  Engineering, INBB c/o Eldor Lab, Bologna — a biology lab, not an academic
  number theory group. Note this is a single-author preprint-to-MDPI pipeline
  (v1 2020-03-08 on Preprints.org → MDPI Mathematics 2023 11(18) 4006, both by
  Gatti), so treat the peer-review status lightly: MDPI *Mathematics* is a
  peer-reviewed journal, but the claim has not been checked here.

## Bearing on this run

A genuinely different-looking handle: instead of tracking `{0,2}` blocks, the
route asks whether `p_n − 2^{n−1}` is bounded by a polynomial in the primes.
If the bound were proved it would settle GC by itself, but it is **not proved
here and not confirmed to be proved in the paper** (the digest does not present
a proof). The `P_{n−1}(1)` quantity grows like a factorial-ish object
(`max K_S` contains `(n−1)!·s_1`), so the inequality `p_n − 2^{n−1} ⩽ P_{n−1}(1)`
is trivially true in practice for large n — the question is whether the paper's
derivation has teeth.

**Do not cite the MDPI paper for anything beyond its abstract-level claim until
a full text is obtained.** It is a second route to have on file if the block
route stalls, not a result to build on.

## What would falsify / confirm the approach

- Falsify: if `p_n − 2^{n−1} > P_{n−1}(1)` for some n where GC holds (easy to
  test numerically once the polynomial is implemented) — the "implication" would
  be vacuous in the range where its hypothesis fails.
- Confirm: obtaining the full text and checking the proof of the inequality's
  sufficiency.