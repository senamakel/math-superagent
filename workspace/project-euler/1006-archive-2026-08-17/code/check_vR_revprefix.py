import json

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

D=json.load(open("out/exact_state_1_120.json"))

K=120
n=0
while word_len(n)<4*(K+1): n+=1
word=S(n)
# infinite fibonacci word prefix F[0:K]
F = word[:K]

fails=0
for k in range(1, K+1):
    pref = F[:k]
    rev = pref[::-1]
    val_rev = int(rev)
    actual = D[str(k)]['vR']
    if val_rev != actual:
        fails+=1
        if fails<5:
            print(f"k={k}: rev-prefix={rev}={val_rev} actual={actual}")
print("v_R(k) == reverse(F[:k]) failures over k=1..%d:"%K, fails)
