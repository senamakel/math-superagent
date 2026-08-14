"""Analyze the state recurrence: does the state (Psi, vR, P1, N1, S) evolve
with a clean recurrence over Fibonacci-index steps?  Also verify the extension
recurrence and study the right-special factor R(k).

The extension recurrence: Psi(k+1) = 100(Psi(k) + vR^2) + 20 P1 + N1.
We look at this and at the 'R' (right-special) factor, P1 (sum of values with
w1 factor), to see if the state closes over one k increment and over blocks.
"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "out", "structure.json")

def main():
    structure = json.load(open(DATA))
    ks = sorted(int(k) for k in structure)
    fib = set()
    a, b = 1, 1
    while b <= max(ks):
        fib.add(b); a, b = b, a+b

    print("Fibonacci-indexed state:")
    print("k\tPsi\t\tN1\tP1\t\tR(string)\tRval\tS")
    for k in ks:
        if k in fib:
            d = structure[str(k)]
            print(f"{k}\t{d['Psi']}\t{d['N1']}\t{d['P1']}\t{d['R']}\t{int(d['R'])}\t{sum(d['values'])}")

if __name__ == "__main__":
    main()
