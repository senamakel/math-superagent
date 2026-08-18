# Żołądek M(3)≥11 — dispute resolved, both sides now held

*Cycle 2026 (librarian). Finding for the scholar to digest into a claim block.*

## What was missing

The library cited M(3) ≥ 11 to Żołądek, "Eleven small limit cycles in a cubic
vector field", Nonlinearity 8 (1995) 843–860, but held only secondary mentions
(Torregrosa 2024, Liang–Torregrosa). The primary is paywalled at IOP
(doi:10.1088/0951-7715/8/5/011; no open mirror found this cycle).

## What was added this cycle (full texts, both held)

1. **P. Yu, M. Han, "A study on Żołądek's example", J. Appl. Anal. Comput.
   1(1) (2011) 143–153** — `research/sources/yu-2011-study-on-zoladek-example.full.md`
   (src https://publish.uwo.ca/~pyu/pub/preprints/YH_JAAC2011a.pdf)
   — Focus-value computation shows that for Żołądek's proposed cubic integrable
   example, the **first-order (ε-order) focus values yield at most nine
   small-amplitude limit cycles** around the center. So the example as claimed
   (eleven) did not appear to work at first order.

2. **Y. Tian, P. Yu, "Bifurcation of small limit cycles in cubic integrable
   systems using higher-order analysis", arXiv:1708.07864 (2017)** —
   `research/sources/tian-yu-bifurcation-small-limit-cycles-cubic-2017-arxiv.full.md`
   — Higher-order (normal-form / higher-Melnikov) analysis of the *same* system
   shows it **can indeed have eleven small-amplitude limit cycles under
   perturbations up to at least 7th order**; pattern of cycle-counts computed up
   to 39th-order perturbations, with **no more than eleven** found.

## Resolution

- The Yu–Han "at most nine" is the **first-order** ceiling (all ε-order focus
  values vanish past V₉, then V₁₀⋯ vanish identically because the Vᵢ₁ are
  linear); the eleven arise from **higher-order** (ε², ε³, …) focus values.
- So Żołądek's original claim M(3) ≥ 11 is **confirmed** by a held primary
  re-analysis (Tian–Yu 2017), and the status of "M(3) ≥ 11" upgrades from
  asserted-by-secondary-source to **confirmed by held primary computation**.
- Taken together with Torregrosa 2024 (held; two one-parameter cubic families
  with **twelve** small-amplitude cycles, claim `h16-torregrosa-cubic-12-small-cycles-2024`),
  the current best local bound is **M(3) ≥ 12**, not 11.
- Also visible in Yu–Han's introduction: for *general* (non-integrable) cubic
  systems perturbing a linear center, nine small-amplitude cycles at a single
  point were already known ([8] Lloyd–Pearson 2012, JAAC 2:293–304), and
  multi-point configurations reach 10–13 (refs [9]–[17]), consistent with
  H(3) ≥ 13 = Li–Liu–Yang 2009 (secondary-only in this library; JDE
  paywalled, doi:10.1016/j.jde.2009.01.038).

## Bearing on the run

The small-amplitude thread is now primary-anchored at both ends (Bautin M(2)=3
held in full; M(3)≥12 Torregrosa held in full). This is not a DRR target — it
is the M(n)/local-cyclicity instrument chain, relevant to the
certified-lower-bound approach (`approach-certified-lower-bound-target-escalated`).

```claim
id: m3-zoladek-eleven-confirmed-tian-yu-2017
statement: The cubic integrable system of Zoladek (Nonlinearity 8 (1995) 843-860,
  "Eleven small limit cycles in a cubic vector field") does yield eleven
  small-amplitude limit cycles around a center under suitable cubic
  perturbations. Yu-Han 2011 (JAAC 1:143-153) showed the first-order (eps-order)
  focus values give at most nine; Tian-Yu 2017 (arXiv:1708.07864) showed the
  full higher-order analysis gives eleven (confirmed under perturbations up to
  at least 7th order; no more than eleven through 39th-order perturbations).
hypotheses: planar cubic (degree <= 3) polynomial systems; small-amplitude
  (local) limit cycles bifurcating from an elementary center of an integrable
  cubic system via (generalized) Hopf bifurcation; perturbations of degree <= 3.
holds-here: yes
status: asserted (sourced-primary) -- Yu-Han 2011 and Tian-Yu 2017 full texts
  held; Zoladek 1995 primary itself paywalled (IOP) and not held.
evidence: verified-computationally (secondary) -- Tian-Yu compute focus values /
  higher-order Melnikov coefficients exactly (symbolic), confirming the eleven.
  The original claim of Zoladek 1995 is additionally re-proven, not just
  re-reported. The exact count "no more than eleven up to 39th order" is their
  computed pattern, not a proof of an upper bound for all perturbations.
note: research/notes/zoladek-eleven-cycles-resolved.md
bearing: anchors M(3) >= 11 from held primary re-analysis, resolving the
  Yu-Han-vs-Zoladek apparent dispute (nine at first order, eleven at higher
  order). Together with Torregrosa 2024 (twelve, held) the current best local
  bound is M(3) >= 12.
falsifier: a held primary showing the Tian-Yu computation is wrong, or a
  published higher-order analysis giving more than eleven for that system
  (would upgrade), or the original Zoladek 1995 primary contradicting this
  reading (expected to agree).
answers: -- (a new settled finding, not a response to a standing request)
```

## Not obtained this cycle

- Żołądek 1995 primary (IOP paywalled; no open copy located).
- De Gruyter "Planar Dynamical Systems" (Liu–Li–Huang 2014, doi:10.1515/9783110298369)
  full text: OAPEN handle and De Gruyter PDF both 403 / no text layer. Frontier row stays.
- Rousseau 1997 Nonlinear Analysis survey (paywalled; content subsumed by held
  RSZ/RR + Ilyashenko surveys — low value, recorded as not obtained).
- DRR 1994 primary catalogue (paywalled; metadata-only anchor already held).