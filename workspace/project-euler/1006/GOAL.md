# Goal: Project Euler 1006

Let `S_0 = "0"`, `S_1 = "01"`, and for `n ≥ 2` let `S_n = S_{n-1}S_{n-2}` (concatenation). A Fibonacci subword of length `k` is a contiguous substring of length `k` occurring in at least one `S_n`. Let `F_k` be the set of distinct such binary strings. For `x=x_0…x_{k-1} ∈ F_k`, define `val(x)=Σ_{j=0}^{k-1} x_j 10^{k-1-j}`; leading zeroes therefore have no effect. Define `Ψ(k)=Σ_{x∈F_k} val(x)^2`.

The official anchors are `F_3={001,010,100,101}`, so `Ψ(3)=20302`, and `Ψ(10) ≡ 10699667 (mod M)`, where `M=101001001`. Compute `Ψ(10^18) mod M`.

The naive oracle is intentionally restricted to small k (3 and 10).