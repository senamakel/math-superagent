"""Directly verify c0-odd and c2-odd counts over n=1..400 agree with prior run
(both reported 211), and confirm my incremental counter matches direct at 400.
Also print the full {#, difference} trajectory to show the 211=211 is a
crossing, not a regularity."""
import sys

def direct(N):
    a0 = a2 = 0
    traj = []
    for n in range(1, N+1):
        m = 2**n
        c0 = c1 = c2 = 0
        while m > 0:
            d = m % 3
            if d == 0: c0 += 1
            elif d == 1: c1 += 1
            else: c2 += 1
            m //= 3
        if c0 % 2: a0 += 1
        if c2 % 2: a2 += 1
        traj.append((n, a0, a2))
    return a0, a2, traj

N = 400
a0, a2, traj = direct(N)
print(f"N={N}: #c0odd={a0} #c2odd={a2} equal={a0==a2}")

# count how many n where a0==a2
eq = [n for (n,a,b) in traj if a==b]
print("n where a0==a2:", eq)
# also at 200
a0_200, a2_200, _ = direct(200)
print("N=200:", a0_200, a2_200, "equal:", a0_200==a2_200)

# verify incremental at 400 too
digits=[1]; ia0=ia2=0
for n in range(1,N+1):
    carry=0
    for i in range(len(digits)):
        v=digits[i]*2+carry; digits[i]=v%3; carry=v//3
    while carry: digits.append(carry%3); carry//=3
    c0=c1=c2=0
    for d in digits:
        if d==0:c0+=1
        elif d==1:c1+=1
        else:c2+=1
    if c0%2: ia0+=1
    if c2%2: ia2+=1
print("incremental at 400:", ia0, ia2, "matches direct:", (ia0,ia2)==(a0,a2))
