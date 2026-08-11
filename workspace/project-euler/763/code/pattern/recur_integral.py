# Investigate the order-7 recurrence beyond the fitted 15 terms.
# Does it produce integer values? Does it match D(20)/D(100) from the statement?
from gmpy2 import mpz

D = [mpz(1), mpz(1), mpz(3), mpz(9), mpz(30), mpz(99), mpz(336),
     mpz(1134), mpz(3855), mpz(13086), mpz(44499), mpz(151263),
     mpz(514419), mpz(1749267), mpz(5949063)]

# recurrence: 3 D[n] = 9 D[n-1]+12 D[n-2]-17 D[n-3]-30 D[n-4]-31 D[n-5]+63 D[n-6]
def rec3(vals):  # vals[-1..-7] = D[n-1..n-7]
    return (9*vals[-1] + 12*vals[-2] - 17*vals[-3] - 30*vals[-4]
            - 31*vals[-5] + 63*vals[-6]), 3  # numerator, denominator

seq = list(D)
fails = []
for n in range(15, 201):
    num, den = rec3(seq)
    if num % den != 0:
        fails.append((n, num, num % den))
        break
    seq.append(num // den)

if fails:
    n, num, rem = fails[0]
    print(f"Recurrence FAILS integrality at n={n} (first extrapolated term):")
    print(f"  3*D({n}) numerator = {num}, remainder mod 3 = {rem}")
    print("=> The order-7 recurrence does NOT extend beyond the fitted 15 terms.")
else:
    print("Integer at all extrapolated terms")
    for n in (15, 20, 21, 100):
        print(f"  D({n}) = {seq[n]}")
    print("D(20) match stmt:", seq[20]==9204559704)
    print("D(100)%1e9 match stmt:", (seq[100] % mpz(10)**9)==780166455)
