<!-- source: https://github.com/atcoder/ac-library/blob/master/atcoder/internal_math.hpp | converted from HTML -->

ac-library/atcoder/internal_math.hpp at master · atcoder/ac-library · GitHub

Skip to content

You signed in with another tab or window. [Reload][1] to refresh your session. You signed out in another tab or window. [Reload][1] to refresh your session. You switched accounts on another tab or window. [Reload][1] to refresh your session. Dismiss alert

{{ message }}

### Uh oh!

There was an error while loading. [Please reload this page][1].

[atcoder][2] /**[ac-library][3]**Public

- [Notifications][4] You must be signed in to change notification settings
- [Fork 267][4]
-

[Star 2.3k][4]

[3]

## Files Expand file tree

master

/

# internal_math.hpp

Copy path

Blame

More file actions

Blame

More file actions

## Latest commit

## History

[History][5]

[5] History

212 lines (189 loc) · 5.55 KB

master

/

# internal_math.hpp

Copy path

Top

## File metadata and controls

-

Code

-

Blame

212 lines (189 loc) · 5.55 KB

[Raw][6]

Copy raw file

Download raw file

Open symbols panel

Edit and raw actions

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

109

110

111

112

113

114

115

116

117

118

119

120

121

122

123

124

125

126

127

128

129

130

131

132

133

134

135

136

137

138

139

140

141

142

143

144

145

146

147

148

149

150

151

152

153

154

155

156

157

158

159

160

161

162

163

164

165

166

167

168

169

170

171

172

173

174

175

176

177

178

179

180

181

182

183

184

185

186

187

188

189

190

191

192

193

194

195

196

197

198

199

200

201

202

203

204

205

206

207

208

209

210

211

212

#ifndef ATCODER_INTERNAL_MATH_HPP

#define ATCODER_INTERNAL_MATH_HPP 1

#include <utility>

#ifdef _MSC_VER

#include <intrin.h>

#endif

namespace atcoder {

namespace internal {

// @param m `1 <= m`

// @return x mod m

constexpr long long safe_mod(long long x, long long m) {

x %= m;

if (x < 0) x += m;

return x;

}

// Fast modular multiplication by barrett reduction

// Reference: https://en.wikipedia.org/wiki/Barrett_reduction

// NOTE: reconsider after Ice Lake

struct barrett {

unsigned int _m;

unsigned long long im;

// @param m `1 <= m`

explicit barrett(unsigned int m) : _m(m), im((unsigned long long)(-1) / m + 1) {}

// @return m

unsigned int umod() const { return _m; }

// @param a `0 <= a < m`

// @param b `0 <= b < m`

// @return `a * b % m`

unsigned int mul(unsigned int a, unsigned int b) const {

// [1] m = 1

// a = b = im = 0, so okay

// [2] m >= 2

// im = ceil(2^64 / m)

// -> im * m = 2^64 + r (0 <= r < m)

// let z = a*b = c*m + d (0 <= c, d < m)

// a*b * im = (c*m + d) * im = c*(im*m) + d*im = c*2^64 + c*r + d*im

// c*r + d*im < m * m + m * im < m * m + 2^64 + m <= 2^64 + m * (m + 1) < 2^64 * 2

// ((ab * im) >> 64) == c or c + 1

unsigned long long z = a;

z *= b;

#ifdef _MSC_VER

unsigned long long x;

_umul128(z, im, &x);

#else

unsigned long long x =

(unsigned long long)(((unsigned __int128)(z)*im) >> 64);

#endif

unsigned long long y = x * _m;

return (unsigned int)(z - y + (z < y ? _m : 0));

}

};

// @param n `0 <= n`

// @param m `1 <= m`

// @return `(x ** n) % m`

constexpr long long pow_mod_constexpr(long long x, long long n, int m) {

if (m == 1) return 0;

unsigned int _m = (unsigned int)(m);

unsigned long long r = 1;

unsigned long long y = safe_mod(x, m);

while (n) {

if (n & 1) r = (r * y) % _m;

y = (y * y) % _m;

n >>= 1;

}

return r;

}

// Reference:

// M. Forisek and J. Jancina,

// Fast Primality Testing for Integers That Fit into a Machine Word

// @param n `0 <= n`

constexpr bool is_prime_constexpr(int n) {

if (n <= 1) return false;

if (n == 2 || n == 7 || n == 61) return true;

if (n % 2 == 0) return false;

long long d = n - 1;

while (d % 2 == 0) d /= 2;

constexpr long long bases[3] = {2, 7, 61};

for (long long a : bases) {

long long t = d;

long long y = pow_mod_constexpr(a, t, n);

while (t != n - 1 && y != 1 && y != n - 1) {

y = y * y % n;

t <<= 1;

}

if (y != n - 1 && t % 2 == 0) {

return false;

}

}

return true;

}

template <int n> constexpr bool is_prime = is_prime_constexpr(n);

// @param b `1 <= b`

// @return pair(g, x) s.t. g = gcd(a, b), xa = g (mod b), 0 <= x < b/g

constexpr std::pair<long long, long long> inv_gcd(long long a, long long b) {

a = safe_mod(a, b);

if (a == 0) return {b, 0};

// Contracts:

// [1] s - m0 * a = 0 (mod b)

// [2] t - m1 * a = 0 (mod b)

// [3] s * |m1| + t * |m0| <= b

long long s = b, t = a;

long long m0 = 0, m1 = 1;

while (t) {

long long u = s / t;

s -= t * u;

m0 -= m1 * u; // |m1 * u| <= |m1| * s <= b

// [3]:

// (s - t * u) * |m1| + t * |m0 - m1 * u|

// <= s * |m1| - t * u * |m1| + t * (|m0| + |m1| * u)

// = s * |m1| + t * |m0| <= b

auto tmp = s;

s = t;

t = tmp;

tmp = m0;

m0 = m1;

m1 = tmp;

}

// by [3]: |m0| <= b/g

// by g != b: |m0| < b/g

if (m0 < 0) m0 += b / s;

return {s, m0};

}

// Compile time primitive root

// @param m must be prime

// @return primitive root (and minimum in now)

constexpr int primitive_root_constexpr(int m) {

if (m == 2) return 1;

if (m == 167772161) return 3;

if (m == 469762049) return 3;

if (m == 754974721) return 11;

if (m == 998244353) return 3;

int divs[20] = {};

divs[0] = 2;

int cnt = 1;

int x = (m - 1) / 2;

while (x % 2 == 0) x /= 2;

for (int i = 3; (long long)(i)*i <= x; i += 2) {

if (x % i == 0) {

divs[cnt++] = i;

while (x % i == 0) {

x /= i;

}

}

}

if (x > 1) {

divs[cnt++] = x;

}

for (int g = 2;; g++) {

bool ok = true;

for (int i = 0; i < cnt; i++) {

if (pow_mod_constexpr(g, (m - 1) / divs[i], m) == 1) {

ok = false;

break;

}

}

if (ok) return g;

}

}

template <int m> constexpr int primitive_root = primitive_root_constexpr(m);

// @param n `n < 2^32`

// @param m `1 <= m < 2^32`

// @return sum_{i=0}^{n-1} floor((ai + b) / m) (mod 2^64)

unsigned long long floor_sum_unsigned(unsigned long long n,

unsigned long long m,

unsigned long long a,

unsigned long long b) {

unsigned long long ans = 0;

while (true) {

if (a >= m) {

ans += n * (n - 1) / 2 * (a / m);

a %= m;

}

if (b >= m) {

ans += n * (b / m);

b %= m;

}

unsigned long long y_max = a * n + b;

if (y_max < m) break;

// y_max < m * (n + 1)

// floor(y_max / m) <= n

n = (unsigned long long)(y_max / m);

b = (unsigned long long)(y_max % m);

std::swap(m, a);

}

return ans;

}

} // namespace internal

} // namespace atcoder

#endif // ATCODER_INTERNAL_MATH_HPP

You can’t perform that action at this time.


## Links

[1]: 
[2]: /atcoder
[3]: /atcoder/ac-library
[4]: /login?return_to=%2Fatcoder%2Fac-library
[5]: /atcoder/ac-library/commits/master/atcoder/internal_math.hpp
[6]: https://github.com/atcoder/ac-library/raw/refs/heads/master/atcoder/internal_math.hpp
