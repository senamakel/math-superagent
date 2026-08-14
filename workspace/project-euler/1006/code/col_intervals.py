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

K = 60
n = 0
while word_len(n) < 3*(K+1):
    n += 1
word = S(n)

for k in range(2, 16):
    subs = sorted({word[i:i+k] for i in range(len(word)-k+1)})
    # rows = subs (each is a binary string of length k)
    # For column i (0-indexed from left = MSB), find circular interval of rows where bit is 1
    rows = len(subs)  # k+1
    print(f"--- k={k}, {rows} rows ---")
    for i in range(k):
        ones = [j for j in range(rows) if subs[j][i]=='1']
        # check circular interval: when we go around, at most one transition 1->0 and 0->1 (circular)
        # mark run
        mask = [1 if j in ones else 0 for j in range(rows)]
        # check circularity of ones
        print(f"  col {i}: ones={ones}")
