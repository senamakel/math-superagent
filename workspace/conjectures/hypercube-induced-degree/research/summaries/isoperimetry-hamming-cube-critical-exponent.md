# Isoperimetry on the Hamming cube near the critical exponent

Source: Polona Durcik, Paata Ivanisvili, Joris Roos, "Sharp isoperimetric
inequalities on the Hamming cube near the critical exponent", arXiv:2407.12674,
2024. URL: https://arxiv.org/abs/2407.12674

## What it establishes

The paper studies a family of isoperimetric-type quantities on the Hamming cube
{0,1}^n interpolating between the vertex boundary (β = 0) and the edge boundary
(β = 1). For a set A and β ≥ 0, define

    Eh^β_A = E[ h_A(x)^β ],

where h_A(x) is the number of edges joining x to the complement when x ∈ A
(0 otherwise); E is expectation under the uniform measure on {0,1}^n.

Main result: for all β ≥ β_0 = 0.50057 and A with |A| ≤ 1/2,

    Eh^β_A  >=  |A| (log_2(1/|A|))^β ,

with equality when A is a subcube. This extends the previously known threshold
β ≥ log_2(3/2) ≈ 0.585. At the critical exponent β = 1/2 the paper gives
sharp/asymptotically sharp bounds for small sets (|A| → 0+), including precise
leading-term constants; for |A| → 1− asymptotics are given but sharpness is not
fully settled.

Technique: a new Bellman-type function built from the Gaussian isoperimetric
profile, certified by computer-assisted verification with interval arithmetic.
Connections: progress toward a conjecture of Kahn and Park on partitioning the
hypercube; sharp Poincaré-type inequalities for Boolean-valued functions near L1.

## Relevance to problem.md

This family of `Eh^β` quantities is exactly the kind of object that could
produce a **maximum** rather than an average, because it involves powers of a
per-vertex boundary function. Talagrand initiated the study of Eh^β_A for
general β and proved dimension-free lower bounds at β = 1/2 — but the paper
notes that *no sharp lower bound is currently known for β = 1/2 even now*.
It is an active frontier, not a closed tool. This does not directly bound the
maximum internal degree D(S), but it is the same family of quantities an
alternative line might use.
