> **Excerpt only — read this first.** The complete text is beside it at `research/loopy.full.md`; open that only when this file does not answer the question, because it is large. Replace this excerpt with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, and specific enough that nobody needs the full text.

<!-- source: https://en.wikipedia.org/wiki/Loopy_game | converted from HTML -->

Loopy game - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

 |

**This article has multiple issues.**Please help **[improve it][1]**or discuss these issues on the **[talk page][2]**. *( [Learn how and when to remove these messages][3])*

[image: icon] [4]

 |

This article **relies on a [single source][5]**. Please help [improve this article][1] by [adding citations to reliable sources][6]. Unsourced material may be challenged and [removed][7].
*Find sources:*["Loopy game"][8] – [news][9]**·**[newspapers][10]**·**[books][11]**·**[scholar][12]**·**[JSTOR][13]*( January 2025)**( [Learn how and when to remove this message][3])*

 |

[image: icon] [4]

 |

An editor has determined that **[sufficient sources exist][14]**to establish the subject's [notability][15]. Please help [improve this article][16] by [adding citations to reliable sources][6]. Unsourced material may be challenged and removed.
*Find sources:*["Loopy game"][8] – [news][9]**·**[newspapers][10]**·**[books][11]**·**[scholar][12]**·**[JSTOR][13]*( September 2025)**( [Learn how and when to remove this message][3])*

 |

*( [Learn how and when to remove this message][3])*

 |

Type of game in combinatorial game theory

For game console, see [Casio Loopy][17].

In [combinatorial game theory][18], a **loopy game**is a [game][19] in which players can return to game states they have previously encountered, creating cycles in the [game tree][20]. This contrasts with **loop-free games**, where players can never return to previously encountered positions. Loop-free [finite games][21] are also referred to as **short games**. [1] Multiple real-life games allow repetitions ( [Fox and Geese][22], [Hare and Hounds][23], Backsliding Toads and Frogs). [Go][24] stands somewhere in-between with the "ko" rule restricting many, but not all, repetitions. [2]

The study of loopy games extends traditional combinatorial game theory by incorporating games that can theoretically continue indefinitely due to their cyclic nature. They introduce additional complexity in analysis and can exhibit behaviors not found in finite games.

The infinite nature of loopy games, similar to [transfinite games][25], introduces an additional outcome beyond the traditional win-loss dichotomy: a **tie**or **draw**. In this framework, a player is said to **survive**a game if they achieve either a tie or a win, expanding the classical analysis of game outcomes.

For [impartial games][26] that contain loops, analysis can be conducted using extensions of the [Sprague–Grundy theorem][27], which generalizes the classical result to handle the complexities introduced by cyclic game structures.

## Notation

[[edit][28]]

In combinatorial game theory notation, games are defined recursively by specifying the moves available to the Left and Right players using the format {Left options|Right options}. Some fundamental loopy games include:

- **dud**: {dud|dud} - a game where both players can only move back to the same position, creating an infinite loop with no winner (known as the "deathless universal draw")
- **on**: {on|} - a game where only the Left player has a move (back to the same position), while Right has no moves and loses immediately
- **off**: {|off} - a game where only the Right player has a move (back to the same position), while Left has no moves and loses immediately

These canonical loopy games exhibit interesting algebraic properties. For instance, on + off = dud, and dud + G = dud for any game G, demonstrating that dud acts as an [absorbing element][29] under game addition.

## Stoppers

[[edit][30]]

Stoppers are loopy games that have no subpositions with infinite alternating runs. Unlike generic loopy games, stoppers can never tie.

## Examples

[[edit][31]]

- [Checkers][32]
- [Fox and Geese][22]

## References

[[edit][33]]


*[excerpt ends; 4434 characters not shown — see `research/loopy.full.md`]*
