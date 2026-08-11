> **Excerpt only — read this first.** The complete text is one level down at `research/L0/siegel_zugzwang.full.md`; open that only when this file does not answer the question, because it is large. Replace this excerpt with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://library.slmath.org/books/Book56/files/12siegel.pdf | converted from PDF -->

Games of No Chance 3
MSRI Publications
Volume 56, 2009
 Coping with cycles

AARON N. SIEGEL

ABSTRACT. Loopy games are combinatorial games in which repetition is per-
mitted. The possibility of nonterminating play inevitably raises difﬁculties,
and several theories have addressed these by imposing a variety of assumptions
on the games under consideration. In this article we survey some signiﬁcant
results on partizan loopy games, focusing on the theory developed in the 1970s
by Conway, Bach and Norton.

1. Introduction

A substantial portion of combinatorial games research focuses on games with-
out repetition — those that are guaranteed to terminate after some ﬁnite number
of moves. Such games are highly tractable, both theoretically and computa-
tionally, and the full force of the classical partizan theory can be brought to bear
upon them. The great success of this theory has produced a vast body of splendid
results, but it has also resulted in an unjust neglect of games with repetition.
In the late 1970s, John Conway and his students, Clive Bach and Simon
Norton, introduced a disjunctive theory of partizan games with repetition —
called loopy games because their game graphs may contain cycles. They showed
that in many interesting cases, such games admit canonical forms. The past few
years have witnessed some signiﬁcant applications of this theory, to games as
diverse as Fox and Geese, Hare and Hounds, Entrepreneurial Chess, and one-
dimensional Phutball. In light of these advances, it is time for a reappraisal of
the theory with an eye to the future.

A short history. The ﬁrst disjunctive theory of loopy games is due to Cedric
A. B. Smith and Aviezri Fraenkel. They showed (independently) that the usual
Sprague–Grundy theory generalizes well to loopy games. In particular, many
impartial loopy games are equivalent to nimbers, and the remainder are char-
acterized by their nimber-valued options. Over a period of several decades,

91

92 AARON N. SIEGEL

Fraenkel and his students explored this theory in depth. They constructed nu-
merous examples and studied both their solutions and their computational com-
plexity.
The partizan theory was introduced by Robert Li, who studied Zugzwang
games, those in which it is a disadvantage to move. Li showed that Zugzwang
games are completely characterized by a certain pair of ordinary numbers. Soon
thereafter, Conway, Bach and Norton extended Li’s theory to a much broader
class of games. They showed that many loopy games  — including most po-
sitions encountered in actual play — decompose into a pair of much simpler
games, called the sides of  . Their theory was published in the ﬁrst edition of
Winning Ways, together with a handful of examples, most notably the children’s
game Fox and Geese.
Intermittent progress was made over the next twenty years, but it was not until
2003 that loopy games saw a full-ﬂedged revival. John Tromp and Jonathan
Welton had recently detected an error in the Winning Ways analysis of Fox and
Geese, and Berlekamp set out to repair it. His corrected analysis appears in the
second edition of Winning Ways. Berlekamp’s effort led to the development of
new algorithms, which in turn paved the way for a re-examination of several
other loopy games mentioned in Winning Ways.
In this survey, the Winning Ways theory is introduced ﬁrst, so that earlier
developments — notably those of Smith, Fraenkel and Li — can be presented
in the modern context. Section 2 is an expository overview of some interest-
ing properties of loopy games, with a focus on Fox and Geese. Much of that
material is formalized in Section 3, and in Section 4 we tackle the theory of
sides as it appears in Winning Ways. Each of these sections also addresses some
related topics. Section 5 discusses several speciﬁc partizan games that have been

*[excerpt ends; 60052 characters not shown — see `research/L0/siegel_zugzwang.full.md`]*
