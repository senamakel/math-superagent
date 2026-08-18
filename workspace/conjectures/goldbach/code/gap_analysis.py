from pathlib import Path

fail=[302, 332, 458, 542, 632, 692, 872, 902, 1544, 1964, 2522, 2642, 2834, 4544, 4952, 6932, 7442, 9170, 11114, 11672, 12224, 13562, 17072, 22922, 34082, 34892, 35912]
g=[fail[i]-fail[i-1] for i in range(1,len(fail))]
print('gaps:',g)
print('gaps mod 6:',[x%6 for x in g])
print('gaps mod 30:',[x%30 for x in g])
print('gap==30 count:',g.count(30),'of',len(g))
print('gaps divisible by 30:',sum(1 for x in g if x%30==0),'of',len(g))
# cumulative distribution of gaps
from collections import Counter
c=Counter(g)
print('gap histogram:',sorted(c.items()))
# q+2 = 3t prime correlation: for failures, verify n-302 pattern? just print residues n mod 12
print('failures mod 12:',[n%12 for n in fail])
print('failures mod 30:',[n%30 for n in fail])
print('unique residues mod 30:',sorted(set(n%30 for n in fail)))
