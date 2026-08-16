import json, sys
sys.path.insert(0, 'code')
from lib.primes import primes_mod4_string, h_string  # check names
print([n for n in dir(__import__('lib.primes', fromlist=['x'])) if not n.startswith('_')])
data = json.load(open('code/out/nu2_primes_xor_40000.json'))
print("data[32769] =", data[32769])