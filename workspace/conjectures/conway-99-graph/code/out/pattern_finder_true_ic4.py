# True induced-C4 family sequence over the mu=2 sub-family:
# induced C4 = #nonedges/2 = v*k(k-2)/8  (proved from c7 + double-counting).
# The capture induced_C4_family.py labels v*k(k-2)/4 (=nonedges) as "ic4" -- MISLABEL.
# Correct genuine induced-C4 sequence:
ks = [4,14,22,112,994]
true_ic4 = []
nonedges = []
for k in ks:
    v = 1 + k*k//2
    ne = v*(v-1-k)//2          # = v*k(k-2)/4
    nonedges.append(ne)
    true_ic4.append(ne//2)     # induced C4
print("k                ", ks)
print("nonedges vk(k-2)/4", nonedges)
print("true induced C4   ", true_ic4)
print("(capture label 'ic4' should read 'nonedges'; true ic4 = nonedges/2)")
