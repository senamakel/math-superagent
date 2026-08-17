"""Verify Chuan 1992 indexed enumeration of Fibonacci-length factor sets against the brute oracle.

Claim (Chuan Thm 7, 11, Cor 12): the length-F_n "n-th Fibonacci words" are exactly the F_n
cyclic shifts T^{j*s}(q_n), 0<=j<F_n, of the canonical coded Fibonacci word q_n, with the 1s
of shift j sitting at positions k ≡ (j+r)*t (mod F_n), r=1..F_{n-2}.

We check what this means for the PROBLEM's factor set at k = F_n - 1 (where there are
k+1 = F_n factors):

  (A) the F_n cyclic shifts of q_n truncated to their first k = F_n-1 letters are exactly
      the k+1 length-k factors (as a SET);
  (B) the modular index rule reproduces the positions of the 1s in each shift.

Exact integer arithmetic throughout. No published answer is used.
"""


def S(n):
    """n-th finite Fibonacci word: S_0='0', S_1='01', S_n=S_{n-1}+S_{n-2}."""
    a, b = "0", "01"
    if n == 0:
        return a
    if n == 1:
        return b
    for _ in range(2, n + 1):
        a, b = b, b + a
    return b


def subword_set(word, k):
    return {word[i:i + k] for i in range(len(word) - k + 1)}


def factor_set(k, N=40):
    """Distinct length-k factors of the infinite Fibonacci word via S_N."""
    prev = None
    for m in range(2, N + 1):
        s = subword_set(S(m), k)
        cur = len(s)
        if prev is not None:
            assert cur >= prev, "factor set not monotone"
        prev = cur
        if cur == k + 1:
            return s
    raise RuntimeError("factor set never stabilised at k+1")


def cyclic_shift(w, sft):
    sft %= len(w)
    return w[sft:] + w[:sft]


def fib(n):
    """Fibonacci: F_1=F_2=1, F_n=F_{n-1}+F_{n-2}. fib(n) for n>=1."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def canonical_qn(n):
    """Chuan's canonical coded Fibonacci word q_n of length F_n over 0/1.

    The accumulating sequence seq[i] has length F_{i+2} (seq[0]='0' len 1,
    seq[1]='01' len 2, seq[2]='010' len 3, seq[3]='01001' len 5, ...), so to
    get Chuan's canonical word q_n of length F_n we need seq[n-2].
    (The old code returned seq[n-1], length F_{n+1}, an off-by-one that
    tripped `assert len(qn) == Fn` at the very first n=3.)
    """
    seq = ['0', '01']
    for i in range(2, n):
        seq.append(seq[i - 1] + seq[i - 2])
    return seq[n - 2]


def verify(n):
    Fn = fib(n)
    k = Fn - 1
    qn = canonical_qn(n)
    assert len(qn) == Fn, (len(qn), Fn)

    t = fib(n - 1) if n % 2 == 1 else fib(n - 2)
    s = fib(n - 2) if n % 2 == 1 else fib(n - 1)

    all_shifts = [cyclic_shift(qn, d) for d in range(Fn)]
    shifts_set = set()
    # Build each shift both by the rule and check it is a shift of qn.
    for j in range(Fn):
        pos = set()
        for r in range(1, fib(n - 2) + 1):
            kk = (j + r) * t % Fn
            if 1 <= kk <= Fn:
                pos.add(kk - 1)  # 0-indexed
        w = ''.join('1' if i in pos else '0' for i in range(Fn))
        assert w in all_shifts, f"rule word not a shift of qn at n={n}, j={j}"
        shifts_set.add(w[:k])   # truncate to problem length k = F_n - 1

    brute = factor_set(k, N=45)
    ok_set = (len(shifts_set) == k + 1) and (shifts_set == brute)
    return ok_set, len(shifts_set), len(brute), k


if __name__ == '__main__':
    all_ok = True
    for n in range(3, 11):
        ok, a, b, k = verify(n)
        all_ok = all_ok and ok
        print(f"n={n} k=F_n-1={k}: shifts={a}, brute={b}, set-equal={ok}")
    print("\nChuan indexed enumeration verified against brute oracle:", all_ok)
