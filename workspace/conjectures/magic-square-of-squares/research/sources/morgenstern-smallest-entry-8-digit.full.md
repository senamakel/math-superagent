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

S u p p o s e   w e   h a v e   a   3 ‐ s q u a r e   a r i t h m e t i c   p r o g r e s s i o n   g i v e n   b y   L 2 ,   M n 2 ,   H n 2
w h e r e   0   <   L   <   M n   <   H n ,   a n d   s u p p o s e   t h a t   t h e   s m a l l e s t   v a l u e ,   L   =   1 .
H e r e   i s   a   l i s t   o f   t h e   p r o g r e s s i o n s   f o r   n   =   1   . . .   5 .

            n       L 2         M n 2         H n 2             S T E P

          ‐ ‐ ‐   ‐ ‐ ‐     ‐ ‐ ‐ ‐ ‐     ‐ ‐ ‐ ‐ ‐       ‐ ‐ ‐ ‐ ‐ ‐ ‐
            1       1 2           5 2           7 2                 2 4
            2       1 2         2 9 2         4 1 2               8 4 0
            3       1 2       1 6 9 2       2 3 9 2           2 8 5 6 0
            4       1 2       9 8 5 2     1 3 9 3 2         9 7 0 2 2 4
            5       1 2     5 7 4 1 2     8 1 1 9 2     3 2 9 5 9 0 8 0

E v e r y   3 ‐ s q u a r e   a r i t h m e t i c   p r o g r e s s i o n   s t a r t i n g   f r o m   1   c a n   b e   p r o d u c e d
u s i n g   a   s i m p l e   r e c u r s i o n .     N o t e   h o w   f a s t   t h e   s t e p   v a l u e s   i n c r e a s e   i n   s i z e .
I f   t h e r e   w e r e   a   m a g i c   s q u a r e   h a v i n g   1   a s   t h e   s m a l l e s t   v a l u e ,   b u t   w i t h
t h e   l a r g e s t   v a l u e   h a v i n g   1 0 0   d i g i t s ,   t h a t   s o l u t i o n   c o u l d   b e   f o u n d   i n   a b o u t
6 6   i t e r a t i o n s   o f   t h e   r e c u r s i o n .

B u t   b e c a u s e   a n y   c h o i c e   o f   t h e   l a r g e s t   s t e p   v a l u e   i s   m o r e   t h a n   t w i c e   t h e   s i z e
o f   a n y   s t e p   v a l u e   b e l o w   i t ,   t h e r e   c a n ' t   b e   a   s e l e c t i o n   o f   t h r e e   s t e p   v a l u e s
w i t h   t h e   r e l a t i o n s h i p   ( a ,   b ,   a + b ) .     T h e r e f o r e   L   =   1   c a n n o t   b e   t h e   s m a l l e s t
e n t r y   i n   t h i s   7 ‐ s q u a r e   c o n f i g u r a t i o n .     T h i s   a l s o   m e a n s   t h a t   1   c a n n o t   b e   t h e
s m a l l e s t   e n t r y   i n   a n y   3 x 3   m a g i c   s q u a r e   o f   d i s t i n c t   s q u a r e s .

3 / 2 6

O t h e r   s t a r t i n g   v a l u e s   c a n   b e   p r o v e d   i m p o s s i b l e   u s i n g   a   t e r m i n a t i o n   c o n d i t i o n ,
d e r i v e d   i n   t h i s   p a p e r .   I t   h a s   b e e n   f o u n d   t h a t   t h e   t e r m i n a t i o n   c o n d i t i o n   o c c u r s
s u r p r i s i n g l y   e a r l y   i n   a   g e n e r a t e d   s e q u e n c e   o f   c a n d i d a t e   s t e p   v a l u e s .     S o   t h e
i m p o s s i b i l i t y   o f   e a c h   s t a r t i n g   v a l u e   t a k e s   v e r y   l i t t l e   t i m e   t o   p r o v e .

                                                    = = = = = = = = = = = = = = = = = =

T h i s   p a p e r   c o n t a i n s   a   p r o o f   t h a t   a l l   3 ‐ s q u a r e   a r i t h m e t i c   p r o g r e s s i o n s   w i t h
a   f i x e d   s t a r t i n g   v a l u e   c a n   b e   p r o d u c e d   b y   s i m p l e   r e c u r s i o n s   o f   a n
e a s i l y   o b t a i n a b l e   f i n i t e   s e t   o f   g e n e r a t o r s .

E a c h   r e c u r s i v e l y   p r o d u c e d   s e q u e n c e   c o n s i s t s   o f   v a l u e s   i n   a   n e a r ‐ g e o m e t r i c
p r o g r e s s i o n   i n c r e a s i n g   b y   a b o u t   3 4   t i m e s   f o r   e a c h   i t e r a t i o n ,   s o   t h e   n u m b e r s
g e t   v e r y   l a r g e   v e r y   f a s t .     T h i s   m a k e s   i t   p o s s i b l e   t o   d o   a   q u i c k   b u t   c o m p l e t e
s e a r c h   f o r   m a g i c   s q u a r e s   h a v i n g   e x t r e m e l y   l a r g e   n u m b e r s .

B u t   b e t t e r   t h a n   t h a t ,   t h i s   p a p e r   c o n t a i n s   a   p r o o f   t h a t   i f   a n   e n u m e r a t i o n   i s
d o n e   f o r   a   p a r t i c u l a r   s t a r t i n g   v a l u e ,   t h e n   o n c e   a   c e r t a i n   c o n d i t i o n   o c c u r s ,
i t   i s   n o   l o n g e r   p o s s i b l e   t o   a c h i e v e   a   s o l u t i o n ,   a n d   s o   t h e   e n u m e r a t i o n
c a n   b e   t e r m i n a t e d   a s   i m p o s s i b l e   t o   s a t i s f y .

P a r t   1
G e n e r a t i n g   A l l   A r i t h m e t i c   P r o g r e s s i o n s
T h i s   p a r t   o f   t h e   p a p e r   d e v e l o p s   a n d   p r o v e s   a   t e c h n i q u e   f o r   g e n e r a t i n g
a l l   p o s s i b l e   3 ‐ s q u a r e   a r i t h m e t i c   p r o g r e s s i o n s   h a v i n g   a   f i x e d   s t a r t i n g   v a l u e .
T h e   t e c h n i q u e   u s e s   a   r e c u r s i v e   f o r m u l a   w h i c h   t a k e s   a   " g e n e r a t o r "   p r o g r e s s i o n
a n d   p r o d u c e s   a n   i n f i n i t e   s e r i e s   o f   p r o g r e s s i o n s   w i t h   i n c r e a s i n g   v a l u e s .

T h e   A r i t h m e t i c   P r o g r e s s i o n   F o r m u l a
T h e   3 ‐ s q u a r e   a r i t h m e t i c   p r o g r e s s i o n   u n d e r   s t u d y   i s
          L 2 ,   M n 2 ,   H n 2 ,
w h e r e   L   i s   f i x e d .
T h e   s t e p   v a l u e   o f   t h e   p r o g r e s s i o n   =   M n 2   ‐   L 2   =   H n 2   ‐   M n 2 .
T h i s   i s   e x p r e s s e d   i n   t h i s   p a p e r   a s

( 1 )     L 2   =   2 M n 2   ‐   H n 2 ;       0   <   L   <   M n   <   H n .

W e   w a n t   t o   r e p r e s e n t   a   g i v e n   v a l u e   o f   L 2   a s   t h i s   b i n a r y   q u a d r a t i c   f o r m
i n   a l l   p o s s i b l e   w a y s .     W e   a l s o   w a n t   t o   g e n e r a t e   t h o s e   r e p r e s e n t a t i o n s ,
a s   n e e d e d ,   i n   H n   o r d e r :     H 1   <   H 2   <   H 3 ,   a n d   s o   o n .

4 / 2 6

T h e   r e c u r s i o n   d e s c r i b e d   b e l o w   w i l l   a c c o m p l i s h   t h i s ,   h o w e v e r ,   i t   m u s t   b e   n o t e d
t h a t   p u t t i n g   a   r e p r e s e n t a t i o n   u s i n g   ( M n , H n )   i n t o   t h e   r e c u r s i o n   d o e s   n o t
i n   g e n e r a l   p r o d u c e   ( M n + 1 , H n + 1 ) .     F o r   e x a m p l e ,   i f   L   i s   p r i m e ,
t h e n   p u t t i n g   ( M n , H n )   i n t o   t h e   r e c u r s i o n   w i l l   p r o d u c e   ( M n + 3 , H n + 3 ) .
T h u s ,   i n   t h i s   c a s e   w e   n e e d   t h r e e   d i f f e r e n t   r e c u r s i v e   s e q u e n c e s   i n   o r d e r
t o   p r o d u c e   a l l   t h e   r e p r e s e n t a t i o n s .

I n   t h i s   p a p e r ,   t h e   n u m b e r   o f   d i f f e r e n t   r e c u r s i v e   s e q u e n c e s   n e e d e d   t o   p r o d u c e
a l l   H n   v a l u e s   f o r   a   g i v e n   L   i s   g i v e n   b y   g .
T h a t   i s ,   p u t t i n g   ( M n , H n )   i n t o   t h e   r e c u r s i o n   p r o d u c e s   ( M n + g , H n + g ) .

F o r w a r d   R e c u r s i o n   T h e o r e m
G i v e n   a   r e p r e s e n t a t i o n   o f   ( 1 )   u s i n g   ( M n , H n )   f o r   a   g i v e n   L ,
t h e n   ( M n + g , H n + g )   g i v e n   b y
( 2 a )     M n + g   =   3 M n   +   2 H n ,
( 2 b )     H n + g   =   3 H n   +   4 M n
i s   a l s o   a   r e p r e s e n t a t i o n .

P r o o f
S t a r t i n g   w i t h
          2 M n + g 2   ‐   H n + g 2 ,
s u b s t i t u t e   ( 2 a ) ,   ( 2 b ) ,
          2 ( 3 M n   +   2 H n ) 2   ‐   ( 3 H n   +   4 M n ) 2 ,
e x p a n d   t h e   t e r m s ,
          1 8 M n 2   +   8 H n 2   +   2 4 H n M n   ‐   ( 9 H n 2   +   1 6 M n 2   +   2 4 H n M n ) ,
a n d   c a n c e l ,   p r o d u c i n g
          2 M n 2   ‐   H n 2 ,

w h i c h   f r o m   ( 1 )   i s   e q u a l   t o   L 2 .
T h u s
          2 M n + g 2   ‐   H n + g 2   =   L 2 .

R e m a r k
N o t e   t h a t   t h e   r e c u r s i o n   h a s   o n l y   p o s i t i v e   c o e f f i c i e n t s ,   t h e r e f o r e
s t a r t i n g   w i t h   a   r e p r e s e n t a t i o n   u s i n g   p o s i t i v e   n u m b e r s ,   t h e   r e c u r s i o n   p r o d u c e s
a   s e q u e n c e   o f   r e p r e s e n t a t i o n s   u s i n g   i n c r e a s i n g l y   l a r g e r   p o s i t i v e   n u m b e r s .

5 / 2 6

