"""Verify the k2=5 genus closed form against the computed table, and compare
its structure to the known k2=3, k2=4 forms (periodic-in-m drop at multiples
of the small index m)."""
G = [10,12,14,16,16,20,22,24,26,26,30,32,34,36,36,40,42,44,46]  # (k1,5), k1=6..24
K = list(range(6,25))

def g5(k1):
    # closed form: 2k1-2, but 2k1-4 at multiples of 5
    return (2*k1-2) - (2 if k1 % 5 == 0 else 0)

mism = [(k1,g,g5(k1)) for k1,g in zip(K,G) if g5(k1)!=g]
print("k2=5 closed form g(k1)=2k1-2 (or 2k1-4 if 5|k1):",
      "NONE" if not mism else mism)

# first differences -> period 5 pattern 2,2,2,0,4
diffs = [G[i+1]-G[i] for i in range(len(G)-1)]
print("first differences:", diffs)
print("claim period-5 diff pattern [2,2,2,0,4]:",
      all(diffs[i]==[2,2,2,0,4][i%5] for i in range(len(diffs))))

print("\n--- Compare structure to small-column families ---")
def g3(n):  # pair {3,n}
    return (n-1) if n%3!=0 else (n-2)
def g4(n):  # pair {4,n}
    if n%2==1: return 3*(n-1)//2
    else: return 3*(n-2)//2 + (1 if n%4==2 else 0)
def g5_(n):
    return (2*n-2) - (2 if n%5==0 else 0)
print("k2=3: g=n-1 except multiples of 3 -> n-2  (drop structure, period 3)")
print("k2=4: periodic mod 4 (odd/even split)")
print("k2=5: g=2n-2 except multiples of 5 -> 2n-4  (period 5)")

# Also test candidate extension: does k2=3's 2*floor(drop) idea generalize?
# For each small column m, genus ~ (m-1)n - something, with periodic drop mod m.
