import sympy
from collections import Counter
n=sympy.Symbol('n')

table={}
for N in range(2,13):
    with open(f"data/level_{N}.txt") as f: lines=f.read().splitlines()
    c=Counter()
    for ln in lines: c[int(ln.split("|")[1].strip())]+=1
    table[N]=dict(c)
table[13]={7:612,8:9342,9:51678,10:172044,11:393660,12:590490,13:531441}
table[14]={7:267,8:7122,9:54756,10:237897,11:688905,12:1417176,13:1948617,14:1594323}

print("=== diagonal M=N: count == 3^(N-1)? for all N===")
for N in sorted(table):
    if N in table[N]:
        c=table[N][N]
        print(f"N={N}: M=N count={c}, 3^(N-1)={3**(N-1)}, match={c==3**(N-1)}")

forms={0:lambda n:1,1:lambda n:n-3,2:lambda n:(n-5)*(n+2)/2,
       3:lambda n:(n**3-73*n+168)/6,
       4:lambda n:n**4/24+n**3/4-sympy.Rational(205,24)*n**2+sympy.Rational(97,4)*n+27}
# reconstruct D(N) = sum over M of modeled count, compare to actual D(N)
print("\n=== reconstruct D(N) from modeled columns k=0..4 ===")
total_actual={2:3,3:9,4:30,5:99,6:336,7:1134,8:3855,9:13086,10:44499,11:151263,12:514419,13:1749267,14:5949063}
for N in sorted(total_actual):
    model_sum=0
    for k,f in forms.items():
        M=N-k
        if M in table[N] and M>=1:
            model_sum += sympy.simplify(f(n)).subs(n,N)*3**(N-2*k-1)
    # if the modeled k=0..4 columns already cover ALL M (i.e., no M with larger k used)
    allM=[]
    for k in range(0,N-1):
        M=N-k
        if M in table[N]: allM.append(M)
    # determine how many M not coverable by k=0..4
    uncovered=[M for M in table[N] if N-M>4]
    note = f"{len(uncovered)} M-rows beyond k=4 (k={[N-M for M in uncovered]}) not modeled" if uncovered else "all M covered by k=0..4"
    print(f"N={N}: modeled_sum={model_sum}, actual D={total_actual[N]}, match={model_sum==total_actual[N]} ; {note}")

# explicit: for N where k<=4 covers everything
print("\nN=8: model covers M=4..8 (k=4..0)? rows:", [(M,N-M) for M in table[8]])
print("N=9 covers M=5..9 (k=4..0): rows:", [(M,N-M) for M in table[9]])
# full reconstruction of D(8),D(9) where all columns modeled
for N in (8,9):
    s=0
    for M in table[N]:
        k=N-M; s+=forms[k](n)*3**(N-2*k-1)
    s=sympy.simplify(s)
    print(f"full-model D({N}) = {s}, actual {total_actual[N]}, match {s==total_actual[N]}")
