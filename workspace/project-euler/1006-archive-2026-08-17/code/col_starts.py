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

K = 12
n = 0
while word_len(n) < 3*(K+1):
    n += 1
word = S(n)

for k in range(1, K+1):
    subs = sorted({word[i:i+k] for i in range(len(word)-k+1)})
    rows = len(subs)
    M = rows  # k+1
    starts = []
    sizes = []
    for i in range(k):
        ones = {j for j in range(M) if subs[j][i]=='1'}
        # find circular interval: find a start s such that ones = {s, s+1, ..., s+len-1} mod M (consecutive increasing)
        # try each possible start
        found = None
        for s in range(M):
            # extend from s
            # check if ones equals a consecutive run starting at s going up
            # find length L such that {(s+t) mod M: t=0..L-1} == ones
            if len(ones)==0:
                found=(None,0); break
            # compute run from each one, find the 'first' after a gap
            # simpler: find all transitions
            arr = [1 if j in ones else 0 for j in range(M)]
            # circular interval means: treat as circular, count transitions
            # find start: scan for 0->1 transition
            start = None
            for j in range(M):
                if arr[j]==0 and arr[(j+1)%M]==1:
                    start=(j+1)%M
                    # verify run
            # Also handle case where it's the full circle
            if start is None:
                found=(0,M) if all(arr) else None
            else:
                # length of run
                L=0; j=start
                while arr[j]==1:
                    L+=1; j=(j+1)%M
                found=(start,L)
            break
        starts.append(found[0])
        sizes.append(found[1])
    print(f"k={k} (M={M}):")
    print("  starts:", starts)
    print("  sizes :", sizes)
