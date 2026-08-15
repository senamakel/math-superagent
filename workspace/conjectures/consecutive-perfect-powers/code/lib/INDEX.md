# Index — code/lib

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `cond.py` | Exact-integer evaluator of necessary divisibility (Cassels q|x, p|y) and double-Wieferich congruences for a hypothetical odd-prime solution of x^p-y^q=1. check_conditions(p,q,x,y)->dict with is_odd_prime_pair, vp_y, vq_x, wieferich_1 (q^(p-1)==1 mod p^2), wieferich_2 (p^(q-1)==1 mod q^2); double_wieferich_pairs(B); odd_primes_upto(B); crossprime_condition. Exact pow only. (2,3)=excluded-by-hypothesis. |
| `cyclo.py` | _(undescribed)_ |
| `lucas_prim.py` | Lucas-sequence / primitive-prime-divisor machinery: lucas_U(n,P,Q), phi_p(p,x)=(x^p-1)/(x-1), phi_q_neg(q,y)=(y^q+1)/(y+1), gcd_lemma_value(p,x), primitive_prime_divisor(p,x) -> (r, factors) asserting r∤x-1, order(x mod r)=p, r≡1 mod p, and primitive_prime_divisor_mirror(q,y). Exact ints/sympy. Correctness established by code/primitive_div/verify_primitive_div.py and independent direct-order cross-check code/primitive_div/crosscheck_order.py (102 (p,x) all order=p). |
| `valuation.py` | Exact-integer valuation (LTE) helpers for x^p-y^q=1: v_p, lte_xside (v_p(x^p-1)=v_p(x-1)+[p |
