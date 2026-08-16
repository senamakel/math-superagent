from sympy import symbols
x = symbols('x')
# designed near-miss: mult 18 at 1 (covers 1..17), force j=18 share via root 1 mult 18
# but j=18 needs root shared; mult-18 covers only j=1..17, so add a second coincident
# root: (x-1)^19 would be trivial; use mult 18 + mult such that another root repeats
f = (x-1)**18 * (x-2)**2