E x a m p l e
T h e   n u m b e r   o f   d i f f e r e n t   r e c u r s i o n   s e q u e n c e s   t h a t   c a n   b e   p r o d u c e d   f o r   a   g i v e n   L
i s   g i v e n   b y   g .     S u p p o s e   t h a t   L   =   7 .     I t   w i l l   b e   f o u n d   t h a t   g   =   3 .
T h e   s m a l l e s t   r e p r e s e n t a t i o n   u s e s
          ( M 1 , H 1 )   =   (   1 3 ,   1 7 ) ;   7 2   =   2 ( 1 3 2 )   ‐   1 7 2 .
P u t t i n g   t h e s e   v a l u e s   i n t o   t h e   r e c u r s i o n   p r o d u c e s
          ( M 4 , H 4 )   =   (   7 3 , 1 0 3 ) ;   7 2   =   2 ( 7 3 2 )   ‐   1 0 3 2 ;

          ( M 7 , H 7 )   =   ( 4 2 5 , 6 0 1 ) ;   7 2   =   2 ( 4 2 5 2 )   ‐   6 0 1 2 .

H e r e   i s   t h e   s e c o n d   s m a l l e s t   r e p r e s e n t a t i o n   f o r   L   =   7 .
I t   p r o d u c e s   a   d i f f e r e n t   s e q u e n c e .
          ( M 2 , H 2 )   =   (   1 7 ,   2 3 ) ;   7 2   =   2 ( 1 7 2 )   ‐   2 3 2 .
P u t t i n g   t h e s e   v a l u e s   i n t o   t h e   r e c u r s i o n   p r o d u c e s
          ( M 5 , H 5 )   =   (   9 7 , 1 3 7 ) ;   7 2   =   2 ( 9 7 2 )   ‐   1 3 7 2 ;

          ( M 8 , H 8 )   =   ( 5 6 5 , 7 9 9 ) ;   7 2   =   2 ( 5 6 5 2 )   ‐   7 9 9 2 .

H e r e   i s   t h e   t h i r d   s m a l l e s t   r e p r e s e n t a t i o n   w h e r e   H g   =   7 L .

          ( M 3 , H 3 )   =   (     3 5 ,     4 9 ) ;   7 2   =   2 ( 3 5 2 )   ‐   4 9 2 .
P u t t i n g   t h e s e   v a l u e s   i n t o   t h e   r e c u r s i o n   p r o d u c e s
          ( M 6 , H 6 )   =   (   2 0 3 ,   2 8 7 ) ;   7 2   =   2 ( 2 0 3 2 )   ‐   2 8 7 2 ;

          ( M 9 , H 9 )   =   ( 1 1 8 3 , 1 6 7 3 ) ;   7 2   =   2 ( 1 1 8 3 2 )   ‐   1 6 7 3 2 .

R e m a r k
N o t e   t h a t   H 1   t h r o u g h   H 9   a r e   i n   i n c r e a s i n g   o r d e r ,
e v e n   t h o u g h   t h e y   c a m e   f r o m   m u l t i p l e   s e q u e n c e s .     I t   w i l l   b e   p r o v e d   b e l o w
t h a t   t h i s   w i l l   a l w a y s   b e   t r u e   f o r   a n y   L .

R e v e r s e   R e c u r s i o n   F o r m u l a s
S o l v i n g   f o r   t h e   i n v e r s e   r e c u r s i o n   f o r m u l a s   f r o m   ( 2 a ) ,   ( 2 b ) ,
( 3 a )     M n   =   3 M n + g   ‐   2 H n + g ,
( 3 b )     H n   =   3 H n + g   ‐   4 M n + g .

R e m a r k
S i n c e   t h e   f o r w a r d   r e c u r s i o n   t a k e s   p o s i t i v e   v a l u e s   a n d   p r o d u c e s   a   s e q u e n c e
o f   e v e r ‐ i n c r e a s i n g   v a l u e s ,   t h e   r e v e r s e   r e c u r s i o n   m u s t   p r o d u c e   a   s e q u e n c e   o f
e v e r ‐ d e c r e a s i n g   v a l u e s .

6 / 2 6

5 / 7   L e m m a
G i v e n   a   r e p r e s e n t a t i o n   o f   ( 1 )   u s i n g   ( M n , H n )   f o r   a   g i v e n   L ,
i f
          H n   >   7 L ,
t h e n
          M n   <   ( 5 / 7 ) H n .

P r o o f
I f   H n   >   7 L   t h e n
          L   <   H n / 7
a n d   c o m b i n i n g   w i t h   ( 1 )
          2 M n 2   =   H n 2   +   L 2   <   H n 2   +   H n 2 / 4 9
o r
          M n 2   <   ( 2 5 / 4 9 ) H n 2
o r
          M n   <   ( 5 / 7 ) H n .

R e v e r s e   R e c u r s i o n   R e d u c t i o n   L e m m a
G i v e n   a   r e p r e s e n t a t i o n   o f   ( 1 )   u s i n g   ( M n + g , H n + g )   f o r   a   g i v e n   L ,
t h e n   a p p l y i n g   t h e   r e v e r s e   r e c u r s i o n   ( 3 a ) , ( 3 b )   t o   p r o d u c e   ( M n , H n ) ,
i f
          H n + g   >   7 L ,
t h e n
          H n   >   L .

P r o o f
I f   H n + g   >   7 L ,   t h e n   f r o m   t h e   5 / 7   L e m m a
          M n + g   <   ( 5 / 7 ) H n + g .
C o m b i n i n g   w i t h   ( 3 a ) ,
          H n   =   3 H n + g   ‐   4 M n + g   >   3 H n + g   ‐   4 ( 5 / 7 ) H n + g
o r
          H n   >   H n + g / 7 .
A n d   s i n c e   H n + g   >   7 L ,
          H n   >   L .

7 / 2 6

F i n i t e   G e n e r a t o r   T h e o r e m
A   g e n e r a t o r   i s   a   r e p r e s e n t a t i o n   o f   ( 1 )   t h a t   i s   n o t   p r o d u c e d   b y   a n y   o t h e r
r e p r e s e n t a t i o n   u s i n g   t h e   r e c u r s i o n   ( 2 a ) , ( 2 b ) .     F o r   a   g i v e n   v a l u e   o f   L ,
t h e r e   i s   a   f i n i t e   n u m b e r ,   g ,   o f   g e n e r a t o r s   u s i n g   ( M 1 , H 1 )   . . .   ( M g , H g )
a n d   L   <   H 1   <   . . .   <   H g   <   7 L .

P r o o f
S t a r t i n g   f r o m   a n y   r e p r e s e n t a t i o n   w h e r e   H n   >   7 L   a n d   a p p l y i n g   t h e   r e v e r s e
r e c u r s i o n   ( 3 a ) , ( 3 b )   r e p e a t e d l y ,   w e   w i l l   e v e n t u a l l y   e n c o u n t e r   a   t e r m i n a l
r e p r e s e n t a t i o n   w i t h   H t   <   7 L ,   f o r   s o m e   t .
W h e n   t h i s   h a p p e n s ,   t h e   p r e v i o u s   r e p r e s e n t a t i o n   t h a t   p r o d u c e d   i t
m u s t   h a v e   h a d   H t + g   >   7 L ,   t h u s   t h i s   t e r m i n a l   r e p r e s e n t a t i o n
m u s t   h a v e   H t   >   L   b y   t h e   R e v e r s e   R e c u r s i o n   R e d u c t i o n   L e m m a .

T h e r e f o r e ,   t h i s   t e r m i n a l   r e p r e s e n t a t i o n   h a s   L   <   H t   <   7 L ,
a n d   i s   t h e   g e n e r a t o r   o f   t h e   s e q u e n c e   o f   r e p r e s e n t a t i o n s   t h a t   w e r e
e n c o u n t e r e d   u s i n g   t h e   a b o v e   r e v e r s e   r e c u r s i o n   p r o c e d u r e .     W h e n   t h e
f o r w a r d   r e c u r s i o n   ( 2 a ) , ( 2 b )   i s   a p p l i e d ,   a l l   r e p r e s e n t a t i o n s
i n   t h a t   s e q u e n c e   a r e   r e a c h a b l e .

S i n c e   s t a r t i n g   f r o m   a n y   r e p r e s e n t a t i o n   a n d   a p p l y i n g   t h e   r e v e r s e   r e c u r s i o n
a l w a y s   e v e n t u a l l y   p r o d u c e s   a   r e p r e s e n t a t i o n   w i t h   L   <   H t   <   7 L ,
t h e n   a l l   r e p r e s e n t a t i o n s   w i t h   n u m b e r s   g r e a t e r   t h a n   t h a t   r a n g e   a r e   r e a c h a b l e
b y   s t a r t i n g   w i t h   a   r e p r e s e n t a t i o n   i n   t h a t   r a n g e   a n d   a p p l y i n g   t h e
f o r w a r d   r e c u r s i o n .     S i n c e   t h a t   r a n g e   i s   f i n i t e   f o r   a   g i v e n   v a l u e   o f   L ,
t h e   n u m b e r   o f   g e n e r a t o r s   i s   f i n i t e   f o r   a   g i v e n   L .

R e m a r k
F i n d i n g   a l l   g e n e r a t o r s   i s   j u s t   a   m a t t e r   o f   t e s t i n g   v a l u e s   f o r   H n ,
n   =   1   . . .   g ‐ 1 ,   i n   t h e   r a n g e   L   . . .   7 L   t h a t   s a t i s f y   ( 1 ) ;
t h e n   a d d i n g   H g   =   7 L ,   w h i c h   i s   a l w a y s   a   g e n e r a t o r .
P a r t   3   o f   t h i s   p a p e r   s h o w s   t h a t   t h e r e   e x i s t   f a s t e r   w a y s .

8 / 2 6

G e n e r a t o r   N o n r e d u n d a n c y   T h e o r e m
A l l   r e p r e s e n t a t i o n s   u s i n g   ( M n , H n )   w i t h   L   <   H n   <   7 L   a r e   g e n e r a t o r s .

R e m a r k
W h e n   s e a r c h i n g   f o r   g e n e r a t o r s   i n   t h e   f i n i t e   r a n g e ,   t h e r e   i s   n o   c h a n c e
t h a t   o n e   o f   t h e m   c o u l d   b e   p r o d u c e d   b y   a n o t h e r   i n   t h e   s a m e   r a n g e .
T h e r e f o r e ,   i n   a   c o m p u t e r   p r o c e d u r e ,   t h e r e   i s   n o   n e e d   t o   c h e c k   f o r
d u p l i c a t e   v a l u e s .

P r o o f
G i v e n   a   r e p r e s e n t a t i o n   u s i n g   ( H n , M n )   w i t h   L   <   H n   <   7 L ,
t h e n   f r o m   ( 1 ) ,
          2 M n 2   =   H n 2   +   L 2   >   2 L 2
t h u s
          M n   >   L .

F r o m   t h e   r e c u r s i o n   ( 2 a ) ,
          H n + g   =   3 H n   +   4 M n
a n d   s i n c e
          3 H n   +   4 M n   >   3 L   +   4 L   =   7 L
w e   h a v e
          H n + g   >   7 L .

T h e r e f o r e ,   o n e   a p p l i c a t i o n   o f   t h e   r e c u r s i o n   o n   a   g e n e r a t o r
a l w a y s   p r o d u c e s   a   r e p r e s e n t a t i o n   p a s t   t h e   r a n g e   o f   t h e   g e n e r a t o r s .
S o   t h e r e   i s   n o   c h a n c e   o f   f i n d i n g   a   n o n ‐ g e n e r a t o r   i n   t h e   g e n e r a t o r   r a n g e .

