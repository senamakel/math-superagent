import json
D=json.load(open("out/exact_state_1_120.json"))
# recompute E(k)=sum of values of length-k factors ending in 1
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
K=120
n=0
while word_len(n)<4*(K+1): n+=1
word=S(n)
E={}
for k in range(1,K+1):
    wk={word[i:i+k] for i in range(len(word)-k+1)}
    E[k]=sum(int(w) for w in wk if w[-1]=='1')

for k in range(1,31):
    print(f"k={k}: E(k)={E[k]}, P1(k)={D[str(k)]['P1']}, (E(k+1)-N1(k))/10={ (E[k+1]-D[str(k)]['N1'])//10 }")
print()
print("P1(k) == (E(k+1)-N1(k))/10 :", all((E[k+1]-D[str(k)]['N1'])//10==D[str(k)]['P1'] for k in range(1,120)))
