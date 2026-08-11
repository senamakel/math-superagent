<!-- source: https://en.wikipedia.org/wiki/Disjunctive_sum | converted from HTML -->

Disjunctive sum - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

Operation in combinatorial game theory

In the mathematics of [combinatorial games][1], the **sum**or **disjunctive sum**of two games is a game in which the two games are played in parallel, with each player being allowed to move in just one of the games per turn. The sum game finishes when there are no moves left in either of the two parallel games, at which point (in [normal play][2]) the last player to move wins. This operation may be extended to disjunctive sums of any number of games, again by playing the games in parallel and moving in exactly one of the games per turn. It is the fundamental operation that is used in the [Sprague–Grundy theorem][3] for [impartial games][4] and which led to the field of [combinatorial game theory][1] for [partisan games][5].

## Application to common games

[[edit][6]]

Disjunctive sums arise in games that naturally break up into components or regions that do not interact except in that each player in turn must choose just one component to play in. Examples of such games are [Go][7], [Nim][8], [Sprouts][9], [Domineering][10], the [Game of the Amazons][11], and the [map-coloring games][12].

In such games, each component may be analyzed separately for simplifications that do not affect its outcome or the outcome of its disjunctive sum with other games. Once this analysis has been performed, the components can be combined by taking the disjunctive sum of two games at a time, combining them into a single game with the same outcome as the original game.

## Mathematics

[[edit][13]]

The sum operation was formalized by Conway (1976). It is a [commutative][14] and [associative operation][15]: if two games are combined, the outcome is the same regardless of what order they are combined, and if more than two games are combined, the outcome is the same regardless of how they are grouped.

The negation −*G*of a game *G*(the game formed by trading the roles of the two players) forms an [additive inverse][16] under disjunctive sums: the game *G*+ −*G*is a [zero game][17] (won by whoever goes second) using a simple echoing strategy in which the second player repeatedly copies the first player's move in the other game. For any two games *G*and *H*, the game *H*+*G*+ −*G*has the same outcome as *H*itself (although it may have a larger set of available moves).

Based on these properties, the class of combinatorial games may be thought of as having the structure of an [abelian group][18], although with a [proper class][19] of elements rather than (as is more standard for groups) a set of elements. For an important subclass of the games called the [surreal numbers][20], there exists a multiplication operator that extends this group to a [field][21].

For impartial [misère][2] play games, an analogous theory of sums can be developed, but with fewer of these properties: these games form a [commutative][14] [monoid][22] with only one nontrivial invertible element, called [star][23] ( [*][23]), of order two.

## References

[[edit][24]]

- [Conway, John Horton][25] (1976), *[On Numbers and Games][26]*, Academic Press.

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Disjunctive_sum&oldid=1285733584][27] "

[Category][28]:

- [Combinatorial game theory][29]

Hidden categories:

- [Articles with short description][30]
- [Short description matches Wikidata][31]

Search

Disjunctive sum

Add languages Add topic


## Links

[1]: https://en.wikipedia.org/wiki/Combinatorial_game_theory
[2]: https://en.wikipedia.org/wiki/Misère_game
[3]: https://en.wikipedia.org/wiki/Sprague–Grundy_theorem
[4]: https://en.wikipedia.org/wiki/Impartial_game
[5]: https://en.wikipedia.org/wiki/Partisan_game
[6]: /w/index.php?title=Disjunctive_sum&amp;action=edit&amp;section=1
[7]: https://en.wikipedia.org/wiki/Go_(board_game)
[8]: https://en.wikipedia.org/wiki/Nim
[9]: https://en.wikipedia.org/wiki/Sprouts_(game)
[10]: https://en.wikipedia.org/wiki/Domineering
[11]: https://en.wikipedia.org/wiki/Game_of_the_Amazons
[12]: https://en.wikipedia.org/wiki/Map-coloring_games
[13]: /w/index.php?title=Disjunctive_sum&amp;action=edit&amp;section=2
[14]: https://en.wikipedia.org/wiki/Commutativity
[15]: https://en.wikipedia.org/wiki/Associativity
[16]: https://en.wikipedia.org/wiki/Additive_inverse
[17]: https://en.wikipedia.org/wiki/Zero_game
[18]: https://en.wikipedia.org/wiki/Abelian_group
[19]: https://en.wikipedia.org/wiki/Class_(set_theory)
[20]: https://en.wikipedia.org/wiki/Surreal_number
[21]: https://en.wikipedia.org/wiki/Field_(mathematics)
[22]: https://en.wikipedia.org/wiki/Monoid
[23]: https://en.wikipedia.org/wiki/Star_(game_theory)
[24]: /w/index.php?title=Disjunctive_sum&amp;action=edit&amp;section=3
[25]: https://en.wikipedia.org/wiki/John_Horton_Conway
[26]: https://en.wikipedia.org/wiki/On_Numbers_and_Games
[27]: https://en.wikipedia.org/w/index.php?title=Disjunctive_sum&amp;oldid=1285733584
[28]: /wiki/Help:Category
[29]: /wiki/Category:Combinatorial_game_theory
[30]: /wiki/Category:Articles_with_short_description
[31]: /wiki/Category:Short_description_matches_Wikidata
