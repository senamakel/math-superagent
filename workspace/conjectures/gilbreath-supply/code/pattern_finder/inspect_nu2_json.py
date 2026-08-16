#!/usr/bin/env python3
"""Extract the dyadic subsequence nu2(2^k) from the canonical JSON, plus other
structured subsequences, and report exact values."""
import json, sys
sys.path.insert(0, "/workspace/code")

with open("/workspace/code/out/nu2_primes_xor_40000.json") as f:
    data = json.load(f)

# figure out the structure: could be list or dict
print("type:", type(data))
if isinstance(data, dict):
    keys = list(data.keys())[:5]
    print("sample keys:", keys)
    # try to get values
    vals = data.get("nu2") or data.get("values") or data
    if isinstance(vals, dict):
        # keyed by string n
        items = sorted((int(k), v) for k, v in vals.items())
        print("min n:", items[0][0], "max n:", items[-1][0], "count:", len(items))
    else:
        print("len:", len(vals))
elif isinstance(data, list):
    print("len:", len(data))
    print("first 5:", data[:5])
