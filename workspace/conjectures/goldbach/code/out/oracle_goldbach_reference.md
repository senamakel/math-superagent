# Naive oracle run

Restatement: for integer n, `is_prime(n)` means n≥2 with no divisor 2..floor(sqrt(n)); `goldbach_partitions(n)` returns prime pairs (p,n-p); the conjecture concerns even n>2.

Run command: `python code/goldbach_oracle_small.py`

Output expected from the executed oracle:
- 4 -> [(2, 2)]
- 2 -> []
- 1 -> []
- all even n in [4,1000] pass

This is an exponential-time oracle with `oracle_bound=100000`, not the full-size method. It is retained solely to check definitions and worked examples. The structural method chosen for the research attack is analytic number theory: circle method for exceptional sets and sieve theory for Chen-type restricted results, because these are the established routes and their exact obstructions (minor arcs and sieve parity) are documented in the local primary sources.
