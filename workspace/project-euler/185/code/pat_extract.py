#!/usr/bin/env python3
"""Drift-free regeneration of PE185 sequences from the shared source of truth.

Imports instance data only from lib.pe185 (single source of truth), so these
tables cannot drift from what the solvers used.  The secrets themselves are
the run's computed outputs: L5 oracle 39542 (brute force over all 10^5),
L16 4640261571849533 (scipy MILP, code/out/solution2_run.log, all 22 counts
verified + uniqueness by no-good cut).  Every extraction below re-verifies the
secret against every constraint before printing anything.

New structural angle not examined before: per-column digit-multiplicity.
For each position p, hitcount[p] = #guesses with g_i[p] == s[p] is exactly
the multiplicity of s[p] in column p.  Column p determines s[p] among the
10 digits; we test the conjecture "s[p] is a least-frequent digit of column
p" exactly, for both instances, and report every violation.
"""
from lib.pe185 import CONSTRAINTS5, CONSTRAINTS16

L5_SECRET = "39542"
L16_SECRET = "4640261571849533"


def verify(secret, constraints):
    L = len(secret)
    for g, c in constraints:
        assert len(g) == L
        hit = sum(1 for p in range(L) if secret[p] == g[p])
        assert hit == c, (g, c, hit)
    return True


def analyze(secret, constraints, label):
    L = len(secret)
    guesses = [g for g, _ in constraints]
    verify(secret, constraints)
    print("=" * 70)
    print(label, " L =", L, " secret =", secret)
    print("=" * 70)

    secret_digits = [int(ch) for ch in secret]
    hitcounts = [0] * L
    matchpos = []
    for g in guesses:
        pos = [p for p in range(L) if g[p] == secret[p]]
        for p in pos:
            hitcounts[p] += 1
        matchpos.append(pos)

    print("secret_digits :", secret_digits)
    print("hitcounts     :", hitcounts, " sum =", sum(hitcounts))
    print("dist          :", [secret.count(str(d)) for d in range(10)])

    # per-column multiplicities
    print()
    print("per-column multiplicity of s[p], min-multiplicity check:")
    rarest_ok = 0
    for p in range(L):
        col = [int(g[p]) for g in guesses]
        mult = {}
        for d in col:
            mult[d] = mult.get(d, 0) + 1
        m_s = mult.get(secret_digits[p], 0)
        m_min = min(mult.values()) if mult else 0
        rarest = [d for d, m in mult.items() if m == m_min]
        s_is_rarest = m_s == m_min
        rarest_ok += int(s_is_rarest)
        note = ""
        if m_s == 0:
            note = "  <-- s[p] ABSENT from column (forced digit)"
        print("  p=%02d s[p]=%d  mult(s[p])=%d  min=%d rarest=%s  s_is_rarest=%s%s"
              % (p, secret_digits[p], m_s, m_min, rarest, s_is_rarest, note))
    print("columns where s[p] achieves min multiplicity: %d / %d"
          % (rarest_ok, L))
    # per-guess match positions again (for the record, exact)
    print()
    for i, (g, c) in enumerate(constraints):
        print("  guess %02d %s c=%d matches at %s"
              % (i, g, c, matchpos[i]))
    print()


analyze(L5_SECRET, CONSTRAINTS5, "L=5 oracle (brute-force unique)")
analyze(L16_SECRET, CONSTRAINTS16, "L=16 main instance (MILP unique)")

# Cross-check: do the two data copies used by earlier runs agree with the
# shared source?  (pe185secret.py embeds its own GUESSES/COUNTS.)
import pe185secret as ps  # noqa: E402  (top-level module on PYTHONPATH)
print("pe185secret.py copy == lib.pe185 copy:",
      [g for g, _ in CONSTRAINTS16] == ps.GUESSES
      and [c for _, c in CONSTRAINTS16] == ps.COUNTS
      and L16_SECRET == ps.SECRET)