"""Independent extraction of core SUPPLY sequences from the canonical JSON,
with guard verification, to feed the exact sequence tools.

JSON d[i] = nu2(i+1) per the authoritative pattern-finder deliverables
(guard claims: nu2(53)=18 -> d[52], nu2(64)=27 -> d[63], nu2(4000)=1975 ->
d[3999]).  I re-verify these guards here before trusting any term.
"""
import json

d = json.load(open('/workspace/code/out/nu2_primes_xor_40000.json'))
print("json length", len(d))
# JSON is indexed d[i] = nu2(i) directly (index == n): probes show value 18 at
# index 53, 27 at 64, 1975 at 4000, 20081 at 40000.
assert d[53] == 18, d[53]
assert d[64] == 27, d[64]
assert d[4000] == 1975, d[4000]
assert d[40000] == 20081, d[40000]
print("guards nu2(53)=18, nu2(64)=27, nu2(4000)=1975, nu2(40000)=20081 all pass")

# nu2(n) for n=2.. : d[i]=nu2(i)  =>  nu2(n)=d[n]
nu2 = [d[n] for n in range(2, 40001)]
S = [(n-2) - 2*d[n] for n in range(2, 40001)]

def dump(name, L, K):
    with open(f'/tmp/{name}.py.txt', 'w') as f:
        f.write(f"{name} = {L[:K]}")

dump('nu2', nu2, 400)
dump('S',   S,   400)
print("nu2 first 24 (n=2..25):", nu2[:24])
print("S   first 24 (n=2..25):", S[:24])
# identity 2*nu2-(n-2) == -S check
ok = all(2*nu2[i] - ((i+2)-2) == -S[i] for i in range(len(nu2)))
print("identity 2*nu2-(n-2)=-S holds for all n in [2,40000]:", ok)
# S parity
ok2 = all(S[i] % 2 == ((i+2)-2) % 2 for i in range(len(S)))
print("S(n) = n-2 mod 2 for all n:", ok2)
# D increment always odd
D = [S[i+1]-S[i] for i in range(len(S)-1)]
print("D(n)=S(n+1)-S(n) always odd:", all(x % 2 == 1 for x in D))

# nu2(2^k) k=3..15 : nu2(n)=d[n], n=2^k
dy = [d[(1<<k)] for k in range(3, 16)]
print("nu2(2^k) k=3..15:", dy)

# nu2 at n = 2^k+1
print("nu2(2^k+1) k=3..15:", [d[(1<<k)+1] for k in range(3, 16)])
