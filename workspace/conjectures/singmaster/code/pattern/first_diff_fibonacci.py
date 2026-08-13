"""Verify: the family parameters' first differences are single Fibonacci numbers.

n_i = F_{2i+2}F_{2i+3}-1, k_i = F_{2i}F_{2i+3}-1  (i=1,2,...)
Conjecture from first-difference inspection:
    n_i - n_{i-1} = F_{4i+3}   (i >= 2)
    k_i - k_{i-1} = F_{4i+1}   (i >= 2)
i.e. first differences are single Fibonacci numbers with indices 4i+3 / 4i+1.

Also check the derived closed form identity:
    F_m F_{m+1} - F_{m-2}F_{m-1} = F_{2m-1}
    F_m F_{m+3} - F_{m-2}F_{m+1} = F_{2m+1}
which justify the two claims above.
"""
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

N = 200
fibs = [fib(i) for i in range(N + 10)]

# Check the two closed-form identities on a wide index range
print("=== Closed-form identities ===")
okF = okK = True
for m in range(3, 60):
    if fibs[m]*fibs[m+1] - fibs[m-2]*fibs[m-1] != fibs[2*m-1]:
        okF = False
    if fibs[m]*fibs[m+3] - fibs[m-2]*fibs[m+1] != fibs[2*m+1]:
        okK = False
print("F_m F_{m+1} - F_{m-2}F_{m-1} == F_{2m-1}  for m=3..59:", okF)
print("F_m F_{m+3} - F_{m-2}F_{m+1} == F_{2m+1}  for m=3..59:", okK)

# Now the actual family parameters vs first-difference Fibonacci claim
print("\n=== Family first differences vs Fibonacci ===")
print("%2s %12s %12s | %12s %12s | %8s %8s %8s %8s" % (
    "i", "n_i", "k_i", "diff_n", "diff_k", "F_{4i+3}", "matchN",
    "F_{4i+1}", "matchK"))
alln = allk = True
for i in range(1, 13):
    n = fibs[2*i+2]*fibs[2*i+3] - 1
    k = fibs[2*i]*fibs[2*i+3] - 1
    if i >= 2:
        # n_i - n_{i-1}, k_i - k_{i-1}
        mn = fibs[2*(i-1)+2]*fibs[2*(i-1)+3] - 1
        mk = fibs[2*(i-1)]*fibs[2*(i-1)+3] - 1
        dn, dk = n - mn, k - mk
        Fn, Fk = fibs[4*i+3], fibs[4*i+1]
        mN, mK = (dn == Fn), (dk == Fk)
        alln = alln and mN
        allk = allk and mK
        print("%2d %12d %12d | %12d %12d | F%02d=%8d %8s | F%02d=%8d %8s"
              % (i, n, k, dn, dk, 4*i+3, Fn, mN, 4*i+1, Fk, mK))
    else:
        print("%2d %12d %12d |" % (i, n, k))

print("\nRESULT: n_i-n_{i-1}=F_{4i+3} for i=2..12:", alln)
print("RESULT: k_i-k_{i-1}=F_{4i+1} for i=2..12:", allk)
