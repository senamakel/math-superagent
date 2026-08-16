#!/usr/bin/env python3
"""INDEPENDENT verification of the fair-variance Null/Ratio-B capture for the
SUPPLY fold, via a genuinely different oracle path.

CAPTURE (code/out/fair_variance_at_40000.txt) used lib.supply_fold.s_sos:
the submask-PRODUCT zeta in the +-1 algebra ((-1)^{T(n,d)} = prod_{s subseteq d}
tau_{n-1-s}).  It reported nu2[40000]=20081 and, for the sequence
{a_n = nu2(n)/n : n=2..N}, prefix population variance s2_N with Ratio A =
s2_N*4N and Ratio B = s2_N*4N/log(N) (the correct log(N)/(4N) null):
1.4428@1000, 1.3921@4000, 1.3605@10000, 1.3368@20000, 1.3155@40000,
Ratio A = 13.9394@40000; deep-tail dip density c=None over [36000,40000].

THIS SCRIPT's oracle is the DIRECT submask-XOR decomposition of the same fold,
T(n,d) = XOR over bitwise submasks s of d of h[n-1-s], evaluated by
  (L) a from-scratch literal per-submask expansion (the definition itself, XOR
      over the submask descent (o-1)&d),
  (Z) an exact subset-XOR zeta transform in the 0/1 algebra (numpy uint8;
      g[d] = XOR_{s subseteq d} b_s, b_s = h[n-1-s], via g[x] ^= g[x^bit]),
      the closed form of the SAME direct decomposition -- algebraically
      different from s_sos (bit XOR, no +-1 products),
  (D) lib.supply_fold.s_direct (the library's own literal direct oracle), kept
      as a second literal route.
Four-way agreement on n=2..200 with s_sos (part a); checkpoints nu2(4000)=1975,
nu2(53)=18, nu2(64)=27, nu2(40000)=20081 (part b); full exact prefix to
N_ZETA=40000 by (Z) -- the efficient direct route -- with (L) full literal to
N_LIT=4000 and multi-oracle samples (L/Z/D/s_sos) beyond that (parts c, d).

ALL NUMBERS ARE MEASURED, NOT PROVED.  Exact integer / Fraction arithmetic
everywhere except display; Ratio A/B floats only at display.

Complexity: (L) per-n O(sum_{d<n} 2^popcount(d)) = O(n^{log_2 3}) (oracle),
full literal prefix to 4000 parallelised; (Z) per-n O(n log n), O(2^ceil log n)
space, full prefix to 40000 parallelised; samples beyond via all routes.
"""
import os
import time
import math
import json
import multiprocessing as mp
from fractions import Fraction

import numpy as np

from lib.supply_fold import s_sos, s_direct
from lib.primes import h_string
from lib.direct_fold import nu2_literal_direct, nu2_xor_zeta

N_ZETA = 40000          # full exact prefix by the XOR-zeta direct route
N_LIT = 10000           # full literal (from-scratch oracle) prefix
CHECKPOINTS = [1000, 4000, 10000, 20000, 40000]
# multi-oracle sample values beyond the literal range (dyadic stress + spread)
SAMPLES = [1400, 2000, 4096, 6000, 8192, 10000, 15000, 16384, 20000, 24000,
           30000, 32768, 36000, 38000, 39999]
NP = int(os.environ.get("NPROC", "28"))

OUT = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "out",
    "fair_variance_independent_verify.txt"))
os.makedirs(os.path.dirname(OUT), exist_ok=True)

CAPTURE_RB = {1000: 1.4428, 4000: 1.3921, 10000: 1.3605,
              20000: 1.3368, 40000: 1.3155}
CAPTURE_RA = {1000: 9.9665, 4000: 11.5461, 10000: 12.5309,
              20000: 13.2389, 40000: 13.9394}
CAPTURE_S2 = {1000: 2.49163e-3, 4000: 7.21633e-4, 10000: 3.13272e-4,
              20000: 1.65487e-4, 40000: 8.71213e-5}
CAPTURE_MU = {1000: 0.491111, 4000: 0.497383, 10000: 0.498860,
              20000: 0.499381, 40000: 0.499671}
