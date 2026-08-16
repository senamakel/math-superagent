# Cross-source tie-back: Yuster's ψ_k = Ho's α_k/(1+α_k) — algebraic verification

<!-- regenerator-trigger -->

**Question.** Two order-k "barrier" constants appear independently in the
library: Yuster's ψ_k (unique root of (1−x)^k = x in [0,1], arXiv:2302.12276)
and Ho's α_k (unique positive root of x(1+x)^(k−1) = 1, arXiv:2601.19327). The
summaries claim ψ_k = α_k/(1+α_k). Is that identity real, and does ψ_2 =
(3−√5)/2?

**Verification — pure algebra (no numerics needed).** Let p = α_k/(1+α_k). Then

```
1 − p = 1/(1 + α_k)
(1 − p)^k = 1/(1 + α_k)^k
```

and `(1−p)^k = p` iff `1/(1+α_k)^k = α_k/(1+α_k)` iff `1 = α_k(1+α_k)^(k−1)`,
which is exactly α_k's defining equation. Hence p satisfies the defining
equation of ψ_k; by uniqueness of the root in [0,1], **ψ_k = α_k/(1+α_k)**.
∎

**k = 2 case.** α_2 solves α(1+α) = 1, so α_2 = (√5−1)/2 = 1/φ. Then
ψ_2 = (1/φ)/(1 + 1/φ) = 1/(φ+1) = 1/φ² = (3−√5)/2 ≈ 0.381966. This is the
iid-entropy / Chase–Lovett barrier. ∎

**Why it matters.** This confirms the "two families are one family" claim in
the digests: the (3−√5)/2 barrier is the k=2 member of the α_k/(1+α_k) /
ψ_k family, so the order-k generalisation is a single spine, not two. It also
vindicates the identity checked numerically in `yuster_psi_k_check.py` (which
was written but not executed) — the algebraic proof subsumes the numeric check.

```claim
id: psi-alpha-tieback
statement: Yuster's ψ_k (root of (1-x)^k=x in [0,1]) equals Ho's α_k/(1+α_k),
  where α_k is the unique positive root of x(1+x)^(k-1)=1; in particular
  ψ_2 = α_2/(1+α_2) = (3-sqrt5)/2. Hence the order-k barrier family of the
  approximate-k-union-closed entropy method is one family: ψ_k = α_k/(1+α_k),
  with (3-sqrt5)/2 its k=2 member.
hypotheses: k real > 1 (defining equations of ψ_k, α_k each have a unique root
  in (0,1)).
holds-here: yes
status: proved (algebraic identity derived above; subsumes the numeric check)
bearing: unifies Yuster's ψ_k and Ho's α_k formulations into one barrier
  family; confirms the (3-sqrt5)/2 iid barrier is the k=2 case of the order-k
  approximate-union-closed spine.
anchor: code/out/psi_alpha_tieback_verify.md ; full texts research/sources/
  yuster-almost-k-union-closed-2023.html.full.md and
  ho-generalized-boppana-lean-2026.html.full.md
follows-from: yuster-psi-k-approx-optimal, ho-generalized-boppana-k
```

A transcendent check of the same identity at k=2..10 was intended via
`code/out/yuster_psi_k_check.py`; the algebraic derivation above is the
second, independent route and is exact rather than numerical.
