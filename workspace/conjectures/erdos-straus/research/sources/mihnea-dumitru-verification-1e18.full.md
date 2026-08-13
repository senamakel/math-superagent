<!-- source: https://arxiv.org/html/2509.00128v1 | converted from HTML -->

Further verification and empirical evidence for the Erdős-Straus conjecture

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2509.00128v1 [math.NT] 29 Aug 2025

# Further verification and empirical evidence for the Erdős-Straus conjecture

Spiridon Mihnea Bogdan C. Dumitru Thanks: Faculty of Mathematics and Computer Science, University of Bucharest.

August, 2025

###### Abstract

We provide empirical evidence for the Erdős-Straus conjecture by improving computational bounds to 10 18 10^{18} and by evaluating the solution-counting function f ⁡ ( p) f(p) for this conjecture.

## 1 Background

The Erdős-Straus conjecture states that every fraction of the form 4 n \frac{4}{n} can be expanded as the sum of 3 unit fractions 1 x + 1 y + 1 z \frac{1}{x}+\frac{1}{y}+\frac{1}{z} with x, y, z ∈ ℕ ∗ x,y,z\in\mathbb{N^{*}}. The study of this conjecture is concerned with the case where n n is a prime number, as unit fraction decompositions for composite numbers n n can be obtained from smaller prime numbers: if n = k ​ p n=kp for some prime p p, and Erdős-Straus holds for p p, then 4 p = 1 x + 1 y + 1 z \frac{4}{p}=\frac{1}{x}+\frac{1}{y}+\frac{1}{z} and consequently 4 n = 4 k ​ p = 1 k ​ x + 1 k ​ y + 1 k ​ z \frac{4}{n}=\frac{4}{kp}=\frac{1}{kx}+\frac{1}{ky}+\frac{1}{kz}.

## 2 Extending Salez bounds

Many attempts to prove the full conjecture use modular identities involving p p. For instance, Mordell [3] was the first to show that the conjecture is true for all primes, except possibly a small subset given by the modular identity p ≡ r p\equiv r (mod 840 840), where r ∈ { 1,121,169,289,361, 529 } r\in\{1,121,169,289,361,529\}. Currently, the known sets of modular identities are not enough to completely exhaust all possibilities for p p. However, this approach leads to computational methods that allow the conjecture to be verified up to a large bound. The best-performing method of this type is described by Salez [4], whose result we extend.

### 2.1 Process

Salez defined a modular filter S m S_{m} as the set of residue classes mod m m for which the conjecture is known to be true and offered an algorithm to produce these filters. Using modular filters, Salez immediately obtains the Mordell result by applying the Chinese remainder theorem on the identities implied by S 5 = { 0, 2, 3 } S_{5}=\{0,2,3\} and S 7 = { 0, 3, 5, 6 } S_{7}=\{0,3,5,6\}. By performing this process with the first 7 7 prime filters, up to S 23 S_{23}, Salez obtained the set R 7 R_{7} of residues modulo some G 7 G_{7} that must be checked. Proof for p ≤ 10 17 p\leq 10^{17} follows by verification of integers that escape filtering up to that bound.

We improved this bound to p ≤ 10 18 p\leq 10^{18} by extending this approach with S 29 S_{29}, obtaining a set R 8 R_{8} with | R 8 | = 2101514 |R_{8}|=2101514 residue classes modulo G 8 = 25878772920 G_{8}=25878772920 for which we must check the conjecture. Considering the efficiency ratios G 7 | R 7 | \frac{G_{7}}{|R_{7}|} and G 8 | R 8 | \frac{G_{8}}{|R_{8}|}, this set is roughly twice as efficient.

We divided work in batches B k = { r + k ​ G 8 | r ∈ R 8 } B_{k}=\{r+kG_{8}\,|\,r\in R_{8}\} for the sake of multithreading. Verifying the conjecture for all primes p ≤ 10 18 p\leq 10^{18} is equivalent to checking all batches up to k = 38641709 k=38641709, which can be done in parallel. Additionally, the original 10 17 10^{17} result saves us the need to check the first k = 3864170 k=3864170 batches. To verify the integers in any given batch B k B_{k}, we used Salez’ algorithm to precompute a set 𝒮 \mathcal{S} of prime filters with | 𝒮 | = 140000 |\mathcal{S}|=140000. Then, for each n ∈ B k n\in B_{k}, we iterated over each S m ∈ 𝒮 S_{m}\in\mathcal{S} and checked if n n is filtered by S m S_{m}.

### 2.2 Details

