#!/usr/bin/env python3
"""
Directive 60 — open step of thread research/threads/dyadic-periodicity-collapse.md:

  "measure inf_n nu2/n for P = 3,5,7,9 (a plateau there would kill the supply
   usefulness of the converse)."

THE MEANINGFUL SUPPLY QUESTION.  The odd-factor converse (CONJECTURED) is:
for an odd-factor periodic halved-gap bit string, nu2(q_n) >= c(P)*n for some
c(P) > 0.  The supply use is: this holds for ALL n (every q_n), which is what
Lemma 5.4's budget needs.  A PLATEAU means the ratio nu2(n)/n keeps dipping
toward 0 at larger and larger n — i.e. there is NO uniform positive c(P) that
works for all sufficiently large n, even though the average ratio is positive.

nu2(n) here = the dyadic FOLD WEIGHT (number of 1-bits among the right-diagonal
fold cells c = 1..n-3, with h the periodic halved-gap bit string), the object
the dyadic dichotomy programs measure, and an upper bound on the true
{0,2}-suffix count.

Reported, for each P, over n up to N:
  avg(n) = mean of nu2(n')/n' over n' in [N/2, N]   (the late average ratio)
  inf over n >= N0  = min_{N0 <= n <= N} nu2(n)/n   for N0 = 100, 500, 1000
  the argmin and value of that inf (with the small-n regime N0=3 excluded as a
  startup artifact)
  whether the inf over large-n keeps DIPPING (a new low set after n > N/3).

If the large-n infimum settles at a positive value and no new low is set late,
the ratio is bounded away from 0 (no plateau in range -> converse not refuted
by an asymptotic dip up to N).

MATH / COST: fold cell c is XOR of h[m-1-c..m-1] with Pascal-row-c mod-2
coefficients (m = n-2).  Computed by submask walk: O(N^2) exact-XORs, O(N)
memory, one h array.  This is a fixed-range measurement, not an answer-space
search.
"""
import time


def submasks(c):
    out = []
    i = c
    while True:
        out.append(i)
        if i == 0:
            break
        i = (i - 1) & c
    return out


def fold_weight_at(h, mm):
    """fold weight over cells c=1..mm-1 using the LAST mm entries of h."""
    base = len(h) - mm
    w = 0
    for c in range(1, mm):
        s = 0
        for i in submasks(c):
            s ^= h[base + mm - 1 - c + i]
        w += s
    return w


def run(P, word, N):
    h = [int(word[j % len(word)]) for j in range(N + 2)]
    # collect nu2(n) for all n up to N
    vals = {}   # n -> fold weight
    for n in range(4, N + 1):
        mm = n - 2
        w = fold_weight_at(h[:n], mm)
        vals[n] = w

    # late average ratio over [N/2, N]
    half = N // 2
    late_avg = sum(vals[n] / n for n in range(half, N + 1)) / (N + 1 - half)

    # inf over n >= N0
    def inf_from(N0):
        seg = [(n, vals[n] / n) for n in range(N0, N + 1)]
        best = min(r for _, r in seg)
        arg = next(n for n, r in seg if r == best)
        return best, arg, vals[arg]

    inf100 = inf_from(100)
    inf500 = inf_from(500)
    inf1000 = inf_from(1000)

    # plateau / late-dipping check: is the running min still being updated past N/3?
    running = float('inf')
    late_updates = []
    for n in range(4, N + 1):
        r = vals[n] / n
        if r < running:
            running = r
            if n > N // 3:
                late_updates.append((n, vals[n], round(r, 5)))
    return late_avg, inf100, inf500, inf1000, late_updates


def main():
    N = 3000
    words = {3: [0, 0, 1], 5: [0, 0, 0, 0, 1],
             7: [0] * 6 + [1], 9: [0] * 8 + [1]}
    print("Directive 60 open step: asymptotic inf_n nu2(n)/n for odd-factor periods")
    print("nu2(n) = dyadic fold weight over right-diagonal fold cells c=1..n-3")
    print("        (periodic 2-then-odds halved-gap bits, word repeated).")
    print("N =", N, " exact integers, O(N^2) submask-XORs, O(N) memory.\n")
    hdr = (f"{'P':>2} {'word':>11} {'late avg r':>9} {'inf>=100':>8} "
           f"{'inf>=500':>8} {'inf>=1000':>9} {'argmin>=1000':>11}")
    print(hdr)
    print("-" * len(hdr))
    results = {}
    for P in (3, 5, 7, 9):
        w = words[P]
        t0 = time.time()
        late_avg, inf100, inf500, inf1000, late_up = run(P, w, N)
        dt = time.time() - t0
        results[P] = (late_avg, inf100, inf500, inf1000, late_up)
        print(f"{P:>2} {''.join(map(str,w)):>11} {late_avg:>9.4f} {inf100[0]:>8.4f} "
              f"{inf500[0]:>8.4f} {inf1000[0]:>9.4f} {inf1000[1]:>11}   ({dt:.1f}s)")
        if late_up:
            print(f"     late new lows past n={N//3}: {late_up[:6]}")
        else:
            print(f"     no new low past n={N//3}: large-n infimum set early, no asymptotic plateau")

    print("\nVERDICT bounds (numerical, over n<=%d, exact integers):" % N)
    for P in (3, 5, 7, 9):
        late_avg, inf100, inf500, inf1000, late_up = results[P]
        stable = (len(late_up) == 0) or (late_avg > 0.05 and inf1000[0] > 0.01)
        print(f"  P={P}: late-avg ratio {late_avg:.4f}, inf over n>=1000 = "
              f"{inf1000[0]:.4f}, argmin n={inf1000[1]}, {'no late plateau' if stable else 'LATE PLATEAU DIPPING'}")
    print("\nReading: for each P, if inf over n>=1000 stays positive and no late new low,")
    print("the converse is NOT refuted by an asymptotic dip up to N=3000 — but the")
    print("converse remains CONJECTURED (this is numerical evidence only, not a proof).")


if __name__ == "__main__":
    main()
