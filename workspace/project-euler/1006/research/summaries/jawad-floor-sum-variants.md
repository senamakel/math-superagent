# Jawad, Floor Sum of Arithmetic Progression and Other Variants

Source: https://asfjwd.github.io/2020-04-24-floor-sum-ap/

This exposition derives Euclidean-algorithm recurrences for arithmetic-progression floor sums and variants including weighted sums `g=Σ i floor((ai+b)/c)` and square moments `h=Σ floor((ai+b)/c)^2`. Quotient extraction handles `a,b≥c`; the complementary-floor transformation swaps the roles of `a,c` and reduces the range. The same recursive state is shared by the coupled moments, giving logarithmic recursion depth in the Euclidean parameters rather than iteration over `n`. This supports the standard floor-sum primitive needed by PE1006, but does not itself prove the additional aggregation over all Sturmian intercepts required by the Euler problem.

The source is an algorithmic exposition rather than a peer-reviewed theorem source; use it as implementation evidence, not as the sole proof of the PE1006 reduction.