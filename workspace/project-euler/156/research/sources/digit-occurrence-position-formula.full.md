<!-- source: https://web.archive.org/web/20170709023503/http://www.geeksforgeeks.org/number-of-occurrences-of-2-as-a-digit-in-numbers-from-0-to-n/ | converted from HTML -->

Number of occurrences of 2 as a digit in numbers from 0 to n - GeeksforGeeks

▲

**Interview Preparation |

[Company Preparation][1] |

[Top Topics][2] |

[Placements][3] |

[Interview Corner][4] |

[Recent Interview Experiences][5] |

[GQ Home Page][6] |

[Quiz Corner][7] |

[LMNs][8] |

**Practice Platform** |

[What's New ?][9] |

[Leaderboard !!][10] |

[Company-wise Problems][11] |

[Topic-wise Problems][12] |

[Subjective Problems][13] |

[Difficulty Level - School][14] |

[Difficulty Level - Basic][15] |

[Difficulty Level - Easy][16] |

[Difficulty Level - Medium][17] |

[Difficulty Level - Hard][18] |

[How to pick a difficulty level?][19] |

[Explore More...][20] |

**Programming Languages** |

[C][21] |

[C++][22] |

[Java][23] |

[Python][24] |

[SQL][25] |

**Important Quick Links** |

[School Programming][26] |

[Operating Systems][27] |

[DBMS][28] |

[Computer Networks][29] |

[Engineering Mathematics][30] |

[Design Patterns][31] |

[Common Interview Puzzles][32] |

[Web Technology][33] |

[G-Facts][34] |

[Computer Graphics][35] |

[Image Processing][36] |

[Project Ideas][37] |

Count the number of 2s as digit in all numbers from 0 to n.

Examples:

```

Input : 22
Output : 6
Explanation: Total 2s that appear as digit
             from 0 to 22 are (2, 12, 20,
             21, 22);

Input : 100
Output : 20
Explanation: total 2's comes between 0 to 100
are (2, 12, 20, 21, 22..29, 32, 42, 52, 62, 72,
82, 92);
```

## ******[Recommended: Please solve it on “ PRACTICE ” first, before moving on to the solution.][38]

A **Simple Brute force**solution is to iterate through all numbers from 0 to n. For every number being visited, count the number of 2’s in it. Finally return total count.

Below is C++ implementation of the idea.

```

// C++ program to count 2s from 0 to n
#include <bits/stdc++.h>
using namespace std;

/* Counts the number of '2' digits in a
  single number */
int number0f2s(int n)
{
    int count = 0;
    while (n > 0)
    {
        if (n % 10 == 2)
            count++;

        n = n/10;
    }
    return count;
}

/* Counts the number of '2' digits between
   0 and n */
int numberOf2sinRange(int n)
{
    int count = 0 ; // Initialize result

    // Count 2's in every number from 2 to
    // n
    for (int i=2; i <= n; i++)
        count += number0f2s(i);

    return count;
}

// Driver Code
int main()
{
    cout << numberOf2sinRange(22);
    cout << endl;
    cout << numberOf2sinRange(100);
    return 0;
}
```

Output:

```

 6
 20
```

**Improved Solution **
The idea is to look at the problem digit by digit. Picture a sequence of numbers:

```

0  1  2  3  4  5  6  7  8  9
10 11 12 13 14 15 16 17 18 19
20 21 22 23 24 25 26 27 28 29
......
110 111 112 113 114 115 116 117 118 119
```

We know that roughly one tenth of the time, the last digit will be a 2 since it happens once in any sequence of ten numbers. In fact, any digit is a 2 roughly one tenth of the time.

We say “roughly” because there are (very common) boundary conditions. For example, between 1 and 100, the 10’s digit is a 2 exactly 1/10 th of the time. However, between 1 and 37, the 10’s digit is a 2 much more than 1/10 th of the time.

We can work out what exactly the ratio is by looking at the three cases individually: digit 2.

**Case digits < 2 **
Consider the value x = 61523 and digit at index d = 3 (here indexes are considered from right and rightmost index is 0). We observe that x[d] = 1. There are 2s at the 3rd digit in the ranges 2000 – 2999, 12000 – 12999, 22000 – 22999, 32000 32999, 42000 – 42999, and 52000 – 52999. So there are 6000 2’s total in the 3rd digit. This is the same amount as if we were just counting all the 2s in the 3rd digit between 1 and 60000.

In other words, we can round down to the nearest 10 d+1, and then divide by 10, to compute the number of 2s in the d-th digit.

```

if x[d) < 2: count2sinRangeAtDigit(x, d) =
  Compute y = round down to nearest 10d+1
  return y/10
```

**Case digit > 2 **
Now, let’s look at the case where d-th digit (from right) of x is greater than 2 (x[d] > 2). We can apply almost the exact same logic to see that there are the same number of 2s in the 3rd digit in the range 0 – 63525 as there as in the range 0 – 70000. So, rather than rounding down, we round up.

```

if x[d) > 2: count2sinRangeAtDigit(x, d) =
  Compute y = round down to nearest 10d+1
  return y / 10
```

**Case digit = 2 **
The final case may be the trickiest, but it follows from the earlier logic. Consider x = 62523 and d = 3. We know that there are the same ranges of 2s from before (that is, the ranges 2000 – 2999, 12000 – 12999, … , 52000 – 52999). How many appear in the 3rd digit in the final, partial range from 62000 – 62523? Well, that should be pretty easy. It’s just 524 (62000, 62001, … , 62523).

```

if x[d] = 2: count2sinRangeAtDigit(x, d) =
   Compute y = round down to nearest 10d+1
   Compute z = right side of x (i.e., x%  10d)
   return y/10 + z + 1
```

Now, all we need is to iterate through each digit in the number. Implementing this code is reasonably straightforward.

Below is C++ implementation of the idea.

```

// C++ program to count 2s from 0 to n
#include <bits/stdc++.h>
using namespace std;

/* Counts the number of 2s in a number at d-th
   digit */
int count2sinRangeAtDigit(int number, int d)
{
    int powerOf10 = (int)pow(10, d);
    int nextPowerOf10 = powerOf10 * 10;
    int right = number % powerOf10;

    int roundDown = number - number % nextPowerOf10;
    int roundup = roundDown + nextPowerOf10;

    int digit = (number / powerOf10) % 10;

    // if the digit in spot digit is
    if (digit < 2)
        return roundDown / 10;

    if (digit == 2)
        return roundDown / 10 + right+ 1;

    return roundup / 10;
}

/* Counts the number of '2' digits between 0 and n */
int numberOf2sinRange(int number)
{
    // Convert integer to String to find its length
    stringstream convert;
    convert << number;
    string s = convert.str();
    int len = s.length();

    /* Traverse every digit and count for every digit */
    int count = 0;
    for (int digit= 0; digit < len; digit++)
        count += count2sinRangeAtDigit(number, digit);

    return count;
}

// Driver Coden
int main()
{
    cout << numberOf2sinRange(22) << endl;
    cout << numberOf2sinRange(100);
    return 0;
}
```

Output:

```

 6
 20
```

This article is contributed by **Mr. Somesh Awasthi**. If you like GeeksforGeeks and would like to contribute, you can also write an article using [contribute.geeksforgeeks.org][39] or mail your article to contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks.
Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above.

Big Rectangle Blog Bottom -->

# **[GATE CS Corner][40] [Company Wise Coding Practice][41]**

## Recommended Posts:

- [Primality Test | Set 4 (Solovay-Strassen)][42]
- [43]
- [43]
- [43]
- [43]

arrPost.push(''); -->

[image: Facebook] [44][image: Google] [45][image: LinkedIn] [46][image: Twitter] [47][image: Pinterest][image: Reddit] [48][image: StumbleUpon] [49][image: Tumblr] [50]

Writing code in comment? Please use [ide.geeksforgeeks.org][51], generate link and share the link here.

Load Comments Share this post!

@geeksforgeeks, [Some rights reserved][52] [Contact Us!][53] [About Us!][54] [Advertise with us!][55] [Privacy Policy][56] [57] [58] [59] [60] [61] [62]


## Links

[1]: https://web.archive.org/web/20170709023503/http://www.geeksforgeeks.org/company-preparation/
[2]: https://web.archive.org/web/20170709023503/http://www.geeksforgeeks.org/interview-preparation-for-software-developer/
[3]: https://web.archive.org/web/20170709023503/http://www.geeksforgeeks.org/placements-gq/
[4]: https://web.archive.org/web/20170709023503/http://www.geeksforgeeks.org/company-interview-corner/
[5]: https://web.archive.org/web/20170709023503/http://www.geeksforgeeks.org/category/interview-experiences/
[6]: https://web.archive.org/web/20170709023503/http://www.geeksforgeeks.org/geeksquiz-home/
[7]: https://web.archive.org/web/20170709023503/http://www.geeksforgeeks.org/quiz-corner-gq/
[8]: https://web.archive.org/web/20170709023503/http://www.geeksforgeeks.org/lmns-gq/
[9]: https://web.archive.org/web/20170709023503/http://practice.geeksforgeeks.org/recent.php?ref=home
[10]: https://web.archive.org/web/20170709023503/http://practice.geeksforgeeks.org/ranking.php?ref=home
[11]: https://web.archive.org/web/20170709023503/http://practice.geeksforgeeks.org/company-tags/?ref=home
[12]: https://web.archive.org/web/20170709023503/http://practice.geeksforgeeks.org/topic-tags/?ref=home
[13]: https://web.archive.org/web/20170709023503/http://practice.geeksforgeeks.org/subjective-page.php?ref=home
[14]: https://web.archive.org/web/20170709023503/http://practice.geeksforgeeks.org/School/0/0/?ref=home
[15]: https://web.archive.org/web/20170709023503/http://practice.geeksforgeeks.org/Basic/0/0/?ref=home
[16]: https://web.archive.org/web/20170709023503/http://practice.geeksforgeeks.org/Easy/0/0/?ref=home
[17]: https://web.archive.org/web/20170709023503/http://practice.geeksforgeeks.org/Medium/0/0/?ref=home
[18]: https://web.archive.org/web/20170709023503/http://practice.geeksforgeeks.org/Hard/0/0/?ref=home
[19]: https://web.archive.org/web/20170709023503/http://practice.geeksforgeeks.org/pickACategory.php?ref=home
[20]: https://web.archive.org/web/20170709023503/http://practice.geeksforgeeks.org/?ref=home
[21]: https://web.archive.org/web/20170709023503/http://www.geeksforgeeks.org/c/
[22]: https://web.archive.org/web/20170709023503/http://www.geeksforgeeks.org/c-plus-plus/
[23]: https://web.archive.org/web/20170709023503/http://www.geeksforgeeks.org/java/
[24]: https://web.archive.org/web/20170709023503/http://www.geeksforgeeks.org/python/
[25]: https://web.archive.org/web/20170709023503/http://www.geeksforgeeks.org/sql-tutorial/
[26]: https://web.archive.org/web/20170709023503/http://www.geeksforgeeks.org/school-programming/
[27]: https://web.archive.org/web/20170709023503/http://www.geeksforgeeks.org/operating-systems/
[28]: https://web.archive.org/web/20170709023503/http://www.geeksforgeeks.org/dbms/
[29]: https://web.archive.org/web/20170709023503/http://www.geeksforgeeks.org/computer-network-tutorials/
[30]: https://web.archive.org/web/20170709023503/http://www.geeksforgeeks.org/engineering-mathematics-tutorials/
[31]: https://web.archive.org/web/20170709023503/http://www.geeksforgeeks.org/category/design-pattern/
[32]: https://web.archive.org/web/20170709023503/http://www.geeksforgeeks.org/category/puzzles/
[33]: https://web.archive.org/web/20170709023503/http://www.geeksforgeeks.org/web-technology/
[34]: https://web.archive.org/web/20170709023503/http://www.geeksforgeeks.org/category/gfact/
[35]: https://web.archive.org/web/20170709023503/http://www.geeksforgeeks.org/tag/computer-graphics/
[36]: https://web.archive.org/web/20170709023503/http://www.geeksforgeeks.org/tag/image-processing/
[37]: https://web.archive.org/web/20170709023503/http://www.geeksforgeeks.org/category/project/
[38]: https://web.archive.org/web/20170709023503/http://practice.geeksforgeeks.org/problems/occurences-of-2-as-a-digit/1
[39]: https://web.archive.org/web/20170709023503/http://www.contribute.geeksforgeeks.org/
[40]: https://web.archive.org/web/20170709023503/http://quiz.geeksforgeeks.org/gate-corner-2/
[41]: https://web.archive.org/web/20170709023503/http://practice.geeksforgeeks.org/company-tags
[42]: https://web.archive.org/web/20170709023503/http://www.geeksforgeeks.org/primality-test-set-4-solovay-strassen/
[43]: 
[44]: https://web.archive.org/web/20170709023503/http://www.facebook.com/sharer.php?u=http://www.geeksforgeeks.org/number-of-occurrences-of-2-as-a-digit-in-numbers-from-0-to-n/
[45]: https://web.archive.org/web/20170709023503/https://plus.google.com/share?url=http://www.geeksforgeeks.org/number-of-occurrences-of-2-as-a-digit-in-numbers-from-0-to-n/
[46]: https://web.archive.org/web/20170709023503/http://www.linkedin.com/shareArticle?mini=true&amp;url=http://www.geeksforgeeks.org/number-of-occurrences-of-2-as-a-digit-in-numbers-from-0-to-n/
[47]: https://web.archive.org/web/20170709023503/https://twitter.com/share?url=http://www.geeksforgeeks.org/number-of-occurrences-of-2-as-a-digit-in-numbers-from-0-to-n/&amp;text=Number of occurrences of 2 as a digit in numbers from 0 to n&amp;hashtags=GeeksforGeeks
[48]: https://web.archive.org/web/20170709023503/http://reddit.com/submit?url=http://www.geeksforgeeks.org/number-of-occurrences-of-2-as-a-digit-in-numbers-from-0-to-n/&amp;title=Number of occurrences of 2 as a digit in numbers from 0 to n
[49]: https://web.archive.org/web/20170709023503/http://www.stumbleupon.com/submit?url=http://www.geeksforgeeks.org/number-of-occurrences-of-2-as-a-digit-in-numbers-from-0-to-n/&amp;title=Number of occurrences of 2 as a digit in numbers from 0 to n
[50]: https://web.archive.org/web/20170709023503/http://www.tumblr.com/share/link?url=http://www.geeksforgeeks.org/number-of-occurrences-of-2-as-a-digit-in-numbers-from-0-to-n/&amp;title=Number of occurrences of 2 as a digit in numbers from 0 to n
[51]: https://web.archive.org/web/20170709023503/http://ide.geeksforgeeks.org/
[52]: https://web.archive.org/web/20170709023503/http://creativecommons.org/licenses/by-nc-nd/2.5/in/deed.en_US
[53]: https://web.archive.org/web/20170709023503/http://www.geeksforgeeks.org/about/contact-us/
[54]: https://web.archive.org/web/20170709023503/http://www.geeksforgeeks.org/about/
[55]: https://web.archive.org/web/20170709023503/http://www.geeksforgeeks.org/advertise-with-us/
[56]: https://web.archive.org/web/20170709023503/http://www.geeksforgeeks.org/privacy-policy/
[57]: https://web.archive.org/web/20170709023503/https://www.facebook.com/GeeksforGeeks-316764689022/timeline/
[58]: https://web.archive.org/web/20170709023503/https://twitter.com/geeksforgeeks
[59]: https://web.archive.org/web/20170709023503/https://www.linkedin.com/company-beta/1299009
[60]: https://web.archive.org/web/20170709023503/https://play.google.com/store/apps/details?id=free.programming.programming
[61]: https://web.archive.org/web/20170709023503/https://www.microsoft.com/en-us/store/apps/geeksforgeeks-official/9nblggh4rh30
[62]: https://web.archive.org/web/20170709023503/https://itunes.apple.com/us/app/geeksforgeeks/id1101205459?ls=1&amp;mt=8
