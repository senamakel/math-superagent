# Lu 2026 — analytic remainder audit

Full text: [[lu-h14-3-hemicycle-html.full]] (arXiv:2607.13785v2). RR comparison: [[rousseau-roussarie-center-graphics-nilpotent.full]] (Roussarie–Rousseau 2015 source held under the workspace's RR record).

## Source-backed claim blocks

```claim
id: lu-h14-3-root-uniqueness-hypotheses
statement: In Lu's center calculation, after the analytic coordinate changes and on the first-obstruction zero graph, equation (14.11) has a unique local analytic root e=psi(a,t_c,B) because its derivative with respect to e is nonzero at the source; psi vanishes on a=0 and t_c=0, and two one-variable Hadamard integrals imply psi=a t_c V. Substitution into the degree-six polynomial, which also vanishes on those two slices, yields L2=a(B+m)U with U(0)=1/48 and U a unit.
hypotheses: H14^3 source-normalized family; local source neighborhood; equation (14.11); implicit-function nondegeneracy in e; analytic (not merely C^infty) coordinate/root dependence; t_c=B+m and e=d+a as defined by Lu.
holds-here: unchecked
status: asserted
bearing: This is the exact local root-uniqueness and Hadamard-divisibility step behind the center ideal; it is not supplied by the verified recurrence alone.
anchor: research/sources/lu-h14-3-hemicycle-html.full.md#L640-L715
contradicts: none
follows-from: lu-finite-core-identity-half-checked
answers: lu-h14-3-analytic-remainder
```

```claim
id: lu-h14-3-hadamard-division-domain
statement: Lu claims Hadamard division of the center return/displacement on a common physical word domain: after a finite stopped-word atlas is constructed, Proposition 24 supplies nested domains W^- compactly contained in W^+; on the center face W^+ is star-shaped under the displayed contractions, has fixed first-port/section margins, and both center slices lie in complete period-annulus domains. Theorem 23 then divides first in tau and then in (a,t_c), giving F0=tau A+a t_c C and the stated three-factor decomposition without continuation in ell or division by a finite-smooth saddle-node normalizer.
hypotheses: retained source word; all primitive first hits have already been stopped and have common physical domains; positive section/port margins; analytic dependence; complete center domains; no continuation through a listed gate/barrier.
holds-here: unchecked
status: asserted
bearing: This is a geometric/domain hypothesis needed before Hadamard division; the exact center first-integral and inverse-integrating-factor identities are only algebraic checks and do not prove common-domain completeness.
anchor: research/sources/lu-h14-3-hemicycle-html.full.md#L709-L755
contradicts: none
follows-from: lu-h14-3-global-center-domains-checked-statements
answers: lu-h14-3-analytic-remainder
```

```claim
id: lu-h14-3-domain-completeness-claimed
statement: Lu claims completeness of the physical stopped atlas and regime routing: Theorem 10 gives a finite acyclic stopped-word graph and says every degeneration is a labelled adjacent word, terminal no-passage face, or collapsed interval; Proposition 12 gives exact-once representation of every collar cycle; Proposition 14 and Proposition 53 assign every retained word to exactly one zero theorem, with source/mixed faces handled independently. For the center slices, the reversible first integral and quadratic inverse-integrating factor identify the connected section interval and its possible endpoints as y=-1, K_Q=0, the extra center/saddle, or a compactification face.
hypotheses: fixed physical collar; sufficiently small full five-parameter parameter ball; finite signed root/sector/port cover; transverse cuts and positive first-port margins; singular boxes have the stated finite sector/endpoint structure; analytic stable-manifold/flow-box and implicit-hit results apply on separated cells.
holds-here: unchecked
status: asserted
bearing: This is the domain-completeness/exhaustiveness part of Theorem 1. The paper explicitly says the computer enumeration does not prove physical domains, first-port exhaustiveness, gate positivity, or source localization; those remain human arguments.
anchor: research/sources/lu-h14-3-hemicycle-html.full.md#L274-L379; research/sources/lu-h14-3-hemicycle-html.full.md#L735-L770; research/sources/lu-h14-3-hemicycle-html.full.md#L1038-L1048
contradicts: none
follows-from: drr-lu-claims-h14-3
answers: lu-h14-3-analytic-remainder
```

```claim
id: lu-h14-3-zero-theorem-hypotheses
statement: Lu's analytic zero package is conditional on physical regime hypotheses: Theorem 30 gives at most two source-chart fixed points on each noncompact normalized-action cell after the matched expansion and monotone coordinate q, with k=0 reduced to an affine/identity case; Theorem 32 gives at most one isolated periodic orbit only on the exact mixed face B=a=0 in the stated cone; Theorem 36 invokes Mourtada's QRH finiteness for separated hyperbolic words; Theorem 38 invokes DIR for exactly one genuine central block with hyperbolic complement; Theorem 49 gives at most two QBF/four QHH zeros for complete-lips words in the middle chart; Theorem 51 gives at most four zeros per through component and 24 per signed root-scale word. Every theorem excludes zero eigenvalues, lost sections, changed first ports, collar exits, or non-complete lips configurations by routing them to another named regime.
hypotheses: exact-once stopped itinerary; stated section/clock/first-port margins; source, mixed, hyperbolic, central, complete-lips, middle, or root-scale regime hypotheses respectively; analytic or QRH hypotheses where invoked; coefficient apex interpreted as an identity with no isolated zeros.
holds-here: unchecked
status: asserted
bearing: These are the paper's actual zero-count reductions, but their applicability to every physical word depends on the unverified atlas/domain/exhaustiveness arguments above. No theorem here by itself proves the full H14^3 result.
anchor: research/sources/lu-h14-3-hemicycle-html.full.md#L1250-L1282; research/sources/lu-h14-3-hemicycle-html.full.md#L1320-L1434; research/sources/lu-h14-3-hemicycle-html.full.md#L1510-L1545; research/sources/lu-h14-3-hemicycle-html.full.md#L1920-L1950; research/sources/lu-h14-3-hemicycle-html.full.md#L2330-L2425
contradicts: none
follows-from: lu-h14-3-domain-completeness-claimed
answers: lu-h14-3-analytic-remainder
```

## Gap identified

The held source gives a detailed claimed proof, not an independently established proof. The verified Lu/RR algebraic core does not verify: (1) the implicit-function/root-uniqueness hypotheses and analytic dependence at every specialization; (2) the two-slice vanishing used for exact Hadamard divisibility; (3) common physical-domain/star-shapedness and completeness of both center period-annulus slices; (4) exhaustiveness of the stopped first-port and regime cover; or (5) the applicability of imported QRH/DIR zero theorems to every retained word. Lu itself says the finite computation does not prove physical domains, clock signs, Gaussian estimates, gate positivity, source localization, or first-port exhaustiveness (Appendix B), and says the algebraic checks do not prove common perturbed return domains or chart coverage (Appendix A/C). Thus the main theorem remains asserted-by-source and unchecked, not closed by the clean-room focal/cofactor checks.
