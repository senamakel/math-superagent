import json
data = json.load(open('/workspace/code/out/blocks_depth1000.json'))
b = data['b']
print("total", len(b))
# print first 512
print(",".join(str(x) for x in b[:512]))
