"""Verify the Moore-bound lower bound on vertices of a min-degree>=3, girth>=9
graph, and on girth>=5. Standard Moore bound: with min degree d and girth g,
a BFS ball of radius floor((g-1)/2) around a vertex is a regular tree, giving
n >= 1 + d*sum_{i=0}^{r-1}(d-1)^i where r = floor((g-1)/2).
Here d=3.
"""
def moore(d, g):
    r = (g - 1) // 2
    return 1 + d * sum((d - 1) ** i for i in range(r))

for g in [5, 6, 7, 8, 9, 10, 11, 12]:
    print(f"girth>={g}: r=floor((g-1)/2)={ (g-1)//2 }, min n (d=3) = {moore(3,g)}")
