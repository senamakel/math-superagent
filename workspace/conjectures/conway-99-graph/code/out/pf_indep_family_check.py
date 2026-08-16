"""Independent fresh check of the family-sequence catalogue for srg(v,k,1,2).

Feasible members from integer feasibility (a | 63): a=2u+1 in {3,7,9,21,63},
u in {1,3,4,10,31}, k=u^2+u+2, v=1+k^2/2.
Recover each family count from its closed form and run the sequence tools.
"""
u_list = [1, 3, 4, 10, 31]
k = [uu*uu + uu + 2 for uu in u_list]
v = [1 + kk*kk//2 for kk in k]

triangles = [v[i]*k[i]//6 for i in range(5)]
# coclique bound alpha = (u*k+2)/2
coclique = [(u_list[i]*k[i]+2)//2 for i in range(5)]
# pentagons = v*k*(k-2)*(k-4)/5
pents = [v[i]*k[i]*(k[i]-2)*(k[i]-4)//5 for i in range(5)]
# hexagons (induced C6) = v*k*(k-2)*(2k^2-21k+53)/12
hexs = [v[i]*k[i]*(k[i]-2)*(2*k[i]*k[i]-21*k[i]+53)//12 for i in range(5)]
# outer blocks = k(k-2)(k-4)/12
outer = [k[i]*(k[i]-2)*(k[i]-4)//12 for i in range(5)]
# distance-2 = k(k-2)/2
d2 = [k[i]*(k[i]-2)//2 for i in range(5)]
# n3 cap = v*k(k-2)/4
n3cap = [v[i]*k[i]*(k[i]-2)//4 for i in range(5)]
# number of lines (points x replication /3)
lines = [v[i]*7//3 for i in range(5)]  # replication k/2: v*(k/2)/3

print("u      =", u_list)
print("k      =", k)
print("v      =", v)
print("a      =", [2*uu+1 for uu in u_list])
print("tri    =", triangles)
print("lines  =", lines)
print("pent   =", pents)
print("hex    =", hexs)
print("outer  =", outer)
print("dist2  =", d2)
print("cocl   =", coclique)
print("n3cap  =", n3cap)
