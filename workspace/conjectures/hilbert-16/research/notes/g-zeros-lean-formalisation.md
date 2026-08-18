# G-zeros formalisation note

`code/lean/h16_2_finite_cyclicity_G_zeros-f287dd45.lean` passed `lean_check` with no sorry and only `propext`, `Classical.choice`, and `Quot.sound`. It defines transition maps, their finite composition, and the displacement as composition minus identity. The theorem proves that an assumed finite zero set has a natural-number bound by choosing its `ncard`. `analyticExpansion` and `finitelyGeneratedModule` are explicit binders but are not used in this implication; the substantive analytic rank/finiteness theorem remains an unproved hypothesis.
