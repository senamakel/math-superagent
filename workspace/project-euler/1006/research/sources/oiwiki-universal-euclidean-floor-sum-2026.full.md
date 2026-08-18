<!-- source: https://oi-wiki.org/math/number-theory/euclidean/ | converted from HTML -->

类欧几里德算法 - OI Wiki

跳转至

- 比赛相关
- 题型
- [学习路线][1]
- [学习资源][2]
- 技巧
- [出题][3]

- 工具软件
- 评测工具
- [命令行][4]
- [命令行编译与调试][5]
- [编译器][6]
- [WSL (Windows 10)][7]
- [Special Judge][8]
- Testlib
- [Polygon][9]
- [OJ 工具][10]
- [LaTeX 入门][11]
- [Git][12]

- 语言基础
- 高级数据类型
- [函数][13]
- [文件操作][14]

- C++ 标准库
- [STL 算法][15]
- [bitset][16]
- [string][17]
- [pair][18]

- C++ 进阶
- [编译优化][19]

- [C++ 与其他常用语言的区别][20]
- [Pascal 转 C++ 急救][21]
- [Python 速成][22]
- [Java 速成][23]
- [Java 进阶][24]

- 算法基础
- [枚举][25]
- [模拟][26]
- [递归 & 分治][27]
- [贪心][28]
- 排序
- [前缀和 & 差分][29]
- [二分][30]
- [倍增][31]
- [构造][32]

- 搜索
- 动态规划
- [其它 DP 方法][33]

- 字符串
- [后缀自动机 (SAM)][34]
- [后缀平衡树][35]
- [广义后缀自动机][36]
- [后缀树][37]
- [Manacher][38]
- [回文树][39]
- [序列自动机][40]
- [最小表示法][41]
- [Lyndon 分解][42]
- [Main–Lorentz 算法][43]

- 数学
- [位操作][44]
- [二进制集合操作][45]
- [高精度计算][46]
- [快速幂][47]
- [置换和排列][48]
- [弧度制与坐标系][49]
- [复数][50]
- 数论
- 万能欧几里得算法
- 习题
- 参考资料与注释

- [Meissel–Lehmer 算法][51]
- [连分数][52]
- [Stern–Brocot 树与 Farey 序列][53]
- [二次域][54]
- [Pell 方程][55]

- 多项式与生成函数
- 组合数学
- 线性代数
- 线性规划
- 抽象代数
- 概率论
- 博弈论
- 数值算法
- [序理论][56]
- [杨氏矩阵][57]
- [拟阵][58]
- [Berlekamp–Massey 算法][59]

- 数据结构
- 堆
- 块状数据结构
- [单调栈][60]
- [单调队列][61]
- [ST 表][62]
- [树状数组][63]
- 线段树
- [划分树][64]
- 二叉搜索树 & 平衡树
- [跳表][65]
- 可持久化数据结构
- 树套树
- [K-D Tree][66]
- 动态树
- [析合树][67]
- [PQ 树][68]
- [手指树][69]
- [霍夫曼树][70]

- 图论
- [有向无环图][71]
- [拓扑排序][72]
- 最短路问题
- 生成树问题
- [斯坦纳树][73]
- [拆点][74]
- 连通性相关
- [环计数问题][75]
- [最小环][76]
- [2-SAT][77]
- [欧拉图][78]
- [哈密顿图][79]
- [二分图][80]
- [平面图][81]
- [弦图][82]
- [图的着色][83]
- 网络流
- 图的匹配
- [Prüfer 序列][84]
- [矩阵树定理][85]
- [LGV 引理][86]
- [最大团搜索算法][87]
- [支配树][88]
- [图上随机游走][89]

- 计算几何
- 杂项

- [分数规划][90]
- 随机化
- [悬线法][91]
- [有限状态自动机][92]
- [计算理论基础][93]
- [字节顺序][94]
- [约瑟夫问题][95]
- [表达式求值][96]
- [在一台机器上规划任务][97]
- [主元素问题][98]
- [Garsia–Wachs 算法][99]
- [15-puzzle][100]
- [Kahan 求和][101]
- [珂朵莉树/颜色段均摊][102]
- [空间优化简介][103]

- 专题

- 万能欧几里得算法
- 习题
- 参考资料与注释

[104]

# 类欧几里德算法

## 引入

类欧几里德算法是洪华敦在 2016 年冬令营营员交流中提出的内容．它常用于解决形如

⌊ 𝑎 𝑖 + 𝑏 𝑐 ⌋ ⌊ a i + b c ⌋

结构的数列（下标为 𝑖 i ）的求和问题．它的主要想法是，利用分数自身的递归结构，将问题转化为更小规模的问题，递归求解．因为分数的递归结构和 [欧几里得算法][105] 存在直接的 [联系][106] ，因此，这一求和方法也称为类欧几里得算法．

因为 [连分数][52] 和 [Stern–Brocot 树][53] 等方法同样刻画了分数的递归结构，所以利用类欧几里得算法可以解决的问题，通常也可以用这些方法解决．与这些方法相比，类欧几里得算法通常更容易理解，它的实现也更为简明．

## 类欧几里得算法

最简单的例子，就是求和问题：

𝑓 ( 𝑎, 𝑏, 𝑐, 𝑛) = 𝑛 ∑ 𝑖 = 0 ⌊ 𝑎 𝑖 + 𝑏 𝑐 ⌋, f ( a, b, c, n) = ∑ i = 0 n ⌊ a i + b c ⌋,

其中， 𝑎, 𝑏, 𝑐, 𝑛 a, b, c, n 都是正整数．

### 代数解法

首先，将 𝑎, 𝑏 a, b 对 𝑐 c 取模，可以简化问题，将问题转化为 0 ≤ 𝑎, 𝑏 < 𝑐 0 ≤ a, b < c 的情形：

𝑓 ( 𝑎, 𝑏, 𝑐, 𝑛) = 𝑛 ∑ 𝑖 = 0 ⌊ 𝑎 𝑖 + 𝑏 𝑐 ⌋ = 𝑛 ∑ 𝑖 = 0 ⌊ ( ⌊ 𝑎 𝑐 ⌋ 𝑐 + ( 𝑎 m o d 𝑐)) 𝑖 + ( ⌊ 𝑏 𝑐 ⌋ 𝑐 + ( 𝑏 m o d 𝑐)) 𝑐 ⌋ = 𝑛 ∑ 𝑖 = 0 ( ⌊ 𝑎 𝑐 ⌋ 𝑖 + ⌊ 𝑏 𝑐 ⌋ + ⌊ ( 𝑎 m o d 𝑐) 𝑖 + ( 𝑏 m o d 𝑐) 𝑐 ⌋) = 𝑛 ( 𝑛 + 1) 2 ⌊ 𝑎 𝑐 ⌋ + ( 𝑛 + 1) ⌊ 𝑏 𝑐 ⌋ + 𝑓 ( 𝑎 m o d 𝑐, 𝑏 m o d 𝑐, 𝑐, 𝑛). f ( a, b, c, n) = ∑ i = 0 n ⌊ a i + b c ⌋ = ∑ i = 0 n ⌊ ( ⌊ a c ⌋ c + ( a mod c)) i + ( ⌊ b c ⌋ c + ( b mod c)) c ⌋ = ∑ i = 0 n ( ⌊ a c ⌋ i + ⌊ b c ⌋ + ⌊ ( a mod c) i + ( b mod c) c ⌋) = n ( n + 1) 2 ⌊ a c ⌋ + ( n + 1) ⌊ b c ⌋ + f ( a mod c, b mod c, c, n).

现在，考虑转化后的问题．令

𝑚 = ⌊ 𝑎 𝑛 + 𝑏 𝑐 ⌋. m = ⌊ a n + b c ⌋.

那么，原问题可以写作二次求和式：

𝑛 ∑ 𝑖 = 0 ⌊ 𝑎 𝑖 + 𝑏 𝑐 ⌋ = 𝑛 ∑ 𝑖 = 0 𝑚 − 1 ∑ 𝑗 = 0 [𝑗 < ⌊ 𝑎 𝑖 + 𝑏 𝑐 ⌋]. ∑ i = 0 n ⌊ a i + b c ⌋ = ∑ i = 0 n ∑ j = 0 m − 1 [j < ⌊ a i + b c ⌋].

交换求和次序，这需要对于每个 𝑗 j 计算满足条件的 𝑖 i 的范围．为此，将条件变形：

𝑗 < ⌊ 𝑎 𝑖 + 𝑏 𝑐 ⌋ = ⌈ 𝑎 𝑖 + 𝑏 + 1 𝑐 ⌉ − 1 ⟺ 𝑗 + 1 < ⌈ 𝑎 𝑖 + 𝑏 + 1 𝑐 ⌉ ⟺ 𝑗 + 1 < 𝑎 𝑖 + 𝑏 + 1 𝑐 ⟺ 𝑐 𝑗 + 𝑐 − 𝑏 − 1 𝑎 < 𝑖 ⟺ ⌊ 𝑐 𝑗 + 𝑐 − 𝑏 − 1 𝑎 ⌋ < 𝑖. j < ⌊ a i + b c ⌋ = ⌈ a i + b + 1 c ⌉ − 1 ⟺ j + 1 < ⌈ a i + b + 1 c ⌉ ⟺ j + 1 < a i + b + 1 c ⟺ c j + c − b − 1 a < i ⟺ ⌊ c j + c − b − 1 a ⌋ < i.

变形过程中多次利用了 [取整函数][107] 的性质．代入变形后的条件，原式可以写作：

\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor \right]\\ &=\sum_{j=0}^{m-1}\left(n-\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor\right)\\ &=nm-f\left(c,c-b-1,a,m-1\right). \end{aligned} " aria-hidden=true class=NCM-N display=true> \left\lfloor\frac{cj+c-b-1}{a}\right\rfloor \right]\\ &=\sum_{j=0}^{m-1}\left(n-\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor\right)\\ &=nm-f\left(c,c-b-1,a,m-1\right). \end{aligned}" style=min-width:19.391em> 𝑓 ( 𝑎, 𝑏, 𝑐, 𝑛) = 𝑚 − 1 ∑ 𝑗 = 0 𝑛 ∑ 𝑖 = 0 \left\lfloor\frac{cj+c-b-1}{a}\right\rfloor \right]" space=2> [𝑖 " space=4> > ⌊ 𝑐 𝑗 + 𝑐 − 𝑏 − 1 𝑎 ⌋] = 𝑚 − 1 ∑ 𝑗 = 0 ( 𝑛 − ⌊ 𝑐 𝑗 + 𝑐 − 𝑏 − 1 𝑎 ⌋) = 𝑛 𝑚 − 𝑓 ( 𝑐, 𝑐 − 𝑏 − 1, 𝑎, 𝑚 − 1). \left\lfloor\frac{cj+c-b-1}{a}\right\rfloor \right]\\&=\sum_{j=0}^{m-1}\left(n-\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor\right)\\&=nm-f\left(c,c-b-1,a,m-1\right).\end{aligned}" display=block xmlns=http://www.w3.org/1998/Math/MathML> \left\lfloor\frac{cj+c-b-1}{a}\right\rfloor \right]\\&=\sum_{j=0}^{m-1}\left(n-\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor\right)\\&=nm-f\left(c,c-b-1,a,m-1\right).\end{aligned}" columnspacing=0em displaystyle=true rowspacing=3pt> f ( a, b, c, n) = ∑ j = 0 m − 1 ∑ i = 0 n \left\lfloor\frac{cj+c-b-1}{a}\right\rfloor \right]" data-mjx-texclass=INNER> [i ">> ⌊ c j + c − b − 1 a ⌋] = ∑ j = 0 m − 1 ( n − ⌊ c j + c − b − 1 a ⌋) = n m − f ( c, c − b − 1, a, m − 1). \left\lfloor\frac{cj+c-b-1}{a}\right\rfloor \right]\\ &=\sum_{j=0}^{m-1}\left(n-\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor\right)\\ &=nm-f\left(c,c-b-1,a,m-1\right). \end{aligned} " src=data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7>

令 ( 𝑎 ′, 𝑏 ′, 𝑐 ′, 𝑛 ′) = ( 𝑐, 𝑐 − 𝑏 − 1, 𝑎, 𝑚 − 1) ( a ′, b ′, c ′, n ′) = ( c, c − b − 1, a, m − 1) ，这就又回到了前面讨论过的 c'" aria-hidden=true breakable=true class=NCM-N> 𝑎 ′ "> > 𝑐 ′ c'" xmlns=http://www.w3.org/1998/Math/MathML> a ′ ">> c ′ c'" src=data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7> 的情形．

将这两步转化结合在一起，可以发现在过程中， ( 𝑎, 𝑐) ( a, c) 不断地取模后交换位置，直到 𝑎 = 0 a = 0 ．这就类似于对 ( 𝑎, 𝑐) ( a, c) 进行辗转相除，这也是类欧几里德算法的得名．它的时间复杂度是 𝑂 ( l o g ⁡ m i n { 𝑎, 𝑐 }) O ( log ⁡ min { a, c }) 的．

在计算过程中，可能会出现 𝑚 = 0 m = 0 的情形，此时内层递归会出现 𝑛 = − 1 n = − 1 ．这并不影响最终的结果．但是，如果要求出现 𝑚 = 0 m = 0 时，直接终止算法，那么算法的时间复杂度可以改良为 𝑂 ( l o g ⁡ m i n { 𝑎, 𝑐, 𝑛 }) O ( log ⁡ min { a, c, n }) 的．

对复杂度的解释

利用该算法和欧几里得算法的相似性，很容易说明它的时间复杂度是 𝑂 ( l o g ⁡ m i n { 𝑎, 𝑐 }) O ( log ⁡ min { a, c }) 的．因此，只需要说明，如果在 𝑚 = 0 m = 0 时终止算法，那么它的时间复杂度也是 𝑂 ( l o g ⁡ 𝑛) O ( log ⁡ n) 的．

