#!/usr/bin/env python3
"""First-step execution of adopted approach fold-second-moment-krawtchouk.

Runs, in exact integer / F2 / exact-Fraction arithmetic:

  1. ROW SET. For each d in [2, n-1], M_d = { n-1-d+o : o submask of d }, with
     |M_d| = 2^popcount(d) as the check.
  2. DECISIVE DISTANCE DISTRIBUTION. A_k = #{ d != d' : |M_d XOR M_{d'}| = k }
     for n in {16,24,32,48,64,96,128}; report A_2 and the growth verdict
     (O(n) vs Theta(n^2)), and F_n(z) at z = 1-2p for p = 0.585 (exact
     Fraction -17/100); is F_n(z) = O(n)?  (condition (C))
  3. IDENTITY VERIFICATION (exact enumeration). For small n and p in
     {0.3, 0.5, 0.585}: E[eps_d eps_d'] = (1-2p)^{|M_d XOR M_d'|}, and
     E[S^2] = F_n(1-2p) ===> var(S) = F_n(1-2p) - E[S]^2 (with the mean
     E[S] = sum_d (1-2p)^{|M_d|} computed exactly). We also report the
     approach-doc's "-(n-2)" version and note it holds only when E[S]^2 = n-2.
  4. KRAWTCHOUK DIAGONALIZATION. Verify F_n(z) =
       2^{-n} sum_omega (1-z)^{wt(omega)} (1+z)^{n-wt(omega)} C_n^hat(omega)^2
     exactly for small n and several exact z.
  5. NEGATIVE CONTROLS. all-ones, Thue-Morse, single-isolated-1 inputs at
     n up to 128: exact S(n) and how far actual |S| deviates from the iid
     model's prediction sqrt(F_n(1-2p)-(n-2)) (using p = 0.585 reference, and
     the input's own measured density). The controls must FAIL the iid model
     (i.e. not be iid-balanced), or the bridge checks nothing.

Everything is exact: ints for counts, Fractions for F_n at rational z. The
only floats are printed density ratios, clearly labeled.
"""
from fractions import Fraction

from lib.downset_rows import (
    popcount, row_positions, row_mask, row_masks, row_size, row_dist,
    distance_distribution, enumerator, cross_character_sum,
    krawtchouk_enumerator,
)


# ---------------------------------------------------------------- row weights
def check_row_weights(n):
    """|M_d| = 2^popcount(d) for all d in [2, n-1]."""
    bad = []
    for d in range(2, n):
        rp = row_positions(n, d)
        if len(rp) != row_size(n, d) or len(rp) != (1 << popcount(d)):
            bad.append(d)
        assert len(rp) == (1 << popcount(d))
    return len(bad), list(range(2, n))


def rows_overlap_check(n, masks):
    """All rows land in [0, n-1]; sizes even; masks distinct per d."""
    for i, m in enumerate(masks):
        assert m >> n == 0
        assert popcount(m) % 2 == 0
    assert len(masks) == len(set(masks))


# ------------------------------------------------------------ distance dist.
def distance_report(n, z_ref):
    """A_k distribution, A_2 count, and F_n(z_ref) = (n-2) + sum A_k z^k.

    Returns (A, A2, F_ref, n_z2_terms) where n_z2_terms = sum_k A_k for
    reporting total off-diagonal pairs.
    """
    A, nrows, masks = distance_distribution(n)
    assert nrows == n - 2, (n, nrows)
    # only even k allowed: A_1 must be 0, no odd distances
    for k in A:
        assert k % 2 == 0, (n, k)
    A2 = A.get(2, 0)
    # F_n(z) = (n-2) + sum_k A_k z^k, aggregated
    total = Fraction(n - 2)
    for k, cnt in A.items():
        total += Fraction(cnt) * (z_ref ** k)
    offdiag = sum(A.values())
    return A, A2, total, offdiag


# ------------------------------------------------------------ identity verif
def eps_matrix(n, p):
    """Exact E[eps_d eps_d'] and E[eps_d], E[S^2], E[S] by exact enumeration
    over all 2^n inputs weighted by iid Bernoulli(p) (p a Fraction).

    Returns (E2_pairs: dict {(d,d'): Fraction}, Evec dict {d: Fraction},
             ES2 Fraction, ES Fraction, rows masks)."""
    masks = row_masks(n)
    ds = list(range(2, n))
    E2 = {(a, b): Fraction(0) for a in ds for b in ds}
    Evec = {d: Fraction(0) for d in ds}
    for x in range(1 << n):
        prob = Fraction(1)
        for j in range(n):
            if (x >> j) & 1:
                prob *= p
            else:
                prob *= 1 - p
        # eps_d = 1 - 2*parity(x & mask_d)
        ed = {}
        for d in ds:
            par = popcount(x & masks[ds.index(d)]) & 1
            ed[d] = 1 if par == 0 else -1
        for a in ds:
            Evec[a] += prob * ed[a]
            for b in ds:
                E2[a, b] += prob * ed[a] * ed[b]
    ES = sum(Evec.values())
    ES2 = Fraction(0)
    for a in ds:
        for b in ds:
            ES2 += E2[a, b]
    return E2, Evec, ES2, ES, masks


