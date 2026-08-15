"""Explore the descent x^2 - y^q = 1 for odd prime q, exact arithmetic.

Reproduces the structure computationally: for every (x, y, q) with
x^2 - y^q = 1, x odd, x^2 <= N, factor y^q = (x-1)(x+1), compute the descent
object and print the equation it must satisfy.  This is NOT a search of the
answer space at full size -- it is a small bound used to check the descent
shapes that the proof relies on.
"""
import sys
sys.path.insert(0, "/workspace/code")

from lib.perfectpow import iroot, is_perfect_power_k, is_square, is_prime


def v2(n):
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def odd_part(n):
    while n % 2 == 0:
        n //= 2
    return n


def analyze(q, N):
    """For all odd x with x^2 <= N and y^q = x^2 - 1 a perfect q-th power,
    print the descent structure: u=(x-1)/2, v=(x+1)/2, v-u=1, uv=y^q/4,
    and the 2-adic split of {u,v}."""
    print(f"=== q = {q} ===")
    max_x = int(N ** 0.5) + 1
    results = []
    for x in range(2, max_x + 1):
        if x % 2 == 0:
            continue
        m = x * x - 1
        y = iroot(m, q)
        if y ** q == m and y > 0:
            results.append((x, y))
    print(f"solutions with x odd, x^2<={N}, y^q=x^2-1: {results}")
    for (x, y) in results:
        u, v = (x - 1) // 2, (x + 1) // 2
        assert v - u == 1
        uv = u * v
        assert 4 * uv == x * x - 1 == y ** q
        # 2-adic structure
        ty = v2(y)
        need = q * ty - 2  # v_2(uv)
        # exactly one of u,v even
        if v2(u) >= v2(v):
            even, odd = u, v
        else:
            even, odd = v, u
        eu = even // (2 ** v2(even))   # odd part of even factor
        print(f"  x={x} y={y} v2(y)={ty}: u={u}, v={v}, "
              f"v2(uv)={v2(uv)}, need {need}; even factor {even} = 2^{v2(even)} * {eu}, "
              f"odd factor={odd}")
        # is the odd factor a q-th power? is the odd part of even a q-th power?
        print(f"     odd-factor is q-th power: {is_perfect_power_k(odd, q)}, "
              f"odd-part-of-even is q-th power: {is_perfect_power_k(eu, q)}")


if __name__ == "__main__":
    for q in (3, 5, 7, 11, 13):
        analyze(q, 10 ** 12)
