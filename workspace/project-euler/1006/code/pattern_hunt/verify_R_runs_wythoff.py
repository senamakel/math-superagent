"""PE1006 pattern: Wythoff run structure of the right-special factors R_k.

Exact verification, k = 1..KMAX, of the conjectures read off the data
(ext_recurrence.txt, k = 1..40):

  (A) V(R_k) (decimal value of the unique right-special length-k factor,
      R_k the unique w in F_k with BOTH w0, w1 in F_{k+1}) is constant
      exactly on runs [s_j, s_{j+1}-1], with s_1 = 2 and
          s_j = floor(j * phi^2),   j = 1, 2, 3, ...
      (upper Wythoff sequence A001950).  The k=1 run [1,1] holds V = 0.
  (B) Within a run, R_k = '0'*(k - s_j) + R_{s_j}   (left zero-padding,
      which is why V(R_k) is constant on the run).
  (C) Every run length is 2 or 3.
  (D) Pure report: runs of constant S1(k) = sum_{w in F_k, w*'1' in F_{k+1}}
      V(w); compare their boundaries with the V-runs.  No conjecture.

First term that would falsify (A): the first j with s_j != floor(j*phi^2),
or the first k where V is not constant on the claimed run.  The program
prints the first mismatch and stops there.

All word computation is exact integer arithmetic.  phi^2 floors use
Decimal with 300 digits: j*phi^2 is irrational for j != 0 and its
distance to the nearest integer is >= 1/(2*j*phi^2 + 2) (> 1e-5 for
j <= 3000), so 300 digits is far beyond the needed margin; every j is
additionally cross-checked at precision 400 and via the Beatty identity
s_j = j + floor(j*phi).

Byproducts (exact, same factor data):
  * J(k) = #{w in F_k : w1 in F_{k+1}} re-verified == 1 + floor((k+1)/phi^2)
  * the k-step recurrence of the cycle-3 note re-verified exactly:
        Psi(k+1) = 100 Psi(k) + 100 V(R_k)^2 + 20 S1(k) + J(k)
  * Psi(k) computed exactly for k <= 150; palindrome digits of Psi(k)
    reported (data show palindromes exactly for k = 1..7).
"""
from decimal import Decimal, getcontext

KMAX = 3000


def fib_prefix(L):
    a, b = '0', '01'
    while len(b) < L:
        a, b = b, b + a
    return b


