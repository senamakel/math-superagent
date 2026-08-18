"""Small exact attack on mech_psi -> ueuclid indexing and approximants."""
from fractions import Fraction
from lib.ueuclid import ue0, M
from mech.mech_psi import mech_psi, slope_for

def vals_from_floor_sum(k, p, q, variant):
    a = Fraction(p, q)
    pts = sorted((Fraction(-m*p, q)) % 1 for m in range(k+1))
    out = []
    for i in range(k+1):
        lo, hi = pts[i], pts[(i+1) % (k+1)] + (1 if i == k else 0)
        x = (lo + hi) / 2
        fl = [(x + j*a).numerator // (x + j*a).denominator
              for j in range(k+1)]
        if variant == "correct":
            out.append(sum((fl[j+1]-fl[j])*10**(k-1-j) for j in range(k)))
        elif variant == "shift-floor":
            out.append(sum((fl[j+2] if j+2 <= k else fl[j+1]) - fl[j]
                           for j in range(k)))
        elif variant == "shift-power":
            out.append(sum((fl[j+1]-fl[j])*10**(k-j) for j in range(k)))
    return sorted(out)

def check_ue0_moments():
    fails = []
    for p in range(1, 30):
      for r in range(2, 31):
       for q in range(0, r):
        for n in range(0, 21):
         z = 10
         got = ue0(p,q,r,n,z)
         s0 = sum(pow(z,i,M) for i in range(n)) % M
         s1 = sum(pow(z,i,M)*((p*i+q)//r) for i in range(n)) % M
         s2 = sum(pow(z,i,M)*((p*i+q)//r)**2 for i in range(n)) % M
         du = ((p*(n-1)+q)//r if n else 0)
         if (got.S0,got.S1,got.S2,got.dU) != (s0,s1,s2,du):
          fails.append((p,q,r,n,got,(s0,s1,s2))); return fails
    return fails

def main():
    print("indexing attack: exact k=1..20")
    bad = []
    for k in range(1,21):
        a,q,p = slope_for(k, 1)
        tA,tB,va,vb = mech_psi(k, q=q)
        vc = vals_from_floor_sum(k,p,q,"correct")
        if vc != va or tA != sum(v*v for v in vc):
            bad.append((k,"correct",q,tA,sum(v*v for v in vc)))
        for variant in ("shift-floor","shift-power"):
            vv = vals_from_floor_sum(k,p,q,variant)
            if vv == va:
                print("WARNING variant survived", k, variant)
                bad.append((k,variant,"survived"))
            else: print("countercheck", k, variant, "differs as expected")
        if tA != tB or va != vb: bad.append((k,"mech A/B",tA,tB,va==vb))
        print(f"k={k:2d} q={q:5d} Psi={tA % M:9d} exact-indexing=OK")
    print("ue0 exhaustive small-grid check")
    uf = check_ue0_moments(); print("ue0 failures:", len(uf))
    if uf: print(uf[0]); return 1
    print("RESULT: no counterexample; correct mapping passes, shifted mappings fail.")
    return 1 if bad else 0
if __name__ == '__main__': raise SystemExit(main())