def identity_check(n, p_list):
    print(f"\n==[3] IDENTITY VERIFICATION (exact 2^n enumeration) ==")
    for p_float in p_list:
        p = Fraction(p_float).limit_denominator(10 ** 6)
        z = 1 - 2 * p
        masks = row_masks(n)
        ds = list(range(2, n))
        E2, Evec, ES2, ES, _ = eps_matrix(n, p)
        # (a) pairwise XOR moment
        pmax = pmin = Fraction(0)
        allok = True
        for a in ds:
            for b in ds:
                pred = z ** row_dist(masks[ds.index(a)], masks[ds.index(b)])
                ok = (E2[a, b] == pred)
                allok = allok and ok
                if not ok:
                    pmax = max(pmax, abs(E2[a, b] - pred))
        # (b) mean
        mean_pred = sum((z ** popcount(masks[ds.index(d)])) for d in ds)
        mean_ok = (ES == mean_pred)
        # (c) E[S^2]
        F = enumerator(n, z, masks)
        es2_ok = (ES2 == F)
        # (d) var, and the approach-doc "-(n-2)" version
        var_true = ES2 - ES * ES
        var_diag = F - Fraction(n - 2)          # approach-doc version
        var_diag_ok = (var_true == var_diag)
        print(f"  n={n} p={p_float} (exact {p}, z={z}):")
        print(f"     pairwise XOR moment all-match = {allok}"
              f"{'  [MISMATCH max|diff|=' + str(pmax) + ']' if not allok else ''}  "
              f"({len(ds)*(len(ds)-1)} off-diag pairs + {len(ds)} diag)")
        print(f"     mean E[S] = {ES} == pred {mean_pred} : {mean_ok}")
        print(f"     E[S^2] = {ES2} == F_n(z) {F} : {es2_ok}")
        print(f"     var(S) = {var_true} ;  F_n(z)-(n-2) = {var_diag} ; "
              f"equal-iff-E[S]^2=n-2 : {var_diag_ok}")


# ------------------------------------------------------------ Krawtchouk
def krawtchouk_check(n_list, z_list):
    print(f"\n==[4] KRAWTCHOUK DIAGONALIZATION (exact) ==")
    for n in n_list:
        spec = cross_character_sum(n)
        for z in z_list:
            zf = Fraction(z) if not isinstance(z, Fraction) else z
            Fdir = enumerator(n, zf)
            Fk = krawtchouk_enumerator(n, zf, spec)
            ok = (Fdir == Fk)
            print(f"  n={n} z={zf}: direct={Fdir}  krawtchouk={Fk}"
                  f"  {'OK' if ok else 'MISMATCH'}")


# ------------------------------------------------------------ negative ctrl
def thue_morse(n):
    """h[j] = popcount(j) mod 2."""
    return [popcount(j) & 1 for j in range(n)]