def main():
    L = 3 * KMAX + 100          # >= Lmin(k) = k + NextFib(k) - 1 for k <= KMAX+1
    W = fib_prefix(L)
    B = [1 if c == '1' else 0 for c in W]
    p10k = [1] * (KMAX + 3)
    for t in range(1, KMAX + 3):
        p10k[t] = p10k[t - 1] * 10

    def build_dict(k):
        """dict: length-k factor (k-bit int) -> its decimal value."""
        d = {}
        mask = (1 << k) - 1
        code, val = 0, 0
        for i in range(k):
            code = (code << 1) | B[i]
            val = val * 10 + B[i]
        for p in range(L - k + 1):
            d[code] = val                      # same code -> same word -> same val
            if p + k < L:
                b = B[p + k]
                d0 = (code >> (k - 1)) & 1     # bit leaving the window
                val = (val - d0 * p10k[k - 1]) * 10 + b
                code = ((code << 1) | b) & mask
        return d

    V_R = [None] * (KMAX + 2)
    S1 = [None] * (KMAX + 2)
    J = [None] * (KMAX + 2)
    Rstr = [None] * (KMAX + 2)
    Psi = [None] * (KMAX + 2)

    Fk = build_dict(1)
    for k in range(1, KMAX + 1):
        Fk1 = build_dict(k + 1)
        rs, ones = [], []
        for code, val in Fk.items():
            e1 = ((code << 1) | 1) in Fk1
            if e1:
                ones.append((code, val))
                if (code << 1) in Fk1:
                    rs.append((code, val))
        assert len(rs) == 1, k
        rcode, rval = rs[0]
        V_R[k] = rval
        S1[k] = sum(v for _, v in ones)
        J[k] = len(ones)
        Rstr[k] = format(rcode, '0%db' % k)
        if k <= 150:
            Psi[k] = sum(v * v for _, v in Fk.items())
        Fk = Fk1

    # ---------------- V-runs ----------------
    runs = []
    start, v0 = 1, V_R[1]
    for k in range(2, KMAX + 1):
        if V_R[k] != v0:
            runs.append((start, k - 1, v0))
            start, v0 = k, V_R[k]
    runs.append((start, KMAX, v0))
    assert runs[0] == (1, 1, 0), runs[0]

    # ---------------- Wythoff check (A,C) ----------------
    getcontext().prec = 300
    phi2 = (Decimal(3) + Decimal(5).sqrt()) / 2
    phi = (Decimal(1) + Decimal(5).sqrt()) / 2
    firstbad = None
    starts = []
    for j in range(1, len(runs)):
        a, b, v = runs[j]
        exp = int(Decimal(j) * phi2)
        getcontext().prec = 400
        exp2 = int(Decimal(j) * phi2)
        exp3 = j + int(Decimal(j) * phi)
        getcontext().prec = 300
        assert exp == exp2 == exp3, (j, exp, exp2, exp3)
        starts.append(a)
        if a != exp:
            firstbad = (j, a, exp)
            break
    lengths = [b - a + 1 for a, b, _ in runs]

    # ---------------- S1 runs ----------------
    s1runs = []
    start, v0 = 1, S1[1]
    for k in range(2, KMAX + 1):
        if S1[k] != v0:
            s1runs.append((start, k - 1, v0))
            start, v0 = k, S1[k]
    s1runs.append((start, KMAX, v0))
    # containment of each S1-run in some V-run
    vi = 0
    contained = 0
    for (a, b, v) in s1runs:
        while runs[vi][1] < a:
            vi += 1
        if runs[vi][0] <= a and b <= runs[vi][1]:
            contained += 1

    # ---------------- exact byproducts ----------------
    c1_check = all(J[k] == 1 + int(Decimal(k + 1) / phi2) for k in range(1, KMAX + 1))
    # recurrence, exact, k = 1..149
    rec_ok = True
    rec_firstbad = None
    for k in range(1, 150):
        lhs = Psi[k + 1]
        rhs = 100 * Psi[k] + 100 * V_R[k] * V_R[k] + 20 * S1[k] + J[k]
        if lhs != rhs:
            rec_ok = False
            rec_firstbad = k
            break
    pals = [k for k in range(1, 151) if str(Psi[k]) == str(Psi[k])[::-1]]

    # ---------------- outputs ----------------
    with open('code/out/r_runs_wythoff.txt', 'w') as fh:
        fh.write(f"KMAX={KMAX} L={L}  #V-runs={len(runs)}\n")
        fh.write(f"run starts s_j (j=1..{len(starts)}), first 60:\n")
        fh.write(' '.join(map(str, starts[:60])) + '\n')
        fh.write(f"last 10 starts: {' '.join(map(str, starts[-10:]))}\n")
        fh.write(f"lengths histogram: {{2:{lengths.count(2)}, "
                 f"3:{lengths.count(3)}, other:{[l for l in set(lengths) if l not in (2, 3)]}}}\n")
        fh.write(f"Wythoff (A): {'OK, all j to ' + str(len(starts)) if firstbad is None else 'FAIL first ' + str(firstbad)}\n")
        fh.write(f"zero-padding (B): checked inline below\n")
        fh.write(f"#S1-runs={len(s1runs)}  S1-runs contained in V-runs: {contained}/{len(s1runs)}\n")
        fh.write(f"J(k)=c1(k+1) exactly k=1..KMAX: {c1_check}\n")
        fh.write(f"Psi recurrence exact k=1..149: {rec_ok}" + ("" if rec_ok else f" first fail at {rec_firstbad}") + "\n")
        fh.write(f"Psi(k) palindrome for k in: {pals}\n")
        fh.write("first runs: (j, s_j, end, len, V)\n")
        for j in range(1, min(len(runs), 25) + 1):
            a, b, v = runs[j - 1]
            if j == 1:
                continue
            fh.write(f"  j={j:4d} s={a:5d} end={b:5d} len={b-a+1} V={v}\n")
    # also raw sequences to files
    with open('code/out/s1_exact.txt', 'w') as fh:
        for k in range(1, KMAX + 1):
            fh.write(f"{k} {S1[k]}\n")
    with open('code/out/vR_exact.txt', 'w') as fh:
        for k in range(1, KMAX + 1):
            fh.write(f"{k} {V_R[k]}\n")

    # ---------------- zero padding check (B) ----------------
    pad_ok = True
    pad_first = None
    for (a, b, v) in runs:
        base = Rstr[a]
        for k in range(a, b + 1):
            if Rstr[k] != '0' * (k - a) + base:
                pad_ok = False
                pad_first = (a, k, Rstr[k][:30], ('0' * (k - a) + base)[:30])
                break
        if not pad_ok:
            break
    print("== V-runs of right-special factors, KMAX =", KMAX)
    print("  #runs:", len(runs), " lengths:", {l: lengths.count(l) for l in sorted(set(lengths))})
    print("  (A) Wythoff run starts s_j = floor(j*phi^2):",
          'VERIFIED for j=1..%d' % len(starts) if firstbad is None else 'FAIL ' + str(firstbad))
    print("  (B) zero-padding within runs:",
          'VERIFIED' if pad_ok else 'FAIL first ' + str(pad_first))
    print("  (D) S1-runs:", len(s1runs), "contained in V-runs:", contained, "/", len(s1runs))
    print("  J(k)=1+floor((k+1)/phi^2) exact:", c1_check)
    print("  Psi recurrence exact k=1..149:", rec_ok)
    print("  Psi(k) palindromes k<=150:", pals)
    print("  first 30 run starts:", starts[:30])
    print("wrote code/out/r_runs_wythoff.txt, s1_exact.txt, vR_exact.txt")


if __name__ == '__main__':
    main()