"""Check the Lind 1968 index alignment against the verified family members.

The run's verified family (code/family_seq/family_sequences.py):
    C(n+1, k+1) = C(n, k+2),  n_i = F_{2i+2}F_{2i+3}-1, k_i = F_{2i}F_{2i+3}-1,
    i=1 => C(15,5) = C(14,6) = 3003.

Question: which (s)-indexed Lind formula reproduces n=15, k=5 (or the
C(n,2) = C(k+1,k-1) form)?  The OCR of the 1968 scan shows n = F_{2s}F_{2s+3},
k = F_{2s-2}F_{2s+1}, but this must be checked because OCR of scanned math is
unreliable.
"""
import math

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# candidates for n = F_{2s}F_{2s+3}  (OCR) vs F_{2s}F_{2s+1} (guess)
print("s | F_{2s}F_{2s+3} | F_{2s}F_{2s+1} | k=F_{2s-2}F_{2s+1} | C(n,2) | C(k+1,k-1) | C(k+1,2)")
for s in range(1, 6):
    n1 = fib(2*s) * fib(2*s + 3)          # OCR reading
    n2 = fib(2*s) * fib(2*s + 1)          # alt guess
    k = fib(2*s - 2) * fib(2*s + 1)       # OCR reading
    if n1 >= 2: a1 = math.comb(n1, 2); b1 = math.comb(k + 1, k - 1)
    else: a1 = b1 = -1
    if n2 >= 2: a2 = math.comb(n2, 2); b2 = math.comb(k + 1, 2)
    else: a2 = b2 = -1
    print("%d | %14d | %13d | %17d | %10d | %12d | %10d"
          % (s, n1, n2, k, a1, b1, b2))

print()
print("Verified family members (both-mirror, from witnesses.json/family_sequences.py):")
print("  i=1: C(15,5) = C(14,6) = 3003")
print("  i=2: C(104,39) = C(103,40) = 61218182743304701891431482520")
print("Check whether any Lind candidate equals these: C(15,2)=105, C(14,2)=91, ...")
print("=> The OCR indices F_{2s}F_{2s+3}/F_{2s-2}F_{2s+1} do NOT reproduce 15/5 or 3003;")
print("   the reliable transferable content is the Pell/unit-group derivation, not the")
print("   index alignment, which must come from the run's verified modern form.")