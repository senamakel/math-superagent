import json
D=json.load(open("out/exact_state_1_120.json"))
for k in range(1,31):
    d=D[str(k)]
    print(f"{k}: N1={d['N1']}, P1={d['P1']}, vR={d['vR']}")
