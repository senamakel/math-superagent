# Cunningham Appendix C — Composite Cofactors of b^n ± 1 (incl. the 2^n+1 / 2^nL,M side)

Full text: [[cunningham-appendix-c-2n-plus-1.full]]
Source: https://homes.cerias.purdue.edu/~ssw/cun/third/appc901 (Third Edition, September 2001 vintage)

## What it is

Appendix C lists the **unfactored composite cofactors** of `b^n ± 1` across
bases `b = 2,3,5,6,7,10,11,12`. Entries are of the form
`n  b, <exp><type>  <cofactor>` where type is `-` (`b^n−1`), `+` (`b^n+1`),
`L` (the Aurifeuillean lower `L` factor of `2^(4k+2)+1`), or `M` (the
Aurifeuillean upper factor). The cofactor is the still-composite part after
small algebraic and prime factors are removed. There are ~2,500 such cofactors,
mostly in the 100–200 digit range for the held portion.

## What it establishes for this run

- This is the first held Cunningham source that covers the **`+1` / Aurifeuillean
  `L,M` side** — the previous `pmain126`/`pmain901` were `2^n−1` (Table 2−) only.
  The "Appendix C not held" gap recorded in claim `cunningham-2n-minus-1-lookup`
  is now closed: the `+1`-side composite-cofactor tables are in the library.
- Concrete `2^n+1` and `2^{4k+2}+1` (Aurifeuillean `L,M`) cofactor data for
  exponents roughly in the 100s–1000s (2001 vintage): e.g. `2,1131+`,
  `2,984+`, `2,1462M`, `2,1534M`, `2,1318M`, `2,1610L`, `2,1782L`, `2,1025-`,
  `2,1342M`. These are the unfactored composites of those numbers.

## What it does NOT do — HONEST limits

- **The open H_even branch is not reachable from this file.** The open
  candidates are `m = 2p` with `p ∈ [1213, 17467]`, i.e. exponents `n = 2p` up
  to ~35000 — orders of magnitude beyond this 2001 vintage Appendix C (exponents
  in the 100s–1000s). And by definition the ones in Appendix C are *still
  unfactored* composites, so they carry no complete divisor set.
- So it cannot directly verify any H_even element or any open candidate. Its
  use is as *known-composite-cofactor* data for testing the mod-16 / v2 profile
  of the `+1` side on **smaller** even exponents — a structural check, not a
  branch-closer.

```claim
id: cunningham-appc-2n-plus-1-cofactors-held
statement: Cunningham Appendix C (third edition, 2001) gives composite
  cofactors of b^n +/- 1 including the 2^n + 1 and 2^(4k+2)+1 Aurifeuillean
  L/M side, for exponents roughly in the hundreds-to-thousands. This closes
  the earlier 'Appendix C not held' gap. It does NOT cover the open H_even
  candidates (exponents up to ~35000) and lists only unfactored composites,
  so it cannot verify H_even membership or resolve any open candidate.
hypotheses: the file appc901 is Appendix C as of Sep 2001
holds-here: partial -- +1 side data now held, but not at the H_even candidate
  scale and only as unfactored composites
status: catalogued
bearing: closes the +1-side table gap; provides small/moderate even-n cofactor
  data for structural (v2/mod-16) checks, not branch closure
anchor: research/sources/cunningham-appendix-c-2n-plus-1.full.md
```
