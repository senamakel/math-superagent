"""Extract core sequences from the guard-checked nu2 JSON for sequence tools.

d[n] = nu2(n) for n = 1..40000 (index 0 = n=1).
S(n) = (n-2) - 2*nu2(n)  signed excess
D(n) = S(n+1) - S(n)      increment
Prints the first `K` terms of several derived sequences as Python lists
so they can be pasted into analyze_sequence / find_linear_recurrence.
"""
import json

d = json.load(open('code/out/nu2_primes_xor_40000.json'))
# index: d[i] = nu2(i+1).  Guard checks: nu2(53)=18 -> d[52], nu2(64)=27 -> d[63], nu2(4000)=1975 -> d[3999]
assert d[52] == 18, d[52]
assert d[63] == 27, d[63]
assert d[3999] == 1975, d[3999]

K = 512
# nu2 from n=2: d[n-1] (nu2(2)=d[1]=0)
nu2 = [d[n-1] for n in range(2, 2+K)]
S = [(n-2) - 2*d[n-1] for n in range(2, 2+K)]
D = [S[i+1]-S[i] for i in range(len(S)-1)]

print("IDX  n  nu2  S")
for i in range(30):
    n = i+2
    print(i, n, nu2[i], S[i])

def fmt(name, L):
    print(f"\n{name} ({len(L)} terms):")
    print(L)

fmt("nu2", nu2)
fmt("S", S)
fmt("D", D)
print("\nS parity first 30 (should equal n mod 2):", [s % 2 for s in S[:30]])
print("(n-2) parity first 30:", [(i%2) for i in range(30)])
