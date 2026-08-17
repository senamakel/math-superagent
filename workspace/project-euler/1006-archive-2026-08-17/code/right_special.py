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

K = 120
n = 0
while word_len(n) < 5*(K+1):
    n += 1
word = S(n)

# For each k, find right-special factor: the length-k factor that extends to both w0 and w1 within word
previous = None
for k in range(1, K+1):
    subs = {word[i:i+k] for i in range(len(word)-k+1)}
    # extend: check membership of w+'0' and w+'1' in length-(k+1) factors
    subs2 = {word[i:i+k+1] for i in range(len(word)-(k+1)+1)}
    R = None
    for w in subs:
        if w+'0' in subs2 and w+'1' in subs2:
            R = w
            break
    val = int(R)
    # block id: group by val
    print(f"{k}: v_R={val}, binary={R}")
