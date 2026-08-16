import math
LP2 = math.log(2.0)
def h(x):
    if x<=0 or x>=1: return 0.0
    return -x*math.log(x)/LP2 - (1-x)*math.log(1-x)/LP2

# The collapsed alpha=0 coupling value at t=1/2, a=(3-sqrt5)/2, independent:
a = (3-math.sqrt(5))/2
t = 0.5
b = (a+1)/2
beta = (t-a)/(b-a)
w1 = (1-beta) + beta/2   # weight on p=a
w2 = beta/2              # weight on p=1
# marginal atoms a and 1; h(1)=0
eh = w1*h(a)
# e_indep: only (a,a)*(a,a) survives (any coordinate 1 gives arg=1, h(1)=0)
e_indep = w1*w1*h(2*a - a*a)
ratio = e_indep/eh
phi2 = (1+math.sqrt(5))/4
print("independent recomputation of collapsed Gamma_hat(1/2):")
print(f"  a={a:.12f}  beta={beta:.12f}  w1={w1:.12f}")
print(f"  ratio = {ratio:.12f}")
print(f"  phi/2 = {phi2:.12f}")
print(f"  equal within float? {abs(ratio-phi2)<1e-12}")
print(f"  < 1 (so NOT a certificate of density 1/2)? {ratio<1.0}")
