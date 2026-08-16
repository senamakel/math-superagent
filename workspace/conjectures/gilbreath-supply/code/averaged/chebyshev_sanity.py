#!/usr/bin/env python3
"""TASK C — Chebyshev logic sanity.

Demonstrates that a bounded mean alone does NOT imply any density-1 lower
bound. We build one elementary sequence a_n in {c/2, 1} with mean exactly c,
yet the set where a_n >= c/2 has density strictly < 1 that never approaches 1.

Concrete instance with c = 0.49:
  * let the fraction of entries equal to 1 be p1 and the fraction equal to
    c/2 = 0.245 be p2 = 1 - p1. The mean is p1*1 + p2*0.245.
  * We want a large fraction K = 9/10... no—we choose the construction so the
    mean is exactly c while the "large" entries (>= c/2, here the 0.9s and the
    c/2s both qualify) are not density-1.
  * The prompt's suggested shape: a_n = 0.9 for ~54% and a_n = 0.245 (= c/2)
    for ~46%, giving mean 0.49, but the set {a_n >= c/2} then INCLUDES all
    entries (since both 0.9 and 0.245 >= 0.245). That would be density 1, which
    is NOT the demonstration wanted.

We instead aim to show the real point: bounded mean c does not force the set
{a_n >= c - epsilon} to have density near 1. The cleanest such witness uses a
distribution with expectation c but a positive lower tail P(a_n = c/2) = theta
for a fixed theta > 0 (independent of N): mean = theta*(c/2) + (1-theta)*1 = c
=> theta = 2(1-c)/(2-c). For c=0.49: theta = 2*0.51/1.51 = 0.6755. So
P(a_n = c/2) ≈ 0.6755 has a fixed positive mass below c, so the set where
a_n >= c (not just c/2) has density only 1 - theta ≈ 0.3245, bounded away
from 1. And a_n >= c/2 is trivially everything.

To match the prompt's literal two-value request while keeping the density-1
claim true, I construct the *complementary* witness that the prompt intends:
a_n takes only the two values {c/2, 1}, so trivially every term is >= c/2 and
the interesting bound "a_n >= c/2" is not restrictive. The non-trivial density
statement that a bounded mean CANNOT deliver is P(a_n >= c): here that set has
density only 1 - theta ≈ 0.32, never approaching 1.

This is a concise, exact demonstration on one fixed set of parameters;
there is no scaling to do, so no bound is pushed.
"""
import os


def run_task_c(out):
    out.append("=" * 70)
    out.append("TASK C — Chebyshev logic sanity: bounded mean != density-1")
    out.append("=" * 70)
    c = 0.49
    # two-point distribution a in {c/2, 1} with E[a] = c exactly:
    #   theta*P(c/2) + (1-theta)*1 = c  -> theta = 2(1-c)/(2-c)
    theta = 2.0 * (1 - c) / (2 - c)
    out.append(f"c = {c}")
    out.append(f"two-point a in {{c/2, 1}} with E[a] = c exactly:")
    out.append(f"  P(a=c/2)   = theta = 2(1-c)/(2-c) = {theta:.6f}")
    out.append(f"  P(a=1)     = 1-theta             = {1-theta:.6f}")
    out.append(f"  check mean = {theta*(c/2) + (1-theta)*1:.6f} = c  (exact)")
    out.append("")
    # Existence: build one explicit finite prefix realising exactly these counts.
    # For a length-L block, make floor/round theta*L entries equal c/2 and the
    # rest equal 1, so the sample mean is very close to c.
    L = 1000
    k = int(round(theta * L))          # number of c/2 entries
    seq = [c / 2] * k + [1.0] * (L - k)
    mean = sum(seq) / L
    # density of terms >= c  (the only non-trivial 'large' set since all terms
    # are >= c/2 already):
    dens_ge_c = sum(1 for x in seq if x >= c) / L
    dens_ge_half = sum(1 for x in seq if x >= c / 2) / L
    out.append("EXPLICIT FINITE PREFIX (L=1000):")
    out.append(f"  #(a=c/2) = {k}   #(a=1) = {L-k}")
    out.append(f"  sample mean = {mean:.6f}")
    out.append(f"  P(sample a >= c/2) = {dens_ge_half:.4f}   (trivially 1: "
               "all terms are c/2 or 1)")
    out.append(f"  P(sample a >= c)   = {dens_ge_c:.4f}   (bounded away from 1)")
    out.append("")
    out.append("LESSON (the sanity check's point): the statement "
               "'(1/N)Σa_n is bounded below' "
               "is a Chebyshev/mean condition; it does NOT imply that the set "
               "where a_n is large has density approaching 1. Here the mean is "
               "exactly c yet P(a_n >= c) stays ~0.32 < 1 for every N. In the "
               "SUPPLY analogue (GOAL priority 1), the averaged form "
               "M(N)=mean(ν₂/n) rising to ~0.49 is a *bounded-mean* fact; "
               "turning it into 'ν₂(n) >= c·n for density-1 many n' is exactly "
               "the step that does NOT follow from the mean alone and needs a "
               "second moment / concentration argument.")
    return out


def main():
    out = run_task_c([])
    text = "\n".join(out) + "\n"
    print(text)
    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "out")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "chebyshev_sanity.txt"), "w") as f:
        f.write(text)


if __name__ == "__main__":
    main()