令 𝑚 = ⌊ ( 𝑎 𝑛 + 𝑏) / 𝑐 ⌋ m = ⌊ ( a n + b) / c ⌋ ，并记 𝑆 = 𝑚 𝑛 S = m n ， 𝑘 = 𝑚 / 𝑛 k = m / n ，它们分别相当于几何直观（见下一节）中点阵图的面积和直线的斜率．对于充分大的 𝑛 n ，近似有 𝑘 ≐ 𝑎 / 𝑐 k ≐ a / c ．

考察 𝑆 S 和 𝑘 k 在算法过程中的变化．第一步取模时， 𝑛 n 保持不变， 𝑘 k 近似由 𝑎 / 𝑐 a / c 变为 ( 𝑎 m o d 𝑐) / 𝑐 ( a mod c) / c ，相当于斜率由 𝑘 k 变为 𝑘 − ⌊ 𝑘 ⌋ k − ⌊ k ⌋ ，而 𝑆 S 也近似变为原来的 ( 𝑘 − ⌊ 𝑘 ⌋) ( k − ⌊ k ⌋) 倍．第二步交换横纵坐标时， 𝑆 S 近似保持不变， 𝑘 k 则变为它的倒数．因此，若设两步操作后，二元组 ( 𝑘, 𝑆) ( k, S) 变为 ( 𝑘 ′, 𝑆 ′) ( k ′, S ′) ，则有 𝑘 ′ = ( 𝑘 − ⌊ 𝑘 ⌋) − 1 k ′ = ( k − ⌊ k ⌋) − 1 且 𝑆 ′ = ( 𝑘 − ⌊ 𝑘 ⌋) 𝑆 S ′ = ( k − ⌊ k ⌋) S ．

因为 1 ≤ ⌊ 𝑘 ′ ⌋ ≤ 𝑘 ′ < ⌊ 𝑘 ′ ⌋ + 1 1 ≤ ⌊ k ′ ⌋ ≤ k ′ < ⌊ k ′ ⌋ + 1 ，所以，递归计算两轮后，乘积缩小的倍数最少为

( 𝑘 ′ − ⌊ 𝑘 ′ ⌋) ( 𝑘 − ⌊ 𝑘 ⌋) = 1 − ⌊ 𝑘 ′ ⌋ 𝑘 ′ < 1 − ⌊ 𝑘 ′ ⌋ ⌊ 𝑘 ′ ⌋ + 1 = 1 ⌊ 𝑘 ′ ⌋ + 1 ≤ 1 2. ( k ′ − ⌊ k ′ ⌋) ( k − ⌊ k ⌋) = 1 − ⌊ k ′ ⌋ k ′ < 1 − ⌊ k ′ ⌋ ⌊ k ′ ⌋ + 1 = 1 ⌊ k ′ ⌋ + 1 ≤ 1 2.

因此，至多 𝑂 ( l o g ⁡ 𝑆) O ( log ⁡ S) 轮，算法必然终止．因为从第二轮开始，每轮开始时的 𝑆 S 总是不超过上一轮取模结束后的 𝑆 S ，而后者大致为 𝑘 𝑛 2 k n 2 且 𝑘 < 1 k < 1 ，因而 𝑂 ( l o g ⁡ 𝑆) ⊆ 𝑂 ( l o g ⁡ 𝑛) O ( log ⁡ S) ⊆ O ( log ⁡ n) ．这就得到了上述结论．

模板题的参考实现如下：

模板题实现（ [Library Checker - Sum of Floor of Linear][108] ）

```
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
```

 |

```
#include <iostream>

long long solve(long long a, long long b, long long c, long long n) {
  long long n2 = n * (n + 1) / 2;
  if (a >= c || b >= c)
    return solve(a % c, b % c, c, n) + (a / c) * n2 + (b / c) * (n + 1);
  long long m = (a * n + b) / c;
  if (!m) return 0;
  return m * n - solve(c, c - b - 1, a, m - 1);
}

int main() {
  int t;
  std::cin >> t;
  for (; t; --t) {
    int a, b, c, n;
    std::cin >> n >> c >> a >> b;
    std::cout << solve(a, b, c, n - 1) << '\n';
  }
  return 0;
}
```

 |

### 几何直观

这个算法还可以从几何的角度理解．类欧几里得算法可以解决的问题主要是直线下整点计数问题．

如下图最左部分所示，该求和式相当于求直线

𝑦 = 𝑎 𝑥 + 𝑏 𝑐 y = a x + b c

下方， 𝑥 x 轴上方（不包括 𝑥 x 轴），且横坐标位于 [0, 𝑛] [0, n] 之间的格点数目．

首先，移除斜率和截距中的整数部分．这一步相当于将上图中间部分的蓝点数量单独计算出来．当斜率和截距都是整数时，蓝点一定构成一个梯形阵列，也就是说，不同纵列的格点形成等差数列，因而这些点的数量是容易计算的．将这些点移除后，剩余的格点和上图最右部分的红点数量一致．问题就转化成了斜率和截距都小于一的情形．因为梯形的高为 𝑛 + 1 n + 1 且两个底边长度分别为 ⌊ 𝑏 / 𝑐 ⌋ ⌊ b / c ⌋ 和 ( ⌊ 𝑎 / 𝑐 ⌋ 𝑛 + ⌊ 𝑏 / 𝑐 ⌋) ( ⌊ a / c ⌋ n + ⌊ b / c ⌋) ，所以，利用梯形面积公式，这一步骤可以归纳为算式

𝑓 ( 𝑎, 𝑏, 𝑐, 𝑛) = 𝑓 ( 𝑎 m o d 𝑐, 𝑏 m o d 𝑐, 𝑐, 𝑛) + 1 2 ( 𝑛 + 1) ( ⌊ 𝑏 𝑐 ⌋ + ( ⌊ 𝑎 𝑐 ⌋ 𝑛 + ⌊ 𝑏 𝑐 ⌋)). f ( a, b, c, n) = f ( a mod c, b mod c, c, n) + 1 2 ( n + 1) ( ⌊ b c ⌋ + ( ⌊ a c ⌋ n + ⌊ b c ⌋)).

然后，翻转横纵坐标轴．如下图最左部分所示，图中的红点和蓝点构成了一个横向长度为 𝑛 n 、纵向长度为 𝑚 = ⌊ ( 𝑎 𝑛 + 𝑏) / 𝑐 ⌋ m = ⌊ ( a n + b) / c ⌋ 的矩形点阵．要计算红点的数量，只需要计算蓝点的数量，再用矩形点阵的数量减去蓝点的数量即可．翻转后，上图左半部分中的蓝点点阵就变成了某条直线下的红色点阵．而且，翻转后，斜率大于一，就又回到了上文已经处理过的情形．

关键在于如何计算新的红色点阵上方的直线的方程．将上图最左部分的横纵坐标轴翻转，就得到上图中间部分．翻转后的红色点阵上方的直线（中间部分的实线），并非对应翻转前的直线（最左部分的实线），而是翻转前的直线向左上平移一点点的结果（最左部分的虚线）．这是因为，如果直接将直线（最左部分的实线）翻转，将得到中间部分的虚线，但是按照定义，它下方的格点包括恰好落在直线上的格点，这就会导致直线上的格点重复计数．为了避免这一点，需要将翻转直线 𝑦 = ( 𝑎 𝑥 + 𝑏) / 𝑐 y = ( a x + b) / c 后得到的直线 𝑦 = ( 𝑐 𝑥 − 𝑏) / 𝑎 y = ( c x − b) / a 向下平移一点点，得到直线 𝑦 = ( 𝑐 𝑥 − 𝑏 − 1) / 𝑎 y = ( c x − b − 1) / a ，这样它下方的点阵才恰为翻转前的蓝色点阵．

还有另一处细节需要处理．上图中间部分的直线的截距是负数，这意味着还没有回到之前的初始情形．要让截距恢复为非负数，只需要将直线（中间部分的实线）向左平移一个单位．这样做不会漏掉任何格点，因为翻转前的蓝色点阵中没有纵坐标为零的点，翻转后也就不存在横坐标为零的点．最后，直线方程就变为 𝑦 = ( 𝑐 𝑥 + 𝑐 − 𝑏 − 1) / 𝑎 y = ( c x + c − b − 1) / a ；同时，点阵的横坐标的上界也从 𝑚 m 变成了 𝑚 − 1 m − 1 ．这一步骤可以归纳为算式

𝑓 ( 𝑎, 𝑏, 𝑐, 𝑛) = 𝑚 𝑛 − 𝑓 ( 𝑐, 𝑐 − 𝑏 − 1, 𝑎, 𝑚 − 1). f ( a, b, c, n) = m n − f ( c, c − b − 1, a, m − 1).

这种递归的算法行得通，主要有两个原因：

- 第一，直线的斜率不断地先取小数部分再取倒数，这等价于计算直线斜率 𝑘 = 𝑎 / 𝑐 k = a / c 的 [连分数展开][106] ．因为有理分数的连分数展开的长度是 𝑂 ( l o g ⁡ m i n { 𝑎, 𝑐 }) O ( log ⁡ min { a, c }) 的，所以这一过程一定在 𝑂 ( l o g ⁡ m i n { 𝑎, 𝑐 }) O ( log ⁡ min { a, c }) 步后终止；
- 第二，因为每次翻转坐标轴的时候，直线斜率都是小于一的，因此，直觉上应该有 𝑚 < 𝑛 m < n ，也就是说，经过这样一轮迭代后，横坐标的范围一直是在缩小的．前文的复杂度计算中通过严格的分析说明，每两轮迭代后， 𝑛 n 至多为原来的一半，故而这一过程一定在 𝑂 ( l o g ⁡ 𝑛) O ( log ⁡ n) 步后终止．

这也是斜率为有理数时的类欧几里得算法的复杂度是 𝑂 ( l o g ⁡ m i n { 𝑎, 𝑐, 𝑛 }) O ( log ⁡ min { a, c, n }) 的原因．

利用类似的几何直观，可以将类欧几里得算法推广到斜率为无理数的情形，具体分析请参考后文的例题．

### 例题

[【模板】类欧几里得算法][109]

多组询问．给定正整数 𝑎, 𝑏, 𝑐, 𝑛 a, b, c, n ，求

𝑓 ( 𝑎, 𝑏, 𝑐, 𝑛) = 𝑛 ∑ 𝑖 = 0 ⌊ 𝑎 𝑖 + 𝑏 𝑐 ⌋, 𝑔 ( 𝑎, 𝑏, 𝑐, 𝑛) = 𝑛 ∑ 𝑖 = 0 𝑖 ⌊ 𝑎 𝑖 + 𝑏 𝑐 ⌋, ℎ ( 𝑎, 𝑏, 𝑐, 𝑛) = 𝑛 ∑ 𝑖 = 0 ⌊ 𝑎 𝑖 + 𝑏 𝑐 ⌋ 2. f ( a, b, c, n) = ∑ i = 0 n ⌊ a i + b c ⌋, g ( a, b, c, n) = ∑ i = 0 n i ⌊ a i + b c ⌋, h ( a, b, c, n) = ∑ i = 0 n ⌊ a i + b c ⌋ 2. 解答一

类似于 𝑓 f 的推导，可以得到 𝑔, ℎ g, h 的递归表达式．

首先，利用取模，将问题转化为 0 ≤ 𝑎, 𝑏 < 𝑐 0 ≤ a, b < c 的情形：

𝑔 ( 𝑎, 𝑏, 𝑐, 𝑛) = 𝑔 ( 𝑎 m o d 𝑐, 𝑏 m o d 𝑐, 𝑐, 𝑛) + ⌊ 𝑎 𝑐 ⌋ 𝑛 ( 𝑛 + 1) ( 2 𝑛 + 1) 6 + ⌊ 𝑏 𝑐 ⌋ 𝑛 ( 𝑛 + 1) 2, ℎ ( 𝑎, 𝑏, 𝑐, 𝑛) = ℎ ( 𝑎 m o d 𝑐, 𝑏 m o d 𝑐, 𝑐, 𝑛) + 2 ⌊ 𝑏 𝑐 ⌋ 𝑓 ( 𝑎 m o d 𝑐, 𝑏 m o d 𝑐, 𝑐, 𝑛) + 2 ⌊ 𝑎 𝑐 ⌋ 𝑔 ( 𝑎 m o d 𝑐, 𝑏 m o d 𝑐, 𝑐, 𝑛) + ⌊ 𝑎 𝑐 ⌋ 2 𝑛 ( 𝑛 + 1) ( 2 𝑛 + 1) 6 + ⌊ 𝑏 𝑐 ⌋ 2 ( 𝑛 + 1) + ⌊ 𝑎 𝑐 ⌋ ⌊ 𝑏 𝑐 ⌋ 𝑛 ( 𝑛 + 1). g ( a, b, c, n) = g ( a mod c, b mod c, c, n) + ⌊ a c ⌋ n ( n + 1) ( 2 n + 1) 6 + ⌊ b c ⌋ n ( n + 1) 2, h ( a, b, c, n) = h ( a mod c, b mod c, c, n) + 2 ⌊ b c ⌋ f ( a mod c, b mod c, c, n) + 2 ⌊ a c ⌋ g ( a mod c, b mod c, c, n) + ⌊ a c ⌋ 2 n ( n + 1) ( 2 n + 1) 6 + ⌊ b c ⌋ 2 ( n + 1) + ⌊ a c ⌋ ⌊ b c ⌋ n ( n + 1).

然后，利用交换求和次序，可以进一步转化．同样地，令

𝑚 = ⌊ 𝑎 𝑛 + 𝑏 𝑐 ⌋. m = ⌊ a n + b c ⌋.

那么，对于和式 𝑔 g ，有

