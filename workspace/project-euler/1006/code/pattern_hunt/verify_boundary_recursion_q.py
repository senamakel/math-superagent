"""Verify the O(n) recursion for B_n = Psi(F_{n+1}-1) at the Fibonacci
boundary, where the factor set = cyclic windows of the standard word q_n.

q_1='0', q_2='01', q_{n+1}=q_n q_{n-1};  |q_n| = F_{n+1}.

The cyclic windows of q_{n+1} = S T (S=q_n, T=q_{n-1}, a=|S|, b=|T|) of length
a+b-1 are exactly q_{n+1} with one letter deleted:
  - delete S-letter i (i = 0..a-1): window = S[i+1:] T S[:i]
  - delete T-letter j (j = 0..b-1): window = T[j+1:] S T[:j]

So the multisets are
  W(S;T) = { S[i+1:] T S[:i] : i }   (a windows)
  W(T;S) = { T[j+1:] S T[:j] : j }   (b windows)

Their value sets are:
  val(W(S;T)) = val(S[i+1:] S[:i]) * 10^b + val(T)
              = cyc_i(S) * 10^b + val(T),   where cyc_i(S) = val of S rotated
                left by i+1, truncated to a-1  (= S[i+1:] S[:i], length a-1)
  val(W(T;S)) = val(T[j+1:] T[:j]) * 10^(a) ... NO: T[j+1:] T[:j] has length
                b-1, and it is followed by S, so
              = val(T[j+1:] T[:j]) * 10^a + val(S)

WAIT.  Check against the concrete example q_4 = S T = '010' '01':
  - delete S-letter i=0 ('0'): S[1:] T S[:0] = '10' + '01' + '' = '1001'
  - delete S-letter i=1 ('1'): S[2:] T S[:1] = '0' + '01' + '0' = '0010'
  - delete S-letter i=2 ('0'): S[3:] T S[:2] = '' + '01' + '01' = '0101'
  - delete T-letter j=0 ('0'): T[1:] S T[:0] = '1' + '010' + '' = '1010'
  - delete T-letter j=1 ('1'): T[2:] S T[:1] = '' + '010' + '0' = '0100'
which matches the hand-check.  So:

  val(S[i+1:] T S[:i]) = val(S[i+1:] S[:i]) * 10^b + val(T)     (length b part)
  val(T[j+1:] S T[:j]) = val(S) * 10^(b-1) ... NO: T[j+1:] has length b-1-j,
                         T[:j] has length j, so T[j+1:] T[:j] has length b-1,
                         followed by S (length a), total a+b-1: value
                         val(T[j+1:] T[:j]) * 10^a + val(S).

Hence
  B_{n+1} = sum_i (cyc_i(S)*10^b + val(T))^2
          + sum_j (val(T[j+1:] T[:j])*10^a + val(S))^2
where cyc_i(S) = val(S[i+1:] S[:i])  (length a-1) and
      cyc_j(T) = val(T[j+1:] T[:j])  (length b-1).

Expand:
  B_{n+1} = 10^{2b} * sum_i cyc_i(S)^2
          + 2*10^b * val(T) * sum_i cyc_i(S)
          + a * val(T)^2
          + 10^{2a} * sum_j cyc_j(T)^2
          + 2*10^a * val(S) * sum_j cyc_j(T)
          + b * val(S)^2.

But sum_i cyc_i(S)^2 = B_n (windows of q_n) and sum_j cyc_j(T)^2 = B_{n-1}
(windows of q_{n-1}).  And sum_i cyc_i(S) = M1(a-1), sum_j cyc_j(T) = M1(b-1)
(position-balance at these k).  Thus:

  B_{n+1} = 10^{2b} B_n + 2*10^b val(T) M1(a-1) + a val(T)^2
          + 10^{2a} B_{n-1} + 2*10^a val(S) M1(b-1) + b val(S)^2.

This is the corrected recursion (the previous one had 10^{2b-2} and 10^{b-1}
for the T-window terms, which was wrong because T[j+1:] T[:j] is followed by
S of length a, not a-1).
"""
import sys

sys.path.insert(0, "code/mech")
sys.path.insert(0, "code")
from mech_psi import mech_psi  # noqa: E402


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def std_word(n):
    if n == 1:
        return "0"
    if n == 2:
        return "01"
    return std_word(n - 1) + std_word(n - 2)


def val(w):
    return int(w) if w else 0


def c1(k):
    import math
    return 1 + int(k * (3 - math.sqrt(5)) / 2)


