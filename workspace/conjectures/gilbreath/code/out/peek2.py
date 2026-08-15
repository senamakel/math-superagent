def load(fn):
    with open("/workspace/code/out/pattern_finder_outputs/"+fn) as f:
        return [int(x) for x in f.read().split()]

for fn in ["d_first512","excess_e_first512","F_first512"]:
    s = load(fn+".txt")
    print(fn, "n=",len(s), "first8", s[:8], "min",min(s),"max",max(s))
