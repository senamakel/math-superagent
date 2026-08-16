"""Understand |A_k mod 3^j| = 2^j: is it a collapse? Are the classes nested in j?
And is 2^j an exact structure or a coincidence? Also compare to |A_j| = 2^(j-1).
"""
def survivor_sets(K):
    sets = {1: {0}}
    A = {0}
    cur = 1
    while cur < K:
        L = 2 * 3 ** (cur - 1)
        next_mod = 3 ** (cur + 1)
        g = pow(2, L, next_mod)
        p3k = 3 ** cur
        Anext = set()
        for r in A:
            base = pow(2, r, next_mod)
            gp = 1
            for j in range(3):
                v = (base * gp) % next_mod
                d = (v // p3k) % 3
                if d in (0, 1):
                    Anext.add(r + j * L)
                gp = gp * g % next_mod
        A = Anext
        cur += 1
        sets[cur] = A
    return sets

sets = survivor_sets(20)
A = sets[20]
print("|A_20| =", len(A), " (=2^19=", 2**19, ")")
# count classes mod 3^j and compare with available: survivors count, 3^j
print("\n=== collapse structure: |A_20 mod 3^j|, |A_20|, 3^j ===")
prev_classes = None
nested = True
for j in range(1, 13):
    mod = 3**j
    c = {r % mod for r in A}
    print(f"  j={j:2d}: mod={mod:7d} classes={len(c):6d}  3^j={mod}  2^j={2**j}  "
          f"2^(k-1)={len(A)}")
    if prev_classes is not None:
        # classes mod 3^(j-1) vs classes mod 3^j reduced
        red = {x % 3**(j-1) for x in c}
        if red != prev_classes:
            nested = False
            print("    NOT nested!")
    prev_classes = c
print("nested over j: ", nested)

# Also check: is |A_k mod 3^j| independent of which k >= j+1 (already shown), 
# and does it equal 2^j for ALL k>=j+1? Show a k small.
print("\n=== |A_k mod 3^j| for k=j+1 (minimum) ===")
for j in range(1, 9):
    k = j + 1
    mod = 3 ** j
    print(f"  k={k}, j={j}: classes={len({r % mod for r in sets[k]})} (2^j={2**j})")
