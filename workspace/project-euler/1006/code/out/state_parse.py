"""Correct parse of psi_state_1_200.txt: k,P_mod,S_mod,N1,N0,P1_mod,vR_mod."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
def load_state():
    data = {}
    with open(HERE + "/psi_state_1_200.txt") as f:
        f.readline()
        for line in f:
            p = line.strip().split(",")
            k = int(p[0]); data[k] = dict(
                P_mod=int(p[1]), S_mod=int(p[2]), N1=int(p[3]),
                N0=int(p[4]), P1_mod=int(p[5]), vR_mod=int(p[6]))
    return data

st = load_state()
ks = sorted(st)
print("header: k,P_mod,S_mod,N1,N0,P1_mod,vR_mod")
for k in [1,2,3,4,5,6,7,8,10,13,21]:
    d=st[k]
    print(k, d)
