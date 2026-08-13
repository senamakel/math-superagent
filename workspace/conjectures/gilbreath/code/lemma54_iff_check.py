# Test Granville Lemma 5.4 on real primes, INCLUDING the case he discards.
# delta_k(q_n) = A_k[n-k].  0-2 cycle of delta(q_{n-1}) = maximal {0,2} suffix.
# Claim (his iff, before weakening): success at q_n  <=>  v_n <= 2*nu2(q_{n-1}) + 2,
# where v_n = delta_{tau_n}(q_n) and tau_n = start index of that cycle.
N=2000000
s=bytearray([1])*(N+1); s[0]=s[1]=0
for i in range(2,int(N**0.5)+1):
    if s[i]: s[i*i::i]=bytearray(len(s[i*i::i]))
P=[i for i in range(N+1) if s[i]]
M=2500
rows=[P[:M+3]]
for k in range(1,M+2):
    p=rows[-1]; rows.append([abs(p[i+1]-p[i]) for i in range(len(p)-1)])
def diag(n): return [rows[k][n-k] for k in range(n+1)]   # k=0..n, delta_n = rows[n][0]
def cycle_start(d):
    t=len(d)-1                      # d[-1] is the green terminal
    body=d[:-1]; i=len(body)
    while i>2 and body[i-1] in (0,2): i-=1
    return i
iff_viol=0; suff_viol=0; zero_cases=0; n_ok=0; tested=0
for n in range(20,M):
    dprev=diag(n-1); dcur=diag(n)
    tau=cycle_start(dprev)
    cyc=dprev[tau:-1]
    if any(x not in (0,2) for x in cyc): continue
    nu2=cyc.count(2)
    if tau>=len(dcur)-1: continue
    v=dcur[tau]
    success = (dcur[-1]==1)
    tested+=1
    if success: n_ok+=1
    pred = (v <= 2*nu2+2)
    if pred!=success: iff_viol+=1
    gstar=max(rows[1][1:n+1])
    if gstar<=2*nu2+2 and not success: suff_viol+=1
    # the discarded case: some delta_{k-1}(q_n)=0 inside the gray block
    if 0 in dcur[tau:-1]: zero_cases+=1
print("tested n:",tested," all successful:",n_ok==tested,"(",n_ok,")")
print("iff  v<=2*nu2+2 <=> success : violations =",iff_viol)
print("suff g*<=2*nu2+2 => success : violations =",suff_viol)
print("rows where the discarded delta=0 case actually occurs:",zero_cases,
      "(%.1f%%)"%(100*zero_cases/max(1,tested)))
