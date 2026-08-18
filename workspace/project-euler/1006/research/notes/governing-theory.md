# Governing theory note

The source library establishes the relevant framework: the infinite Fibonacci word is a characteristic Sturmian word, hence has exactly k+1 distinct factors of each length k. Sturmian words admit equivalent mechanical/rotation descriptions. For the Fibonacci slope α=1/φ², use

 d_j(x)=⌊x+(j+1)α⌋−⌊x+jα⌋.

The length-k digit vector is constant as x moves within each component of the circle cut by {−mα mod 1:0≤m≤k}; there are k+1 components. Therefore Ψ(k) is a sum over k+1 rotation representatives. Interpreting the vector as a decimal number gives a geometrically weighted sum of floor values, so its square expands into weighted first and second moments of floor-linear forms. The Fibonacci continued fraction α=[0;2,1,1,…] permits an Euclidean recursion, generalising the standard floor_sum algorithm, whose cost is logarithmic in the integer parameters rather than proportional to k.

This is the structural reduction to implement. The source-backed part is the Sturmian/mechanical representation and factor count; the weighted second-moment recursion and its exact decimal indexing are a derivation to be verified mechanically.

## Claim block

```claim
id: governing-fibonacci-sturmian-mechanical
status: established
statement: The infinite Fibonacci word fixed by 0→01, 1→0 is a characteristic Sturmian word of slope 1/φ². Sturmian words have exactly k+1 distinct factors of length k and admit a mechanical/irrational-rotation description; the length-k factor is constant on the k+1 intervals cut by the orbit points {-jα mod 1}.
hypotheses: α irrational; factors are contiguous factors of the Fibonacci fixed point.
holds_here: yes
source: https://www.cambridge.org/core/product/identifier/CBO9781107326019A016/type/BOOK_PART
source: https://arxiv.org/abs/math/0106217
source: https://www.jstor.org/stable/2371261
```
