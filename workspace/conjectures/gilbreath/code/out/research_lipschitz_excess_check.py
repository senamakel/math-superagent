#!/usr/bin/env python3
"""Empirical first-step for candidate `lipschitz-excess-lyapunov`.

Tests the exact identity b_{k+1} = leading zero-run of the local excess
e_i = max(0, |h_i - h_{i+1}| - 1) on halved rows, and the candidate Lyapunov
claim E(h_{k+1}) <= E(h_k) where E(h) = sum_i e_i.

Halved row h_k(i) = A_k(i)/2 for i >= 1 (h_k(0)=1). b_{k+1} = block profile of
row k+1 (leading {0,2} run) / ... actually block_profile counts original {0,2};
halved it counts {0,1}. We compute in original units to match block_profile.
The threshold is |h_i-h_{i+1}|<=1 i.e. |A_i - A_{i+1}|<=2 in original units.
"""
from lib.gilbreath import primes_up_to, rows_generator, block_profile


def halved(row):
    """halved nonnegative row, exact (entries assumed even for i>=1)."""
    return row  # same, but we compute excess in original units: |d|>2 -> excess


def excess(row):
    # e_i in original units: max(0, |A_i - A_{i+1}| - 2)
    return [max(0, abs(row[i] - row[i + 1]) - 2) for i in range(len(row) - 1)]


def E(row):
    return sum(excess(row))


def leading_zero_run(row):
    n = 0
    for x in row:
        if x == 0:
            n += 1
        else:
            break
    return n


def main():
    import sys
    depth = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 2000000
    primes = primes_up_to(limit)
    gen = rows_generator(primes, depth)
    rows = [next(gen) for _ in range(depth + 1)]
    print(f"primes={len(primes)} depth={depth} width={len(rows[0])}")

    # identity check: b_{k+1} == leading zero-run of excess of row k
    id_fail = 0
    for k in range(depth):
        ex = excess(rows[k])
        zero_run = leading_zero_run(ex)
        b_next = block_profile(rows[k + 1])
        if zero_run != b_next:
            id_fail += 1
            if id_fail <= 5:
                print(f"  IDENTITY FAIL k={k}: zero_run={zero_run} b_next={b_next}")
    print(f"IDENTITY b_{k+1}=leading zero-run of excess : {'PASS' if id_fail==0 else f'{id_fail} FAILS'}")

    # E monotonicity
    Ek = [E(rows[k]) for k in range(depth + 1)]
    viol = 0
    first_viol = None
    for k in range(depth):
        if Ek[k + 1] > Ek[k]:
            viol += 1
            if first_viol is None:
                first_viol = k
            if viol <= 8:
                print(f"  E INCREASE k={k}: E={Ek[k]} -> E={Ek[k+1]}  (b_{k}={block_profile(rows[k])}, b_{k+1}={block_profile(rows[k+1])})")
    print(f"E monotone (E_{k+1}<=E_k): {'PASS all' if viol==0 else f'{viol} violations, first at k={first_viol}'}")

    # report E values at regeneration rows and non-regen rows
    regen = []
    for k in range(1, depth + 1):
        if block_profile(rows[k]) > block_profile(rows[k - 1]) - 1:
            regen.append(k)
    print("regen rows (block grew):", regen[:60], "..." if len(regen) > 60 else "")
    # E changes at regens
    sum_inc = 0
    sum_dec = 0
    for k in range(depth):
        d = Ek[k + 1] - Ek[k]
        is_regen = (block_profile(rows[k + 1]) > block_profile(rows[k]) - 1)
        if is_regen:
            sum_inc += d if d > 0 else 0
        else:
            sum_dec += d if d > 0 else 0  # increases on erosion rows
    print(f"total E-increase on regen rows={sum_inc}; on erosion rows={sum_dec}")


if __name__ == "__main__":
    main()
