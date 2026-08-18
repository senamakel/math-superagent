#!/usr/bin/env python3
"""One-shot inspection of the focal_6coeff checkpoint (no source modified)."""
import json

data = json.load(open("code/out/.focal_6coeff_state.json"))
print("done_through:", data["done_through"])
print("total_elapsed:", data["total_elapsed"])
print("V keys:", sorted(int(k) for k in data["V"].keys()))
for k in sorted(int(k) for k in data["wall"].keys()):
    print("  degree %d: wall %.1fs" % (k, data["wall"][str(k)]))
