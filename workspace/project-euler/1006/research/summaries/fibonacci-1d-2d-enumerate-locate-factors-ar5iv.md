# Fibonacci factor-location source

**Source:** https://arxiv.org/html/2207.04304  [[fibonacci-1d-2d-enumerate-locate-factors-ar5iv.full]]

Sivasankar–Rama state the needed 1D location theorem (in the rabbit/complement convention). If F(n)≤k<F(n+1), the k+1 distinct length-k Fibonacci factors are prefixes of length k of rotations of f_{n+1}, with indices {0,…,F(n)-1} together with {F(n+2)-k-1,…,F(n+1)-1}. They also give a conjugate-prefix formulation and Zeckendorf descriptions of occurrence positions.

The factor-set claim transfers to PE1006 because complement/reversal conventions preserve the relevant set after the corresponding digit translation; exact numerical indices still require the small-k mechanical-word check. This is the primary source for the contiguous-window reduction, but it does not evaluate the decimal square sum or supply an O(log k) aggregation.