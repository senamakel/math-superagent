import json
data = json.load(open('code/out/nu2_primes_xor_40000.json'))
N = len(data)-1
print("max index", N, "nu2(40000)=", data[40000])

def subseq(name, fn, limit=40):
    vals=[]
    for n in range(2, min(N, 120000)+1):
        v = fn(n)
        if v is not None:
            vals.append(v)
        if len(vals)>=limit: break
    print(name, "len", len(vals))
    print(" ".join(map(str, vals)))
    print()

# powers of two
subseq("pow2", lambda n: data[n] if (n & (n-1))==0 else None, 24)
# numbers with n-1 a power of two => n = 2^k+1
subseq("2^k+1", lambda n: data[n] if (n-1) and ((n-1)&(n-2))==0 else None, 24)
# n = 2^k - 1 (Mersenne-like index)
subseq("2^k-1", lambda n: data[n] if (n+1) and ((n+1)&n)==0 else None, 24)
# odd n
subseq("odd", lambda n: data[n] if n%2==1 else None, 40)
# n multiple of small powers of 2
for m in (3,4,8):
    subseq(f"mult{m}", lambda n:m, None) # placeholder not used
