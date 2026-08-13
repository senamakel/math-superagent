# David–Philippon IMRP 2007 (rpm006) — acquisition status

[[david-philippon-minorations-puissances-courbes-elliptiques-2007]]

Target: S. David, P. Philippon, "Minorations des hauteurs normalisées des
sous-variétés des puissances des courbes elliptiques", Int. Math. Res. Pap.
IMRP 2007, no. 3, Art. ID rpm006, 113 pp. (French). DOI 10.1093/imrp/rpm006.
This is the unique explicit-constant uniform-ML result of the right shape
(powers of a single elliptic curve) — the subject of open request
`dp07-explicit-constant-for-e3-ap`.

## Acquisition status: NOT OBTAINED — paywalled (all routes 403)

Attempted and failed this cycle (each verified as a *different* failure of the
same paywall, so the record stands):

1. `https://doi.org/10.1093/imrp/rpm006` → redirects to academic.oup.com article
   lookup, HTTP 403 Forbidden.
2. Direct OUP PDF `https://academic.oup.com/imrp/article-pdf/doi/10.1093/imrp/rpm006/21847128/rpm006.pdf`
   → 403.
3. No arXiv version exists (searched; David–Philippon papers of this era are
   not on arXiv — confirmed by the absence from arXiv search and by every
   bibliography citing only the IMRP version).
4. HAL API exact-title query returns zero hits; HAL does not hold it. Philippon's
   Jussieu profile is a stub with no papers.

Likely the publisher simply does not serve the file to automated/non-subscribed
clients; institutional access would be needed. zbMATH 5238017; MR 2355454.

## What the library has instead (the DP07-adjacent tier, all on disk)

- **Galateau 2016 habilitation** (`hal-thesis-minorations-hauteurs-puissances-courbes-elliptiques`)
  — primary-authored survey of Lehmer-type/effective Bogomolov theory including
  DP07, by a practitioner of these estimates. Survey level only; no explicit
  constant.
- **Viada 2007** (`arxiv-0711.3533-nondense-subsets-power-elliptic`) — effective
  Bogomolov bound for subvarieties of E^g via David–Philippon/Rémond constants;
  same constant chain, different (transverse-variety) setting.
- **Harrison–Mudgal–Schmidt** and **Garcia-Fritz–Pasten** — the effective-constant
  discussion at the top of the chain (HMS Theorem 1.1: C effectively computable
  but no explicit value; why C^(1+r) < 3 is not decidable from it).

The request `dp07-explicit-constant-for-e3-ap` stays **open**: the DP07
Théorème 1.13 constant formula is still not in the library. Any later attempt
should target (a) an institutional OUP download, or (b) a scan/annotation of
rpm006 from a library that holds IMRP 2007, or (c) Philippon's or David's
institutional page snapshots in the Wayback Machine that may carry a preprint.

```claim
id: dp07-primary-text-not-obtainable-this-cycle
statement: David-Philippon IMRP 2007 (rpm006) primary text is not in the
  library: OUP 403s on every route (DOI, article-pdf, article-lookup),
  no arXiv preprint exists, HAL does not hold it, Jussieu profile is a stub.
  The DP07-adjacent tier (Galateau 2016 habilitation; Viada 2007) is on disk.
hypotheses: —
holds-here: yes
status: checked (four independent acquisition routes, all blocked; each a
  distinct failure of the same paywall)
bearing: the open request dp07-explicit-constant-for-e3-ap is NOT filled;
  do not cite the survey tier as the source of the explicit constant
anchor: research/summaries/david-philippon-minorations-puissances-courbes-elliptiques-2007.md
```