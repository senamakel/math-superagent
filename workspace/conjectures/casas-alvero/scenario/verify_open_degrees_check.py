"""Independent re-check of scenario/verify_open_degrees.py's comparison, per the
steering directive (config/directives.jsonl at=1786871082735).

Claim being verified: the published open-degree list <= 100 (Castryck et al
2012) should EQUAL the complement of the settled-family coverage (m<=5 families
p^k, 2p^k, 3p^k, 4p^k, 5p^k with their bad-prime exclusions, plus n<=8 and
n=12).  For a single degree n:
    consistency  :=  pub_open(n) == (not covered(m<=5)(n))
    genuine mismatch := pub_open(n) == covered(m<=5)(n)
The old (buggy) comparison collected pub != cov as a "mismatch", which flags the
CONSISTENT case.  This program shows the negative controls fail under the buggy
comparison and pass under the correct one.

The coverage predicate itself is intentionally unchanged: 20=4*5 and 28=4*7 are
open precisely because p=5 and p=7 are bad-prime exclusions in the 4p^k family,
and p=5 being bad in the 5p^k family too.  Only the comparison is under test.
"""
from sympy import isprime, factorint

def is_prime_power(n):
    return len(factorint(n)) == 1

def prime_power_base(n):
    f = factorint(n)
    if len(f) == 1:
        return list(f)[0], f[list(f)[0]]
    return None, None

EXCL5 = {2, 3, 7, 11, 131, 193, 599, 3541, 8009}
EXCL4 = {3, 5, 7}
EXCL3 = {2}

def covered_no67(n):
    """Covered by p^k, 2p^k, 3p^k, 4p^k, 5p^k (m<=5) families, or n<=8 / n=12."""
    if n <= 8 or n == 12:
        return True
    if is_prime_power(n):
        return True
    if n % 2 == 0 and is_prime_power(n // 2):
        return True
    if n % 3 == 0 and is_prime_power(n // 3):
        if prime_power_base(n // 3)[0] not in EXCL3:
            return True
    if n % 4 == 0 and is_prime_power(n // 4):
        if prime_power_base(n // 4)[0] not in EXCL4:
            return True
    if n % 5 == 0 and is_prime_power(n // 5):
        if prime_power_base(n // 5)[0] not in EXCL5:
            return True
    return False

published_open = [20, 24, 28, 30, 35, 36, 40, 42, 45, 48, 55, 56, 60, 63, 66,
                  70, 72, 77, 78, 80, 84, 88, 90, 91, 98, 99, 100]
pub_open = set(published_open)

def cov(n):  # coverage WITHOUT 6/7 families, as in the script
    return covered_no67(n)

# --- Negative controls: known settled (16 = 2^4) and known open (20 = 4*5). ---
def side(n, label):
    c = cov(n)
    pub = n in pub_open
    consistent_correct = (pub == (not c))
    buggy_flag = (pub != c)          # old comparison: flags pub != cov as mismatch
    print(f"  {label:28s} n={n:3d}: covered={c!s:5s} pub_open={pub!s:5s} "
          f"correct-consistent={consistent_correct!s:5s} buggy-would-flag={buggy_flag!s}")
    return consistent_correct, buggy_flag

print("=== Negative controls (directive) ===")
# Negative control: a known-settled degree (16=2^4) and a known-open degree (20)
# must each land on the CORRECT (consistent) side of the right comparison,
# while the OLD buggy comparison (pub != cov) falsely flags BOTH of them.
r16 = side(16, "known SETTLED (2^4)")
r20 = side(20, "known OPEN (4*5 and 5*2^2)")
assert r16 == (True, True), "16 consistent under correct; buggy( pub!=cov ) must falsely flag it"
assert r20 == (True, True), "20 consistent under correct; buggy( pub!=cov ) must falsely flag it"
# The directive's exact exemplar: n=28 (pub_open=True, cov=False) is PERFECT
# agreement, but the buggy comparison counted it as a mismatch.
r28 = side(28, "OPEN exemplar (4*7, p=7 bad)")
assert r28 == (True, True), "28 is consistent under correct; buggy falsely flags it"
print("  => Negative controls hold: under the CORRECT comparison 16, 20, 28 all land "
      "on the consistent side; under the OLD buggy (pub!=cov) comparison all three "
      "are FALSELY flagged as mismatches.  That proves the old comparison was inverted.")

# --- Full comparison over (8,100], n != 12 -----------------------------------
print("\n=== Full comparison over all n in (9..100), n != 12 ===")
news_mismatch = []   # correct: genuine mismatches (pub == cov)
buggy_mismatch = []  # old: collected pub != cov
for n in range(9, 101):
    if n == 12:
        continue
    c = cov(n)
    pub = n in pub_open
    if pub == c:
        news_mismatch.append(n)   # genuine mismatch: pub_open == covered
    if pub != c:
        buggy_mismatch.append(n)  # old false positives (consistency case)

print("  GENUINE mismatches (pub_open == covered):", news_mismatch)
print("  # genuine:", len(news_mismatch))
print("  OLD/BUGGY would have reported as 'mismatch':", buggy_mismatch)
print("  # old-buggy:", len(buggy_mismatch))
for n in news_mismatch:
    print(f"    n={n:3d}: covered={cov(n)} pub_open={n in pub_open}")
    pp = is_prime_power(n)
    print(f"       how covered/not: p^k={pp}")
    from sympy import primefactors
    print(f"       prime factors: {primefactors(n)}")
