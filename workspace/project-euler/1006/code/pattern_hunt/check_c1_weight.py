"""Verify the two candidate structural handles exactly, independently:

(1) c1(k) = number of distinct length-k factors starting with '1'
        = 1 + floor(k/phi^2)
    vs brute count, k=1..100.

(2) weight distribution: the k+1 factors have exactly two weights
    {floor(k/phi^2), ceil(k/phi^2)}.

(3) c0(k) = (k+1) - c1(k): check it equals (the decorrelated Sturmian count)
    i.e. number of factors starting with '0'.
"""
from decimal import Decimal, getcontext
getcontext().prec = 60

def fib_word(min_len):
    a, b = '0', '01'
    while len(b) < min_len:
        a, b = b, b + a
    return b

def phi2():
    return (Decimal(3) + Decimal(5).sqrt()) / Decimal(2)

def fl(x):
    # exact floor of a positive Decimal
    return int(x.to_integral_value(rounding='ROUND_FLOOR'))

def main():
    kmax = 100
    word = fib_word(4 * kmax + 8)
    L = len(word)
    P = phi2()
    p2 = Decimal(1) / P   # 1/phi^2
    bad_c1 = []
    bad_w = []
    for k in range(1, kmax + 1):
        factors = set(word[i:i+k] for i in range(L - k + 1))
        assert len(factors) == k + 1
        c1 = sum(1 for w in factors if w[0] == '1')
        # floor(k/phi^2): compute via Decimal
        v = Decimal(k) * p2
        flv = fl(v)
        # robust floor: if v is within 1e-40 of an integer it could be exact/atm
        expect = 1 + flv
        if c1 != expect:
            bad_c1.append((k, c1, expect))
        # weight distribution
        weights = {}
        for w in factors:
            weights[sum(1 for ch in w if ch == '1')] = weights.get(sum(1 for ch in w if ch == '1'), 0) + 1
        ws = sorted(weights.keys())
        lo = fl(Decimal(k) * p2)
        hi = -(-int(Decimal(k) * p2) // 1)  # ceiling(decimal)
        # ceiling of k/phi^2
        cv = Decimal(k) * p2
        ce = int(cv) if cv == int(cv) else int(cv) + 1
        if set(ws) != {lo, ce}:
            bad_w.append((k, ws, (lo, ce)))
    print(f"c1(k)=1+floor(k/phi^2), k=1..{kmax}: {'HOLDS' if not bad_c1 else 'FAIL ' + str(bad_c1[:3])}")
    print(f"weight dist = {{floor,ceil(k/phi^2)}}, k=1..{kmax}: {'HOLDS' if not bad_w else 'FAIL ' + str(bad_w[:3])}")
    # c0 check: number starting with 0 = (k+1)-c1
    bad_c0 = []
    for k in range(1, kmax + 1):
        factors = set(word[i:i+k] for i in range(L - k + 1))
        c1 = sum(1 for w in factors if w[0] == '1')
        c0 = sum(1 for w in factors if w[0] == '0')
        if c0 != (k + 1) - c1:
            bad_c0.append(k)
    print(f"c0=(k+1)-c1 (complement identity): {'HOLDS' if not bad_c0 else 'FAIL'}")

if __name__ == "__main__":
    main()