\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor \right]\\ &=\sum_{j=0}^{m-1}\dfrac{1}{2}\left(\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor+n+1\right)\left(n-\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor\right)\\ &=\dfrac{1}{2}mn(n+1) - \dfrac{1}{2}\sum_{j=0}^{m-1}\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor - \dfrac{1}{2}\sum_{j=0}^{m-1}\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor^2\\ &=\dfrac{1}{2}mn(n+1) - \dfrac{1}{2}f(c,c-b-1,a,m-1) - \dfrac{1}{2}h(c,c-b-1,a,m-1). \end{aligned} " aria-hidden=true class=NCM-N display=true> \left\lfloor\frac{cj+c-b-1}{a}\right\rfloor \right]\\ &=\sum_{j=0}^{m-1}\dfrac{1}{2}\left(\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor+n+1\right)\left(n-\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor\right)\\ &=\dfrac{1}{2}mn(n+1) - \dfrac{1}{2}\sum_{j=0}^{m-1}\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor - \dfrac{1}{2}\sum_{j=0}^{m-1}\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor^2 \\ &=\dfrac{1}{2}mn(n+1) - \dfrac{1}{2}f(c,c-b-1,a,m-1) - \dfrac{1}{2}h(c,c-b-1,a,m-1). \end{aligned}" style=min-width:36.126em> 𝑔 ( 𝑎, 𝑏, 𝑐, 𝑛) = 𝑛 ∑ 𝑖 = 0 𝑖 ⌊ 𝑎 𝑖 + 𝑏 𝑐 ⌋ = 𝑛 ∑ 𝑖 = 0 𝑚 − 1 ∑ 𝑗 = 0 𝑖 [𝑗 < ⌊ 𝑎 𝑖 + 𝑏 𝑐 ⌋] = 𝑚 − 1 ∑ 𝑗 = 0 𝑛 ∑ 𝑖 = 0 𝑖 \left\lfloor\frac{cj+c-b-1}{a}\right\rfloor \right]" space=2> [𝑖 " space=4> > ⌊ 𝑐 𝑗 + 𝑐 − 𝑏 − 1 𝑎 ⌋] = 𝑚 − 1 ∑ 𝑗 = 0 1 2 ( ⌊ 𝑐 𝑗 + 𝑐 − 𝑏 − 1 𝑎 ⌋ + 𝑛 + 1) ( 𝑛 − ⌊ 𝑐 𝑗 + 𝑐 − 𝑏 − 1 𝑎 ⌋) = 1 2 𝑚 𝑛 ( 𝑛 + 1) − 1 2 𝑚 − 1 ∑ 𝑗 = 0 ⌊ 𝑐 𝑗 + 𝑐 − 𝑏 − 1 𝑎 ⌋ − 1 2 𝑚 − 1 ∑ 𝑗 = 0 ⌊ 𝑐 𝑗 + 𝑐 − 𝑏 − 1 𝑎 ⌋ 2 = 1 2 𝑚 𝑛 ( 𝑛 + 1) − 1 2 𝑓 ( 𝑐, 𝑐 − 𝑏 − 1, 𝑎, 𝑚 − 1) − 1 2 ℎ ( 𝑐, 𝑐 − 𝑏 − 1, 𝑎, 𝑚 − 1). \left\lfloor\frac{cj+c-b-1}{a}\right\rfloor \right]\\&=\sum_{j=0}^{m-1}\dfrac{1}{2}\left(\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor+n+1\right)\left(n-\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor\right)\\&=\dfrac{1}{2}mn(n+1) - \dfrac{1}{2}\sum_{j=0}^{m-1}\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor - \dfrac{1}{2}\sum_{j=0}^{m-1}\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor^2\\&=\dfrac{1}{2}mn(n+1) - \dfrac{1}{2}f(c,c-b-1,a,m-1) - \dfrac{1}{2}h(c,c-b-1,a,m-1).\end{aligned}" display=block xmlns=http://www.w3.org/1998/Math/MathML> \left\lfloor\frac{cj+c-b-1}{a}\right\rfloor \right]\\&=\sum_{j=0}^{m-1}\dfrac{1}{2}\left(\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor+n+1\right)\left(n-\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor\right)\\&=\dfrac{1}{2}mn(n+1) - \dfrac{1}{2}\sum_{j=0}^{m-1}\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor - \dfrac{1}{2}\sum_{j=0}^{m-1}\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor^2 \\&=\dfrac{1}{2}mn(n+1) - \dfrac{1}{2}f(c,c-b-1,a,m-1) - \dfrac{1}{2}h(c,c-b-1,a,m-1).\end{aligned}" columnspacing=0em displaystyle=true rowspacing=3pt> g ( a, b, c, n) = ∑ i = 0 n i ⌊ a i + b c ⌋ = ∑ i = 0 n ∑ j = 0 m − 1 i [j < ⌊ a i + b c ⌋] = ∑ j = 0 m − 1 ∑ i = 0 n i \left\lfloor\frac{cj+c-b-1}{a}\right\rfloor \right]" data-mjx-texclass=INNER> [i ">> ⌊ c j + c − b − 1 a ⌋] = ∑ j = 0 m − 1 1 2 ( ⌊ c j + c − b − 1 a ⌋ + n + 1) ( n − ⌊ c j + c − b − 1 a ⌋) = 1 2 m n ( n + 1) − 1 2 ∑ j = 0 m − 1 ⌊ c j + c − b − 1 a ⌋ − 1 2 ∑ j = 0 m − 1 ⌊ c j + c − b − 1 a ⌋ 2 = 1 2 m n ( n + 1) − 1 2 f ( c, c − b − 1, a, m − 1) − 1 2 h ( c, c − b − 1, a, m − 1). \left\lfloor\frac{cj+c-b-1}{a}\right\rfloor \right]\\ &=\sum_{j=0}^{m-1}\dfrac{1}{2}\left(\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor+n+1\right)\left(n-\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor\right)\\ &=\dfrac{1}{2}mn(n+1) - \dfrac{1}{2}\sum_{j=0}^{m-1}\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor - \dfrac{1}{2}\sum_{j=0}^{m-1}\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor^2\\ &=\dfrac{1}{2}mn(n+1) - \dfrac{1}{2}f(c,c-b-1,a,m-1) - \dfrac{1}{2}h(c,c-b-1,a,m-1). \end{aligned} " src=data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7>

对于和式 ℎ h ，有

\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor \right]\\ &=\sum_{j=0}^{m-1}(2j+1)\left(n-\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor\right)\\ &=nm^2 - \sum_{j=0}^{m-1}\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor - 2\sum_{j=0}^{m-1}j\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor\\ &=nm^2 - f(c,c-b-1,a,m-1) - 2g(c,c-b-1,a,m-1). \end{aligned} " aria-hidden=true class=NCM-N display=true> \left\lfloor\frac{cj+c-b-1}{a}\right\rfloor \right]\\ &=\sum_{j=0}^{m-1}(2j+1)\left(n-\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor\right)\\ &=nm^2 - \sum_{j=0}^{m-1}\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor - 2\sum_{j=0}^{m-1}j\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor\\ &=nm^2 - f(c,c-b-1,a,m-1) - 2g(c,c-b-1,a,m-1). \end{aligned}" style=min-width:31.142em> ℎ ( 𝑎, 𝑏, 𝑐, 𝑛) = 𝑛 ∑ 𝑖 = 0 ⌊ 𝑎 𝑖 + 𝑏 𝑐 ⌋ 2 = 𝑛 ∑ 𝑖 = 0 𝑚 − 1 ∑ 𝑗 = 0 ( 2 𝑗 + 1) [𝑗 < ⌊ 𝑎 𝑖 + 𝑏 𝑐 ⌋] = 𝑚 − 1 ∑ 𝑗 = 0 𝑛 ∑ 𝑖 = 0 ( 2 𝑗 + 1) \left\lfloor\frac{cj+c-b-1}{a}\right\rfloor \right]" space=2> [𝑖 " space=4> > ⌊ 𝑐 𝑗 + 𝑐 − 𝑏 − 1 𝑎 ⌋] = 𝑚 − 1 ∑ 𝑗 = 0 ( 2 𝑗 + 1) ( 𝑛 − ⌊ 𝑐 𝑗 + 𝑐 − 𝑏 − 1 𝑎 ⌋) = 𝑛 𝑚 2 − 𝑚 − 1 ∑ 𝑗 = 0 ⌊ 𝑐 𝑗 + 𝑐 − 𝑏 − 1 𝑎 ⌋ − 2 𝑚 − 1 ∑ 𝑗 = 0 𝑗 ⌊ 𝑐 𝑗 + 𝑐 − 𝑏 − 1 𝑎 ⌋ = 𝑛 𝑚 2 − 𝑓 ( 𝑐, 𝑐 − 𝑏 − 1, 𝑎, 𝑚 − 1) − 2 𝑔 ( 𝑐, 𝑐 − 𝑏 − 1, 𝑎, 𝑚 − 1). \left\lfloor\frac{cj+c-b-1}{a}\right\rfloor \right]\\&=\sum_{j=0}^{m-1}(2j+1)\left(n-\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor\right)\\&=nm^2 - \sum_{j=0}^{m-1}\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor - 2\sum_{j=0}^{m-1}j\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor\\&=nm^2 - f(c,c-b-1,a,m-1) - 2g(c,c-b-1,a,m-1).\end{aligned}" display=block xmlns=http://www.w3.org/1998/Math/MathML> \left\lfloor\frac{cj+c-b-1}{a}\right\rfloor \right]\\&=\sum_{j=0}^{m-1}(2j+1)\left(n-\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor\right)\\&=nm^2 - \sum_{j=0}^{m-1}\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor - 2\sum_{j=0}^{m-1}j\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor\\&=nm^2 - f(c,c-b-1,a,m-1) - 2g(c,c-b-1,a,m-1).\end{aligned}" columnspacing=0em displaystyle=true rowspacing=3pt> h ( a, b, c, n) = ∑ i = 0 n ⌊ a i + b c ⌋ 2 = ∑ i = 0 n ∑ j = 0 m − 1 ( 2 j + 1) [j < ⌊ a i + b c ⌋] = ∑ j = 0 m − 1 ∑ i = 0 n ( 2 j + 1) \left\lfloor\frac{cj+c-b-1}{a}\right\rfloor \right]" data-mjx-texclass=INNER> [i ">> ⌊ c j + c − b − 1 a ⌋] = ∑ j = 0 m − 1 ( 2 j + 1) ( n − ⌊ c j + c − b − 1 a ⌋) = n m 2 − ∑ j = 0 m − 1 ⌊ c j + c − b − 1 a ⌋ − 2 ∑ j = 0 m − 1 j ⌊ c j + c − b − 1 a ⌋ = n m 2 − f ( c, c − b − 1, a, m − 1) − 2 g ( c, c − b − 1, a, m − 1). \left\lfloor\frac{cj+c-b-1}{a}\right\rfloor \right]\\ &=\sum_{j=0}^{m-1}(2j+1)\left(n-\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor\right)\\ &=nm^2 - \sum_{j=0}^{m-1}\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor - 2\sum_{j=0}^{m-1}j\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor\\ &=nm^2 - f(c,c-b-1,a,m-1) - 2g(c,c-b-1,a,m-1). \end{aligned} " src=data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7>

从几何直观的角度看，这些非线性的求和式相当于给区域中的每个点 ( 𝑖, 𝑗) ( i, j) 都赋予了相应的权重 𝑤 ( 𝑖, 𝑗) w ( i, j) ．除了这些权重之外，其余部分的计算过程是完全一致的．对于权重的选择，一般地，有

𝑛 ∑ 𝑖 = 0 𝑖 𝑟 ⌊ 𝑎 𝑖 + 𝑏 𝑐 ⌋ 𝑠 = 𝑛 ∑ 𝑖 = 0 𝑚 − 1 ∑ 𝑗 = 0 𝑖 𝑟 ( ( 𝑗 + 1) 𝑠 − 𝑗 𝑠) [𝑗 < ⌊ 𝑎 𝑖 + 𝑏 𝑐 ⌋]. ∑ i = 0 n i r ⌊ a i + b c ⌋ s = ∑ i = 0 n ∑ j = 0 m − 1 i r ( ( j + 1) s − j s) [j < ⌊ a i + b c ⌋].

本题的另一个特点是， 𝑔 g 和 ℎ h 在递归计算时，会相互交错．因此，需要将 ( 𝑓, 𝑔, ℎ) ( f, g, h) 作为三元组同时递归．

```
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
```

 |

```
#include <iostream>

struct Data {
  int f, g, h;
};

Data solve(long long a, long long b, long long c, long long n) {
  constexpr long long M = 998244353;
  constexpr long long i2 = (M + 1) / 2;
  constexpr long long i6 = (M + 1) / 6;
  long long n2 = (n + 1) * n % M * i2 % M;
  long long n3 = (2 * n + 1) * (n + 1) % M * n % M * i6 % M;
  Data res = {0, 0, 0};
  if (a >= c || b >= c) {
    auto tmp = solve(a % c, b % c, c, n);
    long long aa = a / c, bb = b / c;
    res.f = (tmp.f + aa * n2 + bb * (n + 1)) % M;
    res.g = (tmp.g + aa * n3 + bb * n2) % M;
    res.h = (tmp.h + 2 * bb * tmp.f % M + 2 * aa * tmp.g % M +
             aa * aa % M * n3 % M + bb * bb % M * (n + 1) % M +
             2 * aa * bb % M * n2 % M) %
            M;
    return res;
  }
  long long m = (a * n + b) / c;
  if (!m) return res;
  auto tmp = solve(c, c - b - 1, a, m - 1);
  res.f = (m * n - tmp.f + M) % M;
  res.g = (m * n2 + (M - tmp.f) * i2 + (M - tmp.h) * i2) % M;
  res.h = (n * m % M * m - tmp.f - tmp.g * 2 + 3 * M) % M;
  return res;
}

int main() {
  int t;
  std::cin >> t;
  for (; t; --t) {
    int n, a, b, c;
    std::cin >> n >> a >> b >> c;
    auto res = solve(a, b, c, n);
    std::cout << res.f << ' ' << res.h << ' ' << res.g << '\n';
  }
  return 0;
}
```

 |

