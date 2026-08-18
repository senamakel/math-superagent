# Babichev & Shpakova — weighted floor moments

**Source:** https://arxiv.org/html/2607.17961v1  [[babichev-shpakova-weighted-floor-moments-2026.full]]

The paper gives an exact near-linear algorithm for a lattice-rectangle problem. Its relevant mathematical result is a constant-size weighted-floor moment treatment: affine floor queries are normalized and recursively transformed through Euclidean coefficient paths; boundary corrections are finite and the moment state remains closed. It proves O(log)-depth Euclidean recursion for a fixed query/state family (the full application also batches divisor layers).

This supports the general principle behind PE1006's universal-Euclidean arithmetic, but **does not establish Ψ(k), Fibonacci factors, or the required aggregation over k+1 intercepts**. Its displayed kernels use polynomial index weights and its geometric/weighted application is not the exact base-10 geometric monoid needed here. Therefore it is corroborating context, not a direct solution or a replacement for the OI-Wiki/fhq/LOJ138 geometric recursion.