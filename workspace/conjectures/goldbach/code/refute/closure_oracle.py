from sympy import primerange


def goldbach_failures(bound):
    ps = set(primerange(2, bound + 1))
    return [n for n in range(4, bound + 1, 2)
            if not any(n-p in ps for p in ps if p <= n//2)]


def check_closure_assertions(bound=200):
    failures = goldbach_failures(bound)
    print('Goldbach failures up to', bound, ':', failures)
    if not failures:
        print('empty-case closure test: vacuous (no exception)')
        return
    m = min(failures)
    print('minimal failure:', m)
    # translation closure
    for k in range(1, (bound - m)//2 + 1):
        if m + 2*k not in failures:
            print('  translation closure FAILS: m+', 2*k, '=', m + 2*k, 'is representable')
            break
    else:
        print('  translation closure holds up to', bound)
    # multiplication closure
    for p in primerange(3, bound//m + 1):
        if m*p not in failures:
            print('  multiplication closure FAILS: m*', p, '=', m*p, 'is representable')
            break
    else:
        print('  multiplication closure holds up to', bound)
    # density
    print('  failure density among evens up to', bound, ':',
          len(failures), '/', bound//2, '=', len(failures)/(bound//2))

if __name__ == '__main__':
    check_closure_assertions(200)
