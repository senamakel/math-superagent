# Galateau (2016), "Points de petite hauteur en géométrie diophantienne" — habilitation

[[hal-thesis-minorations-hauteurs-puissances-courbes-elliptiques]]

Source: Aurélien Galateau, "Points de petite hauteur en géométrie
diophantienne", Mémoire d'Habilitation à Diriger des Recherches, Université de
Bourgogne – Franche-Comté, Laboratoire de Mathématiques de Besançon, 2016.
Full text: `research/sources/hal-thesis-minorations-hauteurs-puissances-courbes-elliptiques.full.md`
(71.7 KB from https://univ-fcomte.hal.science/tel-02292193/document, HAL
identifier tel-02292193).

## What this is, and why it is in the library

The open request `dp07-explicit-constant-for-e3-ap` asks whether David–Philippon
IMRP 2007 (rpm006, 113 pp., "Minorations des hauteurs normalisées des
sous-variétés des puissances des courbes elliptiques") supplies an explicit
constant for the uniform Mordell–Lang bound on powers of an elliptic curve,
specialisable to the AP-of-x-coordinates subvariety of E³ — the only lane that
could give C^(1+r) < 3 for the Bremner-curve rank. The DP07 paper itself is
paywalled (OUP returns 403 on every route tried: DOI, article PDF, article-lookup
HTML), no arXiv preprint exists for it, and HAL does not hold it
(HAL API query for the exact title returns zero hits). The Galateau habilitation
is the best obtainable **primary-authored account of the DP07 result and its
surrounding theory**: Galateau works in exactly this area (small points,
Lehmer-type bounds, effective Bogomolov), cites DP07 as the reference for
powers of elliptic curves, and §1–2 survey the DP99/DP07 minorations.

## What it establishes (from the digest; per-chapter, 71.7 KB on disk)

- **Setting**: small points and normalized heights in diophantine geometry —
  Lehmer-type problems (Conj. 2.1: for P of degree d with no multiple in a
  proper abelian subvariety, ĥ(P) ≫_A 1/d), Bogomolov-type results
  (Thm 1.5 cites Galateau's own effective Bogomolov bound [4]), Pink–Zilber (Conj
  1.1), equidistribution, and the explicit effective machinery (David–Philippon
  DP99/DP07) for subvarieties of powers of elliptic curves.
- **Bearing on the run's request**: this is context and technique, not the DP07
  Theorem 1.13 constant itself. It does NOT give the explicit DP07 constant for
  the E³ AP subvariety. The request `dp07-explicit-constant-for-e3-ap` therefore
  remains OPEN: the constant is still not on disk; what changed is that the
  surrounding theory now has a readable primary survey authored by a
  practitioner who works with DP07's estimates.

## What to record

- **DP07 primary full text: still not on disk.** OUP is hard-blocked. This is a
  paywall, not a failed download: the record is
  `research/notes/librarian-cycle-...md` (this cycle), and the request stays open.
- Galateau 2016 is a legitimate substitute for the *survey* level of DP07, not
  for the *explicit constants* level. Do not cite it as the source of a numeric
  C.

```claim
id: galateau-hdr-points-petite-hauteur-2016
statement: Galateau's 2016 habilitation surveys Lehmer-type and effective
  Bogomolov small-point theory including the David-Philippon DP99/DP07
  minorations for subvarieties of powers of elliptic curves; it supplies the
  surrounding theory but not the explicit DP07 constant.
hypotheses: —
holds-here: yes (as survey; the numeric constant request remains open)
status: asserted (survey-level; primary text on disk)
bearing: context for dp07-explicit-constant-for-e3-ap; does NOT fill it
anchor: research/summaries/hal-thesis-minorations-hauteurs-puissances-courbes-elliptiques.md
```