"""Verify the refutation of candidate 1 (Kummer-Lucas q-binomial carry lift).

Candidate 1 asserts A_k(i) is the signed forward difference Delta_k(i) with the
absolute value applied only as a single end fold: A_k(i) = |Delta_k(i)|, where
Delta_k(i) = sum_{j<=k} (-1)^{k-j} C(k,j) A_0(i+j).

The run's claim fwd-diff-identity-refuted says this FAILS at (k,i)=(3,2):
|Delta_3(2)| = 4 but A_3(2) = 0 (inside the {0,2} block). Reproduce.
"""
import math

def primes_up_to(n):
    sieve = bytearray(b'\x01')*(n+1)
    sieve[0:2] = b'\x00\x00'
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            sieve[i*i::i] = b'\x00'*((n-i*i)//i+1)
    return [i for i in range(2, n+1) if sieve[i]]

A0 = primes_up_to(300)  # plenty of primes

def signed_fwd_diff(k, i):
    # Delta_k(i) = sum_{j<=k} (-1)^{k-j} C(k,j) A0(i+j)
    s = 0
    for j in range(k+1):
        s += ((-1)**(k-j)) * math.comb(k, j) * A0[i+j]
    return s

def gilbreath_triangle(depth):
    rows = [A0[:]]
    for _ in range(depth):
        r = rows[-1]
        nxt = [abs(r[i]-r[i+1]) for i in range(len(r)-1)]
        rows.append(nxt)
    return rows

rows = gilbreath_triangle(6)

print("Prime triangle rows A1..A3 (first 10 entries):")
for k in [1,2,3]:
    print(f"  A_{k} = {rows[k][:10]}")
print()

print("Checking candidate-1 identity A_k(i) == |signed Delta_k(i)|:")
violations = 0
first = None
for k in range(1, 4):
    for i in range(0, len(rows[k])-1):
        sd = signed_fwd_diff(k, i)
        if rows[k][i] != abs(sd):
            violations += 1
            if first is None:
                first = (k, i, rows[k][i], abs(sd))
print(f"  total violations among k=1..3: {violations}")
print(f"  first violation: (k,i)=({first[0]},{first[1]}), "
      f"A_k(i)={first[2]}, |Delta|={first[3]}")
