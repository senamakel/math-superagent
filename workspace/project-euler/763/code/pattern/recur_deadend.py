# Characterize the order-7 recurrence extrapolation precisely.
from gmpy2 import mpz

D = [1, 1, 3, 9, 30, 99, 336, 1134, 3855, 13086, 44499, 151263,
     514419, 1749267, 5949063]
D = [mpz(x) for x in D]

# 3 D[n] = 9 D[n-1]+12 D[n-2]-17 D[n-3]-30 D[n-4]-31 D[n-5]+63 D[n-6]
def rec3(vals):
    return (9*vals[-1] + 12*vals[-2] - 17*vals[-3] - 30*vals[-4]
            - 31*vals[-5] + 63*vals[-6])

seq = list(D)
for n in range(15, 22):
    num = rec3(seq)
    q, r = divmod(num, 3)
    print(f"n={n}: 3*D(n) numerator = {num}, /3 = {q} rem {r}  -> integer: {r==0}")
    if r == 0:
        seq.append(q)
    else:
        print("  !! NON-INTEGER: recurrence cannot equal integer D(n). DEAD END.")
        break

print("\nGiven D(20)=9204559704 (statement). The recurrence does not even reach")
print("an integer at n=18, so it can never reproduce D(20) or D(100).")
