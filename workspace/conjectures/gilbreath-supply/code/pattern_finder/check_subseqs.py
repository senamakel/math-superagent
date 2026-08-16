import json, sys
data = json.load(open('code/out/nu2_primes_xor_40000.json'))
# index -> n: determine convention. guards: nu2(53)=18, nu2(64)=27, nu2(4000)=1975, nu2(40000)=20081
# find index i where value==18 and others
for i,v in enumerate(data[:200]):
    if v==18:
        print("first 18 at index", i, "=> n =", i+2 if False else i) 
# brute: search for n mapping. Try convention n = i (1-based) and n = i+2
# just print candidates for value 18 within first 80
c18=[i for i,v in enumerate(data[:80]) if v==18]
c27=[i for i,v in enumerate(data[:90]) if v==27]
print("idx with 18:", c18[:6])
print("idx with 27:", c27[:6])