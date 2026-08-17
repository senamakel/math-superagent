> **Encyclopedic context — the Happy Ending problem and its taxonomy.**

# Wikipedia — Happy Ending problem

> **Source:** `https://en.wikipedia.org/wiki/Happy_ending_problem` (full text at `research/sources/wikipedia-happy-ending-problem.full.md`). **Encyclopedic context only** — every statement here is secondary and must defer to the primary sources (Erdős–Szekeres 1935/1961, Tóth–Valtr, Suk, Peters–Szekeres) this library holds. Verified against the library's primary claims: consistent.

## What it establishes (encyclopedic, consistent with primaries)

- **The theorem and the name.** Any 5 points in general position contain 4 in convex position; and for any N, sufficiently large sets contain N in convex position (the ES finiteness theorem). The "happy ending" name: Klein–Szekeres marriage.
- **Convention.** General position = no two coincide, no three collinear. Same as this run's convention.
- **Small values** (matches the library's `es-exact-values` claim): ES(3)=3, ES(4)=5 (Klein), ES(5)=9 (Turán/Makai/Kalbfleisch et al.), ES(6)=17 (Peters–Szekeres 2006). ES(7) conjectured 33, open.
- **Lower/upper bounds.** $2^{n-2}+1 \le \mathrm{ES}(n) \le \binom{2n-4}{n-2}+1$; Suk $2^{n+o(n)}$; best HMPT $2^{n+O(\sqrt{n\log n})}$. All confirmed against the primaries in [[morris-soltan - The Erdos-Szekeres problem on points in convex position - survey BAMS 2000]].
- **Adjacent taxonomy** (the drift-guard value of this page):
  - **Empty convex polygons / Erdős–Szekeres–Horton problem**: convex n-gon with no point inside. $h(5)=10$, $h(6)=30$, $h(n)$ does not exist for n≥7 (Horton; the library's newly-digested `horton-no-empty-7gon`). _Not_ the ES(n) conjecture.
  - **Higher dimensions / k-holes**: Scheucher's $g^{(d)}$ (library `scheucher-sat`, adjacent).

## Bearing

This is the fastest single pointer for the exact values, the bound chain, and the
empty-side taxonomy — useful for GOAL's small-value criterion and for keeping the
empty-hexagon/k-hole results out of the planar ES(n) claim. It adds nothing the
primaries do not establish more reliably; cite it as context, never as proof.

```claim
id: wiki-happy-ending-small-values
statement: (encyclopedic) ES(3)=3, ES(4)=5, ES(5)=9, ES(6)=17; ES(7) conjectured 33, open; bounds 2^{n-2}+1 <= ES(n) <= C(2n-4,n-2)+1, with Suk and HMPT asymptotic improvements; empty-convex-n-gon number h(n) exists only for n<=6 with h(5)=10, h(6)=30.
hypotheses: general position (no two coincide, no three collinear).
holds-here: yes — consistent with this run's primary-backed exact-values and Horton/empty-hexagon claims.
status: catalogued (encyclopedic digest; each value is primary-backed elsewhere in the library).
bearing: single-pointer reference for exact values and the adjacent-problem taxonomy; drift guard against reporting empty-hexagon/k-hole numbers as ES progress.
anchor: research/summaries/wikipedia-happy-ending-problem.md
follows-from: es-exact-values, es61-lower-bound, horton-no-empty-7gon, heule-scheucher-empty6
```
