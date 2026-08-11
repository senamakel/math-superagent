"""Verify Cabanillas Prop 9/10 (arXiv:1904.01874) on a small instance.

We want, for given irrational alpha in (0,1) and target beta in [0,1), the n<=N
minimizing ||n*alpha - beta||_Z.  Cabanillas enumerates the candidates as:
  best RIGHT (n alpha mod 1 >= beta): n=0, and
       n = sum_{i=1}^{2k-1} b_i q_{i-1} + j*q_{2k-1}, j in {0..b_{2k}-1}, k>=1
  best LEFT  (n alpha mod 1 <= beta): (termination n=sum b_i q_{i-1}), and
       n = sum_{i=1}^{2k}   b_i q_{i-1} + j*q_{2k},   j in {0..b_{2k+1}-1}, k>=0
where (b_i) is the alpha-numeration of beta and q are convergent denominators.
We check that brute-force argmin over n in [0,N] is attained among the candidates.
"""
import math

def cf(a, terms):
    out = []
    for _ in range(terms):
        ai = int(math.floor(a))
        out.append(ai)
        a = a - ai
        if a == 0:
            break
        a = 1.0 / a
    return out

def convergents(cflist):
    # p_k/q_k convergents; also return list of (p,q)
    p_prev2, q_prev2 = 0, 1   # (-1 index upto a0)
    p_prev1, q_prev1 = 1, 0
    out = []
    for a in cflist:
        p = a * p_prev1 + p_prev2
        q = a * q_prev1 + q_prev2
        p_prev2, q_prev2 = p_prev1, q_prev1
        p_prev1, q_prev1 = p, q
        out.append((p, q))
    return out

def delta_seq(q_list, alpha):
    # delta_{-1}=1, delta_0=alpha, delta_i = -a_i*delta_{i-1}+delta_{i-2}
    # but easier: delta_i = |q_i*alpha - p_i|  (decreasing)
    ds = []
    for (p, q) in q_list:
        ds.append(abs(q * alpha - p))
    return ds

def alpha_numeration(alpha, beta, a_list, q_list, terms):
    # delta_{-1}=1, delta_0=alpha
    d = [1.0, alpha]
    for i in range(2, terms + 1):
        ai = a_list[i - 1]
        d.append(-ai * d[i - 1] + d[i - 2])
    # d[i] = delta_{i-1}; delta_{-1}=d[0], delta_0=d[1],...
    b = []
    beta_k = beta
    for k in range(1, terms + 1):
        ak = a_list[k - 1]
        dk_1 = d[k - 1]   # delta_{k-1} = d[k-1]? delta_{-1}=d[0] => delta_{k-1}=d[k-1]
        bk = min(ak, math.ceil(beta_k / dk_1))
        b.append(bk)
        beta_k = bk * dk_1 - beta_k
    return b, d

def run_case(alpha, beta, N, terms=30):
    a_list = cf(alpha, terms)
    conv = convergents(a_list)
    q_list = [q for (p, q) in conv]
    b, d = alpha_numeration(alpha, beta, a_list, q_list, terms)

    cands = set()
    cands.add(0)
    # best right
    for k in range(1, terms // 2):
        pref = sum(b[i - 1] * q_list[i - 2] for i in range(1, 2 * k))  # sum_{i=1}^{2k-1} b_i q_{i-1}
        for j in range(0, b[2 * k - 1]):
            cands.add(pref + j * q_list[2 * k - 1])
    # best left
    for k in range(0, terms // 2):
        pref = sum(b[i - 1] * q_list[i - 2] for i in range(1, 2 * k + 1))  # sum_{i=1}^{2k} b_i q_{i-1}
        for j in range(0, b[2 * k]):
            cands.add(pref + j * q_list[2 * k])

    def dist(n):
        return abs((n * alpha - beta) - round(n * alpha - beta))

    # brute force argmin over 0..N
    bestn = min(range(0, N + 1), key=dist)
    bestd = dist(bestn)
    cand_best = min([n for n in cands if 0 <= n <= N], key=dist)
    ratio = None
    if bestd > 0:
        ratio = cand_best and dist(cand_best) / bestd or None
    # global minimum value among candidates vs brute minimum value
    cand_min_d = min(dist(n) for n in cands if 0 <= n <= N)
    ok = abs(cand_min_d - bestd) < 1e-12
    return bestn, cand_best, bestd, cand_min_d, ok, sorted(cands), b

if __name__ == "__main__":
    import math
    pi = math.pi
    beta = pi - math.floor(pi)
    # case: alpha = sqrt(2)-1
    alpha = math.sqrt(2) - 1
    N = 500
    bestn, cand_best, bestd, cand_min_d, ok, cands, b = run_case(alpha, beta, N)
    print("alpha={:.6f} beta={:.6f} N={}".format(alpha, beta, N))
    print("numeration digits (first 12):", b[:12])
    print("brute argmin n={}  dist={:.4g}".format(bestn, bestd))
    print("candidates-within-N min dist={:.4g}  match={}".format(cand_min_d, ok))
    print("#candidates total:", len(cands))

    # also test a couple more alphas
    for sq in (3, 5, 7, 11):
        alpha = math.sqrt(sq) - math.floor(math.sqrt(sq))
        ok = run_case(alpha, beta, 300)[5]
        print("alpha=srqt({})-floor min matches brute: {}".format(sq, ok))