We note a few things about this process. First, not all integers are filtered by filters in 𝒮 \mathcal{S}. We saved these numbers for later processing and found that none of them were prime, therefore they are accounted for by some earlier prime p p which was filtered out. Second, some filters are more efficient than others, in that they appear to filter more numbers. We ran our C++ checking program over the first k = 7100 k=7100 batches and found that, for instance, S 31 S_{31} filtered out a majority of numbers, while most filters were successful 0 0 times. After each of these k k batches, we sorted the filters according to the total number of integers they filtered. By using the most efficient filters first, we decrease the time it takes to check a batch.

We also remark that computer-aided checking of numbers greater than 10 17 10^{17} requires us to work around the integer size limits of most programming languages. We generated R 8 R_{8} using a Python rewrite of Salez’ algorithm, as the language does not have integer limits, and checked the remaining integers in C++ using the arbitrary-precision integer library GMP 1 1 1 [https://github.com/esc-paper/erdos-straus][3]. The inability to use a machine integer for calculations incurred a significant runtime penalty. Our process completed in about 2 weeks with a medium setup.

## 3 Solution counting

Another approach to the Erdős-Straus conjecture is based on a solution-counting function f ⁡ ( p) = | { ( x, y, z) | 4 p = 1 x + 1 y + 1 z } | f(p)=|\{(x,y,z)\,|\,\frac{4}{p}=\frac{1}{x}+\frac{1}{y}+\frac{1}{z}\}| for p ∈ ℕ ∗ p\in\mathbb{N^{*}}. Elsholtz and Tao [2] proved that f ⁡ ( p) f(p) is upper-bounded polylogarithmically. Furthermore, Bradford [1] shows that for any given p p, all possible x x belong to a finite search space ⌈ p 4 ⌉ ≤ x ≤ ⌈ p 2 ⌉ \lceil\frac{p}{4}\rceil\leq x\leq\lceil\frac{p}{2}\rceil and provides an explicit construction of y y and z z from x x, given the existence of some divisor d | x 2 d\mid x^{2} that verifies one of two identities, which we may term the Bradford conditions, depending on the type of the solution, that is, if p ∤ y p\nmid y (Type-1) or if p | y p\mid y (Type-2). This allows us to evaluate f ⁡ ( p) f(p), although we remark this is computationally expensive for large p p.

The Erdős-Straus conjecture itself is equivalent to the statement f ⁡ ( p) > 0 ​ ∀ p ∈ ℕ ∗ f(p)>0\;\,\forall p\in\mathbb{N^{*}}. We considered only the ordered set 𝒫 = { p | p prime, p ≡ r (mod 840), r ∈ { 1,121,169,289,361, 529 } } \mathcal{P}=\{p\;|\;p\,\textrm{prime},\,p\equiv r\,\textrm{(mod 840)},\,r\in\{1,121,169,289,361,529\}\}, as for all other primes the conjecture is known to be true [3]. We evaluated f ⁡ ( 𝒫 i) f(\mathcal{P}_{i}) for i ∈ 1, N ¯ i\in\overline{1,N}, where N = 66737 N=66737 and 𝒫 i \mathcal{P}_{i} denotes the i i -th element of 𝒫 \mathcal{P}. This corresponds to the "difficult" primes p ≤ 3.5 ⋅ 10 7 p\leq 3.5\cdot 10^{7}.

Counting the number of divisors verifying the Bradford conditions across all possible x x for some prime p p is equivalent to computing f ⁡ ( p) f(p). We checked these conditions for a total of T = 29860049601808 T=29860049601808 divisors of squares of allowable x x for primes p p in our considered subset of 𝒫 \mathcal{P} and found that S = 18601583 S=18601583 of those divisors satisfied at least one of the identities, producing one valid solution to the conjecture for p p.

[image: Refer to caption] Figure 1: Semi-logarithmic scatter plot of f ⁡ ( 𝒫 i) f(\mathcal{P}_{i}) for i ∈ 1, N ¯ i\in\overline{1,N}, by solution type

Based on this trial, we find that, empirically, f ⁡ ( p) f(p) appears to be increasing consistent with the Elsholtz-Tao upper bound, and furthermore that solutions of Type-1 abound relative to those of Type-2, having found S 1 = 12763383 S_{1}=12763383 solutions of Type-1 and only S 2 = 5838200 S_{2}=5838200 of Type-2. Figure 1 shows a scatter plot of our f ⁡ ( p) f(p) data.

## 4 Bibliography

## References

- [1] Kyle Bradford. Elemental patterns from the erdos straus conjecture, 2024.
- [2] Christian Elsholtz and Terence Tao. Counting the number of solutions to the erdos-straus equation on unit fractions, 2015.
- [3] L. J. Mordell. Diophantine equations, volume 30 of Pure and applied mathematics (Academic Press). Academic Press, London, New York, 1969.
- [4] Serge E. Salez. The erdos-straus conjecture new modular equations and checking up to n = 10 17 n=10^{17}, 2014.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: https://github.com/esc-paper/erdos-straus
