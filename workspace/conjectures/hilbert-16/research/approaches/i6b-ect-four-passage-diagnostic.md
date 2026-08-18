# I^1_6b ECT-route diagnostic

## Theory and source scope
Roussarie–Shan–Zhu (2015), §2.2, explicitly says that finite cyclicity requires a **uniform** bound on zeros of a displacement map over all parameters, and that the blow-up covers parameter space by infinitely many sectors before extracting a finite subcover. Their Theorem 2.3 gives second-type Dulac passages with a resonant term and a remainder whose regularity depends on fractional powers and logarithmic factors. These hypotheses do not state that four passages belong to one common ECT family.

## Mechanical diagnostic
`code/refute/i6b_ect_diagnostic.py` is an exact SymPy oracle, captured in `code/out/i6b_ect_diagnostic.captured.txt`. The new check is exact Wronskian algebra.

* Two individually ECT pairs, `(1,x)` and `(-1,-x)`, each have nonzero Wronskian, while their sum is `(0,0)` with zero Wronskian. Thus “each passage/block is ECT, therefore the sum of four passages is ECT” is false without a common basis, coefficient sign/variation restrictions, or a direct Wronskian theorem for the composed map.
* The toy displacement `D(eps,x)=eps^2*(x-1)+eps^3*(x-2)^2` has identically zero coefficient of `eps` but nonzero second coefficient. Hence a vanishing slow-divergence integral invalidates first-order control; it does not imply zero displacement or absence of cycles. One must restart at the first nonzero higher-order term, uniformly across parameter sectors.

## Exact scope
Status: **diagnostic/refutation of the inference**, not a dynamical counterexample. The polynomial pairs do not satisfy the normal form, transition-map identities, compatibility conditions, or parameter relations of the actual `I^1_6b` family. Therefore the artifact does not refute finite cyclicity, the RR boundary result, or the open problem. It identifies the smallest missing hypotheses:

1. a single explicitly defined function space containing the four composed passages;
2. a proof that its ordered basis has all initial Wronskians nonzero on every sector and parameter boundary;
3. a treatment of vanishing slow divergence by higher-order leading terms and uniform remainder bounds.

The existing bounded toy scans and iterated-log toy (`code/out/i6b_ect_bounded_search.captured.txt`, `i6b_second_type_toy.captured.txt`) agree, but are not faithful dynamics. No larger scan was made: increasing a toy coefficient box would only sample more surrogates and settle no new mathematical question.
