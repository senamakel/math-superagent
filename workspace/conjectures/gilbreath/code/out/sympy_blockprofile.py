import json
from sympy import find_linear_recurrence, symbols

data = json.load(open('code/out/blocks_depth1000.json'))
b = data['b']
n = symbols('n')
print("len b =", len(b))
for order in [3,4,5,6,8,10,12,15,20,30,40,50,60]:
    try:
        rec = find_linear_recurrence(b, n, order) if order <= 60 else None
        if rec:
            print(f"order {order}: FOUND", rec)
        else:
            print(f"order {order}: none")
    except Exception as e:
        print(f"order {order}: error {e}")
