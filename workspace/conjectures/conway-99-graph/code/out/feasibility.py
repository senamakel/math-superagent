"""Feasibility of srg(v,k,lambda,mu) members — exact integer check.

This is a FEASIBILITY check, not the oracle. The oracle (srg check on an
adjacency matrix) lives elsewhere. Here we compute, for lambda=1, mu=2:
  - v from counting: v = 1 + k + k*(k-2)//2
  - r,s roots of x^2 - (lam-mu)x - (k-mu) = x^2 + x - (k-2)
  - multiplicities f (of r), g (of s) via integrality condition
    f = (-k - (v-1)*s)//... using the standard formula:
    f = ((-k + (v-1)*mu*... )) -- use exact projection form:
    f = ( -k*(k-1) - k*lam + ... ) -- simpler: use
    f = ((v-1)*mu - 2*k*(k-... ) hmm; use known formula
    f,g = ((v-1) +- (k - (v-1)*(lam-mu))/sqrt((lam-mu)**2 + 4*(k-mu)))/2
    with sign: for r = 3, s = -4 here.

Standard multiplicity formulas:
  f,rrelation: let delta = (lam-mu)**2 + 4*(k-mu). r,s = (lam-mu +- sqrt(delta))/2.
  f = ((v-1)*s + k*... ) -- easiest exact:
  f = 1/2 * [ (v-1) - (2*k + (v-1)*(lam-mu))/sqrt(delta) ]  for the NEGATIVE eigenvalue
  g = 1/2 * [ (v-1) + (2*k + (v-1)*(lam-mu))/sqrt(delta) ]
Check with known case k=14,v=99: delta=49 sqrt=7, lam-mu=-1.
  term = 2*k + (v-1)*(-1) = 28 - 98 = -70; /7 = -10.
  f = (98 - (-10))/2 = 54; g = (98 + (-10))/2 = 44.  ✓ (matches 54,44)
We print exact integer feasibility. Uses only integer arithmetic (sympy for
exact sqrt check).
"""
from sympy import integer_nthroot, Rational

lam, mu = 1, 2

def feas(k):
    v = 1 + k + k*(k-2)//2
    delta = (lam-mu)**2 + 4*(k-mu)   # 4k - 7
    root, perfect = integer_nthroot(delta, 2)
    if not perfect:
        return v, None, None, False, "4k-7 not a perfect square"
    # eigenvalue multiplicities; numerator must be even and integer
    # term = 2k + (v-1)*(lam-mu)  ; /sqrt(delta)
    term = 2*k + (v-1)*(lam-mu)
    if term % root != 0:
        return v, None, None, False, "multiplicity numerator not divisible by sqrt"
    q = term // root
    num = (v-1) - q
    if num % 2 != 0:
        return v, None, None, False, "multiplicity not integer (odd numerator)"
    g = num // 2          # multiplicity of NEGATIVE eigenvalue
    f = v - 1 - g         # multiplicity of r
    if f < 0 or g < 0:
        return v, f, g, False, "negative multiplicity"
    return v, f, g, True, "feasible"

print("k    v    f(r)  g(s)  feasible  note")
for k in [4, 8, 14, 22, 32, 44, 112, 994]:
    v, f, g, ok, note = feas(k)
    print(f"{k:>4} {v:>5} {str(f):>6} {str(g):>6}  {str(ok):>8}  {note}")
