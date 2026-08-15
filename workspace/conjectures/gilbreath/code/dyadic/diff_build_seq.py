#!/usr/bin/env python3
"""Directly diff the on-disk build_seq against candidate indexings to locate
the exact gap-to-bit convention that reproduces the claimed table."""

def build_ondisk(h_pattern, n_terms):
    period = len(h_pattern)
    q = [2, 3]
    while len(q) < n_terms:
        m = len(q)          # appending q_{m+1}; gap is q_m->q_{m+1}
        j = m - 2           # bit index
        q.append(q[-1] + (2 if h_pattern[j % period] else 4))
    return q[:n_terms]

def build_offset(h_bits, n_terms, offset):
    # gap number g counts from 1: gap g = q_{g+1}->q_{g+2}.
    # offset decides h index: j = g - offset  (we'll tabulate).
    qseq = [2, 3]
    while len(qseq) < n_terms:
        g = len(qseq) - 1
        j_bit = g - offset
        b = h_bits[j_bit]
        qseq.append(qseq[-1] + (2 if b else 4))
    return qseq[:n_terms]

# run with Thue-Morse and P=3 to find which offset reproduces on-disk
def tm_word(n):
    return [bin(j).count("1") & 1 for j in range(n)]

N = 60
tm = tm_word(N + 5)
p3 = [0, 0, 1] * ((N + 5) // 3 + 1)

ref_tm = build_ondisk(tm, N)
ref_p3 = build_ondisk(p3, N)
print("on-disk TM head:", ref_tm[:12])
print("on-disk P3 head:", ref_p3[:12])

for off in range(-2, 5):
    s_tm = build_offset(tm, N, off)
    s_p3 = build_offset(p3, N, off)
    d_tm = (s_tm == ref_tm)
    d_p3 = (s_p3 == ref_p3)
    print("offset %d (h[g-off] governs gap g=q_{g+1}->q_{g+2}): "
          "TM match %s  P3 match %s" % (off, d_tm, d_p3))
    print("    TM head:", s_tm[:10])
