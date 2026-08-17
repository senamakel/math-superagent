"""PE1006 pattern hunt: check the right-extension recurrence structure of the
factor sets F_k, and extract the new sequences it involves.

Facts being verified (exact, against the brute factor sets):
  * exactly one length-k factor R_k is right-special (has both '0' and '1'
    as right extensions); every other factor has exactly one right extension;
  * the set identity F_{k+1} = { w.b : w in F_k, b in ext(w) } holds (this is
    trivial from factor-closedness, checked anyway);
  * recurrence for the value sum T(k) = sum V(w) and the square sum
    Psi(k) = sum V(w)^2:
        J(k)   = # of pairs (w,b) with b = '1' a right extension of w
        S1(k)  = sum of V(w) over pairs (w,b='1')
        T(k+1) = 10*T(k) + 10*V(R_k) + J(k)
        Psi(k+1) = 100*Psi(k) + 100*V(R_k)^2 + 20*S1(k) + J(k)
    (derived from  V(w1)=10V(w)+1, V(w0)=10V(w), R counted twice).

Writes code/out/ext_recurrence.txt with rows
    k  V(R_k)  J(k)  P1(k+1)  S1(k)
where P1(k+1) = number of length-(k+1) factors ending in '1' = J(k).
"""
from brute import fib_word


def distinct_factors(word, k):
    return {word[i:i + k] for i in range(len(word) - k + 1)}


def val(w):
    return int(w, 10) if w else 0


def main():
    k_max = 40
    W = fib_word(4 * k_max + 10)          # comfortably past Lmin(k_max)
    F = {}
    for k in range(1, k_max + 2):
        F[k] = distinct_factors(W, k)

    rows = []
    for k in range(1, k_max + 1):
        Fk = F[k]
        # right extensions of each w: letters b with w+b in F[k+1]
        ext = {}
        for w in Fk:
            e = [b for b in '01' if w + b in F[k + 1]]
            ext[w] = ''.join(sorted(e))
            assert len(e) in (1, 2)
        special = [w for w in Fk if len(ext[w]) == 2]
        assert len(special) == 1, (k, special)
        R = special[0]

        J = sum(1 for w in Fk for b in ext[w] if b == '1')
        S1 = sum(val(w) for w in Fk for b in ext[w] if b == '1')
        P1_next = sum(1 for w in F[k + 1] if w[-1] == '1')

        # set identity F_{k+1} = { w.b : ... }
        built = {w + b for w in Fk for b in ext[w]}
        assert built == F[k + 1], (k, built ^ F[k + 1])

        # value-sum recurrence (needs T(k) computed loop-wise)
        if k == 1:
            Tk = sum(val(w) for w in Fk)
            Pk = sum(val(w) ** 2 for w in Fk)
        else:
            pass  # Tk, Pk carried from previous iteration
        Tk1 = 10 * Tk + 10 * val(R) + J
        Pk1 = 100 * Pk + 100 * val(R) ** 2 + 20 * S1 + J
        Tbrute = sum(val(w) for w in F[k + 1])
        Pbrute = sum(val(w) ** 2 for w in F[k + 1])
        assert Tk1 == Tbrute, (k, Tk1, Tbrute)
        assert Pk1 == Pbrute, (k, Pk1, Pbrute)
        assert J == P1_next, (k, J, P1_next, R)
        rows.append((k, val(R), J, P1_next, S1))
        Tk, Pk = Tk1, Pk1

    with open('code/out/ext_recurrence.txt', 'w') as fh:
        for k, vR, J, P1, S1 in rows:
            fh.write(f"{k} {vR} {J} {P1} {S1}\n")

    print("right-extension recurrence verified exactly for k = 1..%d:" % k_max)
    print("  (i)  every F_k has exactly one right-special factor R_k")
    print("  (ii) F_{k+1} = { w.b : w in F_k, b in ext(w) }")
    print("  (iii) T(k+1) = 10*T(k) + 10*V(R_k) + J(k)  (value sums)")
    print("  (iv) Psi(k+1) = 100*Psi(k) + 100*V(R_k)^2 + 20*S1(k) + J(k)")
    print("  (v)  J(k) == # length-(k+1) factors ending in '1'")
    print()
    print("first 20 rows: k  V(R_k)  J(k)  P1(k+1)  S1(k)")
    for row in rows[:20]:
        print("   ", row)
    print("... wrote code/out/ext_recurrence.txt")


if __name__ == '__main__':
    main()