def single_isolated(n):
    """h with a single 1 at position pos (chosen well inside), else 0."""
    h = [0] * n
    h[n // 2] = 1
    return h


def s_exact(n, h):
    """Exact S(n) = sum_{d=2}^{n-1} eps_d via the SOS submask-product transform
    (from lib.supply_fold), cross-checked against direct summation for small n."""
    from lib.supply_fold import s_sos, s_direct
    Ss, ones = s_sos(n, h)
    if n <= 40:
        Sd, onesd = s_direct(n, h)
        assert Ss == Sd and ones == onesd, (n, Ss, Sd)
    return Ss


def control_report(n_list, z_ref, p_ref):
    """Negative controls. iid model prediction for typical |S| is
    sqrt(var_model) where var_model = F_n(1-2p) - E[S]^2 with E[S] =
    sum_d (1-2p)^{|M_d|}. We use p_ref (prime value 0.585). We report the
    exact |S(n)| for each structured input and |S| vs the model std and vs n."""
    print(f"\n==[5] NEGATIVE CONTROLS (exact S(n); model p_ref={p_ref}) ==")
    models = {}
    for n in n_list:
        masks = row_masks(n)
        A, nrows, _ = distance_distribution(n)
        z = 1 - 2 * Fraction(p_ref).limit_denominator(10 ** 6)
        F = enumerator(n, z, masks)
        ES = sum(z ** popcount(m) for m in masks)
        var_model = max(Fraction(0), F - ES * ES)
        models[n] = float(var_model) ** 0.5
    names = {"allones": None, "thuemorse": thue_morse,
             "single1": single_isolated}
    for label, fn in names.items():
        print(f"  --- {label} ---")
        for n in n_list:
            h = [1] * n if label == "allones" else fn(n)
            S = s_exact(n, h)
            pc = sum(h) / n                       # measured density (float)
            pred_std = models[n]
            ratio = abs(S) / pred_std if pred_std > 0 else float("inf")
            print(f"    n={n:4d}  |S|/n={abs(S)/n:7.4f}  "
                  f"|S|/sqrt(n)={abs(S)/(n**0.5):8.2f}  "
                  f"iid-model-std(p={p_ref})={pred_std:7.2f}  "
                  f"ratio|S|/std={ratio:9.2f}  measured-density={pc:.3f}")


# ------------------------------------------------------------------- main
def main():
    import sys
    print("=" * 78)
    print("FOLD SECOND MOMENT / KRAWTCHOUK — first step (exact arithmetic)")
    print("=" * 78)

    # [1] row weights
    print("\n==[1] ROW SET: |M_d| = 2^popcount(d) ==")
    for n in (8, 16, 32, 64, 128):
        bad, all_d = check_row_weights(n)
        masks = row_masks(n)
        rows_overlap_check(n, masks)
        d = 6
        print(f"    n={n}: |M_d|=2^popcount(d) for all d in {all_d[0]}..{all_d[-1]}"
              f": {'ALL OK' if bad == 0 else 'FAIL ' + str(bad)}"
              f"  (rows={len(masks)}, sizes even)")

    # [2] distance distribution + F_n(1-2p)
    p585 = Fraction(117, 200)          # 0.585
    z585 = 1 - 2 * p585                # -17/100
    print("\n==[2] DECISIVE DISTANCE DISTRIBUTION ==")
    print(f"    reference z = 1-2*{float(p585)} = {z585} (exact {z585})")
    Ns = (16, 24, 32, 48, 64, 96, 128)
    print(f"    {'n':>5} {'A_2':>7} {'A_2/n':>8} {'A_2/n^2':>10} "
          f"{'F_n(z)':>10} {'F_n/n':>8} {'cross-sum':>10}")
    A2s = {}
    Fs = {}
    for n in Ns:
        A, A2, F, offdiag = distance_report(n, z585)
        A2s[n] = A2
        Fs[n] = float(F)
        cross = float(F) - (n - 2)
        print(f"    {n:5d} {A2:7d} {A2/n:8.3f} {A2/n**2:10.3e} "
              f"{float(F):10.3f} {float(F)/n:8.3f} {cross:10.3f}")
    # growth verdict for A_2 via log-log fit on the sparse set
    import math
    def fit(xs, ys):
        n = len(xs)
        lx = [math.log(x) for x in xs]
        ly = [math.log(y) for y in ys]
        mx = sum(lx) / n
        my = sum(ly) / n
        sxx = sum((xi - mx) ** 2 for xi in lx)
        sxy = sum((xi - mx) * (yi - my) for xi, yi in zip(lx, ly))
        return sxy / sxx
    expA2 = fit(list(A2s), list(A2s.values()))
    expF = fit(list(Fs), list(Fs.values()))
    print(f"\n    log-log exponent over n in {min(Ns)}..{max(Ns)}:  "
          f"A_2 ~ n^{expA2:.2f},  F_n(z) ~ n^{expF:.2f}")
    print("    verdict A_2: O(n) if exponent<=~1; Theta(n^2) if ~2 -> "
          f"exponent={expA2:.2f}")
    print("    verdict F_n(z)=O(n) (condition C): exponent={:.2f}".format(expF))

    # extended exact sweep to confirm F_n/n -> 1 and A_2 stays O(n)
    print("\n    extended exact sweep (A_2 and F_n):")
    for n in (256, 512, 1024):
        A, A2, F, offdiag = distance_report(n, z585)
        print(f"      n={n:5d}  A_2={A2:8d}  A_2/n={A2/n:7.3f}  "
              f"F_n(z)={float(F):10.3f}  F_n/n={float(F)/n:7.4f}")

    # [3] identity verification
    identity_check(10, [0.3, 0.5, 0.585])

    # [4] Krawtchouk
    krawtchouk_check([4, 5, 6, 7], [1, Fraction(1, 2), Fraction(3, 4),
                                    Fraction(-17, 100)])

    # [5] controls
    control_report([16, 32, 64, 128], z585, 0.585)

    print("\nDONE")
    # sanity duplicate of F for the capture file (recompute here detached)


if __name__ == "__main__":
    main()
