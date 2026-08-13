# Approach: Chabauty–Coleman on the 7th/8th-square hyperelliptic curves

```approach
idea: Apply the Chabauty–Coleman method (p-adic integration) directly to the
specific hyperelliptic curves that Bremner's 2001 classification produces when
demanding a seventh or eighth square entry. Chabauty (1941): if C/Q is a curve
of genus g ≥ 2 and rk J(Q) < g, then C(Q) is finite. Coleman (1985): under the
same hypothesis the rational points are effectively computable via p-adic
integration. Bremner II §2 (Category VII) gives the explicit quartics:
equation (12) is the condition that already gave the 7-square witness at λ=13,
p=9, q=2; equations (13) are the three remaining entries' square conditions.
The 8th square means realising one of (13) as a square simultaneously with
(12). This defines a curve; if its genus g ≥ 2 and its Jacobian rank r < g,
Chabauty–Coleman either finds all rational points or proves none exist beyond
the known witness. Covering all 16 configurations would settle the 8-square
sub-question.
status: refuted (for Category VII — genus 1 blocks Chabauty–Coleman; other configurations unknown but no witness exists)
killed-by: This run computed genus of the three eq. (13) quartics at λ=13 (Category VII) using two independent routes (Sage HyperellipticCurve and sympy discriminant) — all three are genus 1 (elliptic curves), not genus ≥ 2. Chabauty–Coleman's decisive hypothesis g ≥ 2 fails. The first-step was executed (code/out/bremner2_quartics.txt) and returned: GENUS 1 for (13a),(13b),(13c). The correct tool for genus-1 curves is elliptic 2-descent/Selmer on E: y²=F(x), which is the subject of the root-number-parity-four-curves approach. Whether any other 7→8 configuration in Bremner's 16 yields a curve of genus ≥ 2 with r < g is unverified, but no 7-square witness is known in any configuration other than Category VII, so there is no explicit curve to apply Chabauty–Coleman to.
first-step-result: genus 1 for all three eq. (13) quartics at λ=13 (code/out/bremner2_quartics.txt). Chabauty–Coleman does not engage — the genus-≥2 hypothesis fails. The computation verified eq. (12) at the witness (p=9,q=2) → square = 373²·34², confirming the Bremner witness reconstruction. The approach's own first-step criterion "if r ≥ g for all three, Chabauty–Coleman does not apply and the approach is closed" is satisfied, but it's worse than r ≥ g — the genus itself is 1, so neither r<g nor r≥g is a meaningful question.
precedent: A. Bremner, "On squares of squares II", Acta Arith. 99 (2001) 289-308
  (library: research/sources/bremner-on-squares-of-squares-II-2001.full.md) gives
  the explicit quartics (12)-(13) for Category VII, the 7-square witness, and the
  bounded search; C. Chabauty, CRAS 212 (1941); R. Coleman, Duke Math J 52 (1985);
  Coleman integration for even-degree hyperelliptic curves, LMS J Comput Math 18 (2015).
  The decisive hypothesis r < g is unverified for every magic-square curve;
  this approach is adopted on the strength of the explicit first-step being
  computable, not on a guarantee that r < g holds.
first-step: From Bremner II §2 eq. (12)-(13), write a SageMath/Sympy script that
  (a) substitutes λ=13 and the known 7-square witness (p=9,q=2) to verify eq.(12)
  is indeed a perfect square; (b) for each of the three quartics in (13) with λ=13,
  treats "quartic(p,q) = Y²" as a curve over Q, computes its genus; (c) if genus ≥ 2,
  performs a 2-descent to bound the Jacobian rank; (d) reports whether r < g for
  any of the three. If r ≥ g for all three, Chabauty–Coleman does not apply and
  the approach is closed with that as a result.
```

## What this reformulation is actually called

