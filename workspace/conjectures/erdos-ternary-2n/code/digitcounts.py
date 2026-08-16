def base3(m):
    if m == 0: return "0"
    d=[]
    while m>0:
        d.append(str(m%3)); m//=3
    return "".join(reversed(d))

def counts(nmax):
    c2=[]; c1=[]; c0=[]
    for n in range(nmax+1):
        m=2**n
        s=base3(m)
        c2.append(s.count('2'))
        c1.append(s.count('1'))
        c0.append(s.count('0'))
    return c2,c1,c0

c2,c1,c0 = counts(80)
print("c2 (A260683):")
print(c2)
print("c1 (A036461):")
print(c1)
print("c0:")
print(c0)
print("len2:", len(c2))
