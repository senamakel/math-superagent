# Kaiser–Rolin–Speissegger 2007 — transition maps at non-resonant hyperbolic singularities are o-minimal

Full text: [[kaiser-rolin-speissegger-transition-maps-ominimal.full]]
(arXiv:math/0612745; published Adv. Math. 224 (2010) 2535–2553).

## What the source establishes (held full text, abstract verbatim)

**Main result:** there is a model-complete and o-minimal expansion ℝ_𝒬 of the real
field such that, for any planar analytic vector field ξ and any isolated, non-resonant
hyperbolic singularity p of ξ, a transition map for ξ at p is definable in ℝ_𝒬. The
expansion also defines all convergent generalized power series with natural support
and is polynomially bounded.

**Hypotheses (load-bearing):** isolated, **non-resonant hyperbolic** singularities;
analytic field. The non-resonance is essential — resonant hyperbolic points and
non-hyperbolic (nilpotent/semi-hyperbolic/degenerate) points are outside the
theorem's scope.

## What it lets this run conclude

- This is the o-minimality route's positive boundary: the NRH_d class (planar analytic
  fields whose limit periodic sets have only non-resonant hyperbolic singularities)
  is the settled restricted class behind claim `h16-ominimality-route-roussarie`.
- The open DRR graphics contain resonant hyperbolic, nilpotent, semi-hyperbolic, and
  degenerate singularities — precisely the complement of this theorem's hypotheses.
  O-minimality of the transition maps for THOSE vertices is exactly the open
  conjecture (Roussarie's programme), not a theorem this source supplies.
- It is the primary anchor for why the run's `h16-ominimality-route-roussarie` claim
  is a restricted-class result: the settled NRH_d class does not include the open
  graphics, and a candidate argument for a degenerate graphic cannot invoke
  o-minimality of its transitions without proving it.

```claim
id: h16-kaiser-rolin-speissegger-nrh-transition-ominimal
statement: Kaiser–Rolin–Speissegger (arXiv:math/0612745, Adv. Math. 224 (2010) 2535): there is a model-complete o-minimal expansion R_Q of the real field in which transition maps at isolated NON-RESONANT hyperbolic singularities of planar analytic vector fields are definable; R_Q also defines all convergent generalized power series with natural support and is polynomially bounded.
hypotheses: planar analytic vector field; isolated non-resonant hyperbolic singularity; transition map on a transversal.
holds-here: yes — for the NRH_d restricted class; NOT for the open DRR graphics (resonant/nilpotent/semi-hyperbolic/degenerate vertices).
status: asserted
evidence: full text held at research/sources/kaiser-rolin-speissegger-transition-maps-ominimal.full.md; abstract states the main theorem.
falsifier: a non-resonant hyperbolic transition map not definable in any such expansion, or an error in the model-completeness proof.
sources: https://arxiv.org/abs/math/0612745
anchor: research/sources/kaiser-rolin-speissegger-transition-maps-ominimal.full.md
follows-from: h16-ominimality-route-roussarie
answers:
```
