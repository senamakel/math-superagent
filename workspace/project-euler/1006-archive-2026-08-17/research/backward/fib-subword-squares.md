# Proof skeleton: Fibonacci subword square sum

```skeleton
goal: Compute Psi(10^18) mod 101001001, where Psi(k) = sum over the k+1 distinct
      length-k factors of the infinite Fibonacci word f of (decimal(w))^2,
      reading each binary string w as a decimal integer with leading zeros dropped.
implies: Given a parameterization of each length-k factor w_j (0 <= j <= k) as a
         binary string (G1), express the decimal value of w_j as a linear combination
         of basis terms (e.g. powers of 2 times indicator bits), then substitute
         into sum_{j=0}^k (decimal(w_j))^2. Compute this sum in closed form (G2)
         by exploiting the Zeckendorf / Ostrowski structure of the index set,
         then evaluate the resulting expression at k=10^18 modulo 101001001
         using fast exponentiation of recurrences (G3).
status: sketched
rests-on: PE1006-kplus1-FACT
killed-by:
```

```gap
id: G1-factor-parameterization
lemma: For every k >= 1, there exists an explicit description of each of the k+1
       distinct length-k factors of the infinite Fibonacci word f = lim S_n.
       Specifically, there is a bijection j -> w_j (0 <= j <= k) such that w_j
       is the unique length-k factor that begins at a position determined by j
       in the Ostrowski / Zeckendorf numeration system, and w_j can be generated
       as a binary string in O(k) time (or its decimal value computed directly).
status: open
discharged-by:
thread:
next: Use the known Sturmian structure: the k+1 factors of length k are the
      prefixes of length k of the k+1 distinct right-infinite suffixes determined
      by the slope. For the Fibonacci word (slope 1/phi^2), enumerate the factors
      explicitly for small k (k <= 40) and code the Ostrowski-indexed generation
      rule, verifying against R0-small-brute.
```

```gap
id: G2-sum-closed-form
lemma: Using the parameterization from G1, the sum Psi(k) = sum_{j=0}^k
       (decimal(w_j))^2 can be expressed as a closed form in k, or as a linear
       recurrence of fixed order (independent of k), possibly with terms
       involving powers of 2, Fibonacci numbers, and sums over Zeckendorf
       representations. The expression must be evaluable at k=10^18 without
       iterating over the k+1 factors.
status: open
discharged-by:
thread:
next: For moderate k (k up to, say, 200), compute Psi(k) by brute force (R0),
      then compute the parameterized w_j decimal values from G1, and attempt to
      fit or derive the sum-of-squares formula by pattern analysis on the
      decimal values grouped by their Ostrowski index. Candidate structure:
      the k+1 factors split into two families: those starting with '0' (which
      are prefixes of f shifted by one) and those starting with '1' (which are
      prefixes of the complement / swap). The decimal values may follow a
      Fibonacci-like recurrence in k.
```

```gap
id: G3-fast-evaluation
lemma: The expression from G2 can be evaluated at k = 10^18 modulo 101001001
       using O(log k) arithmetic operations, by reducing the recurrence to
       matrix exponentiation or by evaluating a closed form with fast modular
       exponentiation of powers of 2 and Fibonacci numbers modulo 101001001.
status: open
discharged-by:
thread:
next: Once G2 is settled, implement the recurrence or closed form in Python
      using sympy or gmpy2 for exact modular arithmetic, with matrix
      exponentiation (binary exponentiation) to handle k=10^18. Validate
      against R0 for all reachable k (k <= 40).
```
