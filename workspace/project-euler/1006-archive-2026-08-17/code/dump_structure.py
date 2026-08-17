"""Exact brute-force structural dump of the Fibonacci-factor combinatorics, k=1..60.

For each k we build S_N with N chosen so that |S_N| >= 3(k+1) (so both the
length-k and length-(k+1) factor sets are fully populated), collect the
distinct length-k contiguous substrings (k+1 of them) and the distinct
length-(k+1) substrings, and record:

  factors     : the k+1 factors in sorted() order, as binary strings
  values      : int(w) for each factor (leading zeros ignored)
  extensions  : per-factor extension letter: '0' (only w0 is a factor),
                '1' (only w1 is a factor), 'S' (both  -> right-special)
  Psi         : sum of v^2 (full integer)
  Psi_mod     : Psi mod 101001001
  A           : sum of v
  N1          : number of length-k factors w with w+'1' also a factor
  P1          : sum of v over those w with w+'1' a factor
  R           : int value of the unique right-special factor of length k
                (asserted to be exactly one per k)
  C           : C(j,l;k) = number of the k+1 factors with a '1' at both
                positions j and l, for 0 <= j <= l < k, keyed "j,l"

Method identical to code/brute.py and code/dump_factors.py: build S_N and
collect set substrings. All arithmetic exact integers.

Saves everything to code/out/structure.json.
"""

import json
import os


def S(n):
    """Return the n-th Fibonacci word as a str (S_0="0", S_1="01")."""
    a, b = "0", "01"
    if n == 0:
        return a
    if n == 1:
        return b
    for _ in range(2, n + 1):
        a, b = b, b + a
    return b


def word_len(n):
    """|S_n| = Fib(n+2) with Fib(1)=Fib(2)=1."""
    a, b = 1, 1  # Fib(1), Fib(2)
    if n == 0:
        return a
    if n == 1:
        return 2
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def minimal_N(min_len):
    """Smallest N with |S_N| >= min_len."""
    N = 0
    while word_len(N) < min_len:
        N += 1
    return N


def subword_set(word, k):
    return {word[i:i + k] for i in range(len(word) - k + 1)}


MOD = 101001001


def main():
    out_dir = os.path.join(os.path.dirname(__file__), "out")
    os.makedirs(out_dir, exist_ok=True)

    structure = {}

    print("k : N : count : Psi : Psi_mod : A : N1 : P1 : R")
    for k in range(1, 61):
        # |S_N| >= 3(k+1) so both factor(k) and factor(k+1) sets are complete.
        N = minimal_N(3 * (k + 1))
        word = S(N)

        subk = subword_set(word, k)
        assert len(subk) == k + 1, f"k={k}: count {len(subk)} != k+1 in S_{N}"
        factors = sorted(subk)
        values = [int(w) for w in factors]

        # Extension structure via length-(k+1) factors.
        subk1 = subword_set(word, k + 1)
        assert len(subk1) == k + 2, f"k={k}: k+1-count {len(subk1)} != k+2 in S_{N}"

        Psi = sum(v * v for v in values)
        A = sum(values)

        # Right-special: exactly one factor extends both ways.
        right_special = [w for w in factors if (w + '0') in subk1 and (w + '1') in subk1]
        assert len(right_special) == 1, f"k={k}: {len(right_special)} right-special factors (expect 1)"
        R = int(right_special[0])

        N1 = 0
        P1 = 0
        extensions = []
        for i, w in enumerate(factors):
            ext0 = (w + '0') in subk1
            ext1 = (w + '1') in subk1
            if ext0 and ext1:
                extensions.append('S')
            elif ext1:
                extensions.append('1')
            elif ext0:
                extensions.append('0')
            else:
                raise AssertionError(f"k={k}: factor {w} has no extension")
            if ext1:
                N1 += 1
                P1 += values[i]

        # C matrix: number of factors with '1' at both positions j and l.
        C = {}
        for j in range(k):
            for l in range(j, k):
                cnt = sum(1 for w in factors if w[j] == '1' and w[l] == '1')
                C[f"{j},{l}"] = cnt

        structure[str(k)] = {
            "N": N,
            "factors": factors,
            "values": values,
            "extensions": extensions,
            "Psi": Psi,
            "Psi_mod": Psi % MOD,
            "A": A,
            "N1": N1,
            "P1": P1,
            "R": R,
            "C": C,
        }

        if k <= 25:
            print(f"{k:2d} : {N:2d} : {len(factors):3d} : {Psi} : {Psi % MOD} : {A} : {N1:2d} : {P1} : {R}")

    # Detailed k=1..20 listing.
    print()
    print("Detailed factor lists with extension letters, k=1..20:")
    for k in range(1, 21):
        d = structure[str(k)]
        print(f"k={k}:")
        for w, v, e in zip(d["factors"], d["values"], d["extensions"]):
            print(f"   {w!r:10s} v={v}  ext='{e}'")
        print(f"   N1={d['N1']} P1={d['P1']} R={d['R']}")

    # Confirm unique right-special factor for all k<=60.
    ok = all(len([w for w in structure[str(k)]['factors']
                  if (w + '0') in subword_set(S(structure[str(k)]['N']), k + 1)
                  and (w + '1') in subword_set(S(structure[str(k)]['N']), k + 1)]) == 1
              for k in range(1, 61))
    print()
    print("Unique right-special factor held for every k=1..60:", ok)

    out_path = os.path.join(out_dir, "structure.json")
    with open(out_path, "w") as fh:
        json.dump(structure, fh, indent=1)
    print("Saved structure to", out_path)

    # Sanity checks against the two worked examples.
    print()
    print("Check: Psi(3) =", structure["3"]["Psi"], "(expect 20302)")
    print("Check: Psi(10) mod 101001001 =", structure["10"]["Psi_mod"], "(expect 10699667)")


if __name__ == "__main__":
    main()
