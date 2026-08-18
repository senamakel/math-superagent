# Efficient-method status

The exact problem is:

- S_0 is the one-symbol string `0` and S_1 is `01`.
- For n≥2, S_n=S_{n−1}S_{n−2}.
- F_k is the set of distinct contiguous length-k factors appearing in some S_n.
- For a binary word x=x_0…x_{k−1}, val(x)=Σ_{j=0}^{k−1}x_j10^{k−1−j}, with leading zeroes naturally ignored.
- Ψ(k)=Σ_{x∈F_k}val(x)^2; target Ψ(10^18) mod M, M=101001001.

The governing result is Sturmian factor complexity: the infinite limit of the S_n is the Fibonacci characteristic Sturmian word, and every Sturmian word has exactly k+1 distinct factors of length k. Mechanical rotation coding parametrizes those factors by floor differences. This reduces the statistic to a quadratic sum of geometrically weighted floor-difference digits over k+1 rotation cells.

A universal-Euclidean recurrence can evaluate an individual affine floor-line weighted moment, but the needed aggregation over all k+1 intercept cells has not been proved to close in fixed dimension. Published sources in the local library on Fibonacci-automatic words, factor positions, Rauzy graphs, Ostrowski addition, and linear factor complexity do not supply that missing theorem. Existing programs are O(k), not valid at 10^18.

The naive oracle was executed and reproduces both statement anchors: F_3 and Ψ(3)=20302, and Ψ(10)≡10699667 mod M. Therefore no honest full-size evaluator or final residue is currently available. The placeholder `code/solution.py` deliberately raises `NotImplementedError` rather than presenting an unproved answer.
