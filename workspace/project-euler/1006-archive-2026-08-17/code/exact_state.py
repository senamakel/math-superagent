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
MOD=101001001
K=120
n=0
while word_len(n)<4*(K+1): n+=1
word=S(n)
# store exact state
import json
D={}
for k in range(1,K+1):
    wk={word[i:i+k] for i in range(len(word)-k+1)}
    wk1={word[i:i+k+1] for i in range(len(word)-(k+1)+1)}
    vals={w:int(w) for w in wk}
    N1=sum(1 for w in wk if (w+'1') in wk1)
    P1=sum(vals[w] for w in wk if (w+'1') in wk1)
    vR=next(vals[w] for w in wk if (w+'0') in wk1 and (w+'1') in wk1)
    Rstr=next(w for w in wk if (w+'0') in wk1 and (w+'1') in wk1)
    P=sum(v*v for v in vals.values())
    D[k]=dict(N1=N1,P1=P1,vR=vR,R=Rstr,P=P)

# save exact
with open("out/exact_state_1_120.json","w") as f:
    json.dump(D,f)
print("saved exact state k=1..120")

# look at P1 vs vR: try P1 = c*vR + ... or relation where P1 is sum of values of factors ending-1
# For a factor extending by 1, value = v_w. Hmm.
# Let's check: P1(k) relative to vR(k)²
print("\nk : vR² mod M : P1 mod M : P mod M")
for k in [1,2,3,4,5,6,10,15,20,25,30,40,50,60]:
    d=D[k]
    print(f"  {k}: vR²={d['vR']*d['vR']%MOD}, P1={d['P1']%MOD}, P={d['P']%MOD}, N1={d['N1']}")
