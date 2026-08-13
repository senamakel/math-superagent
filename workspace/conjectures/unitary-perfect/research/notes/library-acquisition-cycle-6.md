# Library acquisition cycle 6 — reconfirmation of blocked rows; no new downloads

## What this cycle did

The library phase is closed (directive 8): the frontier's multi-cited rows are all
held. This cycle re-attempted the only two open REQUESTS rows with real content
value — **Frei 1978** and **Goto 2007** — using fresh multi-formulation searches
(`exa_search`, several distinct phrasings for each), not just re-hitting the
previously-failed endpoints. Both remain blocked. Nothing new was downloaded.

## Results

| Request | Fresh search outcome | Verdict |
| --- | --- | --- |
| **Frei 1978**, *On unitary perfect numbers*, Elem. Math. 33 (1978) 95–96 | Only hits are OEIS A002827 recording the theorem (Amiram Eldar 2019 comment: UPN not divisible by 3 ⇒ `2^m\|n`, `m ≥ 144`, `ω ≥ 144`, `n > 10^440`), the MaRDI bibliographic item Q1247995, and unrelated 1978 papers. e-periodica remains captcha-walled at `pid=edm-001:1978:33::216`; no alternate full-text host surfaced. | **Still OPEN.** OEIS comment remains the only record; the theorem is load-bearing for "is 3 \| n forced?" but cannot be verified against primary. |
| **Goto 2007** (with K. Okeya), RMJM 37(5):1557–1576, DOI 10.1216/rmjm/1194275935 | Paywalled at Project Euclid; **no free preprint** anywhere (no Zenodo / CiNii / Kyushu-repository copy; Goto's TUAT page `ma.noda.tus.ac.jp/u/tg` lists the paper but gives no PDF link). MaRDI item Q2478044 records the result: UPN with k distinct prime factors ⇒ `N < 2^(2^k)`; UHN ⇒ `N < (2^(2^k))^k`. | **Still OPEN** for primary; the bound itself is already captured in the library via MaRDI (claim `goto2007-upper-bound-upn-2-2^k`). Low marginal value — it is a finiteness-adjacent counting bound, not a constraint on `H_even`. |
| **Subbarao–Cook–Newberry–Weber 1972**, Delta 3(1):22–26 | Not re-attempted: ualberta scan has no text layer; low-value seed note. | **OBSTRUCTED** (as recorded). |

## Independent confirmation of the run's premise

Fresh searches for a **divisor-level residue-class distribution theorem for
primitive prime divisors of `Φ_{4p}(2)`** returned nothing on target. The only
classical adjacent hit is Schinzel, *On primitive prime factors of `a^n − b^n`*
(paywalled); the cyclotomic-coefficient-distribution papers that surface (Gallot–
Moree–Hommersom; Beiter/Kloosterman threads) study coefficients of `Φ_n`, not
residue classes of its prime divisors. This is consistent with Maciejewski
arXiv:2605.20475's stated claim (paper §5.3) that the missing
divisor-transference / (H1)(H2) theorem does not exist in the literature — the
gap the run's adopted `second-moment-character-mod16` approach targets with
quartic reciprocity + Dirichlet orthogonality.

## Bearing on REQUESTS.md

No row changes status except re-confirmation. Both open content rows are kept
**OPEN** (do not re-attempt the same endpoints; a future fetch of either needs a
genuinely new host). The rest of the library is unchanged and comprehensive.

## Library shape

Unchanged from cycle 5: origin/definition, canonical head (Subbarao–Warren 1966,
Wall 1975, Graham 1989, Wall 1987/1988), branch target (Maciejewski full text),
analytic machinery (BGH 2022, Hong 2022, Ford 2014, FKL 2010, BHV 2001), divisor-
class neighbours, quartic reciprocity (Williams 1976 primary), lookups (Cunningham
2± tables + Appendix C, OEIS A002827/A057447), context (Guy, Handbook, EoM).
