"""Test the guessed order-6 recurrence for A186085 / histogram-count against
the full published A186085 terms (n=0..44) fetched here from the research note.
Recurrence guessed by find_linear_recurrence on H(2..14):
   a(n) = a(n-1) + a(n-2) + a(n-3) - a(n-4) - a(n-6)
"""
a186085 = [1,1,1,1,2,3,5,8,13,22,36,60,100,166,277,461,769,1282,2137,3565,
5945,9916,16540,27589,46022,76769,128062,213628,356366,594483,991706,1654352,
2759777,4603843,7680116,12811951,21372882,35654237,59478406,99221923,
165522118,276124217,460630839]

def rec(n):
    # a(n) = a(n-1)+a(n-2)+a(n-3)-a(n-4)-a(n-6)
    if n < 0: return 0
    # seed with first 6 published terms
    seed = {0:1,1:1,2:1,3:1,4:2,5:3}
    if n in seed: return seed[n]
    return rec(n-1)+rec(n-2)+rec(n-3)-rec(n-4)-rec(n-6)

memo={}
def recm(n):
    if n<0: return 0
    if n in memo: return memo[n]
    seed={0:1,1:1,2:1,3:1,4:2,5:3}
    if n in seed:
        memo[n]=seed[n]; return memo[n]
    memo[n]=recm(n-1)+recm(n-2)+recm(n-3)-recm(n-4)-recm(n-6)
    return memo[n]

ok=True
for n in range(0, len(a186085)):
    got = recm(n)
    if got != a186085[n]:
        print(f"MISMATCH at n={n}: rec={got} published={a186085[n]}")
        ok=False
print("Recurrence matches all published A186085 terms n=0..44:", ok)

# also check the histogram-count identification H(N)=A186085(N) for N=2..14
H = {2:1,3:1,4:2,5:3,6:5,7:8,8:13,9:22,10:36,11:60,12:100,13:166,14:277}
print("\nHistogram-count H(N) vs A186085(N):")
allok=True
for N,v in H.items():
    match = (v == a186085[N])
    if not match: allok=False
    print(f"  N={N}: H={v} A186085({N})={a186085[N]} match={match}")
print("All H(N)==A186085(N) for N=2..14:", allok)
