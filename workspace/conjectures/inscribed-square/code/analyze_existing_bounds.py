from fractions import Fraction

# Exact bounds emitted by check_oracle.py for a=2 and n divisible by 4.
ns = [8, 12, 16, 20, 24, 32]
bounds = [Fraction(4, n) / (1 + Fraction(4, n*n)) for n in ns]
# Same expression in reduced integer form: 8n/(n^2+4).
print('n:', ns)
print('bounds:', [str(x) for x in bounds])
print('numerators:', [x.numerator for x in bounds])
print('denominators:', [x.denominator for x in bounds])
print('strictly_decreasing:', all(bounds[i] > bounds[i+1] for i in range(len(bounds)-1)))
