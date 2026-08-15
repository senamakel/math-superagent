import sys
sys.path.insert(0, "/workspace/code")
from lib.qcube import internal_degree_distribution, max_internal_degree

S4 = [0, 1, 2, 5, 6, 11, 12, 13, 14]
print("n=4 witness profile:", internal_degree_distribution(4, S4))
print("n=4 witness max degree:", max_internal_degree(4, S4))

# parity classes of Q_4
even = [v for v in range(16) if bin(v).count("1") % 2 == 0]
odd = [v for v in range(16) if bin(v).count("1") % 2 == 1]
def parity_plus_one(S):
    S = set(S)
    if len(S) != 9:
        return False
    for v in range(16):
        if S == set(even) | {v}:
            return True
        if S == set(odd) | {v}:
            return True
    return False
print("even parity class:", even, "size", len(even))
print("odd parity class:", odd, "size", len(odd))
print("witness is parity+one?", parity_plus_one(S4))
