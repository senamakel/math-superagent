#!/usr/bin/env python3
"""From-scratch independent verification of the run's odd-period affine supply
law (claim dyadic-oddfactor-affine-modulus-lifting).  NO lib imports — own
code only, exact integers.

Model (canonical, matching the claim's stated hypotheses and the run's code):
  2-then-odds halved-gap bit string h of odd period P, tail-1 word
  h = [0]*(P-1)+[1].  q_1=2, q_2=3, and the gap after q_m (m>=2) is
  2 if h[(m-2) mod P]==1 else 4 (bit index cycled from word position 0).

nu2(n) = number of 2s in the maximal {0,2} suffix of the right diagonal
  delta(q_n), body convention (exclude the terminal entry).  delta_k(q_n)=
  A_k[n-k] with A_0 = q sequence.

Methods used:
  * incremental_diagonals: the right-diagonal recurrence computed from scratch
    (D_0=[q_1]; D_n extends D_{n-1} by D_n[0]=q_{n+1}, D_n[k]=|D_n[k-1]-D_{n-1}[k-1]|).
    O(N^2) absolute differences, O(N) memory.
  * literal_triangle_nu2: a literal full absolute-difference triangle built
    row by row per prefix, right diagonal read off directly.  O(n^2) per n.
  * Cross-check (oracle, rule 9): incremental == literal for every n in a
    small window, to validate the incremental method before running it at N.

Checks delivered:
  (a) P=3: is nu2(n) == 2*floor((n-1)/3) exactly for all tested n?
  (b) P=3: is the per-residue-affine law nu2(n+3)-nu2(n) constant per residue
      class of n mod 3?  Constants c_r, min c_r, implied slope.
  (c) P=7 (Mersenne, k=3, word [0]*6+[1]): per-residue-affine constants c_r
      mod 7; is sum_r c_r == 3^3-3 = 24 (claim mersenne-nu2-affine-selfsimilar-
      recursion / the general sum c_r = 3^k-3)?  Also report min c_r == 2.
"""
import sys

# ---------------------------------------------------------------- construction
def q_seq(word, n_terms):
    """First n_terms terms of the 2-then-odds sequence with periodic halved-gap
    bit string `word`.  q[0]=2, q[1]=3; gap after q_m is 2 if bit else 4,
    cycled from word index 0."""
    q = [2, 3]
    P = len(word)
    while len(q) < n_terms:
        bit = word[(len(q) - 2) % P]
        q.append(q[-1] + (2 if bit else 4))
    return q[:n_terms]


def incremental_diagonals(seq):
    """Yield delta(q_n) for n=0,1,2,... (delta has n+1 entries).  From-scratch
    implementation of the right-diagonal recurrence.  O(N^2) diffs, O(N) mem."""
    D = [seq[0]]                      # delta(q_1), n=0
    yield D
    for n in range(1, len(seq)):
        newD = [0] * (n + 1)
        newD[0] = seq[n]              # new term enters at the bottom
        for k in range(1, n + 1):
            newD[k] = abs(newD[k - 1] - D[k - 1])
        D = newD
        yield D


def body_nu2(diag):
    """# of 2s in the maximal {0,2} suffix of diag[:-1] (body convention:
    exclude the terminal entry, which is 1 on successful columns)."""
    c = 0
    for v in reversed(diag[:-1]):
        if v in (0, 2):
            c += v == 2
        else:
            break
    return c


# ------------------------------------------------- literal triangle (oracle)
def literal_triangle_nu2(word, n):
    """nu2(n) by building the FULL absolute-difference triangle of the length-n
    prefix and reading the right diagonal directly.  O(n^2) per call."""
    row = q_seq(word, n)
    rows = [row]
    while len(rows[-1]) > 1:
        r = rows[-1]
        rows.append([abs(r[i] - r[i + 1]) for i in range(len(r) - 1)])
    diag = [rows[k][n - 1 - k] for k in range(n)]     # A_k[n-k], right diagonal
    return body_nu2(diag)


def cross_check(word, nmax):
    """Validate incremental vs literal for every n in [2, nmax].
    The incremental diagonal with enumerate-index e is over prefix q_1..q_{e+1}
    (prefix length e+1), so nu2(n) is read at e = n-1."""
    seq = q_seq(word, nmax)
    nu2_inc = {}
    for e, d in enumerate(incremental_diagonals(seq)):
        n = e + 1                       # prefix length q_1..q_n
        if n >= 2:
            nu2_inc[n] = body_nu2(d)
    bad = []
    for n in range(2, nmax + 1):
        if literal_triangle_nu2(word, n) != nu2_inc[n]:
            bad.append(n)
    return bad, nu2_inc


def nu2_all(word, N):
    """nu2(n) for n in [2, N] via the (already cross-checked) incremental route."""
    seq = q_seq(word, N)
    out = {}
    for e, d in enumerate(incremental_diagonals(seq)):
        n = e + 1
        if n >= 2:
            out[n] = body_nu2(d)
    return out


def per_residue_constants(vals, P, nmin, nmax):
    """c_r = {nu2(n+P)-nu2(n)} for n in [nmin, nmax-P], n ≡ r (mod P).
    Returns (dict r->set-of-diffs, all_constant_bool)."""
    out = {}
    for r in range(P):
        diffs = set()
        for n in range(nmin, nmax - P + 1):
            if n % P == r:
                diffs.add(vals[n + P] - vals[n])
        out[r] = diffs
    return out


