import sys, itertools
sys.path.insert(0, '/workspace/code')
from dyadic_oddfactor_inf_new2 import build_seq, scan_nu2_cyc
from lib.rightdiag import incremental_diagonals, cycle_and_nu2


def true_nu2(word, n):
    q = build_seq(word, n + 1)
    for k, dd in enumerate(incremental_diagonals(q)):
        if k == n:
            break
    tau, nu2 = cycle_and_nu2(dd)
    return nu2


def minimal_period(word):
    L = len(word)
    for d in range(1, L + 1):
        if L % d == 0 and all(word[j] == word[j % d] for j in range(L)):
            return d
    return L


print("TRUE nu2 (canonical cycle_and_nu2) at large n over ALL words of small odd periods")
print("Worst (smallest-large-n) words, and whether any odd-period word has bounded nu2.\n")
for P in (3, 5, 7):
    worst = []
    n_bounded = 0
    for bits in itertools.product([0, 1], repeat=P):
        w = list(bits)
        if minimal_period(w) != P:
            continue          # only primitive/odd-minimal-period words
        a = true_nu2(w, 2000)
        b = true_nu2(w, 12000)
        worst.append((b, a, w))
        if b < 15:
            n_bounded += 1
    worst.sort()
    print("P=%d: %d primitive odd-period words; # with true nu2(12000)<15 = %d"
          % (P, len(worst), n_bounded))
    print("   smallest true-nu2(12000) words (nu2@12000, nu2@2000, word):")
    for b, a, w in worst[:5]:
        print("     %6d %6d %s" % (b, a, ''.join(map(str, w))))
    print()