R e l a t i v e   P l a c e m e n t   T h e o r e m
A n y   t w o   d i f f e r e n t   r e c u r s i v e   s e q u e n c e s   p r o d u c e   m u t u a l l y   e x c l u s i v e
s e t s   o f   r e p r e s e n t a t i o n s   a n d   t h e i r   r e l a t i v e   p l a c e m e n t s   w i t h i n   t h e   s e t s
o f   s e q u e n c e s   n e v e r   c h a n g e .     T h i s   i s   b e c a u s e   H j   <   H k   i m p l i e s   H j + g   <   H k + g
f o r   a n y   j   a n d   k .

R e m a r k
T h i s   i s   i m p o r t a n t   f o r   t h e   o r d e r l y   e n u m e r a t i o n   o f   r e p r e s e n t a t i o n s .
T h e   e x a m p l e   a b o v e   w i t h   L   =   7   a n d   g   =   3   s h o w s   t h a t   t h e   H n   v a l u e s
a r e   p r o d u c e d   i n   i n c r e a s i n g   o r d e r   b y   a p p l y i n g   t h e   r e c u r s i o n   o n c e   f o r   e a c h
g e n e r a t o r   s e q u e n c e ,   t h e n   r e p e a t i n g   t h e   r e c u r s i o n   o n c e   e a c h   f o r   t h e
p r o d u c e d   v a l u e s ,   a n d   s o   o n .

9 / 2 6

P r o o f
S u p p o s e   ( M j , H j )   a n d   ( M k , H k )   a r e   u s e d   i n   t w o   d i f f e r e n t   r e p r e s e n t a t i o n s
p r o d u c e d   f r o m   p o s s i b l y   d i f f e r e n t   g e n e r a t e d   s e q u e n c e s   w i t h
          H j   <   H k .

W e   h a v e
          2 M j 2   ‐   H j 2   =   L 2 ,

          2 M k 2   ‐   H k 2   =   L 2 ,
t h u s
          2 M j 2   =   H j 2   +   L 2
a n d   s i n c e   H j   <   H k

          2 M j 2   <   H k 2   +   L 2
o r
          2 M j 2   <   2 M k 2
o r
          M j   <   M k .
T h e r e f o r e ,
          H j   <   H k   i m p l i e s   M j   <   M k .

S u p p o s e   t h a t   g   i s   t h e   n u m b e r   o f   g e n e r a t o r s   a n d   t h e   f o r w a r d   r e c u r s i o n
( 2 a ) , ( 2 b )   p r o d u c e s   H j + g   f r o m   H j   a n d   H k + g   f r o m   H k   i n   t h e
s e t s   o f   s e q u e n c e s .
T h e n
          H j + g   =   3 H j   +   4 M j
a n d   s i n c e   H j   <   H k   a n d   M j   <   M k
          H j + g   <   3 H k   +   4 M k
o r
          H j + g   <   H k + g .
T h e r e f o r e ,
          H j   <   H k   i m p l i e s   H j + g   <   H k + g
f o r   a n y   j   a n d   k ,   a n d   t h e i r   r e l a t i v e   p l a c e m e n t   n e v e r   c h a n g e s .
T h i s   a l s o   m e a n s   t h a t   t h e i r   v a l u e s   c a n   n e v e r   b e   t h e   s a m e ,   t h u s   m u l t i p l e
r e c u r s i v e   s e q u e n c e s   p r o d u c e   m u t u a l l y   e x c l u s i v e   v a l u e s .

1 0 / 2 6

P a r t   2
E n u m e r a t i n g   P o t e n t i a l   M a g i c   S q u a r e s
T h i s   p a r t   o f   t h e   p a p e r   d e s c r i b e s   a   p r o c e d u r e   f o r   e n u m e r a t i n g   a   s e q u e n c e
o f   3 ‐ s q u a r e   a r i t h m e t i c   p r o g r e s s i o n s   i n   o r d e r   t o   f i n d   a   m a g i c   s q u a r e .
W h e n   c e r t a i n   c o n d i t i o n s   o c c u r   i n   t h e   s e q u e n c e ,   t h e   p r o c e d u r e   t e r m i n a t e s
b e c a u s e   i t   i s   n o   l o n g e r   p o s s i b l e   t o   s a t i s f y   t h e   m a g i c   s q u a r e   r e q u i r e m e n t s .
T h e s e   t e r m i n a t i o n   c o n d i t i o n s   a r e   p r o v e d   b e l o w .

M a g i c   S q u a r e   R e q u i r e m e n t s
S e e   t h e   I n t r o d u c t i o n   t o   t h i s   p a p e r   f o r   a   d e s c r i p t i o n   o f   t h e   7 ‐ s q u a r e
s u b s e t   o f   t h e   3 x 3   m a g i c   s q u a r e   o f   d i s t i n c t   s q u a r e s   t h a t   w e   a r e   s t u d y i n g .
F o r   a   s o l u t i o n   t o   t h i s   c o n f i g u r a t i o n ,   w e   n e e d   t o   f i n d   t h r e e   3 ‐ s q u a r e
a r i t h m e t i c   p r o g r e s s i o n s   h a v i n g   t h e   s a m e   s t a r t i n g   v a l u e   a n d   t h e i r
s t e p   v a l u e s   m u s t   h a v e   t h e   r e l a t i o n s h i p   ( a ,   b ,   a + b ) .     I n   o t h e r   w o r d s ,
t h e   s u m   o f   t h e   s t e p   v a l u e s   o f   t h e   f i r s t   t w o   a r i t h m e t i c   p r o g r e s s i o n s
e q u a l s   t h e   s t e p   v a l u e   o f   t h e   t h i r d .

W e   c a n   a l s o   e x p r e s s   t h i s   w i t h   t w i c e   t h e   s t e p   v a l u e s .
T w i c e   t h e   s t e p   v a l u e   o f   a r i t h m e t i c   p r o g r e s s i o n   L 2 ,   M n 2 ,   H n 2

i s   ( H n 2   ‐   L 2 ) .

S o   w e   n e e d   t o   f i n d   t h r e e   r e p r e s e n t a t i o n s   o f   L 2   t h a t   u s e
( M i , H i ) ,   ( M j , H j ) ,   ( M k , H k )   a n d   t h a t   s a t i s f y   t h e   e q u a t i o n

          ( H i 2   ‐   L 2 )   +   ( H j 2   ‐   L 2 )   =   ( H k 2   ‐   L 2 ) .
N o t e   t h a t   H k   m u s t   b e   t h e   l a r g e s t   t e r m .

A d d i n g   2 L 2   t o   b o t h   s i d e s   g i v e s

( 4 )     H i 2   +   H j 2   =   H k 2   +   L 2 ;       H i   <   H j   <   H k .

M a g i c   S q u a r e   E n u m e r a t i o n   P r o c e d u r e
A f t e r   f i n d i n g   t h e   g e n e r a t o r s   ( M 1 , H 1 )   . . .   ( M g , H g ) ,   a r r a n g e d   i n
i n c r e a s i n g   H n   v a l u e ,   t h e n   t h e   r e s t   o f   t h e   r e p r e s e n t a t i o n s   c a n   b e

p r o d u c e d   i n   o r d e r ,   o n e   a t   a   t i m e ,   a n d   s u c c e s s i v e   v a l u e s   o f   H n 2
p u t   i n t o   a   l i s t .     T h e   i n c r e a s i n g   o r d e r   i s   g u a r a n t e e d   b y   t h e
R e l a t i v e   P l a c e m e n t   T h e o r e m .

E a c h   t i m e   a   n e w   H k 2   i s   p r o d u c e d ,   i t   c a n   b e   c h e c k e d   w i t h

c o m b i n a t i o n s   o f   H i 2   v a l u e s   t h a t   c o m e   b e f o r e   i t   i n   t h a t   l i s t
t o   t r y   a n d   s a t i s f y   ( 4 ) .

1 1 / 2 6

C h e c k i n g   i s   q u i c k e r   t h a n   y o u   m i g h t   t h i n k .     T h i s   i s   b e c a u s e ,
m o s t   o f   t h e   t i m e ,   H k ‐ 2 2   +   H k ‐ 1 2   <   H k 2   +   L 2 .
T h i s   m e a n s   t h a t   t h e   b i g g e s t   s u m   t h a t   c a n   b e   m a d e
u s i n g   p r e v i o u s   H i   v a l u e s   i s   t o o   s m a l l .
S o ,   a f t e r   j u s t   a   s i n g l e   c h e c k ,   a l l   p o s s i b l e   c o m b i n a t i o n s
u s i n g   t h e   l a t e s t   H k   c a n   b e   r e j e c t e d .

I t   w i l l   a l s o   b e   s e e n   b e l o w   t h a t   i f   t h e   s u m   i s   t o o   s m a l l   b y   2 L 2 ,
t h a t   i s ,   H k ‐ 2 2   +   H k ‐ 1 2   <   H k 2   ‐   L 2 ,   t h e n   H k + g ,   H k + 2 g ,   e t c .
c a n   a l s o   b e   r e j e c t e d .

W h e n   t h i s   s i m p l e   c a s e   d o e s   n o t   o c c u r ,   c h e c k i n g   c o m b i n a t i o n s   u s i n g   H k
c a n   b e   d o n e   i n   a t   w o r s t   l i n e a r   t i m e   i n   t h e   l e n g t h   o f   t h e   l i s t .
H e r e   i s   a   g e n e r a l   p r o c e d u r e .

          S e t   k   : =   n ;   i   : =   1 ;   j   : =   k ‐ 1
          D o
              C o m p a r e   H i 2   +   H j 2   t o   H k 2   +   L 2 ;
              I f   t o o   s m a l l ,   i n c r e m e n t   i ;
              E l s e   I f   t o o   l a r g e ,   d e c r e m e n t   j ;
              E l s e   j u s t   r i g h t ;   ( y o u   h a v e   f o u n d   a   m a g i c   s q u a r e   o f   7   s q u a r e s )
          W h i l e   i   <   j   ( w h i c h   w i l l   b e   a t   m o s t   k ‐ 2   t i m e s )

E x a m p l e
L e t ' s   u s e   t h e   L   =   7   n u m b e r s   a b o v e .

          n         1       2       3         4         5         6         7         8           9
          H n     1 7     2 3     4 9     1 0 3     1 3 7     2 8 7     6 0 1     7 9 9     1 6 7 3

i = 1 , j = 2 , k = 3
H 3 2   +   L 2   =   4 9 2   +   7 2   =   2 4 5 0 .

H 1 2   +   H 2 2   =   1 7 2   +   2 3 2   =   8 1 8 ,   t o o   s m a l l   b y   m o r e   t h a n   2 x 7 2 .

i = 2 , j = 3 , k = 4
H 4 2   +   L 2   =   1 0 3 2   +   7 2   =   1 0 6 5 8 .

H 2 2   +   H 3 2   =   2 3 2   +   4 9 2   =   2 9 3 0 ,   t o o   s m a l l   b y   m o r e   t h a n   2 x 7 2 ,
s o   i t ' s   n o t   n e c e s s a r y   t o   c h e c k   i = 1
b e c a u s e   t h e   s u m   w i l l   b e   e v e n   s m a l l e r .

