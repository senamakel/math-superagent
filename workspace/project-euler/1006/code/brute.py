from pathlib import Path

MOD = 101001001

def fib_word(n):
    a, b = "0", "01"
    if n == 0:
        return a
    if n == 1:
        return b
    for _ in range(2, n + 1):
        a, b = b, b + a
    return b

def factors(k):
    seen = set()
    previous = None
    n = 0
    while True:
        w = fib_word(n)
        seen.update(w[i:i+k] for i in range(max(0, len(w)-k+1)))
        if seen == previous and len(w) >= 2*k:
            return seen
        previous = set(seen)
        n += 1

def psi(k, modulus=None):
    value = sum(int(x)**2 for x in factors(k))
    return value if modulus is None else value % modulus

if __name__ == "__main__":
    f3 = factors(3)
    assert f3 == {"001", "010", "100", "101"}
    assert psi(3) == 20302
    assert psi(10, MOD) == 10699667
    print("F3 =", sorted(f3))
    print("Psi(3) =", psi(3))
    print("Psi(10) mod M =", psi(10, MOD))
