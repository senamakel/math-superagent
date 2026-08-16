"""Hand/machine check of the three witnesses and the candidate invariants,
independent of Z3 — the oracle the SMT encoding must agree with.

Witnesses: n=0 -> 2^0=1=1_3 [1]
           n=2 -> 2^2=4=11_3 [1,1]
           n=8 -> 2^8=256=100111_3 [1,1,1,0,0,1]  (low-to-high)
Contains-2 values: n=1 -> 2_3, n=3 -> 22_3, n=5 -> 1012_3.
"""
from erdos.oracle import digit_free

def low_digits(n, L):
    m = 2 ** n
    return [(m // (3 ** i)) % 3 for i in range(L)]

def polarity(d):
    return sum((-1) ** i * d[i] for i in range(len(d)))

def carry_doubling_total(d):
    # digit string d (low->high) is a base-3 value; compute total carries doubling it.
    carry = 0
    total = 0
    for a in d:
        t = 2 * a + carry
        carry = t // 3
        total += carry
    return total

print("=== witness expansions and free/not-free ===")
for n in (0, 2, 8, 1, 3, 5):
    print(f"n={n}: digit_free={digit_free(n)}  low10={low_digits(n,10)}")

print()
print("=== candidate invariants on the digit-free witnesses (0,2,8) ===")
for n in (0, 2, 8):
    d = low_digits(n, 40)
    c1 = sum(d)
    E = sum(d[i] for i in range(0, 40, 2))
    O = sum(d[i] for i in range(1, 40, 2))
    pol = polarity(d)
    car = carry_doubling_total(d)
    print(f"n={n}: c1={c1} E={E} O={O} Polarity={pol} "
          f"Polarity%3={pol%3} Polarity%2={pol%2} carry_total={car} carry%2={car%2}")