i = 3 , j = 4 , k = 5
H 5 2   +   L 2   =   1 3 7 2   +   7 2   =   1 8 8 1 8 .

H 2 2   +   H 3 2   =   4 9 2   +   1 0 3 2   =   1 3 0 1 0 ,   t o o   s m a l l   b y   m o r e   t h a n   2 x 7 2 ,
s o   i t ' s   n o t   n e c e s s a r y   t o   c h e c k   i = 1   o r   i = 2
b e c a u s e   t h e   s u m   w i l l   b e   e v e n   s m a l l e r .

1 2 / 2 6

A s   t h e   f o l l o w i n g   p r o o f s   w i l l   s h o w ,   w e   n e e d   n o t   e n u m e r a t e   a n y   f u r t h e r .

T o   p r o v e   t h e   E n u m e r a t i o n   T e r m i n a t i o n   T h e o r e m ,   w e   n e e d   t w o   l e m m a s .

C h a n g i n g   G e o m e t r i c   P r o g r e s s i o n   L e m m a
I f   ( M j , H j )   a n d   ( M k , H k )   w i t h   j   <   k   a r e   u s e d   i n   ( 1 ) ,   t h e n
          H j + g / H j   >   H k + g / H k
a n d
          M j + g / M j   <   M k + g / M k .

P r o o f
I f   ( M j , H j )   a n d   ( M k , H k )   w i t h   j   <   k   a r e   u s e d   i n   ( 1 ) ,   t h e n
          H j   <   H k
t h u s
          L 2 / H j 2   >   L 2 / H k 2 .

D i v i d i n g   ( 1 )   b y   H n 2   g i v e s

          L 2 / H n 2   =   2 M n 2 / H n 2   ‐   1 .
S u b s t i t u t i n g   j   a n d   k   f o r   n   a n d   c o m b i n i n g   t h e   a b o v e   r e s u l t ,
          2 M j 2 / H j 2   ‐   1   >   2 M k 2 / H k 2   ‐   1
o r
          M j / H j   >   M k / H k .

U s i n g   t h e   f o r w a r d   r e c u r s i o n   f o r m u l a   ( 2 b )   a n d   d i v i d i n g   b y   H n ,
          H n + g / H n   =   3   +   4 M n / H n .
S u b s t i t u t i n g   j   a n d   k   f o r   n   a n d   c o m b i n i n g   t h e   a b o v e   r e s u l t ,
          H j + g / H j   =   3   +   4 M j / H j   >   3   +   4 M k / H k   =   H k + g / H k ,
T h e r e f o r e
          H j + g / H j   >   H k + g / H k .

R e p e a t i n g   t h e   d e r i v e d   c o n d i t i o n
          M j / H j   >   M k / H k
w e   a l s o   h a v e
          H j / M j   <   H k / M k .

U s i n g   t h e   f o r w a r d   r e c u r s i o n   f o r m u l a   ( 2 a )   a n d   d i v i d i n g   b y   M n ,
          M n + g / M n   =   3   +   2 H n / M n .
S u b s t i t u t i n g   j   a n d   k   f o r   n   a n d   c o m b i n i n g   t h e   a b o v e   r e s u l t ,
          M j + g / M j   =   3   +   2 H j / M j   <   3   +   2 H k / M k   =   M k + g / M k .
T h e r e f o r e
          M j + g / M j   <   M k + g / M k .

1 3 / 2 6

C o r r e s p o n d i n g   C o m b i n a t i o n   R e j e c t i o n   L e m m a
G i v e n   t h e   v a l u e s   H i ,   H j ,   H k   f r o m   a   s e q u e n c e   o f   r e p r e s e n t a t i o n s
o f   ( 1 )   f o r   a   g i v e n   L ,   w i t h   i   <   j   <   k ,

( C a s e   1 )
i f
          H i 2   +   H j 2   <   H k 2   ‐   L 2
t h e n
          H i + g 2   +   H j + g 2   <   H k + g 2   ‐   L 2 ;

( C a s e   2 )
i f
          H i 2   +   H j 2   >   H k 2   +   L 2
t h e n
          H i + g 2   +   H j + g 2   >   H k + g 2   +   L 2 .

R e m a r k
T h i s   m e a n s   t h a t   o n c e   o n e   o f   t h e   a b o v e   t w o   c a s e s   b e c o m e s   t r u e ,   i t   w i l l   a l s o
b e   t r u e   f o r   t h e   c o r r e s p o n d i n g   c o m b i n a t i o n   o f   v a l u e s   w i t h   i n d e x   o f f s e t s   o f
m u l t i p l e s   o f   g .     T h a t   i s ,   i f   i t ' s   t r u e   f o r   t h e   c o m b i n a t i o n   ( H i , H j , H k ) ,
t h e n   i t   w i l l   b e   t r u e   f o r   ( H i + g , H j + g , H k + g ) ,   ( H i + 2 g , H j + 2 g , H k + 2 g ) ,   a n d   s o   o n .

A l l   o f   t h e m   w i l l   p r o d u c e   a   s u m   o u t s i d e   o f   t h e   i n t e r v a l   H k 2   ±   L 2 ,
a n d   t h e r e f o r e   c a n   n e v e r   s a t i s f y   ( 4 ) .     T h e r e f o r e ,   i t   w i l l   n o   l o n g e r
b e   n e c e s s a r y   t o   c h e c k   t h o s e   c o m b i n a t i o n s   i n   t h e   r e s t   o f   t h e   e n u m e r a t i o n
f o r   a   g i v e n   v a l u e   o f   L .

P r o o f
( C a s e   1 )
I f
          H i 2   +   H j 2   <   H k 2   ‐   L 2 ,

t h e n   a d d i n g   2 L 2   t o   b o t h   s i d e s   a n d   u s i n g   ( 1 )   w e   g e t
          2 M i 2   +   2 M j 2   <   2 M k 2 .

M u l t i p l y i n g   b y   ( M k + g / M k ) 2 ,

          2 M i 2 ( M k + g / M k ) 2   +   2 M j 2 ( M k + g / M k ) 2   <   2 M k + g 2 .

F r o m   t h e   C h a n g i n g   G e o m e t r i c   P r o g r e s s i o n   L e m m a   w i t h   j   <   k ,
          M j + g / M j   <   M k + g / M k .
S q u a r i n g   a n d   r e a r r a n g i n g ,   w e   g e t
          M j + g 2   <   M j 2 ( M k + g / M k ) 2 .
S i m i l a r l y ,   w i t h   i   <   k ,
          M i + g 2   <   M i 2 ( M k + g / M k ) 2 .

1 4 / 2 6

C o m b i n i n g   t h e   a b o v e   r e s u l t s ,
          2 M i + g 2   +   2 M j + g 2   <   2 M k + g 2

a n d   t h e n   s u b t r a c t i n g   2 L 2   f r o m   b o t h   s i d e s   a n d   u s i n g   ( 1 ) ,
          H i + g 2   +   H j + g 2   <   H k + g 2   ‐   L 2 .

( C a s e   2 )
I f
          H i 2   +   H j 2   >   H k 2   +   L 2 ,

t h e n   m u l t i p l y i n g   b y   ( H k + g / H k ) 2 ,   w e   g e t

          H i 2 ( H k + g / H k ) 2   +   H j 2 ( H k + g / H k ) 2   >   H k + g 2   +   L 2 ( H k + g / H k ) 2 .

F r o m   t h e   C h a n g i n g   G e o m e t r i c   P r o g r e s s i o n   L e m m a   w i t h   j   <   k ,
          H j + g / H j   >   H k + g / H k .
S q u a r i n g   a n d   r e a r r a n g i n g ,   w e   g e t
          H j + g 2   >   H j 2 ( H k + g / H k ) 2 .
S i m i l a r l y ,   w i t h   i   <   k ,
          H i + g 2   >   H i 2 ( H k + g / H k ) 2 .

C o m b i n i n g   t h e   a b o v e   r e s u l t s ,
          H i + g 2   +   H j + g 2   >   H k + g 2   +   L 2 ( H k + g / H k ) 2 ,
a n d   s i n c e   H k + g / H k   >   1 ,

          H i + g 2   +   H j + g 2   >   H k + g 2   +   L 2 .

E n u m e r a t i o n   T e r m i n a t i o n   T h e o r e m
I f   f o r   g   c o n s e c u t i v e   v a l u e s   o f   H k ,   ( r + 1   <   k   <   r + g ) ,   f o r   s o m e   r ,

( 5 )     H 1 2   +   H k ‐ 1 2   <   H k 2   ‐   L 2
a n d   f o r   e a c h   c o m b i n a t i o n   o f   H i   a n d   H j ,   i   <   j   <   k ,
e i t h e r
( 6 )     H i 2   +   H j 2   <   H k 2   ‐   L 2
o r
( 7 )     H i 2   +   H j 2   >   H k 2   +   L 2 ,
t h e n   i t   i s   i m p o s s i b l e   f o r   a n y   H i ,   H j ,   H k   c o m b i n a t i o n
w h e r e   i   <   j   <   k   a n d   k   >   r + 1 ,   t o   s a t i s f y   ( 4 )   a n d   t h e
m a g i c   s q u a r e   e n u m e r a t i o n   f o r   t h e   g i v e n   v a l u e   o f   L   c a n   b e   t e r m i n a t e d .

P r o o f
I f   ( 6 )   o r   ( 7 )   a p p l i e s ,   t h e n   w e   k n o w   f r o m   t h e   C o r r e s p o n d i n g
C o m b i n a t i o n   R e j e c t i o n   L e m m a   t h a t   a l l   f u t u r e   c o r r e s p o n d i n g
c o m b i n a t i o n s   w i l l   n o t   s a t i s f y   ( 4 ) .
B u t   t h i s   d o e s n ' t   c o v e r   a l l   p o s s i b l e   f u t u r e   c o m b i n a t i o n s .
N e w   c o m b i n a t i o n s   w i l l   b e   c r e a t e d
b e c a u s e   t h e r e   a r e   m o r e   r e p r e s e n t a t i o n s   i n   t h e   l i s t .

1 5 / 2 6

F o r   e x a m p l e ,   s u p p o s e   ( 7 )   i s   m e t   u s i n g   i = 2 , j = k ‐ 1 ;   t h e   s u m   i s   t o o   b i g .
T h e n   w e   a l s o   k n o w   t h a t   ( 7 )   i s   m e t   u s i n g   i = 2 + g , j = k ‐ 1 + g .     B u t   t h e n ,
n e w   c o m b i n a t i o n s   w h e r e   i = 1 . . . g + 1   a n d   j = k ‐ 1 + g   c o u l d   h a v e   a   s m a l l e r   s u m .
T h e s e   w o u l d   n e e d   t o   b e   t e s t e d   ‐ ‐   u n l e s s   y o u   k n e w   t h a t   ( 5 )   w a s   m e t .
T h e n   a l l   n e w   c o m b i n a t i o n s   w o u l d   h a v e   a   s u m   w h i c h   w a s   t o o   s m a l l .
T h e r e f o r e ,   a f t e r   g   c o n s e c u t i v e   r e j e c t i o n s   u s i n g   t h e   a b o v e   c r i t e r i a ,
a l l   c o m b i n a t i o n s ,   o l d   a n d   n e w ,   c a n   b e   r e j e c t e d .

