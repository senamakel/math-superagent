"""Exact pattern checks on sequences already computed by this run.

This is not a Collatz proof. It parses the captured CF and shape-scan outputs,
then checks exact recurrences/identities and deliberately tests the first
natural extrapolation beyond the shape-scan range.
"""
from pathlib import Path
import ast, re, math


def parse_cf():
    text = Path("code/out/cf_log23_terms.txt").read_text()
    get = lambda label: ast.literal_eval(re.search(label + r"\n(\[.*?\])", text, re.S).group(1))
    return get(r"terms a_0\.\.a_99:"), get(r"convergent denominators q_0\.\.q_99:"), get(r"convergent numerators p_0\.\.p_99:")


def parse_hits():
    text = Path("code/out/shape_scan.txt").read_text()
    return ast.literal_eval(re.search(r"integer hits: (\[.*\])", text).group(1))


def main():
    a, q, p = parse_cf()
    print("CF lengths:", len(a), len(p), len(q))
    # Exact standard continued-fraction identities.
    print("gcd(q_n,q_{n-1})=1 for all supplied n:", all(math.gcd(q[i], q[i-1]) == 1 for i in range(1, len(q))))
    print("p_n q_{n-1}-p_{n-1}q_n is ±1 for all supplied n:", all(abs(p[i]*q[i-1]-p[i-1]*q[i]) == 1 for i in range(1, len(q))))
    print("q_n strictly increases for n>=2:", all(q[i] > q[i-1] for i in range(2, len(q))))
    hits = parse_hits()
    positive = [h for h in hits if h[3] > 0]
    print("shape-scan hits:", len(hits), "positive:", positive)
    print("positive hit values all equal 1:", all(h[3] == 1 for h in positive))
    # Candidate pattern: positive hits with equal gaps 2 continue for all k.
    # This is tested beyond the original scan by exact formula, not enumerated shapes.
    def value_equal_two(k):
        L, m = 2*k, k
        S = sum(3**(m-1-j) * 2**(2*j) for j in range(m))
        return S // (2**L - 3**m), S % (2**L - 3**m)
    print("equal-gap-2 direct tests k=1..20:")
    print([(k,)+value_equal_two(k) for k in range(1,21)])
    print("equal-gap-2 gives x=1 exactly through k=20:", all(value_equal_two(k) == (1,0) for k in range(1,21)))

if __name__ == '__main__':
    main()