[[清华集训 2014] Sum][110]

多组询问．给定正整数 𝑛 n 和 𝑟 r ，求

𝑛 ∑ 𝑑 = 1 ( − 1) ⌊ 𝑑 √ 𝑟 ⌋. ∑ d = 1 n ( − 1) ⌊ d r ⌋. 解答一

如果 𝑟 r 是完全平方数，那么当 √ 𝑟 r 为偶数时，和式为 𝑛 n ；否则，和式依据 𝑛 n 奇偶性不同，在 0 0 和 − 1 − 1 之间交替变化．下面考虑 𝑟 r 不是完全平方数的情形．

为了应用类欧几里得算法，首先将求和式转化为熟悉的形式：

𝑛 ∑ 𝑑 = 1 ( − 1) ⌊ 𝑑 √ 𝑟 ⌋ = 𝑛 ∑ 𝑑 = 1 ( 1 − 2 ( ⌊ 𝑑 √ 𝑟 ⌋ m o d 2)) = 𝑛 − 2 𝑛 ∑ 𝑑 = 1 ( ⌊ 𝑑 √ 𝑟 ⌋ − 2 ⌊ ⌊ 𝑑 √ 𝑟 ⌋ 2 ⌋) = 𝑛 − 2 𝑛 ∑ 𝑑 = 1 ⌊ 𝑑 √ 𝑟 ⌋ + 4 𝑛 ∑ 𝑑 = 1 ⌊ 𝑑 √ 𝑟 2 ⌋ = 𝑛 − 2 𝑓 ( 𝑛, 1, 0, 1) + 4 𝑓 ( 𝑛, 1, 0, 2) ∑ d = 1 n ( − 1) ⌊ d r ⌋ = ∑ d = 1 n ( 1 − 2 ( ⌊ d r ⌋ mod 2)) = n − 2 ∑ d = 1 n ( ⌊ d r ⌋ − 2 ⌊ ⌊ d r ⌋ 2 ⌋) = n − 2 ∑ d = 1 n ⌊ d r ⌋ + 4 ∑ d = 1 n ⌊ d r 2 ⌋ = n − 2 f ( n, 1, 0, 1) + 4 f ( n, 1, 0, 2)

其中的函数 𝑓 f 具有形式

𝑓 ( 𝑎, 𝑏, 𝑐, 𝑛) = 𝑛 ∑ 𝑖 = 1 ⌊ 𝑎 √ 𝑟 + 𝑏 𝑐 𝑖 ⌋. f ( a, b, c, n) = ∑ i = 1 n ⌊ a r + b c i ⌋.

与正文中的算法不同的是，此处的斜率不再是有理数．设斜率

𝑘 = 𝑎 √ 𝑟 + 𝑏 𝑐. k = a r + b c.

同样分为两种情形讨论．如果 𝑘 ≥ 1 k ≥ 1 ，那么

𝑓 ( 𝑎, 𝑏, 𝑐, 𝑛) = 𝑛 ∑ 𝑖 = 1 ⌊ 𝑘 𝑖 ⌋ = 𝑛 ∑ 𝑖 = 1 ⌊ ( 𝑘 − ⌊ 𝑘 ⌋) 𝑖 ⌋ + ⌊ 𝑘 ⌋ 𝑛 ∑ 𝑖 = 1 𝑖 = ⌊ 𝑘 ⌋ 𝑛 ( 𝑛 + 1) 2 + 𝑓 ( 𝑎, 𝑏 − 𝑐 ⌊ 𝑘 ⌋, 𝑐, 𝑛). f ( a, b, c, n) = ∑ i = 1 n ⌊ k i ⌋ = ∑ i = 1 n ⌊ ( k − ⌊ k ⌋) i ⌋ + ⌊ k ⌋ ∑ i = 1 n i = ⌊ k ⌋ n ( n + 1) 2 + f ( a, b − c ⌊ k ⌋, c, n).

问题转化为斜率小于一的情形．如果 𝑘 < 1 k < 1 ，那么设 𝑚 = ⌊ 𝑛 𝑘 ⌋ m = ⌊ n k ⌋ ，有

