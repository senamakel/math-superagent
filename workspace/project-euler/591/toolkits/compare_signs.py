"""Compare positive-only (solution.py, results_full.txt) vs both-sign (solution_bothsides.py,
results_full_bothsides.txt) at n=1e13: verify both-sign is never worse and strictly better
where b sign flipped; recheck S.
"""
import math, mpmath as mp
mp.mp.dps = 50
PI = mp.mpf('3.14159265358979323846264338327950288419716939937510')

pos = {}
for line in open('/workspace/results_full.txt'):
    p = line.split()
    if p and p[0].isdigit():
        pos[int(p[0])] = (int(p[1]), int(p[2]), int(p[3]))
both = {}
for line in open('/workspace/results_full_bothsides.txt'):
    p = line.split()
    if p and p[0].isdigit():
        both[int(p[0])] = (int(p[1]), int(p[2]), int(p[3]))

def err_of(d, b, a):
    sd = mp.sqrt(d)
    return abs(PI - (a + b*sd))

worse = []
better = []
same = 0
for d in both:
    if d not in pos: continue
    e_pos = err_of(d, pos[d][0], pos[d][1])
    e_both = err_of(d, both[d][0], both[d][1])
    if e_both > e_pos + mp.mpf('1e-30'):
        worse.append((d, e_pos, e_both))
    elif e_both < e_pos - mp.mpf('1e-30'):
        better.append((d, mp.nstr(e_pos,5), mp.nstr(e_both,5), pos[d][2], both[d][2]))
    else:
        same += 1
print(f"same={same}, strictly better with both-sign={len(better)}, worse={len(worse)}")
print("better cases (d, err_pos, err_both, |a|_pos, |a|_both):")
for row in better:
    print("  ", row)
print("worse:", worse)
Spos = sum(pos[d][2] for d in pos)
Sboth = sum(both[d][2] for d in both)
print("S positive-only:", Spos, " S both-sign:", Sboth, " delta:", Sboth-Spos)
# verify S both matches file
print("S both from file:", [int(l.split()[1]) for l in open('/workspace/results_full_bothsides.txt') if l.startswith('S')])