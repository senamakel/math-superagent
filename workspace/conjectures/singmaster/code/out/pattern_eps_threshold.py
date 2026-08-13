import math
# The boundary condition: k_j < exp((ln n_j)^{(2/3+eps)})  <=>  ln k_j < (ln n_j)^{2/3+eps}
# ln k ~ (4j+3)A - ln5 ; ln n ~ (4j+5)A - ln5 ; A=ln phi
# boundary holds iff (ln k) < (ln n)^(2/3+eps)
#   eps<1/3: exponent<1 => RHS/LHS ~ j^{eps-1/3} -> 0 => interior for large j (finite boundary)
#   eps=1/3: exponent=1, (ln n)>(ln k) always => boundary for ALL j  (infinite)
#   eps>1/3: exponent>1 => RHS dominates => boundary for all large j (infinite)
phi=(1+math.sqrt(5))/2; A=math.log(phi)
for eps in [0.20,0.32,1/3,0.35,0.5,0.9]:
    bnd=0; int_=0; interior_first=None
    for j in range(1,40000):
        lnn=(4*j+5)*A-math.log(5); lnk=(4*j+3)*A-math.log(5)
        b = lnk < lnn**(2/3+eps)
        if not b and interior_first is None: interior_first=j
        bnd += b; int_ += (not b)
    print("eps=%.4f 2/3+eps=%.4f: boundary j count=%d, interior=%d, first interior j=%s"%(eps,2/3+eps,bnd,int_,interior_first))
