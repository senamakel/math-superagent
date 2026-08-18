# Brute-force oracle for PE1006
# complexity_class: exponential (factor-set enumeration); oracle_bound: small k only.
def fib_word_at_least(length):
    a, b = "0", "01"
    while len(b) < length:
        a, b = b, b + a
    return b

def factors(k):
    w = fib_word_at_least(3*k + 5)
    return {w[i:i+k] for i in range(len(w)-k+1)}

def psi(k):
    return sum(int(s)**2 for s in factors(k))

if __name__ == "__main__":
    assert factors(3) == {"001", "010", "100", "101"}
    assert psi(3) == 20302
    M = 101001001
    assert psi(10) % M == 10699667
    for k in range(1, 21):
        assert len(factors(k)) == k+1
    print("Psi(3)=", psi(3))
    print("Psi(10) mod 101001001=", psi(10) % M)
    print("factor counts k=1..20: OK")
