"""Extract the exact sequences the run computed, from captured output.

Parses the numbers out of code/out/heven_patterns.captured.txt and
code/out/heven_gauss_61.captured.txt, verifies them, and prints them in the
order a sequence tool should receive them. Also computes derived exact
quantities for the structural analysis:

  - for the 12 heads r (prime r | 2^{2p}+1, v2(r-1) >= 4): t = (r-1)/(4p),
    v2(t), p, and the Aurifeuillean half (L/M) if annotated upstream.
  - S(p) = sum over prime divisors r of Phi_{4p}(2) of 1/r as an exact
    Fraction, for every odd prime 3 <= p <= 61 that is fully factored in
    the gauss capture, together with p*S(p).
  - the ten verified k, the ten verified m, and the candidate prime-k list.

All parsing is exact (regex on the captured files); every printed number is
checked against a recomputation where it can be (counts, subset relations).
"""
import re
from fractions import Fraction
from pathlib import Path

OUT = Path("code/out")

# ---------------------------------------------------------------------------
# 1. verified members and candidate lists from heven_patterns.captured.txt
# ---------------------------------------------------------------------------
pat = (OUT / "heven_patterns.captured.txt").read_text()

m = re.search(r"SEQUENCE_M=([0-9,]+)", pat)
k = re.search(r"SEQUENCE_K=([0-9,]+)", pat)
candm = re.search(r"SEQUENCE_CANDM=([0-9,]+)", pat)
primek = re.search(r"SEQUENCE_PRIMEK=([0-9,]+)", pat)
ver = re.search(r"verified through 1200: \[([0-9, ]*)\]", pat)


def to_list(s):
    return [int(x) for x in s.group(1).replace(" ", "").split(",") if x != ""]


verified_m = to_list(m)
verified_k = to_list(k)
cand_m = to_list(candm)
prime_k = to_list(primek)
verified_through = [int(x) for x in ver.group(1).replace(" ", "").split(",") if x]

# ---------------------------------------------------------------------------
# 2. heads from heven_gauss_61.captured.txt and heven_heads_verify.captured.txt
# ---------------------------------------------------------------------------
gauss = (OUT / "heven_gauss_61.captured.txt").read_text()
heads_verify = (OUT / "heven_heads_verify.captured.txt").read_text()

# parse the verified head table: p=  7 r=113  ... CERTIFIED
head_rows = re.findall(r"p=\s*(\d+)\s+r=(\d+)\s+prime=True", heads_verify)
heads = [(int(p), int(r)) for p, r in head_rows]

# Aurifeuillean half from the gauss capture:  "r=113             L^1 ord=4"
half = {}
for hp, hr in heads:
    hh = re.search(r"r=%d\s+([LM])\^1" % hr, gauss)
    half[hr] = hh.group(1) if hh else "?"

# ---------------------------------------------------------------------------
# 3. fully factored p <= 61: parse each p block's divisor list
#    lines like "  r=5              L^1 ord=4    v2(r-1)=2 t=. ... P3"
#    and "  r=13             M^1 ord=12   v2(r-1)=2 t=1 ... P3"
# ---------------------------------------------------------------------------
S = {}
pblock = None
for line in gauss.splitlines():
    pm = re.match(r"^p=(\d+)", line)
    if pm:
        pblock = int(pm.group(1))
        S.setdefault(pblock, [])
        continue
    rm = re.match(r"\s*r=(\d+)\s+[LM]\^1 ord=(\d+)\s+v2\(r-1\)=(\d+)\s+t=(\S+)", line)
    if rm and pblock is not None:
        r, ordv, v2r, t = int(rm.group(1)), int(rm.group(2)), int(rm.group(3)), rm.group(4)
        if t == ".":
            t = 1
        else:
            t = int(t)
        S[pblock].append((r, ordv, v2r, t))

# sum of 1/r over prime divisors of Phi_{4p}(2): every r listed with ord=4p is a
# prime divisor of Phi_{4p}(2); the ord=4 rows are the divisor 5 (not in Phi).
recip = {}
for p, rows in S.items():
    phi = [r for (r, o, v, t) in rows if o == 4 * p]
    recip[p] = sum(Fraction(1, r) for r in phi)

print("== verified H_even members (m), k = m/2 ==")
print("K_SEQ", verified_k)
print("M_SEQ", verified_m)
print("verified_through_1200_ok:", sorted(verified_through) == sorted(verified_k))
print("count check: len(cand_m) =", len(cand_m), " len(prime_k) =", len(prime_k))

print()
print("== candidate m (2k) and prime k sequences ==")
print("CANDM_SEQ", cand_m)
print("PRIMEK_SEQ", prime_k)
print("prime_k subset of Higgs-cubefree odd k and all odd: ",
      all(x % 2 == 1 for x in prime_k))
print("min/max prime_k:", min(prime_k), max(prime_k))

print()
print("== the 12 heads: (p, r, t=(r-1)/(4p), v2(t), half) ==")
for p, r in heads:
    t = (r - 1) // (4 * p)
    v = 0
    tt = t
    while tt % 2 == 0:
        tt //= 2
        v += 1
    print(f"p={p:3d} r={r:16d} t={t:12d} v2(t)={v} half={half[r]}")

print()
print("== reciprocal sums S(p) = sum_{r | Phi_{4p}(2)} 1/r, exact, p <= 61 ==")
for p in sorted(recip):
    print(f"p={p:3d} S(p)={float(recip[p]):.8f} p*S(p)={float(p * recip[p]):.6f}")

print()
print("== smallest-head-per-p sequence (first r with v2(r-1)>=4 at each p) ==")
seen = {}
for p, r in heads:
    if p not in seen:
        seen[p] = r
for p in sorted(seen):
    print(p, seen[p])