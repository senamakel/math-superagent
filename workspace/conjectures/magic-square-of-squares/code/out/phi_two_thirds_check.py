#!/usr/bin/env python3
"""Check |Phi(B)| == (2/3) * S(B) where S(B)=sum phi(n), and the asymptotic.

Closed form: |Phi(B)| = sum_{M even<=B} phi(M) + (1/2) sum_{M odd<=B} phi(M).
Claim to test: is 3*|Phi(B)| == 2*S(B) exactly for all B, or only asymptotically?
"""
def phi_up_to(N):
    phi = list(range(N + 1))
    for p in range(2, N + 1):
        if phi[p] == p:
            for m in range(p, N + 1, p):
                phi[m] -= phi[m] // p
    return phi

B = 400000
phi = phi_up_to(B)
E = O = S = 0
exact_hits = 0
mism_shown = 0
for M in range(1, B+1):
    if M % 2 == 0:
        E += phi[M]
    else:
        O += phi[M]
    S += phi[M]
    Phi = 2*E + O          # = 2*|Phi|
    if Phi == 2*S and Phi % 3 == 0:
        exact_hits += 1
    # 3*|Phi| == 2*S  <=> 3*(2E+O)/2 == 2S  <=> 3(2E+O) == 4S
    if 3*(2*E + O) == 4*S:
        if mism_shown < 3:
            mism_shown += 1
    # rather track 2*|Phi| vs 4S/3
print("B max:", B)
# |Phi| = (2E+O)/2 ; asymptotic |Phi| ~ (2/3) S
Phi = (2*E + O)/2
print(f"B={B}: |Phi|={Phi:.0f}, S={S}, (2/3)S={2*S/3:.2f}, |Phi|/((2/3)S)={Phi/(2*S/3):.8f}")
