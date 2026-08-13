"""Structural check: v2 distribution of prime divisors of 2^m + 1 (m even)
against the paper's claim that known factors of open candidates have
v2 in {2,3} only (no r ≡ 1 mod 16).

Uses: (a) Appendix C cofactors as a sanity cross-check list; (b) direct
factorization of 2^m+1 for accessible even m to tabulate v2(q-1) over
q | 2^m+1. This tests Conjecture 29's premise on the reachable empirical scale.

This is a structural check, not a search for a sixth UPN.
"""
import sympy
import re

def v2(n):
    return (n & -n).bit_length() - 1 if n else 0

def divisors_mod16(mmax):
    """For even m<=mmax, factor 2^m+1, collect v2(q-1) for each prime q."""
    results = {}
    for m in range(2, mmax+1, 2):
        N = 2**m + 1
        fac = sympy.factorint(N)
        v2s = [v2(q-1) for q in fac]
        results[m] = (fac, v2s)
    return results

def main():
    # 1. Reproduce the paper's claim on open-candidate-like scale is impossible
    #    (exponents to 35000), so we test on the reachable even-m scale and
    #    report what the v2 distribution looks like.
    print("Explicit assertion: this covers reachable even m, NOT the paper's")
    print("open candidates (m=2p, p up to 17467). It is a scaling smaller run,")
    print("a structural probe of the v2 profile, not branch closure.\n")

    mmax = 60
    res = divisors_mod16(mmax)
    for m in sorted(res):
        fac, v2s = res[m]
        # count primes with v2>=4 (≡1 mod 16)
        ge4 = sum(1 for x in v2s if x >= 4)
        print(f"m={m:3d}  #primes={len(fac):2d}  v2(q-1) multiset={sorted(v2s)}  n_r(r>=4)={ge4}")

    # 2. Read Appendix C cofactor list for 2,n+ / 2,nL / 2,nM entries (sanity)
    try:
        with open("research/sources/cunningham-appendix-c-2n-plus-1.full.md") as f:
            text = f.read()
        entries = re.findall(r"\b2,\s*(\d+)\s*([+\-LM])\s*(\d+)", text)
        print(f"\nAppendix C has {len(entries)} entries matching '2,n<+/L/M' pattern")
        # sample the + and M side
        plus = [e for e in entries if e[1] == '+']
        lm = [e for e in entries if e[1] in 'LM']
        print(f"  of which 2,n+ : {len(plus)}, 2,nL/M (Aurifeuillean): {len(lm)}")
        print("  sample 2,n+ cofactors:", [e[0] for e in plus[:12]])
    except FileNotFoundError:
        print("Appendix C file not found at expected path")

if __name__ == "__main__":
    main()
