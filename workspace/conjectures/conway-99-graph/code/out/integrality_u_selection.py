"""Find every u for which eigenvalue-multiplicity integrality passes in the
family srg(v,k,1,2), parametrized by k = u^2+u+2 (so sqrt(4k-7)=2u+1).

The multiplicity of the negative eigenvalue is
  g = 1/2 * [ (v-1) - (2k-(v-1))/(2u+1) ]
where v = 1 + k + k(k-2)/2.
Integrality: (2k-(v-1)) divisible by (2u+1) AND the resulting (v-1)-q even.

We scan u up to large and report exactly which u pass.  This is a search over
the DESCRIPTION length (u is an index into a closed-form family), not over the
answer space; it is verifying a claimed classification.
"""
def passes(u):
    k = u*u + u + 2
    v = 1 + k + k*(k-2)//2
    root = 2*u + 1
    num = 2*k - (v-1)
    if num % root != 0:
        return False
    q = num // root
    return ((v-1) - q) % 2 == 0

hits = []
for u in range(1, 2000):
    if passes(u):
        hits.append(u)
print("u passing integrality up to 2000:", hits)
print("count:", len(hits))

# The claimed five
claimed = [1, 3, 4, 10, 31]
print("claimed subset present:", all(u in hits for u in claimed))
print("any beyond the five among first 2000:", [u for u in hits if u not in claimed])

# Probe structure of {1,3,4,10,31} and candidate next terms under a few maps
seq = [1, 3, 4, 10, 31]
print("seq:", seq)
print("diffs:", [b-a for a,b in zip(seq, seq[1:])])
print("ratios:", [b/a for a,b in zip(seq, seq[1:])])
# Is there a relation u_{n+1} = u_n^2 ... ? 31 ~ 1+3+... no.
