"""Generate exact nu2(n) (verified library oracle) and write term lists/files."""
import sympy, sys
from lib.supply_fold import s_sos, h_from_r

N = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
ps = list(sympy.primerange(1, 10**9))
q = ps[:N+1]
r = [x % 4 for x in q]
h = h_from_r(r)

nu2 = [0]*(N+1)
for n in range(2, N+1):
    _, ones = s_sos(n, h)
    nu2[n] = ones
assert nu2[53] == 18 and nu2[64] == 27 and nu2[4000] == 1975, nu2[53]
print("guards ok", flush=True)

import json
json.dump([nu2[n] for n in range(2, N+1)], open('code/out/pattern_nu2_verified.json','w'))
# text lists for the sequence tools
V = [nu2[n] for n in range(2, N+1)]
S = [(n-2)-2*nu2[n] for n in range(2, N+1)]
D = [S[i+1]-S[i] for i in range(len(S)-1)]
open('code/out/pattern_nu2_terms.txt','w').write(" ".join(map(str,V)))
open('code/out/pattern_S_terms.txt','w').write(" ".join(map(str,S)))
open('code/out/pattern_D_terms.txt','w').write(" ".join(map(str,D)))
print("wrote files; nu2 len", len(V), "S len", len(S), "D len", len(D))
print("nu2.first25", V[:25])
print("S.first25", S[:25])
print("D.first25", D[:25])
