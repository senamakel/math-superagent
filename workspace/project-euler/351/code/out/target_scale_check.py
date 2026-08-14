"""Target-scale application of the exact mod-12 / parity laws at n = 10^8.

The final answer H(10^8) = 11762187201804552 must satisfy, as an exact
consequence of the period-4 laws (which hold for every n >= 2 by the argument
phi(k) even for k >= 3):
  * n = 10^8 == 0 (mod 4)  =>  H(10^8) mod 12 == 0  and  A(10^8) even,
  * Phi(10^8) even (n >= 2).
This program checks those residues directly on the recorded final values.
"""
H = 11762187201804552
A = H // 6                     # A063985(10^8) = 1960364533634092
Phi = 10**8 * (10**8 + 1) // 2 - A

print("n = 10^8, n mod 4 =", 10**8 % 4)
print("H(10^8) mod 12 =", H % 12, "(law: 0 because n mod 4 == 0)")
print("A(10^8) mod 2  =", A % 2, "(law: 0 because n mod 4 == 0)")
print("Phi(10^8) mod 2 =", Phi % 2, "(law: 0 because n >= 2)")
print("H/6 integral:", H % 6 == 0)
print("all laws hold:", H % 12 == 0 and A % 2 == 0 and Phi % 2 == 0 and H % 6 == 0)
