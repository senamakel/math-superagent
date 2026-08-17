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
K=30
n=0
while word_len(n)<4*(K+1): n+=1
word=S(n)
F=word[:200]
for k in [3,5,6,7,10,12]:
    wk=sorted({word[i:i+k] for i in range(len(word)-k+1)})
    wk1={word[i:i+k+1] for i in range(len(word)-(k+1)+1)}
    ext1=[w for w in wk if (w+'1') in wk1]
    rev=F[:k][::-1]
    print(f"k={k}: reverse(F[:k])={rev}")
    print(f"     ext1 factors={ext1}")
