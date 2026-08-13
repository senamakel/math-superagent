<!-- source: https://github.com/gttrcr/ResearchCode/blob/main/OEIS/A347924.cs | converted from HTML -->

rescode/OEIS/A347924.cs at main · gttrcr/rescode · GitHub

Skip to content

You signed in with another tab or window. [Reload][1] to refresh your session. You signed out in another tab or window. [Reload][1] to refresh your session. You switched accounts on another tab or window. [Reload][1] to refresh your session. Dismiss alert

{{ message }}

[gttrcr][2] /**[rescode][3]**Public

- [Notifications][4] You must be signed in to change notification settings
- [Fork 0][4]
-

[Star 0][4]

[3]

## Files Expand file tree

main

/

# A347924.cs

Copy path

Blame

More file actions

Blame

More file actions

## Latest commit

## History

[History][5]

[5] History

109 lines (94 loc) · 4.18 KB

main

/

# A347924.cs

Copy path

Top

## File metadata and controls

-

Code

-

Blame

109 lines (94 loc) · 4.18 KB

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

﻿using System;

using System.Collections.Generic;

using System.IO;

using System.Linq;

using System.Numerics;

using System.Threading;

using System.Threading.Tasks;

using Wolf; //use https://github.com/gttrcr/ParallelWolf

namespace OEIS

{

//driver function

//A347924.GenMthGilbreathPolynomial(3, 10);

class A347924

{

protected static string folder = "A347924\\";

public static void GenMthGilbreathPolynomial(int start, int length)

{

CreateOEISSequence(PrimeGCPolynomials(start, length, false)).Dispose();

}

protected static WolframLink PrimeGCPolynomials(int start, int delta = 1, bool output = true, WolframLink wolf = null)

{

List<BigInteger> prime = PrimeGen.GeneratePrimes(start + delta);

if (wolf == null)

wolf = new WolframLink();

return GCPolynomials(prime, start, output, wolf);

}

private static readonly Mutex writeMutex = new Mutex();

private static WolframLink GCPolynomials(List<BigInteger> seq, int start, bool output = false, WolframLink wolf = null)

{

if (wolf == null)

wolf = new WolframLink();

if (Directory.Exists(folder))

Directory.Delete(folder, true);

if (output)

Console.SetBufferSize(9999, 100);

Parallel.For(start, seq.Count, new ParallelOptions() { MaxDegreeOfParallelism = 8 }, (int i) =>

{

int terms = i;

double percentage = 0;

List<BigInteger> max = GC.MaxK(seq.GetRange(0, i), terms + 3, () =>

{

if (output)

{

writeMutex.WaitOne();

Console.SetCursorPosition(0, i - start);

Console.WriteLine((int)(100 * (++percentage / (terms + 3))));

writeMutex.ReleaseMutex();

}

});

string str = string.Join(",", max.Select(x => x.ToString()));

str = "t:={" + str + "};res:=Table[t[[n]]-2^(n+" + (i - 1).ToString() + "),{n,1,Length[t]}];FindSequenceFunction[res,n]";

str = wolf.Wolf(str);

string path = folder + i.ToString() + ".txt";

Directory.CreateDirectory(Path.GetDirectoryName(path));

File.WriteAllText(path, str);

});

if (output)

Console.SetCursorPosition(0, seq.Count - start);

return wolf;

}

protected static WolframLink CreateOEISSequence(WolframLink wolf = null, bool A347925 = false)

{

if (wolf == null)

wolf = new WolframLink();

string[] files = Directory.GetFiles(folder);

files = files.OrderBy(x => Convert.ToInt32(Path.GetFileNameWithoutExtension(x))).ToArray();

int a = 0;

List<Tuple<string, string>> sequence = new List<Tuple<string, string>>();

for (int i = 0; i < files.Length; i++)

{

int m = Convert.ToInt32(Path.GetFileNameWithoutExtension(files[i]));

string content = File.ReadAllText(files[i]);

string den = wolf.Wolf("Denominator[" + content + "]");

string coeff = wolf.Wolf("CoefficientList[(" + den + ") (" + content + "), n]");

List<string> l = wolf.ToArray(coeff);

if (A347925)

sequence.Add(new Tuple<string, string>((++a).ToString(), den.ToString()));

else

{

l.ForEach(x => sequence.Add(new Tuple<string, string>((++a).ToString(), x)));

for (int c = l.Count; c < m; c++)

sequence.Add(new Tuple<string, string>((++a).ToString(), "0"));

}

}

string res = "";

sequence.ForEach(x => res += x.Item1 + " " + x.Item2 + Environment.NewLine);

Console.WriteLine(res);

Console.WriteLine();

Console.WriteLine(string.Join(", ", sequence.Select(x => x.Item2)));

//File.WriteAllText("..\\..\\b347360.txt", res);

return wolf;

}

}

}

You can’t perform that action at this time.


## Links

[1]: 
[2]: /gttrcr
[3]: /gttrcr/rescode
[4]: /login?return_to=%2Fgttrcr%2Frescode
[5]: /gttrcr/rescode/commits/main/OEIS/A347924.cs
[6]: https://github.com/gttrcr/rescode/raw/refs/heads/main/OEIS/A347924.cs
