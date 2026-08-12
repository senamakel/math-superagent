"""Two falsifiable structural hypotheses about the PE185 L=16 secret.

H1: secret[p] is the modal digit of the guess column at position p
    (column-majority rule). Falsifiable position by position.
H2: the 31 within-guess pairs of match positions (sum_i C(c_i,2)) form a
    near-uniform design over the 120 position pairs. Falsifiable by the
    pair-coverage histogram.
Also reported: per-guess position-independent digit-overlap with the secret
(multiset overlap) next to c_i - to see whether wrong-position matches carry
any regular relation.

All checks exact; no sampling.
"""
from collections import Counter

GUESSES = [
    "5616185650518293", "3847439647293047", "5855462940810587",
    "9742855507068353", "4296849643607543", "3174248439465858",
    "4513559094146117", "7890971548908067", "8157356344118483",
    "2615250744386899", "8690095851526254", "6375711915077050",
    "6913859173121360", "6442889055042768", "2321386104303845",
    "2326509471271448", "5251583379644322", "1748270476758276",
    "4895722652190306", "3041631117224635", "1841236454324589",
    "2659862637316867",
]
COUNTS = [2, 1, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 1, 2, 0, 2, 2, 3, 1, 3, 3, 2]
SECRET = "4640261571849533"
L = len(SECRET)

# --- H1: column majority ---
agree = 0
for p in range(L):
    col = Counter(g[p] for g in GUESSES)
    top = col.most_common(2)          # ties: [d1, c1], [d2, c2]
    strict_majority = top[0][0] if (len(top) == 1 or top[0][1] > top[1][1]) else None
    hit = SECRET[p] == top[0][0]
    agree += hit
    print("pos %2d  column freq %s  col-mode=%s  secret=%s  secret_is_mode=%s"
          % (p, dict(sorted(col.items())), top[0][0], SECRET[p], hit))
print("H1: positions where secret[p] == column mode:", agree, "of", L)
print("H1: positions where secret[p] == STRICT column mode:",
      sum(1 for p in range(L)
          if SECRET[p] == Counter(g[p] for g in GUESSES).most_common(1)[0][0]),
      "of", L)

# --- H2: pair coverage of match-position sets ---
paircount = Counter()
for g in GUESSES:
    pos = [p for p in range(L) if g[p] == SECRET[p]]
    for i in range(len(pos)):
        for j in range(i + 1, len(pos)):
            paircount[(pos[i], pos[j])] += 1
total_pairs = sum(paircount.values())
print("\nH2: within-guess match-position pairs:", total_pairs,
      "(expected sum C(c_i,2) =",
      sum(c * (c - 1) // 2 for c in COUNTS), ")")
print("H2: distinct position-pairs covered:", len(paircount), "of",
      L * (L - 1) // 2)
hist = Counter(paircount.values())
print("H2: coverage histogram (times-covered: #pairs):", dict(sorted(hist.items())))

# --- position-independent digit overlap per guess ---
print("\nper-guess multiset overlap with secret vs c_i:")
for i, g in enumerate(GUESSES):
    ov = sum((Counter(g) & Counter(SECRET)).values())
    print("  %02d  overlap=%2d  c=%d" % (i, ov, COUNTS[i]))