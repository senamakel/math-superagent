```approach
id: kodaira-dimension-general-type
idea: Compute the Kodaira dimension of the compactified nine-square surface
  and apply Bombieri-Lang for κ=2.
status: superseded
killed-by: Superseded by `resolve-magic-surface-birational` (adopted this
  round).  The original approach naively compactified the affine
  parametrisation (c, u, v) in weighted projective space without knowing
  the singular locus.  The adopted approach uses the KNOWN 256 singular
  points of the magic variety X ⊂ P⁸ (Michaud-Rodgers 2019) to guide the
  resolution, making it algorithmic rather than blind.  The parked version
  is obsolete — all its goals are now first-steps of the adopted approach,
  with the singular locus resolved rather than ignored.
first-step: NONE — superseded by resolve-magic-surface-birational.
precedent: as originally written.
```