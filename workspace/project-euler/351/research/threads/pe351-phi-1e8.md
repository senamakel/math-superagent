# Thread: computing Phi(10^8) for PE 351

```thread
question: What is the summatory totient Phi(10^8) = sum_{k<=10^8} phi(k),
          and hence H(10^8) = 3*10^8*(10^8+1) - 6*Phi(10^8)?
status: resolved — Phi(10^8) = 3039635516365908 (two independent sieve routes
        agree: incremental totient sieve, code/lib/totient.py; Möbius-inversion
        sum, code/verify_mobius.py); H(10^8) = 11762187201804552 (also via
        Chai Wah Wu's A063985 recursion: A063985(10^8)=1960364533634092,
        H=6·A063985, patterns.py).
rests-on: gauss-divisor-sum-of-totient (research/notes/pe351-governing-theory.md);
          summatory-totient-mobius-identity; totient-sum-verification-values;
          totient-sum-fast-recursion.
blocked-by: nothing.
next: none — the final answer is computed and cross-checked three ways.
```

The library establishes:
- H(n) = 6*sum_{k<=n}(k - phi(k)) = 3n(n+1) - 6*Phi(n)  [OEIS A216453].
- Phi(n) = (1/2)(1 + sum_{d<=n} mu(d) floor(n/d)^2)  [MathWorld; Wikipedia].
- Gauss identity sum_{d|n} phi(d) = n, hence the floor-grouped recursion
  [MathWorld TotientFunction eq. (15); Wikipedia Totient summatory function].
- Phi(10^8) = 3039635516365908  [OEIS A064018; Brown 2025 computed to 10^19].
- Chai Wah Wu's A063985 recursion  [OEIS A063985].

Reference point for the forward loop: A216453 gives H(5)=30, H(10)=138,
H(1000)=1177848 exactly (check: 6*(500500-304192) = 6*196308 = 1177848).
