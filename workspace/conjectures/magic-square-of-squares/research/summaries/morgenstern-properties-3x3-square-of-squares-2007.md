> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/morgenstern-properties-3x3-square-of-squares-2007.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: http://www.multimagie.com/MorgensternMssProperties.pdf | converted from PDF -->

1 / 1 1

      3 x 3   M a g i c   S q u a r e   o f   S q u a r e s   P r o p e r t i e s

                                                      L e e   M o r g e n s t e r n

                                                              J u l y ,   2 0 1 5

                                                    A b s t r a c t

          O l d   p r o p e r t i e s   n e w l y   p r o v e d   u s i n g   o n l y   e l e m e n t a r y   n u m b e r   t h e o r y .
          P r o o f s   o f   n e w   p r o p e r t i e s   n o t   c o v e r e d   e l s e w h e r e .
          U n d e r s t a n d i n g   t h e   p r o o f s   r e q u i r e s   k n o w l e d g e   o f   o n l y   m o d u l a r   a r i t h m e t i c
          a n d   q u a d r a t i c   r e s i d u e s .

I n t r o d u c t i o n
T h i s   p a p e r   w a s   i n s p i r e d   b y   L a n d o n   W .   R a b e r n ' s   " P r o p e r t i e s   o f   m a g i c   s q u a r e s
o f   s q u a r e s "   w h i c h   u s e s   a l g e b r a i c   n u m b e r   t h e o r y   t o   p r o v e   s e v e r a l   p r o p e r t i e s
o f   t h e   e n t r i e s   i n   a   3 x 3   m a g i c   s q u a r e   o f   d i s t i n c t   s q u a r e s .     A l l   o f   R a b e r n ' s
p r o p e r t i e s   c a n   b e   d e r i v e d   f r o m   t h e   p r o p e r t i e s   o f   t h r e e ‐ s q u a r e   a r i t h m e t i c
p r o g r e s s i o n s   w h i c h   r e q u i r e   o n l y   e l e m e n t a r y   n u m b e r   t h e o r y .

T h i s   p a p e r   e x p l a i n s   t h e s e   o l d   p r o p e r t i e s   i n   a   n e w   w a y   m a k i n g   t h e   p r o o f s
m o r e   u n d e r s t a n d a b l e   t o   a   w i d e r   a u d i e n c e   a n d   g i v i n g   g r e a t e r   i n s i g h t   i n t o
w h y   t h e s e   p r o p e r t i e s   a r e   t r u e .

T h i s   p a p e r   a l s o   c o n t a i n s   p r o o f s   o f   p r o p e r t i e s   n o t   c o v e r e d   i n   R a b e r n ' s   p a p e r .

L e m m a s   t h a t   a r e   u s e d   i n   t h e   p r o o f s
T h e s e   a r e   a l l   p r o v a b l e   u s i n g   e l e m e n t a r y   n u m b e r   t h e o r y .

L e m m a   1   T h e   s q u a r e   o f   a n   e v e n   n u m b e r   i s   0   ( m o d   4 ) .
( 2 n ) 2   =   4 n 2 ,   w h i c h   i s   a   m u l t i p l e   o f   4 .

L e m m a   2   T h e   s q u a r e   o f   a n   o d d   n u m b e r   i s   1   ( m o d   4 ) .
( 2 n + 1 ) 2   =   4 n 2   +   4 n   +   1   =   4 n ( n + 1 )   +   1 .

L e m m a   3   ‐ 1   i s   a   q u a d r a t i c   r e s i d u e   o f   a l l   1   ( m o d   4 )   p r i m e s ,
b u t   a   q u a d r a t i c   n o n ‐ r e s i d u e   o f   a l l   3   ( m o d   4 )   p r i m e s .

L e m m a   4   2   i s   a   q u a d r a t i c   r e s i d u e   o f   a l l   1   a n d   7   ( m o d   8 )   p r i m e s
b u t   a   q u a d r a t i c   n o n ‐ r e s i d u e   o f   a l l   3   a n d   5   ( m o d   8 )   p r i m e s .

L e m m a   5   I f   x   a n d   p   h a v e   n o   c o m m o n   f a c t o r ,   t h e n   t h e r e   e x i s t s   y
s u c h   t h a t   x y   =   1   ( m o d   p ) .

2 / 1 1

A P   L e m m a s

D e f i n i t i o n
A n   A P ,   A r i t h m e t i c   P r o g r e s s i o n   o f   t h r e e   s q u a r e s ,   A 2   < =   C 2   < =   B 2 ,
i s   s u c h   t h a t   B 2   ‐   C 2   =   C 2   ‐   A 2 ,   w h i c h   c a n   a l s o   b e   w r i t t e n
A 2   +   B 2   =   2 C 2 .

L e m m a   6   A l l   A P s   a r e   s c a l e d   v e r s i o n s   o f   p r i m i t i v e   A P s .
I f   d   =   g c d ( A , B , C ) ,   t h e n   t h e r e   e x i s t s   a , b , c   s u c h   t h a t
A   =   a d ,   B   =   b d ,   C   =   c d ,   a n d
a 2   +   b 2   =   2 c 2
w i t h   a , b , c   p a i r w i s e   c o p r i m e .

L e m m a   7   A   p r i m i t i v e   A P   h a s   t h e   f o r m u l a

*[excerpt ends; 23185 characters not shown — see `research/sources/morgenstern-properties-3x3-square-of-squares-2007.full.md`]*
