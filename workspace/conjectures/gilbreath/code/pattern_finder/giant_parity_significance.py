"""Final significance: do giants prefer EVEN pre-jump event rows beyond the
event base rate?  Plus boundary-state parity profile.

Conventions (authoritative): b[i] = {0,2}-block length of row i+1 (1-based).
  Event at pre-jump row r (1-based): b[r] > b[r-1].  Giant: jump > 1000.
  Pre-jump rows of the giants are the r for which the (2,4)-pair fires.

Datasets:
  2e7: blocks_depth1000.json (rows 1..161 live) -> 43 events, 13 giants.
  3e8: wider_width_b_clean.json (rows 1..238 live) -> 51 events, 15 giants.

Checks:
  A. exact hypergeometric P(>= k even giants | event even base) for each
     dataset and for the distinct-union set (14 giants, event base from 3e8).
  B. FOR THE RECORD the exception i=161 is genuine at 3e8 (landing flooring
     10,834,187 >> 1000), so "giants are even-row, except i=161" is a
     statement with one REAL exception -- state it that way.
  C. boundary parity: using e_bits/i_bits (halved edge, next-to-edge) and
     intruder c at 2e7 rows 1..161: split (e=2), (c=4), (e=2 & c=4) by row
     parity and by pre-jump-event parity.  The event set = (e=2 & c=4):
     does the event base itself prefer even rows, and do GIANT events among
     the even-row events prefer even rows further?
"""
import json, math

def hypergeom_upper(n_pop, k_pop, n_draw, k_obs):
    """P(X >= k_obs), X ~ Hypergeom(n_pop, k_pop, n_draw)."""
    total = math.comb(n_pop, n_draw)
    p = 0.0
    for kk in range(k_obs, min(k_pop, n_draw) + 1):
        p += math.comb(k_pop, kk) * math.comb(n_pop - k_pop, n_draw - kk) / total
    return p

b10 = json.load(open('code/out/blocks_depth1000.json'))['b']
bw = json.load(open('code/out/wider_width_b_clean.json'))['b']

def events_giants(br, live):
    ev = [i for i in range(1, live + 1) if br[i] > br[i - 1]]
    gi = [r for r in ev if br[r] - br[r - 1] > 1000]
    return ev, gi

for label, br, live in [("2e7 rows 1..161", b10, 161),
                        ("3e8 rows 1..238", bw, 238)]:
    ev, gi = events_giants(br, live)
    even_ev = sum(1 for e in ev if e % 2 == 0)
    even_gi = sum(1 for g in gi if g % 2 == 0)
    print(f"== {label} ==")
    print(f"  events {len(ev)} (even {even_ev}, {even_ev/len(ev):.3f}), "
          f"giants {len(gi)} (even {even_gi}, {even_gi/len(gi):.3f})")
    print(f"  giant pre-jump rows {gi}")
    print(f"  hypergeom P(>= {even_gi} even giants | event even base "
          f"{even_ev}/{len(ev)}) = "
          f"{hypergeom_upper(len(ev), even_ev, len(gi), even_gi):.5f}")

# distinct union (de-duplicated giant events; the 3e8 makes row 161 real)
union = sorted(set([34, 56, 64, 68, 94, 96, 110, 112, 126, 130, 134, 146,
                    161, 174, 238]))
u_even = [g for g in union if g % 2 == 0]
u_odd = [g for g in union if g % 2 == 1]
print(f"\n== distinct-union giants (2e7 + 3e8) ==")
print(f"  {len(union)} giants, even pre-jump {len(u_even)} "
      f"({len(u_even)/len(union):.3f}), odd {u_odd}")
evw, giw = events_giants(bw, 238)
even_evw = sum(1 for e in evw if e % 2 == 0)
p = hypergeom_upper(len(evw), even_evw, len(union), len(u_even))
print(f"  hypergeom vs 3e8 event base ({even_evw}/{len(evw)}): P = {p:.5f}")
# and with the artifact row 238 removed (it is capped: jump a lower bound)
gen = [g for g in union if g != 238]
g_even = sum(1 for g in gen if g % 2 == 0)
p2 = hypergeom_upper(len(evw), even_evw, len(gen), g_even)
print(f"  minus capped 238 ({len(gen)} genuine): P = {p2:.5f}")
print(f"  the exception i=161: at 3e8 it is GENUINE (jump 4323712, landing "
      f"flooring 10834187) -- a real odd-row giant.")

# ---- boundary-state parity (2e7 rows 1..161) ----
print("\n== boundary-state parity profile (2e7, rows 1..161) ==")
def bits(fn):
    with open(fn) as f:
        return [int(t) for t in f.read().split()]
e_bits = bits('code/out/pattern_finder_outputs/e_bits.txt')
c = []
with open('code/out/pattern_finder_outputs/c.txt') as f:
    for tok in f.read().split():
        c.append(None if tok == 'None' else int(tok))
n = min(161, len(e_bits), len(c))
def split(pred):
    ev = sum(1 for k in range(n) if (k + 1) % 2 == 0 and pred(k))
    od = sum(1 for k in range(n) if (k + 1) % 2 == 1 and pred(k))
    return ev, od
e2_e, e2_o = split(lambda k: e_bits[k] == 1)          # edge == 2
c4_e, c4_o = split(lambda k: c[k] == 4)               # intruder == 4
b_e, b_o = split(lambda k: e_bits[k] == 1 and c[k] == 4)  # event = (2,4)
print(f"edge=2  : even-row {e2_e}, odd-row {e2_o}  (even frac "
      f"{e2_e/(e2_e+e2_o):.3f})")
print(f"intruder=4: even-row {c4_e}, odd-row {c4_o}  (even frac "
      f"{c4_e/(c4_e+c4_o):.3f})")
print(f"(e=2,c=4) events: even-row {b_e}, odd-row {b_o}  (even frac "
      f"{b_e/(b_e+b_o):.3f})")

# giants vs event rows: distribution of jumps by parity of pre-jump row
print("\n== giant jumps by pre-jump-row parity (3e8) ==")
for r in union:
    j = bw[r] - bw[r - 1]
    print(f"  pre-jump row {r:4d} {'EVEN' if r % 2 == 0 else 'ODD '}: "
          f"jump {j:9d}, land {bw[r]:9d}")