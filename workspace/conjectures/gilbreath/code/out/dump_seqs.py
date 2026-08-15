import json
base = "/workspace/code/out/pattern_finder_outputs/"
def read_lines(fn):
    with open(base+fn) as f:
        return [int(x) for x in f.read().split()]
b = read_lines("b_genuine.txt")
print("b count:", len(b))
# block profile first 161 genuine
print("BLOCK_PROFILE_GENUINE")
print(",".join(map(str,b)))
# growth: jumps (positive increments b_{k+1}-b_k)
diffs = [b[i+1]-b[i] for i in range(len(b)-1)]
print("positive jumps at:", [i+1 for i,d in enumerate(diffs) if d>0])
print("max b:", max(b), "at row", b.index(max(b))+1)
# ratio of consecutive local maxima b
# Let's also print NU2 and dev
for fn,lab in [("e_ballot_corrected_first512.txt","E-verified-corrected"),
               ("W_switch_prefix_first512.txt","W"),
               ("d_first512.txt","d")]:
    pass