E x a m p l e
J u s t   f o r   c o m p l e t e n e s s ,   l e t ' s   t r y   t h e   e n u m e r a t i o n   f o r   L   =   1 ,   t o   p r o v e
t h a t   t h e   c o m m e n t s   i n   t h e   I n t r o d u c t i o n   a r e   t r u e .
O n l y   t h e   f i r s t   t h r e e   r e p r e s e n t a t i o n s   a r e   n e e d e d   b e c a u s e   g   =   1 .

          n       1       2         3
          H n     7     4 1     2 3 9

i = 1 , j = 2 , k = 3
H 3 2   ‐   L 2   =   2 3 9 2   ‐   1 2   =   5 7 , 1 2 0 .

H 1 2   +   H 2 2   =   7 2   +   4 1 2   =   1 7 3 0 .
C o n d i t i o n s   ( 5 )   a n d   ( 6 )   a r e   m e t   a n d   s i n c e   g   =   1 ,   w e   a r e   d o n e .     T h u s ,
1   c a n n o t   b e   t h e   l o w e s t   e n t r y   i n   a n y   3 x 3   m a g i c   s q u a r e   o f   d i s t i n c t   s q u a r e s .

E x a m p l e
L   =   4 1   i s   t h e   s m a l l e s t   v a l u e   o f   L   w h e r e   c o n d i t i o n   ( 7 )   a p p e a r s .
S i n c e   L   i s   p r i m e ,   g   =   3 .     W e   o n l y   n e e d   t h e   f i r s t   f i v e   r e p r e s e n t a t i o n s .

          n           1         2         3         4         5
          H n     1 1 3     1 1 9     2 8 7     6 7 9     7 1 3

i = 1 , j = 2 , k = 3
H 3 2   ‐   L 2   =   2 8 7 2   ‐   4 1 2   =   8 0 , 6 8 8 .

H 1 2   +   H 2 2   =   1 1 3 2   +   1 1 9 2   =   2 6 , 9 3 0 .
C o n d i t i o n s   ( 5 )   a n d   ( 6 )   a r e   m e t .

i = 2 , j = 3 , k = 4
H 4 2   ‐   L 2   =   6 7 9 2   ‐   4 1 2   =   4 5 9 , 3 6 0 .

H 2 2   +   H 3 2   =   1 1 9 2   +   2 8 7 2   =   9 6 , 5 3 0 .
C o n d i t i o n   ( 6 )   i s   m e t   f o r   t h e   l a r g e s t   v a l u e s   o f   i   a n d   j ,
t h e r e f o r e   c o n d i t i o n   ( 6 )   i s   m e t   f o r   a l l   c o m b i n a t i o n s ,
c o n d i t i o n   ( 5 )   b e i n g   o n e   o f   t h e m .

i = 3 , j = 4 , k = 5
H 5 2   +   L 2   =   7 1 3 2   +   4 1 2   =   5 1 0 , 0 5 0 .

H 3 2   +   H 4 2   =   2 8 7 2   +   6 7 9 2   =   5 4 3 , 4 1 0 .
C o n d i t i o n   ( 7 )   i s   m e t ,   s o   w e   n e e d   t o   t e s t   k = 5   f u r t h e r .

1 6 / 2 6

i = 2 , j = 4 , k = 5
H 5 2   ‐   L 2   =   7 1 3 2   ‐   4 1 2   =   5 0 6 , 6 8 8

H 2 2   +   H 4 2   =   1 1 9 2   +   6 7 9 2   =   4 7 5 , 2 0 2 .
C o n d i t i o n   ( 6 )   i s   m e t .     A l l   t h e   r e s t   o f   t h e   c o m b i n a t i o n s
w i l l   h a v e   l o w e r   s u m s   t h a n   t h i s   o n e ,   s o   t h e y   a l l   s a t i s f y   c o n d i t i o n   ( 6 ) .
C o n d i t i o n   ( 5 )   i s   a l s o   s a t i s f i e d .

W e   h a v e   3   c o n s e c u t i v e   r e j e c t i o n s   o f   a l l   c o m b i n a t i o n s ,   s o   4 1 2   c a n n o t
b e   t h e   l o w e s t   e n t r y   i n   a n y   3 x 3   m a g i c   s q u a r e   o f   d i s t i n c t   s q u a r e s .

E x a m p l e
L   =   7 1   i s   t h e   s m a l l e s t   v a l u e   o f   L   w h e r e   a   v a l u e   o f   H k   c a n n o t   b e
r e j e c t e d   a n d   m o r e   r e p r e s e n t a t i o n s   h a v e   t o   b e   g e n e r a t e d .
S i n c e   L   i s   p r i m e ,   g   =   3 .

          n         1         2         3         4           5           6           7
          H n     9 7     3 9 1     4 9 7     6 3 1     2 2 9 7     2 9 1 1     3 6 8 9

i = 1 , j = 2 , k = 3
H 3 2   ‐   L 2   =   4 9 7 2   ‐   7 1 2   =   2 4 1 , 9 6 8 .

H 1 2   +   H 2 2   =   9 7 2   +   3 9 1 2   =   1 6 2 , 2 9 0 .
C o n d i t i o n s   ( 5 )   a n d   ( 6 )   a r e   m e t .

i = 2 , j = 3 , k = 4
H 4 2   ‐   L 2   =   6 3 1 2   ‐   7 1 2   =   3 9 3 , 1 2 0 .

H 4 2   +   L 2   =   6 3 1 2   +   7 1 2   =   4 0 3 , 2 0 2 .

H 2 2   +   H 3 2   =   3 9 1 2   +   4 9 7 2   =   3 9 9 , 8 9 0 .
N e i t h e r   c o n d i t i o n   ( 6 )   o r   ( 7 )   i s   m e t ,   s o   w e   c a n ' t   r e j e c t   t h i s   c o m b i n a t i o n .
S i n c e   t h e   s u m   i s   t o o   s m a l l   f o r   ( 4 )   t o   b e   s a t i s f i e d ,   t h e r e ' s   n o   n e e d   t o   t r y
i = 1 , j = 3   o r   i = 1 , j = 2 ,   w h i c h   w o u l d   m a k e   a n   e v e n   s m a l l e r   s u m .

i = 3 , j = 4 , k = 5
H 5 2   ‐   L 2   =   2 2 9 7 2   ‐   7 1 2   =   5 , 2 7 1 , 1 6 8 .

H 3 2   +   H 4 2   =   4 9 7 2   +   6 3 1 2   =   6 4 5 , 1 7 0 .
C o n d i t i o n   ( 6 )   i s   m e t   a n d   t h u s   i s   m e t   b y   a l l   o t h e r   c o m b i n a t i o n s
i n c l u d i n g   c o n d i t i o n   ( 5 ) .

k = 6
S i n c e   a l l   c o m b i n a t i o n s   o f   k = 3   w e r e   r e j e c t e d   w i t h   ( 5 )   a n d   ( 6 ) ,   a l l   f u t u r e
c o m b i n a t i o n s   o f   k = 6 ,   k = 9 ,   e t c .   a r e   a l s o   r e j e c t e d   a n d   n e e d   n o t   b e   t e s t e d .

i = 5 , j = 6 , k = 7
H 7 2   +   L 2   =   3 6 8 9 2   +   7 1 2   =   1 3 , 6 1 3 , 7 6 2 .

H 5 2   +   H 6 2   =   2 2 9 7 2   +   2 9 1 1 2   =   1 3 , 7 5 0 , 1 3 0 .
C o n d i t i o n   ( 7 )   i s   m e t ,   s o   w e   n e e d   t o   t e s t   k = 7   f u r t h e r .

1 7 / 2 6

i = 4 , j = 6 , k = 7
H 7 2   ‐   L 2   =   3 6 8 9 2   ‐   7 1 2   =   1 3 , 6 0 3 , 6 8 0 .

H 4 2   +   H 6 2   =   6 3 1 2   +   2 9 1 1 2   =   8 , 8 7 2 , 0 8 2 .
C o n d i t i o n   ( 6 )   i s   m e t .     A l l   t h e   r e s t   o f   t h e   c o m b i n a t i o n s
w i l l   h a v e   l o w e r   s u m s   t h a n   t h i s   o n e ,   s o   t h e y   a l l   s a t i s f y   c o n d i t i o n   ( 6 ) .
C o n d i t i o n   ( 5 )   i s   a l s o   s a t i s f i e d .

W e   n o w   h a v e   3   c o n s e c u t i v e   r e j e c t i o n s   o f   a l l   c o m b i n a t i o n s ,   s o   7 1 2   c a n n o t
b e   t h e   l o w e s t   e n t r y   i n   a n y   3 x 3   m a g i c   s q u a r e   o f   d i s t i n c t   s q u a r e s .

E x a m p l e
L   =   4 9   i s   n o t   a   p r i m e   a n d   g   =   5 .

          n         1         2         3         4         5         6         7
          H n     7 1     1 1 9     1 6 1     2 5 7     3 4 3     4 5 7     7 2 1

T h e   f i r s t   5   t e s t s   a l l   m e e t   c o n d i t i o n s   ( 5 )   a n d   ( 6 ) ,   s o   w e   h a v e
5   c o n s e c u t i v e   r e j e c t i o n s   o f   a l l   c o m b i n a t i o n s .

E x a m p l e
L   =   1 1 9   i s   n o t   a   p r i m e   a n d   g   =   9 .
I t   w i l l   b e   f o u n d   t h a t   k   =   3 , 4 , 6 , 7 , 8   c a n ' t   b e   r e j e c t e d ,
b u t   k   =   9   t h r o u g h   1 7   a r e   r e j e c t e d ,   m a k i n g   9   c o n s e c u t i v e   r e j e c t i o n s .

P a r t   3
F i n d i n g   G e n e r a t o r s
T h i s   p a r t   o f   t h e   p a p e r   d e s c r i b e s   e f f i c i e n t   m e t h o d s   f o r   f i n d i n g
g e n e r a t o r s .     F o r   l a r g e   v a l u e s   o f   L ,   f i n d i n g   a l l   t h e   g e n e r a t o r s
c a n   b e   m o r e   t i m e ‐ c o n s u m i n g   t h a n   d o i n g   t h e   c a l c u l a t i o n s   t o   s e a r c h   f o r
t h e   m a g i c   s q u a r e   r e q u i r e m e n t s   a n d   t o   r e j e c t   c o m b i n a t i o n s .

P r i m e   F a c t o r   R e d u c t i o n
I n   a   3 ‐ s q u a r e   a r i t h m e t i c   p r o g r e s s i o n ,   i f   e i t h e r   t h e   l o w e s t   o r   h i g h e s t
v a l u e s   h a v e   a   p r i m e   f a c t o r   o f   t h e   f o r m   8 k + 3   o r   8 k + 5 ,   t h e n   a l l   t h r e e
t e r m s   w i l l   h a v e   t h a t   f a c t o r .     T h i s   a l s o   m e a n s   t h a t   a l l   7   o f   t h e   e n t r i e s
i n   a   m a g i c   s q u a r e   w i l l   h a v e   t h a t   f a c t o r .     S o   w e   c a n   d i v i d e   o u t   t h e   f a c t o r
p r o d u c i n g   a   s m a l l e r   m a g i c   s q u a r e .     T h e r e f o r e   i t   i s   n o t   n e c e s s a r y   t o   t e s t
v a l u e s   o f   L   a n d   H   h a v i n g   t h o s e   p r i m e s   a s   f a c t o r s .

