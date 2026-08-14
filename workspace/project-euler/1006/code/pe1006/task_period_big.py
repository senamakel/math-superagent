"""Compute P(k)=Psi(k) mod M for k=1..KMAX cheaply and test periodicity.

The length-k factor set of the infinite Fibonacci word f is just the set of
distinct length-k substrings of a prefix of f. We compute P(k) mod M for a
large range and search for the smallest period T (testing that
seq[i]==seq[i+T] for all i in range), which if found lets us reach k=10^18.
"""
import sys
KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
MOD = 101001001

# build f to length 3*KMAX+50
a, b = "0", "01"
while len(b) < 3 * KMAX + 50:
    a, b = b, b + a
f = b

seq = []
for k in range(1, KMAX + 1):
    win = {f[i:i+k] for i in range(len(f) - k + 1)}
    assert len(win) == k + 1, (k, len(win), len(f))
    P = sum(int(w) ** 2 for w in win) % MOD
    seq.append(P)

print(f"computed P mod {MOD} for k=1..{KMAX}")

# periodicity search: smallest T with seq[i]==seq[i+T] for all i in range
# over the full window (require at least one full period + margin)
N = len(seq)
found = None
# test T up to N//2
for T in range(1, N // 2 + 1):
    if all(seq[i] == seq[i + T] for i in range(N - T)):
        found = T
        break
print("smallest pure period T (over full available data):", found)

# Also scan for a period holding over a window (last half), allowing the
# possibility of a longer period that needs more data.
print("\nfirst 60 residues:", seq[:60])
