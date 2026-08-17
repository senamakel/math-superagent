<!-- source: https://en.oi-wiki.org/math/euclidean/ | converted from HTML -->

Euclidean-like Algorithm - OI Wiki Skip to content

- Competitions
- Problem Types
- [Studying Roadmap][1]
- [External Resources][2]
- Tricks
- [Problemsetting][3]

- Tools
- [Judging Tools][4]
- [Commandline][5]
- [WSL (Windows 10)][6]
- [Special Judge][7]
- Testlib
- [Polygon][8]
- [OJ Tools][9]
- [Beginner LaTeX][10]

- Programming
- C++ Basics
- Advanced Data Types
- [Functions][11]
- [File Operations][12]

- C++ Standard Libraries
- [Algorithms in STL][13]
- [bitset][14]
- [string][15]

- Advanced C++

- [C VS C++][16]
- [Quick Guide to C++ for Pascal Users][17]
- [Python Quick Guide][18]
- [Java Quick Guide][19]

- Algorithm
- [Prefix Sum & Adjacent Difference][20]
- [Bisect][21]
- [Binary Lifting][22]
- [Constructive Algorithms][23]

- Search
- DP
- [Misc. DP][24]

- String
- [Suffix Automation (SAM)][25]
- [Suffix Binary Search Tree][26]
- [General SAM][27]
- [Suffix Sum][28]
- [Manacher][29]
- [Palindrome Tree][30]
- [Sequence Automation][31]
- [Minimal Representation][32]
- [Lyndon Decomposition][33]

- Math
- Comments

