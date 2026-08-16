#!/usr/bin/env python3
"""Generate the candidate module pool for the es-nogon scored search.

Writes `candidates/c_<name>.py` modules, each exposing `points(k)`.

Families (each module's `points` then has its own deterministic behaviour):
  A. ES intics / affine / integerization variants. These are affine or scaling
     images of the verified ES no-convex-k set, so they preserve general
     position and the no-convex-k property at the *same* size (16@k=6, 32@k=7)
     — they certify that the scorer's 16/32 baseline is stable under the whole
     affine group (a strong check of the scorer, not of ES(7)).
  B. Perturbed ES sets: the ES set with a few points nudged by a small integer
     vector. Perturbation generally destroys the no-k-gon, so the certified
     score drops — this measures robustness.
  C. Subsets / enlargements of ES (drop points, or ES capped to a size < rung).
  D. Random small integer sets in a box, various sizes (mostly low score).
  E. Convex-layered sets of controlled layer size (a distinct construction).

Every module does deterministic, exact-integer work only.  The names are
exported in a manifest written to candidates/MANIFEST.py so the driver can
import them.
"""

import random
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)  # ensure _base importable when run standalone
from _base import es_int, affine, to_ints

from lib.es_construct import es_set


def write(module_id, body):
    path = os.path.join(HERE, "c_%s.py" % module_id)
    head = (
        '"""Auto-generated candidate module: %s."""\n'
        "import math\n"
        "from fractions import Fraction\n"
        "from lib.es_construct import es_set\n\n"
        "def _to_int(points):\n"
        "    if not points: return []\n"
        "    den=1\n"
        "    for (x,y) in points:\n"
        "        den=math.lcm(den,Fraction(x).denominator)\n"
        "        den=math.lcm(den,Fraction(y).denominator)\n"
        "    return [(Fraction(x).numerator*(den//Fraction(x).denominator),\n"
        "             Fraction(y).numerator*(den//Fraction(y).denominator))\n"
        "            for (x,y) in points]\n"
        "def _es_int(k):\n"
        "    return _to_int(es_set(k))\n"
        "def _aff(pts,a,b,c,d,e,f):\n"
        "    return [(a*x+b*y+c, d*x+e*y+f) for (x,y) in pts]\n"
    ) % module_id
    with open(path, "w") as f:
        f.write(head)
        f.write(body)
        f.write("\n\nif __name__ == '__main__':\n    import sys\n")
        f.write("    k=int(sys.argv[1]) if len(sys.argv)>1 else 7\n")
        f.write("    print('points(%d)->%d'%(k,len(points(k))))\n")
    return module_id


NAMES = []

# ---------------- Family A: ES affine / scaling variants --------------------
# each names the transform; all preserve size (so they certify same score).
_A = [
    ("es_mirror_x", "[( -x, y) for (x,y) in _es_int(k)]"),
    ("es_mirror_y", "[( x,-y) for (x,y) in _es_int(k)]"),
    ("es_origin_flip", "[( -x,-y) for (x,y) in _es_int(k)]"),
    ("es_transpose", "[( y, x) for (x,y) in _es_int(k)]"),
    ("es_transpose_neg", "[( -y,-x) for (x,y) in _es_int(k)]"),
    ("es_swap_neg_y", "[( y,-x) for (x,y) in _es_int(k)]"),
    ("es_rot90", "[( -y, x) for (x,y) in _es_int(k)]"),
    ("es_rot180", "[( -x,-y) for (x,y) in _es_int(k)]"),
    ("es_shear_x", "[(x+3*y, y) for (x,y) in _es_int(k)]"),
    ("es_shear_y", "[(x, 2*x+y) for (x,y) in _es_int(k)]"),
    ("es_scale2", "[(2*x, 2*y) for (x,y) in _es_int(k)]"),
    ("es_scale3", "[(3*x, 3*y) for (x,y) in _es_int(k)]"),
    ("es_scale5", "[(5*x, 5*y) for (x,y) in _es_int(k)]"),
    ("es_xscale_yscale", "[(4*x, 7*y) for (x,y) in _es_int(k)]"),
    ("es_aff11", "_aff(_es_int(k), 1,2,100, 3,1,-50)"),
    ("es_aff12", "_aff(_es_int(k), 2,-1,0, 1,3,0)"),
    ("es_translate", "[(x-100000, y+200000) for (x,y) in _es_int(k)]"),
    ("es_refl_diag", "[(x+y, x-y) for (x,y) in _es_int(k)]"),
    ("es_persp_x", "[(7*x - 3*y, x + 2*y) for (x,y) in _es_int(k)]"),
    ("es_bigscale", "[(123*x, 456*y) for (x,y) in _es_int(k)]"),
]
for name, expr in _A:
    write(name, "def points(k):\n    return %s\n" % expr)
    NAMES.append(name)

# ---------------- Family B: perturbed ES sets ----------------------------
# deterministic pseudo-perturbations; keep exact ints.
_rng = random.Random(20240607)


def perturbed_points(k, n_flip, mag):
    base = es_int(k)
    idx = list(range(len(base)))
    _rng.shuffle(idx)
    out = list(base)
    for i in idx[:n_flip]:
        x, y = out[i]
        dx = _rng.randint(-mag, mag)
        dy = _rng.randint(-mag, mag)
        out[i] = (x + dx, y + dy)
    return out


