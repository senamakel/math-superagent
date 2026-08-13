"""Corrected parity falsification: are giant rows odd beyond the event base rate?

Conventions (fixed after off-by-one): both JSON b arrays are 1-based rows,
b[i] = block length of row i+1.  Event row r (1-based): b[r] > b[r-1].
Giant = event with jump j = b[r]-b[r-1] > 1000.

Data sources:
  depth-1000 (2e7 sieve): code/out/blocks_depth1000.json — giant rows
      [35,57,65,69,95,97,111,113,127,131,135,147,162] (13; row 162 capped).
  3e8-wide run: code/out/wider_width_b_clean.json — giant rows
      [35,57,65,69,95,97,111,113,127,131,135,147,162,175] (14, all genuine).
  The two runs share the first 13 rows; the 3e8 run makes row 162 GENUINE
  (jump 4,323,712) and adds row 175.  So there are 14 DISTINCT giant events.

Null: giants are a random subset of event rows (hypergeometric on the
observed even/odd split of events).  Report the exact one-sided p-value.
Also report binomial vs event-base-rate and vs all-rows.

Exact arithmetic: math.comb.
"""
import json, math

def events_and_giants(br):
    ev = [i for i in range(1, len(br)) if br[i] > br[i - 1]]
    gi = [r for r in ev if br[r] - br[r - 1] > 1000]
    return ev, gi

def hypergeom_left(n_pop, k_pop, n_draw, k_obs):
    """P(X >= k_obs) for X ~ Hypergeometric(n_pop, k_pop, n_draw)."""
    total = math.comb(n_pop, n_draw)
    p = 0.0
    for kk in range(k_obs, min(k_pop, n_draw) + 1):
        p += math.comb(k_pop, kk) * math.comb(n_pop - k_pop, n_draw - kk) / total
    return p

b10 = json.load(open('code/out/blocks_depth1000.json'))['b']
bw = json.load(open('code/out/wider_width_b_clean.json'))['b']

for label, br, live in [
    ("depth-1000 (2e7), rows 1..161", b10, 161),
    ("3e8-wide, rows 1..238", bw, 238),
]:
    ev, gi = events_and_giants(br)
    ev = [e for e in ev if e <= live]
    gi = [g for g in gi if g <= live]
    n_ev = len(ev)
    odd_ev = sum(1 for e in ev if e % 2 == 1)
    even_ev = n_ev - odd_ev
    n_gi = len(gi)
    odd_gi = sum(1 for g in gi if g % 2 == 1)
    print(f"== {label} ==")
    print(f"  events {n_ev}: odd-row {odd_ev} ({odd_ev/n_ev:.3f}), "
          f"even-row {even_ev}")
    print(f"  giants {n_gi}: rows {gi}")
    print(f"  odd-row giants {odd_gi}/{n_gi}")
    # hypergeometric: draw n_gi giants from n_ev events, of which odd_ev odd
    p = hypergeom_left(n_ev, odd_ev, n_gi, odd_gi)
    print(f"  exact hypergeom P(>= {odd_gi} odd giants | event base "
          f"{odd_ev}/{n_ev}) = {p:.4f}")

print()
print("== distinct giant events over the combined record ==")
distinct = sorted(set([35, 57, 65, 69, 95, 97, 111, 113, 127, 131, 135, 147,
                       162, 175]))
odd = [d for d in distinct if d % 2 == 1]
print(f"{len(distinct)} distinct giant rows: {distinct}")
print(f"odd rows: {len(odd)}/{len(distinct)}; even-row giants: "
      f"{[d for d in distinct if d % 2 == 0]}")

# what are the giant digits?  since base rate ~0.72 odd, sanity check
# binomial p vs plain 1/2
n, k = len(distinct), len(odd)
p_half = 0.0
for kk in range(k, n + 1):
    p_half += math.comb(n, kk) * 0.5 ** n
print(f"vs plain 1/2: P(>= {k} of {n} odd rows | p=0.5) = {p_half:.4f}")

# bonus: do the giant rows coincide with something simpler, e.g. powers of 2
# or primes?  print factorish info
for d in distinct:
    print(f"  row {d}: odd={d%2==1}, mod4={d%4}, mod8={d%8}, "
          f"is_pow2={d & (d-1) == 0}")