#!/usr/bin/env python3
"""Find the exact range where K(n) satisfies a(n)=a(n-1)+a(n-7)-a(n-8),
and where K(n)=floor(3n/7). Report the first falsifying term of each.
Also compute deg_Q(V(n)^2) exactly for small n.
"""
import mpmath as mp


def K_of_n(n):
    th = mp.pi / n
    t = mp.tan(th)
    best = None
    for k in range(0, n + 1):
        if mp.sin(k * th) - (k + n) * t * mp.cos(k * th) < 0:
            best = k
    return best


def main():
    mp.mp.dps = 80
    N = 300
    K = {n: K_of_n(n) for n in range(1, N + 1)}

    # recurrence a(n)=a(n-1)+a(n-7)-a(n-8): first differences period 7.
    # Find first n=9..N where it fails.
    first_rec_fail = None
    for n in range(9, N + 1):
        if K[n] != K[n - 1] + K[n - 7] - K[n - 8]:
            first_rec_fail = n
            break
    print("first n where the order-8 recurrence fails:", first_rec_fail)

    # also where floor(3n/7) fails
    first_floor_fail = None
    for n in range(3, N + 1):
        if K[n] != 3 * n // 7:
            first_floor_fail = n
            break
    print("first n where K(n)!=floor(3n/7):", first_floor_fail)

    # confirm the recurrence holds over n=3..40 (the tool's 38 terms)
    ok = all(K[n] == K[n - 1] + K[n - 7] - K[n - 8] for n in range(9, 41))
    print("recurrence holds over n=9..40:", ok)


if __name__ == "__main__":
    main()
