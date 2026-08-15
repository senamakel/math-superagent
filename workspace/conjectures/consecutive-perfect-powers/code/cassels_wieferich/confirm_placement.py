"""Exact placement check for the double-Wieferich congruences, exact integer math.

Independent, self-contained confirmation (no floats) of the exact pairing:

    q^(p-1) = 1 (mod p^2)   [q on the LEFT,  square of p on the RIGHT]
    p^(q-1) = 1 (mod q^2)   [p on the LEFT,  square of q on the RIGHT]

using the catalogued minimal double-Wieferich pair (p,q) = (83, 4871), and the
mirror / swap negatives so the reader can SEE why the wrong placement fails.

Also sanity-check the reversal: if we (incorrectly) paired base-with-same-modulus
(p^(q-1) mod p^2 and q^(p-1) mod q^2), the congruences would hold trivially by
Fermat for unrelated reasons, so the placement is genuinely the non-trivial one.
"""
import itertools


def pow_mod(a, e, m):
    return pow(a, e, m)


def report(label, p, q):
    print(f"[{label}] (p,q)=({p},{q})")
    print(f"   q^(p-1) mod p^2 = {pow_mod(q, p-1, p*p)}   (want 1: q is base-p Wieferich)")
    print(f"   p^(q-1) mod q^2 = {pow_mod(p, q-1, q*q)}   (want 1: p is base-q Wieferich)")
    ok = pow_mod(q, p - 1, p * p) == 1 and pow_mod(p, q - 1, q * q) == 1
    # wrong placement for contrast
    wrong1 = pow_mod(q, p - 1, q * q) == 1
    wrong2 = pow_mod(p, q - 1, p * p) == 1
    print(f"   -> correct placement both? {ok}")
    print(f"   (wrong placement: q^(p-1) mod q^2==1 ? {wrong1}; p^(q-1) mod p^2==1 ? {wrong2})")
    return ok


# Known minimal double-Wieferich odd-prime pair (catalogued): (83, 4871).
report("correct-placement (83,4871)", 83, 4871)
print()
# A non-double-Wieferich pair for contrast, e.g. (3,5):
report("contrast (3,5) not double-Wieferich", 3, 5)
print()
# Known solution: p=2 even -- the congruences (odd-prime only) must fail,
# showing the hypothesis does the excluding, not the congruence.
report("known-solution (2,3)", 2, 3)