def main():
    N = 2000
    nmin = 200            # skip the small-n O(1) transient for affinity checks
    print("=" * 78)
    print("FROM-SCRATCH (no lib imports) verification of claim")
    print("  dyadic-oddfactor-affine-modulus-lifting")
    print("=" * 78)

    # ---------------- P=3 ----------------
    word3 = [0, 0, 1]
    print("\n[STEP 0] cross-check incremental vs literal full-triangle (oracle)")
    bad, _ = cross_check(word3, 40)
    print(f"  P=3: incremental == literal for n=2..40? "
          f"{'YES (0 mismatches)' if not bad else 'NO: ' + str(bad)}")
    assert not bad, "incremental method disagrees with literal triangle"

    vals3 = nu2_all(word3, N)
    P = 3
    print("\n[STEP 1] P=3 (word [0,0,1]); nu2(n) vs closed form 2*floor((n-1)/3)")
    # (a) literal closed form, all n in window
    cf_mismatch = [(n, vals3[n], 2 * ((n - 1) // 3))
                   for n in range(2, N + 1)
                   if vals3[n] != 2 * ((n - 1) // 3)]
    print(f"  closed form 2*floor((n-1)/3) matches for all n in [2,{N}]? "
          f"{'YES' if not cf_mismatch else 'NO (mismatch count %d)' % len(cf_mismatch)}")
    if cf_mismatch:
        # report which residues fail and the actual exact law
        per_r = {}
        for n, v, f in cf_mismatch:
            per_r.setdefault(n % 3, []).append((n, v, f))
        print("  mismatches by residue (first 4 each):")
        for r in sorted(per_r):
            print(f"    n%3={r}: " + "; ".join(f"n={n} nu2={v} cf={f}" for n, v, f in per_r[r][:4]))
        # exact law: on each residue nu2(n+3)-nu2(n)=2, so nu2(n)=2*(n//3)+offset_r
        print("  exact per-residue affine form (nu2(n) = 2*floor(n/3) + offset_r):")
        for r in range(3):
            ns = [n for n in range(nmin, N) if n % 3 == r]
            offs = {vals3[n] - 2 * (n // 3) for n in ns}
            print(f"    residue {r}: offset = {offs} (constant={len(offs)==1})")

    # (b) per-residue affinity
    res3 = per_residue_constants(vals3, P, nmin, N)
    const3 = all(len(s) == 1 for s in res3.values())
    cs3 = [next(iter(s)) for s in res3.values()]
    print(f"\n[STEP 2] P=3 per-residue affinity nu2(n+3)-nu2(n) constant per residue? "
          f"{'YES' if const3 else 'NO'}")
    print(f"  c_r = {cs3}; min c_r = {min(cs3)}; mean c_r = {sum(cs3) / P:.4f}; "
          f"density slope = (sum c_r)/P^2 = {sum(cs3) / (P * P):.6f}")
    print(f"  all c_r == 2? {all(c == 2 for c in cs3)}  "
          f"(min c_r >= 2 required by the claim: {min(cs3) >= 2})")

    # ---------------- P=7 Mersenne ----------------
    word7 = [0] * 6 + [1]
    bad7, _ = cross_check(word7, 40)
    print("\n[STEP 3] P=7 oracle cross-check:", "YES" if not bad7 else str(bad7))
    assert not bad7
    vals7 = nu2_all(word7, N)
    res7 = per_residue_constants(vals7, 7, nmin, N)
    const7 = all(len(s) == 1 for s in res7.values())
    cs7 = [next(iter(s)) if len(s) == 1 else None for s in res7.values()]
    S7 = sum(c for c in cs7 if c is not None)
    print(f"\n[STEP 4] P=7 (Mersenne k=3, word [0]*6+[1]); affine={const7}")
    print(f"  c_r = {cs7}")
    if const7:
        print(f"  sum_r c_r = {S7}; target 3^3-3 = {3**3-3}; match={S7 == 3**3-3}")
        print(f"  min c_r = {min(cs7)}; all even? {all(c % 2 == 0 for c in cs7)}")

    print("\n" + "=" * 78)
    print("VERDICT")
    print("=" * 78)
    if not bad and const3 and all(c == 2 for c in cs3):
        print("  (a) per-residue-affine law (the claim's actual statement): HOLDS,")
        print("      c_r = 2 for every residue, min c_r = 2, slope 2/3.")
    a_ok = not cf_mismatch
    print(f"  (a') literal closed form nu2(n)=2*floor((n-1)/3) for ALL n: "
          f"{'HOLDS' if a_ok else 'REFUTED (holds only at n%3==0; see STEP 1)'}")
    print(f"  (b) per-residue affinity nu2(n+3)-nu2(n)=c_r, c_r constant per residue: "
          f"{'YES' if const3 else 'NO'}")
    print(f"  (c) P=7 Mersenne sum of constants == 24: "
          f"{'YES' if (const7 and S7 == 24) else 'NO'}")
    sys.exit(0 if (const3 and const7 and S7 == 24) else 1)


if __name__ == "__main__":
    main()
