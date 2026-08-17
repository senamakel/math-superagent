#!/usr/bin/env python3
"""Count the entries in Castryck et al.'s companion file badprimes7.txt (now held
at research/sources/castryck2012_badprimes7.txt.full.md as markdown-converted).

The paper's Theorem 4 states 366 bad primes for degree 7; de Frutos Marin's
thesis/abstract say 661.  This script counts the actual list mechanically
(no hand-counting) and takes the count as authoritative.

Reads the held .full.md file, extracts the primes between the first '[' and the
final '];', and reports:
  - the count N
  - whether the largest entry equals the 135-digit prime quoted in Thm 4
  - whether 7 is absent (the degree itself is good: Thm 4 says smallest
    non-bad prime apart from p=7 is 127)
  - whether 127 is absent (good) and all primes < 127 except 7 are present
  - N == 366 verdict against the arXiv Thm 4 statement
"""
import re
import sys
from pathlib import Path

SRC = Path("/workspace/research/sources/castryck2012_badprimes7.txt.full.md")

text = SRC.read_text(encoding="utf-8")
# List starts after "badprimes7 := [" and ends at the closing "];"
m = re.search(r"badprimes7\s*:=\s*\[(.*?)\];", text, re.S)
if not m:
    sys.exit("FAIL: could not locate the list in the file")
body = m.group(1)
primes = [int(p) for p in re.findall(r"\d+", body)]

print(f"COUNT: {len(primes)} primes in badprimes7.txt")

# largest entry vs the 135-digit prime quoted in Thm 4
quoted = 249847120216983926479165256672374830117371749836786068968700949838499096141806825287856933123954724798488422551659890912229726792102063
print(f"LARGEST == Thm4 quoted: {max(primes) == quoted}")
print(f"  largest is {max(primes)}")

# structural checks from Thm 4: smallest non-bad prime apart from 7 is 127
s = set(primes)
print(f"7 in list (should be False): {7 in s}")
print(f"127 in list (should be False): {127 in s}")
small_bad = [p for p in range(2, 127) if p in s]
print(f"bad primes < 127: {small_bad}")
print(f"count of bad primes < 127: {len(small_bad)}")
good_below_127 = [p for p in range(2, 127) if p not in s]
print(f"good primes (not in list) < 127: {good_below_127}")

# verdict against the two candidate counts
print()
print(f"VERDICT vs arXiv Thm 4 '366': {'MATCH' if len(primes) == 366 else 'MISMATCH'}")
print(f"VERDICT vs de Frutos '661':      {'MATCH' if len(primes) == 661 else 'MISMATCH'}")
print(f"ALL CHECKS PASSED: {len(primes) == 366 and 7 not in s and 127 not in s and max(primes) == quoted}")