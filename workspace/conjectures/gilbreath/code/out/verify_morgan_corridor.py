import json
from itertools import product

def frontier(row):
    for i in range(1, len(row)):
        if row[i] not in (0,2):
            return i
    return None

n_forces=0; bad=[]
for xs in product([0,2], repeat=7):
    x=[1]+list(xs)+[4]
    y=[abs(x[i]-x[i+1]) for i in range(len(x)-1)]
    z=[abs(y[i]-y[i+1]) for i in range(len(y)-1)]
    u=[abs(z[i]-z[i+1]) for i in range(len(z)-1)]
    v=[abs(u[i]-u[i+1]) for i in range(len(u)-1)]
    ok=(frontier(y)==7 and frontier(z)==6 and frontier(u)==5 and len(v)>=5 and v[4]==4)
    if ok:
        bad.append(xs)
    if xs[3]==0 and xs[4]==0 and xs[5]==0 and xs[6]==0:
        n_forces+=1

print("launchpads with x4=x5=x6=x7=0:", n_forces, "/ 128")
print("corridor-feeding launchpads:", len(bad))
viol=[b for b in bad if any(b[i]==2 for i in (3,4,5,6))]
print("corridor feeders with some x4..x7=2 (would refute forcing):", len(viol), viol[:5])
# all corridor feeders should have x4..x7=0
print("every corridor feeder has x4=x5=x6=x7=0:", all(all(b[i]==0 for i in (3,4,5,6)) for b in bad))

# real row 2
row2=[1,0,2,2,2,2,2,2,4]
print("real row2 x1..x7 =", row2[1:8], "-> x4..x7 =", row2[4:8])
print("row2 is a corridor feeder:", tuple(row2[1:8]) in [tuple(b) for b in bad])