- [Bezout's Theorem][34]
- [Multiplicative Inverse][35]
- [Congruence Equation][36]
- [Chinese Remainder Theorem][37]
- [Quad Residue][38]
- [BSGS][39]
- [Primitive Root][40]
- [Lucas's Theorem][41]
- [Mobius Inversion Formula][42]
- [Du's Algorithm][43]
- [Powerful Number (Ex. Du's)][44]
- [Min_25's Algotithm][45]
- [Zhouge Algorithm][46]
- [Pollard-Rho][47]
- [Continued Fraction][48]
- [Stern-Brocot Tree & Farey Sequence][49]
- [Pell Equation][50]

- 多项式
- 生成函数
- 线性代数
- 线性规划
- 组合数学
- [概率初步][51]
- [置换群][52]
- [斐波那契数列][53]
- [博弈论][54]
- [牛顿迭代法][55]
- [数值积分][56]
- [分段打表][57]

- Data Structure
- Heap
- Block Data Structure
- [Monotonous Stack][58]
- [Monotonous Queue][59]
- [Sparse Table][60]
- [Segment Tree][61]
- [Fenwick][62]
- [Li Chao Tree][63]
- [Segment History Extreme][64]
- [Dividing Tree][65]
- Binary Search / Balanced Trees
- [Skiplist][66]
- Persistent Data Structure
- Tree in Tree
- [K-D Tree][67]
- [ODT][68]
- Dynamic Tree
- [Divide Combine Tree][69]

- Graph Theory
- [矩阵树定理][70]
- [有向无环图][71]
- [拓扑排序][72]
- [最小生成树][73]
- [最小直径生成树][74]
- [最短路][75]
- [拆点][76]
- [差分约束][77]
- [k 短路][78]
- 连通性相关
- [2-SAT][79]
- [欧拉图][80]
- [哈密顿图][81]
- [二分图][82]
- [最小环][83]
- [平面图][84]
- [图的着色][85]
- 网络流
- 图的匹配
- [Prufer 序列][86]
- [LGV 引理][87]
- [弦图][88]

- Comp. Geometry
- Misc

- [分数规划][89]
- 随机化
- [悬线法][90]
- [计算理论基础][91]
- [字节顺序][92]
- [约瑟夫问题][93]
- [格雷码][94]
- [表达式求值][95]
- [在一台机器上规划任务][96]
- [主元素问题][97]

- Topics
- About Hulu

- Comments

[][98]

# Euclidean-like Algorithm

类欧几里德算法由洪华敦在 2016 年冬令营营员交流中提出的内容，其本质可以理解为，使用一个类似辗转相除法来做函数求和的过程。

## 引入 ¶

设

f(a,b,c,n)=\sum_{i=0}^n\left\lfloor \frac{ai+b}{c} \right\rfloor

其中 a,b,c,n 是常数。需要一个 O(\log n) 的算法。

这个式子和我们以前见过的式子都长得不太一样。带向下取整的式子容易让人想到数论分块，然而数论分块似乎不适用于这个求和。但是我们是可以做一些预处理的。

如果说 a\ge c 或者 b\ge c ，意味着可以将 a,b 对 c 取模以简化问题：

\begin{split} f(a,b,c,n)&=\sum_{i=0}^n\left\lfloor \frac{ai+b}{c} \right\rfloor\\ &=\sum_{i=0}^n\left\lfloor \frac{\left(\left\lfloor\frac{a}{c}\right\rfloor c+a\bmod c\right)i+\left(\left\lfloor\frac{b}{c}\right\rfloor c+b\bmod c\right)}{c}\right\rfloor\\ &=\frac{n(n+1)}{2}\left\lfloor\frac{a}{c}\right\rfloor+(n+1)\left\lfloor\frac{b}{c}\right\rfloor+ \sum_{i=0}^n\left\lfloor\frac{\left(a\bmod c\right)i+\left(b\bmod c\right)}{c} \right\rfloor\\ &=\frac{n(n+1)}{2}\left\lfloor\frac{a}{c}\right\rfloor +(n+1)\left\lfloor\frac{b}{c}\right\rfloor+f(a\bmod c,b\bmod c,c,n) \end{split}

那么问题转化为了 a<c,b<c 的情况。观察式子，你发现只有 i 这一个变量。因此要推就只能从 i 下手。在推求和式子中有一个常见的技巧，就是条件与贡献的放缩与转化。具体地说，在原式 \displaystyle f(a,b,c,n)=\sum_{i=0}^n\left\lfloor \frac{ai+b}{c} \right\rfloor 中， 0\le i\le n 是条件，而 \left\lfloor \dfrac{ai+b}{c} \right\rfloor 是对总和的贡献。

要加快一个和式的计算过程，所有的方法都可以归约为 **贡献合并计算**。但你发现这个式子的贡献难以合并，怎么办？**将贡献与条件做转化**得到另一个形式的和式。具体地，我们直接把原式的贡献变成条件：

\sum_{i=0}^n\left\lfloor \frac{ai+b}{c} \right\rfloor =\sum_{i=0}^n\sum_{j=0}^{\left\lfloor \frac{ai+b}{c} \right\rfloor-1}1\\

现在多了一个变量 j ，既然算 i 的贡献不方便，我们就想办法算 j 的贡献。因此想办法搞一个和 j 有关的贡献式。这里有另一个家喻户晓的变换方法，笔者概括为限制转移。具体来说，在上面的和式中 n 限制 i 的上界，而 i 限制 j 的上界。为了搞 j ，就先把 j 放到贡献的式子里，于是我们交换一下 i,j 的求和算子，强制用 n 限制 j 的上界。

\begin{split} &=\sum_{j=0}^{\left\lfloor \frac{an+b}{c} \right\rfloor-1} \sum_{i=0}^n\left[j<\left\lfloor \frac{ai+b}{c} \right\rfloor\right]\\ \end{split}

这样做的目的是让 j 摆脱 i 的限制，现在 i,j 都被 n 限制，而贡献式看上去是一个条件，但是我们仍把它叫作贡献式，再对贡献式做变换后就可以改变 i,j 的限制关系。于是我们做一些放缩的处理。首先把向下取整的符号拿掉

j<\left\lfloor \frac{ai+b}{c} \right\rfloor \Leftrightarrow j+1\leq \left\lfloor \frac{ai+b}{c} \right\rfloor \Leftrightarrow j+1\leq \frac{ai+b}{c}\\

然后可以做一些变换

j+1\leq \frac{ai+b}{c} \Leftrightarrow jc+c\le ai+b \Leftrightarrow jc+c-b-1< ai

最后一步，向下取整得到：

jc+c-b-1< ai\Leftrightarrow \left\lfloor\frac{jc+c-b-1}{a}\right\rfloor< i

这一步的重要意义在于，我们可以把变量 i 消掉了！具体地，令 m=\left\lfloor \frac{an+b}{c} \right\rfloor ，那么原式化为

\begin{split} f(a,b,c,n)&=\sum_{j=0}^{m-1} \sum_{i=0}^n\left[i>\left\lfloor\frac{jc+c-b-1}{a}\right\rfloor \right]\\ &=\sum_{j=0}^{m-1} n-\left\lfloor\frac{jc+c-b-1}{a}\right\rfloor\\ &=nm-f\left(c,c-b-1,a,m-1\right) \end{split}

这是一个递归的式子。并且你发现 a,c 分子分母换了位置，又可以重复上述过程。先取模，再递归。这就是一个辗转相除的过程，这也是类欧几里德算法的得名。

容易发现时间复杂度为 O(\log n) 。

## 扩展 ¶

理解了最基础的类欧几里德算法，我们再来思考以下两个变种求和式：

g(a,b,c,n)=\sum_{i=0}^ni\left\lfloor \frac{ai+b}{c} \right\rfloor\\ h(a,b,c,n)=\sum_{i=0}^n\left\lfloor \frac{ai+b}{c} \right\rfloor^2

### 推导 g ¶

我们先考虑 g ，类似地，首先取模：

g(a,b,c,n) =g(a\bmod c,b\bmod c,c,n)+\left\lfloor\frac{a}{c}\right\rfloor\frac{n(n+1)(2n+1)}{6}+\left\lfloor\frac{b}{c}\right\rfloor\frac{n(n+1)}{2}

接下来考虑 a<c,b<c 的情况，令 m=\left\lfloor\frac{an+b}{c}\right\rfloor 。之后的过程我会写得很简略，因为方法和上文略同：

\begin{split} &g(a,b,c,n)=\sum_{i=0}^ni\left\lfloor \frac{ai+b}{c} \right\rfloor\\ &=\sum_{j=0}^{m-1} \sum_{i=0}^n\left[j<\left\lfloor\frac{ai+b}{c}\right\rfloor\right]\cdot i \end{split}

这时我们设 t=\left\lfloor\frac{jc+c-b-1}{a}\right\rfloor ，可以得到

\begin{split} &=\sum_{j=0}^{m-1}\sum_{i=0}^n[i>t]\cdot i\\ &=\sum_{j=0}^{m-1}\frac{1}{2}(t+n+1)(n-t)\\ &=\frac{1}{2}\left[mn(n+1)-\sum_{j=0}^{m-1}t^2-\sum_{j=0}^{m-1}t\right]\\ &=\frac{1}{2}[mn(n+1)-h(c,c-b-1,a,m-1)-f(c,c-b-1,a,m-1)] \end{split}

### 推导 h ¶

同样的，首先取模：

\begin{split} h(a,b,c,n)&=h(a\bmod c,b\bmod c,c,n)\\ &+2\left\lfloor\frac{b}{c}\right\rfloor f(a\bmod c,b\bmod c,c,n) +2\left\lfloor\frac{a}{c}\right\rfloor g(a\bmod c,b\bmod c,c,n)\\ &+\left\lfloor\frac{a}{c}\right\rfloor^2\frac{n(n+1)(2n+1)}{6}+\left\lfloor\frac{b}{c}\right\rfloor^2(n+1) +\left\lfloor\frac{a}{c}\right\rfloor\left\lfloor\frac{b}{c}\right\rfloor n(n+1) \end{split}

考虑 a<c,b<c 的情况， m=\left\lfloor\dfrac{an+b}{c}\right\rfloor, t=\left\lfloor\dfrac{jc+c-b-1}{a}\right\rfloor.

我们发现这个平方不太好处理，于是可以这样把它拆成两部分：

n^2=2\dfrac{n(n+1)}{2}-n=\left(2\sum_{i=0}^ni\right)-n

这样做的意义在于，添加变量 j 的时侯就只会变成一个求和算子，不会出现 \sum\times \sum 的形式：

\begin{split} &h(a,b,c,n)=\sum_{i=0}^n\left\lfloor \frac{ai+b}{c} \right\rfloor^2 =\sum_{i=0}^n\left[\left(2\sum_{j=1}^{\left\lfloor \frac{ai+b}{c} \right\rfloor}j \right)-\left\lfloor\frac{ai+b}{c}\right\rfloor\right]\\ =&\left(2\sum_{i=0}^n\sum_{j=1}^{\left\lfloor \frac{ai+b}{c} \right\rfloor}j\right) -f(a,b,c,n)\\ \end{split}

接下来考虑化简前一部分：

\begin{split} &\sum_{i=0}^n\sum_{j=1}^{\left\lfloor \frac{ai+b}{c} \right\rfloor}j\\ =&\sum_{i=0}^n\sum_{j=0}^{\left\lfloor \frac{ai+b}{c} \right\rfloor-1}(j+1)\\ =&\sum_{j=0}^{m-1}(j+1) \sum_{i=0}^n\left[j<\left\lfloor \frac{ai+b}{c} \right\rfloor\right]\\ =&\sum_{j=0}^{m-1}(j+1)\sum_{i=0}^n[i>t]\\ =&\sum_{j=0}^{m-1}(j+1)(n-t)\\ =&\frac{1}{2}nm(m+1)-\sum_{j=0}^{m-1}(j+1)\left\lfloor \frac{jc+c-b-1}{a} \right\rfloor\\ =&\frac{1}{2}nm(m+1)-g(c,c-b-1,a,m-1)-f(c,c-b-1,a,m-1) \end{split}

因此

h(a,b,c,n)=nm(m+1)-2g(c,c-b-1,a,m-1)-2f(c,c-b-1,a,m-1)-f(a,b,c,n)

在代码实现的时侯，因为 3 个函数各有交错递归，因此可以考虑三个一起整体递归，同步计算，否则有很多项会被多次计算。这样实现的复杂度是 O(\log n) 的。

[模板题代码实现][99]

```
#include <bits/stdc++.h>
#define int long long
using namespace std;
const int P = 998244353;
int i2 = 499122177, i6 = 166374059;
struct data {
  data() { f = g = h = 0; }
  int f, g, h;
};  // 三个函数打包
data calc(int n, int a, int b, int c) {
  int ac = a / c, bc = b / c, m = (a * n + b) / c, n1 = n + 1, n21 = n * 2 + 1;
  data d;
  if (a == 0) {  // 迭代到最底层
    d.f = bc * n1 % P;
    d.g = bc * n % P * n1 % P * i2 % P;
    d.h = bc * bc % P * n1 % P;
    return d;
  }
  if (a >= c || b >= c) {  // 取模
    d.f = n * n1 % P * i2 % P * ac % P + bc * n1 % P;
    d.g = ac * n % P * n1 % P * n21 % P * i6 % P + bc * n % P * n1 % P * i2 % P;
    d.h = ac * ac % P * n % P * n1 % P * n21 % P * i6 % P +
          bc * bc % P * n1 % P + ac * bc % P * n % P * n1 % P;
    d.f %= P, d.g %= P, d.h %= P;

    data e = calc(n, a % c, b % c, c);  // 迭代

    d.h += e.h + 2 * bc % P * e.f % P + 2 * ac % P * e.g % P;
    d.g += e.g, d.f += e.f;
    d.f %= P, d.g %= P, d.h %= P;
    return d;
  }
  data e = calc(m - 1, c, c - b - 1, a);
  d.f = n * m % P - e.f, d.f = (d.f % P + P) % P;
  d.g = m * n % P * n1 % P - e.h - e.f, d.g = (d.g * i2 % P + P) % P;
  d.h = n * m % P * (m + 1) % P - 2 * e.g - 2 * e.f - d.f;
  d.h = (d.h % P + P) % P;
  return d;
}
int T, n, a, b, c;
signed main() {
  scanf("%lld", &T);
  while (T--) {
    scanf("%lld%lld%lld%lld", &n, &a, &b, &c);
    data ans = calc(n, a, b, c);
    printf("%lld %lld %lld\n", ans.f, ans.h, ans.g);
  }
  return 0;
}
```

---

*build*Last update and/or translate time of this article ， Check the history
*edit*Found smelly bugs? Translation outdated? Wanna contribute with us? [Edit this Page on Github][98]
*people*Contributor of this article sshwy, FFjet
*translate*Translator of this article Visit the original article!
*copyright*The article is available under **[CC BY-SA 4.0][100] & [SATA][101]**; additional terms may apply.

## Comments


## Links

[1]: ../../contest/roadmap/
[2]: ../../contest/resources/
[3]: ../../contest/problemsetting/
[4]: ../../tools/judgers/
[5]: ../../tools/cmd/
[6]: ../../tools/wsl/
[7]: ../../tools/special-judge/
[8]: ../../tools/polygon/
[9]: ../../tools/oj-tool/
[10]: ../../tools/latex/
[11]: ../../lang/func/
[12]: ../../lang/file-op/
[13]: ../../lang/csl/algorithm/
[14]: ../../lang/csl/bitset/
[15]: ../../lang/csl/string/
[16]: ../../lang/c-cpp/
[17]: ../../lang/pas-cpp/
[18]: ../../lang/python/
[19]: ../../lang/java/
[20]: ../../basic/prefix-sum/
[21]: ../../basic/binary/
[22]: ../../basic/binary-lifting/
[23]: ../../basic/construction/
[24]: ../../dp/misc/
[25]: ../../string/sam/
[26]: ../../string/suffix-bst/
[27]: ../../string/general-sam/
[28]: ../../string/suffix-tree/
[29]: ../../string/manacher/
[30]: ../../string/pam/
[31]: ../../string/seq-automaton/
[32]: ../../string/minimal-string/
[33]: ../../string/lyndon/
[34]: ../bezouts/
[35]: ../inverse/
[36]: ../linear-equation/
[37]: ../crt/
[38]: ../quad-residue/
[39]: ../bsgs/
[40]: ../primitive-root/
[41]: ../lucas/
[42]: ../mobius/
[43]: ../du/
[44]: ../powerful-number/
[45]: ../min-25/
[46]: ../zhou/
[47]: ../pollard-rho/
[48]: ../continued-fraction/
[49]: ../stern-brocot/
[50]: ../pell-equation/
[51]: ../expectation/
[52]: ../permutation-group/
[53]: ../fibonacci/
[54]: ../game-theory/
[55]: ../newton/
[56]: ../integral/
[57]: ../dictionary/
[58]: ../../ds/monotonous-stack/
[59]: ../../ds/monotonous-queue/
[60]: ../../ds/sparse-table/
[61]: ../../ds/seg/
[62]: ../../ds/fenwick/
[63]: ../../ds/li-chao-tree/
[64]: ../../ds/seg-beats/
[65]: ../../ds/dividing/
[66]: ../../ds/skiplist/
[67]: ../../ds/kdt/
[68]: ../../ds/odt/
[69]: ../../ds/divide-combine/
[70]: ../../graph/matrix-tree/
[71]: ../../graph/dag/
[72]: ../../graph/topo/
[73]: ../../graph/mst/
[74]: ../../graph/mdst/
[75]: ../../graph/shortest-path/
[76]: ../../graph/node/
[77]: ../../graph/diff-constraints/
[78]: ../../graph/kth-path/
[79]: ../../graph/2-sat/
[80]: ../../graph/euler/
[81]: ../../graph/hamilton/
[82]: ../../graph/bi-graph/
[83]: ../../graph/min-circle/
[84]: ../../graph/planar/
[85]: ../../graph/color/
[86]: ../../graph/prufer/
[87]: ../../graph/lgv/
[88]: ../../graph/chord/
[89]: ../../misc/frac-programming/
[90]: ../../misc/hoverline/
[91]: ../../misc/cc-basic/
[92]: ../../misc/endianness/
[93]: ../../misc/josephus/
[94]: ../../misc/gray-code/
[95]: ../../misc/expression/
[96]: ../../misc/job-order/
[97]: ../../misc/main-element/
[98]: https://oiwiki-en.netlify.app/edit-landing/?ref=/math/euclidean.md
[99]: https://www.luogu.com.cn/problem/P5170
[100]: https://creativecommons.org/licenses/by-sa/4.0/deed
[101]: https://github.com/zTrix/sata-license
