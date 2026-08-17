"""Study C(i,j;k) = number of k+1 length-k factors with '1' at positions i and j.

From the identity value(w) = sum_i w_i * 10^(k-1-i),
   Psi(k) = sum_{i,j} C(i,j;k) * 10^(2k-2-i-j).

We extract N(i;k)=C(i,i;k) and the full C(i,j;k) from structure.json and look
for the closed form. For a Sturmian word each length-k factor has floor/ceil(k*a)
ones, and the one-count per position should be a mechanical-word (floor) form.
"""
import json, os
from fractions import Fraction

with open(os.path.join(os.path.dirname(__file__),"..","out","structure.json")) as f:
    structure = json.load(f)

ks = sorted(int(k) for k in structure)

# print N(i;k) and C(i,0;k),C(i,1;k) rows for several k
for k in [8, 10, 15, 20, 30]:
    d = structure[str(k)]
    C = d["C"]  # keys "j,l"
    kk = k
    print(f"--- k={kk} ---")
    print("  N(i;k) = C(i,i):", {i: C[f"{i},{i}"] for i in range(kk)})
    # fractions: total ones sum and count
    vals = d["values"]
    # sum of ones over all factors
    total_ones = sum(w.count('1') for w in d["factors"])
    print(f"  total ones = {total_ones} (expect (k+1)*k*a ~ {(kk+1)*kk*0.38197:.0f})")
    # C(i,j) for j=0
    print("  C(i,0):", {i: C[f"{min(i,0)},{max(i,0)}"] for i in range(kk)})
    print("  C(i,1):", {i: C[f"{min(i,1)},{max(i,1)}"] for i in range(kk)})

# Try to find N(i;k) closed form N(i;k) = floor((k-i)*a + c) type
a = (3 - 5**0.5)/2
print()
print("Check N(i;k) = floor((k-i)*a+c): pick k=20")
k=20
d=structure[str(k)]
N = {i: d["C"][f"{i},{i}"] for i in range(20)}
for c in [1.0, 0.0, -0.5, 0.5]:
    matches = all(N[i]==int(((k-i)*a+c)) for i in range(20))
    print(f"  c={c}: all match floor((k-i)a+c)? {matches}")
