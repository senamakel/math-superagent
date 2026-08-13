from math import comb

def run():
    from itertools import product
    def signed_fwd_diff(seq, k, i):
        return sum(((-1)**(k-j)) * comb(k,j) * seq[i+j] for j in range(k+1))
    def absdiff_entry(seq, k, i):
        row = list(seq)
        for _ in range(k):
            row = [abs(row[j]-row[j+1]) for j in range(len(row)-1)]
        return row[i]

    print("Counterexample check: seq=[5,1,6]")
    print("  A_2(0) =", absdiff_entry([5,1,6],2,0), " |fwd| =", abs(signed_fwd_diff([5,1,6],2,0)))

    n_mism = 0
    first = []
    for L in range(2,6):
        for seq in product(range(6), repeat=L):
            for k in range(1, L):
                for i in range(L-k):
                    absval = absdiff_entry(seq,k,i)
                    fd = signed_fwd_diff(seq,k,i)
                    if absval != abs(fd):
                        n_mism += 1
                        if len(first) < 8:
                            first.append((list(seq),k,i,absval,abs(fd)))
    print("Total mismatches (L<=5, values 0..5):", n_mism)
    for f in first:
        print("  ", f)

run()
