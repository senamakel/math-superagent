<!-- source: https://zenn.dev/yatyou/articles/47831bf5576657?locale=en | converted from HTML -->

Understanding and Implementing floor_sum() in O(log(max(a, m)))

#### i Translated by AI

The content below is an AI-generated translation. This is an experimental feature, and may contain errors. [View original article][1]

[2] [3]

[Rust][4]

[AtCoder][5]

[tech][6]

## Introduction

To start off, let's try to calculate the following value:

f(n, m, a, b) = \sum_{i=0}^{n-1} \Big\lfloor \frac{ai+b}{m} \Big\rfloor

Many of you might have thought of an O(n) algorithm. Below, I will introduce an algorithm that calculates this in O\big(\log \max(a, m)\big) time.

## The Algorithm

### Step 1

First, we expand a and b as follows:

\begin{equation*} \begin{cases} a = d_a m + r_a \\ b = d_b m + r_b \\ \end{cases} ,\quad 0 \le r_a, r_b \lt |m| \end{equation*}

Then, f can be written as:

\begin{align*} f(n, m, a, b) &= \sum_{i=0}^{n-1}\Big\lfloor \frac{r_a i + r_b}{m} + d_a i + d_b \Big\rfloor \\ &= \frac{n(n-1)}{2} d_a + n d_b + f(n, m, r_a, r_b) \end{align*}

Since 0 \le r_a, r_b \lt |m|, the following holds:

\begin{align*} f(n, m, r_a, r_b) &= (0 + \cdots + 0) + (1 + \cdots + 1) + \cdots + (k + \cdots + k) \\ 0 \le k \coloneqq \Big\lfloor \frac{r_a (n-1) + r_b}{m} \Big\rfloor \le n - 1 \end{align*}

### Step 2: Change of Order of Summation

The following fact holds:

For any i satisfying 0 \le i \le k, there exists at least one j that satisfies \lfloor (r_a j + r_b) / m \rfloor = i.

Therefore, we can expect a reduction in computational complexity by **changing the order of summation**. In other words, if we can count the number of occurrences of i in O(1), the calculation finishes in O(k). To achieve this, we just need to find the maximum or minimum j that satisfies \lfloor (r_a j + r_b) / m \rfloor = i.

\begin{equation*} i \le \frac{r_a j + r_b}{m} \lt i + 1 \quad\Rightarrow\quad \frac{m i - r_b}{r_a} \le j_i \end{equation*}

Therefore,

\begin{align*} f(n, m, r_a, r_b) &= 0 \cdot (j_1 - j_0) + 1 \cdot (j_2 - j_1) + \cdots + k \cdot (n - j_{k}) \\ &= kn - \sum_{i=1}^k j_i \\ &= kn - \sum_{i=1}^k \Big\lceil \frac{mi - r_b}{r_a} \Big\rceil \\ \end{align*}

### Step 3: Recursion

The following fact holds:

\lfloor x \rfloor = -\lceil -x \rceil

Using this, we can turn f into a recursive function:

\begin{align*} f(n, m, r_a, r_b) &= kn + \sum_{i=1}^k \Big\lfloor -\frac{mi - r_b}{r_a} \Big\rfloor \\ &= kn + \sum_{i=0}^{k-1} \Big\lfloor -\frac{m (k - i) - r_b}{r_a} \Big\rfloor \\ &= kn + \sum_{i=0}^{k-1} \Big\lfloor \frac{m i - m k + r_b}{r_a} \Big\rfloor \\ &= kn + f(n, r_a, m, -m k + r_b) \end{align*}

Noting that m and r_a are swapped, it is clear that the computational complexity becomes the same as that of the Euclidean algorithm.

By the way, when r_a = 0, the above equation fails. Since f(n, m, 0, r_b) = n d_b, we can avoid this by using r_a = 0 as the termination condition for the recursion.

## Implementation

I will briefly explain the key points of the implementation.

1. I use `div_euclid()`and `rem_euclid()`for division. In standard division, the remainder can be negative, but these methods guarantee the remainder is always positive. In other words, they perform "floor division." This ensures the function works correctly even when the argument to the floor function is negative.
2. When `m`is zero, it results in a division-by-zero panic. To prevent this, you could use `std::num::NonZeroI64`. Similarly, since `n`is non-negative, you could use `u64`. It is good practice to provide a wrapper function for the function to take advantage of these type safety benefits.

```
/// Calculate $\sum_{i=0}^{n-1} \lfloor \frac{ai+b}{m} \rfloor$ with $\O(\log a)$ time complexity.
fn floor_sum(n: i64, m: i64, a: i64, b: i64) -> i64 {
    assert_ne!(m, 0);
    assert!(n >= 0);

    let (div_a, rem_a) = (a.div_euclid(m), a.rem_euclid(m));
    let (div_b, rem_b) = (b.div_euclid(m), b.rem_euclid(m));

    let mut res = n * (n - 1) / 2 * div_a + n * div_b;
    if rem_a == 0 {
        return res;
    }

    let k = (rem_a * n - rem_a + rem_b).div_euclid(m);
    res += n * k;
    res += floor_sum(k, rem_a, m, rem_b - m * k);

    res
}
```

## Verify

## References

[2] [3]

### Discussion


## Links

[1]: /yatyou/articles/47831bf5576657
[2]: https://twitter.com/intent/tweet?url=https://zenn.dev/yatyou/articles/47831bf5576657&amp;text=Understanding%20and%20Implementing%20floor_sum()%20in%20O(log(max(a%2C%20m)))%EF%BD%9Cqdot3&amp;hashtags=zenn
[3]: https://b.hatena.ne.jp/add?mode=confirm&amp;url=https://zenn.dev/yatyou/articles/47831bf5576657&amp;title=Understanding%20and%20Implementing%20floor_sum()%20in%20O(log(max(a%2C%20m)))%EF%BD%9Cqdot3
[4]: /topics/rust
[5]: /topics/atcoder
[6]: /tech-or-idea