T h i s   l e a v e s   v a l u e s   o f   L   a n d   H   h a v i n g   p r i m e   f a c t o r s   o f   o n l y   8 k + 1   a n d   8 k + 7 .
T h e   f i r s t   o f   t h e s e   n u m b e r s   a r e
1 ,   7 ,   1 7 ,   2 3 ,   3 1 ,   4 1 ,   4 7 ,   4 9 ,   7 1 ,   7 3 ,   7 9 ,   8 9 ,   9 7 ,   1 0 3 ,   1 1 3 ,   1 1 9 .

1 8 / 2 6

T h i s   r e d u c e s   t h e   n u m b e r   o f   L   v a l u e s   t h a t   n e e d   t o   b e   t e s t e d
a n d   a l s o   r e d u c e s   t h e   n u m b e r   o f   H   v a l u e s   t h a t   n e e d   t o   b e   s e a r c h e d
t o   f i n d   t h e   g e n e r a t o r s .     T h e y   b o t h   c o m e   f r o m   t h e   s a m e   l i s t .

P r o o f
G i v e n
          L 2   =   2 M 2   ‐   H 2 ,
w e   f a c t o r   t h i s   i n   t h e   u n i q u e   f a c t o r i z a t i o n   d o m a i n   Z [ √ ( 2 ) ]   a s
          L 2   =   ( M √ ( 2 )   +   H ) ( M √ ( 2 )   ‐   H ) .
I f   a   p r i m e   o f   t h e   f o r m   8 k + 3   o r   8 k + 5 ,   w h i c h   i s   a l s o   a   p r i m e   i n
t h e   d o m a i n   Z [ √ ( 2 ) ] ,   i s   a   f a c t o r   o f   L ,   t h e n   i t   m u s t   a l s o   b e
a   f a c t o r   o f   ( M √ ( 2 )   +   H )   o r   ( M √ ( 2 )   ‐   H ) .     I f   i t   i s   a   f a c t o r
o f   o n e   o f   t h e m ,   i t   i s   a l s o   a   f a c t o r   o f   t h e   c o n j u g a t e ,   s o   i t   i s   a
f a c t o r   o f   b o t h .     I f   i t   i s   a   f a c t o r   o f   b o t h ,   t h e n   i t   i s   a l s o   a   f a c t o r
o f   t h e i r   d i f f e r e n c e ,   w h i c h   i s   2 H .     S i n c e   t h e   f a c t o r   i s   o d d ,   i t   i s
a   f a c t o r   o f   L .     I f   i t   i s   a   f a c t o r   o f   H   a n d   L   a n d   o d d ,   t h e n   i t   i s   a l s o
a   f a c t o r   o f   M .     T h u s ,   i t   i s   a   f a c t o r   o f   a l l   t h r e e   t e r m s   a n d   c a n   b e
f a c t o r e d   o u t   t o   p r o d u c e   a   s m a l l e r   s o l u t i o n .     T h e r e f o r e ,   v a l u e s   o f   L
h a v i n g   p r i m e   f a c t o r s   o f   8 k + 3   o r   8 k + 5   n e e d   n o t   b e   t e s t e d .

F o r m u l a   f o r   t h e   N u m b e r   o f   G e n e r a t o r s
I f   t h e   p r i m e   f a c t o r i z a t i o n   o f
          L   =   p a q b . . . r c ,
t h e n   t h e   n u m b e r   o f   g e n e r a t o r s
          g   =   ( 2 a   +   1 ) ( 2 b   +   1 )   . . .   ( 2 c   +   1 ) .

E x a m p l e s
F o r   L   =   1 ,   g   =   1 .
G i v e n   t h a t   p ,   q ,   r   a r e   p r i m e s :
I f   L   =   p ,   t h e n   g   =   3 .
I f   L   =   p 2 ,   t h e n   g   =   5 .
I f   L   =   p 3 ,   t h e n   g   =   7 .
I f   L   =   p q ,   t h e n   g   =   9 .
I f   L   =   p 2 q ,   t h e n   g   =   1 5 .
I f   L   =   p q r ,   t h e n   g   =   2 7 .

1 9 / 2 6

G e n e r a t o r s   C o m e   I n   P a i r s
I f   ( M n , H n )   i s   a   g e n e r a t o r   f o r   a   g i v e n   L ,   t h e n   s o   i s   ( M p , H p )   g i v e n   b y
          M p   =   1 7 M n   ‐   1 2 H n ,
          H p   =   2 4 M n   ‐   1 7 H n .

P r o o f
W e   h a v e   t o   p r o v e   t h a t   ( M p , H p )   g i v e s   a   r e p r e s e n t a t i o n   o f   L 2   u s i n g   ( 1 ) .
S t a r t i n g   w i t h
          2 M p 2   ‐   H p 2
a n d   s u b s t i t u t i n g   t h e   r e l a t i o n   a b o v e
          2 ( 1 7 M n   ‐   1 2 H n ) 2   ‐   ( 2 4 M n   ‐   1 7 H n ) 2
e x p a n d   t h e   t e r m s   a n d   c a n c e l ,   p r o d u c i n g
          2 M n 2   ‐   H n 2

w h i c h   i s   e q u a l   t o   L 2 .

W e   a l s o   h a v e   t o   p r o v e   t h a t   t h e   f o r m u l a   p r o d u c e s   g e n e r a t o r s
f r o m   o t h e r   g e n e r a t o r s .
I f   ( M n , H n )   i s   a   g e n e r a t o r ,
t h e n   t h e i r   v a l u e s   r a n g e   f r o m
          M   =   L ,   H   =   L   t o     M   =   5 L ,   H   =   7 L .
T h u s   H p   r a n g e s   b e t w e e n
          2 4 L   ‐   1 7 L   a n d   2 4 x 5 L   ‐   1 7 x 7 L
o r
          7 L   a n d   L ,
t h e   s a m e   r a n g e   a s   H n   w h e n   i t   i s   a   g e n e r a t o r .

A l s o ,   t h e   c a s e   w h e r e   H p   =   H n   d o e s n ' t   e x i s t   s i n c e   i f
          H n   =   H p   =   2 4 M n   ‐   1 7 H n .
t h e n
          ( 3 / 4 ) H n   =   M n
a n d   p u t t i n g   t h i s   i n t o   ( 1 )   g i v e s
          2 ( 9 / 1 6 ) H n 2   ‐   H n 2   =   L n 2
o r
        H n 2   =   8 L 2
o r
        H n   =   L √ ( 8 )
w h i c h   c a n   n e v e r   b e   a n   i n t e g e r .

2 0 / 2 6

T h e   P r e ‐ G e n e r a t o r   M e t h o d
I n   t h e   f o r m u l a   f o r   t h e   n u m b e r   o f   g e n e r a t o r s ,   g   i s   a l w a y s   a n   o d d   n u m b e r .
B u t   H g   =   7 L   i s   a l w a y s   a   g e n e r a t o r .
S o   t h a t   l e a v e s   a n   e v e n   n u m b e r   o f   o t h e r   g e n e r a t o r s   b e t w e e n   L   a n d   7 L .
A s   t h e   a b o v e   p r o o f   s h o w s ,   t h e s e   o t h e r   g e n e r a t o r s   c o m e   i n   r e l a t e d   p a i r s .

S u p p o s e   t h a t   w e   h a v e   a   c o m p l e t e   s e t   o f   g e n e r a t o r s   f o r   a   g i v e n   L ,
A p p l y i n g   t h e   r e v e r s e   r e c u r s i o n   t o   t h e s e   v a l u e s
p r o d u c e s   a l l   v a l u e s   l e s s   t h a n   L   s o   t h a t   H n ‐ g   <   M n ‐ g   <   L .
A l l   M n ‐ g   v a l u e s   w i l l   b e   p o s i t i v e ,   b u t   e x a c t l y   h a l f   o f   t h e   H n ‐ g   v a l u e s
w i l l   b e   n e g a t i v e .
I f   H n   >   L √ ( 8 ) ,   t h e n   H n ‐ g   >   0 .
I f   H n   <   L √ ( 8 ) ,   t h e n   H n ‐ g   <   0 .

I f   ( M n ‐ g , ‐ H n ‐ g )   s a t i s f i e s   ( 1 ) ,   t h e n   s o   d o e s   ( M n ‐ g , H n ‐ g ) .
T h i s   m e a n s   t h a t   t h e   n e g a t i v e   v a l u e s   o f   H n ‐ g   a n d   p o s i t i v e   v a l u e s   o f   H n ‐ g
c o m e   i n   p a i r s   o f   e q u a l   a b s o l u t e   v a l u e .

T h e r e f o r e ,   w e   c a n   d o   a   f a s t e r   s e a r c h   f o r   g e n e r a t o r s   b y
l o o k i n g   f o r   v a l u e s   o f   H n ‐ g   i n   t h e   p r e ‐ g e n e r a t o r   r a n g e   0   <   H n ‐ g   <   L ,
w h i c h   i s   1 / 6   t h e   r a n g e   o f   L   <   H n   <   7 L .
F o r   e a c h   o f   t h e s e   p r e ‐ g e n e r a t o r s ,
w e   l i s t   b o t h   p o s i t i v e   a n d   n e g a t i v e   v a l u e s   o f   H n ‐ g .
W e   t h e n   p u t   t h e   p r e ‐ g e n e r a t o r s   i n t o   t h e   f o r w a r d   r e c u r s i o n
t o   g e t   t h e   g e n e r a t o r s .     T h e n   w e   a d d   H g   =   7 L   t o   t h e   l i s t .

T h e   P r i m e   F a c t o r   R e d u c t i o n   a l s o   a p p l i e s   t o   t h e s e   H n ‐ g   v a l u e s .
I t   i s   s u f f i c i e n t   t o   l i s t   v a l u e s   o f   H n ‐ g   t h a t   h a v e   p r i m e   f a c t o r s   o f
o n l y   8 k + 1   a n d   8 k + 7 .

E x a m p l e
F o r   L   =   7 ,   g   =   3 .
I n   t h e   r a n g e   1   . . .   7 ,   w e   f i n d   1   p r e ‐ g e n e r a t o r .
L i s t i n g   b o t h   t h e   n e g a t i v e   a n d   p o s i t i v e   p r e ‐ g e n e r a t o r s .
          n           1     2
          H n ‐ g   ‐ 1     1
          M n ‐ g     5     5
P u t t i n g   t h e s e   t h r o u g h   t h e   f o r w a r d   r e c u r s i o n   a n d   a d d i n g   7 L   p r o d u c e s
          n         1       2       3
          H n     1 7     2 3     4 9

2 1 / 2 6

E x a m p l e
F o r   L   =   1 1 9   =   7 x 1 7 ,   g   =   9 .
I n   t h e   r a n g e   1   . . .   1 1 9 ,   w e   f i n d   4   p r e ‐ g e n e r a t o r s .
L i s t i n g   b o t h   t h e   n e g a t i v e   a n d   p o s i t i v e   p r e ‐ g e n e r a t o r s .
          n             1       2       3       4       5       6       7         8
          H n ‐ g   ‐ 7 9   ‐ 4 9   ‐ 4 1   ‐ 1 7     1 7     4 1     4 9       7 9
          M n ‐ g   1 0 1     9 1     8 9     8 5     8 5     8 9     9 1     1 0 1
