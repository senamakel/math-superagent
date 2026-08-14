from decimal import Decimal, getcontext
getcontext().prec = 60

def S(n):
    a, b = "0", "01"
    if n == 0: return a
    if n == 1: return b
    for _ in range(2, n+1):
        a, b = b, b + a
    return b

def word_len(n):
    a, b = 1, 2
    if n == 0: return a
    if n == 1: return b
    for _ in range(2, n+1):
        a, b = b, a+b
    return b

MOD = 101001001
K = 200
n = 0
while word_len(n) < 4*(K+1):
    n += 1
word = S(n)

# exact v_R and P1 per k
data = {}
for k in range(1, K+1):
    wk = {word[i:i+k] for i in range(len(word)-k+1)}
    wk1 = {word[i:i+k+1] for i in range(len(word)-(k+1)+1)}
    vals = {w: int(w) for w in wk}
    N1 = sum(1 for w in wk if (w+'1') in wk1)
    P1 = sum(vals[w] for w in wk if (w+'1') in wk1)
    vR = next(vals[w] for w in wk if (w+'0') in wk1 and (w+'1') in wk1)
    data[k] = dict(N1=N1, P1=P1, vR=vR)

# run-length structure of vR (constant value runs)
runs = []
cur_val = None; cur_start=None
for k in range(1,K+1):
    v = data[k]['vR']
    if v != cur_val:
        if cur_val is not None:
            runs.append((cur_start, k-1, cur_val))
        cur_val=v; cur_start=k
runs.append((cur_start,K,cur_val))
print(f"v_R runs for k=1..{K}: (start,end,value)")
for s,e,v in runs:
    print(f"  k={s}..{e} (len {e-s+1}): {v}")

# analyze run lengths
lens = [e-s+1 for s,e,v in runs]
print("\nrun lengths:", lens)

# P1 vs vR relationship, and P1 closed form attempt
# Try P1(k) relation: factors w with w1 factor. Their values v_w. 
phi=(Decimal(1)+Decimal(5).sqrt())/2
alpha=1/Decimal(1)-Decimal(1)  # placeholder
alpha = (Decimal(3)-Decimal(5).sqrt())/2

# check P1+vR type relation
print("\nk, N1, P1, vR (exact):")
for k in [1,2,3,4,5,6,7,8,9,10,15,20,25,30]:
    d=data[k]
    print(f"  k={k}: N1={d['N1']}, P1={d['P1']}, vR={d['vR']}")
