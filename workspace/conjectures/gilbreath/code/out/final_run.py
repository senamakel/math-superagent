from lib.gilbreath import primes_up_to, rows_generator

primes = primes_up_to(200000)
rows = list(rows_generator(primes, 160))
A1 = rows[1]

def block_profile(row):
    L = 0
    for x in row[1:]:
        if x in (0, 2): L += 1
        else: break
    return L

viol = 0; checked = 0
for k in range(2, 160):
    row = rows[k]
    for i in range(1, len(row)):
        lo = i - 1; hi = lo + (k - 1)
        if hi >= len(A1): break
        w = A1[lo:hi + 1]
        R = max(w) - min(w)
        checked += 1
        if row[i] > R: viol += 1
print("C1 all-cells: checked=%d violations=%d" % (checked, viol))

n_live = 0; events = 0; sumR = 0; sumRe = 0; ne = 0; iv = 0
for k in range(1, 160):
    row = rows[k]
    b = block_profile(row)
    if b + 1 >= len(row): continue
    n_live += 1
    y = row[b + 1]; edge = row[b]
    hi = b + (k - 1)
    if hi >= len(A1): continue
    w = A1[b:hi + 1]; R = max(w) - min(w)
    sumR += R
    if y > R: iv += 1
    if (edge, y) == (2, 4):
        events += 1; sumRe += R; ne += 1
print("C1 intruder: live=%d events=%d iviol=%d meanR_all=%.1f meanR_event=%.2f" % (
    n_live, events, iv, sumR/max(1,n_live), sumRe/max(1,ne)))

def sigma(v):
    return sum((-1)**i * v[i] for i in range(len(v)))
c2 = 0
for k in range(1, 160):
    a = rows[k]; b = rows[k+1]
    W = len(a) - 1
    lhs = sigma(b)
    mterm = sum((-1)**i * min(a[i], a[i+1]) for i in range(W))
    rhs = a[0] - ((-1)**W) * a[W] - 2 * mterm
    if lhs != rhs: c2 += 1
print("C2 identity: violations=%d" % c2)
