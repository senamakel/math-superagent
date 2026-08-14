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

K = 2000
n = 0
while word_len(n) < 4*(K+1):
    n += 1
word = S(n)

phi = (Decimal(1)+Decimal(5).sqrt())/2
alpha = Decimal(1)/phi**2   # (3-sqrt5)/2 ~ 0.381966
one_minus_alpha = Decimal(1)-alpha  # (sqrt5-1)/2 ~ 0.618034

failN1 = []; failN0 = []; fail_sum = []
for L in range(2, K+2):
    subs = {word[i:i+L] for i in range(len(word)-L+1)}
    subs_1 = {word[i:i+L-1] for i in range(len(word)-(L-1)+1)}  # length L-1
    subs_L = subs
    # N1(k) with k=L-1 = # length-L factors ending in 1
    e1 = sum(1 for s in subs_L if s[-1]=='1')
    k = L-1
    # N0(k) = # length-(k)=L-1 factors w with w0 a length-L factor.
    # = # length-(L-1) factors that extend by 0 to a factor. Equivalent: # length-L factors ending in 0? 
    # A length-(L-1) factor w extends to w0 iff w0 is a length-L factor. The w that extend by 0 correspond bijectively? 
    # Simplest: # factors of length L-1 whose '0' extension exists = count of distinct length-L factors ending in 0? Not exactly bijective but N0 from earlier = # length-k factors with w0 factor.
    # We'll compute N0 as number of length-(L-1) words w in subs_{L-1} with w+'0' in subs_L.
    subs_prev = {s[:-1] for s in subs_L}  # all prefixes of length L-1 = the L... actually all length-(L-1) factors appear as prefixes? 
    # better compute actual
    subs_Lm1 = {word[i:i+L-1] for i in range(len(word)-(L-1)+1)}
    e0 = sum(1 for w in subs_Lm1 if (w+'0') in subs_L)
    # formulas
    x = Decimal(k+1)*alpha
    ceilN1 = x.to_integral_value(rounding='ROUND_CEILING')
    y = Decimal(k+1)*one_minus_alpha
    ceilN0 = y.to_integral_value(rounding='ROUND_CEILING')
    if e1 != int(ceilN1):
        failN1.append((k,e1,int(ceilN1)))
    if e0 != int(ceilN0):
        failN0.append((k,e0,int(ceilN0)))
    if e1+e0 != k+2:
        fail_sum.append((k,e1+e0,k+2))

print("N1(k)=ceil((k+1)alpha) fails:", len(failN1), failN1[:5])
print("N0(k)=ceil((k+1)(1-alpha)) fails:", len(failN0), failN0[:5])
print("N1+N0==k+2 fails:", len(fail_sum), fail_sum[:5])
