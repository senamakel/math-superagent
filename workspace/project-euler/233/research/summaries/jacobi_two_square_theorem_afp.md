<!-- source: https://isa-afp.org/entries/Sum_Of_Squares_Count.html | converted from HTML -->

The Sum-of-Squares Function and Jacobi's Two-Square Theorem - Archive of Formal Proofs

### Abstract

This entry defines the *sum-of-squares function*$r_k(n)$, which counts the number of ways to write a natural number $n$ as a sum of $k$ squares of integers. Signs and permutations of these integers are taken into account, such that e.g. $1^2+2^2$, $2^2+1^2$, and $(-1)^2+2^2$ are all different decompositions of $5$.

Using this, I then formalise the main result: Jacobi's two-square theorem, which states that for $n > 0$ we have \[r_2(n) = 4(d_1(n) - d_3(n))\ ,\] where $d_i(n)$ denotes the number of divisors $m$ of $n$ such that $m = i\ (\text{mod}\ 4)$.

Corollaries include the identities $r_2(2n) = r_2(n)$ and $r_2(p^2n) = r_2(n)$ if $p = 3\ (\text{mod}\ 4)$ and the well-known theorem that $r_2(n) = 0$ iff $n$ has a prime factor $p$ of odd multiplicity with $p = 3\ (\text{mod}\ 4)$.

### License

[BSD License][1]

### Topics

- [Mathematics/Number theory][2]

### Session Sum_Of_Squares_Count

- [Sum_Of_Squares_Count][3]

### Depends on

- [Dirichlet Series][4]
- [Gaussian Integers][5]
- [List Index][6]

### Used by

- [Theta Functions][7]

## Cite

×

Sum_Of_Squares_Count-AFP

```
@article{Sum_Of_Squares_Count-AFP,
  author  = {Manuel Eberl},
  title   = {The Sum-of-Squares Function and Jacobi's Two-Square Theorem},
  journal = {Archive of Formal Proofs},
  month   = {November},
  year    = {2024},
  note    = {\url{https://isa-afp.org/entries/Sum_Of_Squares_Count.html},
             Formal proof development},
  ISSN    = {2150-914x},
}
```

Copy Download

## Download

× [Download latest][8]

Older releases:

- [Feb 6, 2026][9]: Isabelle2025-2
- [Dec 20, 2025][10]: Isabelle2025-1
- [May 22, 2025][11]: Isabelle2025
- [Mar 17, 2025][12]: Isabelle2025
- [Nov 30, 2024][13]: Isabelle2024


## Links

[1]: https://isa-afp.org/LICENSE
[2]: ../topics/mathematics/number-theory/
[3]: ../thys/Sum_Of_Squares_Count/Sum_Of_Squares_Count.html
[4]: ../entries/Dirichlet_Series.html
[5]: ../entries/Gaussian_Integers.html
[6]: ../entries/List-Index.html
[7]: ../entries/Theta_Functions.html
[8]: https://isa-afp.org/release/afp-Sum_Of_Squares_Count-current.tar.gz
[9]: https://isa-afp.org/release/afp-Sum_Of_Squares_Count-2026-02-06.tar.gz
[10]: https://isa-afp.org/release/afp-Sum_Of_Squares_Count-2025-12-20.tar.gz
[11]: https://isa-afp.org/release/afp-Sum_Of_Squares_Count-2025-05-22.tar.gz
[12]: https://isa-afp.org/release/afp-Sum_Of_Squares_Count-2025-03-17.tar.gz
[13]: https://isa-afp.org/release/afp-Sum_Of_Squares_Count-2024-11-30.tar.gz
