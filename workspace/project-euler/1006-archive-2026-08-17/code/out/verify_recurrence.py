"""Verify the extension recurrence mod M over all available transitions, and
analyze state sequences for recurrences."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
MOD = 101001001

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

# Verify extension recurrence mod M: Psi(k+1) = 100(Psi(k)+vR^2)+20 P1 + N1
ok = True
bad = []
for k in ks[:-1]:
    pred = (100 * (st[k]["P_mod"] + st[k]["vR_mod"]**2) + 20*st[k]["P1_mod"] + st[k]["N1"]) % MOD
    if pred != st[k+1]["P_mod"]:
        ok = False; bad.append((k, pred, st[k+1]["P_mod"]))
print("Extension recurrence holds mod M for all transitions 1..199:", ok)
if bad: print("first bad:", bad[:5])

# Check similar recurrence for S (sum of values): S evolves how?
# S(k+1) = 10*(S(k) + vR) + N1  ?  Let's test: each factor extends by 0 (val*10) or by 1 (val*10+1).
# S(k+1) = 10*(sum over all w of v_w) + 10*vR_extra + N1
# Every factor extends exactly one way except right-special (extends both).
# So S(k+1) = 10*S(k) + (N1 + N0 contributions). Each factor w extends to w0 (val*10) always (all factors end-extend by 0?).
# Actually every factor extends by '0' (since every factor avoids "11"? no). Let's just test empirically.
# hypo: S(k+1) = 10*S(k) + N1  (each w1 contributes +1)
# and the w0 factors contribute 10*v. Every factor extends by 0 => counts (k+1) factors contributing 10*v each => 10*S(k).
# Plus those that extend by 1 contribute an extra 1 each => +N1.
# Wait but right-special extends both, so its w0 copy gives 10vR (already in 10*S) and its w1 gives 10vR+1.
# Every non-special factor extends exactly one way: those that extend by 0 give 10v, those by 1 give 10v+1.
# Sum = sum over w0-extenders of 10v + sum over w1-extenders of (10v+1)
#      = 10*S + (count of 1-extenders)   -- because 10*S covers all factors once, and 1-extenders get one more +1.
# Hmm: S(k+1) = sum over all length-(k+1) factors of value.
# Let each factor w: 10v(w) appears once for its extension by 0 (if extends by 0) or by 1 via 10v+1.
# = sum_w 10 v(w) [every w appears in S(k+1) once via SOME extension] + (number of 1-extensions) *1
# But every w extends: by 0 (giving 10v) and some also by 1 (giving 10v+1, i.e. one extra +1).
# The w0 copy is in S(k+1) and w1 copy too if it exists. So sum = 10*sum_w v + (extensions by 1 count) = 10*S + N1.
# But careful each w contributes a factor to S(k+1) for EACH extension.
okS = True
for k in ks[:-1]:
    pred = (10*st[k]["S_mod"] + st[k]["N1"]) % MOD
    if pred != st[k+1]["S_mod"]:
        okS = False; print("S fail k=",k, pred, st[k+1]["S_mod"])
print("S recurrence S(k+1)=10*S(k)+N1 holds mod M:", okS)

# Test P1 / vR recurrences?
# Examine N1 sequence structure: N1(k) increments by 0/1. Plot increments.
inc = [st[k+1]["N1"]-st[k]["N1"] for k in ks[:-1]]
print("N1 increment density:", sum(inc)/len(inc))
# Is N1(k) = number of length-k factors ending in 1?
# In Sturmian word, count of factors ending in '1'... Let's just record.
# Check: does N1(k) relate to floor((k+1)*alpha)?
import math
phi = (1+5**0.5)/2
alpha = 1/phi**2
print("N1 exact first 60:", [st[k]["N1"] for k in range(1,61)])
