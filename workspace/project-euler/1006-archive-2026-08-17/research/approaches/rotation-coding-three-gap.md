# Approach: rotation coding + three-gap theorem gives a closed form for the column intervals

```approach
idea: Read the Fibonacci word as the coding of the irrational rotation by alpha=(3-sqrt5)/2=1/phi^2 on the unit circle (letter 1 iff the orbit point lands in the top arc [1-alpha,1)=[1/phi,1)). Then the k+1 distinct length-k factors are the codings taken from one representative point in each of the k+1 arcs cut by {1-{i*alpha} : i=0..k}; every column i of the (k+1)xk factor matrix is therefore the circular interval of rows whose representative x satisfies {x+i*alpha} in [1-alpha,1), with endpoints equal to the arc-indices of {1-(i+1)alpha} and {1-i*alpha}. This turns Psi(k) into a double sum of circular-interval intersection sizes that is explicit and telescopes via the three-distance theorem and the continued fraction of alpha, in O(log k).
mechanism: mechanical-word / rotation coding of Sturmian words (Morse-Hedlund); the three-distance theorem for the gap structure of {n*alpha}; Ostrowski numeration / continued-fraction convergents of alpha=1/phi^2=[0;2,1,1,1,...]; the column endpoints l_i,r_i as functions of i and k are the only unknown, and they are determined by floor/Beatty structure, not by enumeration.
status: proposed
precedent: unchecked
first-step: From the already-computed factor matrix (code/out/factors_k40.json) extract, for each k<=40 and each column i, the circular interval of rows holding a 1, i.e. its two endpoints l_i,r_i; verify they equal the arc-indices of {1-(i+1)alpha} and {1-i*alpha} in the sorted set of cut points {1-{i*alpha}:i=0..k}. If that matches for all k<=40, the intersection formula sum_{i,i'} |[l_i,r_i] cap [l_i',r_i']| * 10^{2k-2-i-i'} reproduces Psi(k) with no factor enumeration.
```

## Why this is the right setting

The Fibonacci word is the mechanical word of slope `alpha=1/phi^2` with intercept `rho=alpha`:

    s_n = floor((n+2)alpha) - floor((n+1)alpha)  =  1  iff  {(n+1)alpha} >= 1-alpha = 1/phi.

So `s_n` is the coding of the rotation `x -> x+alpha` on the circle, with the letter `1` coded
by the arc `[1-alpha, 1)` of length `alpha`. Verified by hand on k=3: the four arcs cut by
`{1-{i alpha}: i=0..3} = {0, 0.236, 0.618, 0.854}` give codings `001, 010, 100, 101` — exactly
the four factors, with values `1, 10, 100, 101` and `Psi(3)=20302`.

The factor starting at `x` is `(1[{x+i alpha} >= 1-alpha])_{i=0..k-1}`. Its column `i` is `1`
exactly for `x` in the interval `[{1-(i+1)alpha}, {1-i alpha})` (mod 1). Because the `k+1`
representative points `x_j` occupy the `k+1` arcs cut by `{1-{i alpha}}`, the set of rows with
a `1` in column `i` is a contiguous circular interval, and its two endpoints are the indices of
the arcs containing the two cut-derived points `{1-(i+1)alpha}` and `{1-i alpha}`.

This is a strictly stronger statement than the established `PE1006-columns-circular-intervals`
claim: it gives the *endpoints*, not just the interval lengths. The endpoints are the "three-gap"
quantities: the rank of `{m*alpha}` among `{0,alpha,...,k*alpha}` sorted, computable in
`O(log k)` from the continued fraction `[0;2,1,1,1,...]` (Ostrowski). Then

    Psi(k) = sum_{i,i'=0}^{k-1} N(i,i') * 10^{2k-2-i-i'},
    N(i,i') = |[l_i,r_i] cap [l_i',r_i']| = circular-interval intersection size.

The double sum collapses because `N(i,i')` is a piecewise-quasi-linear function of `(i,i')`
organised by the three gaps; summing it is a telescoping floor-sum, then reduce each power of 10
mod `ord_10(M)=50500500` and each Fibonacci-indexed quantity mod the Pisano period.

## What would kill it

If the endpoints `l_i, r_i` extracted from the factor matrix do NOT equal the arc-indices of
`{1-(i+1)alpha}` and `{1-i alpha}` for some k<=40, the rotation-coding offset is wrong and the
parametrization needs a different intercept/cut convention. That is checked first, cheaply.

## Relation to the open thread

The open thread `factor-parameterization-psi` indexes factors by the lex-order next-factor rule;
this approach instead indexes the *columns* by a closed-form rotation coding. It is the missing
step the thread's own notes gesture at ("collapse the double sum over the balanced two-value
column structure"): it supplies the endpoints `l_i, r_i` that make the collapse exact.
