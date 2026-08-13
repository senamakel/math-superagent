from lib.gilbreath import primes_up_to, rows_generator
import sys

def run(limit, depth, label):
    primes = primes_up_to(limit)
    rows = list(rows_generator(primes, depth))
    A1 = rows[1]
    def block_profile(row):
        L = 0
        for x in row[1:]:
            if x in (0, 2):
                L += 1
            else:
                break
        return L
    events = 0
    n_live = 0
    sumR = 0
    sumR_event = 0
    n_event = 0
    viol = 0
    for k in range(1, depth + 1):
        row = rows[k]
        b = block_profile(row)
        if b + 1 >= len(row):
            continue
        n_live += 1
        y = row[b + 1]
        edge = row[b]
        hi = b + (k - 1)
        if hi >= len(A1):
            continue
        w = A1[b:hi + 1]
        R = max(w) - min(w)
        # also verify intruder <= R (range bound applies to cell b+1)
        if y > R:
            viol += 1
        sumR += R
        if (edge, y) == (2, 4):
            events += 1
            sumR_event += R
            n_event += 1
    print(f"[{label}] live={n_live} events={events} viol_intruder<=R={viol} "
          f"meanR_all={sumR/max(1,n_live):.1f} meanR_at_event={sumR_event/max(1,n_event):.1f}")

run(200000, 160, "sieve2e5 d160")
