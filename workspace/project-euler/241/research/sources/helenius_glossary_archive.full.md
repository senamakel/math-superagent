<!-- source: https://web.archive.org/web/20151210102548/http://pw1.netcom.com/~fredh/mpfn/glossary.html | converted from HTML -->

Multiperfect numbers: Glossary

## A glossary of MPFN-related terms

On this page, "number" always means "positive integer". **abundant**A number is abundant if sigma (n) > 2n, or, equivalently, if index (n) > 2. Another way of saying this is that sum of the proper divisors of n exceeds n. Contrast deficient, perfect.

Any multiple of an abundant number or of a perfect number is abundant. An abundant number which is neither a multiple of another abundant number nor a multiple of a perfect number is called "primitive abundant".

**boost**A set of prime powers which provide support for each in other in a cycle. For example, 43^2 supports 631, 631 supports 79, and 79^2 supports 43, so 43^2 79^2 631 is a boost. When searching for an MPFN, if a candidate number contains 43 and 79 once each, replacing them with 43^2 79^2 631 will produce another likely candidate.

**cascade**The primes or prime powers resulting from factoring sigma of some prime power, then factoring sigma of each prime or prime power in the resulting factorization, and so on.

**deficient**A number is deficient if sigma (n) < 2n, or, equivalently, if index (n) < 2. Another way of saying this is that sum of the proper divisors of n is less than n. Contrast abundant, perfect.

Every divisor of a deficient number is deficient.

**effective exponent**The effective exponent of 2^n is (n + 1) minus the sum of all primes p dividing (n + 1) for which 2^p - 1 is a Mersenne prime.

**fractionally perfect number (FPFN)**A number whose index is a "simple" fraction. Here, "simple" usually means that the denominator is less than ten.

**index**index(n) = sigma (n)/n = sigma_{-1}(n). index(n) is a multiplicative function of n. If index(n) is an integer, n is called multiperfect.

**index champion**A number is an index champion if its index is larger than the index of any smaller number. Also called "superabundant numbers". The first few index champions are 1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, ...

**Mersenne number**A number which is one less than a power of two; 2^n - 1 for a positive integer n.

Mersenne numbers are named for Father Marin Mersenne, a 17th century French mathematician, philosopher and theologian who published a remarkable (but incorrect) statement about which of these numbers are prime. He also started research into MPFNs by corresponding about them with his contemporaries Fermat, Descartes, and others.

**Mersenne prime**A Mersenne number which is prime. In order for 2^n - 1 to be prime, n itself must be prime.

Only 40 Mersenne primes are known; they include the very largest known primes. Much more information about Mersenne primes is available [here][1]; an Internet-based project to search for more of them is [here][2].

**multiperfect number (MPFN)**A number whose index is an integer; equivalently, a number such that the sum of its divisors is a multiple of the number. If the index is two, the number is perfect; if it is greater than two, the number is proper multiperfect. Often "multiperfect" is used to mean "proper multiperfect". MPFNs have also been called "multiply perfect", "pluperfect", "k-fold perfect" or "k-ply perfect". In French, "multiparfait"; in German "mehrfach vollkommen".

The only MPFN with index one is one itself. The first few MPFNs are 1, 6, 28, 120, 496, 672, 8128, 30240, 32760, 523776, 2178540, ...

**multiplicative**A function f on the positive integers is called multiplicative if f(rs) = f(r) f(s) whenever r and s are relatively prime. It follows that f is determined by the values it takes on prime powers: if n = 2^a 3^b 5^c ..., then f(n) = f(2^a) f(3^b) f(5^c) ...

**perfect**A number is perfect if sigma (n) = 2n, or, equivalently, if index (n) = 2. Another way of saying this is that sum of the proper divisors of n equals n. Contrast abundant, deficient.

Every multiple of a perfect number other than itself is abundant, and every proper divisor is deficient. A Mersenne prime multiplied by the preceding power of two is a perfect number; i.e., if 2^p - 1 is prime, then (2^p - 1)*2^(p - 1) is perfect. All even perfect numbers are of this form; it is not known if there any odd perfect numbers.

**proper multiperfect**A number is proper multiperfect if its index is an integer greater than two; i.e., if it is a multiperfect number greater than one which is not perfect. Often "multiperfect" is used to mean "proper multiperfect".

**seed**In the successive adjustment method, a seed is a product of powers of the first k primes, for some small value of k.

**self-support**A prime power has self-support if it provides support for itself.

**sigma**sigma is the sum-of-divisors function; sigma(n) is the sum of all the positive integers dividing n. A generalization is sigma_k(n), the sum of all the kth powers of the divisors of n. sigma_k, and thus sigma = sigma_1, is a multiplicative function.

**substitution**Given MPFNs A,B,C, it may be possible to form a new MPFN D by noting the prime powers that change in going from the factorization of A to the factorization of B, and substituting these changes in the factorization of C. In order to produce a MPFN, the following conditions must hold: every prime power in A which does not exactly divide B must exactly divide C, every prime in B that does not divide A must not divide C, and, if index(A) != index(B), then index(C)*(index(B)/index(A)) must be an integer. If these conditions hold, D = C*(B/A) and index(D) = index(C)*(index(B)/index(A)).

A common substitution in small MPFNs involves replacing 19^2 127 by 19^4 151 911; the index is unchanged.

**successive adjustment**The successive adjustment method attempts to find MPFNs as follows:

Step 1. Set N equal to a seed.
Step 2. Compute S = sigma (N)/N.
Step 3. If S is an integer, output N.
Step 4. Let p be the largest prime occurring in S. Multiply N by p^k, where k is the multiplicity with which p appears in S (if p appears in the denominator of S, k is negative).
Step 5. Go to step 2.

The process is ended when the values of N enter a cycle.

**support**A prime power p^k provides support for a prime q if q appears in the factorization of sigma (p^k).

**triperfect**A number is triperfect if it is multiperfect with index 3.

Only six triperfect numbers are known.

**tweak**Similar to a boost, a tweak is a transformation performed on a candidate MPFN to produce another candidate. Unlike a boost, not all powers are increased. For example, if the candidate contains 43^3 79^2, replacing that with 43^2 79^3 is reasonable because 43^2 provides support for the additional factor of 79, but changing 79^2 to 79^3 removes support for one factor of 43.

##### [Back to main MPFN page][3]
[Back to my home page][4]


## Links

[1]: https://web.archive.org/web/20151210102548/http://primes.utm.edu/mersenne/
[2]: https://web.archive.org/web/20151210102548/http://www.mersenne.org/prime.htm
[3]: index.html
[4]: /web/20151210102548/http://pw1.netcom.com/~fredh/index.html
