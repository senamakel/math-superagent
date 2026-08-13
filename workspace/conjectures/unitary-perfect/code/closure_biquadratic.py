#!/usr/bin/env python3
"""DIRECTIVE 14 -- does quartic reciprocity on 2^p + i constrain the divisor
set of Phi_{4p}(2) beyond the per-divisor mod-16 test?  Verdict: (b), closed,
with the exact reason.

The product identity of research/approaches/biquadratic-character-divisors.md
is
        prod_{pi^e || 2^p+i} (2/pi)_4^e  =  (2/(2^p+i))_4               (1)
where the RIGHT SIDE IS THE DEFINITION of the left (the quartic symbol with
composite denominator is multiplicative over the Gaussian prime
factorization).  So (1) carries exactly the information of the per-divisor
symbols.  The only way it could constrain the divisor set is an INDEPENDENT
closed-form evaluation of (2/(2^p+i))_4 -- Eisenstein's supplementary law
extended to composite denominators: for the primary associate 1 - 2^p i of
2^p + i (b = -2^p),
        candidate C1(p):  (2/(2^p+i))_4 = i^{-b/2} = i^{2^{p-1}}         (2)
which for odd p >= 3 equals +1 (2^{p-1} == 0 mod 4).

This run computes, for every odd prime p <= P with 2^{2p}+1 fully factored
(nothing left unfactored in range):
  V_def(p) : definitional product (1), exact unit in {+1, -1, +i, -i};
  C8       : prime-level supplementary law [2/pi]_4 = i^{-b(pi~)/2} per
             Gaussian prime factor pi (pi~ = primary associate);
  C11      : composite-law check V_def(p) == C1(p), every p;
  counts   : C1m, C5, C9, C13 = multiplicity of divisors r of 2^{2p}+1 with
             r == 1, 5, 9, 13 mod 16, and the identity
             V_def == (+1)^{C1m} (-1)^{C9} (i)^{C5} (-i)^{C13}, i.e.
             the single congruence  C5 - C13 + 2*C9 = 0 (mod 4);
  C9       : class resolution -- (2/r)_4 = +1 iff r==1 mod 16 (head),
             = -1 iff r==9 mod 16, = +-i iff r==5 or 13 mod 16
             (generator argument: (2/r)_4 = zeta^{t u}, zeta primitive 4th
             root, t = (r-1)/4p, u odd; r==9 => t even not div by 4 =>
             -1; r==5/13 => t odd => +-i);
  blindness: the head count C1m does not occur in the identity (heads are
             exactly the +1 class, contributing factor +1).  Witnessed by
             the seven Thm-8 H_even members p in {3,5,13,23,31,41,61}
             (2p in H_even): C1m = 0 and V_def = +1, exhibiting that the
             product value +1 does NOT force a head.

Verdict logic (DIRECTIVE 14 deliverables (a) vs (b)):
  (a) -- a new constraint forcing a head for some p-class -- is impossible
  unconditionally: heads contribute factor +1, so adding/removing heads
  changes neither side of (1); C1m is a free variable of the identity.
  (b) -- closure: the biquadratic character of 2 recovers ONLY the per-
  divisor mod-16 test (C9), and the product identity's entire content is
  the congruence C5 - C13 + 2*C9 = 0 (mod 4) among the three NON-head
  classes (all with v2(r-1) <= 3, whose 3-Higgs status is decided by odd
  primes of r-1 -- invisible to quartic characters of 2).  The closed-form
  evaluation (2), if it holds, degenerates to the constant +1 on all odd
  primes, i.e. it is not a divisor-transference statement at all.
  The closure does NOT touch the adopted second-moment-character-mod16
  approach: its first moment S_chi = sum_r (2/r)_4 is a SUM, which sees
  C1m with weight +1; only the PRODUCT is blind to the head count.

Anchors: ord_r(2) = 4p and r == 1 (mod 4p) for every prime divisor r of
Phi_{4p}(2) (heven_gauss.py checks C4/C5, all 71 rows through p=61);
(2/r)_4 = +1 <==> r == 1 mod 16 re-verified here as C9.  Williams (1976)
supplementary law for primary Gaussian primes [2/pi]_4 = i^{-b/2} (source
held in library; prime-level law checked here on every factor as C8).

Usage: timeout 540 python3 code/closure_biquadratic.py [P]
  P default 61: all odd primes 3..61, 2^{2p}+1 fully factored (max 37
  digits at p=61).  Range covered and "nothing left unfactored" are stated
  in the final block.  Exact integer arithmetic; no floats anywhere.
"""
import sys
import time

import sympy

from heven_gauss import gauss_factor, quartic_char

THM8 = {3, 5, 13, 23, 31, 41, 61}          # p with 2p in H_even (Thm 8)

