"""Compute structural sequences for PE1006 pattern analysis.

Reads structure.json (k=1..60), which has per-k: factors (list), Psi, values,
N1, P1, R (right-special). Extract sequences:
  - Psi(k) exact
  - S(k) = sum of factor values (exact)
  - N1(k), P1(k) exact
  - v_R(k) exact (value of right-special factor)
  - R string itself
  - ones-counts sequence
And Fibonacci-indexed subsequences.
"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "out", "structure.json")

def main():
    structure = json.load(open(DATA))
    ks = sorted(int(k) for k in structure)
    # Psi exact
    print("== exact Psi(k), S(k)=sum values, N1, P1, vR ==")
    rows = []
    for k in ks:
        d = structure[str(k)]
        rows.append((k, d["Psi"], sum(d["values"]), d["N1"], d["P1"], d["R"]))
    for k, P, S, N1, P1, R in rows:
        print(f"{k}\t{P}\t{S}\t{N1}\t{P1}\t{R}")
    # Fibonacci indices
    fib = set()
    a, b = 1, 1
    while b <= max(ks):
        fib.add(b); a, b = b, a+b
    print("\n== Fibonacci-indexed Psi ==")
    for k, P, S, N1, P1, R in rows:
        if k in fib:
            print(k, P)

if __name__ == "__main__":
    main()
