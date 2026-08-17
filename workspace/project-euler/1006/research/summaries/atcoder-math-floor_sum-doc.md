<!-- source: https://atcoder.github.io/ac-library/production/document_en/math.html | converted from HTML -->

[AC Library][1]

# Math

It contains number-theoretic algorithms.

## pow_mod

```
ll pow_mod(ll x, ll n, int m)
```

It returns $x^n \bmod m$.

**Constraints**

- $0 \le n$
- $1 \le m$

**Complexity**

- $O(\log n)$

## inv_mod

```
ll inv_mod(ll x, ll m)
```

It returns an integer $y$ such that $0 \le y < m$ and $xy \equiv 1 \pmod m$.

**Constraints**

- $\gcd(x, m) = 1$
- $1 \leq m$

**Complexity**

- $O(\log m)$

## crt

```
pair<ll, ll> crt(vector<ll> r, vector<ll> m)
```

Given two arrays $r,m$ with length $n$, it solves the modular equation system

$$x \equiv r[i] \pmod{m[i]}, \forall i \in \lbrace 0,1,\cdots, n - 1 \rbrace.$$

If there is no solution, it returns $(0, 0)$. Otherwise, all the solutions can be written as the form $x \equiv y \pmod z$, using integers $y, z$ $(0 \leq y < z = \mathrm{lcm}(m[i]))$. It returns this $(y, z)$ as a pair. If $n=0$, it returns $(0, 1)$.

**Constraints**

- $|r| = |m|$
- $1 \le m[i]$
- $\mathrm{lcm}(m[i])$ is in `ll`.

**Complexity**

- $O(n \log{\mathrm{lcm}(m[i])})$

## floor_sum

```
ll floor_sum(ll n, ll m, ll a, ll b)
```

It returns

$$\sum_{i = 0}^{n - 1} \left\lfloor \frac{a \times i + b}{m} \right\rfloor$$

It returns the answer in $\bmod 2^{\mathrm{64}}$, if overflowed.

**Constraints**

- $0 \leq n \lt 2^{32}$
- $1 \leq m \lt 2^{32}$

**Complexity**

- $O(\log m)$

## Examples

### AC code of [https://atcoder.jp/contests/practice2/tasks/practice2_c][2]

#include <atcoder/math> #include <cstdio> using namespace std; using namespace atcoder; int main() { int t; scanf("%d", &t); for (int i = 0; i < t; i++) { long long n, m, a, b; scanf("%lld %lld %lld %lld", &n, &m, &a, &b); printf("%lld\n", floor_sum(n, m, a, b)); } return 0; }


## Links

[1]: ./index.html
[2]: https://atcoder.jp/contests/practice2/tasks/practice2_c
