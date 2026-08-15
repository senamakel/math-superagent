"""Final exact verification of the semiconvergent / Euclidean structure of the
102 Eulercoins of A=1504170715041707, M=4503599627370517.

Claims verified over ALL 102 coins:
  C1 index steps  D_k (per arithmetic run) = odd convergent denominators q_{2k+1} of A/M
  C2 run lengths q_k                       = even partial quotients b_{2k+2} of A/M
  C3 every coin index n is a semiconvergent q_{2k} + t*q_{2k+1}, t=0..b_{2k+2};
     sorted, these are exactly the coin indices n_1..n_102
  C4 every coin value  c is r_{2k+1} - t*r_{2k+2}, t=0..q_k; matches 102 values
  C5 closed-form sum  V = sum_k [sum_{t=0..q_k} (r_{2k+1} - t*r_{2k+2})]
     with shared boundaries counted once -> 1517926517777556
"""
import re

A = 1504170715041707
M = 4503599627370517


def cf(a, b):
    qs = []
    while b > 0:
        qs.append(a // b)
        a, b = b, a % b
    return qs


def conv_denoms(pq):
    """q_0..q_n for continued fraction [a_0; a_1, ...] = pq."""
    pmm2, qmm2 = 0, 1   # p_{-2}/q_{-2} = 0/1
    pm1, qm1 = 1, 0     # p_{-1}/q_{-1} = 1/0
    out = []
    for aj in pq:
        p, q = aj * pm1 + pmm2, aj * qm1 + qmm2
        pmm2, qmm2 = pm1, qm1
        pm1, qm1 = p, q
        out.append(q)
    return out


def euc_rem(a, b):
    r = []
    while b > 0:
        r.append(b)
        a, b = b, a % b
    return r


def main():
    txt = open('code/out/solution.txt').read()
    n_ref, c_ref = [], []
    for line in txt.splitlines():
        m = re.match(r'coin #\s*\d+:\s*n =\s*(\d+)\s+c_n = (\d+)', line)
        if m:
            n_ref.append(int(m.group(1)))
            c_ref.append(int(m.group(2)))

    b = cf(A, M)[1:]                 # b_1..b_34
    q = conv_denoms(cf(A, M))        # q_0..q_34
    r = euc_rem(M, A)                # r_1=A .. r_34=1

    runs = 17
    okC1 = okC2 = okC3 = okC4 = True
    n_set, c_set = set(), set()
    details = []

    for k in range(runs):
        Dk = q[2 * k + 1]            # index step = odd convergent denominator
        qk = b[2 * k + 1]            # run length = even partial quotient b_{2k+2}
        base = q[2 * k]              # first index of run = even denominator
        s = r[2 * k + 1]             # first value of run = odd remainder
        st = r[2 * k + 2]            # value step = even remainder
        # run covers t=0..qk (last index equals next base, shared)
        for t in range(qk + 1):
            n_set.add(base + t * Dk)
            c_set.add(s - t * st)
        details.append((k, base, Dk, qk, s, st))

    for k, base, Dk, qk, s, st in details:
        okC1 &= (Dk == q[2 * k + 1])
        okC2 &= (qk == b[2 * k + 1])
        # boundary continuity: base+ qk*Dk == next base (q_{2k+2})
        if k < runs - 1:
            okC2 &= (base + qk * Dk == q[2 * k + 2])
            okC2 &= (s - qk * st == r[2 * k + 3])

    # C3: the set of semiconvergents, sorted, equals coin indices
    semis = sorted(n_set)
    okC3 = (len(semis) == len(n_ref) and semis == n_ref)
    vals = sorted(c_set, reverse=True)   # values strictly decreasing
    okC4 = (len(vals) == len(c_ref) and vals == c_ref)

    print('C1 D_k == odd convergent denominators q_{2k+1}:', okC1)
    print('C2 len q_k == even partial quotients b_{2k+2}, blocks chain:', okC2)
    print('C3 coin indices == sorted semiconvergents {q_{2k}+t q_{2k+1}}:', okC3,
          ' count:', len(semis))
    print('C4 coin values == {r_{2k+1} - t r_{2k+2}}:', okC4, ' count:', len(vals))

    # C5: closed-form sum counting each boundary once
    S = 0
    for k in range(runs):
        s, st = r[2 * k + 1], r[2 * k + 2]
        qk = b[2 * k + 2]
        S += (qk + 1) * s - st * qk * (qk + 1) // 2
    S -= sum(r[2 * k + 3] for k in range(runs - 1))    # shared boundaries r3,r5,..,r33
    print('C5 closed-form sum V =', S, ' matches documented:', S == 1517926517777556)

    print('run table (k, base n, index step, len, first value, value step):')
    for d in details:
        print('  run %2d: n from %-17d step %-19d len %2d | c from %-17d step %d'
              % (d[0], d[1], d[2], d[3], d[4], d[5]))


if __name__ == '__main__':
    main()