P u t t i n g   t h e s e   t h r o u g h   t h e   f o r w a r d   r e c u r s i o n   a n d   a d d i n g   7 L   p r o d u c e s
          n           1       2       3       4       5       6       7       8       9
          H n     1 6 7   2 1 7   2 3 3   2 8 9   3 9 1   4 7 9   5 1 1   6 4 1   8 3 3

C o m p o s i t i o n   o f   F o r m s
S u p p o s e   w e   h a v e   a l r e a d y   t e s t e d   L u   a n d   L v   a n d   h a v e   s a v e d   t h e
l i s t   o f   p r e ‐ g e n e r a t o r s   f o r   e a c h .     W e   t h e n   c o m e   t o   L w   =   L u L v .
W e   c a n   d i r e c t l y   c o m p u t e   a l l   t h e   p r e ‐ g e n e r a t o r s   f o r   L w   u s i n g   t h e
l i s t s   o f   p r e ‐ g e n e r a t o r s   f o r   L u   a n d   L v .

T o   d o   t h i s   w e   u s e   t h e   f o l l o w i n g   c o m p o s i t i o n   a n d   s c a l i n g   f o r m u l a s .

( 8 a )     M w   =     ( 2 M u M v   +   H u H v )   ‐     ( M u H v   +   H u M v )
( 8 b )     H w   =   | ( 2 M u M v   +   H u H v )   ‐   2 ( M u H v   +   H u M v ) |

( 9 a )     M w   =   ( 2 M u M v   ‐   H u H v )   ‐     | M u H v   ‐   H u M v |
( 9 b )     H w   =   ( 2 M u M v   ‐   H u H v )   ‐   2 | M u H v   ‐   H u M v |

( 1 0 a )   M w   =   M u L v
( 1 0 b )   H w   =   H u L v

( 1 1 a )   M w   =   M v L u
( 1 1 b )   H w   =   H v L u

2 2 / 2 6

T o   u s e   t h e   a b o v e   f o r m u l a s   f o r   t h e   c a s e   w h e r e   L u   a n d   L v   h a v e   n o
p r i m e   f a c t o r s   i n   c o m m o n ,   f o l l o w   t h i s   p r o c e d u r e .

          F o r   e a c h   ( M u , H u ) ,
              F o r   e a c h   ( M v , H v ) ,
                  U s e   ( 8 a ) , ( 8 b ) ;
                  U s e   ( 9 a ) , ( 9 b ) .

          F o r   e a c h   M u , H u ) ,
              U s e   ( 1 0 a ) , ( 1 0 b ) .

          F o r   e a c h   ( M v , H v ) ,
              U s e   ( 1 1 a ) , ( 1 1 b ) .

I f   L w   i s   a   p o w e r   o f   a   p r i m e ,   p a ,   t h e n   i t s   p r e ‐ g e n e r a t o r s

c a n   b e   c o m p u t e d   f r o m   t h e   p r e ‐ g e n e r a t o r s   f o r   L u   =   p   a n d   L v   =   p a ‐ 1 .
T h e   p r o c e d u r e   i s   d i f f e r e n t ,   d e p e n d i n g   o n   w h e t h e r   t h e   p o w e r   i s   e v e n   o r   o d d .
I t   i s   a l s o   r e q u i r e d   t o   k e e p   t r a c k   o f   t h e   o n e   p r i m i t i v e   p r e ‐ g e n e r a t o r
i n   e a c h   l i s t   o f   p r e ‐ g e n e r a t o r s   f o r   p r i m e   p o w e r s .

F o r   a   p r i m e ,   t h e r e   i s   e x a c t l y   o n e   p r e ‐ g e n e r a t o r   a n d   i t   i s   p r i m i t i v e .
F o r   a   p r i m e   p o w e r ,   f o l l o w   t h i s   p r o c e d u r e .

          T o   c o m p u t e   t h e   s c a l e d   p r e ‐ g e n e r a t o r s   o f   L w :
          F o r   e a c h   ( M v , H v ) ,
              U s e   ( 1 1 a ) , ( 1 1 b ) .

          T o   c o m p u t e   t h e   p r i m i t i v e   p r e ‐ g e n e r a t o r   o f   L w :
          I f   t h e   p o w e r ,   a ,   i s   e v e n
                U s e   ( 8 a ) , ( 8 b )   o n   b o t h   p r i m i t i v e   p r e ‐ g e n e r a t o r s .
          E l s e
                U s e   ( 9 a ) , ( 9 b )   o n   b o t h   p r i m i t i v e   p r e ‐ g e n e r a t o r s .

E x a m p l e
L w   =   7 2 .
F o r   L u   =   7 ,   ( M u , H u )   =   { ( 5 , 1 ) }   a n d   i s   p r i m i t i v e .
F o r   L v   =   7 ,   ( M v , H v )   =   { ( 5 , 1 ) }   a n d   i s   p r i m i t i v e .
T h e   p o w e r   o f   t h e   p r i m e   i s   e v e n ,   s o   w e   u s e   ( 8 a ) , ( 8 b )   a n d   ( 1 1 a ) , ( 1 1 b ) .

                                          L u     M u   H u     M v   H v       M w     H w
            ( 8 a ) ,   ( 8 b )   ‐ ‐ >   ‐ ‐     5     1       5     1       4 1     3 1     ( p r i m i t i v e )
          ( 1 1 a ) , ( 1 1 b )   ‐ ‐ >     7     ‐     ‐       5     1       3 5       7

2 3 / 2 6

E x a m p l e
L w   =   7 3 .

F o r   L u   =   7 ,     ( M u , H u )   =   { ( 5 , 1 ) }   a n d   i s   p r i m i t i v e .

F o r   L v   =   7 2 ,   ( M v , H v )   =   { ( 3 5 , 7 ) ,   ( 4 1 , 3 1 ) } ,
t h e   l a s t   o n e   b e i n g   p r i m i t i v e .
T h e   p o w e r   o f   t h e   p r i m e   i s   o d d ,   s o   w e   u s e   ( 9 a ) , ( 9 b )   a n d   ( 1 1 a ) , ( 1 1 b ) .

                                          L u     M u   H u       M v   H v         M w     H w
            ( 9 a ) ,   ( 9 b )   ‐ ‐ >   ‐ ‐     5     1       4 1   3 1       2 6 5   1 5 1     ( p r i m i t i v e )
          ( 1 1 a ) , ( 1 1 b )   ‐ ‐ >     7     ‐     ‐       4 1   3 1       2 8 7   2 1 7
          ( 1 1 a ) , ( 1 1 b )   ‐ ‐ >     7     ‐     ‐       3 5     7       2 4 5     4 9

E x a m p l e
L w   =   3 9 1   =   1 7 x 2 3
F o r   L u   =   2 3 ,   ( M u , H u )   =   { ( 1 7 , 7 ) } .
F o r   L v   =   1 7 ,   ( M v , H v )   =   { ( 1 3 , 7 ) } .

                                          L u     L v       M u   H u       M v   H v         M w     H w
            ( 8 a ) ,   ( 8 b )   ‐ ‐ >   ‐ ‐     ‐ ‐     1 7     7       1 3     7       2 8 1     7 1
            ( 9 a ) ,   ( 9 b )   ‐ ‐ >   ‐ ‐     ‐ ‐     1 7     7       1 3     7       3 6 5   3 3 7
          ( 1 0 a ) , ( 1 0 b )   ‐ ‐ >   ‐ ‐     1 7     1 7     7       ‐ ‐     ‐       2 8 9   1 1 9
          ( 1 1 a ) , ( 1 1 b )   ‐ ‐ >   2 3     ‐ ‐       ‐     ‐       1 3     7       2 9 9   1 6 1

E x a m p l e
L w   =   1 9 1 5 9   =   4 9 x 3 9 1   =   7 2 x ( 1 7 x 2 3 )
F o r   L u   =   4 9 ,     ( M u , H u )   =   { ( 4 1 , 3 1 ) , ( 3 5 , 7 ) } .
F o r   L v   =   3 9 1 ,   ( M v , H v )   =   { ( 2 8 1 , 7 1 ) , ( 2 8 9 , 1 1 9 ) , ( 2 9 9 , 1 6 1 ) , ( 3 6 5 , 3 3 7 ) } .

                                          L u     L v     M u   H u         M v     H v           M w         H w
            ( 8 a ) ,   ( 8 b )   ‐ ‐ >   ‐ ‐   ‐ ‐ ‐     4 1   3 1     2 8 1     7 1     1 3 6 2 1     1 9 9 9
            ( 8 a ) ,   ( 8 b )   ‐ ‐ >   ‐ ‐   ‐ ‐ ‐     4 1   3 1     2 8 9   1 1 9     1 3 5 4 9       2 8 9
            ( 8 a ) ,   ( 8 b )   ‐ ‐ >   ‐ ‐   ‐ ‐ ‐     4 1   3 1     2 9 9   1 6 1     1 3 6 3 9     2 2 3 1
            ( 8 a ) ,   ( 8 b )   ‐ ‐ >   ‐ ‐   ‐ ‐ ‐     4 1   3 1     3 6 5   3 3 7     1 5 2 4 5     9 8 8 7
            ( 8 a ) ,   ( 8 b )   ‐ ‐ >   ‐ ‐   ‐ ‐ ‐     3 5     7     2 8 1     7 1     1 5 7 1 5   1 1 2 6 3
            ( 8 a ) ,   ( 8 b )   ‐ ‐ >   ‐ ‐   ‐ ‐ ‐     3 5     7     2 8 9   1 1 9     1 4 8 7 5     8 6 8 7
            ( 8 a ) ,   ( 8 b )   ‐ ‐ >   ‐ ‐   ‐ ‐ ‐     3 5     7     2 9 9   1 6 1     1 4 3 2 9     6 6 0 1
            ( 8 a ) ,   ( 8 b )   ‐ ‐ >   ‐ ‐   ‐ ‐ ‐     3 5     7     3 6 5   3 3 7     1 3 5 5 9       7 9 1

            ( 9 a ) ,   ( 9 b )   ‐ ‐ >   ‐ ‐   ‐ ‐ ‐     4 1   3 1     2 8 1     7 1     1 5 0 4 1     9 2 4 1
            ( 9 a ) ,   ( 9 b )   ‐ ‐ >   ‐ ‐   ‐ ‐ ‐     4 1   3 1     2 8 9   1 1 9     1 5 9 2 9   1 1 8 4 9
            ( 9 a ) ,   ( 9 b )   ‐ ‐ >   ‐ ‐   ‐ ‐ ‐     4 1   3 1     2 9 9   1 6 1     1 6 8 5 9   1 4 1 9 1
            ( 9 a ) ,   ( 9 b )   ‐ ‐ >   ‐ ‐   ‐ ‐ ‐     4 1   3 1     3 6 5   3 3 7     1 6 9 8 1   1 4 4 7 9
            ( 9 a ) ,   ( 9 b )   ‐ ‐ >   ‐ ‐   ‐ ‐ ‐     3 5     7     2 8 1     7 1     1 8 6 5 5   1 8 1 3 7
            ( 9 a ) ,   ( 9 b )   ‐ ‐ >   ‐ ‐   ‐ ‐ ‐     3 5     7     2 8 9   1 1 9     1 7 2 5 5   1 5 1 1 3
            ( 9 a ) ,   ( 9 b )   ‐ ‐ >   ‐ ‐   ‐ ‐ ‐     3 5     7     2 9 9   1 6 1     1 6 2 6 1   1 2 7 1 9
            ( 9 a ) ,   ( 9 b )   ‐ ‐ >   ‐ ‐   ‐ ‐ ‐     3 5     7     3 6 5   3 3 7     1 3 9 5 1     4 7 1 1

