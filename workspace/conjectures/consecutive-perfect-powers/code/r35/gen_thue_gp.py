"""Generate the two Thue binary forms for R-35 from the Eisenstein reduction,
verify their indexing (W-coefficient / real-part recovery), and emit .gp scripts
for PARI thue().

CASE I  (3 ∤ y): factors pairwise coprime.  x-w=(r+sw)^5=(R,S*1..w) exactly.
  match x-w=(x,-1):  S(r,s)=5r^4s-10r^3s^2+5rs^4-s^5 = -1,  x=R(r,s)=2S+1? 
  verify x = R (real part) which equals... recompute below.

CASE II (3 | y): x-w=P*beta^5, P=1-w.  Match to (x,-1):
  P*beta^5 = (R+S) + (2S-R)w  -> 2S-R=-1, x=R+S.
  (We do NOT write x-w^2=P*conj^5; the conjugate uses conj(P).)

Generates code/out/r35_thue1.gp and r35_thue2.gp.
"""
Rstr = "r^5 - 10*r^3*s^2 + 10*r^2*s^3 - s^5"
Sstr = "5*r^4*s - 10*r^3*s^2 + 5*r*s^4 - s^5"

def homogeneous_polynomial(coeffs):
    # coeffs: dict {(i,j): coef} with i+j=d (degree d)
    pass

def main():
    # CASE I:  S(r,s) = -1 ; form F1(r,s)=S, f1(x)=F1(x,1)=5x^4-10x^3+5x-1
    f1 = "5*x^4 - 10*x^3 + 5*x - 1"
    # CASE II: 2S - R = -1 ; 
    #   2S - R = -r^5+10r^4s-10r^3s^2-10r^2s^3+10rs^4-s^5
    #   f2(x)=(2S-R)(x,1)= -x^5+10x^4-10x^3-10x^2+10x-1, RHS -1
    f2 = "-x^5 + 10*x^4 - 10*x^3 - 10*x^2 + 10*x - 1"

    # sanity: evaluate forms directly in python over integers for small (r,s)
    def F1(r, s): return 5*r**4*s - 10*r**3*s**2 + 5*r*s**4 - s**5
    def F2(r, s): return -r**5 + 10*r**4*s - 10*r**3*s**2 - 10*r**2*s**3 + 10*r*s**4 - s**5
    def Rv(r, s): return r**5 - 10*r**3*s**2 + 10*r**2*s**3 - s**5
    def Sv(r, s): return 5*r**4*s - 10*r**3*s**2 + 5*r*s**4 - s**5

    # Check identity 2S - R = F2
    ok = True
    for r in range(-6, 7):
        for s in range(-6, 7):
            if 2*Sv(r, s) - Rv(r, s) != F2(r, s):
                print("F2 id mismatch", r, s)
                ok = False
    print("identity 2S-R == F2 holds on box:", ok)

    # Write gp scripts
    gp1 = f"""/* R-35 CASE I Thue: F1(r,s)=5r^4s-10r^3s^2+5rs^4-s^5 = -1.
       Binary form deg5; f1(x)=F1(x,1)=5x^4-10x^3+5x-1. */
f1 = {f1};
T1 = thueinit(f1);
print("CASE I  S(r,s)=-1 root poly f1=", f1);
print("solutions:", thue(T1, -1));
/* also record R(r,s) recovered for each solution in python */
"""
    gp2 = f"""/* R-35 CASE II Thue: 2S-R = -1.
       F2(r,s)=-r^5+10r^4s-10r^3s^2-10r^2s^3+10rs^4-s^5.
       f2(x)=F2(x,1).  thue(T2,-1) or +1. */
f2 = {f2};
T2 = thueinit(f2);
print("CASE II 2S-R=-1 root poly f2=", f2);
print("solutions:", thue(T2, -1));
"""
    # Warning: PARI thue returns solutions (x,y) of F(x,y)=a with y possibly
    # sign.  We'll parse in python.
    with open("code/out/r35_thue1.gp", "w") as fh:
        fh.write(gp1)
    with open("code/out/r35_thue2.gp", "w") as fh:
        fh.write(gp2)
    print("wrote r35_thue1.gp, r35_thue2.gp")

if __name__ == "__main__":
    main()
