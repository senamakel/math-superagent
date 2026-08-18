"""Probe for additional exact low-modulus regularities in Psi(k), using the validated
right-extension recurrence pipeline (Psi(1)=1; Psi(k+1)=100Psi(k)+100V^2+20S1(k)+c1(k+1)).
Check Psi(k) mod 2^a, 5^a, and a few small moduli for patterns in k.
Goal: find cross-check regularities like the mod-100 one (Psi(k)=c1(k) mod 100 = 52 at k=10^18).
"""
import mpmath as mp
mp.mp.dps = 80
PHI2_INV = mp.mpf(1) / ((1 + mp.sqrt(5)) / 2) ** 2

def c1(k):
    return 1 + int(mp.floor(k * PHI2_INV))

def load_pairs(path):
    out = {}
    for line in open(path):
        p = line.split()
        if len(p) >= 2:
            out[int(p[0])] = int(p[1])
    return out

vR = load_pairs("code/out/vR_exact.txt")
s1 = load_pairs("code/out/s1_exact.txt")
K = 3000
Psi = {1: 1}
for k in range(1, K):
    Psi[k+1] = 100*Psi[k] + 100*vR[k]**2 + 20*s1[k] + c1(k+1)

def pattern(mod, label):
    """Report whether Psi(k) mod mod equals some function of k we can identify.
    Just print a table of Psi(k) mod mod for k=1..30 and check if constant/repeating."""
    vals = [Psi[k] % mod for k in range(1, 31)]
    print(f"{label}: Psi(k) mod {mod}, k=1..30:", vals)

for a in [1,2,3,4,5,6,7,8]:
    pattern(2**a, f"2^{a}")
for a in [1,2,3,4]:
    pattern(5**a, f"5^{a}")
for mod in [8, 16, 32, 7, 11, 13]:
    pattern(mod, f"mod{mod}")

# Check specific structural questions:
# (1) Psi(k) mod 4? mod 8?  Since Psi(k) = c1(k) mod 100, and 100 | 20*... 
# (2) Is Psi(k) even/odd pattern?
print("\nPsi(k) parity k=1..20:", [Psi[k] % 2 for k in range(1,21)])
print("c1(k) parity k=1..20:", [c1(k) % 2 for k in range(1,21)])
# (3) Psi(k) mod 100 already equals c1(k); what about mod 4 forcing?
print("Psi mod 4 equals c1 mod 4 (since 100 mod 4=0 chain):",
      all(Psi[k] % 4 == c1(k) % 4 for k in range(1, K+1)))
print("Psi mod 8 equals c1 mod 8 ?:",
      all(Psi[k] % 8 == c1(k) % 8 for k in range(1, K+1)))
print("Psi mod 16 equals c1 mod 16 ?:",
      all(Psi[k] % 16 == c1(k) % 16 for k in range(1, K+1)))
