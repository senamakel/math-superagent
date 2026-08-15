#!/usr/bin/env python3
"""Re-derive Granville's Lemma 5.4 as a constructive descent, and stress-test
it on FAILING sequences, not only the all-successful prime columns.

Lemma 5.4 (arXiv:2607.04166): for a valid, successful q_1..q_{n-1}, the
augmented sequence q_1..q_n succeeds if g*_n <= 2*nu2(q_{n-1}) + 2, where
g*_n = max(g_2..g_n) is the record gap and nu2(q_{n-1}) is the number of 2s in
the 0-2 cycle of the right diagonal of q_{n-1}.

Right diagonal automaton (Granville's augment):
  new_diag[0] = q_n
  new_diag[j+1] = |new_diag[j] - old_diag[j]|
  success of q_1..q_n  <=>  new_diag[-1] == 1

The 0-2 cycle of old_diag starts at index tau (maximal {0,2} suffix of the
body, excluding the green terminal).  nu2 = #2s in it.
v_n = new_diag[tau].  The lemma's iff form: success <=> v_n <= 2*nu2 + 2.

The published proof runs the descent "delta_k in {delta_{k-1}-2, delta_{k-1}}
unless delta_{k-1}=0, an exception to ignore".  We handle the delta=0 case
explicitly: at a 2-aligned position a current 0 BOUNCES to 2 (|0-2|), and at a
0-aligned position it stays 0; either way value stays in {0,2}, and the only
loss is it does not descend.  So the honest invariant is: each 2 in the cycle
consumes <= 2 units of height, each 0 consumes <= 0, and a bounce costs the
height already spent but keeps the value in {0,2}.  Height budget from v_n to
reach {0,1}-region is v_n, so v_n <= 2*nu2 + 2 suffices (the +2 for the
terminal 0/2 slack).
"""
import random


def cycle_info(rd):
    """Right diagonal rd = [delta_0..delta_{n-1}] (delta_0 = q).
    Returns (tau, nu2) of the maximal {0,2} suffix of rd[:-1], or None if none.
    tau = start index of the 0-2 cycle in rd."""
    body = rd[:-1]
    i = len(body)
    while i > 2 and body[i - 1] in (0, 2):
        i -= 1
    cyc = body[i:]
    if any(x not in (0, 2) for x in cyc):
        return None
    return i, cyc.count(2)


def full_diagonal(qs):
    """Right diagonal of the sequence qs, via the absolute-diff triangle.
    Returns [delta_0..delta_{n-1}], delta_0 = qs[-1]."""
    row = list(qs)
    n = len(qs)
    diag = [row[-1]]
    for _ in range(n - 1):
        row = [abs(row[i] - row[i + 1]) for i in range(len(row) - 1)]
        diag.append(row[-1])
    return diag


def augment(rd, a):
    nd = [a]
    val = a
    for x in rd:
        val = abs(val - x)
        nd.append(val)
    return nd


def check_column(qs_upto_n, gstar):
    """qs_upto_n = full sequence q_1..q_n.  Returns (ok, note) per Lemma 5.4
    iff/sufficiency on the final column n."""
    n = len(qs_upto_n)
    rd_prev = full_diagonal(qs_upto_n[:-1])
    rd_cur = full_diagonal(qs_upto_n)
    ci = cycle_info(rd_prev)
    if ci is None:
        return None, "no 0-2 cycle in predecessor"
    tau, nu2 = ci
    if tau >= len(rd_cur) - 1:
        return None, "cycle start at/beyond last index"
    v_n = rd_cur[tau]
    success = (rd_cur[-1] == 1)
    budget = 2 * nu2 + 2
    if success is None:
        return None, "?"
    # iff form
    iff_ok = (success == (v_n <= budget))
    # sufficiency
    suff_ok = (not (gstar <= budget and not success))
    return (iff_ok, suff_ok), dict(tau=tau, nu2=nu2, v_n=v_n, success=success,
                                   budget=budget, gstar=gstar)