2 4 / 2 6

                                          L u     L v     M u   H u         M v     H v           M w         H w
          ( 1 0 a ) , ( 1 0 b )   ‐ ‐ >   ‐ ‐   3 9 1     4 1   3 1       ‐ ‐     ‐ ‐     1 6 0 3 1   1 2 1 2 1
          ( 1 0 a ) , ( 1 0 b )   ‐ ‐ >   ‐ ‐   3 9 1     3 5     7       ‐ ‐     ‐ ‐     1 3 6 8 5     2 7 3 7

          ( 1 1 a ) , ( 1 1 b )   ‐ ‐ >   4 9   ‐ ‐ ‐       ‐     ‐     2 8 1     7 1     1 3 7 6 9     3 4 7 9
          ( 1 1 a ) , ( 1 1 b )   ‐ ‐ >   4 9   ‐ ‐ ‐       ‐     ‐     2 8 9   1 1 9     1 4 1 6 1     5 8 3 1
          ( 1 1 a ) , ( 1 1 b )   ‐ ‐ >   4 9   ‐ ‐ ‐       ‐     ‐     2 9 9   1 6 1     1 4 6 5 1     7 8 8 9
          ( 1 1 a ) , ( 1 1 b )   ‐ ‐ >   4 9   ‐ ‐ ‐       ‐     ‐     3 6 5   3 3 7     1 7 8 8 5   1 6 5 1 3

F i n d i n g   P r e ‐ G e n e r a t o r s   F o r   P r i m e s
T h e   P r e ‐ G e n e r a t o r   M e t h o d   r e d u c e s   t h e   p r o b l e m   f r o m   s c a n n i n g   f o r   g e n e r a t o r s
i n   t h e   r a n g e   L   . . .   7 L   t o   i n s t e a d   s c a n n i n g   i n   t h e   1 / 6   s i z e   r a n g e   0   . . .   L .
T h e   C o m p o s i t i o n   o f   F o r m s   r e d u c e s   t h e   p r o b l e m   t o   s c a n n i n g   f o r   p r e ‐ g e n e r a t o r s
o n l y   f o r   p r i m e s ,   w h i l e   p r e ‐ g e n e r a t o r s   f o r   c o m p o s i t e s   a r e   d i r e c t l y   c o m p u t e d .
T h i s   s e c t i o n   s h o w s   h o w   t o   f u r t h e r   r e d u c e   t h e   w o r k   i n   f i n d i n g   t h e   p r e ‐ g e n e r a t o r
f o r   a   p r i m e   b y   s c a n n i n g   i n   t h e   m u c h   s m a l l e r   r a n g e   0   . . .   √ ( L ) .
A l s o ,   s i n c e   t h e r e   i s   o n l y   o n e   p r e ‐ g e n e r a t o r   f o r   a   p r i m e ,
o n c e   y o u   f i n d   i t ,   y o u   c a n   s t o p   s c a n n i n g .

I n s t e a d   o f   l o o k i n g   f o r   a   r e p r e s e n t a t i o n   f o r   L 2 ,
l o o k   f o r   t h e   r e p r e s e n t a t i o n ,
          L   =   2 m 2   ‐   h 2 ,
t h e n   u s e   o n e   o f   t h e   c o m p o s i t i o n   f o r m u l a s   t o   c o m p u t e
t h e   p r e ‐ g e n e r a t o r   f o r   L 2 .

( 1 2 a )     M   =     2 m 2   +   h 2   ‐   2 m h
( 1 2 b )     H   =   | 2 m 2   +   h 2   ‐   4 m h |

E x a m p l e s
          L       m     h           M       H                           L       m     h           M       H
          7       2     1           5       1                         8 9       7     3         6 5     2 3
        1 7       3     1         1 3       7                         9 7       7     1         8 5     7 1
        2 3       4     3         1 7       7                       1 0 3       8     5         7 3       7
        3 1       4     1         2 5     1 7                       1 1 3       9     7         8 5     4 1
        4 1       5     3         2 9       1                       1 2 7       8     1       1 1 3     9 7
        4 7       6     5         3 7     2 3                       1 3 7       9     5         9 7       7
        7 1       6     1         6 1     4 9                       1 5 1     1 0     7       1 0 9     3 1
        7 3       7     5         5 3     1 7                       1 9 1     1 0     3       1 4 9     8 9
        7 9       8     7         6 5     4 7                       1 9 9     1 0     1       1 8 1   1 6 1

R e m a r k
H e r e   a r e   s o m e   o b s e r v a t i o n s   t h a t   l e a d   t o   s o m e   e x t r a   t i m e   s a v i n g s .
A l l   t h e   h   v a l u e s   a r e   o d d .     A n   m   v a l u e   i s   o d d   w h e n   L   =   8 k + 1 .
A n   m   v a l u e   i s   e v e n   w h e n   L   =   8 k + 7 .     W i l l   t h i s   a l w a y s   b e   t r u e ?

2 5 / 2 6

P r o o f
W e   h a v e
          h 2   =   2 m 2   ‐   L .
2 m 2   i s   e v e n   a n d   L   i s   o d d ,   t h e r e f o r e   h   m u s t   b e   o d d .

T h e   s q u a r e   o f   a n   o d d   n u m b e r   h a s   t h e   f o r m   8 k + 1 .
T h e   s q u a r e   o f   a n   e v e n   n u m b e r   h a s   t h e   f o r m   8 k   o r   8 k + 4 .
W e   h a v e
          2 m 2   =   L   +   h 2 .
S i n c e   h   i s   o d d ,   h 2   h a s   t h e   f o r m   8 k + 1 .
I f   L   h a s   t h e   f o r m   8 k + 1 ,   t h e n   2 m 2   m u s t   h a v e   t h e   f o r m   8 k + 2 ,   a n d   m   m u s t   b e   o d d .
I f   L   h a s   t h e   f o r m   8 k + 7 ,   t h e n   2 m 2   m u s t   h a v e   t h e   f o r m   8 k ,   a n d   m   m u s t   b e   e v e n .

P a r t   4
F u t u r e   R e s e a r c h
T h i s   p a r t   o f   t h e   p a p e r   c o n t a i n s   i d e a s   f o r   e x t e n d i n g   t h e   r e s u l t s   t o   l a r g e r
n u m b e r s   a n d   d e t e r m i n i n g   p l a c e s   w h e r e   a   m a g i c   s q u a r e   m i g h t   b e   h i d i n g .

E x t e n d i n g   t h e   R e s u l t s
T h e   e n u m e r a t i o n   d e s c r i b e d   i n   t h e   I n t r o d u c t i o n   w a s   p e r f o r m e d   u s i n g   t h e
P r e ‐ G e n e r a t o r   M e t h o d ,   b u t   w i t h o u t   t h e   C o m p o s i t i o n   o f   F o r m s   o r   √ ( L )
P r i m e   s c a n n i n g .     T h u s ,   l o o k i n g   f o r   p r e ‐ g e n e r a t o r s   c o n s u m e d   m o s t   o f   t h e   t i m e .
S o   t h e   e n u m e r a t i o n   w a s   a b o r t e d   a f t e r   e x a m i n i n g   v a l u e s   o f   L   u p   t o   7   d i g i t s .

U s i n g   t h e   n e w   m e t h o d s   s h o u l d   s p e e d   u p   t h e   o p e r a t i o n   e n o u g h   s o   t h a t   m u c h
l a r g e r   v a l u e s   f o r   L   c a n   b e   t e s t e d .     A   n e w   i m p l e m e n t a t i o n   w o u l d   r e q u i r e
a   t e c h n i q u e   t o   b u i l d   v a l u e s   o f   L   f r o m   a   l i s t   o f   8 k + 1 / 8 k + 7   p r i m e s ,
s i m i l a r   t o   t h e   t e c h n i q u e   t h a t   C h r i s t i a n   B o y e r   u s e d   i n   h i s   s e a r c h .

I   l o o k   f o r w a r d   t o   a n   i n d e p e n d e n t   v e r i f i c a t i o n   o f   m y   r e s u l t s   a n d   a
p o s s i b l e   e x t e n s i o n   o f   i t ,   p o s s i b l y   e v e n   f i n d i n g   a   m a g i c   s q u a r e .

M a g i c   S q u a r e   S e a r c h   I d e a s
H e r e   a r e   s o m e   i d e a s   f o r   t r y i n g   v a r i o u s   v a l u e s   o f   L   t o   t r y   a n d   f i n d   a
m a g i c   s q u a r e   w i t h o u t   e n u m e r a t i n g   e v e r y t h i n g .

T h e   b e s t   v a l u e   o f   L   t o   u s e   f o r   f i n d i n g   a   m a g i c   s q u a r e   w o u l d   b e   o n e   t h a t
h a d   a   l o t   o f   d i f f e r e n t   s m a l l   p r i m e   f a c t o r s .     T h i s   i s   b e c a u s e   t h e   d e n s i t y
o f   H   v a l u e s   w o u l d   b e   g r e a t e s t ,   i n c r e a s i n g   t h e   c h a n c e   f o r   ( 4 )   t o   b e   m e t .
U s i n g   h i g h e r   p o w e r s   o f   t h e   s a m e   p r i m e   d o e s   n o t   i n c r e a s e   t h e   d e n s i t y
a s   m u c h   a s   d i f f e r e n t   p r i m e s .     T h i s   c a n   b e   s e e n   f r o m   t h e   f o r m u l a   f o r   t h e
n u m b e r   o f   g e n e r a t o r s .

2 6 / 2 6

A   p r o c e d u r e   t o   s e a r c h   f o r   a   m a g i c   s q u a r e   i s   t o   t r y   v a l u e s   o f   L   i n   t h e
f o l l o w i n g   s e q u e n c e ,
          7 ,   7 x 1 7 ,   7 x 1 7 x 2 3 ,   7 x 1 7 x 2 3 x 3 1 ,   e t c .
i n c l u d i n g   t h e   n e x t   p r i m e   f o r   e a c h   s e a r c h .
T h e   i d e a   i s   t h a t   i f   t h e r e   i s   a   s o l u t i o n   u s i n g   a   s u b s e t   o f   t h e s e   p r i m e s ,
t h e n   y o u   w o u l d   f i n d   a   s c a l e d   v e r s i o n   o f   t h e   s o l u t i o n .     S o   t h e r e   i s   n o   n e e d
t o   t r y   e v e r y   s u b s e t   w h e n   y o u   c a n   d o   t h e m   a l l   a t   o n c e .
M a k e   s u r e   y o u   h a v e   y o u r   g i a n t   i n t e g e r   a r i t h m e t i c   p a c k a g e   r e a d y .