This is **Chabauty's method** (1941) with **Coleman's effective refinement**
(1985), the classical p-adic strategy for computing Y(Q) when the Jacobian has
rank below the genus. For hyperelliptic curves the required Coleman integration
is implemented (e.g. Balakrishnan–Besser–Müller quadratic Chabauty; Balakrishnan
et al. ANTS algorithms; the LMS J. Comp. Math. paper "Coleman integration for
even-degree models of hyperelliptic curves"). The name and the theorem are
standard and are not in doubt.

## Precise statement of the theorem and whether its hypotheses hold here

**Chabauty–Coleman theorem (hypotheses):** Let C be a smooth projective curve of
genus g ≥ 2 over Q, with Jacobian J, and suppose the Mordell–Weil rank
r := rk J(Q) satisfies **r < g**. Then C(Q) is finite, and Coleman's method gives
an explicit bound on #C(Q) by integrating at a prime p of good reduction, and
thereby a finite determination of C(Q).

**Do the hypotheses hold here? — UNVERIFIED, and this is the crux.** Bremner II
(2001) states exactly that a seventh square entry means finding rational points
on hyperelliptic curves `f(t) = ☐` "in general of high genus", but it **does not
give the explicit polynomial f(t)** for the 7→8 transition, and **no rank or
genus computation for these curves exists in the literature**. The chain the
candidate requires —

    1. extract explicit f(t) for the 7→8 transition from Bremner's parametrisation,
    2. compute its genus g,
    3. compute (or bound) r = rk J(Q) via 2-descent,
    4. check r < g,

— has **step 1 not even written down by Bremner, and steps 2–4 never done by
anyone**. Without step 4, Chabauty–Coleman simply does not apply (if r ≥ g the
method gives no information; the Coleman–Chabauty bound provably fails when the
rank hypothesis is dropped — see the literature of type "On the Coleman-Chabauty
bound"). Whether r < g holds for any of these curves is unknown.

## Has anyone applied it to this problem?

**No.** Searches turn up the general Chabauty–Coleman/even-degree-hyperelliptic
implementation literature and the hyperelliptic reductions from Bremner, but no
paper applies Chabauty–Coleman (or any p-adic point-counting) to the magic-square-
of-squares hyperelliptic curves. This is a genuinely un-attempted direction.

## What it would buy

Genuinely useful **if** the decisive rank hypothesis r < g holds for a curve in
the 7→8 transition: it would make the rational-point set of that curve
computable and would prove the 8-square sub-question for that configuration
(relative to Bremner's parametrisation). It also sidesteps the K3 cohomology of
the Brauer–Manin route. But it is **speculative**: the first step (explicit f(t))
is not in the literature, and the rank condition is untested. Per GOAL's
falsification discipline, note also that any conclusion drawn must survive the
7-square witness (1): a computation that "proves the 7→8 transition has only the
7-square points" must reproduce and keep that witness.

## Verdict

**status: grounded** — the reformulation is real (Bremner II gives the
hyperelliptic reduction) and the method is a named, standard, implemented
theorem. But the **application rests on an unverified decisive hypothesis**
(r < g for the specific 7→8 transition curve). CORRECTION: the explicit curves
for Category VII ARE in the literature — Bremner II eq. (12)–(13) gives the
quartics — and this run computed (`code/out/bremner2_quartics.txt`) that the
three eq. (13) quartics at λ=13 are genus 1 (elliptic), so Chabauty-Coleman's
genus-≥2 rank hypothesis does not engage for those specific 7→8 curves; the
correct tool there is elliptic 2-descent/Selmer on E: y²=F(x). Whether any
OTHER 7→8 configuration yields a genus-≥2 curve with r < g is unverified.

## Precedent

- A. Bremner, "On squares of squares II", Acta Arith. 99 (2001) 289–308 — the
  six-square → hyperelliptic reduction; says "seventh square = rational points on
  hyperelliptic f(t)=☐, generally high genus"; does **not** give f(t) for the
  7→8 transition, nor any genus/rank. (library: `research/summaries/bremner-on-squares-of-squares-II-2001.md`)
- C. Chabauty, "Sur les points rationnels des courbes algébriques de genre
  supérieur à l'unité", C. R. Acad. Sci. Paris 212 (1941) — the theorem.
- R. Coleman, "Effective Chabauty", Duke Math. J. 52 (1985) — effective version.
- Coleman integration for even-degree hyperelliptic curves, LMS J. Comput. Math.
  18 (2015) — algorithmic implementation.
  https://www.cambridge.org/core/journals/lms-journal-of-computation-and-mathematics/article/coleman-integration-for-evendegree-models-of-hyperelliptic-curves/AF72EF6830BFCDB0BBB14B996A5BE733
- On the Coleman-Chabauty bound (proves the bound fails when r ≥ g) —
  https://www.sciencedirect.com/science/article/abs/pii/S0764444200800415

## First step (if pursued)

Extract from Bremner II's Category VII parametrisation the explicit polynomial
f(t) whose square condition gives the 8th square entry on top of the 7-square
witness; compute its genus the Jacobian rank; only if r < g proceed to Coleman
integration. Until that is done this candidate is a method in search of its
object.

```claim
id: chabauty-coleman-grounded-but-application-open
statement: Bremner II reduces a 7th square entry to rational points on hyperelliptic
  curves f(t)=square (generally high genus); Chabauty-Coleman (r<g) is the standard
  p-adic method to compute such points, but the explicit f(t) for the 7->8 transition,
  its genus, and its Jacobian rank are not in any source, and the decisive r<g
  hypothesis is unverified.
hypotheses: C/Q genus g≥2, rk J(Q)<g
holds-here: unverified (the applicability hypothesis r<g is unknown for every
  magic-square curve; f(t) never written down)
status: sourced/asserted
bearing: the 8-square sub-question could be settled per-configuration IF r<g holds;
  otherwise the method gives nothing
anchor: research/approaches/chabauty-coleman-hyperelliptic.md
```
