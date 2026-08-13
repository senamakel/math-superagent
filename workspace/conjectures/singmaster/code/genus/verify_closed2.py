# k2=5 rows from computed data
rows = [(5,2,2),(6,5,10),(7,5,12),(8,5,14),(9,5,16),(10,5,16),(11,5,20),(12,5,22),
        (13,5,24),(14,5,26),(15,5,26),(16,5,30),(17,5,32),(18,5,34),(19,5,36),(20,5,36),(21,5,40),(22,5,42),(23,5,44),(24,5,46)]
# (k1,k2=5): k1=5 exluded
# genera (k1,5) for k1=6..24: 10,12,14,16,16,20,22,24,26,26,30,32,34,36,36,40,42,44,46
G=[10,12,14,16,16,20,22,24,26,26,30,32,34,36,36,40,42,44,46]
K=range(6,25)
def g25(k1):
    # candidate: 2*floor((k1-1)/2)? check against data
    return 2*((k1-1)//2)
mism=[]
for k1,g in zip(K,G):
    if g25(k1)!=g: mism.append((k1,g,g25(k1)))
print("k2=5 candidate 2*floor((k1-1)/2): mismatches", mism if mism else "NONE")
# try from k2=5 row: note values increase ~2 per k1 but with stalls at k1=10,15,20 (multiples of 5)
# guess: g25(k1)=2(k1-3)+2=2k1-4 for non-multiples, 2k1-5 for multiples? check
def h25(k1):
    return (2*k1-4) if (k1%5!=0) else (2*k1-5)
mism=[]
for k1,g in zip(K,G):
    if h25(k1)!=g: mism.append((k1,g,h25(k1)))
print("k2=5 candidate 2k1-4 (/5:2k1-5):", mism if mism else "NONE")
print("verify the k2=5 data:", list(zip(K,G)))
