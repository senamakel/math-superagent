"""Quick check that the canonical A007902 recurrence in lib/amoeba2d.G
reproduces the 2D amoeba counts a(n) = A007902(n+1).  Imports the single
shared definition from lib/amoeba2d instead of a local copy."""
from lib.amoeba2d import a

expected = [1, 1, 2, 4, 9, 20, 46, 105, 243, 561, 1301, 3014, 6995, 16227, 37668]
got = [a(n) for n in range(1, 16)]
print("recurrence:  ", got)
print("expected(N+1):", expected)
print("MATCH" if got == expected else "MISMATCH")
