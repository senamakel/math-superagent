from lib.es_construct import es_set_blocks
from fractions import Fraction
pts, blocks = es_set_blocks(7)
print("N =", len(pts))
for b, blk in enumerate(blocks):
    print("block", b, "size", len(blk), "first pt", blk[0], "last pt", blk[-1])
# flat index -> block
mp = []
for b, blk in enumerate(blocks):
    for _ in blk:
        mp.append(b)
print("index->block:", mp)
print("claim L = [1,2,3,4,5,16..26]", len([1,2,3,4,5]+list(range(16,27))))
print("claim R = [0,6..15,27..31]", len([0]+list(range(6,16))+list(range(27,32))))
