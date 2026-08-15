"""
Independent Sage cross-check for R-fixed-23 proof.
K = Q(omega), omega^3 = 2, ring of integers Z[omega] (class number 1, PARI).
Every unit is +-(1-omega)^n.  Enumerate a WIDE window in the explicit tuple
ring eta = a + b w + c w^2, w^3 = 2, and read off (c,d) with c^3-2d^3=+-1
and zero w^2 coefficient.  Independent of the PARI thue route.
"""
K.<w> = NumberField(x^3 - 2)
print("class number h(K) =", K.class_number())

def mul(A, B):
    a0,b0,c0 = A; a1,b1,c1 = B
    return (a0*a1 + 2*(b0*c1 + c0*b1),
            a0*b1 + b0*a1 + 2*c0*c1,
            a0*c1 + b0*b1 + c0*a1)

one_minus_w = (1, -1, 0)
inv = (-1,-1,-1)                       # (1-w)^-1 = -(1+w+w^2)
print("check (1-w)*(1-w)^-1 = (1,0,0):", mul(one_minus_w, inv))

sols = set()
WINDOW = 400
for n in range(-WINDOW, WINDOW+1):
    if n >= 0:
        val = (1,0,0)
        for _ in range(n):
            val = mul(val, one_minus_w)
    else:
        val = (1,0,0)
        for _ in range(-n):
            val = mul(val, inv)
    a0,b0,c0 = val
    if c0 == 0:
        c, d = a0, -b0
        N = c**3 - 2*d**3
        if N in (1,-1):
            sols.add((c,d,N))
            print(f"  n={n}: (c,d)=({c},{d})  c^3-2d^3={N}")

print("\nAll (c,d) from unit method, window [-%d,%d]:" % (WINDOW,WINDOW))
for (c,d,N) in sorted(sols): print("  (c,d)=", (c,d), " norm=", N)

# Route through descent cases, keep x,y>0
final = set()
for (c,d,N) in sols:
    if N == -1 and 2*d**3 - c**3 == 1 and c>0 and d>0:
        k = c**3; x = 2*k+1; y = 2*c*d
        if x**2 - y**3 == 1 and y > 0: final.add((x,y))
    if N == 1 and c**3 - 2*d**3 == 1 and c>0 and d>0:
        k = 2*d**3; x = 2*k+1; y = 2*c*d
        if x**2 - y**3 == 1 and y > 0: final.add((x,y))
print("\nFinal (x,y) with y>0:", sorted(final))
print("Contains (3,2):", (3,2) in final)
