"""Verify corrected recurrences exactly (from exact structure.json S, P1, vR, N1)
and analyze N1 increments (Beatty), and the right-special factor structure."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "out", "structure.json")

st = json.load(open(DATA))
ks = sorted(int(k) for k in st)

def get(k):
    d = st[str(k)]
    return dict(Psi=d["Psi"], S=sum(d["values"]), N1=d["N1"],
                P1=d["P1"], vR=int(d["R"]))

# Corrected S recurrence
okS = True
fbad = []
for i in range(len(ks)-1):
    k = ks[i]
    a, b = get(k), get(ks[i+1])
    pred = 10*a["S"] + 10*a["vR"] + a["N1"]
    if pred != b["S"]:
        okS=False; fbad.append((k,pred,b["S"]))
print("S(k+1)=10S(k)+10vR+N1 holds exactly:", okS)
if fbad: print("bad:", fbad[:5])

# Psi extension holds exactly (already known)
okP = True
for i in range(len(ks)-1):
    k=ks[i]; a,b=get(k),get(ks[i+1])
    pred = 100*(a["Psi"]+a["vR"]**2)+20*a["P1"]+a["N1"]
    if pred != b["Psi"]:
        okP=False; print("Psi fail", k)
print("Psi extension holds exactly:", okP)

# N1 increments: Beatty? N1(k) ~ (number of length-k factors ending in 1).
inc = [get(ks[i+1])["N1"]-get(ks[i])["N1"] for i in range(len(ks)-1)]
from collections import Counter
c = Counter(inc)
print("N1 increments distribution:", dict(c))
print("density of +1:", sum(inc)/len(inc))
# Compare to alpha=1/phi^2. Hmm N1 roughly = floor(k*alpha)+? Let's see N1 vs floor(k*alpha)
import math
phi=(1+5**0.5)/2; alpha=1/phi**2
print("k, N1, floor(k*alpha), ceil?")
for k in range(1,41):
    n1=get(k)["N1"]
    print(k, n1, math.floor(k*alpha), int(math.floor(k*alpha)+alpha))
