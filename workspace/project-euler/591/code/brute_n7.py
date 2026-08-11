"""Independent brute force for PE591 at n=10^7.

For each d in a chosen list, scan every b in [-floor(n/sqrt(d)), +floor(n/sqrt(d))],
set a = nint(pi - b*sqrt(d)) clamped to [-n,n], and minimise
|pi - (a + b sqrt(d))| = ||b sqrt(d) - pi||_Z.  All arithmetic in mpmath at dps=40.

This is a mid-scale independent check (n=1e7) between the validated n=1e6 scale
and the target n=1e13, against the corrected both-sides solver results in
results_full_bothsides.txt.

Usage: python brute_n7.py
Output: results_brute_n7.txt (rows: d b a |a| error) plus a comparison report
on stdout against /workspace/results_full_bothsides.txt.
"""
import math
import mpmath as mp

mp.mp.dps = 40

PI = mp.mpf('3.1415926535897932384626433832795028841971693993751058209749445923')
N = 10**7
DS = [2, 13, 14, 15, 18, 19, 21, 22, 27, 29, 41, 42, 52, 59, 80, 98]

def brute_bqa(d, n):
    """Return (b, a, err) minimising |pi - (a + b*sqrt(d))|, |a|,|b| <= n,
    scanning all b in [-floor(n/sqrt(d)), floor(n/sqrt(d))], a=nint(...) clamped."""
    sd = mp.sqrt(d)
    B = int(mp.floor(n / sd))
    best_b = best_a = None
    best_err = None
    for b in range(-B, B + 1):
        a = int(mp.nint(PI - b * sd))
        if a < -n:
            a = -n
        elif a > n:
            a = n
        err = abs((a + b * sd - PI))
        if best_err is None or err < best_err:
            best_err = err
            best_b, best_a = b, a
    return best_b, best_a, best_err

def main():
    rows = []
    report = []
    for d in DS:
        b, a, err = brute_bqa(d, N)
        rows.append((d, b, a, abs(a), err))
        print(f"d={d:2d} b={b:12d} a={a:13d} |a|={abs(a):13d} err={mp.nstr(err, 18)}",
              flush=True)
    with open('/workspace/results_brute_n7.txt', 'w') as f:
        for (d, b, a, absa, err) in rows:
            f.write(f"{d} {b} {a} {absa} {mp.nstr(err, 18)}\n")

    # Compare against corrected both-sides solver file: rows 'd b a |a|', final 'S value'
    solver = {}
    with open('/workspace/results_full_bothsides.txt') as f:
        for line in f:
            parts = line.split()
            if not parts or parts[0] == 'S':
                continue
            solver[int(parts[0])] = tuple(int(x) for x in parts[1:4])

    print("\n=== comparison with results_full_bothsides.txt ===")
    ok = True
    for (d, b, a, absa, err) in rows:
        if d in solver:
            sb, sa, sabsa = solver[d]
            match = (sa == a)
            ok = ok and match
            print(f"d={d:2d}: solver(a={sa}, b={sb}) brute(a={a}, b={b}) |a| "
                  f"{'MATCH' if match else 'MISMATCH'}")
        else:
            ok = False
            print(f"d={d:2d}: WARNING not present in solver results")
    print("\nAll tested d match:", ok)

if __name__ == '__main__':
    main()