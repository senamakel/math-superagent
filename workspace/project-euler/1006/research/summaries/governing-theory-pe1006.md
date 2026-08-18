# Governing theory for PE1006

**Sources:** Lothaire, *Sturmian Words*, https://doi.org/10.1017/CBO9781107326019.003; Sivasankar–Rama, https://arxiv.org/html/2207.04304; OI Wiki universal Euclidean algorithm, https://oi.wiki/math/number-theory/euclidean/.

The Fibonacci fixed point of `0→01, 1→0` is characteristic Sturmian of slope `α=1/φ²`. Sturmian factor complexity is `p(k)=k+1`: exactly the number of distinct contiguous factors of length k. Mechanical-word/irrational-rotation coding says these factors correspond to the k+1 intervals cut by `{−jα mod 1}` for `j=0,…,k`, with digits represented by floor differences.

For arithmetic, the universal Euclidean algorithm recursively reduces affine floor paths via Euclidean quotients while composing contributions in an associative monoid; binary exponentiation makes the path evaluation logarithmic in coefficient sizes rather than in the iteration bound. It can evaluate weighted floor moments after enlarging the monoid, but PE1006 still requires a separate proof that the whole intercept family and all decimal boundary terms close in fixed dimension.