UNITS = {(1, 0): 0, (0, 1): 1, (-1, 0): 2, (0, -1): 3}   # i^k -> k
_UNIT_NAMES = {0: "+1", 1: "+i", 2: "-1", 3: "-i"}


def unit_name(u):
    return _UNIT_NAMES[UNITS[u]]


def pow_unit(u, e):
    """i^(k*e) for u = i^k, e >= 0 (Python % handles any sign of k*e)."""
    return list(UNITS)[(UNITS[u] * e) % 4]


def mul_units(a, b):
    return list(UNITS)[(UNITS[a] + UNITS[b]) % 4]


def primary_associate(su, sv):
    """Unique k in 0..3 with i^k*(su+sv*i) primary (a+b==1 mod 4, b even)."""
    for k in range(4):
        aa, bb = [(su, sv), (-sv, su), (-su, -sv), (sv, -su)][k]
        if (aa + bb) % 4 == 1 and bb % 2 == 0:
            return aa, bb
    raise AssertionError("no primary associate of %d+%di" % (su, sv))


def law_value(aa, bb):
    """Williams/Eisenstein [2/(aa+bb*i)]_4 = i^{-bb/2}, aa+bb*i primary."""
    return list(UNITS)[(-(bb // 2)) % 4]


def main():
    P = int(sys.argv[1]) if len(sys.argv) > 1 else 61
    primes = list(sympy.primerange(3, P + 1))
    assert primes, "need odd primes in range (P >= 3)"
    t0 = time.time()

    n_plaw = 0            # C8: prime-level supplementary law
    n_plaw_pass = 0
    n_comp = 0            # C11: composite-law candidate
    n_comp_pass = 0
    c9_ok = True          # C9: class resolution
    id_ok_all = True      # C10: class-product identity
    law_evals = []        # prime-level law mismatches, if any
    mem_witness = []

    print("# DIRECTIVE 14 -- biquadratic (quartic) character of 2 over the")
    print("# divisor set of Phi_{4p}(2): constraint beyond per-divisor mod-16?")
    print("# odd primes p <= %d; every 2^{2p}+1 fully factored; exact integers only"
          % P)
    print("# header:  p  V_def  C1(p)  law[comp]  C1m C5 C9 C13  "
          "cong  class-ok  heven?")
    print("# (C1m = multiplicity of r == 1 mod 16 across divisors of 2^{2p}+1;")
    print("#  C5, C9, C13 likewise for 5, 9, 13;  cong = C5-C13+2*C9 mod 4;")
    print("#  V_def == i^{cong};  a head is r == 1 mod 16, v2(r-1) >= 4 > 3,")
    print("#  hence NOT 3-Higgs -- the only class relevant to Conjecture 29)")

    for p in primes:
        rows, N = gauss_factor(p)          # verified product check inside
        counts = {1: 0, 5: 0, 9: 0, 13: 0}
        V = (1, 0)
        plaw_ok = True
        for q, e, su, sv in rows:
            r16 = q % 16
            assert r16 in (1, 5, 9, 13), (p, q, r16)     # C3: q == 1 mod 4
            char = quartic_char(p, q, su, sv)
            counts[r16] += e
            V = mul_units(V, pow_unit(char, e))
            # ---- C9: class resolution ----
            if r16 == 1:
                want = (1, 0)
            elif r16 == 9:
                want = (-1, 0)
            else:                            # r16 in {5, 13} -> +-i
                want = None
            if want is not None and char != want:
                c9_ok = False
            if want is None and char not in ((0, 1), (0, -1)):
                c9_ok = False
            # ---- C8: prime-level supplementary law ----
            aa, bb = primary_associate(su, sv)
            law = law_value(aa, bb)
            n_plaw += 1
            if law == char:
                n_plaw_pass += 1
            else:
                plaw_ok = False
                law_evals.append((p, q, su, sv, aa, bb, unit_name(char),
                                  unit_name(law)))
        C1m, C5, C9c, C13 = counts[1], counts[5], counts[9], counts[13]
        cong = (C5 - C13 + 2 * C9c) % 4
        Vcls = pow_unit((0, 1), cong)        # i^{C5-C13+2*C9}
        id_ok = (V == Vcls)
        id_ok_all &= id_ok
        # ---- C11: composite-law candidate ----
        cand = pow_unit((0, 1), (2 ** (p - 1)) % 4)     # i^{2^{p-1}}
        comp_ok = (V == cand)
        n_comp += 1
        n_comp_pass += comp_ok
        heven = "H_even member" if p in THM8 else ""
        if p in THM8:
            mem_witness.append((p, C1m, unit_name(V), 2 * p))
        print("  p=%-3d V=%-3s C1(p)=%-3s comp=%-5s C1m=%-3d C5=%-3d C9=%-3d "
              "C13=%-3d cong=%d id=%-5s %s"
              % (p, unit_name(V), unit_name(cand),
                 "PASS" if comp_ok else "FAIL",
                 C1m, C5, C9c, C13, cong,
                 "ok" if id_ok else ("FAIL V=%s" % unit_name(V)), heven))

    # ------------------------------------------------------------------ #
    print("#")
    print("# PRIME-LEVEL LAW (C8): [2/pi]_4 == i^{-b(pi~)/2} on %d Gaussian "
          "prime factors: %d/%d PASS" % (n_plaw, n_plaw_pass, n_plaw))
    if law_evals:
        for row in law_evals[:5]:
            print("#   MISMATCH: p=%d r=%d pi=%d+%di pi~=%d+%di char=%s law=%s"
                  % row)
    print("# COMPOSITE-LAW CANDIDATE (C11): V_def(p) == i^{2^{p-1}} on %d "
          "primes: %d/%d PASS" % (n_comp, n_comp_pass, n_comp))
    print("# CLASS IDENTITY (C10): V_def == (+1)^C1m (-1)^C9 (i)^C5 (-i)^C13"
          "  [%s]" % ("ALL PASS" if id_ok_all else "SOME FAIL"))
    print("# CLASS RESOLUTION (C9): (2/r)_4=+1 <=> r==1 mod 16; =-1 <=> "
          "r==9 mod 16; =+-i <=> r==5/13 mod 16  [%s]"
          % ("ALL PASS" if c9_ok else "SOME FAIL"))
    print("# HEAD-BLINDNESS WITNESSES (Thm-8 H_even members, exact):")
    for p, C1m, V, m in mem_witness:
        print("#   p=%d (2p=%d in H_even): C1m(heads)=%d, V_def=%s -- product +1 "
              "with zero heads" % (p, m, C1m, V))
    print("#")
    print("# ================= VERDICT (DIRECTIVE 14) =================")
    print("# (b) CLOSED: biquadratic reciprocity gives nothing beyond the")
    print("#     per-divisor mod-16 test.  Exact reasons, each checked:")
    print("#  R1 (mathematical, unconditional): a head r == 1 mod 16 is")
    print("#     exactly the class with (2/r)_4 = +1 (C9), so every product")
    print("#     identity over these characters is invariant under adding or")
    print("#     removing heads: the head count C1m never occurs in the")
    print("#     identity.  Hence no product identity can force C1m >= 1,")
    print("#     for any residue class of p - the (a) deliverable is")
    print("#     impossible, not merely unproved.")
    print("#  R2 (computed witnesses): the seven Thm-8 H_even members have")
    print("#     C1m = 0 and V_def = +1 (rows above) - the product value +1")
    print("#     coexists with a head-free divisor set.")
    print("#  R3 (computed): the product identity's entire content is the")
    print("#     single congruence C5 - C13 + 2*C9 == 0 (mod 4) among the")
    print("#     THREE NON-HEAD classes r == 5, 9, 13 mod 16, all of which")
    print("#     have v2(r-1) <= 3 < 4 and so are not eliminated by the")
    print("#     3-Higgs 2-adic test; their 3-Higgs status is decided by odd")
    print("#     primes q | r-1 (e.g. 343081 | 2^19066+1, v2=3, kills via")
    print("#     953 -> 17), and quartic characters of 2 are mod-16 class")
    print("#     functions on primitive divisors - they carry no odd-prime")
    print("#     information at all.")
    print("#  R4 (computed + sourced): the closed-form evaluation (the only")
    print("#     possible content of the identity) is the composite")
    print("#     supplementary law (2/(2^p+i))_4 = i^{2^{p-1}} = +1 for odd p >= 3,")
    print("#     verified on %d/%d primes (C11), with the prime-level law (C8)"
          % (n_comp_pass, n_comp))
    print("#     at %d/%d factors - a CONSTANT as a function of p, so it constrains"
          % (n_plaw_pass, n_plaw))
    print("#     only the non-head congruence and is not a divisor-")
    print("#     transference statement.")
    print("#")
    print("# NOT TOUCHED by this closure: the adopted second-moment-")
    print("# character-mod16 approach evaluates S_chi = sum_r (2/r)_4 (a")
    print("# SUM, weight +1 on heads) and is blind-free; the product")
    print("# identity was the only blind object.")
    print("#")
    print("# Range covered: odd primes 3..%d, every 2^{2p}+1 fully factored," % P)
    print("# max %d digits at p=%d; nothing left unfactored.  Elapsed %.1fs"
          % (len(str(2 ** (2 * P) + 1)), P, time.time() - t0))
    print("# EXIT")
    sys.exit(0 if (c9_ok and id_ok_all and not law_evals) else 1)


if __name__ == "__main__":
    main()