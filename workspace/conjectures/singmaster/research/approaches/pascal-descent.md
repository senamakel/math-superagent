```approach
idea: Finite-difference descent — use Pascal's rule iterated to expand one binomial coefficient down to the column level of another, producing a sum identity that supposedly forces proximity of the row indices.

status: refuted
killed-by: The Pascal expansion IS an identity, not a constraint — C(x,k1) = sum_{i,j} C(x-i, k2-j) holds for every x,k1,k2 (with k1>k2) by k1-k2 iterations of Pascal's rule. The claim that the growth-rate disparity forces |x-y| to be bounded is the same type of "gap principle" that MRSTT already established for the interior (at most 4 solutions there) and that MRSTT proved cannot extend to the boundary (Prop 1.12 barrier, even under RH). The approach adds no new structural fact: it rewrites the equality as a linear combination, which is always true, and then conjectures that the linear combination forces a proximity that MRSTT's negative result says does not exist in the boundary regime where all witnesses live. This is a reformulation of MRSTT's gap, not a method to close it. Moreover, the "consecutive-block-merge" approach (refuted: identical to SST 1995) already captures the block-product structure; the Pascal descent is the additive counterpart and adds nothing beyond what the library's equal-products classification already provides.
precedent: none — the mechanism is a restatement of MRSTT's interior-vs-boundary dichotomy.
first-step: none — do not re-propose.
```
