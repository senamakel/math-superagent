from math import comb
from itertools import product

def signed_fwd_diff(seq, k, i):
    # k-th signed forward difference at offset i
    return sum(((-1)**(k-j)) * comb(k,j) * seq[i+j] for j in range(k+1))

def absdiff_triangle_entry(seq, k):
    # iterate absolute differences; row k is length len(seq)-k
    row = list(seq)
    for _ in range(k):
        row = [abs(row[j]-row[j+1]) for j in range(len(row)-1)]
    return row

# Counterexample from hand computation
seq = [5,1,6]
print("A_0 =", seq)
row0 = list(seq)
row1 = [abs(row0[j]-row0[j+1]) for j in range(len(row0)-1)]
row2 = [abs(row1[j]-row1[j+1]) for j in range(len(row1)-1)]
print("A_2(0) iterated abs diff =", row2[0])
print("|signed fwd diff Delta_2(0)| =", abs(signed_fwd_diff(seq,2,0)))
print()

# Exhaustive: search all small sequences for any (k,i) where they differ
print("Searching for mismatches (entries, length<=5, values 0..5)...")
count = 0
for L in range(2,6):
    for seq in product(range(6), repeat=L):
        absrows = [(absdiff_triangle_entry(seq,k)) for k in range(1, L)]
        for k in range(1, L):
            for i in range(L-k):
                absval = absdiff_triangle_entry(seq,k)[i]
                fd = signed_fwd_diff(seq,k,i)
                if absval != abs(fd):
                    count += 1
                    if count <= 8:
                        print("  MISMATCH", seq, "k=",k,"i=",i,
                              "absdiff=",absval,"|fwd|=",abs(fd))
print("total mismatches over", "all small seqs:", count)
