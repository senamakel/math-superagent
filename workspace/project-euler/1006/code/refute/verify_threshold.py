"""Independent direct verification of the k=3 refutation.

Candidate (from G-stabilization first-step): n0(k) = smallest n with
|S_{n-1}| >= k.  For k=3, |S_2|=3 so n0(3)=3, word S_3="01001".

Check: does S_3 already contain all 4 length-3 Fibonacci subwords?
The full set of length-3 factors of f (limit word) is {001,010,100,101}.
We verify that S_3 misses '101', so n0=3 is too small a stabilization
threshold.  This reproduces the counterexample the TPTP engine found.
"""


def S(n):
    a, b = "0", "01"
    if n == 0:
        return a
    if n == 1:
        return b
    for _ in range(2, n + 1):
        a, b = b, b + a
    return b


def wl(n):
    a, b = 1, 2
    if n == 0:
        return a
    if n == 1:
        return b
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def subwords(word, k):
    return {word[i:i + k] for i in range(len(word) - k + 1)}


k = 3
# candidate n0: smallest n with |S_{n-1}| >= k
n0 = 1
while wl(n0 - 1) < k:
    n0 += 1
print(f"|S_0..S_4| = {[wl(i) for i in range(5)]}")
print(f"candidate n0({k}) = {n0}")

for n in range(2, 5):
    print(f"  S_{n} = {S(n)}  len-{k} subwords = {sorted(subwords(S(n), k))}")

full = sorted(subwords(S(6), k))  # full factor set of f for k=3
print(f"full length-{k} factor set of f = {full}  (size {len(full)})")
print(f"S_3 has size {len(subwords(S(3),k))} != {k+1}")
print("Refuted: candidate n0(3)=3 does NOT give the stabilized (full) factor set;")
print("'101' is a length-3 Fibonacci subword (it appears in S_4) but not in S_3.")
