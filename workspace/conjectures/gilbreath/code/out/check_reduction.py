"""Check the Gilbreath reduction against the real rows — PENDING (no exec tool).

This run had no exec tool, so this was NOT run. witnesses.json already reports
the same facts in aggregate (leading_entry_is_1, second_entry_always_0_or_2
true over depth_verified=600); this makes them per-row. Run with:
    timeout 540 python3 check_reduction.py 2>&1 | tee check_reduction.captured.txt
"""
import json

with open("witnesses.json") as f:
    W = json.load(f)

def sieve(n):
    s = bytearray(b"\x01") * (n + 1)
    s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i*i:n+1:i] = b"\x00" * (((n - i*i)//i) + 1)
    return [i for i in range(n + 1) if s[i]]

LIMIT = 400000
depth = 600
row = sieve(LIMIT)
checked_shape, checked_iff, first_bad = True, True, None
for k in range(depth):
    nxt = [abs(row[i+1] - row[i]) for i in range(len(row) - 1)]
    if k >= 1 and (nxt[0] % 2 == 0 or any(e % 2 for e in nxt[1:])):
        checked_shape, first_bad = False, ("shape", k); break
    if k >= 1 and len(row) >= 2 and ((nxt[0] == 1) != (row[1] in (0, 2))):
        checked_iff, first_bad = False, ("iff", k); break
    row = nxt

print("shape_preserved_(odd,even,even,...)_for_all_k_ge_1:", checked_shape)
print("iff_A(k+1,0)==1 <-> A(k,1) in {0,2}:", checked_iff)
print("first_bad:", first_bad, "| rows_checked:", depth - 1)
print("witnesses.json aggregate:", W["leading_entry_is_1_for_all_k"],
      W["second_entry_always_0_or_2"])
