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
for k in [3,4,5,6,7,10]:
    wk=sorted({word[i:i+k] for i in range(len(word)-k+1)})
    wk1={word[i:i+k+1] for i in range(len(word)-(k+1)+1)}
    ext1=[w for w in wk if (w+'1') in wk1]
    ext0=[w for w in wk if (w+'0') in wk1]
    both=[w for w in wk if (w+'0') in wk1 and (w+'1') in wk1]
    print(f"k={k}")
    print("  all  factors:", wk)
    print("  ext to 1:", ext1)
    print("  ext to 0:", ext0)
    print("  both (right-special):", both)
    # positions in lex order
    idx={w:i for i,w in enumerate(wk)}
    print("  indices ext1:", [idx[w] for w in ext1])
    print("  indices ext0:", [idx[w] for w in ext0])
    print("  indices right-spec:", [idx[w] for w in both])