CAPTURE_NU2 = {53: 18, 64: 27, 4000: 1975, 40000: 20081}


# ---------------------------------------------------------------------------
# inputs
# ---------------------------------------------------------------------------
def prime_h(n):
    """h[j] = [q_{j+2} != q_{j+1} mod 4] for j = 0..n-1 (length n)."""
    return h_string(n + 2)[:n]


def all_ones_h(n):
    return [1] * n


def thue_morse_h(n):
    return [bin(j).count("1") % 2 for j in range(n)]


def as_u8(h):
    return np.asarray(h, dtype=np.uint8)


FAMILIES = [("PRIMES", prime_h), ("ALL-ONES", all_ones_h),
            ("THUE-MORS", thue_morse_h)]


# ---------------------------------------------------------------------------
# parallel full prefixes
# ---------------------------------------------------------------------------
def _lit_worker(args):
    lo, hi, h = args
    return [(n, nu2_literal_direct(n, h)) for n in range(lo, hi + 1)]


def _zeta_worker(args):
    lo, hi, h = args
    res = []
    for n in range(lo, hi + 1):
        res.append((n, nu2_xor_zeta(n, h[:n])))
    return res


def full_prefix(N, h, worker, nproc):
    nu2 = [0] * (N + 1)
    chunk = max(1, (N - 1) // nproc)
    ranges, lo = [], 2
    while lo <= N:
        hi = min(N, lo + chunk - 1)
        ranges.append((lo, hi, h))
        lo = hi + 1
    with mp.Pool(nproc) as pool:
        for part in pool.imap_unordered(worker, ranges, chunksize=1):
            for (n, v) in part:
                nu2[n] = v
    return nu2


def prefix_literal(N, h, nproc):
    return full_prefix(N, h, _lit_worker, nproc)


def prefix_zeta(N, h, nproc):
    return full_prefix(N, h, _zeta_worker, nproc)


def _sos_worker(args):
    n, h = args
    _, ones = s_sos(n, h[:n])
    return (n, ones)


def _sdirect_worker(args):
    n, h = args
    S, ones = s_direct(n, h[:n])
    return (n, S, ones)


def sample_agreement(ns, h, h8, nproc):
    """All routes on every n in ns. Returns {n: {L,D,Z,SOS}}. Also verifies
    S == (n-2) - 2*ones for the direct route."""
    with mp.Pool(nproc) as pool:
        lit = {}
        for part in pool.imap_unordered(_lit_worker,
                                        [(n, n, h) for n in ns]):
            lit.update(dict(part))
    with mp.Pool(nproc) as pool:
        sdir = {}
        for part in pool.imap_unordered(_sdirect_worker, [(n, h) for n in ns]):
            sdir.update({part[0]: (part[1], part[2])})
    with mp.Pool(nproc) as pool:
        sos = {}
        for part in pool.imap_unordered(_sos_worker, [(n, h) for n in ns]):
            sos.update(dict([part]))
    zeta = {n: nu2_xor_zeta(n, h8[:n]) for n in ns}
    out = {}
    for n in ns:
        L = lit[n]
        Z = zeta[n]
        D, S = sdir[n][1], sdir[n][0]
        SOS = sos[n]
        nd = n - 2
        out[n] = dict(L=L, Z=Z, D=D, S=S, SOS=SOS,
                      Srel=(S == nd - 2 * D))
        assert L == Z == D == SOS, ("route mismatch at n=%d" % n, out[n])
    return out


# ---------------------------------------------------------------------------
# exact prefix statistics (identical convention to the capture)
# ---------------------------------------------------------------------------
def reduce_stats(nu2, N, checkpoints):
    """Running mean mu and population variance s2 of a_n = nu2(n)/n over
    n=2..N (Welford, exact Fractions, count = N-1 values) plus the running
    (1/N)*sum 1/(4n) null accumulator. Mirrors the capture's reduce_stats so
    the checkpoints are directly comparable."""
    mu, M2 = Fraction(0), Fraction(0)
    cnt = 0
    cp = {}
    null_sum = Fraction(0)
    for n in range(2, N + 1):
        r = Fraction(nu2[n], n)
        cnt += 1
        delta = r - mu
        mu = mu + delta / cnt
        delta2 = r - mu
        M2 = M2 + delta * delta2
        s2 = M2 / cnt
        null_sum += Fraction(1, 4 * n)
        if n in checkpoints:
            cp[n] = dict(mu=mu, s2=s2,
                         null_log=null_sum / cnt,
                         null_const=Fraction(1, 4 * cnt))
    return cp


def main():
    t0 = time.time()
    lines = []
    def say(*a):
        s = " ".join(str(x) for x in a)
        print(s, flush=True)
        lines.append(s)

    say("INDEPENDENT VERIFICATION of fair-variance Null/Ratio-B (SUPPLY fold)")
    say("CAPTURE oracle : lib.supply_fold.s_sos (submask-PRODUCT zeta, +-1 algebra)")
    say("THIS RUN oracle: DIRECT submask-XOR decomposition T(n,d)=XOR_{s<=d} h[n-1-s],")
    say("   (L) from-scratch literal per-submask expansion ; (Z) subset-XOR zeta (0/1, uint8)")
    say("   (D) lib.supply_fold.s_direct (library literal direct oracle)")
    say("convention: floored fold d in [2,n-1] (nu2(53)=18, nu2(64)=27)")
    say("all arithmetic exact (ints/Fractions); ratios float only at display")
    say("NPROC=%d" % NP)
    say("")

    # ---------------- entry: four-way agreement n=2..200 (part a) -----------
    hP = prime_h(N_ZETA + 2)
    hP8 = as_u8(hP)
    say("=== (a) four-way agreement n = 2..200 (L, Z, D, s_sos), PRIMES ===")
    ns200 = list(range(2, 201))
    ag = sample_agreement(ns200, hP, hP8, NP)
    bad = [n for n, d in ag.items()
           if not (d["L"] == d["Z"] == d["D"] == d["SOS"] and d["Srel"])]
    say("   n=2..200: L==Z==D==s_sos on all %d n; S==(n-2)-2*ones on all: %s"
        % (len(ns200), not bad))
    assert not bad, bad[:10]
    say("")

    # ---------------- (b) checkpoints from the direct routes ---------------
    say("=== (b) checkpoints: literals (53,64,4000) + literal at 40000 + zeta ===")
    lit53 = nu2_literal_direct(53, hP)
    lit64 = nu2_literal_direct(64, hP)
    lit4000 = nu2_literal_direct(4000, hP)
    lit40000 = nu2_literal_direct(40000, hP)      # ~seconds, oracle
    z53, z64, z4000, z40000 = (nu2_xor_zeta(n, hP8[:n])
                               for n in (53, 64, 4000, 40000))
    for tag, got in [("53", lit53), ("64", lit64), ("4000", lit4000),
                     ("40000", lit40000)]:
        exp = CAPTURE_NU2[int(tag)]
        say("   nu2[%s] literal=%d zeta=%d  capture expects %d : %s"
            % (tag, got, {"53": z53, "64": z64, "4000": z4000,
                          "40000": z40000}[tag], exp,
               "PASS" if got == exp else "FAIL"))
        assert got == exp
    # also s_direct at 40000 (part of sample agreement below? include here)
    Sd, onesd = s_direct(40000, hP[:40000])
    say("   s_direct(40000): S=%d ones=%d (ones==nu2: %s, S==(n-2)-2*ones: %s)"
        % (Sd, onesd, onesd == 20081, Sd == 39998 - 2 * onesd))
    assert onesd == 20081
    say("")

    # -------- (L) full literal prefix to N_LIT, PRIMES (parallel) ----------
    say("=== (L) full literal prefix n = 2..%d, PRIMES (parallel) ===" % N_LIT)
    nu2_lit = prefix_literal(N_LIT, hP, NP)
    say("   computed %d n-values; nu2[%d]=%d" % (N_LIT - 1, N_LIT,
                                                 nu2_lit[N_LIT]))
    # consistency with the four-way block at 200 and the checkpoint at 4000
    assert all(nu2_lit[n] == ag[n]["L"] for n in range(2, 201))
    assert nu2_lit[4000] == 1975
    say("   literal prefix == four-way block on [2,200] and == 1975 at 4000: PASS")
    say("")

    # -------- (Z) full XOR-zeta prefix to N_ZETA for all three families -----
    prefixes = {}
    for (label, gen) in FAMILIES:
        h = gen(N_ZETA + 2)
        say("=== (Z) full XOR-zeta prefix n = 2..%d, %s (parallel) ==="
            % (N_ZETA, label))
        nu2z = prefix_zeta(N_ZETA, as_u8(h), NP)
        prefixes[label] = nu2z
        say("   nu2[%d]=%d  (~%.4f of n)" % (N_ZETA, nu2z[N_ZETA],
                                             nu2z[N_ZETA] / N_ZETA))
        if label == "PRIMES":
            assert nu2z[N_ZETA] == 20081
    say("")

    # -------- multi-oracle sample agreement beyond the prefix range --------
    say("=== samples beyond N_LIT: L/Z/D/s_sos on %d spread n-values ==="
        % len(SAMPLES))
    samp = sample_agreement(SAMPLES, hP, hP8, NP)
    say("   sample n: " + ",".join(str(n) for n in SAMPLES))
    allok = all(d["L"] == d["Z"] == d["D"] == d["SOS"] and d["Srel"]
                for d in samp.values())
    say("   all routes agree on every sample n; S-relation holds: %s" % allok)
    assert allok
    say("")

    # -------- full-prefix cross-check Z vs L on [2, N_LIT] ----------
    mism = [n for n in range(2, N_LIT + 1)
            if prefixes["PRIMES"][n] != nu2_lit[n]]
    say("=== cross-check full prefixes Z vs L on n = 2..%d: %d mismatches"
        % (N_LIT, len(mism)))
    say("   Z prefix and literal prefix are the same sequence to %d: %s"
        % (N_LIT, not mism))
    assert not mism
    say("")

    # ---------------- (c) exact prefix variance, Ratios A and B -------------
    say("=== (c) exact prefix variance & ratios, PRIMES (from Z full prefix) ===")
    cpP = reduce_stats(prefixes["PRIMES"], N_ZETA, CHECKPOINTS)
    say("%5s %12s %12s %10s %10s | %8s %12s" %
        ("N", "mu_N", "s2_N", "s2*4N", "s2*4N/lnN", "cap R.B", "match"))
    rb_all = {}
    ra_all = {}
    for n in CHECKPOINTS:
        d = cpP[n]
        rA = float(d["s2"]) * 4 * n
        rB = float(d["s2"]) * 4 * n / math.log(n)
        rb_all[n], ra_all[n] = rB, rA
        capB = CAPTURE_RB[n]
        capA = CAPTURE_RA[n]
        mB = abs(rB - capB) < 5e-4
        mA = abs(rA - capA) < 5e-3
        mS2 = abs(float(d["s2"]) - CAPTURE_S2[n]) < 1e-7
        mMu = abs(float(d["mu"]) - CAPTURE_MU[n]) < 1e-5
        say("%5d %12.6f %12.5e %10.4f %10.4f | %8.4f %s" %
            (n, float(d["mu"]), float(d["s2"]), rA, rB, capB,
             "PASS" if (mB and mA and mS2 and mMu) else "FAIL"))
        assert mB and mA and mS2 and mMu
    say("   Ratio A at 40000 = %.4f (capture 13.9394)" % ra_all[40000])
    say("   Ratio B sequence: %s" % " ".join("%.3f" % rb_all[n]
                                             for n in CHECKPOINTS))
    say("   capture sequence: 1.443 1.392 1.361 1.337 1.315")
    say("   mu_40000 = %.6f (capture 0.499671); s2_40000 = %.5e (capture "
        "8.71213e-05)" % (float(cpP[40000]["mu"]),
                          float(cpP[40000]["s2"])))
    say("")
    dec = []
    prev = None
    for n in CHECKPOINTS:
        if prev is not None:
            dec.append(rb_all[prev] - rb_all[n])
        prev = n
    say("   per-step decrements (1000->4000->10000->20000->40000): %s"
        % " ".join("%.4f" % d for d in dec))
    say("   per-doubling decrements (1000->2000@?, use 4000->10000 as 2.5x):")
    say("   last two doublings (10000->20000, 20000->40000): %.4f, %.4f "
        "(ratio %.3f) -- decrement barely shrank" %
        (rb_all[10000] - rb_all[20000], rb_all[20000] - rb_all[40000],
         (rb_all[20000] - rb_all[40000]) / (rb_all[10000] - rb_all[20000])))
    say("")

    # ---------------- (d) deep-tail dip check, negative controls ------------
    N_L = 12000
    loT = int(0.9 * N_ZETA)
    pz = prefixes["PRIMES"]
    say("=== (d) deep tail [%d,%d]: nu2(n)/n >= 0.40 for ALL n (PRIMES) ==="
        % (loT, N_ZETA))
    below = [(n, Fraction(pz[n], n)) for n in range(loT, N_ZETA + 1)
             if Fraction(pz[n], n) < Fraction(2, 5)]
    mrat = min(Fraction(pz[n], n) for n in range(loT, N_ZETA + 1))
    say("   count with nu2(n)/n < 0.40 in tail: %d" % len(below))
    say("   min nu2(n)/n over the tail: %s = %.4f" % (mrat, float(mrat)))
    say("   min >= 0.49 (capture: dip density 0 at every c=0.40..0.49): %s"
        % (mrat >= Fraction(49, 100)))
    assert not below
    say("")
    say("   negative controls (must DIP: density of nu2/n < 0.40 in tail >"
        " 0.01):")
    for (label, gen) in FAMILIES[1:]:
        hc = gen(N_L + 2)
        nu2c = prefix_zeta(N_L, as_u8(hc), NP)
        loTc = int(0.9 * N_L)
        d0 = sum(1 for n in range(loTc, N_L + 1)
                 if Fraction(nu2c[n], n) < Fraction(2, 5))
        dens = d0 / (N_L - loTc + 1)
        say("     %-10s tail density(nu2/n<0.40) over [%d,%d] = %.4f  "
            "(capture at 40000: ALL-ONES 1.0000, THUE-MORS 0.9998)"
            % (label, loTc, N_L, dens))
        assert dens > 0.01
    say("")

    # ---------------- summary ----------------
    say("SUMMARY (measured, not proved):")
    say("  oracle used: DIRECT submask-XOR route -- (L) literal expansion, "
        "(Z) exact XOR-zeta,")
    say("    (D) lib.s_direct -- a different algebra/path from the capture's "
        "s_sos (+-1 product zeta).")
    say("  full exact prefixes reached: literal to N=10000 (PRIMES), XOR-zeta "
        "to N=40000 (all 3 families);")
    say("  checkpoints 20000/40000 additionally cross-checked by literal + "
        "s_direct + s_sos samples at %d n-values." % len(SAMPLES))
    say("  Ratio B: %s ; Ratio A(40000)=%.4f -- MATCHES the capture." %
        (" ".join("%.3f" % rb_all[n] for n in CHECKPOINTS), ra_all[40000]))
    say("  convergence classification: Ratio B is DECREASING but the excess "
        "PERSISTS to 40000 (1.443->1.315);")
    say("    per-doubling decrements barely shrink (0.0237, 0.0213, ratio "
        "0.9) -- one decade of data does")
    say("    NOT determine whether limit B is 1 or a constant above 1; "
        "extension to 80000 is separate (fair_variance_extend_80000.py).")
    say("  deep tail [36000,40000]: nu2/n >= 0.49 everywhere for PRIMES "
        "(min %s); controls dip at c=0.40." % mrat)
    say("  NODES: this is a measurement, not a proof; exact arithmetic; "
        "negative controls failed exactly where required.")
    say("runtime %.1fs" % (time.time() - t0))

    text = "\n".join(lines) + "\n"
    with open(OUT, "w") as f:
        f.write(text)
    print("WROTE", OUT)

    # traceability: dump the Z prefix for PRIMES
    dump = os.path.abspath(os.path.join(os.path.dirname(OUT),
                                        "nu2_primes_xor_40000.json"))
    with open(dump, "w") as f:
        json.dump(prefixes["PRIMES"], f)
    print("WROTE", dump)


if __name__ == "__main__":
    main()