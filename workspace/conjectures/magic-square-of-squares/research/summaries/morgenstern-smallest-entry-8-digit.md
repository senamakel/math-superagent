> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/morgenstern-smallest-entry-8-digit.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: http://multimagie.com/MorgensternMssSmallestEntry.pdf | converted from PDF -->

1 / 2 6

S m a l l e s t   E n t r y   i n   a   3 x 3   M a g i c   S q u a r e   o f   S q u a r e s

                                                    L e e   M o r g e n s t e r n

                                                            J u n e ,   2 0 0 7

                                                  A b s t r a c t

              T h i s   p a p e r   d e v e l o p s   a   c o m p u t e r   p r o c e d u r e   t h a t   h a s   p r o v e d   t h a t
              a l l   9   e n t r i e s   o f   a   3 x 3   m a g i c   s q u a r e   o f   d i s t i n c t   s q u a r e s
              m u s t   b e   a t   l e a s t   t h e   s q u a r e s   o f   8 ‐ d i g i t   n u m b e r s .

I n t r o d u c t i o n

P a r t   1   ‐   G e n e r a t i n g   A l l   A r i t h m e t i c   P r o g r e s s i o n s
T h e   A r i t h m e t i c   P r o g r e s s i o n   F o r m u l a
F o r w a r d   R e c u r s i o n   T h e o r e m
R e v e r s e   R e c u r s i o n   F o r m u l a s
5 / 7   L e m m a
R e v e r s e   R e c u r s i o n   R e d u c t i o n   L e m m a
F i n i t e   G e n e r a t o r   T h e o r e m
G e n e r a t o r   N o n r e d u n d a n c y   T h e o r e m
R e l a t i v e   P l a c e m e n t   T h e o r e m

P a r t   2   ‐   E n u m e r a t i n g   P o t e n t i a l   M a g i c   S q u a r e s
M a g i c   S q u a r e   R e q u i r e m e n t s
M a g i c   S q u a r e   E n u m e r a t i o n   P r o c e d u r e
C h a n g i n g   G e o m e t r i c   P r o g r e s s i o n   L e m m a
C o r r e s p o n d i n g   C o m b i n a t i o n   R e j e c t i o n   L e m m a
E n u m e r a t i o n   T e r m i n a t i o n   T h e o r e m

P a r t   3   ‐   F i n d i n g   G e n e r a t o r s
P r i m e   F a c t o r   R e d u c t i o n
F o r m u l a   f o r   t h e   N u m b e r   o f   G e n e r a t o r s
G e n e r a t o r s   C o m e   I n   P a i r s
T h e   P r e ‐ G e n e r a t o r   M e t h o d
C o m p o s i t i o n   o f   F o r m s
F i n d i n g   P r e ‐ G e n e r a t o r s   F o r   P r i m e s

P a r t   4   ‐   F u t u r e   R e s e a r c h
E x t e n d i n g   t h e   R e s u l t s
M a g i c   S q u a r e   S e a r c h   I d e a s

2 / 2 6

I n t r o d u c t i o n

A   n e c e s s a r y   c o n d i t i o n   f o r   a   3 x 3   m a g i c   s q u a r e   o f   d i s t i n c t   s q u a r e s
i s   a   s o l u t i o n   t o   a n y   o f   i t s   7 ‐ s q u a r e   s u b s e t s .
T h i s   p a p e r   s t u d i e s   t h e   f o l l o w i n g   7 ‐ s q u a r e   s u b s e t
w h e r e   a , b , c   >   0   a n d   t h u s ,   c ‐ ( a + b )   i s   t h e   s m a l l e s t   e n t r y .

          ‐ ‐ ‐ ‐ ‐ ‐ ‐     c ‐ ( a + b )     ‐ ‐ ‐ ‐ ‐ ‐ ‐
          c + ( b ‐ a )     c                 c ‐ ( b ‐ a )
          c ‐ b             c + ( a + b )     c ‐ a

T h i s   c o n f i g u r a t i o n   c o n t a i n s   t h r e e   a r i t h m e t i c   p r o g r e s s i o n s   h a v i n g   t h e
s a m e   s t a r t i n g   v a l u e :

          c ‐ ( a + b ) ,   c ‐ b ,   c ‐ ( b ‐ a ) ,   w i t h   s t e p   v a l u e   a ;
          c ‐ ( a + b ) ,   c ‐ a ,   c + ( b ‐ a ) ,   w i t h   s t e p   v a l u e   b ;   a n d
          c ‐ ( a + b ) ,   c ,       c + ( a + b ) ,   w i t h   s t e p   v a l u e   a + b .

S i n c e   t h e s e   v a l u e s   m u s t   b e   s q u a r e s ,   t h i s   m o t i v a t e s   t h e   s t u d y   o f
3 ‐ s q u a r e   a r i t h m e t i c   p r o g r e s s i o n s   h a v i n g   a   f i x e d   s t a r t i n g   v a l u e .
I f   w e   c a n   f i n d   a   s e t   o f   t h r e e   p r o g r e s s i o n s   t h a t   a l s o   h a v e   t h e
s t e p   v a l u e   r e l a t i o n s h i p   ( a ,   b ,   a + b ) ,   w e   w i l l   h a v e   f o u n d   a   m a g i c   s q u a r e
c o n t a i n i n g   a t   l e a s t   7   s q u a r e d   e n t r i e s .


*[excerpt ends; 66273 characters not shown — see `research/sources/morgenstern-smallest-entry-8-digit.full.md`]*
