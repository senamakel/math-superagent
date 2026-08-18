# Efficient-method assessment

## Structural reduction

The governing result is the Sturmian complexity theorem: the Fibonacci fixed point has exactly `k+1` length-`k` factors. Mechanical-word rotation coding represents these factors by the `k+1` cells cut out by the orbit of an irrational rotation of slope `alpha=1/phi^2`. For a cell/intercept `rho`, its digits are

`d_j(rho)=floor(alpha*(j+1)+rho)-floor(alpha*j+rho)`.

The decimal value is then

`V_k(rho)=sum_{j=0}^{k-1} d_j(rho) 10^{k-1-j}`,

and the target is the exact joint moment

`Psi(k)=sum_{rho in the k+1 factor cells} V_k(rho)^2`.

This is the correct reduction because the factors are exactly the mechanical factors, not a sample of them.

## Complexity requirement and current status

A full-size solution must evaluate the joint second moment without iterating over `k+1` factors, because `k=10^18`. The standard Euclidean floor-sum recursion can evaluate weighted moments along one fixed floor path in logarithmic coefficient complexity, but it does not by itself evaluate the coupled sum over all `k+1` intercept cells. A fixed-dimensional associative state for that joint observable would be sufficient; the local reference set does not establish such a state.

Accordingly, this workspace does not have a justified efficient evaluator or a verified numerical answer. `code/solution.py` remains an explicit placeholder rather than silently presenting an unsupported result.

## Counterexample discipline

Any proposed collapse of the joint moment must first agree with the naive oracle at `k=1,2,3`, then with larger small cases. In particular, replacing the joint cell sum by one pinned intercept or by an additive triple `(count, sum V, sum V^2)` is not justified: the local research notes record failures of these reductions at the smallest cases.

## Verification status

The required execution of `code/brute.py` could not be performed in this interface because the mandated `tool_builder` execution namespace is unavailable. Therefore the worked examples are recorded as assertions in the program but are not claimed as executed evidence here. No full-size answer is reported.
