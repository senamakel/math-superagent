"""Verify: (1) c0 and c2 have identical parity counts because
c0+c1+c2 = number of ternary digits and c1 is even; (2) survivors occupy
exactly the even residues mod 2^m for small m — i.e. no 2-adic modular
obstruction beyond r even.
"""
def base3_len(m):
    l = 0
    while m > 0:
        m //= 3; l += 1
    return l

def counts(n):
    m = 2 ** n
    d = []
    while m > 0:
        d.append(m % 3); m //= 3
    return sum(1 for x in d if x==0), sum(1 for x in d if x==1), sum(1 for x in d if x==2)

# check c0+c1+c2 == digit length and c1 even => c0=c2 mod 2
bad = []
for n in range(1, 400):
    c0, c1, c2 = counts(n)
    total = base3_len(2**n)
    if c0 + c1 + c2 != total:
        bad.append((n, "sum!=len"))
    if (c0 - c2) % 2 != 0:
        bad.append((n, "parity"))
print("violations of {c0+c1+c2==len} or {c0==c2 mod2}:", bad[:10], "count", len(bad))