\lfloor k^{-1}j\rfloor] = nm - \sum_{j=1}^m\sum_{i=1}^n[i\le\lfloor k^{-1}j\rfloor]. \end{aligned} " aria-hidden=true class=NCM-N display=true> \lfloor k^{-1}j\rfloor] = nm - \sum_{j=1}^m\sum_{i=1}^n[i\le\lfloor k^{-1}j\rfloor]. \end{aligned}" style=min-width:26.494em> 𝑓 ( 𝑎, 𝑏, 𝑐, 𝑛) = 𝑛 ∑ 𝑖 = 1 ⌊ 𝑘 𝑖 ⌋ = 𝑛 ∑ 𝑖 = 1 𝑚 ∑ 𝑗 = 1 [𝑗 ≤ ⌊ 𝑘 𝑖 ⌋] = 𝑚 ∑ 𝑗 = 1 𝑛 ∑ 𝑖 = 1 [𝑖 " space=4> > ⌊ 𝑘 − 1 𝑗 ⌋] = 𝑛 𝑚 − 𝑚 ∑ 𝑗 = 1 𝑛 ∑ 𝑖 = 1 [𝑖 ≤ ⌊ 𝑘 − 1 𝑗 ⌋]. \lfloor k^{-1}j\rfloor] = nm - \sum_{j=1}^m\sum_{i=1}^n[i\le\lfloor k^{-1}j\rfloor].\end{aligned}" display=block xmlns=http://www.w3.org/1998/Math/MathML> \lfloor k^{-1}j\rfloor] = nm - \sum_{j=1}^m\sum_{i=1}^n[i\le\lfloor k^{-1}j\rfloor].\end{aligned}" columnspacing=0em displaystyle=true rowspacing=3pt> f ( a, b, c, n) = ∑ i = 1 n ⌊ k i ⌋ = ∑ i = 1 n ∑ j = 1 m [j ≤ ⌊ k i ⌋] = ∑ j = 1 m ∑ i = 1 n [i ">> ⌊ k − 1 j ⌋] = n m − ∑ j = 1 m ∑ i = 1 n [i ≤ ⌊ k − 1 j ⌋]. \lfloor k^{-1}j\rfloor] = nm - \sum_{j=1}^m\sum_{i=1}^n[i\le\lfloor k^{-1}j\rfloor]. \end{aligned} " src=data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7>

此处的推导中，交换 𝑖 i 和 𝑗 j 的条件比正文中的情形更为简单，是因为直线 𝑦 = 𝑘 𝑥 y = k x 上没有除了原点之外的格点．关键在于交换后的求和式写成 𝑓 ( 𝑎, 𝑏, 𝑐, 𝑛) f ( a, b, c, n) 的形式，这相当于要求 𝑎 ′, 𝑏 ′, 𝑐 ′ a ′, b ′, c ′ 满足

𝑘 − 1 = 𝑎 ′ √ 𝑟 + 𝑏 ′ 𝑐 ′. k − 1 = a ′ r + b ′ c ′.

这并不困难，只需要将分母有理化，就能得到

𝑘 − 1 = 𝑐 𝑎 √ 𝑟 + 𝑏 = 𝑐 𝑎 √ 𝑟 − 𝑐 𝑏 𝑎 2 𝑟 − 𝑏 2. k − 1 = c a r + b = c a r − c b a 2 r − b 2.

因此，有

𝑎 ′ = 𝑐 𝑎, 𝑏 ′ = − 𝑐 𝑏, 𝑐 ′ = 𝑎 2 𝑟 − 𝑏 2. a ′ = c a, b ′ = − c b, c ′ = a 2 r − b 2.

这说明

𝑓 ( 𝑎, 𝑏, 𝑐, 𝑛) = 𝑛 𝑚 − 𝑓 ( 𝑐 𝑎, − 𝑐 𝑏, 𝑎 2 𝑟 − 𝑏 2, 𝑚). f ( a, b, c, n) = n m − f ( c a, − c b, a 2 r − b 2, m).

为了避免整数溢出，需要每次都将 𝑎, 𝑏, 𝑐 a, b, c 同除以它们的最大公约数．因为这个计算过程和计算 𝑘 k 的连分数的过程完全一致，所以根据 [连分数理论][111] ，只要保证 g c d ( 𝑎, 𝑏, 𝑐) = 1 gcd ( a, b, c) = 1 ，它们在计算过程中必然在整型范围内．另外，尽管 ( 𝑎, 𝑏, 𝑐, 𝑛) ( a, b, c, n) 不会溢出，但是在该题数据范围下， 𝑓 ( 𝑎, 𝑏, 𝑐, 𝑛) f ( a, b, c, n) 可能会超过 6 4 64 位整数的范围，自然溢出即可，无需额外处理，最后结果一定在 [− 𝑛, 𝑛] [− n, n] 之间．

尽管斜率不会变为零，算法的复杂度仍然是 𝑂 ( l o g ⁡ 𝑛) O ( log ⁡ n) 的，这一点从前文关于算法复杂度的论证容易看出．

```
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
```

 |

```
#include <cmath>
#include <iostream>

long long r;
long double sqrt_r;

long long gcd(long long a, long long b) { return b ? gcd(b, a % b) : a; }

unsigned long long f(long long a, long long b, long long c, long long n) {
  if (!n) return 0;
  auto d = gcd(a, gcd(b, c));
  a /= d;
  b /= d;
  c /= d;
  unsigned long long k = (a * sqrt_r + b) / c;
  if (k) {
    return n * (n + 1) / 2 * k + f(a, b - c * k, c, n);
  } else {
    unsigned long long m = n * (a * sqrt_r + b) / c;
    return n * m - f(c * a, -c * b, a * a * r - b * b, m);
  }
}

unsigned long long solve(long long n, long long r) {
  long long sqr = sqrt_r = sqrtl(r);
  if (r == sqr * sqr) return r % 2 ? (n % 2 ? -1 : 0) : n;
  return n - 2 * f(1, 0, 1, n) + 4 * f(1, 0, 2, n);
}

int main() {
  int t;
  std::cin >> t;
  for (; t; --t) {
    int n;
    std::cin >> n >> r;
    long long res = solve(n, r);
    std::cout << res << '\n';
  }
  return 0;
}
```

 |

[Fraction][112]

给定正整数 𝑎, 𝑏, 𝑐, 𝑑 a, b, c, d ，求所有满足 𝑎 / 𝑏 < 𝑝 / 𝑞 < 𝑐 / 𝑑 a / b < p / q < c / d 的最简分数 𝑝 / 𝑞 p / q 中 ( 𝑞, 𝑝) ( q, p) 的字典序最小的那个．

解答

这道题目也是 [Stern–Brocot 树][53] 的经典应用，相关题解可以在 [此处][113] 找到．因为它只依赖于分数的递归结构，所以它同样可以利用类似欧几里得算法的方法求解，故而也可以视作类欧几里得算法的一个应用．

如果 𝑎 / 𝑏 a / b 和 𝑐 / 𝑑 c / d 之间（不含端点）存在至少一个自然数，可以直接取 ( 𝑞, 𝑝) = ( 1, ⌊ 𝑎 / 𝑏 ⌋ + 1) ( q, p) = ( 1, ⌊ a / b ⌋ + 1) ．否则，必然有

⌊ 𝑎 𝑏 ⌋ ≤ 𝑎 𝑏 < 𝑝 𝑞 < 𝑐 𝑑 ≤ ⌊ 𝑎 𝑏 ⌋ + 1. ⌊ a b ⌋ ≤ a b < p q < c d ≤ ⌊ a b ⌋ + 1.

从这个不等式中可以看出， 𝑝 / 𝑞 p / q 的整数部分可以确定为 ⌊ 𝑎 / 𝑏 ⌋ ⌊ a / b ⌋ ，直接消去该整数部分，然后整体取倒数，用于确定它的小数部分．这正是确定 𝑝 / 𝑞 p / q 的连分数的 [基本方法][106] ．若最终的答案是 𝑝 / 𝑞 p / q ，那么算法的时间复杂度为 𝑂 ( l o g ⁡ m i n { 𝑝, 𝑞 }) O ( log ⁡ min { p, q }) ．

此处，有一个细节问题，即取倒数之后得到的字典序最小的分数，是否是取倒数之前的字典序最小的分数．换句话说，满足 𝑎 / 𝑏 < 𝑝 / 𝑞 < 𝑐 / 𝑑 a / b < p / q < c / d 的分数 𝑝 / 𝑞 p / q 中，字典序 ( 𝑞, 𝑝) ( q, p) 最小的，是否也是字典序 ( 𝑝, 𝑞) ( p, q) 最小的．假设不然，设 𝑝 / 𝑞 p / q 是字典序 ( 𝑞, 𝑝) ( q, p) 最小的，但是 𝑟 / 𝑠 ≠ 𝑝 / 𝑞 r / s ≠ p / q 是字典序 ( 𝑟, 𝑠) ( r, s) 最小的．这必然有 𝑟 < 𝑝 r < p 且 𝑞 < 𝑠 q < s ．但是，这说明

𝑎 𝑏 < 𝑟 𝑠 < 𝑟 𝑞 < 𝑝 𝑞 < 𝑐 𝑑. a b < r s < r q < p q < c d.

因此， 𝑟 / 𝑞 r / q 无论按照哪个字典序怎样都是严格更小于当前解的．这与所设条件矛盾．因此，上述算法是正确的．

```
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
```

 |

```
#include <iostream>

void solve(int a, int b, int& p, int& q, int c, int d) {
  if ((a / b + 1) * d < c) {
    p = a / b + 1;
    q = 1;
  } else {
    solve(d, c - d * (a / b), q, p, b, a % b);
    p += q * (a / b);
  }
}

int main() {
  int a, b, c, d, p, q;
  while (std::cin >> a >> b >> c >> d) {
    solve(a, b, p, q, c, d);
    std::cout << p << '/' << q << '\n';
  }
  return 0;
}
```

 |

## 万能欧几里得算法

上一节讨论的类欧几里得算法推导通常较为繁琐，而且能够解决的和式主要是可以转化为直线下（带权）整点计数问题的和式．本节讨论一种更为一般的方法，它进一步抽象了上述过程，从而可以解决更多的问题．因此，这一方法也称为万能欧几里得算法．它同样利用了分数的递归结构求解问题，但是与类欧几里得算法约化问题的思路稍有不同．

仍然考虑最经典的求和问题：

𝑓 ( 𝑎, 𝑏, 𝑐, 𝑛) = 𝑛 ∑ 𝑖 = 1 ⌊ 𝑎 𝑖 + 𝑏 𝑐 ⌋, f ( a, b, c, n) = ∑ i = 1 n ⌊ a i + b c ⌋,

其中， 𝑎, 𝑏, 𝑐, 𝑛 a, b, c, n 都是正整数．

### 问题转化

设参数为 ( 𝑎, 𝑏, 𝑐, 𝑛) ( a, b, c, n) 的线段为

𝑦 = 𝑎 𝑥 + 𝑏 𝑐, 0 < 𝑥 ≤ 𝑛. y = a x + b c, 0 < x ≤ n.

对于这条线段，可以按照如下方法定义一个由 𝑈 U 和 𝑅 R 组成的字符串 𝑆 S ，也称为 **操作序列**：

- 字符串恰有 𝑛 n 个 𝑅 R 和 𝑚 = ⌊ ( 𝑎 𝑛 + 𝑏) / 𝑐 ⌋ m = ⌊ ( a n + b) / c ⌋ 个 𝑈 U 组成；
- 第 𝑖 i 个 𝑅 R 前方的 𝑈 U 的数量恰等于 ⌊ ( 𝑎 𝑖 + 𝑏) / 𝑐 ⌋ ⌊ ( a i + b) / c ⌋ ，其中， 𝑖 = 1, ⋯, 𝑛 i = 1, ⋯, n ．

从几何直观上看，这大致相当于从原点开始，每向右穿过一次竖向的网格线，就写下一个 𝑅 R ，每向上穿过一次横向的网格线，就写下一个 𝑈 U ．如下图所示：

当然，这样的定义还需要考量一系列特殊情形：

- 经过整点（即同时上穿和右穿）时，需要先写 𝑈 U 再写 𝑅 R ；
- 字符串开始时，除了在 ( 0, 1] ( 0, 1] 区间内上穿网格线的次数外，还需要格外补充 ⌊ 𝑏 / 𝑐 ⌋ ⌊ b / c ⌋ 个 𝑈 U ；
- 字符串结束时，不能有格外的 𝑈 U ．

如果对于几何直观的描述有任何不明晰的地方，可以参考上述代数方法的定义辅助理解．几何直观的描述，有助于理解下文的算法过程．

万能欧几里得算法的基本思路，就是将操作序列中的 𝑈 U 和 𝑅 R 都视作某个 [幺半群][114] 内的元素，将整个操作序列视为幺半群内元素的乘积，而问题最终的答案与这个乘积有关．

比如，本题中，可以定义状态向量 𝑣 = ( 1, 𝑦, ∑ 𝑦) v = ( 1, y, ∑ y) ，表示自原点开始，经历了若干次上穿和右穿网格线后，当前的状态．其中，第一个分量是常数，第二个分量是纵坐标 𝑦 y ，第三个分量是要求的和式．起始时，有 𝑣 = ( 1, 0, 0) v = ( 1, 0, 0) ．每向上穿过一次网格线，纵坐标就累加一，即相当于将状态向量右乘以矩阵

𝑈 = ⎛ ⎜ ⎜ ⎜ ⎝ 1 1 0 0 1 0 0 0 1 ⎞ ⎟ ⎟ ⎟ ⎠. U = ( 1 1 0 0 1 0 0 0 1).

每向右穿过一次网格线，和式就累加一次纵坐标，即相当于将状态向量右乘以矩阵

𝑅 = ⎛ ⎜ ⎜ ⎜ ⎝ 1 0 0 0 1 1 0 0 1 ⎞ ⎟ ⎟ ⎟ ⎠. R = ( 1 0 0 0 1 1 0 0 1).

因此，最终的状态就是乘积 ( 1, 0, 0) 𝑆 ( 1, 0, 0) S ，其中， 𝑆 S 理解为上述矩阵的乘积．所求的答案，就是最终状态的第三个分量．

除了将幺半群中的元素定义为矩阵以外，还可以将它们定义为一段操作序列对于最终结果的贡献，然后将操作的乘积定义为两段操作序列的贡献的合并．

本题中，可以定义每段操作序列的贡献为 ( 𝑥, 𝑦, ∑ 𝑦) ( x, y, ∑ y) ．为了严谨地解释这些记号，可以将这些分量都看作是操作序列的函数，也就是说，对于操作序列 𝑆 S ，它的贡献可以写作 ( 𝑥 ( 𝑆), 𝑦 ( 𝑆), ( ∑ 𝑦) ( 𝑆)) ( x ( S), y ( S), ( ∑ y) ( S)) ．其中， 𝑥 ( 𝑆) x ( S) 和 𝑦 ( 𝑆) y ( S) 分别对应着操作序列 𝑆 S 中 𝑅 R 和 𝑈 U 的数量，也就是该线段右穿和上穿网格线的次数．最后一项中的求和符号，一般地，有如下定义：对于操作序列上的函数 𝑓 ( 𝑆) f ( S) ，可以定义 ( ∑ 𝑓) ( 𝑆) ( ∑ f) ( S) ，或记作 ∑ 𝑆 𝑓 ∑ S f ，为下面的表达式：

∑ 𝑆 𝑓: = ∑ { 𝑓 ( 𝑆 [1, 𝑟]): 𝑆 𝑟 = 𝑅 }. ∑ S f:= ∑ { f ( S [1, r]): S r = R }.

其中， 𝑆 𝑟 S r 是 𝑆 S 中的第 𝑟 r 个字符， 𝑆 [1, 𝑟] S [1, r] 是 𝑆 S 中前 𝑟 r 个字符组成的前缀．也就是说，这个求和记号，可以看作是对于操作序列 𝑆 S 中所有以 𝑅 R 结尾的前缀进行的求和．比如说，有

∑ 𝑆 1 = 𝑥, ∑ 𝑆 𝑥 = 1 2 𝑥 ( 𝑥 + 1). ∑ S 1 = x, ∑ S x = 1 2 x ( x + 1).

再比如说， ∑ 𝑦 ∑ y 就是操作序列中，每次右穿网格线时，之前上穿网格线的次数的累加．对于整段操作序列来说， 𝑦 y 在所有以 𝑅 R 结尾的前缀处的值，就是在 𝑖 = 1, ⋯, 𝑛 i = 1, ⋯, n 处的所有 ⌊ ( 𝑎 𝑖 + 𝑏) / 𝑐 ⌋ ⌊ ( a i + b) / c ⌋ 的值．因此，对于整段操作序列计算的 ∑ 𝑦 ∑ y ，就是本题最终要求的量．

初始时，有 𝑈 = ( 0, 1, 0) U = ( 0, 1, 0) ， 𝑅 = ( 1, 0, 0) R = ( 1, 0, 0) ．进一步，可以将两个元素 ( 𝑥 1, 𝑦 1, 𝑠 1) ( x 1, y 1, s 1) 和 ( 𝑥 2, 𝑦 2, 𝑠 2) ( x 2, y 2, s 2) 的乘积定义为

( 𝑥 1, 𝑦 1, 𝑠 1) ⋅ ( 𝑥 2, 𝑦 2, 𝑠 2) = ( 𝑥 1 + 𝑥 2, 𝑦 1 + 𝑦 2, 𝑠 1 + 𝑠 2 + 𝑥 2 𝑦 1). ( x 1, y 1, s 1) ⋅ ( x 2, y 2, s 2) = ( x 1 + x 2, y 1 + y 2, s 1 + s 2 + x 2 y 1).

其中，最后一项贡献合并的结果可以通过如下计算得到：

∑ 𝑆 1 + 𝑆 2 𝑦 = ∑ 𝑆 1 𝑦 + ∑ 𝑆 2 ( 𝑦 + 𝑦 1) = ∑ 𝑆 1 𝑦 + ∑ 𝑆 2 𝑦 + 𝑦 1 ∑ 𝑆 2 1 = 𝑠 1 + 𝑠 2 + 𝑥 2 𝑦 1. ∑ S 1 + S 2 y = ∑ S 1 y + ∑ S 2 ( y + y 1) = ∑ S 1 y + ∑ S 2 y + y 1 ∑ S 2 1 = s 1 + s 2 + x 2 y 1.

容易验证，这个乘法运算满足结合律，且幺元为 ( 0, 0, 0) ( 0, 0, 0) ，所以这些元素在该乘法运算下构成幺半群．所求的答案，就是乘积的第三个分量．

这两种方法都可以得到正确的结果．但是，因为保留了较多的冗余信息，矩阵运算的常数较大，所以第二种方法在处理实际问题时更为实用．

### 算法过程

与类欧几里得算法整体约化不同，万能欧几里得算法约化问题的手段是将这些操作分批次地合并．记字符串对应的操作的乘积为

𝐹 ( 𝑎, 𝑏, 𝑐, 𝑛, 𝑈, 𝑅). F ( a, b, c, n, U, R).

约化过程具体如下：

-

当 𝑏 ≥ 𝑐 b ≥ c 时，操作序列的开始有 ⌊ 𝑏 / 𝑐 ⌋ ⌊ b / c ⌋ 个 𝑈 U ，直接计算它们的乘积，并将这些 𝑈 U 从操作序列中移除．此时，第 𝑖 i 个 𝑅 R 前方的 𝑈 U 的数量等于

⌊ 𝑎 𝑖 + 𝑏 𝑐 ⌋ − ⌊ 𝑏 𝑐 ⌋ = ⌊ 𝑎 𝑖 + ( 𝑏 m o d 𝑐) 𝑐 ⌋. ⌊ a i + b c ⌋ − ⌊ b c ⌋ = ⌊ a i + ( b mod c) c ⌋.

因此，这相当于将线段参数由 ( 𝑎, 𝑏, 𝑐, 𝑛) ( a, b, c, n) 变为 ( 𝑎, 𝑏 m o d 𝑐, 𝑐, 𝑛) ( a, b mod c, c, n) ．所以，对于这种情形，有

𝐹 ( 𝑎, 𝑏, 𝑐, 𝑛, 𝑈, 𝑅) = 𝑈 ⌊ 𝑏 / 𝑐 ⌋ 𝐹 ( 𝑎, 𝑏 m o d 𝑐, 𝑐, 𝑛, 𝑈, 𝑅). F ( a, b, c, n, U, R) = U ⌊ b / c ⌋ F ( a, b mod c, c, n, U, R).
-

当 𝑎 ≥ 𝑐 a ≥ c 时，操作序列中每个 𝑅 R 的前方都至少有 ⌊ 𝑎 / 𝑐 ⌋ ⌊ a / c ⌋ 个 𝑈 U ，可以将它们合并到 𝑅 R 上．也就是说，可以用 𝑈 ⌊ 𝑎 / 𝑐 ⌋ 𝑅 U ⌊ a / c ⌋ R 替代 𝑅 R ．合并后的字符串中，第 𝑖 i 个 𝑅 R 前方的 𝑈 U 的数量等于

⌊ 𝑎 𝑖 + 𝑏 𝑐 ⌋ − ⌊ 𝑎 𝑐 ⌋ 𝑖 = ⌊ ( 𝑎 m o d 𝑐) 𝑖 + 𝑏 𝑐 ⌋. ⌊ a i + b c ⌋ − ⌊ a c ⌋ i = ⌊ ( a mod c) i + b c ⌋.

因此，这相当于将线段参数由 ( 𝑎, 𝑏, 𝑐, 𝑛) ( a, b, c, n) 变为 ( 𝑎 m o d 𝑐, 𝑏, 𝑐, 𝑛) ( a mod c, b, c, n) ．所以，对于这种情形，有

𝐹 ( 𝑎, 𝑏, 𝑐, 𝑛, 𝑈, 𝑅) = 𝐹 ( 𝑎 m o d 𝑐, 𝑏, 𝑐, 𝑛, 𝑈, 𝑈 ⌊ 𝑎 / 𝑐 ⌋ 𝑅). F ( a, b, c, n, U, R) = F ( a mod c, b, c, n, U, U ⌊ a / c ⌋ R).
-

对于剩下的情形，需要翻转横纵坐标，这基本是在交换 𝑈 U 和 𝑅 R ，只是翻转后线段的参数需要仔细计算．结合操作序列的定义可知，需要确定系数 ( 𝑎 ′, 𝑏 ′, 𝑐 ′, 𝑛 ′) ( a ′, b ′, c ′, n ′) 使得变换前的操作序列中，第 𝑗 j 个 𝑈 U 前方的 𝑅 R 的数量恰为 ⌊ ( 𝑎 ′ 𝑗 + 𝑏 ′) / 𝑐 ′ ⌋ ⌊ ( a ′ j + b ′) / c ′ ⌋ 且总共有 𝑛 ′ n ′ 个 𝑈 U ．根据定义可知，

𝑛 ′ = ⌊ 𝑎 𝑛 + 𝑏 𝑐 ⌋ = 𝑚, n ′ = ⌊ a n + b c ⌋ = m,

而第 𝑗 j 个 𝑈 U 前方的 𝑅 R 的数量，就等于最大的 𝑖 i 使得

⌊ 𝑎 𝑖 + 𝑏 𝑐 ⌋ < 𝑗 ⟺ 𝑎 𝑖 + 𝑏 𝑐 < 𝑗 ⟺ 𝑖 < 𝑐 𝑗 − 𝑏 𝑎 ⟺ 𝑖 < ⌈ 𝑐 𝑗 − 𝑏 𝑎 ⌉ = ⌊ 𝑐 𝑗 − 𝑏 − 1 𝑎 ⌋ + 1. ⌊ a i + b c ⌋ < j ⟺ a i + b c < j ⟺ i < c j − b a ⟺ i < ⌈ c j − b a ⌉ = ⌊ c j − b − 1 a ⌋ + 1.

因此， 𝑖 = ⌊ ( 𝑐 𝑗 − 𝑏 − 1) / 𝑎 ⌋ i = ⌊ ( c j − b − 1) / a ⌋ ．这一推导过程与前文类欧几里得算法的推导类似，同样利用了上下取整函数的性质．

有两处细节需要处理：

  - 截距项 − ( 𝑏 + 1) / 𝑎 − ( b + 1) / a 为负数．注意到，如果将线段向左平移一个单位，就可以让截距项恢复为非负数，因为总有 ( 𝑐 − 𝑏 − 1) / 𝑎 ≥ 0 ( c − b − 1) / a ≥ 0 ．因此，可以将交换前的第一段 𝑅 ⌊ ( 𝑐 − 𝑏 − 1) / 𝑎 ⌋ 𝑈 R ⌊ ( c − b − 1) / a ⌋ U 提取出来，只交换剩余操作序列中的 𝑈 U 和 𝑅 R ；
  - 交换 𝑈 U 和 𝑅 R 后，结尾存在多余的 𝑈 U ．因此，交换 𝑈 U 和 𝑅 R 之前，需要首先将最后一段 𝑅 R 提取出来，只交换剩余操作序列中的 𝑈 U 和 𝑅 R ．这一段 𝑅 R 的数量为 𝑛 − ⌊ ( 𝑐 𝑚 − 𝑏 − 1) / 𝑎 ⌋ n − ⌊ ( c m − b − 1) / a ⌋ ．

去掉头尾若干个字符后，第 𝑗 j 个 𝑈 U 前方的 𝑅 R 的数量变为：

⌊ 𝑐 ( 𝑗 + 1) − 𝑏 − 1 𝑎 ⌋ − ⌊ 𝑐 − 𝑏 − 1 𝑎 ⌋ = ⌊ 𝑐 𝑗 + ( 𝑐 − 𝑏 − 1) m o d 𝑎 𝑎 ⌋. ⌊ c ( j + 1) − b − 1 a ⌋ − ⌊ c − b − 1 a ⌋ = ⌊ c j + ( c − b − 1) mod a a ⌋.

回忆起，交换前的序列中 𝑈 U 的数量为 𝑚 = ⌊ ( 𝑎 𝑛 + 𝑏) / 𝑐 ⌋ m = ⌊ ( a n + b) / c ⌋ ．而上述左移一个单位的操作，要求保证交换前至少存在一个 𝑈 U ，也就是 0" aria-hidden=true breakable=true class=NCM-N> 𝑚 "> > 0 0" xmlns=http://www.w3.org/1998/Math/MathML> m ">> 0 0" src=data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7> ．利用这一条件，可以分为两种情形：

  -

对于 0" aria-hidden=true breakable=true class=NCM-N> 𝑚 "> > 0 0" xmlns=http://www.w3.org/1998/Math/MathML> m ">> 0 0" src=data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7> 的情形，处理了上面的两点后，交换完 𝑈 U 和 𝑅 R 的操作序列就是对应着参数为 ( 𝑐, ( 𝑐 − 𝑏 − 1) m o d 𝑎, 𝑎, 𝑚 − 1) ( c, ( c − b − 1) mod a, a, m − 1) 的线段的合法序列．所以，有

𝐹 ( 𝑎, 𝑏, 𝑐, 𝑛, 𝑈, 𝑅) = 𝑅 ⌊ ( 𝑐 − 𝑏 − 1) / 𝑎 ⌋ 𝑈 𝐹 ( 𝑐, ( 𝑐 − 𝑏 − 1) m o d 𝑎, 𝑎, 𝑚 − 1, 𝑅, 𝑈) 𝑅 𝑛 − ⌊ ( 𝑐 𝑚 − 𝑏 − 1) / 𝑎 ⌋. F ( a, b, c, n, U, R) = R ⌊ ( c − b − 1) / a ⌋ U F ( c, ( c − b − 1) mod a, a, m − 1, R, U) R n − ⌊ ( c m − b − 1) / a ⌋.
  -

特别地，对于 𝑚 = 0 m = 0 的情形，交换前的操作序列中只包含 𝑛 n 个 𝑅 R ，无需交换，可以直接返回：

𝐹 ( 𝑎, 𝑏, 𝑐, 𝑛, 𝑈, 𝑅) = 𝑅 𝑛. F ( a, b, c, n, U, R) = R n.

与类欧几里得算法不同，万能欧几里得算法的这一特殊情形需要单独处理，否则会因涉及负幂次而无法正确计算．

利用这些讨论，就可以将问题递归地解决．

假设幺半群内元素单次相乘的时间复杂度是 𝑂 ( 1) O ( 1) 的．那么，如果计算过程中这些元素的幂次计算都使用 [快速幂][47] 进行，最终的算法复杂度就是 𝑂 ( l o g ⁡ m a x { 𝑎, 𝑐 } + l o g ⁡ ( 𝑏 / 𝑐)) O ( log ⁡ max { a, c } + log ⁡ ( b / c)) 的 1 ．

对复杂度的解释

对比（类）欧几里得算法，万能欧几里得算法只是多了求快速幂的步骤．其余的计算过程的复杂度和类欧几里得算法相仿，已经说明是 𝑂 ( l o g ⁡ m i n { 𝑎, 𝑐, 𝑛 }) O ( log ⁡ min { a, c, n }) 的．现在，需要计算这些快速幂的总复杂度．

除了第一轮迭代，都有 𝑏 < 𝑐 b < c ，因此这些迭代每轮都涉及三次快速幂的计算，总的复杂度是：

𝑂 ( l o g ⁡ ⌊ 𝑎 𝑐 ⌋ + l o g ⁡ ⌊ 𝑐 − 𝑏 1 − 1 𝑎 1 ⌋ + l o g ⁡ ( 𝑛 − ⌊ 𝑐 𝑚 − 𝑏 1 − 1 𝑎 1 ⌋)), O ( log ⁡ ⌊ a c ⌋ + log ⁡ ⌊ c − b 1 − 1 a 1 ⌋ + log ⁡ ( n − ⌊ c m − b 1 − 1 a 1 ⌋)),

其中， 𝑎 1 = 𝑎 m o d 𝑐 a 1 = a mod c ， 𝑏 1 = 𝑏 m o d 𝑐 b 1 = b mod c 且 𝑚 = ⌊ ( 𝑎 1 𝑛 + 𝑏 1) / 𝑐 ⌋ m = ⌊ ( a 1 n + b 1) / c ⌋ ．后面两项，分别有估计：

𝑐 − 𝑏 1 − 1 𝑎 1 ≤ 𝑐 𝑎 1, 𝑛 − ⌊ 𝑐 𝑚 − 𝑏 1 − 1 𝑎 1 ⌋ ≤ 𝑛 − 𝑐 𝑚 − 𝑏 1 − 1 𝑎 1 + 1 ≤ 𝑛 − 𝑐 ( ( 𝑎 1 𝑛 + 𝑏 1) / 𝑐 − 1) − 𝑏 1 − 1 𝑎 1 + 1 = 𝑐 + 1 𝑎 1 + 1. c − b 1 − 1 a 1 ≤ c a 1, n − ⌊ c m − b 1 − 1 a 1 ⌋ ≤ n − c m − b 1 − 1 a 1 + 1 ≤ n − c ( ( a 1 n + b 1) / c − 1) − b 1 − 1 a 1 + 1 = c + 1 a 1 + 1.

因此，这两项的复杂度都是 𝑂 ( l o g ⁡ ( 𝑐 / 𝑎 1)) O ( log ⁡ ( c / a 1)) 的．

每一轮迭代中，线段的参数都由 ( 𝑎, ⋅, 𝑐, ⋅) ( a, ⋅, c, ⋅) 变换为 ( 𝑐, ⋅, 𝑎 m o d 𝑐, ⋅) ( c, ⋅, a mod c, ⋅) ，且该轮总的时间复杂度为

𝑂 ( l o g ⁡ 𝑎 𝑐 + l o g ⁡ 𝑐 𝑎 m o d 𝑐). O ( log ⁡ a c + log ⁡ c a mod c).

对于全部递归的轮次，这些项可以裂项相消，因此，最后总和复杂度就是 𝑂 ( l o g ⁡ 𝑎 + l o g ⁡ 𝑐) = 𝑂 ( l o g ⁡ m a x { 𝑎, 𝑐 }) O ( log ⁡ a + log ⁡ c) = O ( log ⁡ max { a, c }) 的．

最后，再加上第一轮迭代中快速幂 𝑈 ⌊ 𝑏 / 𝑐 ⌋ U ⌊ b / c ⌋ 的复杂度 𝑂 ( l o g ⁡ ( 𝑏 / 𝑐)) O ( log ⁡ ( b / c)) ，就得到总的复杂度为 𝑂 ( l o g ⁡ m a x { 𝑎, 𝑐 } + l o g ⁡ ( 𝑏 / 𝑐)) O ( log ⁡ max { a, c } + log ⁡ ( b / c)) ．

万能欧几里得算法的流程可以写成统一的模板，处理具体问题时只需要更改模板类型 `T`的实现即可．

参考实现

```
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
```

 |

```
// Class T implements the monoid.
// Assume that it provides a multiplication operator
//     and a default constructor returning the unity in the monoid.

// Binary exponentiation.
template <typename T>
T pow(T a, int b) {
  T res;
  for (; b; b >>= 1) {
    if (b & 1) res = res * a;
    a = a * a;
  }
  return res;
}

// Universal Euclidean algorithm.
template <typename T>
T euclid(int a, int b, int c, int n, T U, T R) {
  if (b >= c) return pow(U, b / c) * euclid(a, b % c, c, n, U, R);
  if (a >= c) return euclid(a % c, b, c, n, U, pow(U, a / c) * R);
  auto m = ((long long)a * n + b) / c;
  if (!m) return pow(R, n);
  return pow(R, (c - b - 1) / a) * U *
         euclid(c, (c - b - 1) % a, a, m - 1, R, U) *
         pow(R, n - (c * m - b - 1) / a);
}
```

 |

利用万能欧几里得算法可以得到模板题的实现如下：

模板题实现（ [Library Checker - Sum of Floor of Linear][108] ）

```
  1
  2
  3
  4
  5
  6
  7
  8
  9
 10
 11
 12
 13
 14
 15
 16
 17
 18
 19
 20
 21
 22
 23
 24
 25
 26
 27
 28
 29
 30
 31
 32
 33
 34
 35
 36
 37
 38
 39
 40
 41
 42
 43
 44
 45
 46
 47
 48
 49
 50
 51
 52
 53
 54
 55
 56
 57
 58
 59
 60
 61
 62
 63
 64
 65
 66
 67
 68
 69
 70
 71
 72
 73
 74
 75
 76
 77
 78
 79
 80
 81
 82
 83
 84
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
```

 |

```
#include <array>
#include <iostream>

// Switch between matrix and info merging approaches.
#define MATRIX 1

// Class T implements the monoid.
// Assume that it provides a multiplication operator
//     and a default constructor returning the unity in the monoid.

// Binary exponentiation.
template <typename T>
T pow(T a, int b) {
  T res;
  for (; b; b >>= 1) {
    if (b & 1) res = res * a;
    a = a * a;
  }
  return res;
}

// Universal Euclidean algorithm.
template <typename T>
T euclid(int a, int b, int c, int n, T U, T R) {
  if (b >= c) return pow(U, b / c) * euclid(a, b % c, c, n, U, R);
  if (a >= c) return euclid(a % c, b, c, n, U, pow(U, a / c) * R);
  auto m = ((long long)a * n + b) / c;
  if (!m) return pow(R, n);
  return pow(R, (c - b - 1) / a) * U *
         euclid(c, (c - b - 1) % a, a, m - 1, R, U) *
         pow(R, n - (c * m - b - 1) / a);
}

#if MATRIX

template <size_t N>
struct Matrix {
  std::array<long long, N * N> mat;

  auto loc(size_t i, size_t j) const { return mat[i * N + j]; }

  auto& loc(size_t i, size_t j) { return mat[i * N + j]; }

  Matrix() : mat{} {
    for (size_t i = 0; i != N; ++i) {
      loc(i, i) = 1;
    }
  }

  Matrix operator*(const Matrix& rhs) const {
    Matrix res;
    res.mat.fill(0);
    for (size_t i = 0; i != N; ++i) {
      for (size_t k = 0; k != N; ++k) {
        for (size_t j = 0; j != N; ++j) {
          res.loc(i, j) += loc(i, k) * rhs.loc(k, j);
        }
      }
    }
    return res;
  }
};

long long solve(int a, int b, int c, int n) {
  if (!n) return 0;
  Matrix<3> U, R;
  U.loc(0, 1) = R.loc(1, 2) = 1;
  auto res = euclid(a, b, c, n, U, R);
  return res.loc(0, 2);
}

#else

struct Info {
  long long x, y, s;

  Info() : x(0), y(0), s(0) {}

  Info operator*(const Info& rhs) const {
    Info res;
    res.x = x + rhs.x;
    res.y = y + rhs.y;
    res.s = s + rhs.s + rhs.x * y;
    return res;
  }
};

long long solve(int a, int b, int c, int n) {
  if (!n) return 0;
  Info U, R;
  U.y = 1;
  R.x = 1;
  auto res = euclid(a, b, c, n, U, R);
  return res.s;
}

#endif

int main() {
  int t;
  std::cin >> t;
  for (; t; --t) {
    int a, b, c, n;
    std::cin >> n >> c >> a >> b;
    std::cout << solve(a, b, c, n - 1) << '\n';
  }
  return 0;
}
```

 |

### 例题

[【模板】类欧几里得算法][109]

多组询问．给定正整数 𝑎, 𝑏, 𝑐, 𝑛 a, b, c, n ，求

𝑓 ( 𝑎, 𝑏, 𝑐, 𝑛) = 𝑛 ∑ 𝑖 = 0 ⌊ 𝑎 𝑖 + 𝑏 𝑐 ⌋, 𝑔 ( 𝑎, 𝑏, 𝑐, 𝑛) = 𝑛 ∑ 𝑖 = 0 𝑖 ⌊ 𝑎 𝑖 + 𝑏 𝑐 ⌋, ℎ ( 𝑎, 𝑏, 𝑐, 𝑛) = 𝑛 ∑ 𝑖 = 0 ⌊ 𝑎 𝑖 + 𝑏 𝑐 ⌋ 2. f ( a, b, c, n) = ∑ i = 0 n ⌊ a i + b c ⌋, g ( a, b, c, n) = ∑ i = 0 n i ⌊ a i + b c ⌋, h ( a, b, c, n) = ∑ i = 0 n ⌊ a i + b c ⌋ 2. 解答二

为了应用万能欧几里得算法的模板，首先将 𝑖 = 0 i = 0 的项提出来，单独考虑．对于剩下的部分，可以看作是对参数为 ( 𝑎, 𝑏, 𝑐, 𝑛) ( a, b, c, n) 的线段分别计算 ∑ 𝑦, ∑ 𝑥 𝑦, ∑ 𝑦 2 ∑ y, ∑ x y, ∑ y 2 ．如正文所言，有两种将操作序列转换为幺半群元素的方式．

**矩阵运算**：状态向量定义为 ( 1, 𝑥, 𝑦, 𝑥 𝑦, 𝑦 2, ∑ 𝑦, ∑ 𝑥 𝑦, ∑ 𝑦 2) ( 1, x, y, x y, y 2, ∑ y, ∑ x y, ∑ y 2) ．初始状态为 ( 1, 0, 0, 0, 0, 0, 0, 0) ( 1, 0, 0, 0, 0, 0, 0, 0) ，两个操作分别为

𝑈 = ⎛ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎝ 1 0 1 0 1 0 0 0 0 1 0 1 0 0 0 0 0 0 1 0 2 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 ⎞ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎠, 𝑅 = ⎛ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎜ ⎝ 1 1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 1 0 0 1 0 0 0 0 0 1 0 0 1 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 ⎞ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎟ ⎠. U = ( 1 0 1 0 1 0 0 0 0 1 0 1 0 0 0 0 0 0 1 0 2 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1), R = ( 1 1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 1 0 1 1 0 0 0 0 1 0 0 1 0 0 0 0 0 1 0 0 1 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 1).

最终答案为初始状态右乘这些操作矩阵的乘积得到的向量末尾三个分量．

这个做法的常数巨大，并不能通过本题，这里给出细节仅仅是为了辅助理解．

**贡献合并**：一段操作序列的贡献定义为 ( 𝑥, 𝑦, ∑ 𝑦, ∑ 𝑥 𝑦, ∑ 𝑦 2) ( x, y, ∑ y, ∑ x y, ∑ y 2) ．两个操作分别为

𝑈 = ( 0, 1, 0, 0, 0), 𝑅 = ( 1, 0, 0, 0, 0). U = ( 0, 1, 0, 0, 0), R = ( 1, 0, 0, 0, 0).

贡献合并时，有

∑ 𝑆 1 + 𝑆 2 𝑦 = ∑ 𝑆 1 𝑦 + ∑ 𝑆 2 ( 𝑦 + 𝑦 1) = ∑ 𝑆 1 𝑦 + ∑ 𝑆 2 𝑦 + 𝑥 2 𝑦 1, ∑ 𝑆 1 + 𝑆 2 𝑥 𝑦 = ∑ 𝑆 1 𝑥 𝑦 + ∑ 𝑆 2 ( 𝑥 + 𝑥 1) ( 𝑦 + 𝑦 1) = ∑ 𝑆 1 𝑥 𝑦 + ∑ 𝑆 2 𝑥 𝑦 + 𝑥 1 ∑ 𝑆 2 𝑦 + 𝑦 1 ∑ 𝑆 2 𝑥 + 𝑥 1 𝑦 1 ∑ 𝑆 2 1 = ∑ 𝑆 1 𝑥 𝑦 + ∑ 𝑆 2 𝑥 𝑦 + 𝑥 1 ∑ 𝑆 2 𝑦 + 1 2 𝑥 2 ( 𝑥 2 + 1) 𝑦 1 + 𝑥 1 𝑥 2 𝑦 1, ∑ 𝑆 1 + 𝑆 2 𝑦 2 = ∑ 𝑆 1 𝑦 2 + ∑ 𝑆 2 ( 𝑦 + 𝑦 1) 2 = ∑ 𝑆 1 𝑦 2 + ∑ 𝑆 2 𝑦 2 + 2 𝑦 1 ∑ 𝑆 2 𝑦 + 𝑦 2 1 ∑ 𝑆 2 1 = ∑ 𝑆 1 𝑦 2 + ∑ 𝑆 2 𝑦 2 + 2 𝑦 1 ∑ 𝑆 2 𝑦 + 𝑥 2 𝑦 2 1. ∑ S 1 + S 2 y = ∑ S 1 y + ∑ S 2 ( y + y 1) = ∑ S 1 y + ∑ S 2 y + x 2 y 1, ∑ S 1 + S 2 x y = ∑ S 1 x y + ∑ S 2 ( x + x 1) ( y + y 1) = ∑ S 1 x y + ∑ S 2 x y + x 1 ∑ S 2 y + y 1 ∑ S 2 x + x 1 y 1 ∑ S 2 1 = ∑ S 1 x y + ∑ S 2 x y + x 1 ∑ S 2 y + 1 2 x 2 ( x 2 + 1) y 1 + x 1 x 2 y 1, ∑ S 1 + S 2 y 2 = ∑ S 1 y 2 + ∑ S 2 ( y + y 1) 2 = ∑ S 1 y 2 + ∑ S 2 y 2 + 2 y 1 ∑ S 2 y + y 1 2 ∑ S 2 1 = ∑ S 1 y 2 + ∑ S 2 y 2 + 2 y 1 ∑ S 2 y + x 2 y 1 2.

这说明，应该将操作的乘法定义为

( 𝑥 1, 𝑦 1, 𝑠 1, 𝑡 1, 𝑢 1) ⋅ ( 𝑥 2, 𝑦 2, 𝑠 2, 𝑡 2, 𝑢 2) = ( 𝑥 1 + 𝑥 2, 𝑦 1 + 𝑦 2, 𝑠 1 + 𝑠 2 + 𝑥 2 𝑦 1, 𝑡 1 + 𝑡 2 + 𝑥 1 𝑠 2 + ( 1 / 2) 𝑥 2 ( 𝑥 2 + 1) 𝑦 1 + 𝑥 1 𝑥 2 𝑦 1, 𝑢 1 + 𝑢 2 + 2 𝑦 1 𝑠 2 + 𝑥 2 𝑦 2 1). ( x 1, y 1, s 1, t 1, u 1) ⋅ ( x 2, y 2, s 2, t 2, u 2) = ( x 1 + x 2, y 1 + y 2, s 1 + s 2 + x 2 y 1, t 1 + t 2 + x 1 s 2 + ( 1 / 2) x 2 ( x 2 + 1) y 1 + x 1 x 2 y 1, u 1 + u 2 + 2 y 1 s 2 + x 2 y 1 2).

虽然直接验证较为繁琐，但是上述定义的贡献向量在该乘法下的确构成幺半群，单位元为 ( 0, 0, 0, 0, 0) ( 0, 0, 0, 0, 0) ．

对于一般的情形，有

∑ 𝑆 1 + 𝑆 2 𝑥 𝑟 𝑦 𝑠 = ∑ 𝑆 1 𝑥 𝑟 𝑦 𝑠 + ∑ 𝑆 2 ( 𝑥 + 𝑥 1) 𝑟 ( 𝑦 + 𝑦 1) 𝑠 = ∑ 𝑆 1 𝑥 𝑟 𝑦 𝑠 + 𝑟 ∑ 𝑖 = 0 𝑠 ∑ 𝑗 = 0 ( 𝑟 𝑖) ( 𝑠 𝑗) 𝑥 𝑟 − 𝑖 1 𝑦 𝑠 − 𝑗 1 ∑ 𝑆 2 𝑥 𝑖 𝑦 𝑗. ∑ S 1 + S 2 x r y s = ∑ S 1 x r y s + ∑ S 2 ( x + x 1) r ( y + y 1) s = ∑ S 1 x r y s + ∑ i = 0 r ∑ j = 0 s ( r i) ( s j) x 1 r − i y 1 s − j ∑ S 2 x i y j.

只要维护好所有更低幂次的贡献，就可以计算一般情形的和式．

```
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
```

 |

```
#include <iostream>

template <typename T>
T pow(T a, int b) {
  T res;
  for (; b; b >>= 1) {
    if (b & 1) res = res * a;
    a = a * a;
  }
  return res;
}

template <typename T>
T euclid(int a, int b, int c, int n, T U, T R) {
  if (b >= c) return pow(U, b / c) * euclid(a, b % c, c, n, U, R);
  if (a >= c) return euclid(a % c, b, c, n, U, pow(U, a / c) * R);
  auto m = ((long long)a * n + b) / c;
  if (!m) return pow(R, n);
  return pow(R, (c - b - 1) / a) * U *
         euclid(c, (c - b - 1) % a, a, m - 1, R, U) *
         pow(R, n - (c * m - b - 1) / a);
}

constexpr int M = 998244353;

struct Info {
  long long x, y, s, t, u;

  Info() : x(0), y(0), s(0), t(0), u(0) {}

  Info operator*(const Info& rhs) const {
    Info res;
    res.x = (x + rhs.x) % M;
    res.y = (y + rhs.y) % M;
    res.s = (s + rhs.s + rhs.x * y) % M;
    auto tmp = (rhs.x * (rhs.x + 1) / 2 + x * rhs.x) % M;
    res.t = (t + rhs.t + x * rhs.s + tmp * y) % M;
    res.u = (u + rhs.u + 2 * y * rhs.s + rhs.x * y % M * y) % M;
    return res;
  }
};

void solve(int a, int b, int c, int n) {
  Info U, R;
  U.y = 1;
  R.x = 1;
  auto res = euclid(a, b, c, n, U, R);
  auto f = (res.s + b / c) % M;
  auto g = res.t;
  auto h = (res.u + (long long)(b / c) * (b / c)) % M;
  std::cout << f << ' ' << h << ' ' << g << '\n';
}

int main() {
  int t;
  std::cin >> t;
  for (; t; --t) {
    int a, b, c, n;
    std::cin >> n >> a >> b >> c;
    solve(a, b, c, n);
  }
  return 0;
}
```

 |

[[清华集训 2014] Sum][110]

多组询问．给定正整数 𝑛 n 和 𝑟 r ，求

𝑛 ∑ 𝑑 = 1 ( − 1) ⌊ 𝑑 √ 𝑟 ⌋. ∑ d = 1 n ( − 1) ⌊ d r ⌋. 解答二

首先，单独处理 𝑟 r 为完全平方数的情形，与前文完全一致，从略．此处，仅考虑 𝑟 r 不是完全平方数的情形．

本题应用万能欧几里得算法的方式有很多．比如说，可以为每个操作定义一个线性变换：

𝑈 ( 𝑥) = − 𝑥, 𝑅 ( 𝑥) = 𝑥 + 1. U ( x) = − x, R ( x) = x + 1.

操作的乘法定义为线性变换的复合．那么，最终的答案就是操作序列对应的变换的复合得到的函数在 𝑥 = 0 x = 0 处的值．

还可以为每段操作序列定义它的贡献．贡献可以定义为 ( ( − 1) 𝑦, ∑ ( − 1) 𝑦) ( ( − 1) y, ∑ ( − 1) y) ．那么，两个操作分别取

𝑈 = ( 0, − 1), 𝑅 = ( 1, 1). U = ( 0, − 1), R = ( 1, 1).

贡献的合并定义为

( 𝑢 1, 𝑣 1) ⋅ ( 𝑢 2, 𝑣 2) = ( 𝑢 1 𝑢 2, 𝑣 1 + 𝑢 1 𝑣 2). ( u 1, v 1) ⋅ ( u 2, v 2) = ( u 1 u 2, v 1 + u 1 v 2).

容易验证，在该乘法下，所有操作构成了幺半群，且单位元为 ( 0, 1) ( 0, 1) ．最终的答案就是所有元素乘积的第二个分量．

这两种方法是一致的，因为如果将线性变换写作 𝑓 ( 𝑥) = 𝑢 + 𝑣 𝑥 f ( x) = u + v x ，那么线性变换的复合对应的系数的变化，恰恰就是上述操作的乘法．也就是说，这两个幺半群是同构的．

本题中，线段的参数为 ( 𝑘, 𝑛) ( k, n) ，其中， 𝑘 ∈ 𝐑 k ∈ R 为直线的斜率．设操作序列对应的乘积为 𝐹 ( 𝑘, 𝑛, 𝑈, 𝑅) F ( k, n, U, R) ．那么，有如下递归算法：

-

如果 𝑘 ≥ 1 k ≥ 1 ，那么操作序列中每个 𝑅 R 前方都有至少 ⌊ 𝑘 ⌋ ⌊ k ⌋ 个 𝑈 U ，所以，有

𝐹 ( 𝑘, 𝑛, 𝑈, 𝑅) = 𝐹 ( 𝑘 − ⌊ 𝑘 ⌋, 𝑛, 𝑈, 𝑈 ⌊ 𝑘 ⌋ 𝑅). F ( k, n, U, R) = F ( k − ⌊ k ⌋, n, U, U ⌊ k ⌋ R).
-

如果 𝑘 < 1 k < 1 ，那么交换操作序列中的 𝑈 U 和 𝑅 R ，并舍去末尾的 𝑈 U （即交换前的 𝑅 R ），所以，有

𝐹 ( 𝑘, 𝑛, 𝑈, 𝑅) = 𝐹 ( 𝑘 − 1, 𝑚, 𝑅, 𝑈) 𝑅 𝑛 − ⌊ 𝑘 − 1 𝑚 ⌋. F ( k, n, U, R) = F ( k − 1, m, R, U) R n − ⌊ k − 1 m ⌋.

算法中， 𝑘 k 的迭代过程其实就是在求 √ 𝑟 r 的连分数展开．为此，可以应用 [PQa 算法][115] ．求连分数的过程和万能欧几里得算法迭代的过程可以同时进行．

和类欧几里得算法的情形一致，算法的复杂度仍然是 𝑂 ( l o g ⁡ 𝑛) O ( log ⁡ n) 的．

```
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
```

 |

```
#include <algorithm>
#include <cmath>
#include <iostream>

template <typename T>
T pow(T a, int b) {
  T res;
  for (; b; b >>= 1) {
    if (b & 1) res = res * a;
    a = a * a;
  }
  return res;
}

struct LinearTransform {
  int u, v;

  LinearTransform() : u(0), v(1) {}

  LinearTransform operator*(const LinearTransform& rhs) const {
    LinearTransform res;
    res.u = u + v * rhs.u;
    res.v = v * rhs.v;
    return res;
  }

  int eval(int x) const { return u + v * x; }
};

int solve(int n, int r) {
  long double sqrt_r = sqrtl(r);
  int sqr = sqrt_r;
  if (r == sqr * sqr) return sqr % 2 ? (n % 2 ? -1 : 0) : n;
  int P = 0, Q = 1, D = r, val = 0;
  LinearTransform U, R;
  U.v = -1;
  R.u = 1;
  while (n) {
    int a = (P + sqr) / Q;
    R = pow(U, a) * R;
    int m = ((P + sqrt_r) / Q - a) * n;
    P = a * Q - P;
    Q = (D - P * P) / Q;
    int rem = n - (int)(m * (P + sqrt_r) / Q);
    val = pow(R, rem).eval(val);
    std::swap(U, R);
    n = m;
  }
  return val;
}

int main() {
  int t;
  std::cin >> t;
  for (; t; --t) {
    int n, r;
    std::cin >> n >> r;
    std::cout << solve(n, r) << '\n';
  }
  return 0;
}
```

 |

## 习题

模板题：

- [Library Checker - Sum of Floor of Linear][108]
- [Luogu P5170【模板】类欧几里得算法][109]
- [Luogu P5171 Earthquake][116]
- [Luogu P5172 [清华集训 2014] Sum][110]
- [Luogu P4132 [BJOI2012] 算不出的等式][117]
- [LOJ 138. 类欧几里得算法][118]
- [LOJ 6440. 万能欧几里得][119]
- [Luogu P5179 Fraction][112]
- [Codeforces 1182 F. Maximum Sine][120]

应用题：

- [Luogu P4433 [COCI 2009/2010 #1] ALADIN][121]
- [AtCoder Beginner Contest 372 G - Ax + By < C][122]
- [AtCoder Beginner Contest 313 G - Redistribution of Piles][123]
- [AtCoder Beginner Contest 283 Ex - Popcount Sum][124]
- [Codeforces 1098 E. Fedya the Potter][125]
- [Codeforces 868 G. El Toll Caves][126]

## 参考资料与注释

---

1.

通常考虑的问题中， 𝑏 b 都与 𝑎 a 同阶， 𝑂 ( l o g ⁡ ( 𝑏 / 𝑐)) O ( log ⁡ ( b / c)) 这一项可以忽略．而且，如果在调用万能欧几里得算法前，首先进行了一轮类欧几里得算法的取模，消除 𝑏 b 的影响，这一项的快速幂的复杂度是可以规避的．这其实是因为通常的问题中， 𝑈 U 的初始形式较为特殊，它的幂次有着更简单的形式，不需要通过快速幂计算．比如正文的例子中， 𝑈 ⌊ 𝑏 / 𝑎 ⌋ U ⌊ b / a ⌋ 的结果，就是将 𝑈 U 中不在对角线上的那个 1 1 替换成 ⌊ 𝑏 / 𝑎 ⌋ ⌊ b / a ⌋ ，而无需用快速幂计算． ↩

---

**本页面最近更新： 2026/1/7 08:56:54 ， [更新历史][127]
**发现错误？想一起完善？ [在 GitHub 上编辑此页！][104]
**本页面贡献者： [sshwy][128], [StudyingFather][129], [Enter-tainer][130], [Tiphereth-A][131], [H-J-Granger][132], [countercurrent-time][133], [NachtgeistW][134], [c-forrest][135], [Early0v0][136], [Ir1d][137], [MegaOwIer][138], [Xeonacid][139], [AngelKitty][140], [CCXXXI][141], [cjsoft][142], [diauweb][143], [ezoixx130][144], [FFjet][145], [GekkaSaori][146], [Henry-ZHR][147], [Konano][148], [LovelyBuggies][149], [Makkiy][150], [mgt][151], [minghu6][152], [P-Y-Y][153], [PotassiumWings][154], [qz-cqy][155], [SamZhangQingChuan][156], [Suyun514][157], [weiyong1024][158], [alphagocc][159], [cxm1024][160], [GavinZhengOI][161], [Gesrua][162], [Great-designer][163], [iamtwz][164], [ksyx][165], [kxccc][166], [lychees][167], [megakite][168], [Peanut-Tang][169], [r-value][170], [SukkaW][171], [TonyYin0418][172]
**本页面的全部内容在 **[CC BY-SA 4.0][173] 和 [SATA][174]**协议之条款下提供，附加条款亦可能应用


## Links

[1]: ../../../contest/roadmap/
[2]: ../../../contest/resources/
[3]: ../../../contest/problemsetting/
[4]: ../../../tools/cmd/
[5]: ../../../tools/compile-debug/
[6]: ../../../tools/compiler/
[7]: ../../../tools/wsl/
[8]: ../../../tools/special-judge/
[9]: ../../../tools/polygon/
[10]: ../../../tools/oj-tool/
[11]: ../../../tools/latex/
[12]: ../../../tools/git/
[13]: ../../../lang/func/
[14]: ../../../lang/file-op/
[15]: ../../../lang/csl/algorithm/
[16]: ../../../lang/csl/bitset/
[17]: ../../../lang/csl/string/
[18]: ../../../lang/csl/pair/
[19]: ../../../lang/optimizations/
[20]: ../../../lang/cpp-other-langs/
[21]: ../../../lang/pas-cpp/
[22]: ../../../lang/python/
[23]: ../../../lang/java/
[24]: ../../../lang/java-pro/
[25]: ../../../basic/enumerate/
[26]: ../../../basic/simulate/
[27]: ../../../basic/divide-and-conquer/
[28]: ../../../basic/greedy/
[29]: ../../../basic/prefix-sum/
[30]: ../../../basic/binary/
[31]: ../../../basic/binary-lifting/
[32]: ../../../basic/construction/
[33]: ../../../dp/misc/
[34]: ../../../string/sam/
[35]: ../../../string/suffix-bst/
[36]: ../../../string/general-sam/
[37]: ../../../string/suffix-tree/
[38]: ../../../string/manacher/
[39]: ../../../string/pam/
[40]: ../../../string/seq-automaton/
[41]: ../../../string/minimal-string/
[42]: ../../../string/lyndon/
[43]: ../../../string/main-lorentz/
[44]: ../../bit/
[45]: ../../binary-set/
[46]: ../../bignum/
[47]: ../../binary-exponentiation/
[48]: ../../permutation/
[49]: ../../coordinate/
[50]: ../../complex/
[51]: ../meissel-lehmer/
[52]: ../continued-fraction/
[53]: ../stern-brocot/
[54]: ../quadratic/
[55]: ../pell-equation/
[56]: ../../order-theory/
[57]: ../../young-tableau/
[58]: ../../matroid/
[59]: ../../berlekamp-massey/
[60]: ../../../ds/monotonic-stack/
[61]: ../../../ds/monotonic-queue/
[62]: ../../../ds/sparse-table/
[63]: ../../../ds/fenwick/
[64]: ../../../ds/dividing/
[65]: ../../../ds/skiplist/
[66]: ../../../ds/kdt/
[67]: ../../../ds/divide-combine/
[68]: ../../../ds/pq-tree/
[69]: ../../../ds/finger-tree/
[70]: ../../../ds/huffman-tree/
[71]: ../../../graph/dag/
[72]: ../../../graph/topo/
[73]: ../../../graph/steiner-tree/
[74]: ../../../graph/node/
[75]: ../../../graph/rings-count/
[76]: ../../../graph/min-cycle/
[77]: ../../../graph/2-sat/
[78]: ../../../graph/euler/
[79]: ../../../graph/hamilton/
[80]: ../../../graph/bi-graph/
[81]: ../../../graph/planar/
[82]: ../../../graph/chord/
[83]: ../../../graph/color/
[84]: ../../../graph/prufer/
[85]: ../../../graph/matrix-tree/
[86]: ../../../graph/lgv/
[87]: ../../../graph/max-clique/
[88]: ../../../graph/dominator-tree/
[89]: ../../../graph/graph-random-walk/
[90]: ../../../misc/frac-programming/
[91]: ../../../misc/hoverline/
[92]: ../../../misc/fsm/
[93]: ../../../misc/cc-basic/
[94]: ../../../misc/endianness/
[95]: ../../../misc/josephus/
[96]: ../../../misc/expression/
[97]: ../../../misc/job-order/
[98]: ../../../misc/main-element/
[99]: ../../../misc/garsia-wachs/
[100]: ../../../misc/15-puzzle/
[101]: ../../../misc/kahan-summation/
[102]: ../../../misc/odt/
[103]: ../../../misc/space-optimization/
[104]: https://oi-wiki.org/edit-landing/?ref=/math/number-theory/euclidean.md
[105]: ../gcd/#欧几里得算法
[106]: ../continued-fraction/#连分数表示的求法
[107]: ../basic/#取整函数
[108]: https://judge.yosupo.jp/problem/sum_of_floor_of_linear
[109]: https://www.luogu.com.cn/problem/P5170
[110]: https://www.luogu.com.cn/problem/P5172
[111]: ../continued-fraction/#二次无理数
[112]: https://www.luogu.com.cn/problem/P5179
[113]: ../continued-fraction/#连分数的树
[114]: ../../algebra/basic/#群
[115]: ../pell-equation/#pqa-算法
[116]: https://www.luogu.com.cn/problem/P5171
[117]: https://www.luogu.com.cn/problem/P4132
[118]: https://loj.ac/p/138
[119]: https://loj.ac/p/6440
[120]: https://codeforces.com/problemset/problem/1182/F
[121]: https://www.luogu.com.cn/problem/P4433
[122]: https://atcoder.jp/contests/abc372/tasks/abc372_g
[123]: https://atcoder.jp/contests/abc313/tasks/abc313_g
[124]: https://atcoder.jp/contests/abc283/tasks/abc283_h
[125]: https://codeforces.com/problemset/problem/1098/E
[126]: https://codeforces.com/problemset/problem/868/G
[127]: https://github.com/OI-wiki/OI-wiki/commits/master/docs/math/number-theory/euclidean.md
[128]: https://github.com/sshwy
[129]: https://github.com/StudyingFather
[130]: https://github.com/Enter-tainer
[131]: https://github.com/Tiphereth-A
[132]: https://github.com/H-J-Granger
[133]: https://github.com/countercurrent-time
[134]: https://github.com/NachtgeistW
[135]: https://github.com/c-forrest
[136]: https://github.com/Early0v0
[137]: https://github.com/Ir1d
[138]: https://github.com/MegaOwIer
[139]: https://github.com/Xeonacid
[140]: https://github.com/AngelKitty
[141]: https://github.com/CCXXXI
[142]: https://github.com/cjsoft
[143]: https://github.com/diauweb
[144]: https://github.com/ezoixx130
[145]: https://github.com/FFjet
[146]: https://github.com/GekkaSaori
[147]: https://github.com/Henry-ZHR
[148]: https://github.com/Konano
[149]: https://github.com/LovelyBuggies
[150]: https://github.com/Makkiy
[151]: mailto:i@margatroid.xyz
[152]: https://github.com/minghu6
[153]: https://github.com/P-Y-Y
[154]: https://github.com/PotassiumWings
[155]: https://github.com/qz-cqy
[156]: https://github.com/SamZhangQingChuan
[157]: mailto:suyun514@qq.com
[158]: https://github.com/weiyong1024
[159]: https://github.com/alphagocc
[160]: https://github.com/cxm1024
[161]: https://github.com/GavinZhengOI
[162]: https://github.com/Gesrua
[163]: https://github.com/Great-designer
[164]: https://github.com/iamtwz
[165]: https://github.com/ksyx
[166]: https://github.com/kxccc
[167]: https://github.com/lychees
[168]: https://github.com/megakite
[169]: https://github.com/Peanut-Tang
[170]: https://github.com/r-value
[171]: https://github.com/SukkaW
[172]: https://github.com/TonyYin0418
[173]: https://creativecommons.org/licenses/by-sa/4.0/deed.zh
[174]: https://github.com/zTrix/sata-license
