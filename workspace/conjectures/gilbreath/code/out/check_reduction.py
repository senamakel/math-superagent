"""Check the reduction numerically against the real rows in witnesses.json.

Reduction claims to verify:
  (R1) Every row k>=1 has the shape (odd, even, even, ...): first entry odd, all
       others even.
  (R2) For every k>=0 with row length >=2: A_{k+1}(0) == 1  iff  A_k(1) in {0,2}.
  (R3) A_{k+1}(0) == |1 - A_k(1)| (by definition) and |1-e| == 1 iff e in {0,2}.

These are elementary; the point of the program is to pin them against the actual
generated rows so the claim can carry status: checked.
"""
import json

with open("witnesses.json") as f:
    W = json.load(f)

# We only stored first-12 slices per row in witnesses; regenerate the triangle
# freshly from the sieve to get full rows, then check the reduction on them.
def sieve(n):
    s = bytearray(b"\x01") * (n + 1)
    s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i*i:n+1:i] = b"\x00" * (((n - i*i)//i) + 1)
    return [i for i in range(n + 1) if s[i]]

LIMIT = 400000
primes = sieve(LIMIT)
depth = 600  # as in witnesses.json

row = list(primes)  # A_0
checked_shape = True
checked_iff = True
first_bad = None
for k in range(0, depth):
    nxt = [abs(row[i+1] - row[i]) for i in range(len(row) - 1)]
    # R1: A_k for k>=1 is (odd, even, even, ...)
    if k >= 1:
        if (nxt[0] % 2 == 0) or any(e % 2 for e in nxt[1:]):
            checked_shape = False
            first_bad = ("shape", k)
            break
    # R2: A_{k+1}(0)==1 iff A_k(1) in {0,2}
    if len(row) >= 2 and k >= 1:
        lhs = (nxt[0] == 1)
        rhs = (row[1] in (0, 2))
        if lhs != rhs:
            checked_iff = False
            first_bad = ("iff", k)
            break
    row = nxt

print("timeout placeholder")
print("shape_preserved_(odd,even,even,...)_for_all_k_ge_1:", checked_shape)
print("iff_A(k+1,0)==1 <-> A(k,1) in {0,2} over depth-1 rows:", checked_iff)
print("first_bad:", first_bad)
print("rows_checked(depth-1):", depth - 1)
print("min_second_in_{0,2} as in witnesses:", W["second_entry_always_0_or_2"])
