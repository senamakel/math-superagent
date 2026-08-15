from lib.gilbreath import primes_up_to
P = primes_up_to(1_000_000)
hbits=[((P[i+1]-P[i])//2)%2 for i in range(len(P)-1)]
pref=[0]*(len(hbits)+1)
for i,bw in enumerate(hbits): pref[i+1]=pref[i]+bw
print("W_FIRST_100")
print(",".join(str(pref[n]-pref[2]) for n in range(2,102)))
