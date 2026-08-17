"""PE1006 pattern hunt, cycle 3b: run structure of the right-special factors.

Findings to pin down exactly (k = 1..400):
  * R_k (unique right-special length-k factor, as a string) satisfies
    R_{k+1} = '0' + R_k over runs, i.e. V(R_k) is constant on runs
    (V = decimal value of the 0/1 string).
  * runs: maximal intervals [a,b] of constant V(R_k); report all run
    boundaries for k=1..400 and compare against Fibonacci numbers
    (F_n, F_n - 1, F_n - 2 patterns).
  * each run's base word: check whether the run's word is a conjugate
    (rotation) of some S_n.
  * S1(k): behaviour within runs — test S1(k+1) ?= 10*S1(k) + f(R_k, J(k))
    by brute data; report S1 mod M sequence for tool analysis.

Facts already verified by the sibling script (k=1..400): recurrence with
     Psi(k+1) = 100*Psi(k) + 100*V(R_k)^2 + 20*S1(k) + J(k)   mod M
and J(k) = # length-(k+1) factors ending in '1' = c1(k+1).
"""
M = 101001001


def fib_prefix(L):
    a, b = '0', '01'
    while len(b) < L:
        a, b = b, b + a
    return b


def fibs_up_to(N):
    f = [1, 1]
    while f[-1] <= N:
        f.append(f[-1] + f[-2])
    return f[2:]  # 2, 3, 5, 8, ...


def rot_prefixes(w):
    """All rotations of w, as strings."""
    return {w[i:] + w[:i] for i in range(len(w))}


def main():
    kmax = 400
    W = fib_prefix(4 * kmax + 10)
    L = len(W)
    F = {}
    for k in range(1, kmax + 2):
        F[k] = {W[i:i + k] for i in range(L - k + 1)}

    R = {}
    for k in range(1, kmax + 1):
        Fk, Fk1 = F[k], F[k + 1]
        spec = [w for w in Fk if (w + '0' in Fk1) and (w + '1' in Fk1)]
        assert len(spec) == 1
        R[k] = spec[0]

    # runs of constant value V(R_k)  (since R_{k+1}='0'+R_k keeps value)
    runs = []
    start = 1
    v_prev = int(R[1])
    for k in range(2, kmax + 1):
        v = int(R[k])
        if v != v_prev:
            runs.append((start, k - 1, R[start], v_prev))
            start, v_prev = k, v
    runs.append((start, kmax, R[start], v_prev))

    print(f"== runs of constant V(R_k), k=1..{kmax}: {len(runs)} runs ==")
    print("  run      k range        V(R_k)   word")
    for a, b, word, v in runs:
        print(f"  [{a:3d},{b:3d}]  len {b-a+1:3d}   {v:<13d}  {word}")
    # breakpoints
    breaks = [r[0] for r in runs[1:]]
    Fs = fibs_up_to(kmax)
    print()
    print("run starts:", breaks)
    print("check starts against F_n, F_n-1, F_n-2:")
    for bs in breaks:
        hit = [f for f in Fs if f == bs or f - 1 == bs or f - 2 == bs]
        print(f"   {bs}: {'F' + str([f for f in Fs if f in (bs, bs+1, bs+2)]) if hit else 'no fib close'}")

    # each run's base word a conjugate of some S_n?
    S = {0: '0', 1: '01'}
    n = 2
    while len(S[n - 1]) < kmax:
        S[n] = S[n - 1] + S[n - 2]
        n += 1
    print()
    print("== run words vs conjugates of S_n ==")
    all_cj = {}
    for n in S:
        all_cj[n] = rot_prefixes(S[n])
    nbad = 0
    for a, b, word, v in runs:
        hits = [n for n in all_cj if word in all_cj[n]]
        if not hits:
            nbad += 1
            print(f"  run [{a},{b}] word {word}: NOT a conjugate of any S_n")
        else:
            print(f"  run [{a},{b}] word {word}: conjugate of S_{max(hits)}  (S={S[max(hits)]})")
    print(f"runs not conjugates of any S_n: {nbad}")

    # S1(k) sequence and within-run behaviour
    print()
    print("== S1(k) mod M: first few and within-run tests ==")
    # recompute S1 mod M by brute for k=1..kmax
    pow10 = [1] * (kmax + 2)
    for t in range(1, kmax + 2):
        pow10[t] = pow10[t - 1] * 10 % M

    def vmod(s):
        v = 0
        for ch in s:
            v = (v * 10 + int(ch)) % M
        return v

    S1 = {}
    for k in range(1, kmax + 1):
        s1 = 0
        for w in F[k]:
            if w + '1' in F[k + 1]:
                s1 = (s1 + vmod(w)) % M
        S1[k] = s1
    print("S1(1..25) mod M:", [S1[k] for k in range(1, 26)])
    # within-run test: is S1(k+1) = 10*S1(k) + g(k) with small/structured g?
    # print g(k) = S1(k+1) - 10*S1(k) mod M at run interiors and boundaries
    print("g(k) = S1(k+1)-10*S1(k) mod M, k=1..60 (| marks run end):")
    row = []
    for k in range(1, 61):
        g = (S1[k + 1] - 10 * S1[k]) % M
        row.append(f"{k}:{g}")
    print("  " + "  ".join(row[:20]))
    print("  " + "  ".join(row[20:40]))
    print("  " + "  ".join(row[40:60]))
    # save S1
    with open('code/out/s1_res.txt', 'w') as fh:
        for k in range(1, kmax + 1):
            fh.write(f"{k} {S1[k]}\n")
    # save V(R_k) mod M
    with open('code/out/vR_res.txt', 'w') as fh:
        for k in range(1, kmax + 1):
            fh.write(f"{k} {vmod(R[k])}\n")
    print("wrote code/out/s1_res.txt, code/out/vR_res.txt")


if __name__ == '__main__':
    main()