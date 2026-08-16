"""Reproduce the ABGS m=4 consecutive-prime-pair counts and the switch-density ratio,
the exact passage problem.md and the claim ledger cite.

Source: Ash-Beltis-Gross-Sinnott 2011, §7 table for m=4 over 10^3..10^6.
Four ordered pairs mod 4: (1,1) equal, (1,3) switch, (3,1) switch, (3,3) equal.
"""
counts = {(1,1): 16574, (1,3): 22521, (3,1): 22520, (3,3): 16715}
total = sum(counts.values())
switch = counts[(1,3)] + counts[(3,1)]
equal  = counts[(1,1)] + counts[(3,3)]

print("total pairs:", total)
print(f"switch (1,3)+(3,1) = {switch}  = {100*switch/total:.3f}%")
print(f"equal  (1,1)+(3,3) = {equal}   = {100*equal/total:.3f}%")
print(f"switch/equal ratio = {switch/equal:.4f}")
print(f"largest/smallest = {max(counts.values())/min(counts.values()):.4f}")
print("\nEach count vs fair share (total/4 = %.1f):" % (total/4))
for k in [(1,1),(1,3),(3,1),(3,3)]:
    print(f"  {k}: {counts[k]:6d}  dev {counts[k]-total/4:+.1f} "
          f"({100*counts[k]/total-25:+.2f}%)")
