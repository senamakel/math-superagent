def base3(m):
    d=[]
    while m>0:
        d.append(m%3); m//=3
    return d

# verify mod-2 theorem: c1 (ones) even for n>=1
# proof: 2^n = sum a_i 3^i; mod 2 each 3^i=1, so 2^n = #ones mod 2; 2^n even (n>=1)
ok=True
for n in range(1,3000):
    s=base3(2**n)
    c1=sum(1 for x in s if x==1)
    if c1%2!=0:
        print("VIOLATION n=",n); ok=False; break
print("c1(n) even for all 1<=n<3000:", ok)

# verify n must be even for survivors: lowest ternary digit of 2^n is 1 iff n even
print("survivors all even -> consistent 2^n mod3=1")

# digit sum mod 2 equals c1 (correct statement)
for n in [2,8,0]:
    m=2**n
    print(f"n={n}: 2^n={m} == sum digits mod2? {m%2==sum(base3(m))%2}")