_B = [
    ("es_perturb1", "perturbed_points(k,1,3)"),
    ("es_perturb2", "perturbed_points(k,2,3)"),
    ("es_perturb3", "perturbed_points(k,3,3)"),
    ("es_perturb4", "perturbed_points(k,4,2)"),
    ("es_perturb5", "perturbed_points(k,5,1)"),
    ("es_perturb6", "perturbed_points(k,2,10)"),
    ("es_perturb7", "perturbed_points(k,1,50)"),
    ("es_perturb8", "perturbed_points(k,6,5)"),
]
for name, expr in _B:
    write(name, "def perturbed_points(k,n_flip,mag):\n"
                "    import random\n"
                "    r=random.Random('%s')\n"
                "    base=_es_int(k); idx=list(range(len(base))); r.shuffle(idx)\n"
                "    out=list(base)\n"
                "    for i in idx[:n_flip]:\n"
                "        x,y=out[i]; out[i]=(x+r.randint(-mag,mag), y+r.randint(-mag,mag))\n"
                "    return out\n"
                "def points(k):\n    return %s\n" % (name, expr))
    NAMES.append(name)

# ---------------- Family C: subsets / capped ES ---------------------------
_C = [
    ("es_cap_6", "_es_int(k)[:16]"),
    ("es_cap_12", "_es_int(k)[:12]"),
    ("es_cap_20", "_es_int(k)[:20]"),
    ("es_cap_28", "_es_int(k)[:28]"),
    ("es_drop_2", "_es_int(k)[:-2]"),
    ("es_drop_4", "_es_int(k)[:-4]"),
    ("es_first_half", "_es_int(k)[:len(_es_int(k))//2]"),
]
for name, expr in _C:
    write(name, "def points(k):\n    return %s\n" % expr)
    NAMES.append(name)

# ---------------- Family D: random small integer sets ----------------------
_D = [
    ("rand_box_10", 10, 1000),
    ("rand_box_12", 12, 1000),
    ("rand_box_14", 14, 1000),
    ("rand_box_16", 16, 5000),
    ("rand_box_20", 20, 5000),
    ("rand_box_24", 24, 5000),
    ("rand_box_28", 28, 5000),
    ("rand_box_32", 32, 5000),
    ("rand_dense_12", 12, 200),
    ("rand_dense_16", 16, 300),
    ("rand_ellipse_14", 14, 0),
    ("rand_ellipse_16", 16, 0),
]
for name, sz, box in _D:
    if name.startswith("rand_ellipse"):
        # points on narrow ellipse -> tends to convex / layered
        w = box if box else 1
        seed = hash(name) % 10 ** 9
        body = (
            "def points(k):\n"
            "    import random\n"
            "    r=random.Random(%d)\n"
            "    out=[]; s=set()\n"
            "    while len(out)<%d:\n"
            "        t=r.random()\n"
            "        x=int(1000*(r.random()-0.5)); y=int(40*(r.random()-0.5))\n"
            "        p=(x,y)\n"
            "        if p not in s:\n"
            "            s.add(p); out.append(p)\n"
            "    return out\n" % (seed, sz)
        )
    else:
        seed = hash(name) % 10 ** 9
        body = (
            "def points(k):\n"
            "    import random\n"
            "    r=random.Random(%d)\n"
            "    out=[]; s=set()\n"
            "    while len(out)<%d:\n"
            "        p=(r.randint(0,%d), r.randint(0,%d))\n"
            "        if p not in s:\n"
            "            s.add(p); out.append(p)\n"
            "    return out\n" % (seed, sz, box, box)
        )
    write(name, body)
    NAMES.append(name)

# ---------------- Family E: convex-layered sets ----------------------------
# Build a set whose onion layers each have < k points but a substantial total.
# Points placed deterministically on a sequence of increasing-radius concentric
# regular polygons (integer coords via rounding) -- a genuine alternative
# construction with no huge hull layer.

def layered_points(total, per_layer):
    import math
    pts = []
    layer = 0
    rng = random.Random(999)
    while len(pts) < total:
        n = per_layer
        R = 10 * (layer + 1)
        ang0 = rng.random() * (2 * math.pi)
        for i in range(n):
            a = ang0 + 2 * math.pi * i / n + (layer % 2) * (math.pi / n)
            x = int(R * math.cos(a))
            y = int(R * math.sin(a))
            pts.append((x, y))
        layer += 1
    return pts[:total]


_E = [
    ("layered_per3_24", 24, 3),
    ("layered_per3_30", 30, 3),
    ("layered_per4_28", 28, 4),
    ("layered_per4_32", 32, 4),
    ("layered_per5_25", 25, 5),
    ("layered_per5_30", 30, 5),
]
for name, tot, per in _E:
    body = (
        "def points(k):\n"
        "    import math, random\n"
        "    r=random.Random('%s')\n"
        "    pts=[]; layer=0\n"
        "    while len(pts)<%d:\n"
        "        R=10*(layer+1)\n"
        "        ang0=r.random()*2*math.pi\n"
        "        n=%d\n"
        "        for i in range(n):\n"
        "            a=ang0+2*math.pi*i/n+(layer%%2)*(math.pi/n)\n"
        "            pts.append((int(R*math.cos(a)), int(R*math.sin(a))))\n"
        "        layer+=1\n"
        "    return pts[:%d]\n" % (name, tot, per, tot)
    )
    write(name, body)
    NAMES.append(name)

# ---------------- manifest -------------------------------
with open(os.path.join(HERE, "MANIFEST.py"), "w") as f:
    f.write("NAMES = %r\n" % NAMES)
print("wrote %d candidate modules" % len(NAMES))
print(NAMES)
