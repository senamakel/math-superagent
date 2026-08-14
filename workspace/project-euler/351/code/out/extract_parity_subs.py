"""Extract subsequences never examined by prior passes: even-indexed and
odd-indexed terms of A063985 and H (from the stored exact prefix), plus a
check of the mod-2 residue law on each half. Exact integer arithmetic.

Subsequence extraction: A_e(k) = A063985(2k), A_o(k) = A063985(2k+1),
H_e(k) = H(2k), H_o(k) = H(2k+1) for k >= 0, printed as JSON for the
sequence tools (no transcription).
"""
import json

N = 200_000
with open("code/out/seq_A063985.txt") as f:
    A = [int(t) for t in f.read().split()]
with open("code/out/seq_H.txt") as f:
    H = [int(t) for t in f.read().split()]
assert len(A) == N and len(H) == N

# A063985(n) is 1-indexed on disk (file line i holds A(i), i = 1..N).
A_e = [A[2 * k - 1] for k in range(1, N // 2 + 1)]          # A(2k)
A_o = [A[2 * k] for k in range(0, N // 2)]                  # A(2k+1), k=0..N/2-1
H_e = [H[2 * k - 1] for k in range(1, N // 2 + 1)]
H_o = [H[2 * k] for k in range(0, N // 2)]

print("A_e = A(2k), k=1..%d" % len(A_e))
print(json.dumps(A_e[:80]))
print("A_o = A(2k+1), k=0..%d" % len(A_o))
print(json.dumps(A_o[:80]))
print("H_e = H(2k), k=1..%d" % len(H_e))
print(json.dumps(H_e[:80]))
print("H_o = H(2k+1), k=0..%d" % len(H_o))
print(json.dumps(H_o[:80]))

# Parity of the halves under the mod-2 law: A odd iff n mod 4 in {1,2}.
def par(A, n_from, n_to):
    ok, first_bad = True, None
    for n in range(n_from, n_to + 1):
        expect = 1 if n % 4 in (1, 2) else 0
        if A[n - 1] % 2 != expect:
            ok, first_bad = False, n
            break
    return ok, first_bad

print("A parity law on evens n=2..%d:" % N, par(A, 2, N))
print("A parity law on odds n=3..%d:" % N, par(A, 3, N))