def gen_valid(start, gaps, n):
    """2-then-odds strictly increasing valid sequence: q0=2, q1=3, then odd
    q_{k+1}=q_k+g with g from `gaps`; returns list length n."""
    qs = [2, 3]
    while len(qs) < n:
        qs.append(qs[-1] + random.choice(gaps))
    return qs


def gen_failing_candidates():
    """Hand-built failing 2-then-odds valid sequences (Colonna deletion class
    and corridor-failing class)."""
    seqs = []
    # Colonna: delete 7 -> (2,3,5,11,13,17,19,..) gaps 2,2,6,2,4,2 (g<=6)
    seqs.append((2, 3, 5, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43))
    # corridor failing example from Granville table 10 region (gaps small)
    seqs.append((2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 49, 53, 55, 65))
    # (2,3,5,9,11,13,15,17,25,27,29) -> Granville's failing corridor seq (len 11)
    seqs.append((2, 3, 5, 9, 11, 13, 15, 17, 25, 27, 29))
    return seqs


def main():
    random.seed(12345)
    # ---- pass 1: hand-built failing candidates, report per-column ----
    print("== Pass 1: hand-built sequences ==")
    for seq in gen_failing_candidates():
        ss = list(seq)
        fails = []
        for n in range(3, len(ss) + 1):
            gs = [ss[k] - ss[k - 1] for k in range(1, n)]
            gstar = max(gs)
            chk, info = check_column(ss[:n], gstar)
            if chk is None:
                continue
            if not chk[0]:
                fails.append((n, info))
        finals = full_diagonal(ss)
        print(f"seq {ss} bottom={finals[-1]} success={finals[-1]==1}")
        print(f"   iff-violations over its columns: {len(fails)}")
        for (n, info) in fails[:8]:
            print(f"   col n={n}: {info}")

    # ---- pass 2: random valid gap families, count column-level violations ----
    print("\n== Pass 2: random valid 2-then-odds, many failing ==")
    families = {
        "g{2,4,6}": [2, 4, 6],
        "g{2,4,6,8}": [2, 4, 6, 8],
        "g{2,4}": [2, 4],
    }
    for name, gaps in families.items():
        R = 3000
        N = 40
        col_tested = 0
        iff_viol = 0
        suff_viol = 0
        n_success_cols = 0
        n_fail_cols = 0
        for _ in range(R):
            qs = gen_valid([2, 3], gaps, N)
            for n in range(3, N + 1):
                gs = [qs[k] - qs[k - 1] for k in range(1, n)]
                chk, info = check_column(qs[:n], max(gs))
                if chk is None:
                    continue
                col_tested += 1
                if info["success"]:
                    n_success_cols += 1
                else:
                    n_fail_cols += 1
                if not chk[0]:
                    iff_viol += 1
                if not chk[1]:
                    suff_viol += 1
        print(f"{name}: {col_tested} cols tested "
              f"({n_success_cols} succ, {n_fail_cols} FAIL), "
              f"iff_viol={iff_viol}, suff_viol={suff_viol}")

    # ---- pass 3: the delta=0 case rate on real random columns ----
    print("\n== Pass 3: delta=0 bounce-rate inside the gray block ==")
    rd_cases = 0
    bounce = 0
    for _ in range(2000):
        qs = gen_valid([2, 3], [2, 4, 6], 40)
        for n in range(6, 41):
            rd = full_diagonal(qs[:n])
            ci = cycle_info(full_diagonal(qs[:n - 1]))
            if ci is None:
                continue
            tau, nu2 = ci
            if tau >= n:
                continue
            rd_cases += 1
            # gray block indices tau..n-2 of rd_cur
            for k in range(tau, n - 1):
                ante = rd[k - 1] if k >= 1 else rd[0]
                # antecedent alignment: rd_prev[k-1] in {0,2}
                if ante == 0:
                    bounce += 1
    print(f"cells where antecedent value in gray block = 0: {bounce} of {rd_cases}")


if __name__ == "__main__":
    main()