def repunit(k):
    return (10 ** k - 1) // 9


def M1(k):
    return c1(k) * repunit(k)


def cyclic_windows(w):
    """All cyclic windows of w of length |w|-1, as strings."""
    L = len(w)
    out = []
    for s in range(L):
        cyc = w[s:] + w[:s]
        out.append(cyc[: L - 1])
    return out


def main():
    print("== (0) cyclic windows of q_n == factor set at k = |q_n|-1 ==")
    ok_id = True
    for n in range(2, 15):
        k = len(std_word(n)) - 1
        tA, tB, vA, vB = mech_psi(k)
        assert tA == tB
        cw = sum(val(w) ** 2 for w in cyclic_windows(std_word(n)))
        good = (cw == tA)
        ok_id = ok_id and good
        print(f"  n={n:2d} |q_n|={len(std_word(n)):4d} k={k:4d} match={good}")
    print(f"  identity holds n=2..14: {ok_id}")

    print("\n== (1) corrected O(n) recursion ==")
    B = {1: 0, 2: 1, 3: 101}   # B_1=Psi(0)=0, B_2=Psi(1)=1, B_3=Psi(2)=101
    V = {1: 0, 2: 1, 3: 10}    # val(q_n)
    orac = {}
    for n in range(2, 15):
        k = fib(n + 1) - 1
        tA, tB, vA, vB = mech_psi(k)
        orac[n] = tA
    ok_all = True
    print("  n  B_rec(n) == oracle(n)")
    for n in range(2, 13):
        S, T = std_word(n), std_word(n - 1)
        a, b = len(S), len(T)
        vs, vt = val(S), val(T)
        B_next = (
            pow(10, 2 * b) * B[n]
            + 2 * pow(10, b) * vt * M1(a - 1)
            + a * vt * vt
            + pow(10, 2 * a) * B[n - 1]
            + 2 * pow(10, a) * vs * M1(b - 1)
            + b * vs * vs
        )
        B[n + 1] = B_next
        V[n + 1] = V[n] * pow(10, b) + V[n - 1]
        good = (B_next == orac[n + 1])
        ok_all = ok_all and good
        print(f"  {n+1:2d}  {('OK' if good else 'MISMATCH')}")
    print(f"\n  recursion holds n=2..13: {ok_all}")

    print("\n== (2) modular recursion, extended to n=40 ==")
    M = 101001001
    import math
    Bm = {1: 0, 2: 1, 3: 101}
    Vm = {1: 0, 2: 1, 3: 10}
    F = [fib(n) for n in range(1, 41)]
    okm = True
    for n in range(2, 39):
        a, b = F[n], F[n - 1]   # |q_n| = F_{n+1}?? NO: |q_n| = F_{n+1}, so a=F[n+1]... 
        # careful: |q_n| = F_{n+1} with F_1=1,F_2=1,F_3=2,F_4=3,F_5=5,...
        a, b = F[n + 1], F[n]
        vs, vt = Vm[n], Vm[n - 1]
        c1a = 1 + int((a - 1) * (3 - math.sqrt(5)) / 2)
        Ra = (pow(10, a - 1, M) - 1) * pow(9, -1, M) % M
        c1b = 1 + int((b - 1) * (3 - math.sqrt(5)) / 2)
        Rb = (pow(10, b - 1, M) - 1) * pow(9, -1, M) % M
        B_next = (
            pow(10, 2 * b, M) * Bm[n]
            + 2 * pow(10, b, M) * vt * (c1a % M) * Ra
            + (a % M) * vt * vt
            + pow(10, 2 * a, M) * Bm[n - 1]
            + 2 * pow(10, a, M) * vs * (c1b % M) * Rb
            + (b % M) * vs * vs
        ) % M
        Bm[n + 1] = B_next
        Vm[n + 1] = (Vm[n] * pow(10, b, M) + Vm[n - 1]) % M
        if n + 1 <= 14:
            good = (B_next == orac[n + 1] % M)
            okm = okm and good
            if not good:
                print(f"  n={n+1}: MISMATCH rec={B_next} oracle={orac[n+1] % M}")
    print(f"  modular recursion matches oracle n=2..14: {okm}")
    if okm:
        for n in range(14, 41):
            k = F[n + 1] - 1
            print(f"  n={n:2d}  k=F_{n+1}-1 = {k:9d}  Psi mod M = {Bm[n]}")


if __name__ == "__main__":
    main()
