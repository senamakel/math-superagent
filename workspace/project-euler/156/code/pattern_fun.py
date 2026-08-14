import sys, random
sys.path.insert(0, "/workspace/code")
from lib.digits import f_place_value

def sol_eq(n,d):
    return f_place_value(n,d) == n

# Hypothesis A (functional self-similarity):
#   f(k*10^10 + x, d) - (k*10^10+x)  ==  f(x,d) - x   for k=1..8, 0<=x<10^10, d=1..9?
# If true, solution sets are EXACTLY translation-invariant across blocks.
random.seed(1)
fails = []
checked = 0
for d in range(1,10):
    for k in range(1,9):
        if k > d-1:  # beyond digit d's bound the translation may still hold; test anyway
            pass
        for _ in range(3000):
            x = random.randrange(0, 10**10)
            n = k*10**10 + x
            lhs = f_place_value(n,d) - n
            rhs = f_place_value(x,d) - x
            checked += 1
            if lhs != rhs:
                fails.append((d,k,x,n,lhs,rhs))
                if len(fails) > 5: break
        if len(fails) > 5: break
    if len(fails) > 5: break
print(f"Hypothesis A (translation invariance of f(n,d)-n across 10^10 blocks): checked={checked}")
print("  holds exactly:", len(fails)==0)
if fails:
    for f in fails[:5]: print("  FAIL", f)

# Hypothesis B: self-similarity for k in 1..d-1 only (digit d's block range)
failsB=[]; checkedB=0
for d in range(2,10):
    for k in range(1,d):
        for _ in range(5000):
            x = random.randrange(0, 10**10)
            n = k*10**10 + x
            if f_place_value(n,d)-n != f_place_value(x,d)-x:
                failsB.append((d,k,x))
                if len(failsB)>5: break
        if len(failsB)>5: break
print(f"\nHypothesis B (only k=1..d-1): checked={checkedB} holds={len(failsB)==0}")
print(failsB[:5])
