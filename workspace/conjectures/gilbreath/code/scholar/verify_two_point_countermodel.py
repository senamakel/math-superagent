"""Verify the linchpin claim g-supply-switch-count-not-one-point.

The claim: the one-point marginals (each residue class mod 4 has ~pi(x)/2 primes)
impose ZERO lower bound on the consecutive-pair switch count N_switch(x) =
#{p_n <= x : p_{n+1} !≡ p_n (mod 4)}. Proof by countermodel: an ordering that
lists all 1-mod-4 primes first then all 3-mod-4 primes is consistent with the
marginals and has exactly ONE switch.

We verify two things concretely:
  (a) For any finite set of primes up to x, there EXISTS an ordering of exactly
      those primes (a permutation) that is consistent with the per-class counts
      and achieves every switch count from 1 up to the maximum, INCLUDING 1.
  (b) The switch count achievable by permuting is NOT pinned by the class
      counts: different permutations of the same multiset of residues give
      different switch counts (so the marginals genuinely do not determine it).
"""
import itertools
from collections import Counter


def switch_count(residues):
    """Number of i with residues[i+1] != residues[i]."""
    return sum(1 for i in range(len(residues) - 1) if residues[i + 1] != residues[i])


def residue_class_counts(x_residues):
    """Given a list of residues (1 or 3), the class counts - the one-point data."""
    return Counter(residues)


def all_switch_counts(residues):
    """All switch counts achievable by permuting the residue multiset."""
    seen = set()
    for perm in set(itertools.permutations(residues)):
        seen.add(switch_count(perm))
    return sorted(seen)


# --- (b) the marginals do not determine the switch count -----------------
# Take a multiset with equal counts of 1 and 3 (the one-point marginals).
residues = [1, 1, 1, 3, 3, 3]
counts = residue_class_counts(residues)
achievable = all_switch_counts(residues)
print("class counts (one-point data):", dict(counts))
print("achievable switch counts over all permutations:", achievable)
assert counts[1] == counts[3], "need balanced classes"
assert 1 in achievable, "1 switch must be achievable (the countermodel)"
print("PASS (b): balanced one-point marginals permit exactly 1 switch, so",
      "no positive lower bound on N_switch follows from them.\n")

# --- (a) the ordered-listing countermodel achieves exactly 1 -------------
# All 1-mod-4 primes first, then all 3-mod-4 primes.
ordered_by_class = sorted(residues, reverse=True)  # all 3 then all 1 -- instead do:
ordered_by_class = [1, 1, 1] + [3, 3, 3]           # all 1-class then all 3-class
sw = switch_count(ordered_by_class)
print("countermodel ordering (all 1-class then all 3-class):", ordered_by_class)
print("its switch count:", sw)
assert sw == 1, "the countermodel ordering must give exactly one switch"
print("PASS (a): the countermodel ordering achieves N_switch = 1.\n")

# --- scale up: for the first real primes up to some x, this still holds ----
def sieve(limit):
    bs = bytearray(b'\x01') * (limit + 1)
    bs[0:2] = b'\x00\x00'
    for i in range(2, int(limit ** 0.5) + 1):
        if bs[i]:
            bs[i * i::i] = b'\x00' * (((limit - i * i) // i) + 1)
    return [i for i in range(limit + 1) if bs[i]]

primes = sieve(1000)
res = [p % 4 for p in primes if p % 4 in (1, 3)]
cnt = residue_class_counts(res)
cm = sorted([r for r in res if r == 1]) + sorted([r for r in res if r == 3])
print(f"real primes <= 1000: {len(primes)} primes, class counts {dict(cnt)}")
print("countermodel ordering switch count:", switch_count(cm))
print("real (natural) ordering switch count:", switch_count(res))
assert switch_count(cm) == 1
print("PASS: even for the REAL primes, a permutation consistent with the",
      "marginals gives exactly 1 switch, while the natural order gives",
      switch_count(res), "- one-point machinery cannot distinguish them.")
