# Test the conjectured order-7 constant-coefficient linear recurrence for
# D(N) (PE763) against HELD-OUT values the run never computed:
#   D(20) = 9204559704            (statement)
#   D(100) last nine digits = 780166455   (statement)
#
# Recurrence found by exact elimination over D(0..14):
#   D[n] = 3 D[n-1] + 4 D[n-2] - 17/3 D[n-3] - 10 D[n-4] - 31/3 D[n-5] + 21 D[n-6]
# Multiply by 3:
#   3 D[n] = 9 D[n-1] + 12 D[n-2] - 17 D[n-3] - 30 D[n-4] - 31 D[n-5] + 63 D[n-6]
import gmpy2
from gmpy2 import mpz

D = [mpz(1), mpz(1), mpz(3), mpz(9), mpz(30), mpz(99), mpz(336),
     mpz(1134), mpz(3855), mpz(13086), mpz(44499), mpz(151263),
     mpz(514419), mpz(1749267), mpz(5949063)]

def recur_next(vals):
    # vals = last 7 terms, returns next using integer form
    n = len(vals)
    # 3*D[n] = 9 D[n-1]+12 D[n-2]-17 D[n-3]-30 D[n-4]-31 D[n-5]+63 D[n-6]
    num = (9*vals[-1] + 12*vals[-2] - 17*vals[-3] - 30*vals[-4]
           - 31*vals[-5] + 63*vals[-6])
    assert num % 3 == 0
    return num // 3

# extend
seq = list(D)
for n in range(15, 201):
    seq.append(recur_next(seq))

print("Predicted D(15..30):")
for n in range(15, 31):
    print(f"  D({n}) = {seq[n]}")

print("\nPredicted D(20) =", seq[20], "  statement D(20) = 9204559704")
print("  MATCH:", seq[20] == 9204559704)

mod = mpz(10)**9
print("Predicted D(100) % 10^9 =", seq[100] % mod, "  statement = 780166455")
print("  MATCH:", (seq[100] % mod) == 780166455)

print("\nPredicted D(10000) % 10^9 =", seq[10000] % mod)
