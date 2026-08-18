# Reduction-indexing refutation run

The proposed reduction uses the 0-indexed primitive
`sum_{i=0}^{n-1} z^i floor((p*i+q)/r)^h`, while the mechanical word uses
`digit_j=floor(x+(j+1)a)-floor(x+ja)` and decimal weight `10^(k-1-j)`.

Theory used: telescoping of finite differences. With `v=sum digit_j*10^(k-1-j)`, substitution gives the claimed floor-sum formula; the only possible bugs tested here are a shift in the floor index or in the decimal exponent. The universal Euclidean monoid's composition law was already independently checked in the workspace; this run attacks the reduction boundary and `ue0`'s negative-intercept lifting.

The script `code/refute/check_reduction_indexing.py` is an exponential-size oracle only in the tiny bound k<=20; it is not the proposed full-size method.
