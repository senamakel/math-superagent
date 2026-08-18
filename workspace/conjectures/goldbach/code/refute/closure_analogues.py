from sympy import primerange


def run(bound=200):
    # Goldbach predicate: representable as p+q with p,q prime.
    ps = set(primerange(2, bound + 1))
    g = {n for n in range(4, bound + 1, 2)
         if not any(n - p in ps for p in ps if p <= n // 2)}
    print('Goldbach failures up to', bound, ':', sorted(g))
    print('empty-case closure test:', 'vacuous (no exception)' if not g else 'non-vacuous')

    # Analogue 1: "n is a square". Least failure 1? Actually 0 and 1 are squares.
    sq = {n for n in range(bound + 1) if int(n**0.5)**2 == n}
    sq_fail = set(range(bound + 1)) - sq
    print('square predicate least failure:', min(sq_fail),
          'failure density:', len(sq_fail) / bound)

    # Analogue 2: "n is prime". Least failure 1.
    prime_set = set(primerange(2, bound + 1))
    prime_fail = set(range(1, bound + 1)) - prime_set
    print('prime predicate least failure:', min(prime_fail),
          'failure density:', len(prime_fail) / bound)

    # Analogue 3: semiprime predicate, least failure 4.
    semiprime = set()
    for n in range(4, bound + 1):
        fac, x = [], n
        for p in primerange(2, int(x**0.5) + 1):
            while x % p == 0:
                fac.append(p); x //= p
        if x > 1:
            fac.append(x)
        if len(fac) == 2:
            semiprime.add(n)
    semi_fail = set(range(4, bound + 1)) - semiprime
    print('semiprime least failure:', min(semi_fail),
          'failure density:', len(semi_fail) / (bound - 3))

if __name__ == '__main__':
    run()
