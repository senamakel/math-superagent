"""Independent re-verification of the L=16 secret 4640261571849533 against the
22 (guess, c_i) constraints transcribed in lib.pe185, plus a full brute-force
uniqueness check at L=5 and an exact digit-structure report on L=16.

This is my own numeric check (pattern finder) - not the solver's log.
"""
from lib.pe185 import L5, CONSTRAINTS5, L16, CONSTRAINTS16

def matches(s, g):
    return sum(1 for a, b in zip(s, g) if a == b)

# --- L=5 oracle reproduce ---
ok5 = [s for s in range(10**L5)
       if all(matches(f"{s:0{L5}d}", g) == c for _, (g, c) in enumerate(CONSTRAINTS5))]
print("L=5 solutions:", [f"{s:0{L5}d}" for s in ok5], "count:", len(ok5))

# --- L=16 verifier over the MILP answer given in MEMORY ---
ans = "4640261571849533"
print("L=16 answer length:", len(ans), "== L16:", len(ans) == L16)
allok = True
for g, c in CONSTRAINTS16:
    m = matches(ans, g)
    flag = "OK" if m == c else "FAIL"
    if m != c:
        allok = False
    print(f"  {g} : got {m} expect {c}  {flag}")
print("ALL 22 L=16 counts satisfied:", allok)

# --- structural report on the answer digits ---
digits = [int(ch) for ch in ans]
print("digits         :", digits)
print("digit histogram:", {d: digits.count(d) for d in range(10)})
print("sum of digits  :", sum(digits))
