\\ PARI/GP independent cross-check of h^-(Q(zeta_p)) = relative (minus) class number.
\\ Route: direct class-group computation via bnfinit, NOT the Bernoulli-product formula.
\\   h^-(K) = h(K)/h(K^+) with K = Q(zeta_p), K^+ the maximal real subfield
\\   Q(zeta_p + zeta_p^{-1}) of degree (p-1)/2 (degree 1 = Q for p=3).
\\ polsubcyclo gives a defining polynomial of K^+; bnfinit computes the class
\\ group by the Buchmann-Lenstra reduction machinery, independent of any
\\ analytic (Bernoulli) class-number formula. h(K) and h(K^+) are computed
\\ separately; the ratio is h^-.
default(parisizemax, 4000000000);
p=3;  Kpol=polcyclo(p); Kp_pol=polsubcyclo(p,(p-1)/2); BK=bnfinit(Kpol); BR=bnfinit(Kp_pol); hK=BK.clgp[1]; hKp=BR.clgp[1]; printf("p=%3d h(K)=%d h(K+)=%d h-= %d\n",p,hK,hKp,hK/hKp);
p=5;  Kpol=polcyclo(p); Kp_pol=polsubcyclo(p,(p-1)/2); BK=bnfinit(Kpol); BR=bnfinit(Kp_pol); hK=BK.clgp[1]; hKp=BR.clgp[1]; printf("p=%3d h(K)=%d h(K+)=%d h-= %d\n",p,hK,hKp,hK/hKp);
p=7;  Kpol=polcyclo(p); Kp_pol=polsubcyclo(p,(p-1)/2); BK=bnfinit(Kpol); BR=bnfinit(Kp_pol); hK=BK.clgp[1]; hKp=BR.clgp[1]; printf("p=%3d h(K)=%d h(K+)=%d h-= %d\n",p,hK,hKp,hK/hKp);
p=11; Kpol=polcyclo(p); Kp_pol=polsubcyclo(p,(p-1)/2); BK=bnfinit(Kpol); BR=bnfinit(Kp_pol); hK=BK.clgp[1]; hKp=BR.clgp[1]; printf("p=%3d h(K)=%d h(K+)=%d h-= %d\n",p,hK,hKp,hK/hKp);
p=13; Kpol=polcyclo(p); Kp_pol=polsubcyclo(p,(p-1)/2); BK=bnfinit(Kpol); BR=bnfinit(Kp_pol); hK=BK.clgp[1]; hKp=BR.clgp[1]; printf("p=%3d h(K)=%d h(K+)=%d h-= %d\n",p,hK,hKp,hK/hKp);
p=17; Kpol=polcyclo(p); Kp_pol=polsubcyclo(p,(p-1)/2); BK=bnfinit(Kpol); BR=bnfinit(Kp_pol); hK=BK.clgp[1]; hKp=BR.clgp[1]; printf("p=%3d h(K)=%d h(K+)=%d h-= %d\n",p,hK,hKp,hK/hKp);
p=19; Kpol=polcyclo(p); Kp_pol=polsubcyclo(p,(p-1)/2); BK=bnfinit(Kpol); BR=bnfinit(Kp_pol); hK=BK.clgp[1]; hKp=BR.clgp[1]; printf("p=%3d h(K)=%d h(K+)=%d h-= %d\n",p,hK,hKp,hK/hKp);
p=23; Kpol=polcyclo(p); Kp_pol=polsubcyclo(p,(p-1)/2); BK=bnfinit(Kpol); BR=bnfinit(Kp_pol); hK=BK.clgp[1]; hKp=BR.clgp[1]; printf("p=%3d h(K)=%d h(K+)=%d h-= %d\n",p,hK,hKp,hK/hKp);
p=29; Kpol=polcyclo(p); Kp_pol=polsubcyclo(p,(p-1)/2); BK=bnfinit(Kpol); BR=bnfinit(Kp_pol); hK=BK.clgp[1]; hKp=BR.clgp[1]; printf("p=%3d h(K)=%d h(K+)=%d h-= %d\n",p,hK,hKp,hK/hKp);
p=31; Kpol=polcyclo(p); Kp_pol=polsubcyclo(p,(p-1)/2); BK=bnfinit(Kpol); BR=bnfinit(Kp_pol); hK=BK.clgp[1]; hKp=BR.clgp[1]; printf("p=%3d h(K)=%d h(K+)=%d h-= %d\n",p,hK,hKp,hK/hKp);
p=37; Kpol=polcyclo(p); Kp_pol=polsubcyclo(p,(p-1)/2); BK=bnfinit(Kpol); BR=bnfinit(Kp_pol); hK=BK.clgp[1]; hKp=BR.clgp[1]; printf("p=%3d h(K)=%d h(K+)=%d h-= %d\n",p,hK,hKp,hK/hKp);
p=41; Kpol=polcyclo(p); Kp_pol=polsubcyclo(p,(p-1)/2); BK=bnfinit(Kpol); BR=bnfinit(Kp_pol); hK=BK.clgp[1]; hKp=BR.clgp[1]; printf("p=%3d h(K)=%d h(K+)=%d h-= %d\n",p,hK,hKp,hK/hKp);
p=43; Kpol=polcyclo(p); Kp_pol=polsubcyclo(p,(p-1)/2); BK=bnfinit(Kpol); BR=bnfinit(Kp_pol); hK=BK.clgp[1]; hKp=BR.clgp[1]; printf("p=%3d h(K)=%d h(K+)=%d h-= %d\n",p,hK,hKp,hK/hKp);
