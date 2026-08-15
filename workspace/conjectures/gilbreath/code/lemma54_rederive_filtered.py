#!/usr/bin/env python3
"""Re-derive Granville's Lemma 5.4 on its OWN domain: columns whose
predecessor is genuinely successful.

Lemma 5.4 premise: q_1..q_{n-1} is a VALID, SUCCESSFUL sequence (every
preceding column succeeded).  Conclusion (sufficiency): if
g*_n = max gaps <= 2*nu2(q_{n-1}) + 2, then q_1..q_n also succeeds.

The un-filtered run (code/out/lemma54_rederive.captured.txt) reported
suff_viol>0, but that counts columns after an already-failed prefix, where
"failure" is vacuous.  Here we track the running validity of the sequence
and only count a sufficiency-violation when every prior column succeeded —
i.e. the lemma is actually in force at column n.

valids:     sequence is Gilbreath-valid at every column <= n.
pre_succ:  all columns 2..n-1 succeeded (valid up to n-1).
A true counterexample: pre_succ AND g*_n <= 2*nu2+2 AND column n fails.
"""
import random


def cycle_info(rd):
    body = rd[:-1]
    i = len(body)
    while i > 2 and body[i - 1] in (0, 2):
        i -= 1
    cyc = body[i:]
    if any(x not in (0, 2) for x in cyc):
        return None
    return i, cyc.count(2)


def full_diagonal(qs):
    row = list(qs)
    n = len(qs)
    diag = [row[-1]]
    for _ in range(n - 1):
        row = [abs(row[i] - row[i + 1]) for i in range(len(row) - 1)]
        diag.append(row[-1])
    return diag


def column_success(qs_upto_n):
    rd = full_diagonal(qs_upto_n)
    return rd[-1] == 1


def main():
    random.seed(12345)
    families = {
        "g{2,4,6}": [2, 4, 6],
        "g{2,4,6,8}": [2, 4, 6, 8],
        "g{2,4}": [2, 4],
    }
    for name, gaps in families.items():
        R = 6000
        N = 40
        # running validity state for each seq
        col_applicable = 0      # columns where the lemma is in force (pre_succ)
        col_total = 0
        n_fail_cols = 0         # failing columns overall
        suff_counter = 0        # TRUE Lemma 5.4 sufficiency counterexamples
        pre_fail_wasted = 0     # suff_viol whose predecessor already failed (vacuous)
        # track a concrete example
        example = None
        for _ in range(R):
            qs = [2, 3]
            while len(qs) < N:
                qs.append(qs[-1] + random.choice(gaps))
            # running: valid_up_to(n) = all columns 2..n succeeded
            valid = {}   # valid[n]
            prev_ok = True  # columns 2..n-1 all succeeded
            for n in range(3, N + 1):
                ok = column_success(qs[:n])
                valid[n] = prev_ok and ok
                col_total += 1
                if not ok:
                    n_fail_cols += 1
                # lemma premise: valid up to n-1 means all prior columns succeeded
                pre_succ = prev_ok   # all of 2..n-1 succeeded
                if pre_succ:
                    col_applicable += 1
                    gs = [qs[k] - qs[k - 1] for k in range(1, n)]
                    gstar = max(gs)
                    rd_prev = full_diagonal(qs[:n - 1])
                    ci = cycle_info(rd_prev)
                    if ci is None or ci[0] >= n:
                        prev_ok = valid[n]
                        continue
                    tau, nu2 = ci
                    budget = 2 * nu2 + 2
                    if gstar <= budget and not ok:
                        # true counterexample: lemma in force, hyp holds, col fails
                        suff_counter += 1
                        if example is None:
                            example = (
                                n, list(qs[:n]), gstar, nu2, budget, tau)
                prev_ok = valid[n]
        print(f"{name}: cols={col_total} applicable(pre_succ)={col_applicable} "
              f"fail_cols={n_fail_cols} TRUE_LEMMA_COUNTEREXAMPLES={suff_counter}")
        if example:
            n, seq, gstar, nu2, budget, tau = example
            print(f"   example: n={n} seq={seq} g*={gstar} nu2={nu2} "
                  f"budget={budget} -> still fails")
    print("\nA positive suff_counter refutes Lemma 5.4's sufficiency "
          "on the general valid 2-then-odds class (its own domain).")


if __name__ == "__main__":
    main()
