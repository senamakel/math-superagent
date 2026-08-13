"""Does 'event index even' distinguish giant rows from non-giant rows?
Falsification check on the 13/14 parity regularity.

Data:
  depth-1000 prime rows 1..161 (blocks_depth1000.json): 60 regen events,
    13 giants (j>1000, incl. capped i=161).
  wider 3e8 run rows 1..238 (wider_width_b_clean.json): 74 events,
    14 genuine giants.
Tests:
  P1. Among regen events, fraction at even event index (i = row-1):
      giants vs non-giant events.  Is even-index a giant-marker?
  P2. Conditional: P(giant | event & even index) vs P(giant | event) —
      lift.  And P(giant | even index) vs base rate even indices.
  P3. exact hypergeometric/binomial p-value for 13/14 (or 12/13 + capped)
      under the null that giants are uniform over event indices
      (two-sided).
  P4. mod-2 profile of ALL event indices (60 and 74): is the event set
      itself parity-biased? (If events cluster at even rows, giants inherit
      it and the 13/14 is uninteresting.)
  P5. first rows of the b-series (k=1..20) — block-length parity.
Exact integer/float-free arithmetic except the p-values (math.comb exact,
statistics via bisection of the CDF).
"""
import json, math

with open('code/out/blocks_depth1000.json') as f:
    d10 = json.load(f)
b10 = d10['b']                       # rows 1..1000
ev10 = [i + 1 for i in range(1, len(b10)) if b10[i] > b10[i - 1]]  # event rows
gi = [r for r in ev10 if r <= 161]   # live-regime events (rows <=161)
giants10 = [r for r in gi if b10[r] - b10[r - 1] > 1000]
print(f"depth-1000 live events (rows 1..161): {len(gi)}, "
      f"giants: {giants10}")

with open('code/out/wider_width_b_clean.json') as f:
    w = json.load(f)
bw = w['b']
evw = [i + 1 for i in range(1, len(bw)) if bw[i] > bw[i - 1]]
giw = [r for r in evw if r <= 238]
giantsw = [35, 57, 65, 69, 95, 97, 111, 113, 127, 131, 135, 147, 162, 175]
print(f"3e8 live events (rows 1..238): {len(giw)}, giants: {giantsw}")

def parity_profile(events, label):
    even = [e for e in events if e % 2 == 0]
    odd = [e for e in events if e % 2 == 1]
    print(f"{label}: {len(events)} events, even-index {len(even)} "
          f"({len(even)/len(events):.3f}), odd-index {len(odd)}")
    return even, odd

e10, o10 = parity_profile(gi, "depth-1000 live events (rows 1..161)")
ew, ow = parity_profile(giw, "3e8 live events (rows 1..238)")
ee10 = [e for e in gi if e % 2 == 0]
print(f"depth-1000: even-index events = {ee10}")
print(f"3e8       : even-index events = {[e for e in giw if e % 2 == 0]}")

# expected number of even-index rows among 1..161: 80 even rows (2..160)
# P(giant event | even-index event):
def lift(events, giants, n_rows):
    ev = [e for e in events if e % 2 == 0]
    odd = [e for e in events if e % 2 == 1]
    g_ev = [g for g in giants if g % 2 == 0]
    g_odd = [g for g in giants if g % 2 == 1]
    print(f"giants at even event-index: {len(g_ev)}/{len(giants)}; "
          f"giants at odd event-index: {len(g_odd)}/{len(giants)}")
    print(f"  among even-index events: giant rate {len(g_ev)}/{len(ev)} = "
          f"{len(g_ev)/len(ev):.3f}; among odd-index events: "
          f"{len(g_odd)}/{max(1,len(odd))} = {len(g_odd)/max(1,len(odd)):.3f}")
    # binomial p under null P(giant)=uniform over event indices
    # exact two-sided binomial point-prob
    n, k = len(giants), len(g_ev)
    p = (len(ev)) / len(events)      # null prob of even among events
    def binom_pmf(kk):
        return math.comb(n, kk) * p ** kk * (1 - p) ** (n - kk)
    total = sum(binom_pmf(kk) for kk in range(n + 1))
    # two-sided: sum of pmf <= pmf(k)
    pmf_k = binom_pmf(k)
    pval = sum(binom_pmf(kk) for kk in range(n + 1) if binom_pmf(kk) <= pmf_k + 1e-15)
    print(f"exact binomial two-sided p (null P(even|event)={p:.3f}, "
          f"k={k}, n={n}): p={pval:.5f}")
    return pval

print()
print("depth-1000:")
lift(gi, giants10, 161)
print("3e8:")
lift(giw, giantsw, 238)

# combined 26 giants
allg = giants10 + giantsw   # 27 (13 + 14)
allev = sorted(set(gi + giw))
g_even = [g for g in allg if g % 2 == 0]
g_odd = [g for g in allg if g % 2 == 1]
print()
print(f"COMBINED: {len(allg)} giants, even-index {len(g_even)}, odd-index {len(g_odd)}")
print(f"  odd-index giants: {g_odd}")
# null: P(even) = fraction of even rows among 1..238
even_rows = 119
n, k = len(allg), len(g_even)
p = even_rows / 238
pmf = [math.comb(n, kk) * p**kk * (1 - p)**(n - kk) for kk in range(n + 1)]
pmf_k = pmf[k]
pval = sum(v for v in pmf if v <= pmf_k + 1e-15)
print(f"  null P(even-row) = {p:.3f} (rows 1..238): binomial two-sided "
      f"p = {pval:.4f}")

# mod-4 of giant event indices
print()
print("giant event-index mod 4:",
      [sorted(allg)[i] % 4 for i in range(len(allg))])