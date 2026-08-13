```approach
idea: discrete-stefan-free-boundary-block-interface
mechanism: |
  The block boundary position b_k (length of the leading {0,2} block) evolves
  according to exact laws established by this run:

  - Erosion: b_{k+1} = b_k − 1 (always, except at regeneration)
  - Regeneration: when edge x_k = A_k[b_k] = 2 and intruder y_k = A_k[b_k+1] = 4,
    the block extends rightward by j_k ≥ 0 positions, so b_{k+1} = b_k + j_k
  - Drain: y_{k+1} = y_k − 2·[x_k = 2]

  This is EXACTLY a discrete Stefan problem (free boundary problem) from PDE
  theory. In a Stefan problem, a phase boundary (here: the interface between
  the {0,2} "solid" block and the ≥4 "liquid" tail) moves according to the
  local energy balance. The block length b_k is the interface position; the
  intruder y_k is the "temperature" of the liquid at the interface; the edge
  x_k is the "temperature gradient" (flux) into the interface. The drain law
  is heat diffusion in the liquid phase; the regeneration condition (x=2,y=4)
  is the Stefan condition — the interface advances when latent heat is
  absorbed.

  More precisely: define the "enthalpy" H_k = b_k + (k−1). The recharge
  identity H_k = b_1 + Σ_{events i<k}(j_i+1) is a discrete conservation law:
  enthalpy increases exactly by j_i+1 at each regeneration event and is
  constant during erosion. This is the integral form of the Stefan condition
  ∂_t H + ∂_x q = 0 where q is the flux.

  The standard theory of Stefan problems (Caffarelli, Friedman, etc.) provides
  TOOLS that have never been applied to Gilbreath: comparison principles
  (if two configurations have ordered initial data, their interfaces stay
  ordered), energy monotonicity (a Lyapunov functional built from the
  enthalpy and the temperature profile decreases), and universal gradient
  bounds. The conjecture is equivalent to: the interface b_k never reaches 0.
  A Stefan-type comparison principle would prove that if the prime
  configuration has interface b_k ≥ 1 for all k ≤ K (checked computationally),
  and the "heat flux" q (determined by the prime gap statistics) is bounded
  below the threshold that would melt the solid phase, then b_k ≥ 1 for all k.

  The concrete theorem to prove: there exists a function F(y₀, b₀) such that
  if the initial intruder y₀ ≤ G and initial block length b₀ ≥ b_min, then
  the interface b_k never hits 0. The bound F comes from the worst-case
  solution of the Stefan problem given the drain law and the edge-flip
  statistics.

  Why this beats everything on disk: it reframes the problem as a classical
  free-boundary PDE question, where comparison principles and energy methods
  are standard and powerful. No existing approach uses PDE/free-boundary
  theory. It separates the "geometry" of the interface (which is universal
  for any 2-then-odds sequence) from the "forcing" (the prime gap values that
  determine the flux), and the geometry alone may provide a universal lower
  bound on the interface position.

  Named mathematics: Stefan problem, free boundary, enthalpy method, phase
  transition, comparison principle, Caffarelli-type regularity, energy
  monotonicity (Weiss formula).

  Speculative: the exact discrete Stefan problem may not have a direct PDE
  analogue in the literature, and the "flux" (edge value x_k) is not a
  continuous function but a {0,2}-valued Rule 90 process — the free-boundary
  theory would need to be adapted to this discrete, stochastic-like flux.
  But the structural analogy is tight enough that standard methods should
  transfer.
status: proposed
first-step: |
  (a) Formulate the exact discrete Stefan problem. Define the "temperature"
  u(i,k) at position i > b_k in row k (tail entries). The evolution is
  u(i, k+1) = |u(i, k) − u(i+1, k)| for i > b_k, with boundary condition at
  i = b_k given by the intruder y_k. The interface b_k satisfies the Stefan
  condition: b_{k+1} = b_k − 1 when y_k ≥ 6 or (y_k = 4, x_k = 0), and
  b_{k+1} = b_k + j when (y_k = 4, x_k = 2). State this precisely as a
  discrete free-boundary problem.

  (b) Verify the "comparison principle" on the real data: take two rows from
  the depth-1000 data with the same b_k and different y_k values, then
  compare their interface evolution. If larger y consistently leads to slower
  erosion or earlier regeneration, the comparison principle holds empirically.

  (c) Search for "Stefan problem discrete free boundary" and "enthalpy method
  discrete" in the library to ground the approach, focusing on comparison
  principles for discrete parabolic free-boundary problems.

  (d) Write a minimal Stefan solver for the block-interface evolution with
  adversarial flux, and compute the worst-case b_k after k rows given a flux
  bound.
```