"""Emit the srg(v,k,1,2) family sequences fresh from the closed forms, for
independent re-check by the sequence tools. Exact integers only.
u in {1,3,4,10,31}, k=u^2+u+2, v=1+k^2/2, a=2u+1 | 63.
"""
u_list = [1, 3, 4, 10, 31]

def seq_for(name):
    out = []
    for u in u_list:
        k = u*u + u + 2
        v = 1 + k*k//2
        a = 2*u + 1
        s = -(u+1)
        r = u
        T = v*k//6                     # triangles
        p5 = v*k*(k-2)*(k-4)//5        # pentagons
        hx = v*k*(k-2)*(2*k*k-21*k+53)//12   # hexagon base (n3=0 term)
        ob = k*(k-2)*(k-4)//12         # outer blocks
        d2 = k*(k-2)//2                # distance-2 vertices
        coc = (u*k+2)//2               # coclique bound (u*k+2)/2
        n3cap = k*(k-2)*(k*k+2)//8     # n3 cap for k>=6
        m_r = u*(u*u+u+2)*(u*u+2*u+3)//(2*(2*u+1))
        m_s = (u+1)*(u*u+2)*(u*u+u+2)//(2*(2*u+1))
        out.append((u,k,v, a, T, p5, hx, ob, d2, coc, n3cap, m_r, m_s))
    return out

rows = seq_for("x")
names = ["u","k","v","a","T","p5","hx","ob","d2","coc","n3cap","m_r","m_s"]
print("   ".join(f"{n:>8}" for n in names))
for row in rows:
    print("   ".join(f"{x:>8}" for x in row))
print()
# Print each sequence as a comma list for feeding to the tools
for j,name in enumerate(names):
    print(name, ":", ",".join(str(r[j]) for r in rows))
