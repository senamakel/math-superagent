<!-- source: https://atcoder.jp/contests/practice2/editorial/579 | converted from HTML -->

Editorial - AtCoder Library Practice Contest

×

#### Contest started

AtCoder Library Practice Contest has begun.

Close

×

#### Contest is over

AtCoder Library Practice Contest has ended.

Close

Contest Duration: [2020-09-07 22:31:51+0900][1] - [3020-09-07 22:31:51+0900][2] (local time) [Back to Home][3]

- [Top][4]
- [Tasks][5]
- Results

  - [All Submissions][6]

- [Editorial][7]
-

Official

## [C - Floor Sum][8] Editorial by [yosupo][9]

---

\((n, m, a, b \in \mathbb{Z}), (0 \leq n), (1 \leq m)\) について次の関数を高速に計算するアルゴリズムを設計する。

\[f(n, m, a, b) = \sum_{i=0}^{n-1} \left\lfloor \frac{ai + b}{m} \right\rfloor\]

まず、 \(a, b\) に対して \(\bmod{m}\) を取ることができ、 \(a=0\) ならば明らかなので、 \(1 \le a \lt m, 0 \le b \lt m\) の場合に帰着できる。

そして、 \(y = \left\lfloor \frac{an + b}{m} \right\rfloor, z = (an + b) \% m\) として次の等式が成立することが示せる。

\[f(n, m, a, b) = f(y, a, m, z) \]

この等式に従って再帰関数を設計すると、 \(a, m\) がユークリッドの互除法と同じ挙動をするので、 \(O(\log a + \log m)\) 段の再帰で計算できる。以下ではこの等式の証明を示す。

本質的なアイデアは次の式変形である。つまり各 \(i\) について値を足し合わせるのではなく、各値についてその値を超える \(i\) がいくつあるかを数え、足し合わせる。

\[\begin{aligned} f(n, m, a, b) &= \sum_{i=0}^{n-1} \left\lfloor \frac{ai + b}{m} \right\rfloor \\ &= \sum_{x=1}^{y} \left(\#\ of\ i \in \{0, 1, \cdots, n - 1\} s.t. \left\lfloor \frac{ai + b}{m} \right\rfloor \geq x \right) \\ &= \sum_{x=0}^{y - 1} \left( \#\ of\ i \in \{0, 1, \cdots, n - 1\} s.t. \left\lfloor \frac{ai + b}{m} \right\rfloor \geq (y - x) \right) \end{aligned}\]

ここで、内側の式を整理して、

\[\begin{aligned} \left\lfloor \frac{ai + b}{m} \right\rfloor \geq (y - x) &\Leftrightarrow \frac{ai + b}{m} \geq (y - x) \\ &\Leftrightarrow i \geq \frac{(y - x)m - b}{a} \end{aligned}\]

より、次が成立する。

\[\begin{aligned} \left( \#\ of\ i \in \{0, 1, \cdots, n - 1\} s.t. \left\lfloor \frac{ai + b}{m} \right\rfloor \geq (y - x) \right) = \left\lfloor n - \frac{(y - x)m - b}{a} \right\rfloor \end{aligned}\]

最後に、 \(y = \frac{an + b - z}{m}\) を使うと、次のようになり、 \(f(n, m, a, b) = f(y, a, m, z)\) が示される。

\[\begin{aligned} \left\lfloor n - \frac{(y - x)m - b}{a} \right\rfloor &= \left\lfloor n - \frac{(\frac{an + b - z}{m} - x)m - b}{a} \right\rfloor \\ &= \left\lfloor \frac{z + xm}{a} \right\rfloor \\ \end{aligned}\]

なお、この解説は、 こちらの [Pull Request][10] で rsk0315 さんに提案されたコードを解説しています。

posted:
last update:

---

[11]

---

Page Top


## Links

[1]: http://www.timeanddate.com/worldclock/fixedtime.html?iso=20200907T2231&p1=248
[2]: http://www.timeanddate.com/worldclock/fixedtime.html?iso=30200907T2231&p1=248
[3]: /home
[4]: /contests/practice2
[5]: /contests/practice2/tasks
[6]: /contests/practice2/submissions
[7]: /contests/practice2/editorial
[8]: /contests/practice2/tasks/practice2_c
[9]: /users/yosupo
[10]: https://github.com/atcoder/ac-library/pull/88
[11]: https://www.addtoany.com/share
