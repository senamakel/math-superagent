#!/usr/bin/env python3
"""Consolidated refutation script for the ONE established result.

Refutation (see research/notes/refute_single_boundary_one.md, claim
`single-boundary-one-refutes-switch-equivalence-as-stated`):

  The literal windowed form of G-sup-implies-switch, and the unqualified
  R-switch-equivalence, are FALSE. The per-window family h = e_{n-1} -- a
  single 1 at the window's final index n-1, zeros elsewhere -- has switch
  density -> 0, yet

      nu2(n) = wt(Phi_n h) = n - 2 = Theta(n),

  i.e. a sparse single 1 at the shared boundary feeds every depth.

Why it is structurally true: the depth-d diagonal cell is

      T(n,d) = XOR over bitwise submasks o of d of  h[n-1-d+o].

  For every d in [2, n-1], the offset o = d is a bitwise submask of d and
  lands on the final index n-1, where h = 1. Hence T(n,d) = 1 for all n-2
  depths and nu2(n) = n-2. The switch density (fraction of 1s in the window
  away from the amplified boundary spike) is 0.

This script:
  * sweeps n = 4..12 for h = e_{n-1}, computes nu2(n) by the exact
    submask-XOR fold (lib.supply_fold.s_sos, checked against the direct
    oracle t_direct), and reports nu2, nu2/n, and switch density.
  * prints a NEGATIVE CONTROL h = e_0 (a single 1 at the FIRST index), which
    must NOT give the same linear weight -- the boundary-spike mechanism is
    the cause, not "a single 1 anywhere".
  * writes the sweep to code/out/refute_single_boundary_sweep.txt.

All arithmetic exact; only the density ratios are floats.
"""
import os

from lib.supply_fold import t_direct, s_sos


def single_one(n, j):
    """Length-n string h = e_j: a single 1 at index j, zeros elsewhere."""
    h = [0] * n
    h[j] = 1
    return h


def nu2_exact(n, h):
    """nu2(n) = #{ d in [2, n-1] : T(n,d) = 1 }.

    Computed by the O(n log n) submask-product SOS transform and verified
    against the direct submask-XOR oracle. Returns (nu2, ones_sos) identical.
    """
    S, ones = s_sos(n, h)
    # cross-check against the literal oracle on every row (cheap at n<=12)
    ones_direct = sum(t_direct(n, d, h) for d in range(2, n))
    assert ones == ones_direct, (n, ones, ones_direct)
    return ones


def switch_density_excluding_boundary(n, h):
    """Fraction of 1s in the window away from the amplified final index.

    The depth-d diagonal always reads the window's final index n-1 (offset
    o = d, always a submask of d). That single spike is the amplification
    mechanism; stripping it leaves the "true" switch density, which is what
    the refutation says is ~0. Exact count over h[0..n-2], divided by (n-1).
    """
    nonboundary = sum(h[i] for i in range(0, n - 1))
    return nonboundary / (n - 1) if n > 1 else 0.0


def window_density(n, h):
    """Raw fraction of 1s across the whole window h[0..n-1]."""
    return sum(h) / n


def run_sweep(nlo=4, nhi=12):
    """Sweep n = nlo..nhi for the positive (boundary spike) and negative
    (first-index) cases. Returns list of dicts and a multiline table."""
    rows = []
    for n in range(nlo, nhi + 1):
        pos = single_one(n, n - 1)          # the witness: e_{n-1}
        neg = single_one(n, 0)              # negative control: e_0
        nu2_pos = nu2_exact(n, pos)
        nu2_neg = nu2_exact(n, neg)
        rows.append(dict(
            n=n,
            nu2_pos=nu2_pos,
            nu2_n_pos=nu2_pos / (n - 2) if n > 2 else 0.0,
            switch_pos=switch_density_excluding_boundary(n, pos),
            nu2_neg=nu2_neg,
            nu2_n_neg=nu2_neg / (n - 2) if n > 2 else 0.0,
            switch_neg=switch_density_excluding_boundary(n, neg),
        ))
    return rows


def format_table(rows):
    lines = []
    lines.append("n    nu2(e_{n-1})  nu2/n(pos)  switch_density(pos)  "
                 "nu2(e_0)  nu2/n(neg)  switch_density(neg)")
    for r in rows:
        lines.append(
            f"{r['n']:>3}  {r['nu2_pos']:>11}  {r['nu2_n_pos']:>9.3f}  "
            f"{r['switch_pos']:>19.3f}  {r['nu2_neg']:>7}  "
            f"{r['nu2_n_neg']:>9.3f}  {r['switch_neg']:>18.3f}"
        )
    return "\n".join(lines)


def header():
    return (
        "REFUTATION (confirmed, single established result):\n"
        "  the literal windowed form of G-sup-implies-switch, and the\n"
        "  unqualified R-switch-equivalence, are FALSE.\n"
        "  Witness family h = e_{n-1}: a single 1 at the window's final\n"
        "  index n-1, zeros elsewhere. For every depth d in [2,n-1] the\n"
        "  diagonal reads offset o=d (a submask of d) at index n-1 = 1, so\n"
        "  T(n,d)=1 for all n-2 depths:  nu2(n) = n-2 = Theta(n), while the\n"
        "  switch density away from the boundary spike is 0.\n"
        "\n"
        "  RANGE SWEPT: n = 4..12 (inclusive), h length n, d in [2, n-1].\n"
        "\n"
        "  Negative control: h = e_0 (single 1 at the FIRST index) does NOT\n"
        "  give linear weight -- this refutation is about the shared final-\n"
        "  index boundary spike, not about any single 1. See last columns;\n"
        "  the control's nu2/n -> 0 while the positive case's nu2/n = 1.\n"
    )


def main():
    rows = run_sweep(4, 12)
    text = header() + "\n" + format_table(rows) + "\n"

    out_path = "/workspace/code/out/refute_single_boundary_sweep.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        f.write(text)

    print(text)
    print(f"Wrote sweep to {out_path}")

    # explicit confirmation line for the operator
    n = rows[-1]['n']
    latest = rows[-1]
    assert latest['nu2_pos'] == n - 2, latest
    assert latest['switch_pos'] == 0.0, latest
    assert latest['nu2_neg'] < (n - 2), latest
    print(f"\nCONFIRMED: at n={n}, nu2(e_{n-1}) = {latest['nu2_pos']} = n-2 "
          f"(linear, nu2/n = {latest['nu2_n_pos']:.3f}) while switch density "
          f"excluding the boundary spike = 0; negative control nu2(e_0) = "
          f"{latest['nu2_neg']} (sublinear). The boundary spike is the cause.")


if __name__ == "__main__":
    main()
