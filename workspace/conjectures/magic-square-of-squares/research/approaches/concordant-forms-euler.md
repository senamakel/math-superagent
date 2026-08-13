```approach
idea: Settle whether the four linked APs (differences u, v, u+v, u−v through the centre
       e²) map onto Euler's concordant-forms problem, and if so apply the complete
       elliptic-curve theory of concordant numbers. Named mathematics: concordant forms,
       Euler's concordant numbers, their parametrisation by elliptic curves (Ono; Ohashi;
       the modern classifications of concordant forms). ROOT.md §4 flags this as an
       unsettled gap ("maps onto a known concordant-forms problem is worth settling").

mechanism: Each AP "e² ± d both squares" is the condition d/e² = 2t/(1+t²) for rational
       t (the Pythagorean/congruent-number parametrisation), and the four linked
       differences u, v, u+v, u−v with all eight of e²±u, e²±v, e²±(u+v), e²±(u−v)
       squares form a system of simultaneous x² − y² = (difference) conditions — precisely
       a concordant-forms system. Concordant-number theory is complete: each concordant
       form corresponds to a rational point on an explicit elliptic curve, with finitely
       many torsion points plus a Mordell–Weil rank datum. The specific additive relations
       (u+v) − (u−v) = 2v constrain the four associated elliptic curves through isogenies
       and 2-descent, giving a concrete target rather than a re-naming (unlike the refuted
       s-unit approach, which was shown to merely re-express the genus obstruction). The
       decisive difference: concordant forms reduce to elliptic curves (genus 1 with a
       group law), whereas the s-unit/Hyperelliptic route landed on genus ≥ 3 curves.

first-step: Write the eight conditions (1±α), (1±β), (1±(α+β)), (1±(α−β)) all in Q² as
       an explicit concordant-forms system; identify which known concordant-form theorem or
       curve each pair corresponds to, and whether the four curves are linked by the
       isogeny/2-descent data implied by (u+v)−(u−v)=2v. Run the result against the
       Bremner 7-square witness (it must survive — two of the four APs are realized).

status: refuted
killed-by: The single-AP concordant-forms dictionary is complete and already in this
       library (claim concordant-forms-iff-ell-torsion-order-2: each centre AP is a
       concordant instance p=q=1, k=d, on E(-d,d): y^2=x^3-d^2x, equivalent to a rational
       point of order > 2; claim concordant-single-ap-solutions-computable-large: single-AP
       solutions are computable and astronomically large). But the candidate's decisive
       question — do the FOUR linked differences u,v,u+v,u-v map onto a named concordant
       object? — is answered NO by the literature: each AP is an independent concordant
       instance, and the additive linking of four steps sharing one middle term is a K3
       (Bremner II), not a classified concordant-forms system. No source classifies
       simultaneous concordant forms with additively linked steps. The elliptic 2-descent
       machinery the concordant route would bring is precisely what this run already closed
       as subsumed by Bremner II's K3 NS data (simultaneous-congruent-numbers-2selmer,
       refuted). Dictionary grounded for one AP, empty past it.
precedent:
       - https://www.mdpi.com/2227-7390/3/1/2 (Selder & Spindler, "On theta-congruent
         numbers, rational squares in APs, concordant forms and elliptic curves",
         Mathematics 3(1) 2015 2-15; arXiv:1408.1522) — Theorem 2.2 concordant iff
         rational point order > 2; Theorems 3.1/4.7 order-4/8/3 torsion; the single-AP
         dictionary.
       - https://arxiv.org/abs/1907.02148 (Knaf, Selder, Spindler 2019) — 2-descent
         algorithm for concordant-form curves E_{M,N}.
       - claim concordant-forms-iff-ell-torsion-order-2 (research/summaries/selder-spindler-...md)
       - claim concordant-single-ap-solutions-computable-large (research/summaries/knaf-...md)
       - the four-AP K3 is Bremner II 2001 (research/sources/bremner-on-squares-of-squares-II-2001.full.md);
         its 2-descent content subsumes simultaneous-congruent-numbers-2selmer (refuted).

speculation-vs-established: ESTABLISHED (this run, checked) — the four centre lines are
       APs with differences u, v, u+v, u−v; Bremner's witness realizes exactly two of the
       four (near-miss-baseline-and-incidence). ESTABLISHED (sourced) — three-term APs of
       squares = congruent-number setup (ap-three-squares-unique-param). SPECULATION — that
       the four linked differences form a known concordant-forms system and that its
       elliptic-curve theory is restrictive enough to help; the first step is the
       reduction, and it fails if the system does not match any classified concordant form.
```
