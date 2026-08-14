"""Print exact terms from the run's sequence files as JSON arrays, so the
sequence tools are fed exactly what the programs produced (no transcription).
Usage: python3 code/out/dump_terms.py [nterms]
"""
import json, sys

N = int(sys.argv[1]) if len(sys.argv) > 1 else 120
names = ["seq_H", "seq_A063985", "seq_Phi", "seq_phi", "seq_cototient"]
for name in names:
    with open(f"code/out/{name}.txt") as f:
        terms = [int(t) for t in f.read().split()]
    assert len(terms) >= N, (name, len(terms))
    print(name, "n_terms_on_disk =", len(terms))
    print(json.dumps(terms[:N]))
    print()
