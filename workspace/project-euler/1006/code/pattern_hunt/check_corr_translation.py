"""PE1006 pattern hunt: is the pair-correlation of the factor set
translation-invariant at general k?

For each k, let F_k = {k+1 distinct length-k factors}, and for positions
i, j in 1..k define C(i,j) = #{w in F_k : w_i = w_j = '1'}.
If C(i,j) depends only on d = j - i (translation invariance: C(i,j) ==
C(i+1,j+1) whenever both in range), then Psi(k) = sum_{d} A_k(d) * (geometric
in d), i.e. Psi reduces to a lag-sum at every k -- a big structural fact,
since directive 1 establishes it only at k = F_n - 1.

Directive 2 (mechanical word with slope F(n-1)/F(n), intercepts rho_m = -m*a)
predicts: digit at position j of word m = letter (j-m) of the infinite word,
so C(i,j) = # {m in 0..k : x_{j-m} = 1 and x_{i-m} = 1}, a sliding-window
count that in general DOES depend on j (window slides).  This program tests
the facts for k = 1..20 with exact factor enumeration.
"""


def fib_prefix(L):
    a, b = '0', '01'
    while len(b) < L:
        a, b = b, b + a
    return b


def factor_corr(k, word):
    n = len(word)
    facs = {word[i:i + k] for i in range(n - k + 1)}
    assert len(facs) == k + 1
    C = [[0] * (k + 1) for _ in range(k + 1)]  # 1-indexed
    for w in facs:
        for i in range(1, k + 1):
            if w[i - 1] != '1':
                continue
            for j in range(i, k + 1):
                if w[j - 1] == '1':
                    C[i][j] += 1
                    C[j][i] += 1
    return C


def main():
    KMAX = 20
    W = fib_prefix(3 * KMAX + 10)
    print(f"prefix len = {len(W)}")
    for k in range(1, KMAX + 1):
        C = factor_corr(k, W)
        bad = []
        for i in range(1, k):
            for j in range(i + 1, k + 1):
                if i + 1 <= k and j + 1 <= k:
                    if C[i][j] != C[i + 1][j + 1]:
                        bad.append(((i, j), C[i][j], C[i + 1][j + 1]))
        # diagonal C(i,i)
        diag = [C[i][i] for i in range(1, k + 1)]
        print(f"k={k:2d}  translation violations: {len(bad)}  "
              f"diag C(i,i) distinct: {len(set(diag))}  diag: {diag}")
        if bad[:3]:
            print("     first violations:", bad[:3])


if __name__ == '__main__':
    main()