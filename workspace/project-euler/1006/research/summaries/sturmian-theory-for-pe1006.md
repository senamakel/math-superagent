# Sturmian theory relevant to PE1006

Sources: [Frid, Equivalent definitions of Sturmian words](https://www.i2m.univ-amu.fr/wiki/Combinatorics-on-Words-seminar/_media/lectures:lecture8slidessturmian.pdf), [Carton, Sturmian Words](https://www.irif.fr/~carton/Enseignement/MPRI/Dynam-symbol/Documents/sturmian-words.pdf), [Fibonacci word](https://en.wikipedia.org/wiki/Fibonacci_word).

## Governing result
The Fibonacci infinite word, the fixed point of the morphism `0 -> 01`, `1 -> 0`, is Sturmian. A Sturmian infinite binary word has factor complexity `p(k)=k+1`: exactly `k+1` distinct contiguous factors of every length `k`. This is the Morse–Hedlund minimal-complexity characterization (aperiodic binary words attaining the lower bound `p(k)>=k+1`).

The same sources give the mechanical/rotation description: for irrational slope `alpha`, digits are differences of floors `floor((j+1)alpha+rho)-floor(j alpha+rho)`, with the Fibonacci word corresponding (up to convention/complement) to a golden-ratio slope. Factors correspond to the partition of the circle by the finitely many orbit points `{rho-i alpha}`. This converts the factor set into finitely many exact floor expressions; the large-k sum can therefore be reduced to weighted floor sums, evaluated by Euclidean recursion rather than enumerating factors.

The AtCoder Library floor-sum documentation and editorial (https://atcoder.github.io/ac-library/master/document_en/math.html; https://atcoder.jp/contests/practice2/editorial/579) establish the standard Euclidean recurrence for `sum_{i=0}^{n-1} floor((a i+b)/m)`, with logarithmic recursion depth. The required weighted first/second moments are handled by carrying a constant-size segment monoid (count, geometric weight, weighted floor sum, weighted square-floor sum) through the same Euclidean decomposition.

These results apply because the PE word is exactly the morphic Fibonacci fixed point (the finite recursion converges to it), and `gcd(10,101001001)=1`, so geometric weights involving `10^{-1}` are valid modulo the target modulus.