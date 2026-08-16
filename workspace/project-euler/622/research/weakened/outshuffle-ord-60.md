# Ladder: out-shuffle order 60 (Project Euler 622)

The full problem, decomposed into the six specific obstructions that make it
hard, then weakened rung by rung from the trivial seed up to the real target.
Every rung is the *goal* with a named subset of difficulties switched off — not
a lemma, not an alternate route.

```ladder
goal: Sum over all positive even n with s(n) = 60 of n, where s(n) is the order of the out-shuffle permutation of an n-card deck (Project Euler 622); delivered as a kernel-checked Lean equality of naturals.
difficulties: shuffle-order reduction, order-lcm structure, 2^60-1 factorization, prime-power lift, divisor enumeration, kernel final-sum
status: open
```

Notes on the declared difficulties, so each is the specific obstruction and not
a topic:

- **shuffle-order reduction** — the theorem s(n) = ord_{n-1}(2) for all even n:
  the out-shuffle fixes top and bottom cards and sends interior card x to 2x mod
  (n-1), so its order is the multiplicative order of 2 mod the odd number n-1.
  This is the one genuinely combinatorial step, and the Lean encoding of the
  permutation plus its order is where the most content lives.
- **order-lcm structure** — ord_m(2) = lcm over prime powers p^a || m of
  ord_{p^a}(2). This is what turns "m has order 60" into a finite local
  combination problem instead of a search.
- **2^60-1 factorization** — the prime factorization 2^60-1 = 3^2·5^2·7·11·13·31·41·61·151·331·1321
  (hand-derived; must be found by Python and kernel-checked by one multiplication
  in Lean). Also carries the finitization m | 2^60-1 whenever ord_m(2)=60.
- **prime-power lift** — ord_{p^a}(2) = ord_p(2)·p^{max(0, a - v_p(2^{ord_p(2)}-1))}:
  the Wieferich-carry analysis that decides which exponents a are admissible
  (all v_p here are expected to be 1, so the only lifted powers are p=3 and p=5,
  each at most squared).
- **divisor enumeration** — combining the admissible prime powers whose local
  orders lcm to exactly 60, enumerating the divisors, and summing n = m+1. The
  danger is a bound-scaled scan; it must be a structural enumeration over divisors
  of 2^60-1 only.
- **kernel final-sum** — carrying the (large) final sum through the Lean kernel
  by unfolding the constructive enumeration, with `native_decide` refused. The
  value is produced by the structural argument, not by a compiled decision
  procedure.

```rung
id: R-ord51-2
statement: The multiplicative order of 2 modulo 51 is 8: in Lean, orderOf (2 : (ZMod 51)ˣ) = 8 (equivalently, the least m > 0 with 2^m ≡ 1 (mod 51) is 8), proved by unfolding the small powers 2,4,8,16,32,13,26,1.
off: shuffle-order reduction, order-lcm structure, 2^60-1 factorization, prime-power lift, divisor enumeration, kernel final-sum
stance: open
merge: Instantiate ZModˣ order at the deck sizes next: build the out-shuffle on Fin 52 and Fin 86 and compute its order by iteration (rung R-s52-86).
```

```rung
id: R-s52-86
statement: The out-shuffle permutation of a 52-card deck has order 8 and of an 86-card deck has order 8, proved in Lean by constructing the permutation on Fin 52 (resp. Fin 86) and computing its order by iteration — no general reduction is used.
off: shuffle-order reduction, order-lcm structure, 2^60-1 factorization, prime-power lift, divisor enumeration, kernel final-sum
stance: open
merge: Replace direct permutation iteration with the order-lcm route at tiny scale: factor 255 = 3·5·17 and combine divisors by lcm to reach the sum 412 (rung R-sum8).
```

```rung
id: R-sum8
statement: The sum of (m+1) over all divisors m of 255 with ord_m(2) = 8 equals 412 — the worked example in multiplicative-order form, with m ∈ {17, 51, 85, 255}, proved by the order-lcm structure and the factorization 255 = 3·5·17.
off: shuffle-order reduction, 2^60-1 factorization, prime-power lift, kernel final-sum
stance: open
merge: Lift the worked example to the general statement s(n) = ord_{n-1}(2) for all even n: formalize the interior position map x ↦ 2x mod (n-1) and its order (rung R-reduction).
```

```rung
id: R-reduction
statement: For every even n ≥ 2, the order s(n) of the out-shuffle on an n-card deck equals the multiplicative order ord_{n-1}(2), proved in Lean: the out-shuffle fixes the top and bottom cards and sends interior card x to 2x mod (n-1), so the deck returns exactly when 2^k ≡ 1 (mod n-1).
off: order-lcm structure, 2^60-1 factorization, prime-power lift, divisor enumeration, kernel final-sum
stance: open
merge: Instantiate at order 60: ord_m(2) = 60 forces m | 2^60-1; hand the kernel the factorization of 2^60-1 as a literal to check by one multiplication (rung R-factor).
```

```rung
id: R-factor
statement: 2^60 - 1 = 3^2·5^2·7·11·13·31·41·61·151·331·1321, kernel-checked in Lean by a single norm_num multiplication; and ord_m(2) = 60 implies m | 2^60 - 1, so every candidate m is a divisor of 2^60-1.
off: shuffle-order reduction, order-lcm structure, prime-power lift, divisor enumeration, kernel final-sum
stance: open
merge: For each of the 11 primes compute v_p(2^{ord_p(2)}-1) (all expected to be 1, no Wieferich primes) and derive the admissible exponents a from ord_{p^a}(2) | 60 (rung R-lift).
```

```rung
id: R-lift
statement: For every prime p ∈ {3,5,7,11,13,31,41,61,151,331,1321}, v_p(2^{ord_p(2)}-1) = 1 (none is Wieferich), hence ord_{p^a}(2) = ord_p(2)·p^{a-1}; therefore p^a can divide an m with ord_m(2) = 60 only when a = 1 for p ∉ {3,5}, and a ≤ 2 for p = 3,5 (ord_3 = 2, ord_9 = 6, ord_5 = 4, ord_25 = 20, all dividing 60; the next powers give 18 and 100, which do not).
off: shuffle-order reduction, order-lcm structure, divisor enumeration, kernel final-sum
stance: open
merge: Combine the admissible prime powers whose local orders lcm to exactly 60, enumerate the resulting divisors, and sum n = m+1 — a structural enumeration over divisors of 2^60-1, never scanning up to the bound (rung R-final).
```

```rung
id: R-final
statement: The sum of all positive even n with s(n) = 60 equals [the answer], proved in Lean as an equality of naturals: s(n) = ord_{n-1}(2) = 60, so m = n-1 | 2^60-1 with lcm of local orders equal to 60; enumerate the admissible divisors, sum m+1, and check the final sum by kernel unfolding (no native_decide).
off:
stance: open
merge: None — this is the full problem. Settling it exhausts the ladder; mark status exhausted.
```
