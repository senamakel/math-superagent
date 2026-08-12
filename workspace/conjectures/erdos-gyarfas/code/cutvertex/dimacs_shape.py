"""Dump the shape+C4 base CNF for a given n to a DIMACS file.

Usage: python dimacs_shape.py N outfile
"""
import sys
from cutvertex.encode_shape import build_base_shape
from pysat.formula import CNF


def to_dimacs(cnf):
    lines = [f"p cnf {cnf.nv} {len(cnf.clauses)}"]
    for cl in cnf.clauses:
        lines.append(" ".join(map(str, cl)) + " 0")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    n = int(sys.argv[1])
    out = sys.argv[2]
    cnf, top, atoms = build_base_shape(n)
    with open(out, "w") as f:
        f.write(to_dimacs(cnf))
    print(f"n={n} nv={cnf.nv} clauses={len(cnf.clauses)} -> {out}")
