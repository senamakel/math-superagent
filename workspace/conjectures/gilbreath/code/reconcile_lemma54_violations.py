#!/usr/bin/env python3
"""Reconcile the apparent contradiction between two on-disk Lemma 5.4 checks:
- code/lemma54_rederive.py (pass 1 & 2): reports iff_viol and suff_viol on ALL
  columns of a sequence, WITHOUT requiring the predecessor q_1..q_{n-1} to be
  a SUCCESSFUL Gilbreath sequence.
- the failing-sisters check (code/out/lemma54_failing_sisters.captured.txt):
  filters to columns whose prefix q_1..q_{n-1} is already successful, and finds
  ZERO violations.

Lemma 5.4's hypothesis is that q_1..q_{n-1} is valid & SUCCESSFUL.  The
re-derivation's "success <=> x_L in {0,2}" step uses the GREEN TERMINAL = 1,
which is only 1 when the predecessor's terminal entry is 1, i.e. when the
predecessor is successful.  So rederive's pass-1/2 "violations" should all sit
on columns whose predecessor FAILS.

This script splits every tested column by predecessor-success and reports the
violation counts in each bucket.  If the reconciliation is right, all
iff/suff violations live in the predecessor-FAILS bucket and the
predecessor-SUCCEEDS bucket is clean.
"""
import random


def full_diagonal(qs):
    row = list(qs)
    n = len(qs)
    diag = [row[-1]]
    for _ in range(n - 1):
        row = [abs(row[i] - row[i + 1]) for i in range(len(row) - 1)]
        diag.append(row[-1])
    return diag


def cycle_info(rd):
    body = rd[:-1]
    i = len(body)
    while i > 2 and body[i - 1] in (0, 2):
        i -= 1
    cyc = body[i:]
    if any(x not in (0, 2) for x in cyc):
        return None
    return i, cyc.count(2)


def check_column(qs_upto_n, gstar):
    n = len(qs_upto_n)
    rd_prev = full_diagonal(qs_upto_n[:-1])
    rd_cur = full_diagonal(qs_upto_n)
    ci = cycle_info(rd_prev)
    if ci is None:
        return None
    tau, nu2 = ci
    if tau >= len(rd_cur) - 1:
        return None
    v_n = rd_cur[tau]
    success = (rd_cur[-1] == 1)
    budget = 2 * nu2 + 2
    # predecessor is the full sequence q_1..q_{n-1}: successful iff its own
    # terminal diagonal entry is 1.
    pred_success = (rd_prev[-1] == 1)
    iff_ok = (success == (v_n <= budget))
    suff_ok = (not (gstar <= budget and not success))
    return pred_success, success, (iff_ok, suff_ok), dict(tau=tau, nu2=nu2,
                                                          v_n=v_n, budget=budget)


def gen_valid(gaps, n):
    qs = [2, 3]
    while len(qs) < n:
        qs.append(qs[-1] + random.choice(gaps))
    return qs


def main():
    random.seed(12345)
    families = {"g{2,4,6}": [2, 4, 6],
                "g{2,4,6,8}": [2, 4, 6, 8],
                "g{2,4}": [2, 4]}
    for name, gaps in families.items():
        R = 3000
        N = 40
        buckets = {"pred_succ": {"cols": 0, "succ": 0, "fail": 0,
                                 "iff_viol": 0, "suff_viol": 0},
                   "pred_fail": {"cols": 0, "succ": 0, "fail": 0,
                                 "iff_viol": 0, "suff_viol": 0}}
        for _ in range(R):
            qs = gen_valid(gaps, N)
            for n in range(3, N + 1):
                gs = [qs[k] - qs[k - 1] for k in range(1, n)]
                res = check_column(qs[:n], max(gs))
                if res is None:
                    continue
                pred_success, success, (iff_ok, suff_ok), _ = res
                b = buckets["pred_succ"] if pred_success else buckets["pred_fail"]
                b["cols"] += 1
                if success:
                    b["succ"] += 1
                else:
                    b["fail"] += 1
                if not iff_ok:
                    b["iff_viol"] += 1
                if not suff_ok:
                    b["suff_viol"] += 1
        print(f"== {name} ==")
        for bk, d in buckets.items():
            print(f"  {bk}: cols={d['cols']} (succ={d['succ']}, fail={d['fail']}) "
                  f"iff_viol={d['iff_viol']} suff_viol={d['suff_viol']}")


if __name__ == "__main__":
    main()
