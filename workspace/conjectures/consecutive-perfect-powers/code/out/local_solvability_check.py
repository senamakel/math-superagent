# Quick check: does x^p - y^q == 1 (mod r) have a solution for every
# fixed odd-prime pair (p,q)? If yes for every r, then no congruence/
# covering-congruence method can kill a fixed pair -> local methods dead.
from sympy import primerange

def solvable_mod(p, q, r):
    # search residues 0..r-1 (tiny r only)
    for x in range(r):
        xp = pow(x, p, r)
        for y in range(r):
            if (xp - pow(y, q, r)) % r == 1:
                return True
    return False

oddprimes = list(primerange(3, 20))
fails = []
for p in oddprimes:
    for q in oddprimes:
        for r in range(2, 101):
            if not solvable_mod(p, q, r):
                fails.append((p, q, r))
                break  # one failing modulus kills the pair

print("odd-prime pairs tested:", len(oddprimes)**2)
print("pairs with SOME modulus r<=100 where no solution mod r:", fails)
print("conclusion:", "covering possible" if fails else "every pair locally solvable mod all r<=100")
