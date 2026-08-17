<!-- source: https://uvadoc.uva.es/bitstream/10324/3602/1/TESIS367-130927.pdf | converted from PDF -->

FACULTAD DE CIENCIAS

DEPARTAMENTO DE ÁLGEBRA, ANÁLISIS MATEMÁTICO,
 GEOMETRÍA Y TOPOLOGÍA.

TESIS DOCTORAL:
  PERSPECTIVAS ARITMÉTICAS
PARA LA
CONJETURA DE CASAS-ALVERO

Presentada por
Rosa María de Frutos Marín
 para optar al grado de
doctora por la Universidad de Valladolid

Dirigida por:
Antonio Campillo López

PERSPECTIVAS ARITM´ETICAS

PARA LA

CONJETURA DE CASAS-ALVERO

Memoria presentada por
Rosa Mar´ıa de Frutos Mar´ın

para acceder al grado de doctor en Matem´aticas

Dirigida por
Antonio Campillo L´opez

Universidad de Valladolid

21 de Diciembre de 2012

A la memoria de mis padres, Felipe y Merche

Para Elisa,

y para Miguel

´Indice general

Introducci´on VII

1. El enunciado del problema 1

1.1. Preparaci´on de Tschirnhausen . . . . . . . . . . . . . . . . . . . . . . . . . . 2

1.2. Presentaci´on bin´omica del polinomio. La derivada neta . . . . . . . . . . . . 3

1.3. Formulaci´on mediante resultantes . . . . . . . . . . . . . . . . . . . . . . . . 5

1.3.1. Expresi´on en t´erminos de variedades algebraicas . . . . . . . . . . . 8

1.3.2. Expresi´on en t´erminos de ideales . . . . . . . . . . . . . . . . . . . . 9

1.3.3. Empleo de bases de Gr¨obner . . . . . . . . . . . . . . . . . . . . . . 10

2. Problemas parciales ( y primeras respuestas) 15

2.1. El problema parcial con conjunto I de exponentes . . . . . . . . . . . . . . 16

2.2. El monomio puro de una resultante, y el {i}-problema parcial . . . . . . . 17

2.3. El {i, j}-problema parcial . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19

2.4. Viabilidad del empleo de bases de Gr¨obner . . . . . . . . . . . . . . . . . . 30

3. Usando esquemas proyectivos 33

3.1. Esquemas asociados a los problemas total y parcial . . . . . . . . . . . . . . 39

3.2. La reducci´on m´odulo p . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42

3.3. Eliminaci´on de monomios m´odulo p . . . . . . . . . . . . . . . . . . . . . . . 45

3.4. Tri´angulo de Tartaglia en caracter´ıstica positiva . . . . . . . . . . . . . . . . 51

3.5. Los casos de cardinal 1 y 2 para Ip . . . . . . . . . . . . . . . . . . . . . . . 54

3.6. Conjeturas de transmisi´on de hip´otesis . . . . . . . . . . . . . . . . . . . . . 58

3.6.1. Conjeturas de propagaci´on . . . . . . . . . . . . . . . . . . . . . . . 60

3.6.2. Conjeturas de desplazamiento . . . . . . . . . . . . . . . . . . . . . . 62

3.6.3. Enunciado transversal al grado . . . . . . . . . . . . . . . . . . . . . 65

4. Condensaci´on y expansi´on 67

4.1. El supraesquema Yn
′ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67

VI ´INDICE GENERAL

4.2. El m´etodo de condensaci´on . . . . . . . . . . . . . . . . . . . . . . . . . . . 72

4.3. El principio de expansi´on . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76

4.4. Niveles de ineﬁcacia . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80

5. Esquemas alternativos 91

5.1. El esquema de ra´ıces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91

5.2. El esquema de coeﬁcientes ordinarios . . . . . . . . . . . . . . . . . . . . . . 94

5.3. Los supraesquemas X ′
n y R ′
n . . . . . . . . . . . . . . . . . . . . . . . . . . 99

5.4. Aplicaci´on del esquema de ra´ıces . . . . . . . . . . . . . . . . . . . . . . . . 101

5.5. Esquemas sint´eticos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107

5.6. Discriminantes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112

Bibliograf´ıa 121

´Indice alfab´etico 123

Introducci´on

En el art´ıculo de Eduardo Casas-Alvero publicado en 2001 con t´ıtulo Higher order polars

[Cas], dedicado a la relaci´on entre las singularidades de un germen de curva plana y las de

sus sucesivas curvas polares, el autor plantea, por cuestiones t´ecnicas en su investigaci´on,

un problema sobre ra´ıces compartidas por un polinomio de una variable y sus sucesivas

derivadas. A pesar de la apariencia elemental de su formulaci´on dicho problema permanece

abierto, y es bien conocido por la comunidad matem´atica como Conjetura de Casas-Alvero

como, por ejemplo, se muestra en la Feature de Jan Draisma y Johan de Jong [D-J] publi-

cada por la Newsletter de la EMS en junio de 2011. No obstante, Eduardo Casas-Alvero

ya hab´ıa difundido el problema con anterioridad a 2001 entre especialistas en ´algebra y

geometr´ıa, al haber veriﬁcado la diﬁcultad de resolverlo con las t´ecnicas disponibles. He

aqu´ı, en su versi´on m´as b´asica, el enunciado de la conjetura de Casas-Alvero.

Sea Pn(X) un polinomio m´onico de grado n con coeﬁcientes en el cuerpo C

de los n´umeros complejos. Si Pn(X) comparte una ra´ız con cada una de sus

n−1 primeras derivadas Pn
′(X), Pn
′′(X), . . . , Pn
(n-1)(X), entonces existe α ∈ C

tal que Pn(X) = (X −α)n .

En esta Memoria se presentan de forma organizada sucesivos avances sobre la conje-

tura que han ido obteni´endose en los ´ultimos a˜nos, as´ı como el desarrollo de los m´etodos

generales que permiten comprenderlos en sus aspectos conceptuales. Se ha redactado en

forma autocontenida tratando de mostrar, por una parte, hasta qu´e punto las t´ecnicas son

susceptibles de proporcionar resultados sobre la conjetura y, por otra, de descubrir c´omo y

d´onde se localizan escollos de gran diﬁcultad o de pr´actica imposibilidad de ser superados.

Si bien la formulaci´on y el an´alisis de la conjetura de Casas-Alvero es algebraico-geom´etri-

ca, el denominador com´un de los m´etodos y resultados de la Memoria se puede considerar

m´as bien propio de la teor´ıa de n´umeros.

En particular, la Memoria ofrece diversas perspectivas aritm´eticas para la conjetura, sin

excluir otras de naturaleza geom´etrica o computacional, as´ı como diferentes formulaciones

equivalentes de la misma. Entre otras, se muestra que la conjetura puede formularse en

VIII Introducci´on

t´erminos exclusivamente aritm´eticos, o que es equivalente a determinadas propagaciones o

desplazamientos de sus hip´otesis. Pero el enfoque predominante es la reducci´on de la con-

jetura a otra, m´odulo un n´umero primo que sea eﬁcaz para probarla en el nuevo escenario.

En la Memoria se utilizan hasta siete reducciones distintas, con diferentes consecuencias

pr´acticas; pero se muestra que todas ellas poseen id´entica eﬁcacia, proporcionando as´ı un

planteamiento consistente para la conjetura de Casas-Alvero en caracter´ıstica arbitraria.

Los avances y resultados que se presentan en la Memoria, y que se resumen a partir

del pr´oximo p´arrafo, han sido obtenidos por la autora a partir de 2005 en las fechas que

se precisan en esta introducci´on. Tambi´en se precisan las referencias de resultados de

otros autores que han ido apareciendo en la literatura desde entonces. En el momento de

presentar esta Memoria su contenido se puede entender como una referencia general para

todos ellos, as´ı como para determinar l´ımites de aplicaci´on de los m´etodos disponibles y

para realizar futuras investigaciones sobre la conjetura.

Con objeto de acceder a la etapa investigadora del programa de doctorado en Matem´a-

ticas en la Universidad de Valladolid (en la que imparto docencia como profesora Titular de

Escuela Universitaria desde 1989) present´e en 2005 el trabajo [Fru1] en el que proporciona-

ba una soluci´on a la conjetura de Casas-Alvero para el caso en el que el polinomio Pn(X)

dispone solo de tres monomios. Este resultado, que en la Memoria ﬁgura como corolario

2.3.4, expone ya muy claramente, en t´erminos aritm´eticos, el tama˜no de las diﬁcultades

que cabe esperar para la prueba de la conjetura en general.

Esta soluci´on comprende tres etapas sucesivas. La primera consiste en asociar a los

tres grados, i, j , n (con i < j < n) de los monomios de Pn(X), el n´umero entero dado por

∆ = (−1)
ρσ[a ρ (b − c)ρ(b − ac)σ − (−1)σ(a −1)ρ+σ(b −1)ρ]

donde a = ( n
i ), b = ( n
j ), c = ( n- i
n-j ) y ρ = n−j
d , σ = j − i
d , con d = m.c.d.
(n−j, j −i
), y en

demostrar que, para los polinomios considerados, la conjetura queda reducida a la condi-

ci´on ∆ ̸= 0. La segunda, en darse cuenta de que la conjetura para esta clase de polinomios

equivale a aﬁrmar que dicha condici´on se satisface para todas las selecciones posibles de

los valores i, j , n, es decir, a resolver un problema diof´antico concreto. La tercera, en de-

mostrar que para i, j , n dados tiene que existir necesariamente alg´un n´umero primo p con

la propiedad de que sea ∆ distinto de cero m´odulo p.

Cada etapa tiene su peculiaridad. La primera, la complejidad de la expresi´on del entero

∆. La segunda, la diﬁcultad de probar que la ecuaci´on ∆ = 0 no tiene soluciones enteras

i, j , n, con n > j > i > 0. La tercera, que la prueba de la existencia de p no necesita ser cons-

tructiva. N´otese que, de haberse encontrado una soluci´on para la ecuaci´on en la segunda

etapa, se habr´ıa tenido un contraejemplo para la conjetura, pero ello no ha podido suceder

debido a la existencia del primo p en la tercera etapa. M´as a´un, el comentario 2.3.5 pone de

IX

maniﬁesto c´omo la aﬁrmaci´on de que p existe se debe, en el fondo, a un hecho combinatorio.

Desconozco si la conjetura es cierta para polinomios con cuatro monomios. La obser-

vaci´on 5.6.9 permite recuperar la primera y la segunda etapa para este caso, por medio de

un entero δ = δ (n, {i, j, k}) cuya no anulaci´on equivale a la prueba de la conjetura y que,

como viene dado por una resultante, dispone de una expresi´on expl´ıcita en t´erminos de los

grados de los cuatro monomios. La gran complejidad de dicha expresi´on hace que probar

la no existencia de soluciones de la ecuaci´on δ = 0 se presente como un problema intratable.

La tercera etapa reduce la prueba de la conjetura a la existencia de un primo conveniente

para cada valor de los cuatro grados, pero de dicha existencia no tenemos constancia por

el momento. No est´a descartada una eventual soluci´on de esta ecuaci´on y, por tanto, un

contraejemplo a la conjetura.

Las clases de polinomios con pocos monomios (dos, tres o cuatro) dan lugar a una

estrategia recurrente a lo largo de la Memoria que nos permite delimitar, desde una pers-

pectiva aritm´etica, el conocimiento progresivo sobre la conjetura. Para solo dos monomios,

de grados i, n, la validez de la conjetura equivale, por el corolario 2.2.3, a la tautol´ogica

condici´on ∆(n, {i}) = (n
i ) − 1 ̸= 0. En general, dado el grado n y un subconjunto I de

{1, 2, . . . , n−1} se tiene un I-problema parcial de Casas-Alvero que, esencialmente, no es

otra cosa que la conjetura de Casas-Alvero para la clase de polinomios de grado n cuyos

monomios diferentes del l´ıder tienen sus grados en I.

La transformada de Tschirnhausen descrita en la secci´on 1.1 preserva las hip´otesis

y la tesis de la conjetura; puesto que, efectuada sobre un polinomio de grado n y en

las condiciones del problema, permite obviar tanto el t´ermino vicel´ıder (de grado n−1)

como el t´ermino independiente, se deduce que el J -problema de Casas-Alvero, donde

J = {1, 2, . . . , n−2}, es equivalente a la propia conjetura en grado n. Por esta raz´on, a lo

largo de la Memoria nos ce˜nimos a considerar I-problemas parciales para subconjuntos I

de J, siendo el caso particular I = J coincidente con el problema total en grado n.

Salvo en el ´ultimo cap´ıtulo, los polinomios se representan a lo largo de la Memoria

mediante expresiones a las que llamaremos de coeﬁcientes presentados , y consideraremos

derivadas netas en vez de derivadas ordinarias. Esta elecci´on ha permitido utilizar fre-

cuentemente combinatoria en lugar de c´alculo. Un polinomio m´onico presentado sobre un

cuerpo K tiene la forma

Pn(X) = Xn + ( n
1 )b1 Xn-1 + ( n
2 )b2 Xn-2 +. . . + ( n
n-i)bn-i Xi +. . . + ( n
n-1)bn-1 X + ( n
n )bn,

y su derivada neta de orden i es el polinomio presentado —tambi´en m´onico— dado por

Pn
[i](X) = Xn-i + (n-i
1 )b1 Xn-1-i + (n-i
2 )b2 Xn-2-i + . . . + (n-i
n-i)bn-i .

Entre sus propiedades ´utiles encontramos la igualdad (
Pn
[i](X)
)[j ] = Pn
[i+j ](X), y desta-

ca el hecho de que la derivada neta de orden i de un polinomio presentado de grado n

X Introducci´on

cuyos coeﬁcientes est´an dados por la (n -1)-upla (b2, . . . , bn) es exactamente el polinomio

presentado de grado n−i cuyos coeﬁcientes est´an dados por la (n - i -1)-upla (b2, . . . , bn-i).

Si la caracter´ıstica de K es cero entonces existe un ´unico polinomio con coeﬁcientes pre-

sentados para cada polinomio dado por sus coeﬁcientes ordinarios; sin embargo, si tiene

caracter´ıstica positiva no est´a garantizada ni la existencia ni la unicidad en general, como

se muestra en el comentario 3.2.4.

Dado I, si consideramos a las variables bn-i (i ∈ I) como coordenadas homog´eneas en

un espacio proyectivo pesado en el que bn-i tiene peso n−i, y denotamos por Pn(X) el

polinomio presentado de grado n cuyos monomios no l´ıderes son aquellos que tienen grado

en I y cuyos coeﬁcientes est´an dados por los respectivos bn-i, entonces el teorema de los

ceros de Hilbert homog´eneo permite formular la I-conjetura de Casas-Alvero en forma

ideal´ıstica, aﬁrmando en concreto que el radical del ideal I generado por las resultantes

H [i] de Pn(X) y Pn
[i](X), con i ∈ I, es igual al ideal generado por los bn-i, i ∈ I. Este hecho

sugiere la posibilidad de probar la I-conjetura mostrando que los bn-i pertenecen al radical

de I mediante el uso de bases de Groebner. Sin embargo, tal como se muestra en la secci´on

2.4, cuando los grados son gen´ericos tal procedimiento no es postulable ni siquiera para

el caso en que I tiene cardinal dos. En efecto, en una etapa de la aplicaci´on del algoritmo

de Buchberger el entero ∆ aparece como coeﬁciente en un monomio candidato a ser l´ıder,

siendo entonces preceptivo, para continuar aplicando el algoritmo, comprobar si dicho

entero es nulo o no; tarea esta que equivale a la propia demostraci´on de la I-conjetura. En

la referida secci´on se muestra, de hecho, que esta obstrucci´on se presenta cualquiera que

sea la forma de plantear la computaci´on.

La observaci´on anterior me permiti´o asumir en 2005 la imposibilidad de probar la

conjetura mediante el empleo de bases de Groebner cuando el grado n es arbitrario; sin

embargo, los m´etodos computacionales s´ı son aplicables cuando se ﬁjan valores peque˜nos

de n. Como ejemplo, en la subsecci´on 1.3.3 se ofrece una descripci´on expl´ıcita sencilla del

algoritmo de Buchberger que ilustra la prueba de la conjetura para n = 4, proceso que se

vuelve mucho m´as complejo para n = 5. El software que he utilizado para todos los c´alculos

que se reﬂejan en la Memoria ha sido DERIVE, empleado en ´ambitos docentes, priorizando

la comprensi´on conceptual de los m´etodos a la potencia del c´omputo.

En 2006 se public´o el trabajo de Gema D´ıaz Toca y Laureano Gonz´alez Vega [D-G], en el

que se establece la base computacional para la prueba de la conjetura para valores concretos

de n. Mostraron, en particular, la validez de la conjetura para n ≤ 7 , y evidenciaron la

complicaci´on que supone el c´alculo para valores mayores de n. A la vez, tambi´en en 2006,

se public´o el art´ıculo de Hans-Christian Graf von Bothmer, Oliver Labs, Joseph Schicho y

Christiaan van de Woestijne [BLSW] en el que se prueba la conjetura para inﬁnitos valores

de n y, como aportaci´on a´un m´as importante, se introduce la reducci´on de la conjetura

XI

m´odulo un n´umero primo p como t´ecnica para probarla.

Los autores de [BLSW] utilizan coeﬁcientes ordinarios para los polinomios y derivadas

de Hasse, omitiendo el uso de la transformaci´on de Tschirnhausen y empleando, por tanto,

una variable m´as. Considerando el polinomio Pn(X) = Xn + a1 Xn-1 + . . . + an-1 X + a0 y,

para cada i = 1, . . . , n−1, su derivada de Hasse de orden i,

Pn
< i >(X) = (n
i )Xn-i + (n-1
i ) Xn-i-1 +. . . + ( i
i )an-i,

hemos denotado por G< i > a la resultante entre Pn(X) y Pn
< i >(X). En el espacio proyectivo

pesado en el que las an-i son coordenadas homog´eneas de peso n−i, el ideal generado por

los G< i > es homog´eneo, deﬁniendo un subesquema de dicho espacio que en la Memoria

denotamos por Xn
′ y del que diremos que es un esquema de coeﬁcientes ordinarios.

Aunque un esquema est´a dado por una determinada asignaci´on funtorial de un con-

junto a cada anillo conmutativo, en esta Memoria solamente nos resulta ´util la asignaci´on

sobre los cuerpos y, m´as en concreto, sobre el cuerpo C de los n´umeros complejos y sobre

las clausuras algebraicas Fp de los cuerpos Fp, donde p es un n´umero primo. Un espa-

cio proyectivo pesado es un ejemplo de esquema, y cada ideal generado por polinomios

homog´eneos pesados en las variables consideradas deﬁne en ´el un subesquema proyectivo.

Es un resultado no trivial pero bien conocido en geometr´ıa que, si Y es un esquema

proyectivo, entonces la condici´on Y(C) = ̸O es equivalente a que sea Y( Fp ) = ̸O para alg´un

primo p y que, si este es el caso, entonces se cumple Y( Fp ) = ̸O para todos excepto para una

cantidad ﬁnita de primos p. La proposici´on 3.0.3 aporta una prueba constructiva de este

resultado en t´erminos de los anillos de enteros de los cuerpos de n´umeros, cuya teor´ıa [Sam]

es especializada pero m´as pr´actica y asequible que la de esquemas. El planteamiento de

[BLSW] aplica el mencionado resultado al esquema proyectivo Xn
′ para reducir la conjetura

a probar que se tiene Xn
′ (Fp) = ̸O para un primo p conveniente. Los autores demuestran

que en los casos n = p r y n = 2p r el primo p sirve para estos ﬁnes. Tambi´en es f´acilmente

deducible de sus resultados que lo mismo sucede si es n = 3p r y p no es 2.

Estos avances me sugirieron, en 2006, aplicar 3.0.3 al esquema proyectivo de coeﬁ-

cientes presentados Yn, deﬁnido como aquel cuyas variables pesadas son las bn-i y el ideal

est´a generado por las resultantes H [i], i ∈ J. Entre las razones que motivan el estudio

de este esquema —que se ve favorecido por la particularidad de que las derivadas netas

sean polinomios m´onicos—, destaca el inter´es en averiguar si pod´ıa darse el caso de que,

siendo Xn
′(Fp) ̸= ̸O, fuera sin embargo Yn( Fp ) = ̸O —o viceversa—, de tal modo que el

primo en cuesti´on servir´ıa para probar la conjetura por medio de uno de los esquemas aun

cuando ese mismo primo no sirviera para ello utilizando el otro. Como ya se ha apuntado

anteriormente, esto no sucede en ning´un caso; este hecho es un resultado no trivial que se

demuestra en la Memoria (teorema 5.3.1).

XII Introducci´on

Hay, adem´as, una propiedad para cuya visualizaci´on y manejo son particularmente

adecuados los esquemas de coeﬁcientes presentados, y que estimula el empleo de los es-

quemas Zn,I , an´alogos a Yn —de hecho, subesquemas del mismo— que son espec´ıﬁcos

para el an´alisis de los problemas parciales. En el estudio de estos esquemas he concentrado

la atenci´on y el trabajo hasta 2008 y, en consecuencia, la Memoria les dedica un papel

central. Dado un conjunto de exponentes I y el primo p, denotamos por Ip al subconjunto

formado por aquellos i ∈ I tales que (n
i ) es no nulo m´odulo p. La propiedad arriba aludida

constituye el enunciado del teorema 3.3.5, o de resoluci´on por elevaci´on,

Zn,Ip( Fp ) = ̸O ⇐⇒ Zn,I ( Fp ) = ̸O,

que, en particular, establece que p es eﬁcaz para probar la I-conjetura si y solo si lo es

para probar la Ip -conjetura. Este teorema remite, pues, el an´alisis de la conjetura para

casos en que el cardinal de I puede ser arbitrario a la localizaci´on de primos p tales que

el conjunto Ip resulte mucho m´as conveniente.

Su demostraci´on, que re´une varios de los ingredientes m´as empleados en la Memoria

—en particular, el hecho combinatorio 2.3.5 ya referido anteriormente—es tributaria del

teorema 3.3.1, o de resoluci´on por interpretaci´on, el cual establece la legitimidad de con-

clusiones que, siendo obvias en caracter´ıstica cero, no son en absoluto triviales en carac-

ter´ıstica p. En concreto, el teorema de resoluci´on por interpretaci´on permite deducir de

la igualdad Pn(X) = Xn, cuando se veriﬁca sobre el cuerpo Fp, la igualdad Pn
[i](X) = Xn-i

cualquiera que sea el orden i de derivaci´on, pese a todas las distorsiones que puede in-

ducir, m´odulo p, la presencia en sus t´erminos de factores enteros de la forma ( n
n-k) o ( n-i
n-k),

respectivamente. Es destacable el hecho de que su prueba sea totalmente conceptual, libre

de todo c´alculo aritm´etico.

El teorema de resoluci´on por elevaci´on supone un incentivo para tratar de investigar

bajo qu´e condiciones se veriﬁca Zn,I ( Fp ) = ̸O. Como en el caso del cuerpo C, en la Memoria

se muestra la completa resoluci´on de los casos en que I tiene cardinal 1 o 2, en las secciones

2.2 y 2.3, consistente en un cuidadoso desarrollo de los mismos m´etodos que se hab´ıan

empleado para el caso de C de modo que sean v´alidos en caracter´ıstica positiva. La revisi´on

del proceso, que arranca del c´alculo de las resultantes deﬁnidas como un determinante,

permite tambi´en valorar la diﬁcultad de abordar c´alculos similares para cardinales de I

mayores o iguales que 3.

Observemos que el teorema de resoluci´on por interpretaci´on, conjuntamente con la

proposici´on 3.1.4, permitir´ıa probar de modo inmediato que la I-conjetura de Casas-Alvero

es en ambos casos cierta —como, por otra parte, ya hab´ıan establecido los corolarios 2.2.3

y 2.3.4—, pues se tendr´ıa que Zn,I ( Fp ) = ̸O sin m´as que tomar un primo p tal que Ip sea

vac´ıo, primo cuya existencia nos consta gracias, de nuevo, a 2.3.5; sin embargo este no

XIII

es ahora nuestro objetivo: lo que queremos es caracterizar la condici´on Zn,I ( Fp ) = ̸O en

t´erminos de los datos n, I, p, para lo cual, como se ha dicho, es preciso validar sobre Fp
los c´alculos contenidos en 2.2 y 2.3, originalmente realizados en caracter´ıstica cero. Los

resultados se recogen en el teorema 3.5.1 que, concretamente, proporciona las siguientes

caracterizaciones:

Zn,{i}( Fp ) = ̸O si y solo si ( n
i ) ̸≡ 1 mod p.

Zn,{i,j }( Fp ) = ̸O si y solo si se cumplen las tres condiciones siguientes:

(i) a ̸≡ 1 mod p

(ii) b ̸≡ 1 mod p

(iii) a ρ (b − c
)ρ(b − ac
)σ − (−1)σ(a −1
)ρ+σ(b −1
)ρ ̸≡ 0 mod p,

siendo a = ( n
i ), b = ( n
j ), c = (n- i
n-j) y ρ = n-j
d , σ = j - i
d , con d = m.c.d.
(n−j, j −i
)

En la Memoria se obtienen variadas aplicaciones de estos resultados que, combinados entre

s´ı, se expresan como el ya comentado teorema 3.3.1, o como las proposiciones 3.5.3 y 3.5.5,

seg´un que el cardinal de Ip sea cero, uno o dos. Se deducen como respectivos corolarios

3.3.2, 3.5.4 y 3.5.6, nuevas pruebas de los resultados acerca de la validez de la conjetura

en los casos de n = p r, 2p r, 3p r. Tambi´en como consecuencia de 3.5.1 obtuve en 2007 el

corolario 4.2.2, que aﬁrma que la conjetura de Casas-Alvero es cierta para todos los grados

n = 4p r siempre que p sea un primo diferente de 3, 5 o 7. Este resultado, que comuniqu´e en

[Fru2], fue redescubierto en 2011 por Jan Draisma y Johan de Jong como resultado central

de su trabajo [D-J].

Para acceder a la prueba de 4.2.2 ha sido fundamental establecer previamente el teo-

rema 4.1.4, o de eliminaci´on del t´ermino vicel´ıder, seg´un el cual, para todo primo p se

veriﬁca Yn
′( Fp ) = ̸O ⇐⇒ Yn( Fp ) = ̸O,

siendo Yn
′ el esquema de coeﬁcientes presentados en el cual no se ha descartado la presencia

del coeﬁciente b1. La demostraci´on de este resultado concerniente a los cuerpos Fp ilustra,

en particular, que la transformada de Tschirnhausen puede aplicarse en caracter´ıstica

positiva siempre que se consideren polinomios presentados.

La diﬁcultad de probar el resultado 4.1.4 no es conceptual, sino que proviene de la

necesidad de demostrar espec´ıﬁcamente para las expresiones de coeﬁcientes presentados

algunas propiedades que para las expresiones con coeﬁcientes ordinarios son est´andar; es

el caso, por ejemplo, de la regla de la cadena para la derivada neta que se prueba en 4.1.3.

El teorema de eliminaci´on del vicel´ıder permite, junto con el de resoluci´on por elevaci´on

y ciertos c´alculos realizados con n´umeros combinatorios, demostrar el teorema 4.2.1, o de

XIV Introducci´on

resoluci´on por condensaci´on. Este teorema establece la equivalencia

Yhpr ( Fp ) = ̸O ⇐⇒ Yh( Fp ) = ̸O,

aportando la consecuencia de que, si un primo p es eﬁcaz para probar la conjetura de

cierto grado h, entonces ese mismo primo es tambi´en eﬁcaz para probarla en todo grado

de la forma n = hp r. El resultado an´alogo referente al esquema Xn
′ se halla en [BLSW];

v´ease tambi´en, en concreto, la contribuci´on de Woestijne [Woe] realizada en 2010.

Otra notable aplicaci´on de 3.3.1 y 3.5.1 es el teorema 3.6.2, el cual aﬁrma que, para

I = {2, 3, . . . , n−2}, la I-conjetura de Casas-Alvero es cierta en todo grado de la forma

n = p r + 1 o bien n = 2p r + 1, donde p es un n´umero primo. En efecto, utilizando las propie-

dades del tri´angulo de Tartaglia que se desarrollan en la secci´on 3.4 se muestra que Ip es

vac´ıo si es n = p r + 1, e Ip tiene cardinal 2 y adem´as se satisfacen las condiciones de 3.5.5,

si es n = 2p r + 1. El teorema 3.6.2 ha sido redescubierto en 2012 por Wouter Castryck en

el caso n = p + 1 y por Robert Lauterveer y Miryam Ouna¨ıes [L-O] en el caso n = p r + 1, al

estudiar las restricciones para hipot´eticos contraejemplos a la conjetura en estos grados.

Merece ser se˜nalado que estos autores tambi´en han descubierto en [L-O] y [CLO-1] otra

importante restricci´on, ya que han mostrado con nuestra terminolog´ıa que, siendo n = p + 1,

si existiese un contraejemplo en Yn(C) entonces no solo tendr´ıa que veriﬁcarse para ´el que

bn-1 fuese distinto de cero, sino que se veriﬁcar´ıa tambi´en bn-i = bn-j = 0 para al menos dos

´ındices i, j con 0 < i < j < n−1 que adem´as satisfacen una igualdad aritm´etica adicional.

Conviene mencionar que la prueba de este ´ultimo resultado, ajeno a la Memoria, es posible

porque sit´ua al contraemplo en el escenario de la prueba de 3.0.3 y utiliza argumentos

propios de teor´ıa de n´umeros.

Este descubrimiento, complementario de 2.2.3 y 2.3.4, aporta otro aliciente adicional

para investigar los esquemas de coeﬁcientes presentados. Entre otras aplicaciones, ha per-

mitido a los autores de [CLO-1] simpliﬁcar la computaci´on de la validez de la conjetura,

que han logrado contrastar con ´exito para n = 12 mediante la ejecuci´on de algoritmos

programados en Magma y varias semanas de c´omputo.

La validez del teorema 3.6.2 me permiti´o en 2009 y 2010 encontrar varios enunciados

equivalentes a la conjetura de Casas-Alvero, cuya caracter´ıstica principal es que se formu-

lan en t´erminos exclusivamente de la hip´otesis de la misma, sin menci´on expl´ıcita alguna

a su tesis. Se trata de las conjeturas de propagaci´on y desplazamiento de hip´otesis formu-

ladas en las subsecciones 3.6.1 y 3.6.2, y establecidas como equivalentes a la conjetura de

Casas-Alvero en los teoremas 3.6.4 y 3.6.6 respectivamente. La de propagaci´on aﬁrma que

si el polinomio Pn(X) veriﬁca la hip´otesis de Casas-Alvero (i.e., comparte una ra´ız con

cada derivada de grado positivo) entonces igualmente veriﬁca tal hip´otesis el polinomio
(Pn(X)
)d para alg´un entero d > 1 que satisfaga nd = p r + 1 o bien nd = 2p r + 1. En su de-

XV

mostraci´on se invoca al cl´asico teorema de Dirichlet [Ser], para garantizar la existencia de

enteros d > 1 con esta propiedad. La de desplazamiento, por su parte, aﬁrma que si Pn(X)

cumple la hip´otesis de Casas-Alvero, entonces tambi´en la cumple X e · Pn(X) para alg´un

entero e > 0 tal que para n + e la conjetura de Casas-Alvero ya haya sido probada, o bien

que sea n + e = p r + 1 o n + e = 2p r + 1, entero cuya existencia es, en esta ocasi´on, obvia.

Es f´acil veriﬁcar que, salvo unas pocas excepciones, para los primeros cientos de valores

de n los enteros d y e toman valores peque˜nos, especialmente en el caso de e. El corolario

3.6.9 necesita solo del valor e = 1 para mostrar que la aﬁrmaci´on de que la conjetura de

Casas-Alvero es verdadera en todo grado n es equivalente a la aﬁrmaci´on de que siempre

que un polinomio P(X) satisfaga la hip´otesis de Casas-Alvero, tambi´en X · P(X) satisface

dicha hip´otesis. Obs´ervese que el enunciado de esta aﬁrmaci´on es transversal al grado.

Varias veces en esta introducci´on hemos caliﬁcado a un n´umero primo de eﬁcaz para

referirnos a la cualidad que permite emplearlo para probar la validez de la conjetura en

una determinada situaci´on. Ello no es casual, ya que la noci´on de primo eﬁcaz se introduce

t´ecnicamente en la Memoria como una noci´on relativa a un esquema proyectivo Y dado;

en concreto, p es eﬁcaz para Y si se cumple Y (Fp) = ̸O, lo cual, en virtud de 3.0.3, implica

(y en eso consiste su eﬁcacia) que tambi´en se cumple Y (C) = ̸O. En la Memoria se estudian

—de hecho, para cada grado n— siete esquemas proyectivos diferentes, con cada uno de los

cuales la conjetura de Casas-Alvero se expresa mediante la condici´on Y(C) = ̸O; as´ı pues,

ﬁjado un grado, cada uno de ellos dispone de sus primos eﬁcaces si y solo si la conjetura

es cierta para ese grado.

Tres de estos esquemas, los de coeﬁcientes presentados Yn e Yn
′ y el de coeﬁcientes

ordinarios Xn
′ , han sido ya comentados. En el caso de coeﬁcientes ordinarios, omitiendo la

variable a1 se obtiene un subesquema de Xn
′ al que denotaremos por Xn. Por otro lado,

una tercera v´ıa para expresar un polinomio es la que lo hace en t´erminos de sus ra´ıces,

esto es, en la forma
 Pn(X) = ( X − x1) · ( X − x2) · · · · · ( X − xn).

A diferencia de los coeﬁcientes an-i o bn-i, las ra´ıces x1, x2,. . . , xn ocupan posiciones

intercambiables; en la secci´on 5.1 esta simetr´ıa inicial se invierte parcialmente en reducir

los hipot´eticos contraejemplos a una forma preﬁjada que facilita su b´usqueda. La trans-

formaci´on de Tschirnhausen, junto a la condici´on de compartir una ra´ız con Pn
< n-i >(X),

proporciona las restricciones (1) : x1 + x2 + · · · + xn = 0 ; x1 = 0. Asimismo, la condici´on

de compartir una ra´ız con Pn
< 1 >(X) toma la forma (2) : x2 (x2 −x3) = 0. Finalmente, el

resto de condiciones se expresan mediante (3) : K < 2 > = K < 3 > = · · · = K < n-2 > = 0, siendo

K < i > la resultante G< i > reescrita en t´erminos de sus ra´ıces.

El conjunto de condiciones (1), (2), (3), que considerando el peso usual est´an dadas por

polinomios homog´eneos en las variables x1, . . . , xn, deﬁnen el esquema proyectivo Rn en el

XVI Introducci´on

espacio que tiene a estas variables como coordenadas. Si la restricci´on x1 + x2 +· · ·+ xn = 0

se sustituye por la —m´as d´ebil— K <n-1 > = 0, se obtiene el esquema Rn
′ . Diremos que

estos esquemas son esquemas de ra´ıces.

Finalmente, si utilizando la expresi´on con coeﬁcientes ordinarios para un I-polinomio

con I = {k1, . . . , kr} se habilita la variable sl para denotar una ra´ız compartida por Pn(X)

y Pn
< kl >(X), (l = 1, . . . , r), se muestra en la secci´on 5.5 c´omo obtener las r condiciones

polin´omicas homog´eneas Ml(s1, . . . , sr) = 0 que expresan las compatibilidades que las hi-

p´otesis de la conjetura imponen a la totalidad de ra´ıces compartidas. El esquema proyectivo

que deﬁnen los polinomios Ml en el espacio en el que las si son coordenadas se denota

en la Memoria por Sn,I , y diremos de ´el que es un esquema sint´etico. Naturalmente, el

esquema Sn,J —donde J = {1, . . . , n−2}— se aplica al problema total en grado n.

En 2011 he probado uno de los resultados principales de la Memoria. Se trata del

teorema 5.3.1 que, junto al teorema 5.5.2 permiten concluir como corolario que todo primo

p que sea eﬁcaz para uno cualquiera de los siete esquemas Yn, Xn, Rn, Sn,J , Yn
′ , Xn
′, Rn
′ ,

es tambi´en eﬁcaz para cada uno de los restantes. La demostraci´on no es trivial; de hecho,

su diﬁcultad reside en la equivalencia

Xn( Fp ) = ̸O ⇐⇒ Yn( Fp ) = ̸O,

que es el objeto del teorema 5.2.2, junto al teorema de eliminaci´on del vicel´ıder, que

proporciona la equivalencia an´aloga entre Yn e Yn
′. Tal equivalencia no era previsible,

particularmente, entre los esquemas Xn y Xn
′, dado que en caracter´ıstica positiva no

siempre es posible aplicar la transformada de Tschirnhausen a los polinomios expresados

por sus coeﬁcientes ordinarios. N´otese que ha sido demostrada de manera indirecta, gracias

al puente que los mencionados teoremas (5.2.2, junto con un an´alogo para la versi´on prima

de los esquemas, como pilares; 4.1.4, a modo de tablero) tienden entre ambos esquemas.

La noci´on de polinomio presentado se maniﬁesta, de nuevo, como un instrumento valioso

en caracter´ıstica positiva.

El fallido intento de localizar primos que, no siendo eﬁcaces para Xn
′, lo fueran para

alg´un otro esquema ligado a la conjetura, proporciona, gracias al inesperado resultado

de que los siete esquemas estudiados tengan los mismos primos ineﬁcaces, una notable

consecuencia que cabe atribuir a esta Memoria. En efecto, cada uno de los esquemas

plantea sobre Fp un problema de Casas-Alvero en principio diferente; pero el hecho de

que, ﬁjado un grado n, la soluci´on a estos siete problemas sea la misma (s´ı o no, pero

igual para todos ellos, seg´un que el primo p sea o no eﬁcaz para probar la conjetura

de Casas-Alvero original en grado n) permite aﬁrmar que la conjetura de Casas-Alvero

est´a bien deﬁnida en caracter´ıstica positiva y puede formularse a trav´es de cualquiera de

los esquemas considerados. Y ello, pese a que no son esquemas isomorfos entre s´ı.
 XVII

Todos los primos eﬁcaces con n que, hasta el momento, han servido en la pr´actica para

demostrar la conjetura de Casas-Alvero en grado n han sido menores o iguales que n. El

corolario 4.3.2 muestra que solo puede existir un primo que, siendo menor o igual que n,

sea eﬁcaz con ´el, y que, si existe, entonces coincide necesariamente con el primo dominante

de n, esto es, un primo presente en la factorizaci´on de n que supere al producto de las

potencias de los otros primos; cabe se˜nalar que el primo dominante de n no siempre existe,

y que cuando existe no siempre es eﬁcaz. Procede, en ese caso, centrarse en la b´usqueda

de primos eﬁcaces mayores que n. Seg´un el principio de expansi´on enunciado en la secci´on

4.3, el hallazgo de un primo que sea eﬁcaz para n permite decidir que la conjetura es cierta

para los grados de la forma np r.

Para la localizaci´on de primos eﬁcaces se puede utilizar, naturalmente, cualquiera de los

siete esquemas proyectivos anteriormente descritos. Resultados ya comentados muestran

los primos ineﬁcaces para los grados n = 3 y n = 4. En 2009 desarroll´e el contenido completo

de las secciones 4.4 y 5.4 en la forma en que aparecen en la Memoria, y lo comuniqu´e en

[Fru2]; en particular, encontr´e los nueve primos ineﬁcaces con n = 5 de dos maneras —una,

probando 4.4.3 a trav´es del esquema Y5; otra, en 5.4.[n = 5] mediante R5—, as´ı como los

cincuenta y tres primos ineﬁcaces con n = 6, probando 5.4.1. Dichos n´umeros han sido

redescubiertos a trav´es de variantes de los esquemas X5
′ y X6
′ por Castryck, Lauterveer

y Ouna¨ıes [CLO-2] en 2012, y los de n = 5 alternativamente por Chellali y Salinier [C-S].

En [CLO-2] est´a disponible adem´as la lista de los seiscientos sesenta y un primos que son

ineﬁcaces para n = 7, un c´alculo que te´oricamente es posible tambi´en a partir de R7 por el

procedimiento descrito en 5.4.[n = 7] pero que no he completado porque el c´omputo excede

la capacidad del programa DERIVE.

En la secci´on 5.4 los c´alculos dejan claro que el esquema Rn es muy adecuado para

calcular los primos eﬁcaces para valores peque˜nos de n. En efecto, como el lector observar´a,

los c´alculos en 5.4 son, para n = 3, n = 4, extremadamente elementales, mientras que para

n = 5, 6, 7 son susceptibles de ser abordados computacionalmente con m´ınimas casu´ısticas.

En el ejemplo previo al ﬁnal de la Memoria se muestra que Sn,J tambi´en resulta ser un

esquema muy adecuado para este tipo de c´alculos. De hecho, un c´alculo en tres etapas

elementales permite calcular el entero D5, cuyos divisores primos son exactamente los

nueve ineﬁcaces para n = 5.

Los c´alculos de 4.4 disponen de una ventaja adicional sobre los de 5.4, y es que permiten

clasiﬁcar a los primos por niveles de ineﬁcacia respecto de un n ﬁjado, entendiendo que el

nivel cero lo ocupan los primos eﬁcaces, el nivel uno aquellos que son ineﬁcaces para una

I-conjetura en grado n con cardinal de I igual a 1 y, en general, son de nivel k aquellos

que son ineﬁcaces para una I-conjetura en grado n con cardinal de I igual a k pero que no

est´an en los niveles de ineﬁcacia previos. Para n = 4, 5 y 6, los primos ineﬁcaces aparecen

XVIII Introducci´on

clasiﬁcados por niveles en la Memoria debido a los resultados obtenidos en 4.4. En general,

los primos en los niveles de ineﬁcacia 1 y 2 son calculables usando solo aritm´etica, a trav´es

de 3.5.3 y 3.5.5 respectivamente; en la Memoria se ofrece una tabla de dichos niveles hasta

n = 12, que permite observar c´omo el volumen y el tama˜no de los primos que contienen

van aumentando a ritmo creciente cuando lo hace el valor de n.

Las observaciones 5.2.3 y 5.5.3 muestran que, igual que suced´ıa en el caso total, los

diversos esquemas parciales que tienen sentido para una I-conjetura parcial —Zn,I , Xn,I ,

Sn,I — poseen exactamente los mismos primos eﬁcaces; se desprende de ello que, no solo

el conjunto de los primos ineﬁcaces con n, sino su distribuci´on por los distintos niveles de

ineﬁcacia, es independiente del esquema parcial que se considere.

El desarrollo de los esquemas sint´eticos en la secci´on 5.5 ha permitido descubrir un

m´etodo aritm´etico similar para determinar computacionalmente, en la pr´actica, los primos

en el nivel de ineﬁcacia 3. Si se considera un I-problema parcial con cardinal de I mayor

que 2, e i < j son los dos enteros m´as peque˜nos de I, y si consideramos el abierto af´ın de

contraejemplos a la I-conjetura con an-i diferente de cero, entonces la proposici´on 5.5.4

muestra que la inexistencia de tales contraejemplos es equivalente a que el sistema de

ecuaciones algebraicas con q = card(I) −2 inc´ognitas s1, . . . , sq y q + 1 ecuaciones dado en

(5.21) no posea soluci´on, siendo esta equivalencia v´alida tanto sobre el cuerpo C como

sobre los cuerpos Fp.

La intersecci´on del ideal principal generado por los q + 1 polinomios que deﬁnen dichas

ecuaciones con el anillo Z es un ideal principal cuyo generador ∆(n, I ), bien deﬁnido salvo

el signo, lo denominamos en la Memoria discriminante para la I-conjetura en grado n.

El teorema 5.6.2 muestra que la inexistencia de los mencionados contraejemplos tambi´en

equivale a la no anulaci´on de ∆(n, I ). Para I = {i}, se deﬁne ∆(n, I ) = a −1, donde a = ( n
i ),

por convenio. En el caso I = {i, j} el teorema 5.6.8 proporciona la igualdad

∆(n, I ) = (a −1)i (e −1)n-j ∆d, donde e = ( j
i ), d = m.c.d.
(n−j, j −i
)

de modo que el discriminante diﬁere del entero ∆ en un factor consecuente con la sin-

gularizaci´on de los enteros i < j dentro de I que han permitido obtener las ecuaciones

(5.21).

El discriminante puede verse, a todos los efectos, como una generalizaci´on del entero

∆ ligado al {i, j}-problema para los I-problemas con cardinal de I mayor que 2. Si ahora

tomamos I de cardinal 3 se tiene q = 1 y, por tanto, una sola variable y dos ecuaciones en

(5.21), siendo la resultante entre ambas un nuevo valor δ (n, I ) cuya no anulaci´on equivale a

la del discriminante ∆(n, I ) y a la inexistencia de soluciones para (5.21). Salvo que p divida

al entero µ igual al m´aximo com´un divisor de los coeﬁcientes l´ıder de ambas ecuaciones,

la no anulaci´on m´odulo p de la resultante δ (n, I ) caracteriza asimismo la inexistencia de

XIX

soluci´on sobre Fp del mismo sistema (5.21). M´as a´un, con la ´unica posible excepci´on de

los primos que dividen a µ, los divisores primos de ∆(n, I ) y de δ (n, I ) son los mismos,

seg´un 5.6.11, siendo δ (n, I ) un entero —posiblemente enorme— dado expl´ıcitamente por

la f´ormula de la resultante, que es una f´ormula aritm´etica en los datos (n, I).

Como aplicaciones, y entre otras, se tiene que el problema de Casas-Alvero con cuatro

monomios se puede enfocar con las tres etapas comentadas al inicio de la introducci´on;

que la resoluci´on por elevaci´on dispone de un m´etodo aritm´etico viable para la I-conjetura

cuando Ip tiene cardinal 3 y que, para valores peque˜nos del grado, los primos en el nivel

3 de ineﬁciencia son calculables.

La Memoria concluye mostrando que, para todo valor de n, la conjetura de Casas-

Alvero de grado n admite formulaciones aritm´eticas, al enunciarla como la imposibilidad

de determinada igualdad num´erica. Con este ﬁn, se deﬁne el superdiscriminante para el

grado n como el entero dado por

Dn =
 n−2∏

i=1 ∆(n, Ii), donde Ii = {i, i + 1, . . . , n−2}, 0 < i < n −1,

y, como alternativa, el superdiscriminante din´amico como

̃Dn = ∏

i∈A ∆(n, Ii), siendo A = {i ∈ {1, . . . , n −2}∣
∣ a´un se ignora si ∆(n, Ii) es nulo o no
}

—as´ı por ejemplo, ̃Dn = D(n, I1) si es n = p r + 1 o 2p r + 1, en caso de que la conjetura no

se haya probado previamente para el valor n en cuesti´on—. Por construcci´on, el superdis-

criminante permite resumir la conjetura de Casas-Alvero en grado n en que se veriﬁque

Dn ̸= 0; no-igualdad que, din´amicamente, puede traducirse en su equivalente m´as simple,
̃Dn ̸= 0. Los enteros Dn y ̃Dn no tienen, sin embargo, el mismo alcance: como muestra el

teorema 5.6.13, disponer de primo p que no divida a ̃Dn equivale a saber que la conjetura

de Casas-Alvero es cierta en grado n, pero disponer de un primo p que no divida a Dn
garantiza que p es un primo eﬁcaz para n y por tanto demuestra que la conjetura de

Casas-Alvero es cierta para todos los grados de la forma np r.

Se concluye del p´arrafo anterior que todos los primos ineﬁcaces con n se encuentran

en la factorizaci´on de Dn. Para n = 3, 4, 5, el conjunto de divisores primos de Dn coincide

exactamente con el de los primos ineﬁcaces con n; no est´a sin embargo descartado que, en

otros grados, pueda darse una contenci´on estricta.

Cap´ıtulo 1

El enunciado del problema

El Problema de Casas-Alvero consiste en averiguar si la llamada Conjetura de Casas-Alvero

es cierta o no.

Conjetura de Casas-Alvero. Sea Pn(X) un polinomio m´onico de grado n con coeﬁ-

cientes en el cuerpo C de los n´umeros complejos. Si Pn(X) comparte una ra´ız con cada

una de sus n−1 primeras derivadas Pn
′(X), Pn
′′(X), . . . , Pn
(n-1)(X) —esto es, si para cada

i = 1, . . . , n −1, existe αi ∈ C tal que Pn(αi) = P (i)
n (αi) = 0— entonces existe α ∈ C tal

que Pn(X) = (X −α)n .

Conviene remarcar que la hip´otesis de este enunciado se compone exactamente de n−1

aﬁrmaciones independientes acerca de Pn(X) en cada una de las cuales aparece involucrada

una sola de sus sucesivas derivadas; ninguna relaci´on se conoce a priori entre dos derivadas

de diferente orden.

En cuanto a las ra´ıces α1, α2, . . . , αn−1 que Pn(X) comparte respectivamente con su

derivada primera, segunda, etc, en ning´un momento se dice que hayan de ser distintas

(situaci´on que por otro lado, de poder darse, ser´ıa incompatible con la tesis del enunciado).

Tampoco se presupone que todas ellas sean iguales: bajo esa suposici´on el enunciado ser´ıa

una completa obviedad, pues se estar´ıa diciendo que Pn(X) posee una ra´ız de multiplicidad

n que entonces, por cuesti´on de grados, habr´a de ser ´unica. As´ı pues, en el enunciado de la

conjetura las hip´otesis establecen la mera existencia de los n −1 n´umeros αi sin ocuparse

de si puede haber o no coincidencias entre ellos, mientras que la tesis equivale a que esos

n −1 n´umeros sean iguales. Se concluye entonces que la conjetura puede reescribirse en la

siguiente forma:

Conjetura de Casas-Alvero. Sea Pn(X) un polinomio m´onico de grado n con coeﬁ-

cientes complejos. Si para cada i = 1, . . . , n−1 existe αi ∈ C tal que Pn(αi) = P (i)
n (αi) = 0

entonces α1 = α2 = . . . = αn−1 .

2 Cap´ıtulo 1. El enunciado del problema

En la formulaci´on de la conjetura de Casas-Alvero, la condici´on de ser m´onico Pn(X)

puede suprimirse sin m´as peaje que sustituir, en la tesis del enunciado, el que sea Pn(X) =

(X−α)n por que sea Pn(X) = (λX−µ)n para ciertos λ, µ ∈ C, ya que C es algebraicamente

cerrado. Al reescribir la conjetura en t´erminos de las αi no hay ya ninguna distinci´on entre

el caso m´onico y el general, luego es innecesario considerar este aspecto.

1.1. Preparaci´on de Tschirnhausen

Tratando de normalizar de un modo conveniente este problema, se va a ﬁjar el valor de

la ra´ız αn−1 que Pn(X) comparte con Pn
(n-1)(X) haciendo que sea igual a 0. Veremos que

esta condici´on sobre el polinomio no supondr´a p´erdida de generalidad en la conjetura de

Casas-Alvero.

Observaci´on 1.1.1. Pn
(n-1)(X) tiene a 0 como ´unica ra´ız si y solo si el polinomio Pn(X)

carece de t´ermino de grado n−1 (t´ermino vicel´ıder ).

En efecto, si Pn(X) = Xn + a1 Xn-1 + · · · + an, entonces su derivada (n−1)-´esima es

Pn
(n-1)(X) = n! X + (n−1)! a1, cuya ra´ız, α = − a1
n , es nula si y solo si es a1 = 0.

Proposici´on 1.1.2. La conjetura de Casas-Alvero es verdadera si y solo si es verdadera

cuando se reﬁere exclusivamente a los polinomios que tienen nulo el coeﬁciente del t´ermino

vicel´ıder.

Demostraci´on. En el caso de ser a1 ̸= 0, se puede hacer en Pn(X) el cambio de variable

X = Y − a1
n , obteniendo:

Pn(X) = Y n + [−
( n
1
 ) a1
n + a1(n-1
0
 )] Y n−1 + (t´erminos de menor grado) = Q(Y )

El paso de Pn(X) a Q(Y ) se conoce como transformaci´on de Tschirnhausen; observemos

que provoca la cancelaci´on del t´ermino vicel´ıder en Q(Y ). Supongamos ahora que Pn(X)

satisface las hip´otesis de Casas-Alvero, de modo que para cada i = 1, . . . , n−1 se tiene:

Pn(αi) = P (i)
n (αi) = 0 para cierto αi ∈ C. Tomando, para cada i, βi = αi + a1
n , se tendr´a:

Q(βi) = Pn(βi − a1
n ) = Pn(αi) = 0

y adem´as, seg´un la regla de la cadena, se cumplir´a

Q
(i)(βi) = Pn
(i)(βi − a1
n ) = Pn
(i)(αi) = 0.

1.2 Presentaci´on bin´omica del polinomio. La derivada neta 3

Si nos constara que la conjetura de Casas-Alvero es verdadera cuando se reﬁere a poli-

nomios sin t´ermino vicel´ıder, entonces podr´ıamos aplic´arsela a Q(Y ), ya que cumple todos

los requisitos, obteniendo

Q(Y ) = (Y −β)n y, en consecuencia, Pn(X) = Q(Y ) = [ X−
(β− a1
n )]n.

Hemos demostrado que, de ser verdadera esta versi´on d´ebil de la conjetura, lo ser´ıa tambi´en

la versi´on ordinaria. El rec´ıproco es obvio. □

En lo sucesivo, pues, Pn(X) = Xn + ∑n
i=1 ai Xn-i ser´a un polinomio carente de t´ermi-

no vicel´ıder (esto es, con a1 = 0) y que cumple las hip´otesis de Casas-Alvero. Seg´un la

observaci´on 1.1.1, Pn
(n-1)(X) posee a 0 como ´unica ra´ız; decir que la comparte con Pn(X)

signiﬁca que Pn(0) = 0, o lo que es lo mismo, que an = 0. Y, en estas condiciones, un valor

de α para el cual sea Pn(X) = (X −α)n no puede ser otro que α = 0. Todo ello, junto

con la proposici´on 1.1.2, permite reescribir la conjetura de Casas-Alvero de la siguiente

manera:

Conjetura de Casas-Alvero. Sea Pn(X) = Xn + a2 Xn-2 + · · · + an-1X ∈ C[X]. Si

Pn(X) comparte una ra´ız con cada uno de los polinomios Pn
′(X), Pn
′′(X), . . . , Pn
(n-2)(X),

entonces Pn(X) = Xn.

Como podemos apreciar, ﬁjar αn-1 = 0 nos libra de las indeterminadas a1 y an, y nos

ahorra un ´ıtem en el listado de hip´otesis — el referente a Pn
(n-1)(X), que ya ha rendido

su servicio—; adem´as, da una forma mucho m´as manejable a la tesis de la conjetura, que

deja de ser existencial y queda reducida a la veriﬁcaci´on de una igualdad.

1.2. Presentaci´on bin´omica del polinomio. La derivada neta

Poniendo ak = ( n
k ) bk, el polinomio m´onico de grado n y coeﬁcientes complejos gen´erico,

P (X), adopta la forma

P (X) = Xn + ( n
1 )b1 Xn-1 + ( n
2 )b2 Xn-2 +. . . + ( n
n-i)bn-i Xi +. . . + ( n
n-1)bn-1 X + ( n
n )bn

a la que denominaremos presentaci´on bin´omica del polinomio en alusi´on a los coeﬁcientes

bin´omicos ( n
k ) que ﬁguran expl´ıcitamente en ella.

Cuando se deriva un polinomio se incorpora un nuevo factor a cada uno de sus t´erminos,

pero no se trata de un factor com´un. Empleando la presentaci´on bin´omica, la elemental

igualdad ( n
k
 ) · (n−k) = n · (n−1
k
 )

4 Cap´ıtulo 1. El enunciado del problema

permitir´a captar un factor n en cada uno de los t´erminos de P ′(X), pues se tiene:
[
 Xn + n∑

k=1
 ( n
k )bk Xn-k]′ = n Xn-1 + n-1∑

k=1 n (n-1
k ) bk Xn-k-1
.

Deﬁnici´on 1.2.1. Llamaremos derivada neta del polinomio P (X) = Xn + n∑

k=1
 ( n
k )bk Xn-k

al polinomio
 P [1](X) := 1
n · P ′(X) = Xn−1 + n-1∑

k=1
 (n-1
k ) bk X n-k-1,

e iterando (puesto que P [1](X) est´a dado en la presentaci´on bin´omica adecuada a su grado,

y podemos proceder con ´el del mismo modo) se deﬁne la derivada neta de orden i como

el polinomio:

P [i](X) := 1
n(n−1) · · · (n−i + 1) · P (i)(X) = Xn-i + n-i∑

k=1
 (n-i
k ) bk Xn-k-i.

Es decir, hallar la derivada neta de orden i de un polinomio presentado en forma bin´omica

consiste simplemente en rebajar en i unidades tanto el grado de cada t´ermino como el

n´umero superior de cada coeﬁciente bin´omico.

Cada polinomio Pn
[i](X) presenta obviamente las mismas ra´ıces sobre los complejos que

P (i)(X), pero est´a descargado de factores engorrosos y tiene una expresi´on sencilla que es

esencialmente la misma para cualquier i y que se ajusta al mismo patr´on que el polinomio

de partida P (X). Adem´as, conserva la monicidad de este. Por todas estas razones (a las

que debe el nombre que ha recibido), la derivada neta ser´a una herramienta apta y muy

conveniente para el tratamiento del problema de Casas-Alvero.

No deben confundirse las derivadas netas con las derivadas de Hasse, bien conocidas

y de frecuente uso en la literatura, que se deﬁnen como sigue: Dado P (X) = Xn +
∑n
k=1 ak Xn-k, se denomina derivada de Hasse de P (X) de orden i al polinomio

P <i>(X) := 1
i ! · P (i)(X) = ( n
i ) Xn−i + n-i∑

k=1
 (n-k
i ) ak Xn-k-i.

Es clara la relaci´on: P <i>(X) = ( n
i ) P [i](X).

Las derivadas netas constituyen una alternativa a las derivadas de Hasse, respecto de

las cuales presentan algunos rasgos diferenciales interesantes. Obs´ervese por ejemplo que

P [i](X) es m´onico, no as´ı P <i>(X). Adem´as, contrariamente a la de Hasse, la derivada

neta de orden i s´ı es el resultado de aplicar i veces consecutivas la derivaci´on neta de

orden 1, ya que la forma de realizar esta es intr´ınseca al polinomio sobre el que act´ua

(depende solo de su grado, y no del dato circunstancial del orden de derivaci´on en que se

1.3 Formulaci´on mediante resultantes 5

halla). Como consecuencia de ello, la derivaci´on neta s´ı satisface la propiedad, ordinaria

en la derivaci´on usual pero que falta en la de Hasse, de ser

(P [i](X)
)[j ] = P [i+j ](X), ∀i, j ∈ N.

Para ﬁnalizar la secci´on veremos c´omo se enuncia la conjetura de Casas-Alvero cuando

se emplea la presentaci´on bin´omica para el polinomio Pn(X), al que se supone ya sin

t´ermino vicel´ıder, y se habla de las derivadas netas en lugar de las ordinarias (lo cual no

altera el signiﬁcado de las hip´otesis dado que las ra´ıces son las mismas en uno y otro caso).

Conjetura de Casas-Alvero. Se considera el polinomio de coeﬁcientes complejos

Pn(X) = Xn + ( n
2 )b2 Xn-2 + · · · + ( n
n-i)bn-i Xi + · · · + ( n
n-2)bn-2 X2 + ( n
n-1)bn-1 X .

Si Pn(X) comparte una ra´ız con cada uno de los polinomios

Pn
[1](X) = Xn-1 + (n-1
2 )b2 Xn-3 + · · · + (n-1
n-i )bn-i Xi-1 + · · · + (n-1
n-2)bn-2 X + (n-1
n-1)bn-1,

Pn
[2](X) = Xn-2 + (n-2
2 )b2 Xn-4 + · · · + (n-2
n-i )bn-i Xi-2 + · · · + (n-2
n-2)bn-2,
...
Pn
[i](X) = Xn-i + (n-i
2 )b2 Xn-2-i + · · · + (n-i
n-i)bn-i,
...

Pn
[n-2](X)= X2 + ( 2
2 )b2,

entonces Pn(X) = Xn, esto es: b2 = b3 = . . . = bn-1 = 0.

N´otese que, como ya se ha indicado, los polinomios Pn
[i](X) no son otra cosa que los

correspondientes polinomios de grado n−i presentados en forma bin´omica; es decir, se tiene

Pn
[i](X) = Pn-i(X);

en el enunciado anterior, por tanto, se puede sustituir Pn
[i](X) por Pn-i(X) cuando resulte

conveniente.

1.3. Formulaci´on mediante resultantes

Dados dos polinomios P (X) = ∑n
i=0 ai Xn-i, Q(X) = ∑m
i=0 bi Xm-i con coeﬁcientes en un

cuerpo K, la resultante de P (X) y Q(X), que se denota Res(P , Q
), es el valor del deter-

6 Cap´ıtulo 1. El enunciado del problema

minante a0 a1 . . . . . . an
a0 a1 . . . . . . an
. . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . .
a0 a1 . . . . . . an
b0 b1 . . . . . . . . . . . . bm
b0 b1 . . . . . . . . . . . . bm
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
b0 b1 . . . . . . . . . . . . bm
 



 m




 n
 (1.1)

(los espacios en blanco se suponen ocupados por ceros).

En caso de ser a0 = b0 = 0, esto es, si ambos polinomios poseen grados estrictamente

inferiores a los que formalmente se les ha supuesto en la construcci´on descrita, la resultante

ser´a nula pues la primera columna del determinante no contendr´a m´as que ceros.

Si es solamente uno de los polinomios el que est´a en ese supuesto (por ejemplo, si

b0 = 0 pero a0 ̸= 0) entonces el desarrollo del determinante por su primera columna, iterado

tantas veces como sea la diferencia m−r entre el grado m atribuido a Q(X) y su verdadero

grado r, conduce a un resultado id´entico, salvo por la aparici´on del factor no nulo a0
m−r,

al que se hubiera obtenido con una atribuci´on correcta de grado a Q(X).

Y, para el caso en que es a0 · b0 ̸= 0, es bien conocido lo siguiente: La b´usqueda de

polinomios A(X) y B(X) tales que

gr(A(X)
) < m, gr(B(X)
) < n, y se cumpla: A(X) · P (X) − B(X) · Q(X) = 0

produce un sistema de ecuaciones lineales con n + m ecuaciones y n + m inc´ognitas (los

coeﬁcientes de los polinomios buscados) que es homog´eneo y cuya matriz de coeﬁcientes

es —salvo trasposici´on y el cambio de signo de algunas l´ıneas— la que se muestra en (1.1).

Por el teorema de Cramer, la resultante se anula si y solo si existe una soluci´on no trivial

de dicho sistema, esto es, si es posible escribir

P (X)

Q(X) = B(X)

A(X) ,

siendo los polinomios que forman la segunda fracci´on de grado estrictamente menor que

los de la primera. Pero este hecho equivale a que P (X) y Q(X) tengan un divisor com´un

no trivial, lo cual a su vez es equivalente a que P (X) y Q(X) posean en el cuerpo K (cierre

algebraico de K) alguna ra´ız en com´un.

En deﬁnitiva, el hecho de que dos polinomios P (X) y Q(X) pertenecientes a K[X]

compartan una ra´ız en el cierre algebraico de K encuentra su traducci´on exacta, bien

expl´ıcita y concisa, en que se cumpla la igualdad

Res(P , Q
) = 0.

1.3 Formulaci´on mediante resultantes 7

Cuando los coeﬁcientes ai, bi de los polinomios P (X) y Q(X) vienen dados en forma

param´etrica se obtienen generalizaciones de estos hechos. As´ı por ejemplo, si los diferentes

ai, bi son elementos de un anillo de polinomios K[t1, . . . , ts] entonces Res(P , Q
) es igual-

mente un polinomio en las indeterminadas t1, . . . , ts y coeﬁcientes en K, y Res(P , Q
) = 0 es

una ecuaci´on con s inc´ognitas cada una de cuyas soluciones α = (α1, . . . , αs) proporciona

dos polinomios, Pα(X) y Qα(X), tales que

O bien Pα(X) o Qα(X) son el polinomio cero.

O bien son polinomios de grado estrictamente menor que n y que m, respectivamente,

O bien Pα(X) y Qα(X) comparten una ra´ız en el cuerpo K,

sin que las dos ´ultimas posibilidades se excluyan mutuamente.

Como caso particular, si los coeﬁcientes ai, bi se toman como indeterminadas a las

que se asigna pesos iguales a su sub´ındice entonces Res(P , Q
) es un polinomio del anillo

graduado K[a0, . . . , an, b0, . . . , bm] en el que gr(
ak) = k, gr(
bk) = k. En estas condiciones, es

bien conocido que la resultante Res(P , Q
) es, de hecho, un polinomio homog´eneo pesado

de grado n · m; ello se debe a que el grado de un producto elemental no nulo surgido en el

desarrollo del determinante (1.1) que tome, por orden de ﬁlas, los elementos ubicados en

las columnas i1, i2,. . . ,in+m respectivamente, claramente vale

(i1−1
) + (i2−2
) + · · · + (im−m
) + (im+1−1) + · · · + (im+n−n) =

= (i1 + · · · + im+n) − (1 + 2 + · · · + m) − (1 + 2 + · · · + n), (1.2)

y esta suma tiene valor ﬁjo e igual a n · m pues, independientemente de qu´e permutaci´on

(i1, . . . , im+n) se considere, el primer par´entesis de (1.2) acoge a los n + m primeros n´umeros

naturales.

Nota 1.3.1. En general, los coeﬁcientes de los polinomios P (X) y Q(X) ser´an elementos de

un anillo conmutativo (y con elemento unidad) A. Entonces, la resultante R = Res(P , Q
)

deﬁnida por la expresi´on (1.1) es un elemento de A.

Si M es la matriz cuadrada de (1.1) y si ¯v, ¯w son las (n + m)-uplas del anillo de poli-

nomios A [ X] dadas respectivamente por

¯v = (Xm -1P (X),. . . , XP (X), P (X), Xn -1Q(X),. . . , XQ(X), Q(X)
), ¯w = (Xn+m -1,. . . , X, 1),

entonces se veriﬁca la igualdad matricial

M ¯w T = ¯v T

donde el super´ındice T signiﬁca traspuesta. Si interpretamos esta igualdad como un sistema

lineal y tenemos en cuenta que la ´ultima coordenada de ¯w es 1, se deduce de la regla de

Cramer que
 R = R · 1 = det(M ′),

8 Cap´ıtulo 1. El enunciado del problema

donde M ′ es la matriz que se obtiene sustituyendo la ´ultima columna de M por ¯v T .

Desarrollando el determinante de M ′ por los menores de los elementos de dicha ´ultima

columna se demuestra que R pertenece al ideal de A dado por 〈P (X), Q(X)
〉 ∩ A, siendo
〈P (X), Q(X)
〉 el ideal de A[ X] generado por los polinomios P (X) y Q(X).

Otra propiedad de las resultantes que nos ser´a de utilidad —aparte de la obvia igualdad

Res(P , Q
) = (−1)
nm Res(Q, P )— es la que describe su comportamiento frente al producto

de polinomios: Res(P1 · P2, Q
) = Res(P1, Q
) · Res(P2, Q
) (v´ease [Lan]).

1.3.1. Expresi´on en t´erminos de variedades algebraicas

Gracias a la utilidad de la resultante para caracterizar la existencia de una ra´ız com´un a

dos polinomios, el enunciado de Casas-Alvero tal como aparec´ıa en la p´agina 5 puede ser

reescrito en la siguiente forma:

Conjetura de Casas-Alvero. Se considera el polinomio con coeﬁcientes complejos

Pn(X) = Xn + ( n
2 )b2 Xn-2 + · · · + ( n
n-i)bn-i Xi + · · · + ( n
n-2)bn-2 X2 + ( n
n-1)bn-1 X

y, para cada i = 1, . . . , n −2, se considera H [i] := Res(Pn, Pn
[i]), seg´un deﬁniciones pre-

vias. En estas condiciones, si se tiene H [1] = H [2] = · · · = H [n-2] = 0, entonces se cumple

b2 = b3 = · · · = bn-1 = 0.

Si, haciendo un salto cualitativo, pasamos a considerar los coeﬁcientes bi del polinomio

Pn(X) como indeterminadas afectadas de pesos iguales a su sub´ındice, entonces

Cada resultante H [i] es un polinomio homog´eneo pesado de grado n · (n−i) en las

variables b2, . . . , bn−1 y con coeﬁcientes enteros; con las n−2 resultantes que ﬁguran

en el enunciado se genera un ideal de C[b2, . . . , bn-1] al cual denotaremos por I.

El conjunto de soluciones del sistema H [1] = H [2] = · · · = H [n-2] = 0 constituye una

variedad algebraica en el espacio af´ın complejo (n−2)-dimensional; se trata concre-

tamente de la variedad V (I) = {β = (β2, . . . , βn-1) ∈ Cn−2 | f (β) = 0 ∀f ∈ I}.

Las condiciones b2 = b3 = · · · = bn-1 = 0 deﬁnen la variedad algebraica V (⟨b2, . . . , bn-1⟩
),

formada por un ´unico punto —precisamente, el origen— del espacio af´ın Cn−2.

De este modo, el enunciado anterior pasa a expresarse como sigue:

Conjetura de Casas-Alvero. Sea Pn(X) = Xn + ( n
2 )b2 Xn-2 + · · · + ( n
n-1)bn-1 X , y sea,

para cada i = 1, . . . , n−2, el polinomio H [i] := Res(Pn, Pn
[i]) ∈ C[
b2, . . . , bn-1]
. Entonces,

en el espacio af´ın Cn−2, la variedad asociada al ideal I = 〈H [1], H [2], . . . , H [n-2]〉 no con-

tiene m´as puntos que el origen; esto es, se tiene: V (I) = V (⟨b2, . . . , bn-1⟩
).

1.3 Formulaci´on mediante resultantes 9

Observaci´on 1.3.2. Es claro que el ideal I es distinto del ideal maximal J = 〈b2, . . . , bn-1〉,

en el cual est´a estrictamente contenido. En efecto, I est´a generado por n−2 polinomios

homog´eneos pesados de grado n · (n−1), n · (n−2), . . . , 3n y 2n, respectivamente; no puede

por tanto contener polinomios de grado inferior a 2n. Cada bi tiene grado i, con i ≤ n−1,

as´ı que, de hecho, ninguno de los bi se encuentra en I.

1.3.2. Expresi´on en t´erminos de ideales

La tesis del enunciado de Casas-Alvero se ha reducido a la igualdad entre dos variedades

algebraicas:
 V (⟨H [1], H [2], . . . , H [n-2]⟩
) = V (⟨b2, . . . , bn-1⟩
). (1.3)

Dado que el problema est´a planteado sobre el cuerpo algebraicamente cerrado de los

n´umeros complejos, es aplicable el teorema de los Ceros de Hilbert, seg´un el cual la igual-

dad (1.3) entre las dos variedades es equivalente a la igualdad entre los radicales de los

respectivos ideales I = 〈H [1], H [2], . . . , H [n-2]〉 y J = 〈b2, . . . , bn-1〉. Y, puesto que J , por

ser primo, coincide con su propio radical, el problema de Casas-Alvero se transforma en

veriﬁcar la verdad o falsedad del siguiente enunciado:

Conjetura de Casas-Alvero. Sea I el ideal de C[
b2, . . . , bn-1] deﬁnido en la forma

antedicha. Se veriﬁca la igualdad: Rad
(I) = 〈b2, . . . , bn-1〉.

Observaci´on 1.3.3. Ning´un polinomio f ∈ C[
b2, . . . , bn-1] ∖ J pertenece al radical de I,

pues un t´ermino independiente no nulo en f no desaparece por m´as que f se eleve a la

r-´esima potencia, con lo cual es imposible que f r se halle en el ideal homog´eneo I, sea cual

sea el exponente r. Esto prueba la inclusi´on de Rad
(I) en el ideal J , as´ı que la diﬁcultad

real del problema de Casas-Alvero reside en la inclusi´on contraria. Es decir, la cuesti´on

pendiente es determinar la pertenencia o no de los elementos b2, . . . , bn-1 al ideal Rad
(I).

Es bien conocido el siguiente criterio:

Proposici´on 1.3.4 (Criterio de pertenencia al radical). Sea K un cuerpo arbitrario,

sea I = ⟨f1, . . . , fs⟩ un ideal del anillo R = K[x1, . . . , xn] y sea f ∈ R. Entonces f pertenece

al ideal Rad
(I) si y solo si el polinomio 1 pertenece al ideal ˜I = 〈f1, . . . , fs, 1 −zf 〉 del

anillo ̃R = K[x1, . . . , xn, z] (en cuyo caso, ˜I = ̃R).

Demostraci´on. Ver [CLS], p´agina 177. □

Aparece as´ı una nueva formulaci´on de la conjetura de Casas-Alvero, consistente en

postular la pertenencia de los bi al radical de I en la forma equivalente dada por 1.3.4:

10 Cap´ıtulo 1. El enunciado del problema

Conjetura de Casas-Alvero. Sea I = 〈H [1], H [2], . . . , H [n-2]〉 ⊂ C[
b2, . . . , bn-1]
. En-

tonces, para cada i = 2, . . . , n−1, el ideal ̃Ii = 〈H [1], H [2], . . . , H [n-2], 1−zbi〉 del anillo ̃R =

C[
b2, . . . , bn-1, z] contiene al elemento unidad de dicho anillo (y se cumple, por tanto,
̃Ii = ̃R).

1.3.3. Empleo de bases de Gr¨obner

En el anillo K[x] de los polinomios en una variable con coeﬁcientes en un cuerpo K, el

problema de averiguar si un polinomio f pertenece o no a un ideal dado, I = ⟨ g ⟩ — en

K[x] todos los ideales son principales— se resuelve sin m´as que dividir f entre g seg´un el

algoritmo cl´asico, y observar si el resto obtenido es o no nulo. Esta estrategia se extiende

al anillo de los polinomios en varias variables, pero para lograrlo ha sido preciso crear

herramientas espec´ıﬁcas capaces de superar ciertas obstrucciones que no se producen en

el caso de una variable.

En el anillo K[x1, . . . , xn] los ideales ya no son gen´ericamente principales, aunque

s´ı ﬁnitamente generados (teorema de la Base de Hilbert), es decir, de la forma I =

⟨f1, f2, . . . , fs⟩. Cualquier algoritmo de divisi´on destinado a calcular, para un polinomio

dado f , los cocientes a1, . . . , as y el resto r que, bajo ciertas especiﬁcaciones, cumplan

f = a1f1 + a2f2 + · · · + asfs + r,

necesita apoyarse en la previa ordenaci´on de los monomios que permita identiﬁcar al t´ermi-

no l´ıder tanto en el dividendo f como en los divisores f1, . . . , fs. No hay una forma ´unica

de satisfacer este requerimiento; es preciso elegir un orden monomial entre un abanico de

ellos entre los cuales no hay ninguno que sea can´onico o m´as natural que los otros.

Una vez ﬁjado un orden monomial, el algoritmo de divisi´on consiste en cancelar de

forma sistem´atica el t´ermino l´ıder del dividendo (que se actualiza cada vez) mediante

la sustracci´on de alg´un producto de la forma cij mij fi (siendo cij ∈ K y siendo mij un

monomio); cuando el t´ermino l´ıder no sea cancelable por este procedimiento se le transﬁere

al resto, que se constituye por acumulaci´on. El proceso se termina cuando se hace nulo

el dividendo, y entonces, para cada i = 1, . . . s, se tiene ai = ∑ cij mij. El problema, no

menor, es que el uso de los divisores fi est´a priorizado seg´un el orden en que han sido

listados; si se hace una permutaci´on en la lista (f1, . . . , fs) entonces el mismo algoritmo

producir´a resultados posiblemente diferentes de los anteriores; y no solo pueden obtenerse

cocientes distintos sino que incluso puede ser distinto el resto que se obtenga. En particular,

puede ocurrir que al aplicar el algoritmo de divisi´on a un polinomio f = ∑ bifi ∈ I resulte

f = a1f1 + a2f2 + · · · + asfs + r con r ̸= 0. Esto es, el test de pertenencia al ideal I tal

como lo hab´ıamos imaginado puede producir “falsos negativos”. Esta patolog´ıa es la que

vienen a resolver las llamadas bases de Gr¨obner.

1.3 Formulaci´on mediante resultantes 11

Una base de Gr¨obner es un sistema de generadores G = {g1, . . . gt} para el ideal I

cumpliendo la propiedad adicional de que para todo elemento f ∈ I, f ̸= 0, el t´ermino l´ıder

de f sea m´ultiplo del t´ermino l´ıder de alg´un gi ∈ G; por este motivo, ser´a imposible que

el algoritmo de divisi´on de un elemento de I entre los elementos de G produzca resto no

nulo. Es notable el hecho de que la propiedad caliﬁcada aqu´ı como adicional constituye

en realidad una condici´on suﬁciente para que un subconjunto G de I genere al ideal I.

A partir de un sistema de generadores ordinario B = {f1, . . . , fs} puede construirse una

base de Gr¨obner para I mediante el algoritmo de Buchberger, que b´asicamente consiste

en ir generando e incorporando a B nuevos polinomios del ideal, en un modo tal que cada

polinomio reci´en llegado aporte un t´ermino l´ıder que no sea m´ultiplo de ninguno de los

t´erminos l´ıderes preexistentes en B. Un polinomio as´ı, se obtiene a partir de una pareja

fi, fj cuyo S-polinomio deje resto no nulo al ser dividido por la totalidad de los elementos

de B; justamente ese resto se tomar´a para ser un nuevo fk a˜nadido a B. (El S-polinomio

de fi y fj se calcula como sigue:
 S(fi, fj) = ufi − vfj,

donde u y v est´an elegidos de modo que los respectivos t´erminos l´ıder de ufi y de vfj
sean del m´ınimo grado posible que permita su cancelaci´on mutua.)

Cuando los emparejamientos se hacen en forma sistem´atica (incluyendo en cada etapa

a los reci´en llegados) termina alcanz´andose un status en que ya ning´un S-polinomio deja

resto no nulo; exactamente este comportamiento caracteriza a una base de Gr¨obner, luego

B se ha convertido en una de ellas.

Esta base de Gr¨obner puede tener gran cantidad de elementos superﬂuos: todos aque-

llos elementos de B cuyo t´ermino l´ıder sea m´ultiplo del t´ermino l´ıder de alg´un otro com-

pa˜nero pueden suprimirse sin que el conjunto deje de ser una base de Gr¨obner para I; se

habr´a obtenido as´ı una base de Gr¨obner minimal para dicho ideal. No hay unicidad para

las bases de Gr¨obner minimales; sin embargo, partiendo de una cualquiera de ellas y me-

diante un proceso de sustracci´on para eliminar de cada polinomio todos aquellos t´erminos

que sean m´ultiplos de alg´un t´ermino l´ıder, se llega a una base de Gr¨obner reducida. Cada

ideal I posee una ´unica base de Gr¨obner reducida; este hecho proporciona un criterio de

igualdad para ideales: I y J son el mismo ideal si y solo si al calcular sendas bases de

Gr¨obner reducidas se obtiene el mismo resultado.

Regresando al problema de Casas-Alvero, para estudiar si es o no cierta la igualdad

Rad
(I) = 〈b2, . . . , bn-1〉

no podemos recurrir al criterio de comparar las respectivas bases de Gr¨obner reducidas

puesto que no disponemos de un sistema de generadores para Rad
(I) desde el cual iniciar

12 Cap´ıtulo 1. El enunciado del problema

los c´alculos. Ahora bien: tras la ´ultima reformulaci´on del enunciado (p´agina 10), el objetivo

es comprobar si se cumplen o no las n−2 igualdades (i = 2, . . . , n −1):

̃Ii :=
〈H [1], H [2], . . . , H [n-2], 1−zbi〉 = C[
b2, . . . , bn-1, z]
:= ̃R,

cada una de las cuales toma en consideraci´on un ideal, ̃Ii, del que se conoce de forma ex-

pl´ıcita un sistema de generadores, Bi = {H [1], H [2], . . . , H [n-2], 1−zbi}. Debido al car´acter

singular del ideal total ̃R (cuya base de Gr¨oebner reducida es, evidentemente, {1}), cada

una de estas igualdades ser´a cierta si y solo si al aplicarle a Bi el algoritmo de Buchberger

aparece en alg´un momento un polinomio unidad.

Estas reﬂexiones conducen a la siguiente formulaci´on para el problema de Casas-Alvero

en grado n.

Conjetura de Casas-Alvero. Se consideran los polinomios H [1], H [2], . . . , H [n−2] anterior-

mente construidos y, para cada i = 2, . . . , n −1, el ideal ̃Ii = 〈H [1], H [2], . . . , H [n-2], 1 −zbi〉

del anillo ̃R = C[
b2, . . . , bn-1, z]
, en el que se ha ﬁjado un orden monomial cualquiera.

Entonces, para todo i = 2, . . . , n −1, la base de Gr¨obner reducida de ̃Ii es {1}.

Ejemplo. Para n = 4, se tiene: P4(X) = X4 + 6 b2 X2 + 4 b3 X;

H [1] = 27
( b 4
3 + 2 b 3
2 b 2
3 ),

H [2] = 25 b 4
2 + 16 b2 b 2
3 .

La proposici´on 1.3.4 proporciona las siguientes equivalencias:

b2 ∈ Rad
〈H [1], H [2]〉 ⇐⇒ 1 ∈ ̃I2 = 〈H [1], H [2], 1 − b2 z〉

b3 ∈ Rad
〈H [1], H [2]〉 ⇐⇒ 1 ∈ ̃I3 = 〈H [1], H [2], 1 − b3 z〉;

mientras que la pertenencia del elemento unidad a un ideal queda caracterizada por la

aparici´on de dicho elemento en una base de Gr¨obner del ideal.

Trabajando con el orden monomial GRLEX (graduado lexicogr´aﬁco) se ha aplicado

el algoritmo de Buchberger para hallar una base de Gr¨obner de ̃I2 (resp. ̃I3), con los

resultados que se recogen en el cuadro 1.1; de este modo se ha obtenido una demostraci´on

para la conjetura de Casas-Alvero en grado n = 4.

Los c´alculos anteriores se han realizado por medio del programa DERIVE de c´alculo

simb´olico, de extendido empleo en ´ambitos docentes. Dadas las muy limitadas capacidades

del DERIVE como lenguaje de programaci´on, el algoritmo de Buchberger se ha ejecutado

introduciendo una a una las ´ordenes para la ejecuci´on de los sucesivos pasos, llevando

enteramente el control desde fuera del programa. Esto supone, en particular, determinar

por inspecci´on la expresi´on precisa para generar un nuevo S-polinomio, as´ı como localizar

al divisor adecuado (y determinar su factor acompa˜nante) para ordenar cada una de

1.3 Formulaci´on mediante resultantes 13

Para ̃I2 , se obtiene: Para ̃I3 , se obtiene:

f1 = 1
27 H [1] g1 = 1
27 H [1]

f2 = H [2] g2 = H [2]

f3 = b2 z−1 g3 = b3 z−1

S(f1, f2) → f4 = b2 b 4
3 S(g1, g2) → g4 = b2 b 4
3

S(f1, f3) → f5 = b 4
3 z + 2 b 2
2 b 2
3 S(g1, g3) → g5 = 2 b 3
2 b3 + b 3
3

S(f2, f3) → f6 = 25 b 3
2 + 16 b 2
3 S(g2, g5) → g6 = b2 b 3
3

S(f1, f4) → f7 = b 6
3 S(g3, g5) → g7 = 2 b 3
2 + b 2
3

S(f1, f6) → f8 = b 4
3 S(g2, g7) → g8 = b2 b 2
3

S(f3, f6) → f9 = 16 b 2
3 z + 25 b 2
2 S(g3, g8) → g9 = b2 b3

S(f1, f9) → f10 = b 2
2 b 2
3 S(g3, g9) → g10 = b2

S(f3, f10) → f11 = b2 b 2
3 S(g7, g10) → g11 = b 2
3

S(f3, f11) → f12 = b 2
3 S(g3, g11) → g12 = b3

S(f9, f12) → f13 = b 2
2 S(g3, g12) → g13 = 1

S(f3, f13) → f14 = b2

S(f3, f14) → f15 = 1

Cuadro 1.1: Elementos generados sucesivamente mediante el algoritmo de Buchberger

aplicado a los ideales ̃I2 y ̃I3

las sustracciones requeridas por el algoritmo de divisi´on. El modo de proceder adoptado

(manejando siempre los polinomios mediante su nombre, asignado en el mismo momento de

su obtenci´on) garantiza que, incluso una ejecuci´on imperfecta del algoritmo (por ejemplo,

por omitir una sustracci´on o identiﬁcar incorrectamente un t´ermino l´ıder) proporciona

resultados v´alidos, pues no se da opci´on a que se introduzcan polinomios que no sean

pertenecientes al ideal.

Se ha realizado una tentativa de aplicar la misma t´ecnica del ejemplo anterior para

el caso n = 5; pero enseguida resulta evidente que con cuatro indeterminadas la tarea se

vuelve enormemente m´as penosa, no solo por el aumento en la magnitud de la combinatoria

sino tambi´en por razones pr´acticas, como el modo en que DERIVE presenta por pantalla

los resultados, y las manipulaciones requeridas para poder analizarlos. Queda por tanto

de maniﬁesto que la herramienta que se emplea no es la m´as adecuada. Ahora bien:

14 Cap´ıtulo 1. El enunciado del problema

aunque usar programas m´as espec´ıﬁcos de c´alculo simb´olico permitir´ıa resolver el caso

n = 5, y posiblemente algunos casos particulares m´as, se muestra m´as adelante que el

caso general ofrece una obstrucci´on esencial a ser resuelto por este procedimiento. La

obstrucci´on consiste en la diﬁcultad de saber si el coeﬁciente del t´ermino supuestamente

l´ıder de un S-polinomio es en verdad no nulo. Como podr´a apreciarse en la secci´on 2.4,

comprobar si dicho coeﬁciente (dado gen´ericamente) es o no distinto de cero puede ser una

tarea con un grado de diﬁcultad equiparable a la de la propia conjetura.
Cap´ıtulo 2

Problemas parciales ( y primeras

respuestas)

En el cap´ıtulo precedente hemos ﬁjado, para el polinomio de grado n sin t´ermino vicel´ıder

ni t´ermino independiente y con coeﬁcientes en C gen´erico, la que hemos llamado su pre-

sentaci´on bin´omica,

Pn(X) = Xn + ( n
2 )b2 Xn-2 + . . . + ( n
n-i)bn-i Xi + . . . + ( n
n-1)bn-1 X (2.1)

y hemos deﬁnido la derivada neta i-´esima de Pn(X) como el polinomio

Pn
[i](X) = 1
n(n−1) · · · (n−i + 1) · P (i)(X) = Xn-i + (n-i
2 )b2 Xn-2-i + . . . + (n-i
n-i)bn-i . (2.2)

As´ımismo hemos introducido la notaci´on: H [i] = Res(Pn(X), Pn
[i](X)
).

Como hemos visto, el problema de Casas-Alvero para grado n consiste exactamente en

averiguar si Xn es el ´unico polinomio de la forma (2.1) que comparte una ra´ız con cada

una de sus derivadas de orden i = 1, . . . , n −2 o, equivalentemente, si

b2 = 0, b3 = 0, . . . bn−1 = 0

es la ´unica soluci´on del sistema H [1] = 0
...
H [n-2] = 0.
 


 (2.3)

Abordaremos este problema estableciendo versiones d´ebiles del mismo, en las cuales no

se contemplen todos los posibles polinomios de la forma (2.1) sino ´unicamente los que se

ajusten a una particular conﬁguraci´on, la cual vendr´a dada por el conjunto de los grados

i1, i2,. . . , ir de aquellos t´erminos que tienen opci´on a estar efectivamente presentes (esto

16 Cap´ıtulo 2. Problemas parciales ( y primeras respuestas)

es, a aparecer con coeﬁciente no nulo). Habr´a, por consiguiente, tantos problemas d´ebiles

(o parciales) como subconjuntos propios admite el conjunto formado por los grados de los

t´erminos de Pn(X) distintos del l´ıder.

2.1. El problema parcial con conjunto I de exponentes

A pesar de su sencillez, el siguiente hecho ser´a enormemente ´util.

Observaci´on 2.1.1. Si bn-i = 0, entonces la ecuaci´on H [i] = 0 se veriﬁca a fortiori.

En efecto, puesto que el t´ermino independiente de Pn
[i](X) coincide con la variable

bn-i, es evidente que si ´esta se anula entonces Pn(X) y Pn
[i](X) tendr´an en com´un la

ra´ız α = 0 y por tanto la resultante entre ambos, H [i], ser´a nula. Este comportamiento

signiﬁca que la indeterminada bn-i divide al polinomio H [i]; a la misma conclusi´on se

llega independientemente sin m´as que observar que el determinante en que por deﬁnici´on

consiste H [i] lleva a bn-i como el ´unico elemento diferente de cero de la ´ultima columna.

En lo sucesivo, consideraremos que se ha ﬁjado el grado n con que se trabaja.

Deﬁnici´on 2.1.2. Sea J = {1, 2, . . . , n−2}, y sea I = {i1 < i2 < · · · < ir} ⊂ J. Llamare-

mos I -polinomio de grado n al que, aparte del t´ermino l´ıder Xn, no lleva otros t´erminos

que no sean los de grado i1, i2, . . . , ir, esto es, que se ajusta a la forma

Pn(X) = Xn + ( n
n-ir )bn-ir Xir + . . . + ( n
n-i2)bn-i2 Xi2 + ( n
n-i1)bn-i1 Xi1, (2.4)

sin que los coeﬁcientes que aqu´ı ﬁguran se supongan necesariamente distintos de cero.

Restringir el campo de trabajo al de los I -polinomios equivale a imponer de antemano

las n−2−r condiciones de ser bn-j = 0 para todo j ∈ J ∖I; en virtud de la observaci´on 2.1.1,

para todo I -polinomio se satisfacen trivialmente las ecuaciones H [j ] = 0 correspondientes

a los n−2−r sub´ındices j ∈ J ∖I. En consecuencia, el I-polinomio Pn(X) que aparece en

(2.4) es un contraejemplo a la conjetura de Casas-Alvero si y solo si la r-upla de n´umeros

complejos (bn-ir , . . . , bn-i1) es una soluci´on no trivial del sistema

H [i1 ] = 0, H [i2 ] = 0, . . . H [ir ] = 0, (2.5)

puesto que al completar dicha r-upla con n −2 −r ceros ubicados en las posiciones ade-

cuadas se tendr´ıa una soluci´on no trivial del sistema (2.3).

Un contraejemplo de esta naturaleza ser´a llamado un I-contraejemplo.

Observaci´on 2.1.3. En rigor, dado i ∈ I, habr´ıa que distinguir entre la ecuaci´on H [i] = 0

del sistema (2.3), en la cual a´un ﬁguran como inc´ognitas las bn-j con j ∈ J ∖I, y la ecuaci´on

2.2 El monomio puro de una resultante, y el {i}-problema parcial 17

H [i]
∗ = 0 donde ya esas inc´ognitas bn-j han sido sustituidas por ceros, y solo permanecen

vivas las r inc´ognitas bn-ir , . . . , bn-i1; entonces, desde luego, en (2.5) deber´ıan escribirse

las formas con asterisco. Sin embargo, obviaremos esta distinci´on ya que en la pr´actica no

hay ning´un riesgo de confundirlas, y mantendremos la notaci´on H [i] a´un despu´es de haber

sustituido por ceros las variables bn-j en cuesti´on. Dicho sea de paso, lo que por supuesto

s´ı que resulta del todo indiferente es que esta sustituci´on —un homomorﬁsmo de anillos

de C[b2, . . . , bn-1] en C[bn-ir , . . . , bn-i1]— se realice antes o despu´es de haber calculado la

resultante entre los polinomios Pn(X) y Pn
[i](X).

Deﬁnici´on 2.1.4. Para cada conjunto I = {i1 < i2 < · · · < ir} ⊂ J = {1, 2, . . . , n−2} se

deﬁne el problema parcial de Casas-Alvero en grado n y con conjunto de exponentes I (o,

brevemente, el I-problema de Casas-Alvero) como aquel que consiste en averiguar si el

sistema (2.5) posee ´unicamente la soluci´on trivial (en cuyo caso diremos que el I-problema

tiene respuesta aﬁrmativa) o si, por el contrario, existe alguna soluci´on no trivial del

mismo; esto es, si existe alg´un I-contraejemplo al problema (total) de Casas-Alvero en

grado n.

2.2. El monomio puro de una resultante, y el {i}-problema

parcial

Tomando para Pn(X) y Pn
[i](X) las expresiones dadas en (2.1) y (2.2) respectivamente, su

resultante adopta la forma que se muestra en la ﬁgura 2.1. La disposici´on de los elementos

en la matriz invita a visualizarla partida en 9 cajas, de las cuales, las 4 situadas en la zona

superior izquierda, A, B, C y D, son cuadradas de orden n−i.

Proposici´on 2.2.1. Se tiene: H [i] = b n
n-i [ 1−
( n
n-i
 )]n-i + bn-i Qi, donde Qi es un

polinomio cuyos monomios contienen todos al menos una variable bj diferente de bn-i .

Demostraci´on. Como ya se ha se˜nalado en la observaci´on 2.1.1, es claro que H [i] es un

m´ultiplo de bn-i. En particular, si aparece en H [i] alg´un monomio puro, esto es, que so-

lamente involucre una indeterminada, esta habr´a de ser necesariamente bn-i, as´ı que, por

cuesti´on de grados, el monomio no puede ser otro que b n
n-i. En H [i] hay, en total, 2n−i

productos elementales que contienen b n
n-i : obviamente, el producto P de todos los elemen-

tos de la diagonal principal, pero tambi´en, para cada j = 1, . . . , n −i, los (n-i
j ) productos

elementales iguales a ( n
n-i
)j b n
n-i que resultan de sustituir en P a j de los n−i factores

—de valor bn-i — procedentes de la diagonal de D, por los correspondientes factores —de

valor ( n
n-i
) bn-i — que se encuentran en su misma vertical, en la diagonal de B (ver ﬁgura

2.1). A cambio, j factores de valor 1 tomados de A son sustituidos por otros, id´enticos,

18 Cap´ıtulo 2. Problemas parciales ( y primeras respuestas)

n−i
︷ ︸︸ ︷ n−i
︷ ︸︸ ︷ i
︷ ︸︸ ︷

!
| !
|1 0 ( n
2 )b2 · · · · · · · · · !
|
( n
n-i
)
bn-i · · · · · · ( n
n-1
)
bn-1 0 0 !
| 0 0 0 0

0 1 0 ( n
2 )b2 · · · · · · !
| · · · ( n
n-i
)
bn-i · · · · · · ( n
n-1
)
bn-1 0 !
| 0 0 0 0
... . . . . . . . . . !
| . . . . . . . . . !
| ...
... 1 !
| ( n
n-i
)
bn-i . . . !
| . . . ...
... A . . . . . . !
| . . . B . . . !
| . . . ...

0 0 · · · 1 !
| 0 ( n
2 )b2 · · · · · · ( n
n-i
)
bn-i
!
| · · · . . . ( n
n-1
)
bn-1 0
— - -— - -— - -— - -— - -— - -
!
|— - -— - -— - - — - - — - -— - -!
|— - -— - -— - -— - -
1 0 (n-i
2 )
b2 · · · · · · !
| bn-i 0 0 0 0 !
| 0 · · · · · · 0

0 1 · · · · · · !
| bn-i 0 0 0 !
| 0 ...
... . . . . . . . . . !
| . . . ... !
| ... ...
... 1 !
| bn-i
 !
| ...
... C . . . . . . !
| . . . D . . . 0 !
| 0 ...

0 0 · · · 1 !
| 0 (n-i
2 )
b2 · · · · · · · · · bn-i
 !
| 0 · · · · · · 0
— - -— - -— - -— - -— - -— - -
!
|— - -— - -— - - — - - — - -— - -!
|— - -— - -— - -— - -
0 0 · · · · · · 0 !
| 1 0 (n-i
2 )
b2 · · · · · · · · · !
| bn-i 0 · · · 0

0 0 !
| 1 0 (n-i
2 )
b2 · · · !
| bn-i ...
... ... ... !
| . . . . . . . . . !
| . . . 0

0 0 · · · · · · · · · 0 !
| 1 0 (n-i
2 )
b2
 !
| · · · · · · · · · bn-i
 



 n−i





 n−i





 i

Figura 2.1: Resultante de Pn(X) y Pn
[i](X).

de C. Estas maniobras cambian j veces la paridad del n´umero de inversiones, por lo que

los productos elementales se afectan del signo (−1)
j.

Asociando todos los t´erminos de este tipo aparece el factor com´un b n
n-i que multiplica

a cada t´ermino de la siguiente suma:
( n-i
0
 ) − ( n-i
1
 )( n
n-i
 ) + ( n-i
2
 )( n
n-i
 )2 − · · · + (−1)
j( n-i
j
 )( n
n-i
 )j+

+ · · · + (−1)
n-i( n-i
n-i
 )( n
n-i
 )n-i = [ 1 − ( n
n-i
 )]n-i;

los restantes t´erminos llevan a bn-i como factor com´un y, al menos, otra indeterminada

diferente; entre todos constituyen el producto bn-i Qi. □

Proposici´on 2.2.2 (Caso I = {i}). Cuando se considera el {i}-polinomio de grado n,

Pn(X) = Xn + ( n
n-i)bn-i Xi, la ´unica resultante no trivial es H [i] = b n
n-i [ 1−
( n
n-i)]n- i
.

2.3 El {i, j}-problema parcial 19

Demostraci´on. Es una consecuencia inmediata de la proposici´on 2.2.1, ya que todos los

sumandos de Qi contienen al menos un factor bn-j, con j ̸= i, que de antemano est´a susti-

tuido por un cero puesto que Pn(X) es un {i}-polinomio; as´ı pues, Qi queda anulado.

Alternativamente, si el hecho de ser nulas todas las variables bn-j con j ̸= i se traslada

a la matriz mostrada en la ﬁgura 2.1, entonces el c´alculo del determinante carece de

diﬁcultad. Restando cada una de las n−i ﬁlas del primer bloque a su correspondiente

hom´ologa del segundo bloque, y desarrollando por las n columnas con un ´unico elemento

no nulo que entonces presenta la matriz, solo queda calcular un determinante triangular

(de hecho, diagonal) de orden n; el resultado es inmediato y, naturalmente, coincidente

con el del enunciado. □

Corolario 2.2.3. En cualquier grado, y para todo i, el {i}-problema de Casas-Alvero de

grado n tiene respuesta aﬁrmativa, esto es:

No existen {i}-contraejemplos a la conjetura de Casas-Alvero.

Demostraci´on. Al ser 1 ≤ i ≤ n −2, el n´umero combinatorio ( n
n-i ) es distinto de 1; por

tanto, la ecuaci´on H [i] = 0 que, en virtud de la proposici´on 2.2.2 es

b n
n-i [ 1−
( n
n-i
 )]n-i = 0

no tiene en el conjunto C otra soluci´on que bn-i = 0.

2.3. El {i, j}-problema parcial

Ahora que sabemos que no existen, en ning´un grado n ∈ N, contraejemplos a la conjetura

de Casas-Alvero que cuenten con un ´unico t´ermino adicional al l´ıder, es natural preguntarse

si existir´a alg´un contraejemplo con dos t´erminos adicionales.

La respuesta a esta pregunta se descubre en esta secci´on. Para ello, nos ser´a de utilidad

el siguiente lema t´ecnico.

Lema 2.3.1. Sea M la matriz cuadrada de orden r + s que se muestra en la ﬁgura 2.2, en

la cual todos los elementos distintos de los indicados mediante letras o elipsis son iguales

a cero. Entonces, el valor de su determinante viene dado por

det (M ) = [A ρD σ + (−1) ρσB ρC σ] d,

siendo d = m.c.d.
(r, s
), y siendo ρ = r
d , σ = s
d .

Demostraci´on. Es preciso tratar por separado los dos casos siguientes:

Caso 1: r y s primos entre s´ı. Los ´unicos elementos distintos de cero de la matriz M

se encuentran dispuestos en tres l´ıneas diagonales, que son

20 Cap´ıtulo 2. Problemas parciales ( y primeras respuestas)

r
 




s
 



 s
︷ ︸︸ ︷ r
︷ ︸︸ ︷

A | B |
A | B |
A | B |
. . . | | . . .

| . . . | . . .
| A | B
| A | B
− − − − − − − − − − − − − − − − −
C | | D
C | | D
. . . | | . . .
C | | D

Figura 2.2: Matriz M

La diagonal principal, con los elementos mi,i = { A, si 1 ≤ i ≤ r
D, si r + 1 ≤ i ≤ r + s

La paralela superior, con los elementos mi,i+s = B, para 1 ≤ i ≤ r.

La paralela inferior , con los mi,i-r = C, para r + 1 ≤ i ≤ r + s.

Es claro que los productos elementales ArDs y B rC s se encuentran en el desarrollo de

det(M ), yendo el segundo afectado del signo (−1)
rs, ya que la permutaci´on de ´ındices

de columnas que le corresponde es (s + 1, s + 2, . . . , s + r, 1, 2, . . . , s), sin m´as inversiones que

las que presenta cada uno de los r primeros elementos con cada uno de los s ´ultimos.

Falta solo comprobar que todos los dem´as productos elementales son nulos. La t´actica

para ello consistir´a en mostrar que la construcci´on de un producto elemental partiendo de

un elemento de la diagonal principal, y bajo la condici´on de no tomar ning´un elemento

distinto de A, B, C o D, conduce inevitablemente al primero de los dos productos ya

conocidos, ArDs, concluy´endose que no hay m´as productos elementales diferentes de cero

que este (formado por todos los elementos de la diagonal principal), y B rC s, que no

contiene ning´un elemento de dicha l´ınea.

Dado i ≤ r, en la ﬁla del elemento mi,i = A ubicado en la diagonal principal solo hay

otro elemento no nulo, que est´a situado s puestos a su derecha y es mi,i+s = B. A su vez,

en la columna de este ´ultimo solamente hay otro elemento no nulo, situado s puestos m´as

abajo, y que, por tanto, es mi+s,i+s. En consecuencia, para formar un producto elemental

P que evite los ceros y que contenga al factor mi,i, dado que no podemos tomar a mi,i+s
(pues repetir´ıamos ﬁla) y que hemos de incluir un factor extra´ıdo de la columna i + s,

necesariamente ha de tomarse para P el elemento mi+s,i+s. Este elemento puede valer A

2.3 El {i, j}-problema parcial 21

o valer D, lo cual nos es indiferente; lo signiﬁcativo aqu´ı es que se encuentra tambi´en en

la diagonal principal.

Dado ahora i > r, razonando del mismo modo vemos que si P incorpora a mi,i = D

entonces queda excluida la posibilidad de poner a mi,i-r = C, pero eso obliga a tomar al

otro elemento no nulo de la columna i−r, que es mi-r,i-r , perteneciente asimismo a la

diagonal principal.

As´ı pues, basta saber que P contiene un elemento de la diagonal principal para poder

aﬁrmar que tambi´en contiene a otro, al que se llega —seg´un el caso— o bien avanzando s

lugares o bien retrocediendo r lugares a lo largo de la diagonal. Estas dos procedimientos

alternativos entre los cuales ha de elegirse el que corresponda al caso no son, sin embargo,

distintos m´as que en apariencia: recorriendo c´ıclicamente los r + s elementos de la diagonal,

da lo mismo avanzar s que retroceder r lugares a partir de la posici´on i; comportamiento

que queda descrito por la expresi´on i + s ≡ i −r mod r + s.

En deﬁnitiva, si mi,i se encuentra en P, al iterar el argumento anterior se genera una

secuencia del tipo siguiente (los primeros t´erminos son, aqu´ı, supuestos)

i, i + s, i + 2s, i + 2s − r, i + 3s − r, . . . , i + ks − tr, . . . (2.6)

que proporciona —mediante la aritm´etica ordinaria— los ´ındices simples (comprendidos

entre 1 y r + s) de aquellos elementos de la diagonal principal cuya presencia en P se va

deduciendo en pasos sucesivos a partir del dato inicial, i. De forma equivalente, empleando

la aritm´etica modular (m´odulo r + s) obtenemos la misma secuencia de ´ındices bajo la

forma i, i + s, i + 2s, i + 3s, i + 4s, . . . , i + (k + t)s, . . . (2.7)

cuando para cada uno de estos n´umeros, que son clases de equivalencia, se elige el repre-

sentante comprendido entre 1 y r + s. En el grupo aditivo Z/(r+s), el elemento s tiene

orden igual al cardinal del grupo, r + s, puesto que, al ser s primo con r, lo es tambi´en

con r + s. Esto signiﬁca que en Z/(r+s) los r +s elementos s, 2s, 3s, 4s, . . . , (r + s)s son

todos ellos distintos (y el ´ultimo, igual a cero), pero entonces la secuencia dada en (2.7)

es, exactamente,

i, i + s, i + 2s, i + 3s, i + 4s, . . . , i + (r + s−1)s;

est´a formada por r + s elementos distintos y contiene, por tanto, todas las posiciones

de la diagonal principal. Queda as´ı probado que P es, necesariamente, ArDs, de modo

que, en deﬁnitiva, es det (M ) = A rD s + (−1) rsB rC s. Este resultado es conforme con el

enunciado del lema pues, en el caso actual, es d = m.c.d.(r, s) = 1, ρ = r, σ = s.

Caso 2: m.c.d.(r, s) = d > 1. A diferencia del caso anterior, en este caso s´ı van a existir

productos elementales mixtos, esto es, que combinen factores tomados de la diagonal

principal con otros procedentes de las paralelas.

22 Cap´ıtulo 2. Problemas parciales ( y primeras respuestas)

Respecto del caso anterior se mantiene la validez tanto de la descripci´on de M como,

consecuentemente, de los razonamientos para deducir que todo producto elemental P de

M que no tome ning´un cero y en el que se encuentre mi,i ha de contener tambi´en a los

elementos de la diagonal principal cuya posici´on en la misma venga dada por la secuencia

(2.6) en aritm´etica ordinaria o, equivalentemente, por la secuencia (2.7) en aritm´etica

modular (m´odulo r + s). Sin embargo, del an´alisis de dichas secuencias se desprender´an

esta vez conclusiones bien diferentes.

En efecto, siendo r = ρ d y s = σd con ρ y σ primos entre s´ı, en el grupo c´ıclico

Z/(r+s) el elemento s tiene orden ρ + σ, dado que ks solo es divisible entre r + s si kσ lo es

entre ρ + σ, y esto ocurre por primera vez para k = ρ + σ pues m.c.d.(σ, ρ + σ) = 1. Quiere

esto decir que los ρ + σ elementos s, 2s, 3s, 4s, . . . , (ρ + σ)s son todos distintos (siendo el

´ultimo, nulo) y, por lo tanto, en la secuencia (2.7), los ρ + σ primeros t´erminos

i, i + s, i + 2s, i + 3s, i + 4s, . . . , i + (ρ + σ −1)s

tambi´en son todos distintos, mientras que la prolongaci´on de dicha secuencia no hace sino

replicar una y otra vez este fragmento. En particular, el t´ermino que sigue a los ya dados

es, de nuevo, i.

Trasladando las anteriores conclusiones a 2.6, se tiene que sus ρ + σ primeros t´ermi-

nos son distintos pero a partir de ese momento todo se repite; en particular, el primer

t´ermino en repetirse ser´a de la forma i + ks − tr con k + t = ρ + σ (pues ´ese es el n´umero

de pasos necesarios para llegar hasta ´el) y, adem´as, i + ks − tr = i, pues despu´es de ρ + σ

pasos recaemos en el valor inicial. Gr´aﬁcamente, tras ρ + σ pasos se cierra el ciclo de los

elementos de la diagonal principal que se visitan al iterar el razonamiento sobre los factores

obligadamente presentes en P cuando se sabe que mi,i est´a presente. Interesa determinar

el conjunto Ii que forman los ´ındices de los elementos involucrados en dicho ciclo.

Si j pertenece a Ii, entonces j es congruente con i m´odulo d puesto que

j = i + ks − tr = i + d(kσ − tρ);

ahora bien, en el conjunto I = {1, 2, . . . , r + s} hay exactamente r + s
d = ρ + σ n´umeros que

sean congruentes m´odulo d con el elemento i en cuesti´on, luego Ii es justamente el conjunto

formado por todos ellos, esto es, Ii coincide con uno de los siguientes subconjuntos de I:

I1 = { 1 , 1 + d , 1 + 2d , . . . , 1 + (ρ + σ−1)d }

I2 = { 2 , 2 + d , 2 + 2d , . . . , 2 + (ρ + σ−1)d }

...
Id-1 = {
d−1, 2d−1 , 3d−1 , . . . , (ρ + σ)d−1 }

Id = { d , 2 d , 3 d , . . . , (ρ + σ) d };

(obs´ervese que, si i ≡ j mod d, entonces Ii = Ij; basta por tanto usar i = 1, . . . , d).

2.3 El {i, j}-problema parcial 23

Tenemos, en deﬁnitiva, que si mi,i est´a en P, entonces el producto parcial Pi = ∏

j∈Iimj,j

en bloque forma parte de P.

Por otra parte, si mi,i no est´a en P, entonces ha de estar el otro elemento no nulo de

la ﬁla i-´esima (situado en una de las dos paralelas), al cual denotaremos m∗
i ; y otro tanto

suceder´a para los restantes j ∈ Ii, con lo cual esta vez ser´a el producto parcial P ∗
i = ∏

j∈Ii m∗
j
el que forme parte de P.

As´ı pues: Fijado un producto elemental P que no incluya ceros, sabemos que, para

cada i = 1, . . . , d, la contribuci´on al mismo de las ﬁlas i, i + d, i + 2d . . . es, o bien Pi , o bien

P ∗
i . Nada impide que coexistan productos parciales de uno y otro tipo. Hay, por tanto, 2d

diferentes conﬁguraciones posibles para P, tantas como formas de elegir cu´antos y cu´ales

de los d productos parciales se toman del segundo tipo, esto es, tantas como subconjuntos

tiene un conjunto de cardinal d.

Precisando m´as: De las ρ + σ ﬁlas indicadas por los elementos de Ii, ρ se encuentran en-

tre las r primeras ﬁlas y σ entre las s ´ultimas, de modo que ser´a Pi = AρDσ y P ∗
i = B ρC σ ,

expresiones ambas que ya no dependen de i. Por tanto, para cada k = 0, . . . , d, los ( d
k ) pro-

ductos elementales que toman exactamente k productos parciales del tipo segundo tienen

un mismo valor, que es (AρDσ)d−k (B ρC σ)k.

M´as arduo ser´ıa analizar el signo aparejado a cada uno de estos productos elementales;

puede eludirse esa tarea aplicando propiedades b´asicas de los determinantes para calcular

det(M ) de otro modo.

Observemos qu´e sucede si, sobre la matriz M , efectuamos intercambios de ﬁlas que

coloquen en las ρ + σ primeras posiciones a las ﬁlas F1, F1+d, F1+2d. . . , F1+(ρ+σ−1)d y,

seguidamente, intercambios de columnas que pongan en las ρ + σ primeras posiciones a

las columnas C1, C1+d, C1+2d. . . , C1+(ρ+σ−1)d. El signo del determinante se modiﬁca cier-

to n´umero de veces debido a las operaciones en ﬁlas, y otras tantas veces debido a las

operaciones en columnas (pues unas y otras son nominalmente coincidentes) as´ı que, en

deﬁnitiva, tras un n´umero par de cambios, queda como estaba. Pero todos estos movimien-

tos colocan a las antiguas mj ,j con j ∈ I1 en las ρ + σ primeras posiciones de la diagonal

principal y traen, acompa˜n´andolas, a los elementos B y C que compart´ıan ﬁla o columna

con ellas. Pero, como solo se toma una de cada d ﬁlas y una de cada d columnas, las

distancias r o s que originalmente exist´ıan entre ellos quedan convertidas en distancias ρ o

σ, respectivamente. Esto es, se concentran en una caja de tama˜no (ρ + σ) × (ρ + σ) situada

en la esquina superior derecha todos los elementos no nulos de las ﬁlas y columnas de

n´umero j ∈ I1. Esa caja —que llamaremos matriz M1— contiene a los elementos A, B, C,

D dispuestos en tres diagonales seg´un el esquema mostrado en la ﬁgura (2.2), solo que los

n´umeros r y s se ven sustituidos por ρ y σ respectivamente.

24 Cap´ıtulo 2. Problemas parciales ( y primeras respuestas)

Repitiendo el mismo tipo de proceso afectando esta vez a las ﬁlas y columnas de

n´umero j ∈ I2 se logra una caja M2 colocada como intersecci´on de las ρ + σ ﬁlas con las

ρ + σ columnas que siguen a las que contienen a M1. La forma y el contenido de M2 son

id´enticos a los de M1.

Procediendo as´ı sucesivamente con I3, . . . , Id, se recolocan los elementos de M sin

haber alterado el valor del determinante. La matriz que resulta est´a dividida en d × d

cajas cuadradas de tama˜no (ρ + σ) × (ρ + σ), todas las cuales son nulas excepto las cajas

colocadas en la diagonal, que son M1, M2, . . . , Md, todas ellas iguales entre s´ı y que ya han

sido descritas al terminar el proceso que dio lugar a M1.

As´ı pues,
 det(M ) = det(M1) · det(M2) · · · · · det(Md) = [det(M1)
]d. (2.8)

Aplicando a M1 el presente lema 2.3.1 en el caso previamente demostrado (pues ρ y σ

s´ı son primos entre s´ı) se obtiene

det (M1) = A ρD σ + (−1) ρσB ρC σ. (2.9)

La igualdad (2.8), junto con (2.9), establecen la validez de la f´ormula dada en el enunciado

de este lema. □

Proposici´on 2.3.2 (Caso I = {i, j}). Cuando se considera el {i, j}-polinomio de grado n,

Pn(X) = Xn + ( n
n-j)bn-j Xj + ( n
n-i)bn-i Xi,

las dos ´unicas resultantes asociadas al problema de Casas-Alvero que no son trivialmente

nulas son
 H [i] = (−1)
sr+r b j
n-i [ α ρβ σ b ρ+σ
n-j + (−1)ρσ+σ γ ρ+σ b ρ
n-i ] d

H [j ] = (−1) r b i
n-j [ δ ρ b ρ+σ
n-j + (−1)ρσ (1 + γ )ρ b ρ
n-i ] d

donde: r = n−j, s = j −i, d = m.c.d.
(r, s), ρ = r
d , σ = s
d , y donde

α = ( n
j )−
(n- i
n-j); β = ( n
j )−
(n- i
n-j)( n
i ); γ = ( n
i )−1; δ = ( n
j )−1.

Demostraci´on. El proceso para obtener la expresi´on de H [i] puede seguirse en el cuadro

2.1. Para mayor claridad, se han introducido los literales a, b, c, I, J, con el signiﬁcado

que all´ı se expresa, y que se mantendr´a en el resto del cap´ıtulo —obs´ervese el uso t´acito

de las identidades ( n
n-i
) = ( n
i ), ( n
n-j) = ( n
j )—. Los elementos de la matriz que no aparecen

visibles son todos ellos iguales a cero.

2.3 El {i, j}-problema parcial 25

I
 ↑








↓

II
 ↑



↓

III
 ↑








↓

IV
 ↑



↓
 r
︷ ︸︸ ︷ s
︷ ︸︸ ︷ r
︷ ︸︸ ︷ s
︷ ︸︸ ︷ i
︷ ︸︸ ︷

| !
: | !
:1 | bJ !
: aI | !
:
1 | bJ !
: aI | !
:
. . . | !
: . . . . . . | !
:
1 | !
: bJ aI | !
:
— — — — |— — !
: — — — — | — — !
:— — — —
| 1 !
: bJ | aI !
:
| 1 !
: bJ | aI !
:
-·-· -·-· -·-· -·-· | -·-· -·-·!
: -·-· -·-· -·-· -·-· | -·-· -·-· !
:-·-· -·-· -·-· -·-·
1 | cJ !
: I | !
:
1 | cJ !
: I | !
:
. . . | !
: . . . . . . | !
:
1 | !
: cJ I | !
:
— — — — |— — !
: — — — — | — — !
:— — — —
| . . . !
: . . . | . . . !
:
| 1 !
: cJ | I !
:
-·-· -·-· -·-· -·-· | -·-· -·-·!
: -·-· -·-· -·-· -·-· | -·-· -·-· !
:-·-· -·-· -·-· -·-·
| !
: 1 | cJ !
: I
| !
: 1 | cJ !
: I

| !
: . . . | !
:. . . . . .

| !
: 1 | !
: cJ I
 



 r = n−j

}
 s = j −i





 r

}
 s





 i
 Al bloque I se le resta el

bloque III.

Al bloque II se le resta el

bloque IV multiplicado por a.

a := ( n
i )

b := ( n
j )

c := (n-i
n-j)

J := bn-j

I := bn-i
 →
 A := (b−c)J = αJ

B := (a−1)I = γ I

C := 1−a = − γ

D := (b − ac)J = βJ

r
 




s
 {

r
 




s
 {

i
 



 r
︷ ︸︸ ︷ s
︷ ︸︸ ︷ r
︷ ︸︸ ︷ s
︷ ︸︸ ︷ i
︷ ︸︸ ︷

| !
: | !
:0 | A !
: B | !
:
0 | A !
: B | !
:
. . . | !
: . . . . . . | !
:
0 | !
: A B | !
:
— — — — |— — !
: — — — — | — — !
:— — — —
| C !
: D | 0 !
:
| C !
: D | 0 !
:
-·-· -·-· -·-· -·-· | -·-· -·-·!
: -·-· -·-· -·-· -·-· | -·-· -·-· !
:-·-· -·-· -·-· -·-·
1 | ∗ !
: I | !
:
1 | ∗ !
: I | !
:
. . . | !
: . . . . . . | !
:
1 | !
: ∗ I | !
:
— — — — |— — !
: — — — — | — — !
:— — — —
| . . . !
: . . . | . . . !
:
| 1 !
: ∗ | I !
:
-·-· -·-· -·-· -·-· | -·-· -·-·!
: -·-· -·-· -·-· -·-· | -·-· -·-· !
:-·-· -·-· -·-· -·-·
| !
: 1 | ∗ !
: I
| !
: 1 | ∗ !
: I

| !
: . . . | !
:. . . . . .

| !
: 1 | !
: ∗ I
 = (−1)
r(r + s) I s + i
 s
︷ ︸︸ ︷ r
︷ ︸︸ ︷

!
: !
:A !
: B !
:
A !
: B !
:

!
: . . . !
: . . .
!
: A !
: B
— — !
: — — !
:— —
C !
: !
: D
C !
: !
: D
 



 r

}
 s

Cuadro 2.1: C´alculo de H [i] en el {i, j}-problema.

26 Cap´ıtulo 2. Problemas parciales ( y primeras respuestas)

I
 ↑









↓

II
 ↑








↓
 r
︷ ︸︸ ︷ r
︷ ︸︸ ︷ s
︷ ︸︸ ︷ i
︷ ︸︸ ︷

!
: !
: |1 !
: bJ aI !
: |
1 !
: bJ aI !
: |
. . . !
: . . . !
: . . . |
1 !
: bJ !
: aI |
-·-· -·-· -·-· -·-· !
: -·-· -·-· -·-· -·-· !
: -·-· -·-· | -·-· -·-· -·-· -·-·
1 !
: J !
: |
1 !
: J !
: |
. . . !
: . . . !
: |
1 !
: J !
: |
-·-· -·-· -·-· -·-· !
: -·-· -·-· -·-· -·-· !
: -·-· -·-· | -·-· -·-· -·-· -·-·
!
: . . . !
: . . . |
!
: 1 !
: J |
— — — — !
: — — — — !
: — — | — — — —!
: 1 !
: | J
!
: 1 !
: | J

!
: !
: . . . | . . .
!
: !
: 1 | J
 



 r = n-j





 r

}
 s = j -i





 i
 Al bloque I se le resta el

bloque II.

a := ( n
i )

b := ( n
j )

J := bn-j

I := bn-i
 → E := (b−1)J = δJ

F := aI = (1 +γ)I

r
 




r
 




s
 {

i
 



 r
︷ ︸︸ ︷ r
︷ ︸︸ ︷ s
︷ ︸︸ ︷ i
︷ ︸︸ ︷

!
: !
: |0 !
: E F !
: |
0 !
: E F !
: |
. . . !
: . . . !
: . . . |
0 !
: E !
: F |
-·-· -·-· -·-· -·-· !
: -·-· -·-· -·-· -·-· !
: -·-· -·-· | -·-· -·-· -·-· -·-·
1 !
: J !
: |
1 !
: J !
: |
. . . !
: . . . !
: |
1 !
: J !
: |
-·-· -·-· -·-· -·-· !
: -·-· -·-· -·-· -·-· !
: -·-· -·-· | -·-· -·-· -·-· -·-·
!
: . . . !
: . . . |
!
: 1 !
: J |
— — — — !
: — — — — !
: — — | — — — —!
: 1 !
: | J
!
: 1 !
: | J

!
: !
: . . . | . . .
!
: !
: 1 | J
 = (−1)
r J i
 r
︷ ︸︸ ︷ s
︷ ︸︸ ︷

!
: !
:E !
: F !
:
E !
: F !
:

!
: . . . !
: . . .
!
: E !
: F
— — !
: — — !
:— —
1 !
: !
: J
1 !
: !
: J
 



 r

}
 s

Cuadro 2.2: C´alculo de H [j] en el {i, j}-problema.

2.3 El {i, j}-problema parcial 27

A las l´ıneas separadoras que ya se utilizaron en la ﬁgura 2.1 para la demostraci´on de la

proposici´on 2.2.1, se han superpuesto otras (a trazos largos) que, junto con las anteriores,

subdividen la matriz en 5 × 5 cajas; esta partici´on permite apreciar c´omo las r + s = n−i

sustracciones de ﬁlas que se indican producen la matriz que se encuentra en la parte inferior

izquierda del cuadro 2.1. A partir de esta matriz, se desarrolla el determinante s + i veces

por la ´ultima columna —aparece as´ı el factor I s+i = I j— y luego, r veces seguidas por la

primera columna, por lo que surge r veces el factor (−1)
r+s+2 = (−1)
r+s; obs´ervese que, al

tener siempre r y r2 la misma paridad, es (−1)
r(r+s) = (−1)
r+sr. El determinante de orden

n−i que todav´ıa queda pendiente de c´alculo tiene la conﬁguraci´on adecuada para poder

aplicar el lema 2.3.1, seg´un el cual, dicho determinante vale
[A ρD σ + (−1) ρσB ρC σ] d = [(αJ) ρ(βJ) σ + (−1) ρσ(γI) ρ(−γ) σ] d ;

operando y sustituyendo se obtiene para H [i] el resultado esperado.

El c´alculo de la otra resultante, H [j ], se muestra en el cuadro 2.2, y sigue un pro-

cedimiento an´alogo. Una vez hechas las sustracciones de ﬁlas que generan los ceros en la

diagonal de la primera caja, se desarrolla el determinante por sus ´ultimas i columnas y

luego, por cada una de sus r primeras columnas. Aparecen de ese modo los factores J i y

(−1)
(r+2)r = (−1)
r, junto con un determinante de orden n −i que, de nuevo por aplicaci´on

del lema 2.3.1, vale
[E ρJ σ + (−1) ρσF ρ 1σ] d = [(δJ) ρ J σ + (−1) ρσ((1 + γ)I) ρ] d ;

basta ahora operar y sustituir para obtener la conclusi´on. □

Estamos ya en condiciones de caracterizar cu´ando un {i, j}-problema tiene respuesta

aﬁrmativa, y cu´ando no la tiene:

Teorema 2.3.3. El sistema de ecuaciones asociado al {i, j}-problema de grado n,

H [i] = 0, H [j ] = 0, bn-k = 0 ∀k ̸= i, j

posee soluciones diferentes de la trivial si y solo si se veriﬁca la igualdad

a ρ (b − c
)ρ(b − ac
)σ = (−1)σ(a −1
)ρ+σ(b −1
)ρ,

donde a = ( n
i ), b = ( n
j ), c = ( n- i
n-j ) y ρ = n−j
d , σ = j − i
d , con d = m.c.d.
(n−j, j −i
).

Demostraci´on. Una eventual soluci´on (p, q)̸=(0, 0) para el sistema de ecuaciones H [i] = H [j ] = 0

en las dos inc´ognitas bn-j y bn-i ha de tener sus dos componentes diferentes de cero ya

que, en caso contrario, el {i, j}-polinomio correspondiente,

Pn(X) = Xn + ( n
n-j) p Xj + ( n
n-i) q Xi,

28 Cap´ıtulo 2. Problemas parciales ( y primeras respuestas)

ser´ıa en realidad un {j}-polinomio (si q = 0), o un {i}-polinomio (si p = 0) que sirve como

contraejemplo a la conjetura de Casas-Alvero; y esto, seg´un el corolario 2.2.3, es imposible.

Al sustituir dicha soluci´on (p, q) en la expresi´on que para el sistema H [i] = 0, H [j ] = 0

suministra la proposici´on 2.3.2, se obtiene:

(−1)
sr+r q j [ α ρβ σ p ρ+σ+ (−1)ρσ+σ γ ρ+σ qρ ] d = 0

(−1) r pi [ δ ρ p ρ+σ + (−1)ρσ (1 + γ )ρ qρ ] d = 0

lo cual, siendo p · q ̸= 0, se veriﬁca si y solo si se cumple

α ρβ σ p ρ+σ+ (−1)ρσ+σ γ ρ+σ qρ = 0

δ ρ p ρ+σ + (−1)ρσ (1 + γ )ρ qρ = 0;

pero esto signiﬁca que el par (p ρ+σ , q ρ) es una soluci´on no trivial del sistema lineal

homog´eneo, en las inc´ognitas u y v,

α ρβ σ u + (−1)ρσ+σ γ ρ+σ v = 0

δ ρ u + (−1)ρσ (1 + γ )ρ v = 0, (2.10)

cuya matriz de coeﬁcientes tiene determinante ∆ dado por

∆ = (−1)
ρσ[a ρ (b − c
)ρ(b − ac
)σ − (−1)σ(a −1)ρ+σ(b −1)ρ], (2.11)

puesto que es: α = b −c, β = b −ac, γ = a −1 y δ = b −1.

En resumen, se tiene:

(p, q) ̸= (0, 0) es soluci´on de H [i] = H [j ] = 0 ⇐⇒

⇐⇒ (p, q), con p · q ̸= 0, es soluci´on de H [i] = H [j ] = 0 ⇐⇒

⇐⇒ (p ρ+σ, q ρ), con p ρ+σ· q ρ ̸= 0, es soluci´on no trivial de (2.10),

para lo cual es condici´on necesaria la anulaci´on del determinante ∆.

Por otra parte, el que se anule ∆ garantiza la existencia de una soluci´on no trivial

para (2.10) de la forma (u0, v0), aunque no excluye que sea u0·v0 = 0; quien s´ı excluye esta

posibilidad es el hecho de ser maniﬁestamente no nulos tanto δ = (n
j ) −1 como 1 + γ = (n
i ),

con lo cual, la igualdad δ ρ u0 + (−1)ρσ (1 + γ )ρ v0 = 0,

que se obtiene al sustituir dicha soluci´on en la segunda ecuaci´on del sistema (2.10), no

puede veriﬁcarse si solo una componente de (u0, v0) es distinta de cero. Finalmente, el que

sea C un cuerpo algebraicamente cerrado permite escribir u0 = p ρ+σ, v0 = q ρ para

ciertos p, q ∈ C, quedando demostrado que ∆ = 0 es condici´on tambi´en suﬁciente para

que el sistema H [i] = H [j ] = 0 admita una soluci´on (p, q) ̸= (0, 0). □

2.3 El {i, j}-problema parcial 29

Corolario 2.3.4. En cualquier grado, y para cualesquiera i, j, el {i, j}-problema de Casas-

Alvero tiene respuesta aﬁrmativa, esto es:

No existen {i, j}-contraejemplos a la conjetura de Casas-Alvero.

Demostraci´on. En aplicaci´on del teorema anterior, basta comprobar que, cualesquiera que

sean n, i, j ∈ N, con 1 ≤ i < j ≤ n −2, y siendo a = ( n
i ), b = ( n
j ), c = (n-i
n-j), se veriﬁca

a ρ (b − c
)ρ(b − ac
)σ ̸= (−1)σ(a −1)ρ+σ(b −1)ρ (2.12)

siempre que ρ y σ sean enteros positivos.

Si los dos miembros de (2.12) fueran iguales, se tendr´ıa que a divide a b−1 y es, por

tanto, primo con b. Pero, bajo las condiciones dadas, a = ( n
i ) y b = ( n
j ) nunca pueden ser

primos entre s´ı, como muestra la igualdad

( n
i
 )( n−i
n−j
 ) = ( n
j
 )( j
i
 ) (2.13)

(ver comentario 2.3.5). El n´umero a = ( n
i ) divide, obviamente, al producto de la derecha

en (2.13); y es estrictamente mayor que el factor ( j
i ) dado que es n > j. As´ı pues, necesa-

riamente alguno de los factores primos de a debe encontrarse alojado en ( n
j ). Esto prueba

(2.12), y concluye la demostraci´on. □

Notemos que la demostraci´on anterior admite el siguiente enfoque: Se concluye que

la desigualdad (2.12) es cierta porque dicha desigualdad se veriﬁca m´odulo p, siendo p el

factor primo com´un de a y b antes aludido.

Comentario 2.3.5. La igualdad (2.13) puede comprobarse f´acilmente desarrollando am-

bos miembros; sin embargo resulta m´as sencillo e interesante establecerla mediante un

razonamiento de tipo combinatorio.

Consideremos un conjunto A de cardinal n en el que se quiere formar un subconjunto

B de cardinal j, dentro del cual se desea destacar un subsubconjunto C de cardinal i

(recu´erdese que es n > j > i ≥ 1). Al imaginar que dentro del diagrama de Euler-Venn

de A incluimos el de B y en este el de C, a modo de diana, se visualiza inmediatamente

que esta acci´on equivale a partir al conjunto A en los tres subconjuntos disjuntos A∖B,

B ∖C y C, de cardinales respectivos n−j, j −i, i. Para el recuento de las conﬁguraciones

distintas que pueden obtenerse, se presentan dos alternativas:

Multiplicar el n´umero de subconjuntos C ⊂ A diferentes, por el n´umero de particiones

en dos piezas de tama˜no j −i y n−j , respectivamente, que pueden hacerse en A∖C.

o bien, simplemente,

30 Cap´ıtulo 2. Problemas parciales ( y primeras respuestas)

Multiplicar el n´umero de posibles subconjuntos B ⊂ A por el n´umero de posibles

sub-subconjuntos C ⊂ B.

Al igualar los dos resultados se obtiene justamente (2.13), expresi´on que, de hecho, admite

24 variantes puramente formales, como por ejemplo
( n
n−i
 )( n−i
n−j
 ) = ( n
n−j
 )( j
i
 ). (2.14)

Bajo una u otra forma, esta igualdad ser´a utilizada reiteradamente en la demostraci´on

de resultados que son clave en el desarrollo de esta Memoria; as´ı ocurre en la proposici´on

3.3.4, el lema 4.1.3 y el teorema 5.2.2.

2.4. Viabilidad del empleo de bases de Gr¨obner

En la secci´on 1.3.2 qued´o expuesto c´omo el problema total de Casas-Alvero de grado n se
transforma en el problema de averiguar si es falsa o verdadera la aﬁrmaci´on

Para cada k = 2,. . . , n−1, bk ∈ Rad
(〈H [1], H [2], . . . , H [n-2]〉) ⊂ C[
b2, . . . , bn-1]
,

o, equivalentemente, si es falsa o verdadera la aﬁrmaci´on

Para cada k = 2,. . . , n−1, 1 ∈ ̃Ik :=〈H [1], H [2], . . . , H [n-2], 1−zbk〉 ⊂ C[
b2, . . . , bn-1, z]
. (2.15)

Posteriormente, en la secci´on 1.3.3, se muestra c´omo la obtenci´on para cada ideal ̃Ik
de una base de Gr¨obner Bk zanja la cuesti´on acerca de (2.15) —y, en consecuencia, el

problema de Casas-Alvero de grado n— puesto que

1 ∈ ̃Ik ⇐⇒ El elemento 1 se encuentra en Bk.

Previa elecci´on de un orden monomial para C[
b2, . . . , bn-1, z]
, la b´usqueda de la base

de Gr¨obner Bk consiste en aplicar el algoritmo de Buchberger al sistema de generadores
{H [1], H [2], . . . , H [n-2], 1 −zbk}; empleando software espec´ıﬁco para esta tarea puede pro-

cederse con valores sucesivos n = 4, n = 5, etc. mientras no se rebase la capacidad del sis-

tema inform´atico, cosa que con los medios actuales sucede con valores de n muy peque˜nos.1

Pero, m´as all´a de cuantos casos particulares permita solventar, interesa valorar si este

procedimiento ofrece alguna posibilidad de avance en el caso general, esto es, con n gen´eri-

co. Como piedra de toque para el procedimiento nos sirve el {i, j}-problema parcial de

grado n, de diﬁcultad acotada y cuya respuesta ya conocemos.

1En el momento de redactar esta Memoria, los primeros valores de n para los que no se conoce una

prueba conceptual de la conjetura son n = 12 y n = 20. Recientemente en 2012 la conjetura ha sido estable-

cida para n = 12 a trav´es de una computaci´on que, utilizando medios de altas prestaciones, ha consumido

varias semanas en la realizaci´on de los c´alculos, similares aunque alternativos al algoritmo de Buchberger,

precedidos de diversas reducciones o simpliﬁcaciones. Para n = 20 el c´alculo requerido parece actualmente

inabordable.

2.4 Viabilidad del empleo de bases de Gr¨obner 31

Todo lo dicho al inicio de esta secci´on se adapta de forma obvia a un {i, j}-problema de

grado n, que, en consecuencia, se reduce a determinar si es verdadero o falso lo siguiente:

bn-j, bn-i ∈ Rad
(〈H [i], H [j ]〉) ⊂ C[
bn−j, bn-i]
, (2.16)

o, equivalentemente, lo siguiente:

1 ∈ ̃In-j :=〈H [i], H [j ], 1 −zbn-j〉, 1 ∈ ̃In-i :=〈H [i], H [j ], 1 −zbn-i〉, (2.17)

bien entendido que los ideales ̃In-j, ̃In-i, lo son del anillo C[
bn-j, bn-i, z] dado que, como

venimos haciendo, prescindimos de las indeterminadas bk con k ̸= n−j , n−i, nulas por

deﬁnici´on en todo {i, j}-polinomio.

Ahora bien, al demostrar el teorema 2.3.3 se razon´o suﬁcientemente que el sistema

H [i] = 0, H [j ] = 0 en las inc´ognitas bn-j, bn-i posee alguna soluci´on (p, q) distinta de la

trivial si y solo si (p, q) es una soluci´on no trivial del sistema

α ρβ σ b ρ+σ
n-j + (−1)ρσ+σ γ ρ+σ b ρ
n-i = 0

δ ρ b ρ+σ
n-j + (−1)ρσ (1 + γ )ρ b ρ
n-i = 0. (2.18)

Si llamamos G[i] y G[j ], respectivamente, a los primeros miembros de las igualdades en

(2.18) —que, observemos, aparec´ıan (con exponente d) en las expresiones de H [i] y H [j ]

dadas por la proposici´on 2.3.2—, entonces tenemos que

V (⟨H [i], H [j ]⟩
) = V (⟨G[i], G[j ]⟩
),

de modo que el sistema G[i] = G[j ] = 0 puede reemplazar, a todos los efectos —en particular,

en la reducci´on de la conjetura de Casas-Alvero a los enunciados (2.16) y (2.17)— al inicial

sistema H [i] = H [j ] = 0. Concluimos que el {i, j}-problema se reduce a averiguar si es o no

cierta la siguiente aﬁrmaci´on:

1 ∈ ̃Jn-j :=〈G[i], G[j ], 1 −zbn-j〉, 1 ∈ ̃Jn-i :=〈G[i], G[j ], 1 −zbn-i〉, (2.19)

la cual sustituye ventajosamente a (2.17) por la mayor simplicidad de los polinomios que

intervienen.

Se trata ahora de comprobar si las bases de Gr¨obner de estos dos ideales contienen al

polinomio unidad.

Fijamos, pues, un orden monomial en C[
bn-j, bn-i, z]
, que supondremos otorga mayor

orden a b ρ+σ
n-j que a b ρ
n-i. En aplicaci´on del algoritmo de Buchberger, ser´a necesario (en

ambos casos) calcular el S-polinomio de G[i] y G[j ] , pero

S(G[i], G[j ]) = (−1)ρσ [(−1)σ δ ρ γ ρ+σ − (1 + γ )ρ α ρ β σ] b ρ
n-i

32 Cap´ıtulo 2. Problemas parciales ( y primeras respuestas)

= −(−1)
ρσ [a ρ (b − c
)ρ (b − ac
)σ − (−1)σ (a −1
)ρ+σ (b −1
)ρ] b ρ
n-i

= −∆ b ρ
n-i

(se ha utilizado aqu´ı la notaci´on del teorema 2.3.3). En particular, ∆, introducido en (2.11),

es el valor del determinante cuya anulaci´on equivale a la existencia de {i, j}-contraejemplos

a la conjetura de Casas-Alvero, y cuyo an´alisis (con la conclusi´on ﬁnal de que ∆ nunca es

nulo) constituye la demostraci´on del corolario 2.3.4, que da la respuesta (aﬁrmativa) de

todo {i, j}-problema.

La cuesti´on de si ∆ es o no distinto de cero, que fue clave en la resoluci´on directa del

{i, j}-problema, aparece como un obst´aculo que es necesario superar para continuar con

el algoritmo de Buchberger. (Dicho sea de paso, una vez establecido que es ∆ ̸= 0, resulta

inmediato que tanto b ρ
n-i como G[i] −(−1)ρσ+σ γ ρ+σ b ρ
n-i = αρ β σb ρ+σ
n-j pertenecen al ideal

⟨G[i], G[j ]⟩ y, por tanto, bn-i, bn-j ∈ Rad
(〈G[i], G[j ]〉), aﬁrmaci´on equivalente a (2.19)).

Probar con otro orden monomial diferente que esta vez diera prioridad al monomio

b ρ
n-i no permitir´ıa soslayar dicha cuesti´on, pues en ese caso se obtendr´ıa

S(G[i], G[j ]) = ∆ b ρ+σ
n-j .

Cabe preguntarse, por ´ultimo, si la presencia del factor ∆ ( y la obstrucci´on que supone)

no ser´a consecuencia de haber empleado los polinomios G[i] y G[j ] en lugar de los debidos

H [i] y H [j ]. Pero, si escribimos (en notaci´on simpliﬁcada)

G[i] = A b ρ+σ
n-j + B b ρ
n-i , G[j ] = C b ρ+σ
n-j + D b ρ
n-i ,

entonces se tiene que

H [i] = M (A b ρ+σ
n-j + B b ρ
n-i) d , H [j ] = N (C b ρ+σ
n-j + D b ρ
n-i) d ,

y puede comprobarse que el S-polinomio de H [i] y H [j ], mucho m´as aparatoso que el de

G[i] y G[j ], lleva como supuesto t´ermino l´ıder al monomio (b ρ+σ
n-j )d-1 · b ρ
n-i precedido del

coeﬁciente
 d M N Ad-1C d-1(CB − AD) = −d M N Ad-1C d-1∆,

de modo que el persistente obst´aculo que ∆ origina no es atribuible a la preparaci´on

anterior.

La conclusi´on de todo ello es, por tanto, que el m´etodo de las bases de Gr¨obner se

encuentra bloqueado por diﬁcultades de ´ındole no computacional sino aritm´etica, cuya

resoluci´on equivale a la del propio problema de Casas-Alvero.

Cap´ıtulo 3

Usando esquemas proyectivos

Se considera el anillo de polinomios Z[z1, . . . , zm] graduado mediante la asignaci´on de pesos

enteros w1, w2, . . ., wm a sus indeterminadas, y se toman F1, F2, . . ., Fr ∈ Z[z1, . . . , zm], poli-

nomios homog´eneos respecto de dichos pesos. En tales condiciones, el sistema de ecuaciones

F1(z1, . . . , zm) = 0
...
Fr(z1, . . . , zm) = 0
 


 (3.1)

tiene la particularidad siguiente: cualquiera que sea el cuerpo K, si α = (α1, . . . , αm) ∈ Km

es una soluci´on del sistema, entonces la m-upla λα = (λw1α1, λw2α2, . . . , λwm αm) es igual-

mente soluci´on del mismo sistema, para todo λ ∈ K−{0}. Identiﬁcando entre s´ı todas

las m-uplas de la forma λα se constituye un punto [α] del espacio proyectivo pesado

P m−1
w1,. . . ,wm(K) = (Km−{¯0}
)/∼ . Tiene, por tanto, sentido construir un funtor asociado al

sistema (3.1), concretamente, el funtor

Y : {Cuerpos conmutativos} ⇝ {Conjuntos
}

que sobre los objetos viene dado por

Y (K) = { [α] ∈ P m−1
w1,. . . ,wm(K) | F1(α) = F2(α) = . . . = Fr(α) = 0}
;

esto es, Y( K) recoge aquellos puntos [α] del correspondiente espacio proyectivo pesado

tales que cada uno de sus representantes λα es una soluci´on del sistema de ecuaciones.

En esta Memoria (y por abuso de lenguaje) llamaremos esquema proyectivo pesado

al funtor Y , si bien a lo que ese nombre propiamente designa es a una determinada

extensi´on —que se deﬁne tambi´en a partir del sistema (3.1)— del funtor Y a la categor´ıa

de anillos conmutativos; el motivo por el que obviamos dicha extensi´on es que ´unicamente

necesitaremos manejar los conjuntos Y( K) —y, aun esto, solo para ciertos cuerpos K—.

34 Cap´ıtulo 3. Usando esquemas proyectivos

M´as precisamente, los cuerpos que habremos de considerar en este trabajo son, adem´as

del cuerpo C, la clausura algebraica Q del cuerpo Q y, para cada primo p, la clausura

algebraica del cuerpo Fp = Z/(p), a la cual denotaremos por Fp. La clausura algebraica

de un cuerpo K se deﬁne como un cuerpo K que es a la vez algebraicamente cerrado y

extensi´on algebraica de K, signiﬁcando lo primero que todo polinomio de K[ X] encuentra

alguna ra´ız en K, y lo segundo, que todo elemento de K es algebraico sobre K, esto es,

ra´ız de alg´un polinomio perteneciente a K[ X]. Aunque para un cuerpo general cuanto se

sabe de su clausura algebraica es que existe y es ´unica salvo isomorﬁsmo, en los casos

mencionados de K = Q y de K = Fp se dispone de un conocimiento m´as espec´ıﬁco de la

misma.

En el caso de Q, el hecho de disponer de C, que es un supracuerpo para Q con el que

estamos largamente familiarizados, facilita la comprensi´on de Q como el subconjunto de

C formado por los elementos que son algebraicos sobre Q. El cuerpo Q se puede tambi´en

visualizar como la uni´on de todos los cuerpos de n´umeros, es decir, de los subcuerpos K

de C que son extensiones ﬁnitas sobre Q. Decir que el cuerpo K⊂C es una extensi´on ﬁnita

de Q signiﬁca que K es un espacio vectorial de dimensi´on ﬁnita sobre Q (cuerpo al que

contiene); a dicha dimensi´on, usualmente denotada por [K : Q], se la denomina grado de

la extensi´on. En general, una extensi´on de un cuerpo es ﬁnita si y solo si tal extensi´on

est´a ﬁnitamente generada por elementos algebraicos, siendo, en consecuencia, algebraica.

En el caso de Fp, ﬁjando —en principio, de forma abstracta— una clausura algebraica,

Fp, podemos luego visualizarla como la uni´on de todos los cuerpos ﬁnitos de caracter´ıstica

p. Tales cuerpos contienen un subcuerpo isomorfo a Z/(p) = Fp, y son Fp-espacios vectoria-

les de dimensi´on necesariamente ﬁnita; por tanto, su cardinal es la potencia p r para alg´un

entero r ≥ 1. El —salvo isomorﬁsmo— ´unico cuerpo existente con p r elementos, denotado

Fpr , puede interpretarse como el subcuerpo de Fp formado por las ra´ıces del polinomio

Xpr
− X ∈ Fp [ X], que todos sus elementos no nulos satisfacen en virtud del teorema de

Lagrange (y el nulo tambi´en, trivialmente). Rec´ıprocamente, cada α ∈ Fp se encuentra en

el subcuerpo Fp [α] que, por ser ﬁnitamente generado por un elemento algebraico, es una

extensi´on ﬁnita de Fp, de modo que es un cuerpo ﬁnito y de caracter´ıstica p.

Observaci´on 3.0.1. Retornando al esquema proyectivo Y deﬁnido a partir del sistema

homog´eneo pesado (3.1): Puesto que la m-upla ¯0 ∈ Km no proporciona ning´un punto del

espacio proyectivo, la expresi´on Y( K) = ̸O equivale a decir que sobre el cuerpo K el

sistema en cuesti´on ´unicamente posee la soluci´on trivial.

Lema 3.0.2. Para el esquema proyectivo Y dado por (3.1) se tiene que la condici´on

Y(C) = ̸O es equivalente a la condici´on Y(Q) = ̸O.
 35

Demostraci´on. Puesto que toda soluci´on no trivial que el sistema (3.1) encuentre sobre el

cuerpo Q es, obviamente, una soluci´on no trivial sobre C, la implicaci´on “si Y(C) = ̸O

entonces Y(Q) = ̸O ” es inmediata.

Para probar la rec´ıproca, consideremos las parejas de ideales HC , JC de C[z1, . . . , zm]

y H
Q , J
Q de Q[z1, . . . , zm], donde HC y H
Q est´an generados por F1, . . . , Fr y JC y J
Q
est´an generados por z1, . . . , zm. Puesto que tanto C como Q son cuerpos algebraicamente

cerrados, el teorema de los ceros de Hilbert asegura que la condici´on Y(C) = ̸O equivale

a que sea Rad(HC) = Rad(JC) y que la condici´on Y(Q) = ̸O es equivalente a que sea

Rad(H
Q ) = Rad(J
Q ) —en cada caso, en el anillo de polinomios que corresponde—. Como

JC y J
Q son ideales radicales, y como —por ser los polinomios Fi homog´eneos pesados—

se tienen las inclusiones HC ⊂ JC y H
Q ⊂ J
Q , las condiciones Y(C) = ̸O y Y(Q) = ̸O son

equivalentes simplemente a que sea JC ⊂ Rad(HC) y J
Q ⊂ Rad(H
Q ), respectivamente. Pero

a su vez, estas inclusiones equivalen a la existencia de n´umeros enteros di > 0, i = 1, . . . , m

tales que zi di ∈ HC y que zi di ∈ H
Q , respectivamente. Ahora bien, al ser H
Q ⊂ HC, es claro

que zi di ∈ H
Q implica zi di ∈ HC, y por tanto, que Y(Q) = ̸O implica Y(C) = ̸O . □

La siguiente propiedad de los esquemas proyectivos nos resultar´a de extraordinaria

utilidad:

Proposici´on 3.0.3 (Schicho, Graf von Bothmer, Labs, Van de Woestijne). Sea

Y el esquema proyectivo dado por (3.1). Entonces, las siguientes condiciones son equiva-

lentes:

(i ) Para todos los primos p, excepto para un n´umero ﬁnito de ellos, Y( Fp ) es vac´ıo.

(ii ) Existe un primo p tal que Y( Fp ) es vac´ıo.

(iii ) Y(C) es vac´ıo.

Demostraci´on. Como (i) ⇒ (ii) es trivial, demostraremos las implicaciones (ii) ⇒ (iii) y

(iii) ⇒ (i).

Para demostrar (iii) ⇒ (i) consideraremos los cuerpos C y Fp, y los ideales HC y Hp
generados por F1, . . . , Fr en los anillos C[z1, . . . , zm] y Fp[z1, . . . , zm] respectivamente. Si

(iii) es cierto, entonces (ver demostraci´on del lema 3.0.2) podemos tomar enteros di > 0

tales que z di
i ∈ HC, esto es, tales que

z di
i = G1 F1 + G2 F2 + · · · + Gr Fr, para ciertos Gj ∈ C[z1, . . . , zm]. (3.2)

Tomemos ahora un subespacio vectorial T suplementario del subespacio Q en el Q-espacio

vectorial C, de modo que sea C = Q ⊕ T . Escribiendo Gj = G ′
j + G ′′
j (donde el primer su-

mando tiene todos sus coeﬁcientes en Q y el segundo en T ) la expresi´on (3.2) queda

36 Cap´ıtulo 3. Usando esquemas proyectivos

z di
i =
 r∑

j=1 G ′
j Fj +
 r∑

j=1 G ′′
j Fj,

siendo esta la ´unica manera de descomponer z di
i ∈ Q[z1, . . . , zr] en suma de dos polinomios

con coeﬁcientes, respectivamente, en Q y en T —recu´erdese que los Fj tienen sus coe-

ﬁcientes en Z—. La unicidad obliga a que sea nulo ∑ G ′′
j F j y, por tanto, a que sea

z di
i = ∑ G ′
j F j. Lo notable en esta igualdad es el hecho de saber que en la expresi´on (3.2)

los polinomios Gj no son otros que los G ′
j, y tienen coeﬁcientes racionales. Tomemos los

primos p que sean mayores que todos los denominadores de los coeﬁcientes de todos los

Gj, cuando se hace variar j = 1, . . . r y tambi´en se hace variar i = 1, . . . , m (´ındice que, por

simplicidad de notaci´on, no se reﬂeja aqu´ı). Entonces, no solamente los coeﬁcientes de los

F j —que son enteros— sino tambi´en los coeﬁcientes de los Gj, alcanzan a tener en Fp una

imagen mediante la reducci´on m´odulo p (dada, en este caso, por ϕ(a/b) := ϕ(a) · [
ϕ(b)
]−1,

siendo ϕ : Z → Z/(p) = Fp la aplicaci´on caracter´ıstica), ya que sus denominadores no

pueden ser m´ultiplo de p. De este modo obtenemos polinomios F j, Gj sobre Fp, para los

que se conserva la igualdad

z di
i = G1 F 1 + G2 F 2 + · · · + Gr F r, para ciertos F i, Gi ∈ Fp [z1, . . . , zm]. (3.3)

Esta igualdad tiene lugar, de hecho, en el anillo Fp[z1, . . . , zm], e informa de que zi pertenece

al radical de Hp. Dado que ello es as´ı para cada i = 1, . . . , r, se deduce, por el teorema de

los ceros de Hilbert sobre Fp, que es Y( Fp ) = ̸O. Este resultado se ha obtenido para todos

los primos excepto una cantidad ﬁnita, ya que los polinomios Gj reun´ıan entre todos una

cantidad ﬁnita de coeﬁcientes.

Nuestra prueba de la implicaci´on (ii) ⇒ (iii) ser´a m´as t´ecnica, y requiere el uso de anillos

de enteros de cuerpos de n´umeros, as´ı como la aplicaci´on de conocidas propiedades que a

continuaci´on se describen de forma escueta, a ﬁn de que la redacci´on de la prueba resulte

autocontenida. La justiﬁcaci´on de estas propiedades es no trivial, y puede encontrarse, por

ejemplo, en [Ser] o [Sam].

Tomemos un cuerpo de n´umeros K ⊂ C. Los elementos de K que son ra´ıces de alg´un

polinomio m´onico con coeﬁcientes en Z forman un subanillo OK de K que se denomina

anillo de enteros de K. El cuerpo de fracciones de OK es el propio K, y OK contiene

a Z. Como Z-m´odulo, OK es libre y de rango igual al grado [K : Q]. Todos los ideales

primos de OK a excepci´on del ideal (0) son ideales maximales del anillo. Si p es un

ideal maximal, entonces p ∩ Z = (p) para alg´un n´umero primo p, y se tiene que el anillo

cociente OK/p es un cuerpo ﬁnito con p r elementos para cierto r > 0. Rec´ıprocamente,

dado un primo p, existe alg´un ideal maximal p (de hecho, un n´umero ﬁnito de ellos) tal

que p ∩ Z = (p). A partir de un isomorﬁsmo entre los cuerpos ﬁnitos OK/p y Fpr —el

cual existe, pues se trata de dos cuerpos con igual n´umero de elementos— se deduce un

37

homomorﬁsmo de anillos φp : OK → Fp cuyo n´ucleo es p y cuya imagen es Fpr ; este

homomorﬁsmo ser´a utilizado como herramienta para reducir m´odulo p las coordenadas

de los puntos contenidos en Y( K). Como caso particular relevante, para K = Q se tiene

OQ = Z; los ideales maximales de este anillo son los del tipo (p), siendo p un n´umero

primo, y la aplicaci´on φ(p) : Z → Fp es la composici´on de las de reducci´on m´odulo p usual,

ϕ : Z → Z/(p) = Fp, con la de inclusi´on de Fp en Fp.

De gran utilidad resulta la existencia de una valoraci´on v p : K∖{0} → Z asociada a

cada ideal maximal p de OK. Se deﬁne en primer lugar sobre los elementos del anillo de

enteros: Dado α ∈ OK∖{0}, v p(α) := l si α ∈ pl pero α ̸∈ pl+1,

y luego se extiende a los elementos no nulos de K:

Si α, β ∈ OK∖{0}, v p( α

β ) := v p(α) − v p(β).

Es usual ampliar v p a todo K deﬁniendo v p(0) := ∞. Para cualesquiera α, β ∈ K, se

satisfacen las dos propiedades siguientes:

(1) v p(α + β) ≥ m´ın {v p(α), v p(β)
}.

(2) v p(α · β) = v p(α) + v p(β)

Los elementos τ ∈ OK con v p(τ ) = 1, que siempre existen, reciben el nombre de uni-

formizantes. Es de destacar tambi´en el conjunto de los elementos a los que la valoraci´on

les asigna una imagen no negativa, y que coincide con el localizado de OK mediante el

ideal p. Esto es, OK, p = {α ∈ K | v p(α) ≥ 0
}.

El homomorﬁsmo φp de reducci´on m´odulo p se hace extensivo al anillo local OK, p; el

n´ucleo de este homomorﬁsmo lo forman justamente los elementos α cuya valoraci´on es

estrictamente positiva.

Finalmente, si K y L son cuerpos de n´umeros con K⊂L, y si p es un ideal maximal de

OK, entonces se tiene p = q ∩ OK para alg´un ideal maximal q del anillo OL.

Probaremos ahora la implicaci´on (ii) ⇒ (iii) mostrando que si Y( Q) ̸= ̸O entonces se

tiene Y( Fp ) ̸= ̸O para todo primo p; hecho que, a la vista del lema 3.0.2, deja zanjada la

cuesti´on.

Si Y( Q) ̸= ̸O entonces existe alguna soluci´on α = (α1, . . . , αm) ∈ Qm del sistema (3.1)

tal que αj ̸= 0 para al menos un ´ındice j. Como cada componente αi es algebraica sobre

Q, existen cuerpos de n´umeros que contienen a α1, . . . , αm simult´aneamente. Tomemos

uno de ellos, K, y consideremos en su anillo de enteros OK un ideal maximal p tal que

sea p ∩ Z = (p). Escribiendo cada αi como cociente de dos elementos de OK y tomando

38 Cap´ıtulo 3. Usando esquemas proyectivos

como λ el producto de los denominadores obtenidos, se consigue una nueva soluci´on del

sistema (3.1), λα = (λw1α1, . . . , λwmαm), que deﬁne el mismo punto [α] del espacio proyec-

tivo P m−1
w1,. . . ,wm(Q) pero cuyas coordenadas λwiαi se encuentran en OK. As´ı, sin p´erdida

de generalidad, podemos suponer directamente que αi ∈ OK para todo i.

Ahora, si se tuviese v p(αi) = 0 (es decir, α ̸∈ p) para alg´un i, entonces, por reducci´on

m´odulo p se tendr´ıa que (φp(α1), . . . , φp(αm)
) ser´ıa una soluci´on de (3.1) sobre Fp con

φp(αi) ̸= 0 para ese mismo i, y por tanto Y( Fp ) ser´ıa no vac´ıo. Sin embargo, como pudiera

suceder que fuera v p(αi) > 0 para todo i, necesitamos pasar a otro cuerpo de n´umeros

mayor que K sobre el que poder elegir un nuevo representante del punto [α] que ya no

presente ese tipo de problema.

A tal prop´osito, deﬁnimos el n´umero racional

x = m´ın { v p (α1)
w1 , v p (α2)
w2 , . . . , v p (αm)
wm
 } (3.4)

(x es siempre ﬁnito: alg´un v p(αi) pudiera ser ∞, pero todos, no, ya que hay un αj ̸= 0), y

escribimos x = c
d con c, d enteros y d > 0. Tomamos un uniformizante τ ∈OK y un n´umero

complejo µ tal que µd = τ . Puesto que µ es algebraico sobre K, podemos tomar un nuevo

cuerpo de n´umeros L que contenga a K y a µ. Tomemos ahora un ideal maximal q del

anillo de enteros OL veriﬁcando la igualdad q ∩ OK = p. Es f´acil comprobar que se cumple

Si α ∈ K, α ̸= 0, entonces v q(α) = d · v p(α) · v q(µ);

ello es consecuencia del hecho siguiente: Si v p(α) = v, α ̸= 0, entonces α se puede escribir

en la forma α = τ v · β
γ , con β, γ ∈ OK y β, γ ̸∈ p.

esto es, α = µ d · v · β
γ , con β, γ ∈ OL y β, γ ̸∈ q.

Consideramos ahora la soluci´on de (3.1) dada por λα = (λw1α1, . . . , λwmαm) cuando se

toma λ = µ−c ∈ L. Las componentes de esta m-upla se encuentran, de hecho, en el anillo

local OL,q, pues, en efecto,

v q(λwiαi) = v q(µ) · ( − wi · c + v p(αi) · d ) ≥ 0, para todo i = 1, . . . m;

pero adem´as sabemos con certeza que se cumple la igualdad v q(λwiαi) = 0 para al menos

uno de los ´ındices(aquel o aquellos i tales que el cociente v p (αi)
wi , por ser m´ınimo, coincida

precisamente con x = c
d seg´un fue deﬁnido en (3.4)). As´ı pues, no solamente es cierto que

la reducci´on m´odulo q de cada componente de esta soluci´on est´a deﬁnida, sino que adem´as

alguna es no nula, de modo que la r-upla

( φq(λw1 α1), φq(λw2 α2), . . . , φq(λwr αr) )

3.1 Esquemas asociados a los problemas total y parcial 39

determina en efecto un punto del espacio proyectivo P m−1
w1,. . . ,wm(Fp) perteneciente a Y( Fp ).

Nota 3.0.4. La demostraci´on de la proposici´on anterior esquiva el lenguaje y la teor´ıa

abstracta de esquemas. La prueba de Schicho, Graf von Bothmer, Labs y Van de Woestijne

en [BLSW] es no constructiva, y requiere formular resultados especializados de la teor´ıa de

esquemas que se ha considerado innecesario introducir en esta Memoria. Nuestra prueba,

por su parte, requiere utilizar las propiedades de los anillos de enteros de cuerpos de

n´umeros —teor´ıa tambi´en especializada, pero m´as apropiada para un p´ublico general—,

y presenta adem´as la particularidad de ser constructiva.

Nota 3.0.5. Cuando para cada cuerpo K se tenga que Y( K) es vac´ıo, diremos que el

esquema Y carece de entidad geom´etrica. Un ejemplo de esta situaci´on se obtiene si en

(3.1) se toma r = m ≥ 1 y Fj = z lj
j siendo lj > 0 un entero para cada j = 1, . . . , m. Otro

ejemplo se obtiene si se toma m = 0, es decir, si no se considera ninguna variable, ya

que entonces Y( K) es vac´ıo por serlo formalmente el espacio proyectivo (−1)-dimensional

(raz´on por la que ese espacio no se deﬁne en geometr´ıa).

La demostraci´on del lema 3.0.2 puede adaptarse sin ning´un cambio esencial al caso de

caracter´ıstica p ≥ 0 para probar que si K es un cuerpo algebraicamente cerrado de carac-

ter´ıstica p > 0 (resp. p = 0) entonces Y( K) es vac´ıo si y solo si Y( Fp ) es vac´ıo (resp. Y( Q)

es vac´ıo). De ello se deduce que el esquema proyectivo Y carece de entidad geom´etrica si

y solo si Y( Q) es vac´ıo e Y( Fp ) es vac´ıo para todo primo p ; o, equivalentemente, si Y( C)

es vac´ıo e Y( Fp ) es vac´ıo para todo primo p. Como adem´as el teorema 3.0.3 muestra que

la condici´on Y( C) = ̸O es aqu´ı superﬂua, concluimos que el esquema proyectivo Y carece

de entidad geom´etrica si y solo si se tiene Y( Fp ) = ̸O para todo primo p.

3.1. Esquemas proyectivos asociados a los problemas de Casas-

Alvero total y parcial

Sea de nuevo el polinomio Pn(X) = Xn + ( n
2 )b2 Xn-2 + . . . + ( n
n-i)bn-i Xi + . . . + ( n
n-1)bn-1 X

y, para cada i = 1, 2, . . . , n−2, su derivada neta i-´esima, Pn
[i](X), as´ı como la resultante

H [i] = Res(P n , P [i]
n ). Recordemos que en el anillo Z[b2, . . . , bn−1], graduado mediante la

asignaci´on de pesos dada por gr(bk) := k, todos los polinomios H [i] son homog´eneos.

Denotaremos por Yn al esquema proyectivo pesado deﬁnido por las ecuaciones

H [1] = H [2] = . . . = H [n-2] = 0 .

40 Cap´ıtulo 3. Usando esquemas proyectivos

Por otra parte, para cada conjunto de exponentes I = {i1, . . . , ir} ⊂ J = {1, 2, . . . , n−2}, de-

notaremos por Z n,I al esquema proyectivo pesado deﬁnido por las ecuaciones

H [i1 ] = H [i2 ] = . . . = H [ir ] = 0 ; bn-j = 0, ∀j ∈ J ∖I.

Obs´ervese que se trata del sistema que deﬁne el I-problema de Casas-Alvero, bien en-

tendido que, en este contexto, se mantiene a las n−2 indeterminadas bk como inc´ognitas

presentes en el sistema —sin prescindir de las bn-j, expresamente obligadas a ser nulas—,

de modo que todo Z n,I es un subesquema del espacio proyectivo pesado (n-3)-dimensional,

en su acepci´on de esquema.

Observaci´on 3.1.1. Cualquiera que sea el cuerpo K, se veriﬁca

I ⊂ I ′ ⊂ J = {1, 2, . . . , n−2} =⇒ Zn,I ( K) ⊂ Zn,I ′( K) ⊂ Yn( K).

En efecto, basta recordar que, seg´un se vio en la observaci´on 2.1.1, para cada i ∈ J se

cumple: bn-i = 0 ⇒ H [i] = 0 (o, equivalentemente, bn-i divide al polinomio H [i]) y tener

presente que, siendo I = {i1, . . . , ir}, I ′ ∖ I = {k1, . . . , ks}, J ∖ I ′ = {j1, . . . , jt}, entonces

• Z n,I est´a deﬁnido por el sistema
 



 H [i1 ] = · · · = H [ir ] = 0

bn-k1 = · · · = bn-ks = 0

bn-j1 = · · · = bn-jt = 0,

mientras que

• Z n,I ′ est´a deﬁnido por el sistema
 



 H [i1 ] = · · · = H [ir ] = 0

H [k1 ] = · · · = H [ks ] = 0

bn-j1 = · · · = bn-jt = 0

y, el esquema Yn , por el sistema H [1] = H [2] = . . . = H [n-2] = 0.

M´as precisamente, ﬁjado un cuerpo K, los conjuntos Zn,I ( K), Zn,I ′( K) y Yn( K)

son justamente las variedades proyectivas del espacio proyectivo pesado P n−3
2,3,. . . ,n-1(K)

determinadas, respectivamente, por los ideales
〈 H [i1 ] , . . . , H [ir ]; bn-k1 , . . . , bn-ks ; bn-j1 , . . . , bn-jt 〉,
〈 H [i1 ] , . . . , H [ir ] ; H [k1 ] , . . . , H [ks ] ; bn-j1 , . . . , bn-jt 〉,
〈 H [1] , H [2] , . . . , H [n-2] 〉;

las evidentes relaciones de inclusi´on que se dan entre estos ideales signiﬁcan que el esquema

Z n,I es un subesquema de Z n,I ′, y que ambos lo son de Yn.

En los problemas de Casas-Alvero, lo mismo en su forma total que en todas sus formas

parciales, la tesis del enunciado podr´a ser caracterizada muy n´ıtidamente empleando los

esquemas que acabamos de deﬁnir.

3.1 Esquemas asociados a los problemas total y parcial 41

Proposici´on 3.1.2. (a) La conjetura de Casas-Alvero es verdadera para grado n si y

solo si Yn(C) = ̸O, esto es, si el esquema proyectivo Yn carece de puntos sobre C.

(b) El problema parcial de Casas-Alvero en grado n y con exponentes en I tiene respuesta

aﬁrmativa si y solo si Zn,I (C) = ̸O.

Demostraci´on. (a) Es claro, puesto que ambas cosas equivalen a que ¯0 = (0, . . . , 0) sea

la ´unica soluci´on sobre C del sistema homog´eneo H [1] = H [2] = . . . = H [n-2] = 0 ; por el

contrario, la eventual existencia de una soluci´on no trivial del mismo, β = (β2, . . . , βn−1) ∈

Cn-2, signiﬁcar´ıa simult´aneamente que el polinomio

Pn,β(X) = Xn + ( n
2 )β2 Xn-2 + . . . + ( n
n-i)βn-i Xi + . . . + ( n
n-1)βn-1 X

es un contraejemplo a la conjetura de Casas-Alvero en grado n, y que Yn(C) contiene por

lo menos al punto [β ].

(b) Este hipot´etico contraejemplo al problema total ser´ıa un I-contraejemplo si y solo

si fueran nulas las componentes de β ubicadas en ciertas posiciones preﬁjadas (y esto le

pasar´ıa a λβ, para todo λ ∈ C), por lo que el punto [β ] estar´ıa de hecho en Zn,I (C). □

Observaci´on 3.1.3. Dado que el conjunto completo de exponentes, J = {1, 2, . . . , n−2}, es

subconjunto de s´ı mismo, entre los esquemas de tipo Z n,I se encuentra el esquema Z n,J ,

que en nada se diferencia de Yn. Podemos convenir, pues, en considerar al problema total

de Casas-Alvero como uno m´as de los problemas parciales, y tratar conjuntamente todos

ellos. Emplearemos la notaci´on Yn, espec´ıﬁca del problema total, cuando sea preciso poner

´enfasis en que nos referimos a dicho caso.

Podemos ya formular una condici´on suﬁciente para que un I-problema parcial de Casas-

Alvero de grado n tenga respuesta aﬁrmativa.

Proposici´on 3.1.4. Si existe un primo p tal que Zn,I ( Fp ) = ̸O, entonces la conjetura de

Casas-Alvero en grado n no admite ning´un I-contraejemplo. En particular, si Yn( Fp ) = ̸O,

entonces dicha conjetura es verdadera para el grado n.

Demostraci´on. Si, para determinado primo p, Zn,I ( Fp ) = ̸O (resp. Yn( Fp ) = ̸O) entonces,

en virtud de la proposici´on 3.0.3 se tendr´a que Zn,I (C) = ̸O (resp. Yn(C) = ̸O); basta

ahora aplicar la proposici´on 3.1.2. □

La anterior proposici´on se destaca por las posibilidades operativas que ofrece, pero

sucede adem´as que tambi´en es cierto su rec´ıproco, como igualmente se desprende de 3.0.3.

Se tiene entonces un nuevo enunciado equivalente para la conjetura de Casas-Alvero:

42 Cap´ıtulo 3. Usando esquemas proyectivos

Conjetura de Casas-Alvero. Sea Yn el subesquema proyectivo del espacio proyectivo

pesado P n−3
2,3,. . . ,n-1 deﬁnido por las ecuaciones H [1] = H [2] = . . . = H [n-2] = 0. Se veriﬁca

lo siguiente: Existe alg´un n´umero primo p tal que Yn( Fp ) = ̸O.

3.2. La reducci´on m´odulo p

Habida cuenta de la relevancia que acaba de tomar el conjunto Zn,I ( Fp ), procede intere-

sarse por la naturaleza y el signiﬁcado de sus elementos.

La construcci´on de los esquemas Z n,I se ha regido por un discurso —sobre polinomios,

derivadas y ra´ıces compartidas— desarrollado siempre bajo el supuesto de encontrarnos

trabajando sobre C, y por tanto en caracter´ıstica cero. As´ı se obtienen las ecuaciones

H [k ] = 0 (en n −2 inc´ognitas y con coeﬁcientes enteros); ahora bien, una vez ﬁjadas, son

ellas solas quienes deﬁnen por s´ı mismas el esquema.

Para ahora estudiar las soluciones sobre Fp de dichas ecuaciones ser´a muy ´util recupe-

rar, en lo posible, el signiﬁcado original de las mismas. Esta es una tarea delicada que

exige comprobar cuidadosamente cada detalle.

En lo que sigue, consideraremos ﬁjados el grado n y un primo p; I = {i1, . . . , ir}, por

su parte, ser´a un determinado conjunto de exponentes.

Notaci´on. Dado Pn(X) = Xn + ∑

i∈I
 ( n
n-i)bn-i Xi, denotaremos como Pn(X) al polinomio

reducido m´odulo p de Pn(X), esto es,

Pn(X) = Xn + ∑

i∈I
 ( n
n-i) bn-i Xi,

donde ( n
n-i) denota la imagen del n´umero combinatorio ( n
n-i) mediante la aplicaci´on carac-

ter´ıstica ϕ : Z → Z/(p). Obs´ervese que las bn-i permanecen como indeterminadas.

Del mismo modo, para cada k = 1, . . . , n −2, escribiremos

Pn
[k ](X) = Xn-k + ∑

i∈I
i≥k
 (n-k
n-i) bn-i Xi-k,

y tambi´en
 H [k ] = Res( P n, P n
[k ]) ∈ Z/(p)[
b2, . . . , bn-1]
.

Lema 3.2.1. La ecuaci´on H [k ] = 0 admite como soluci´on sobre Fp a la (n−2)-upla β =

(β2, . . . , βn−1) ∈ Fp n-2 si y solo si los dos polinomios

Pn,β (X) = Xn + n−2∑

i = 1
 ( n
n-i) βn-i Xi y Pn,β
[k ](X) = Xn-k + n-2∑

i=1
 (n-k
n-i) βn-i Xi-k,

pertenecientes a Fp[ X], comparten una ra´ız en Fp.

3.2 La reducci´on m´odulo p 43

Demostraci´on. El valor H [k ](β) ∈ Fp es, por construcci´on, igual a la resultante de los

polinomios

Pn,β (X) = Xn + n−2∑

i = 1
 ( n
n-i) βn-i Xi y Pn,β
[k ](X) = Xn-k + n- 2∑

i=1
 (n-k
n-i) βn-i Xi-k

bajo el supuesto de que sus grados son, respectivamente, n y n−k. Esta suposici´on es, en

ambos, casos, correcta (lo garantiza el hecho de ser polinomios formalmente m´onicos: el

coeﬁciente 1 no es nulo en ninguna caracter´ıstica). Entonces, de acuerdo con lo expuesto en

la secci´on 1.3, la anulaci´on de H [k ](β) es condici´on necesaria y tambi´en suﬁciente para que

los polinomios Pn,β (X) y Pn,β
[k ](X) compartan alguna ra´ız en el cuerpo algebraicamente

cerrado Fp.

Ahora bien, en la Z-´algebra Fp, multiplicar por un factor entero h consiste justamente

en multiplicar por el n´umero ϕ(h)∈Z/(p) = Fp, de modo que, desde cualquier punto de vista,

Pn,β (X) es el mismo polinomio que Pn,β (X), as´ı como Pn,β
[k ](X) es el mismo polinomio

que Pn,β
[k ](X). Por tanto, el que (β2, . . . , βn−1) ∈ Fp n-2 satisfaga la ecuaci´on H [k ] = 0 tiene

exactamente el signiﬁcado que le otorga el enunciado del lema. □

Observaci´on 3.2.2. Por la misma raz´on, el valor H [k ](β) = Res( Pn,β , Pn,β
[k ]) ∈ Fp es

id´entico al valor H [k ](β) = Res( Pn,β , Pn,β
[k ] ) . As´ı que, trat´andose de determinar el con-

junto de puntos Zn,I ( Fp ), la ecuaci´on H [k ] = 0 es indistinguible de H [k ] = 0 .

Comentario 3.2.3. Los polinomios reducidos m´odulo p, Pn(X) y Pn
[k ](X), son redun-

dantes con Pn(X) y Pn
[k ](X); en efecto, cuando se les especializa en un punto (β2, . . . , βn-1) ∈

Fp n-2, unos y otros proporcionan iguales resultados. Ahora bien, el hecho de disponer de

ellos como objetos formales distintos de sus an´alogos sin reducir aportar´a claridad en

posteriores razonamientos.

Comentario 3.2.4. Del lema precedente se sigue que, ciertamente, el sistema de ecua-

ciones H [i1 ] = H [i2 ] = . . . = H [ir ] = 0 (siendo bn-k = 0 ∀j ∈ J ∖ I) recoge las condiciones

necesarias y suﬁcientes para que un polinomio de la forma

Pn(X) = Xn + ∑

i∈I
 ( n
n-i) bn-i Xi, con bn-i ∈ Fp,

comparta en Fp una ra´ız con cada uno de los polinomios

Pn
[1](X) , Pn
[2](X) , . . . , Pn
[n-2](X).

Sin embargo, los Pn
[k ](X) no admiten una interpretaci´on obvia como derivadas sucesivas

de Pn(X) (al menos, cuando p ≤ n), pues en caracter´ıstica p el concepto de derivada pierde

44 Cap´ıtulo 3. Usando esquemas proyectivos

consistencia. En efecto, con la derivada habitual, la incorporaci´on de factores procedentes

del exponente convierte en nulos algunos de los t´erminos del resultado (de hecho, la deriva-

da de orden p ser´a el polinomio nulo); en el caso de las derivadas de Hasse y netas, adem´as,

la eliminaci´on de factores producida por la divisi´on ocasiona la eventual reaparici´on de

t´erminos al derivar sucesivamente. El siguiente ejemplo muestra lo err´atico que puede ser

este comportamiento:

Consideramos el polinomio P(X) = X6 + X5 ∈ F2[ X]. En caracter´ıstica 2,

P ′(X) = 6 X 5 + 5 X 4 = X 4

P ′′(X) = 4 X 3 = 0.

Si decidimos emplear la derivada de Hasse, entonces:

P <1>(X) = 6 X 5 + 5 X 4 = X 4

P <2>(X) = 15 X 4 + 10 X 3 = X 4

P <3>(X) = 20 X 3 + 10 X 2 = 0

P <4>(X) = 15 X 2 + 5 X = X 2 + X

P <5>(X) = 6 X + 1 = 1.

La derivada neta, en este caso, ni siquiera puede ser utilizada ya que ser´ıa

P [1](X) = 1

6 · (6 X 5 + 5 X 4) = X5 + 5

6 X4,

lo cual carece de sentido en caracter´ıstica 2. En realidad, la derivada neta solo est´a deﬁnida

para aquellos polinomios que admitan ser escritos en presentaci´on bin´omica, esto es,

P6(X) = X6 + ( 6
1 )b1 X5 + ( 6
2 )b2 X4 + · · · , lo cual no sucede en este ejemplo ya que en F2 la

igualdad ( 6
1 )b1 = 1 es imposible.

Incluso en los casos en que la derivada neta est´a deﬁnida, no est´a bien deﬁnida. Como

ejemplo, en caracter´ıstica 5 se tiene el polinomio P(X) = X5; como este polinomio coin-

cide con P5(X) = X5 + ( 5
1 )b1 X4 + ( 5
2 )b2 X3 + ( 5
3 )b3 X2 + ( 5
4 )b4 X cualesquiera que sean los

valores que se d´e a las indeterminadas bk, ocurrir´a que

P [1](X) = X4 + ( 4
1 )b1 X3 + ( 4
2 )b2 X2 + ( 4
3 )b3 X + ( 4
4 )b4 =

= X4 + 4 b1 X3 + b2 X2 + 4 b3 X + b4,

de modo que la derivada neta de P(X) = X5 coincide con una inﬁnidad de polinomios

distintos.

Naturalmente, nada de esto ocurr´ıa en caracter´ıstica cero, donde la aplicaci´on K-lineal

L0 : K n −→ K[X]<n

(b1, . . . , bn) ↦−→ n∑

i=1
 ( n
i ) bi X n-i

3.3 Eliminaci´on de monomios m´odulo p 45

es biyectiva, y por tanto todo polinomio m´onico de grado n admite una presentaci´on

bin´omica que adem´as es ´unica. De ese modo, la aplicaci´on K-lineal que a cada polinomio

de K[X]<n le env´ıa a su derivada neta de orden k puede factorizarse a trav´es de K n

usando Lk : K n −→ K[X]<n−k

(b1, . . . , bn) ↦−→ n−k∑

i=1
 ( n-k
i ) bi X n-i-k,

con lo cual queda bien deﬁnida en K[X]<n.

En caracter´ıstica p podemos simular este buen comportamiento si, en vez de trabajar

con el concepto de polinomio, lo hacemos con un nuevo concepto, al que denominaremos

polinomio presentado. Un polinomio presentado Pn(X) es un polinomio que admite pre-

sentaci´on bin´omica y para el que se ha ﬁjado (como estructura adicional a la de polinomio)

una presentaci´on bin´omica concreta que hace expl´ıcito el valor de cada uno de los bi, inclu-

so en el caso de que su correspondiente cofactor, (n
i ), sea nulo en caracter´ıstica p. As´ı, un

mismo polinomio da lugar a tantos polinomios presentados como presentaciones bin´omi-

cas diferentes admita. Es claro que, sobre polinomios presentados, la derivaci´on neta y las

derivaciones netas sucesivas s´ı que est´an bien deﬁnidas, y satisfacen todas las propiedades

anteriormente indicadas para la derivaci´on neta.

Observaci´on 3.2.5. En ausencia de una forma de derivar que corresponda al signiﬁcado

que la derivada tiene en caracter´ıstica cero, no parece factible a priori trasladar a carac-

ter´ıstica p la idea del problema de Casas-Alvero. Evidentemente, s´ı que puede trasladarse

el problema de la existencia de polinomios que compartan una ra´ız en Fp con determinados

otros polinomios (esto lo hace el esquema basado en la anulaci´on de las resultantes) pero,

en principio, si tales otros polinomios no responden en aspectos muy b´asicos a lo que cabe

entender por derivada, no parece razonable identiﬁcarlo como un genuino problema de

Casas-Alvero. No obstante, en el cap´ıtulo 5, los teoremas 5.3.1 y 5.5.2 mostrar´an que en

todo caso el problema s´ı puede ser formulado sobre Fp sin ninguna ambig¨uedad.

3.3. Eliminaci´on de monomios m´odulo p

Hemos visto que la reducci´on m´odulo p puede provocar la desaparici´on —por ser m´ultiplo

de p su correspondiente coeﬁciente bin´omico, ( n
n-i
)— de muchos de los t´erminos de Pn(X);

en esta secci´on mostraremos consecuencias ´utiles de este hecho. Comenzamos viendo el caso

extremo en que todos los t´erminos distintos del l´ıder quedan eliminados.

Teorema 3.3.1 (Resoluci´on por interpretaci´on). Si al reducir m´odulo p un I-polinomio

Pn(X) = Xn + ∑

i∈I
 ( n
n-i)bn-i Xi se obtiene Pn(X) = Xn, entonces Zn,I ( Fp ) = ̸O.

46 Cap´ıtulo 3. Usando esquemas proyectivos

Demostraci´on. Para cada k ∈ I, el lema 3.2.1 permite traducir la ecuaci´on H [k ] = 0 por la

aﬁrmaci´on siguiente:

Pn(X) = X n comparte una ra´ız en Fp con Pn
[k ](X) = X n-k + ∑

i∈I
i>k
 (n-k
n-i) bn-i X i-k + (n-k
n-k) bn-k.

Ahora bien, dado que Xn no tiene otra ra´ız que α = 0, tal aﬁrmaci´on signiﬁca que se

cumple la igualdad
 P n
[k ](0) = 0

lo cual, calculando la evaluaci´on indicada en el primer miembro, resulta ser

1 · bn-k = 0.

Queda as´ı probado que, bajo la hip´otesis Pn(X) = Xn, el sistema de ecuaciones que deﬁne

a Zn,I ( Fp ) exige la anulaci´on de todas las componentes y no tiene, por tanto, m´as soluci´on

que la trivial. □

Conviene llamar la atenci´on sobre la potencia del lema 3.2.1 para transformar cada

ecuaci´on H [k ] = 0 (en la que posiblemente ﬁguren varias o incluso todas las indeterminadas

bj) en una aﬁrmaci´on simple acerca de bn-k que la deja resuelta. La mera interpretaci´on

del signiﬁcado que H [k ] = 0 tiene en caracter´ıstica p ha hecho innecesario aplicar otras

t´ecnicas usuales en la resoluci´on de ecuaciones.

Como primera aplicaci´on del teorema 3.3.1 se logra ya demostrar la conjetura de Casas-

Alvero para una inﬁnidad de n´umeros: todos aquellos que sean potencia de un primo.

Corolario 3.3.2. La conjetura de Casas-Alvero es cierta para todo n´umero de la forma

n = p r.

Demostraci´on. Gracias a la proposici´on 3.1.4, es suﬁciente con demostrar que el esquema

Ypr = Z pr,J (siendo J el conjunto completo de exponentes) carece de puntos sobre Fp , es

decir, que se cumple Ypr ( Fp ) = ̸O. Pero esto es consecuencia inmediata del teorema 3.3.1,

puesto que, como es bien conocido, se veriﬁca:

Para todo i = 1, 2, . . . , p r−1, ( pr

i
 ) ≡ 0 mod p,

de modo que el reducido m´odulo p del polinomio Pn(X) = Xn + pr- 2∑

i=1
 ( pr

pr− i
 )bpr-i Xi es

justamente Pn(X) = Xn. □

Notaci´on. Dado un conjunto de exponentes I = {i1, i2, . . . , ir} y un primo p, denotaremos

por Ip al conjunto de los exponentes (diferentes de n) que se conservan cuando se reduce

m´odulo p el I-polinomio Pn(X) = Xn + ∑

i∈I
 ( n
n-i)bn-i Xi . Esto es:

3.3 Eliminaci´on de monomios m´odulo p 47

Ip = { i ∈ I | ( n
n-i)̸= 0 } = { i ∈ I | ( n
i ) ̸≡ 0 mod p }

En consecuencia, para el polinomio reducido se tienen dos expresiones alternativas:

Pn(X) = Xn + ∑

i∈I
 ( n
n-i) bn-i Xi = Xn + ∑

i∈Ip
 ( n
n-i) bn-i Xi,

dado que si j ∈ I∖Ip entonces el t´ermino ( n
n-j) bn-j Xj no precisa ser consignado.

Observaci´on 3.3.3. El enunciado del teorema de resoluci´on por interpretaci´on (3.3.1)

puede ahora reescribirse del siguiente modo: “ Si Ip = ̸O, entonces Zn,I ( Fp ) = ̸O ”

El hecho de que un determinado monomio ( n
n-j) bn-j Xj quede eliminado de Pn(X)

a causa de la congruencia ( n
j ) ≡ 0 mod p no signiﬁca que la variable bn-j vaya a desa-

parecer del problema que nos ocupa, consistente en hallar Zn,I ( Fp ) o, lo que es igual, en

resolver sobre Fp el sistema de ecuaciones

H [i1 ] = H [i2 ] = . . . = H [ir ] = 0 ; bn-i = 0 ∀i ∈ J ∖I, (3.5)

puesto que dicha variable bn-j aparecer´a en los sucesivos polinomios Pn
[k ](X) acompa˜nada

del factor (n-k
n-j) , el cual no tiene por qu´e ser nulo. Por tanto, todas las variables bn-j
con j ∈ I∖Ip siguen tan vigentes como inc´ognitas del sistema (3.5) como las variables

bn-i con i ∈ Ip, que permanecen visibles en Pn(X). Se presenta, no obstante, la siguiente

peculiaridad:

Proposici´on 3.3.4. Se considera el I-polinomio Pn(X) = Xn + ∑

i∈I
 ( n
n-i)bn-i Xi , as´ı como

su reducido m´odulo p, Pn(X) = Xn + ∑

i∈Ip
 ( n
n-i) bn-i Xi. Para cada k ∈ Ip se cumple:

Pn
[k ](X) = Xn-k + ∑

i∈Ip
i≥k
 (n-k
n-i) bn-i Xi-k.

Es decir, para aquellas derivadas Pn
[k ](X) cuyo orden de derivaci´on pertenezca al conjunto

Ip, la reducci´on m´odulo p elimina todos los t´erminos que involucren a las indeterminadas

bn-j con j ∈ I∖Ip, de modo que Pn
[k ](X) solo contiene indeterminadas que estuvieran

efectivamente presentes en Pn(X).

Demostraci´on. Debemos comprobar que si el t´ermino ( n
n-j)bn-j Xj est´a presente en Pn(X)

pero desaparece al pasar a Pn(X), entonces el t´ermino (n-k
n-j )bn-j Xj -k, que est´a presente

48 Cap´ıtulo 3. Usando esquemas proyectivos

en Pn
[k ](X) para k ≤ j, tambi´en va a desaparecer al pasar a Pn
[k ](X), siempre y cuando

k coincida con alguno de los exponentes supervivientes en Pn(X).

Partimos, por tanto, de la siguiente situaci´on:

k ∈ Ip , j ∈ I∖Ip , 1 ≤ k < j < n (3.6)

(pues, obviamente, la igualdad k = j es imposible), y nuestro objetivo es demostrar la

congruencia (n-k
n-j ) ≡ 0 mod p. La clave para lograrlo se encuentra en la igualdad (2.14)

establecida en el comentario 2.3.5, seg´un la cual:

( n
n−k
 )( n−k
n−j
 ) = ( n
n−j
 )( j
k
 ). (3.7)

En efecto, de (3.6) se desprende que p divide a ( n
n-j) pero no divide a ( n
n-k). En es-

tas condiciones, el segundo factor del primer miembro en (3.7) debe ser, necesariamente,

m´ultiplo de p. □

Ejemplo. Con n = 10, I = { 5, 6, 7, 8 }, p = 5, se tiene:

P10(X) = X10 + 45 b2 X8 + 120 b3 X7 + 210 b4 X6 + 252 b5 X5.

Podemos observar que (10
2 ) = 45, (10
3 ) = 120 y (10
4 ) = 210 son congruentes con 0 m´odulo 5,

mientras que (10
5 ) = 252 no lo es, de modo que

P10(X) = X10 + 2 b5 X5, y adem´as Ip = { 5 }.

En los polinomios P10
[k ](X) pueden encontrarse b2, b3, b4 y b5; as´ı, por ejemplo:

P10
[2](X) = X8 + 28 b2 X6 + 56 b3 X5 + 70 b4 X4 + 56 b5 X3,

P10
[3](X) = X7 + 21 b2 X5 + 35 b3 X4 + 35 b4 X3 + 21 b5 X2

y por tanto
 P10
[2](X) = X8 + 3 b2 X6 + b3 X5 + b5 X3,

P10
[3](X) = X7 + b2 X5 + b5 X2.

Ahora bien, la proposici´on 3.3.4 garantiza que en P10
[5](X) no van a ﬁgurar b2, b3 ni b4.

Y, en efecto, se tiene

P10
[5](X) = X5 + 10 b2 X3 + 10 b3 X2 + 5 b4 X + b5,

de modo que: P10
[5](X) = X5 + b5.

3.3 Eliminaci´on de monomios m´odulo p 49

Seg´un se vio en la observaci´on 3.1.1, al ser Ip un subconjunto de I, Z n,Ip es un

subesquema de Z n,I y, en particular, se veriﬁca la inclusi´on Zn,Ip( Fp ) ⊂ Zn,I ( Fp ), de

donde se sigue trivialmente la implicaci´on

Zn,I ( Fp ) = ̸O =⇒ Zn,Ip( Fp ) = ̸O.

Lo que resulta llamativo (y ´util) es que tambi´en es cierta la implicaci´on rec´ıproca.

Teorema 3.3.5 (Resoluci´on por elevaci´on). Sea I el conjunto de exponentes corres-

pondiente al I-polinomio de grado n Pn(X) = Xn + ∑

i∈I
 ( n
n-i)bn-i Xi , y sea p un n´umero

primo. Se veriﬁca
 Zn,Ip( Fp ) = ̸O ⇐⇒ Zn,I ( Fp ) = ̸O.

Demostraci´on. Falta solamente demostrar la implicaci´on hacia la derecha. Con el ﬁn de

distinguir claramente entre los esquemas Z n,I y Z n,Ip introducimos un polinomio auxi-

liar, el Ip -polinomio gen´erico Qn( X) = Xn + ∑

i∈Ip
 ( n
n-i)bn-i Xi , al que vamos a referir la

construcci´on de Z n,Ip .

Pongamos Ip = { k1, k2, . . . , ks } ⊂ I = { i1, i2, . . . , ir }. Sabemos que Zn,I ( Fp ) es

la subvariedad proyectiva de P n−3
2,3,. . . ,n-1(Fp ) deﬁnida por el sistema de ecuaciones H [i1 ] =

H [i2 ] = . . . = H [ir ] = 0 ; bn-i = 0 ∀i ∈ J ∖ I o, equivalentemente, (ver observaci´on 3.2.2)

por el sistema de ecuaciones

H [i1 ] = H [i2 ] = . . . = H [ir ] = 0 ; bn-i = 0 ∀i ∈ J ∖ I , (3.8)

donde H [i] = Res( Pn(X), Pn
[i](X)) para cada i = i1, . . . , ir. De igual manera, Zn,Ip( Fp )

es la subvariedad proyectiva del mismo espacio proyectivo pesado deﬁnida por el sistema

de ecuaciones
 ̂H [k1 ] = ̂H [k2 ] = . . . = ̂H [ks ] = 0 ; bn-i = 0 ∀i ∈ J ∖ Ip , (3.9)

donde ̂H [i] = Res( Qn(X), Qn
[i](X)) para cada i = k1, . . . , ks. Cuando la inclusi´on Ip⊂I es

estricta (el caso contrario carece de inter´es), Qn( X) es distinto de Pn(X): le faltan algunos

de sus t´erminos. Pero como se trata justo de los t´erminos que la reducci´on m´odulo p hace

desaparecer, sucede que Pn(X) y Qn(X) son iguales.

Por otra parte, para un orden de derivaci´on dado, k = 1, . . . , n −2, los polinomios

Pn
[k ](X) y Qn
[k ]( X) diﬁeren en los t´erminos de la forma (n-k
n-i )bn-i X i-k con i ∈ I ∖ Ip,

i ≥ k; la proposici´on 3.3.4 garantiza que para k ∈ Ip estos t´erminos desaparecen al reducir

m´odulo p, de modo que la igualdad Pn
[k ](X) = Qn
[k ](X), que no es en general cierta para k

arbitrario, s´ı que es cierta para k = k1, k2, . . . , ks. Queda as´ı probado que para toda k ∈ Ip

50 Cap´ıtulo 3. Usando esquemas proyectivos

se veriﬁca
 ̂H [ k ] = Res( Qn(X), Qn
[k ](X) ) = Res( Pn(X), Pn
[k ](X) ) = H [ k ].

Observemos que estas resultantes involucran exclusivamente a las indeterminadas bn-k1,

bn-k2,. . ., bn-ks. Estamos ya en condiciones de resolver el sistema (3.8), lo cual se efec-

tuar´a en dos etapas:

Etapa 1. La hip´otesis Zn,Ip( Fp ) = ̸O signiﬁca que el sistema (3.9) ´unicamente posee la

soluci´on trivial; por tanto, el conjunto de condiciones ̂H [k1 ] = ̂H [k2 ] = . . . = ̂H [ks ] = 0

implica que bn-k1 = bn-k2 = . . . = bn-ks = 0. Ahora bien, como acabamos de ver, este

sistema es indistinguible a todos los efectos del sistema H [k1 ] = H [k2 ] = . . . = H [ks ] = 0;

se concluye entonces que el subsistema de (3.8) formado por estas s ecuaciones obliga a

que sean nulas bn-k1, bn-k2, . . . , bn-ks, esto es, justo las variables presentes en Pn(X) que

sobreviven a la reducci´on m´odulo p de dicho polinomio.

Etapa 2. Una vez conocido que bn-k1, bn-k2, . . . , bn-ks son nulas, podemos sustituirlas por

0 en Pn(X), pero entonces tenemos

Pn(X) = Xn + ∑

i∈Ip
 ( n
n-i) · 0 · Xi = Xn.

Aplicando el teorema 3.3.1 (de resoluci´on por interpretaci´on) se obtiene que las r −s

inc´ognitas pendientes de despejar en el sistema (3.8) han de ser tambi´en nulas, esto es, en

deﬁnitiva, que Zn,I ( Fp ) = ̸O. □

La proposici´on 3.1.2 caracterizaba en t´erminos de esquemas la respuesta aﬁrmativa

a los diversos problemas de Casas-Alvero. M´as adelante, la proposici´on 3.1.4 (basada

en la proposici´on 3.0.3 de Schicho, Graf von Bothmer, Labs y Van de Woestijne) propor-

cion´o una condici´on suﬁciente para tal respuesta aﬁrmativa. El teorema 3.3.5 de resoluci´on

por elevaci´on multiplica la potencia de dicha proposici´on al anteponer otra condici´on su-

ﬁciente mucho menos exigente y m´as sencilla de veriﬁcar en ciertos casos. A continuaci´on

recordamos conjuntamente estas tres contribuciones, que van a conﬂuir en un corolario de

extraordinaria aplicabilidad en el futuro.

[ 3.1.2] El I-problema parcial de Casas-Alvero de grado n tiene respuesta aﬁrmativa si y

solo si Zn,I (C) = ̸O.

[ 3.1.4] Si para el primo p se cumple Zn,I ( Fp ) = ̸O, entonces Zn,I (C) = ̸O.

[ 3.3.5] Si para el primo p se cumple Zn,Ip( Fp ) = ̸O, entonces Zn,I ( Fp ) = ̸O (y adem´as

es trivialmente cierta la implicaci´on rec´ıproca).

3.4 Tri´angulo de Tartaglia en caracter´ıstica positiva 51

Corolario 3.3.6. Sea n ∈ N, sea J = {1, 2, . . . , n −2} , y sea I ⊂ J.

Es condici´on suﬁciente para que el I-problema parcial de Casas-Alvero de grado n

tenga respuesta aﬁrmativa, que exista un n´umero primo p tal que Zn,Ip( Fp ) = ̸O.

En particular, si existe un primo p tal que Zn,Jp( Fp ) = ̸O, entonces la conjetura de

Casas-Alvero de grado n es verdadera.

Demostraci´on. La primera aﬁrmaci´on resulta de considerar la cadena de implicaciones

Zn,Ip( Fp ) = ̸O ⇒ Zn,I ( Fp ) = ̸O ⇒ Zn,I (C) = ̸O ⇒ No existen I-contraejemplos a la con-

jetura de Casas-Alvero de grado n

Despu´es, basta recordar que el esquema Yn coincide con Z n,J , y por tanto

Zn,Jp( Fp ) = ̸O ⇒ Yn( Fp ) = Zn,J ( Fp ) = ̸O ⇒ Yn(C) = ̸O ⇒ La conjetura de Casas-Alvero de grado

n no admite contraejemplo alguno
 □

3.4. Tri´angulo de Tartaglia en caracter´ıstica positiva

Como se acaba de ver, ﬁjado n, la conjetura de Casas-Alvero de grado n queda proba-

da si se logra encontrar un primo p tal que Zn,Jp( Fp ) = ̸O, lo cual equivale a que sea

Yn( Fp ) = ̸O (m´as adelante, y debido a que zanja aﬁrmativamente el problema total de

Casas-Alvero en grado n, de un primo con esta cualidad diremos que es un primo eﬁcaz

con n). Dado que existen inﬁnitos primos disponibles, se plantea la cuesti´on de cu´ales

entre ellos pueden m´as plausiblemente conducir a la deseada igualdad Zn,Jp( Fp ) = ̸O, y

en una primera aproximaci´on parece conveniente que Jp sea lo m´as peque˜no —en cuanto

a cardinal— posible. Recordemos que J viene denotando el conjunto completo de expo-

nentes a considerar en el problema de Casas-Alvero de grado n, de modo que

J = {1, 2, . . . , n−2
} y Jp = { i ∈ J | ( n
i ) ̸≡ 0 mod p }.

As´ı pues,para visualizar Jp basta tomar de la l´ınea (n + 1)-´esima del tri´angulo de Tartaglia

todos los elementos a excepci´on del primero y los dos ´ultimos, seg´un se muestra:
( n
0 ) ( n
1 ) ( n
2 ) ( n
3 ) ( n
4 ) . . . ( n
n-3) ( n
n-2) ( n
n-1) ( n
n ),

reduci´endolos a continuaci´on m´odulo p ; los elementos de Jp indican las posiciones en

las que resulta un valor no nulo. Localizar situaciones en que Jp posee pocos elementos

requiere por tanto observar en qu´e ﬁlas del tri´angulo de Tartaglia la reducci´on m´odulo

p produce mayor cantidad de ceros. Para este ﬁn ser´a de gran utilidad la proposici´on

siguiente.

52 Cap´ıtulo 3. Usando esquemas proyectivos

Proposici´on 3.4.1. Sea p un n´umero primo, y sean h, r ∈ N. Se veriﬁcan las siguientes

congruencias:

1. ( hpr

kpr ) ≡ ( h
k
 ) mod p, para todo k = 0, 1, 2, . . . , h.

2. ( hpr

i
 ) ≡ 0 mod p, para todo i ̸= 0 · p r, 1 · p r, 2 · p r, . . . , h · p r.

En particular, (caso h = 1), ( pr

i
 ) ≡ 0 mod p para todo i diferente de 0 y de p r.

Demostraci´on. La f´ormula del binomio de Newton junto con el evidente hecho de que el

n´umero combinatorio ( p
i ) es m´ultiplo de p para todo i = 1, . . . , p−1 proporcionan la iden-

tidad, v´alida en caracter´ıstica p, (a + b)p = ap + b p,

de donde resulta (a + b)p
2 = [(a + b)p ] p = (ap + b p )p = ap
2 + b p
2

e, iterando el procedimiento, (a + b)p
r = ap
r + bp
r .

Siempre en caracter´ıstica p, se obtiene

(a + b)hpr = [(a + b)pr ]h = [ap
r + bp
r ]h = h∑

k = 0
 ( h
k
 ) ap
r(h-k) bp
rk,

expresi´on que necesariamente coincide —en cuanto polinomio de Fp[a, b] — con la dada

directamente por la f´ormula del binomio de Newton,

(a + b)hpr = hpr
∑

i = 0
 ( hpr

i
 ) ahpr- i bi.

Identiﬁcando los coeﬁcientes de una y otra expresi´on se obtienen ya las congruencias del

enunciado. □

Comentario 3.4.2. El fascinante tri´angulo de Tartaglia en caracter´ıstica p (ver, en la

ﬁgura 3.1, el caso p = 3) presenta estructura fractal, y son las l´ıneas correspondientes a

las potencias de p las que delimitan las unidades de distinto orden que lo conﬁguran;

tales l´ıneas —las que contienen a los n´umeros (pr
i ) para i = 0, 1, . . . , p — est´an formadas

exclusivamente por ceros salvo, naturalmente, los elementos inicial y ﬁnal, iguales a 1.

La porci´on del tri´angulo de Tartaglia que queda por encima de la l´ınea p r ser´ıa la unidad

de orden r, T (r). Para cada h = 1, . . . , p −1, en la l´ınea hp r son nulos todos los elementos

excepto los de la forma ( hpr
kpr ) para k = 0, 1, . . . , h, los cuales componen una r´eplica exacta

3.4 Tri´angulo de Tartaglia en caracter´ıstica positiva 53

0 1
1 1 1
2 1 2 1 ´Ultima l´ınea de T (1)

31 = 3 1 · · 1
4 1 1 · 1 1
5 1 2 1 1 2 1
2 · 3 = 6 1 · · 2 · · 1
7 1 1 · 2 2 · 1 1
8 1 2 1 2 1 2 1 2 1 ´Ultima l´ınea de T (2)

32 = 9 1 · · · · · · · · 1
10 1 1 · · · · · · · 1 1
11 1 2 1 · · · · · · 1 2 1
12 1 0 0 1 · · · · · 1 0 0 1
13 1 1 0 1 1 · · · · 1 1 0 1 1
14 1 2 1 1 2 1 · · · 1 2 1 1 2 1
15 1 0 0 2 0 0 1 · · 1 0 0 2 0 0 1
16 1 1 0 2 2 0 1 1 · 1 1 0 2 2 0 1 1
17 1 2 1 2 1 2 1 2 1 1 2 1 2 1 2 1 2 1
2 · 9 = 18 1 · · · · · · · · 2 · · · · · · · · 1
19 1 1 · · · · · · · 2 2 · · · · · · · 1 1
20 1 2 1 · · · · · · 2 1 2 · · · · · · 1 2 1
21 1 0 0 1 · · · · · 2 0 0 2 · · · · · 1 0 0 1
22 1 1 0 1 1 · · · · 2 2 0 2 2 · · · · 1 1 0 1 1
23 1 2 1 1 2 1 · · · 2 1 2 2 1 2 · · · 1 2 1 1 2 1
24 1 0 0 2 0 0 1 · · 2 0 0 1 0 0 2 · · 1 0 0 2 0 0 1
25 1 1 0 2 2 0 1 1 · 2 2 0 1 1 0 2 2 · 1 1 0 2 2 0 1 1
26 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 ´Ult. l´ın. T (3)

33 = 27 1 · · · · · · · · · · · · · · · · · · · · · · · · · · 1
28 1 1 · · · · · · · · · · · · · · · · · · · · · · · · · 1 1
29 1 2 1 · · · · · · · · · · · · · · · · · · · · · · · · 1 2 1
30 1 0 0 1 · · · · · · · · · · · · · · · · · · · · · · · 1 0 0 1
31 1 1 0 1 1 · · · · · · · · · · · · · · · · · · · · · · 1 1 0 1 1

Figura 3.1: Fractal de Tartaglia en caracter´ıstica 3. Los puntos representan ceros

de la l´ınea h, dado que se cumple ( hpr
kpr ) ≡( h
k ) mod p. Adem´as, cada uno de estos n´umeros

resulta ser el v´ertice superior de un tri´angulo igual al tri´angulo unidad de orden r, T (r)

multiplicado por cierto factor que, l´ogicamente, coincide con el valor que se encuentra

en dicho v´ertice, ( h
k ). Esos h + 1 tri´angulos colgados de la l´ınea hp r dejan libres h zonas

triangulares —en posici´on invertida respecto de aquellos— de p r−1 ﬁlas de altura; todos

los elementos ubicados en estas ´areas son iguales a cero. A ﬁn de resaltar visualmente la

estructura, en la ﬁgura 3.1 estos ceros se han representado mediante puntos.

Tenemos as´ı que el trapecio formado por la l´ınea hp r junto con las p r−1 l´ıneas si-

guientes es un mosaico cuyas piezas son las h + 1 copias del tri´angulo T (r) multiplicadas

por los respectivos ( h
k ), y los h tri´angulos invertidos, totalmente llenos de ceros (puntos,

en la ﬁgura 3.1) que aparecen intercalados. Agregando al tri´angulo T (r) los p −1 trapecios

que arrancan de las l´ıneas hp r con h = 1, 2, . . . , p −1, respectivamente, se forma el tri´angulo

T (r + 1), unidad de orden r + 1 en el fractal. Es de destacar el hecho de que toda esta precisa

construcci´on queda completamente explicada por la proposici´on 3.4.1 junto con el modo

en que se propagan hacia las l´ıneas inferiores los valores de los n´umeros combinatorios,

seg´un la propiedad fundamental ( n
i ) + ( n
i+1 ) = (n+1
i+1 ).

Observaci´on 3.4.3. Como alternativa a la demostraci´on que se basa en la f´ormula de

Newton, encontramos la justiﬁcaci´on aritm´etica de las congruencias dadas en 3.4.1 obser-

54 Cap´ıtulo 3. Usando esquemas proyectivos

vando la igualdad

(hp r

kp r
) = hpr · (hpr- 1) · · · (hpr- p) · (hpr- p - 1) · · · (hpr- 2p) · (hpr- 2p - 1) · · · · · · · · · (hpr- kpr + 1)

kpr · (kpr- 1) · · · (kpr- p) · (kpr- p - 1) · · · (kpr- 2p) · (kpr- 2p - 1) · · · · · · · · · 1

en la que se han recuadrado los factores que son m´ultiplo de p; puede apreciarse que

van perfectamente emparejados en numerador y denominador. Adem´as, los factores sin

recuadrar comprendidos entre ellos van siendo congruentes m´odulo p con −1, −2, . . . , 1−p,

tambi´en de forma paralela en numerador y denominador, de modo que sus respectivos

cocientes valen siempre 1 m´odulo p. Por otra parte, considerando solo los recuadros, hay

arriba kp r-1 factores decrecientes de p en p a partir de hp r, y lo mismo abajo, esta vez

a partir de kp r; dividiendo entre p a cada uno de ellos se conserva el valor entero de la

expresi´on, que ahora es directamente interpretable como ( hpr-1

kpr-1 ). Queda as´ı probada la

cadena de congruencias ( hpr
kpr ) ≡ ( hpr-1

kpr-1 ) ≡ ( hpr-2

kpr-2 ) ≡ · · · ≡ ( h
k ) mod p.

El proceso anterior no requiere que h sea primo con p, y puede aplicarse al caso r > s

para demostrar que ( hpr
kps ) ≡ ( hpr-s
k ) mod p. El caso opuesto, r < s, puede obviarse, pues

una simple reescritura lo lleva al caso r = s; en el siguiente ejemplo se muestra c´omo:
( 200 · 73

3 · 7
5 ) = ( 200 · 7
3

200 · 7
3 − 3 · 7
5 ) = ( 200 · 7
3

(200 − 3 · 7
2) 7
3 ), y 7 ̸ ∣
∣ (200 − 3 · 7
2).

Seg´un esto, para ver qu´e sucede con ( hpr
i ) cuando i no es de la forma kp r basta

considerar el caso ( hpr
k ) donde k es primo con p. Se tendr´a, entonces, k = c · p + m, con

0 < m < p. El n´umero combinatorio (hpr
cp ) puede ser m´ultiplo de p, o no serlo; este hecho

no reviste importancia. Lo signiﬁcativo es que (hpr
k ) = ( hpr
c·p+m
) se obtiene a partir de (hpr
cp )

incorporando los m factores que le faltan en numerador y denominador:

( hpr

k
 ) = ( hpr

cp + m
 ) =
 (hpr − cp
) · (hpr − cp − 1
) · · · (hpr − cp − m + 1
)

(cp + m
) · (cp + m − 1 ) · · · (cp + 1
) · ( hpr

cp
 ) (3.10)

Los factores que se a˜naden al denominador van desde cp + 1 hasta cp + m; ninguno de ellos

es, por tanto, m´ultiplo de p. Por el contrario, al numerador le llega seguro un m´ultiplo

de p (ver recuadro), hp r−cp, junto con otros varios factores. La fracci´on surgida en (3.10)

es, pues, un elemento nulo en Fp, concluy´endose que tambi´en lo es ( hpr
k ).

3.5. Los casos de cardinal 1 y 2 para Ip

En el cap´ıtulo 2 qued´o demostrado que, sea cual sea el grado n que se considere, la

conjetura de Casas-Alvero no admite ning´un {i}-contraejemplo ni tampoco ning´un {i, j}-

contraejemplo (corolarios 2.2.3 y 2.3.4, respectivamente). Naturalmente, la segunda ne-

gaci´on incluye lo dicho por la primera; no obstante, conviene resaltar el car´acter aut´onomo

3.5 Los casos de cardinal 1 y 2 para Ip 55

de esta, cuya previa obtenci´on constituy´o un paso necesario para llegar hasta la segunda.

En t´erminos de esquemas proyectivos estos resultados se expresan de la siguiente manera:

Para todo n ∈ N, ∀i, j ∈ {1, 2, . . . , n-2}, Zn,{i}(C) = ̸O y Zn,{i,j}(C) = ̸O.

En el ´ambito de la proposici´on 3.1.4 (Si Zn,I ( Fp ) = ̸O, entonces Zn,I (C) = ̸O), los con-

juntos de la forma Zn,{i}( Fp ) o Zn,{i,j }( Fp ) carecen de inter´es pues, como acabamos

de ver, aquellos resultados a los que podr´ıan darnos acceso han sido ya establecidos con

anterioridad; sin embargo, tras el teorema de resoluci´on por elevaci´on y su corolario 3.3.6

cobran un extraordinario valor. Identiﬁcar bajo qu´e condiciones resultan ser vac´ıos dichos

conjuntos va a proporcionar conclusiones que no se limitan a los {i} ´o {i, j}-problemas,

sino que se extienden a cualquier I-problema para el que pueda hallarse un primo p tal

que el conjunto Ip = { i ∈ I | ( n
i ) ̸≡ 0 mod p } tenga, o bien cardinal 1, o bien cardinal 2.

Es precisamente el trabajo desarrollado en el cap´ıtulo 2 para establecer los preliminares

de los resultados arriba rese˜nados el que permite dar inmediata respuesta a esta cuesti´on.

Teorema 3.5.1. (a) Zn,{i}( Fp ) = ̸O si y solo si ( n
i ) ̸≡ 1 mod p.

(b) Zn,{i,j }( Fp ) = ̸O si y solo si se cumplen las tres condiciones siguientes:

(i ) a ̸≡ 1 mod p

(ii ) b ̸≡ 1 mod p

(iii ) a ρ (b − c
)ρ(b − ac
)σ − (−1)σ(a −1
)ρ+σ(b −1
)ρ ̸≡ 0 mod p,

siendo a = ( n
i ), b = ( n
j ), c = (n- i
n-j) y ρ = n-j
d , σ = j - i
d , con d = m.c.d.
(n−j, j −i
).

Demostraci´on. (a) El esquema Z n,{i} est´a deﬁnido por las ecuaciones H [i] = 0 ; bn-j = 0

para todo j ∈ J ∖ {i}. La proposici´on 2.2.2 hab´ıa dejado establecido que es

H [i] = b n
n-i [ 1−
( n
n-i
 )]n-i
. (3.11)

Sobre el cuerpo Fp la ecuaci´on H [i] = 0 es equivalente a bn-i = 0 si y solo si es 1−
( n
n-i
) ̸= 0,

esto es, si el entero ( n
n-i
) = ( n
i ) no es congruente con 1 m´odulo p. En caso contrario,

cualquier λ ∈ Fp veriﬁcar´a dicha ecuaci´on y, por tanto, el punto [β] = [
(0, 0, . . . , λ, 0, . . . , 0)
]

pertenecer´a al conjunto Zn,{i}( Fp ).

(b) El esquema Z n,{i,j}, a su vez, responde a la ecuaciones H [i] = H [j ] = 0 ; bn-k = 0

para todo k ∈ J ∖ {i, j}. Seg´un la proposici´on 2.3.2, se tiene

H [i] = (−1)
rs+r b j
n-i [ α ρβ σ b ρ+σ
n-j + (−1)ρσ+σ γ ρ+σ b ρ
n-i ] d

H [j ] = (−1) r b i
n-j [ δ ρ b ρ+σ
n-j + (−1)ρσ (1 + γ )ρ b ρ
n-i ] d (3.12)

56 Cap´ıtulo 3. Usando esquemas proyectivos

donde α = b −c, β = b −ac, γ = a −1, δ = b −1, r = n−j = ρd, s = j −i = σd.

Seg´un el apartado (a) de la presente proposici´on, (i) y (ii) son las condiciones necesarias

y suﬁcientes para que sea Zn,{i}( Fp ) = ̸O y Zn,{j }( Fp ) = ̸O ; esto es, para que el sistema

en dos inc´ognitas H [i] = H [j ] = 0 no admita soluciones con solo una componente distinta

de cero. Hemos de ver que, en esa situaci´on, (iii) equivale a que no exista para dicho

sistema ninguna soluci´on con ambas componentes distintas de cero.

La demostraci´on es muy similar a la del teorema 2.3.3; igual que all´ı, una soluci´on
(p, q) con p · q ̸= 0 se caracteriza por anular los dos polinomios que aparecen encerrados

entre corchetes en (3.12), lo cual signiﬁca que (p ρ+σ, q ρ) satisface el sistema de ecuaciones

lineales en las inc´ognitas u y v,

α ρβ σ u + (−1)ρσ+σ γ ρ+σ v = 0

δ ρ u + (−1)ρσ (1 + γ )ρ v = 0, (3.13)

cuya matriz de coeﬁcientes tiene justamente determinante

∆ = (−1)
ρσ[a ρ (b − c
)ρ(b − ac
)σ − (−1)σ(a −1)ρ+σ(b −1)ρ].

Por tanto, la anulaci´on (m´odulo p) de ∆ es condici´on necesaria para la existencia de (p, q).

Para comprobar que es tambi´en suﬁciente, es preciso descartar la existencia de soluciones

no triviales para el sistema (3.13) que sean de la forma (u0, 0) o (0, v0). Pero es que, al

sustituir una soluci´on del tipo (u0, 0) en la segunda ecuaci´on del sistema, se tendr´ıa

δ ρ u0 = 0, con u0 ̸= 0 =⇒ δ = b −1 = 0, en contra de (ii),

mientras que, al sustituir una soluci´on de la forma (0, v0) en la primera ecuaci´on, se tendr´ıa

(−1)ρσ+σ γ ρ+σ v0 = 0, con v0 ̸= 0 =⇒ γ = a −1 = 0, en contra de (i),

luego quedan, en efecto, descartadas tales soluciones. □

Observaci´on 3.5.2. La demostraci´on de 3.5.1(a) ha puesto de maniﬁesto que, en el

contexto del esquema Z n,{i}, la hip´otesis ( n
i ) ≡ 1 mod p convierte sobre Fp a la ecuaci´on

H [i] = 0 en una tautolog´ıa. Es de inter´es precisar la raz´on por la que esto ocurre. Y es que

Pn(X) = Xn + ( n
n-i)bn-i Xi = Xi[ Xn-i + ( n
n-i)bn-i]

Pn
[i](X) = Xn-i + 1 · bn-i
( n
i ) ≡ 1 mod p
 



 ⇒ Pn(X) = Xi · Pn
[i](X)

de modo que en tal situaci´on, Pn
[i](X) forzosamente comparte, no ya una, sino todas sus

ra´ıces con Pn(X).

3.5 Los casos de cardinal 1 y 2 para Ip 57

Nos ocupamos ahora del caso en que Ip tiene cardinal 1.

Proposici´on 3.5.3. Se considera ﬁjado un grado n y un conjunto de exponentes I ⊂ J =

{1, 2, . . . , n−2}. Si existe un primo p tal que Ip = {i} y adem´as ( n
i ) ̸≡ 1 mod p, entonces

el I-problema de Casas-Alvero de grado n tiene respuesta aﬁrmativa.

Demostraci´on. Seg´un el teorema 3.5.1(a), de la hip´otesis ( n
i ) ̸≡ 1 mod p se sigue que

Zn,{i}( Fp ) = ̸O , y dado que Ip = {i}, ello signiﬁca que Zn,Ip( Fp ) = ̸O . Estamos, pues,

en condiciones de aplicar el corolario 3.3.6 para obtener la conclusi´on requerida. □

Corolario 3.5.4. La conjetura de Casas-Alvero es verdadera para los inﬁnitos n´umeros

de la forma n = 2p r.

Demostraci´on. Sea n = 2p r para cierto primo p, siendo r ≥ 1. Por la proposici´on 3.4.1 se

sabe que ( 2pr
i ) ≡ 0 mod p para todos los valores de i ∈ J = {1, 2, . . . , 2pr−2} excepto para

i = pr, para el cual es ( 2pr
pr ) ≡ ( 2
1 ) mod p. Esto es,

Jp = { p r} y ( n
p
r ) ≡ 2 ̸≡ 1 mod p

(puesto que nunca 2−1 puede ser m´ultiplo de p). Basta aplicar ahora la proposici´on 3.5.3

para obtener que el J-problema (esto es, el problema total ) de Casas-Alvero de grado n

tiene respuesta aﬁrmativa. □

Pasamos a ocuparnos del caso en que Ip tiene cardinal 2.

Proposici´on 3.5.5. Sea n ∈ N y sea I ⊂ J = {1, 2, . . . , n−2}. Para que el I-problema de
Casas-Alvero de grado n tenga respuesta aﬁrmativa es condici´on suﬁciente que exista un
primo p para el cual sea Ip = {i, j } y se cumpla:

(i ) a ̸≡ 1 mod p

(ii ) b ̸≡ 1 mod p

(iii ) a ρ (b − c
)ρ(b − ac
)σ − (−1)σ(a −1
)ρ+σ(b −1
)ρ ̸≡ 0 mod p,

siendo a = ( n
i ), b = ( n
j ), c = (n- i
n-j) y ρ = n-j
d , σ = j - i
d , con d = m.c.d.
(n−j, j −i
).

Demostraci´on. En la situaci´on del enunciado se tiene que Zn,Ip( Fp ) = ̸O , de acuerdo con

el teorema 3.5.1(b). Puede, por tanto, aplicarse el corolario 3.3.6, el cual concluye la

prueba. □

Corolario 3.5.6. La conjetura de Casas-Alvero es verdadera para todo n´umero de la forma

n = 3p r, siendo p ̸= 2.

58 Cap´ıtulo 3. Usando esquemas proyectivos

Demostraci´on. Para el conjunto completo de exponentes, J = {1, 2, . . . , 3pr−2
} y en apli-

caci´on de la proposici´on 3.4.1 —relativa a las congruencias m´odulo p que satisfacen los

n´umeros del tipo (hpr
i ) — se obtiene

Jp = {i, j }, donde i = pr , y j = 2pr,

a = ( n
i ) = ( 3pr
pr ) ≡ ( 3
1 ) = 3 mod p,

b = ( n
j ) = ( 3pr
2pr ) ≡ ( 3
2 ) = 3 mod p,

c = ( n-i
n-j ) = ( 2pr
pr ) ≡ ( 2
1 ) = 2 mod p,

d = m.c.d.
(pr, pr) = pr , ρ = pr
d = 1 , σ = pr
d = 1,

seg´un la notaci´on de la proposici´on 3.5.5. Dicha proposici´on garantiza, pues, la respuesta

aﬁrmativa al J-problema (o problema total) de Casas-Alvero de grado n = 3p r, siempre

que se cumplan las condiciones

(i) y (ii) 3 ̸≡ 1 mod p

(iii) 3 (3−2)(3−6) − (−1)
(3−1
)2(3−1
) ̸≡ 0 mod p, esto es, −1 ̸≡ 0 mod p,

condiciones que ´unicamente excluyen al primo p = 2.

3.6. Conjeturas de transmisi´on de hip´otesis

Observaci´on 3.6.1. Todo contraejemplo a la conjetura de Casas-Alvero de grado 12, en

caso de existir, debe necesariamente cumplir la condici´on de que sea b11 ̸= 0.

En efecto: si fuera b11 = 0 entonces dicho contraejemplo ser´ıa en realidad un I-polinomio

con I = J ∖ {1} = {2, 3, . . . , 10}. Pero el primo p = 11 evidentemente divide a todos los

n´umeros combinatorios de la forma ( 12
i ) con i ̸= 0, 1, 11 y 12, de modo que es I11 = ̸O.

El teorema de resoluci´on por interpretaci´on (3.3.1, o bien 3.3.3) nos dice que entonces

se tiene Z12, I ( F11 ) = ̸O, y la proposici´on 3.1.4 a˜nade que, de hecho, es Z12, I (C) = ̸O, esto

es, que no existe tal contraejemplo carente de t´ermino en X.

Teorema 3.6.2. Si p es un n´umero primo y r ≥ 1, entonces la conjetura de Casas-Alvero

de grado n = p r+ 1 o n = 2p r+ 1 no admite contraejemplos cuyo t´ermino de grado 1 tenga

coeﬁciente nulo.

Demostraci´on. En caso de ser n = p r+ 1, la prueba se reduce a formalizar el razonamiento
seguido en la observaci´on anterior. Sabemos que la l´ınea del tri´angulo de Tartaglia que
contiene los n´umeros (pr+ 1
i ) tiene, m´odulo p, la forma

1 1 0 0 0 0 . . . 0 0 0 1 1

3.6 Conjeturas de transmisi´on de hip´otesis 59

(se ha recuadrado la colecci´on de valores obtenidos cuando i recorre J = {1, 2, , . . . , n−2}).

Como consecuencia de ello podemos aﬁrmar que es Jp = {1}.

Desafortunadamente, al ser ( n
1 ) = pr+ 1 ≡ 1 mod p , no es posible emplear la proposi-

ci´on 3.5.3 con referencia al conjunto J. Tomando en cambio el conjunto de exponentes

I = J ∖ {1}, se cumple

Ip = ̸O =⇒ Zn,I ( Fp ) = ̸O =⇒ Zn,I (C) = ̸O,

esto es: entre los polinomios en que est´a ausente el t´ermino de grado 1 no existe ninguno

que sirva como contraejemplo a la conjetura.

El caso n = 2p r+ 1, p ≥ 3 admite una prueba similar a la anterior. Reduciendo m´odulo
p la l´ınea del tri´angulo de Tartaglia que contiene los n´umeros (2pr+ 1
i ), queda de la forma

1 1 0 0 0 . . . 0 2 2 0 0 . . . 0 0 0 1 1

donde el recuadro tiene el mismo signiﬁcado que arriba, y los valores 2 corresponden a

los ´ındices i = p r e i = p r+ 1. As´ı pues, en esta ocasi´on se tiene Jp = {1, p r, p r+ 1} y no

disponemos de resultados que permitan extraer conclusiones ´utiles referidas al conjunto

completo de exponentes, J; en cambio, para I = J ∖ {1} se tiene Ip = {p r, p r+ 1}, de modo

que podemos emplear la proposici´on 3.5.5 en relaci´on con los conjuntos I e Ip.

Para aplicar dicha proposici´on 3.5.5, se considera el conjunto de exponentes I, el primo

p, y los ´ındices i = p r y j = p r+ 1, y se obtiene:

a ≡ 2 mod p, b ≡ 2 mod p, c = ( pr + 1
pr ) ≡ 1 mod p, ρ = p r, σ = 1.

Obviamente se satisfacen las condiciones (i) y (ii) del enunciado, pues es 2 ̸≡ 1 mod p ; y

tambi´en se satisface (iii), ya que se tiene a ρ (b − c
)ρ(b − ac
)σ ≡ 0 mod p, mientras que,

en cambio, es (−1)σ(a −1)ρ+σ(b −1)ρ ≡ −1 mod p. Se concluye entonces, sucesivamente,

que los conjuntos de puntos Zn,Ip( Fp ), Zn,I ( Fp ) y Zn,I (C) son vac´ıos, y que, por tanto,

el I-problema parcial de Casas-Alvero de grado n tiene respuesta aﬁrmativa, esto es, que

ning´un I-polinomio (polinomio carente de t´ermino vicel´ıder, de t´ermino independiente y

tambi´en de t´ermino lineal) puede servir como contraejemplo a la conjetura. □

Si P(X) es un polinomio de grado n que, como todos los que venimos considerando

a partir de la proposici´on 1.1.2, carece de t´ermino vicel´ıder y de t´ermino independiente,

entonces, cualesquiera que sean los enteros d ≥ 2, e ≥ 1, los polinomios [P(X)]d y X e·P(X)

van a carecer no solo de dichos t´erminos sino tambi´en del t´ermino de grado 1. Supongamos

que sea N = d · n, o bien N = e + n, y que se da una de las dos circunstancias siguientes

(i) N = p r + 1 o N = 2p r + 1, donde p es primo y r ≥ 1.

60 Cap´ıtulo 3. Usando esquemas proyectivos

(ii) Se sabe que la conjetura de Casas-Alvero de grado N es cierta.

Entonces, si se supiera que [P(X)]d o X e· P(X) veriﬁcan las hip´otesis de la conjetura de

Casas-Alvero en grado N , y puesto que, en virtud o bien del teorema 3.6.2 o bien de dicha

conjetura —seg´un que se d´e la circunstancia (i) o (ii)—, no pueden ser contraejemplos

de la misma, se tendr´ıa la seguridad de que satisfacen su tesis, esto es, que se cumple

[P(X)]d = XN o X e · P(X) = XN , de donde se deducir´ıa que es P(X) = Xn.

Lo anterior puede considerarse, en teor´ıa, como una posible estrategia para probar la

conjetura de Casas-Alvero de grado n para aquellos valores de n en que su validez no haya

sido a´un establecida. Naturalmente, ello requerir´ıa que fu´esemos capaces de demostrar

que si P(X) veriﬁca las hip´otesis de la conjetura entonces, para valores d, e adecuados,

alguno de los polinomios [P(X)]d o X e · P(X) tambi´en veriﬁca dichas hip´otesis. Tenemos

as´ı dos nuevas conjeturas: el que verdaderamente se produzca, semejante transmisi´on de

las hip´otesis de Casas-Alvero en el caso de [P(X)]d —que llamaremos propagaci´on—, y el

hecho an´alogo en el caso de X e·P(X), que llamaremos desplazamiento. Ambas conjeturas,

que a continuaci´on pasamos a precisar, resultan equivalentes a la de Casas-Alvero, y nada

permite suponer que vayan a mostrarse m´as asequibles que aquella.

3.6.1. Conjeturas de propagaci´on

Llamaremos propagaci´on de hip´otesis a la transmisi´on del cumplimiento de las hip´otesis de

Casas-Alvero desde un polinomio Pn(X) hasta su potencia d-´esima, [Pn(X)]d . Las hip´otesis

de Casas-Alvero para el polinomio de partida constan de n −2 condiciones; n´umero de

condiciones que se convierte en dn −2 para el polinomio [Pn(X)]d . Es decir, la transmisi´on

de las hip´otesis —en caso de producirse— va acompa˜nada de un efecto multiplicador sobre

el n´umero de ´ıtems que las conﬁguran; de ah´ı el t´ermino propagaci´on que se ha elegido

para designar este fen´omeno.

De las dos circunstancias en las que, como hemos dicho, nos ser´ıa de utilidad que se

produjera la propagaci´on de hip´otesis,

(i) N = dn es de la forma p r + 1 o 2p r + 1;

(ii) Se sabe cierta la conjetura de Casas-Alvero de grado N = dn,

la segunda carece actualmente de aplicabilidad, pues —incluyendo los resultados de esta

Memoria—, no se conoce ning´un grado n tal que la conjetura de Casas-Alvero a´un no haya

sido probada para n pero s´ı que lo haya sido para alg´un m´ultiplo suyo, dn.

Por el contrario, cualquiera que sea n ∈ N, s´ı que est´a garantizada la existencia de un

n´umero d ≥ 2 (hay, de hecho, inﬁnitos) para el cual tenga lugar la circunstancia (i); ello

es consecuencia de un cl´asico teorema de Dirichlet que recordamos a continuaci´on.

3.6 Conjeturas de transmisi´on de hip´otesis 61

Teorema 3.6.3 (Dirichlet). Si los n´umeros enteros a y d son primos entre s´ı, entonces

en la progresi´on aritm´etica dada por an = a + nd se encuentran inﬁnitos n´umeros primos.

Demostraci´on. V´ease, por ejemplo, [Ser]. □

Teorema 3.6.4. Las tres conjeturas que se indica son equivalentes entre s´ı.

(a) Conjetura de Casas-Alvero de grado n.

(b) Conjetura de propagaci´on general de grado n: Si Pn(X) = Xn+ ∑n-2
i=1 ( n
n-i)bn-i Xi ∈

C[ X] comparte una ra´ız con cada una de sus derivadas de orden menor o igual que

n−2, entonces para todo d ∈ N el polinomio [
Pn(X)
]d comparte una ra´ız con cada

una de sus derivadas de orden menor o igual que dn−2.

(c) Conjetura de propagaci´on selectiva de grado n: Existe d ∈ N, d ≥ 2, tal que para

N = dn se da la circunstancia (i) o la circunstancia (ii), y tal que si el polinomio

Pn(X) = Xn + ∑n-2
i=1 ( n
n-i)bn-i Xi ∈ C[ X] comparte una ra´ız con cada una de sus

derivadas de orden menor o igual que n−2, entonces [
Pn(X)
]d comparte una ra´ız

con cada una de sus derivadas de orden menor o igual que dn−2.

Demostraci´on. (a)⇒(b): Si Pn(X) comparte respectivas ra´ıces con sus derivadas hasta el

orden n−2 entonces, de ser cierta la conjetura de Casas-Alvero en grado n, se cumplir´a

Pn(X) = Xn y, por lo tanto, [
Pn(X)
]d = Xdn,

polinomio que ciertamente comparte una ra´ız (siempre la misma, α = 0) con cada una de

sus derivadas, de hecho, hasta el orden dn−1.

(b)⇒(c): Se considera la progresi´on aritm´etica {−1 + dn}∞
d = 1. Obs´ervese que d es aqu´ı el

´ındice variable; n est´a ﬁjado y es, desde luego, primo con −1. El teorema de Dirichlet

garantiza que existen en ella inﬁnitos t´erminos primos, todos los cuales salvo acaso el

primero son de la forma p = dn−1 con d ≥ 2. Tomando un valor d que ofrezca esta cualidad,

se estar´a en la circunstancia (i); la conjetura de propagaci´on general asegura el cumplim-

iento de las restantes condiciones.

(c)⇒(a): Sea Pn(X) = Xn + ( n
2 )b2 Xn-2 + . . . + ( n
n-1)bn-1 X veriﬁcando las hip´otesis de

Casas-Alvero. La conjetura de propagaci´on selectiva proporciona cierto entero d tal que el

polinomio

[
Pn(X)
]d = Xnd + d ( n
2 ) b2 Xnd-2 + (t´erminos de grado intermedio) + ( n
n-1)d bn-1
d Xd

satisface todas la hip´otesis de la conjetura de Casas-Alvero de grado N = nd, sabiendo

efectivamente que dicha conjetura es cierta en grado N o bien, en su defecto, que se tiene

62 Cap´ıtulo 3. Usando esquemas proyectivos

N = p r + 1 o 2p r + 1 , de modo que puede aplicarse el teorema 3.6.2. Cualquiera de estas

opciones excluye la posibilidad de que [
Pn(X)
]d sea un contraejemplo a la conjetura de

Casas-Alvero de grado N, luego necesariamente es
[
Pn(X)
]d = XN = Xnd y, por tanto, Pn(X) = Xn,

como se quer´ıa demostrar. □

Observaci´on 3.6.5. Las conjeturas de propagaci´on admiten una formulaci´on en t´erminos

geom´etricos, y tambi´en en t´erminos algebraicos. Hagamos algunas consideraciones.

Aunque el polinomio [
Pn(X)
]d sea de grado dn, sus coeﬁcientes siguen perteneciendo

al anillo Z
[
b2, . . . , bn-1]
.

Obviamente, [Pn(X)]d comparte una ra´ız α con otro polinomio Q(X) si y solo si dicha

ra´ız la comparten Pn(X) y Q(X). As´ı pues, lo que las conjeturas de propagaci´on

aﬁrman es que el propio Pn(X) comparte una ra´ız con cada una de las derivadas

(hasta el orden dn−2) del polinomio [Pn(X)]d.

Introducimos la notaci´on

H [d,k ] := Res(Pn, (P d
n )[k ] ) ∈ C[
b2, . . . , bn-1]
; Id := 〈H [d,1], H [d,2], . . . , H [d,nd - 2]〉

y recuperamos la notaci´on habitual, H [k ] = Res(Pn, P [k ]
n ); I = 〈H [1], H [2], . . . , H [n-2]〉.

Las conjeturas de propagaci´on aﬁrman, entonces, que —para todo d, o bien para un d

espec´ıﬁco, seg´un el caso—, se tiene

Si (β2, β3, . . . , βn-2) ∈ V (I ) entonces (β2, β3, . . . , βn-2) ∈ V (Id),

lo cual se resume en la inclusi´on V (I ) ⊂ V (Id).

Equivalentemente, seg´un el teorema de los Ceros de Hilbert, las conjeturas de propa-

gaci´on postulan —de nuevo, para todo d ∈ N o bien solo para cierto d— que el radical de

I contiene al radical de Id, o lo que es igual, se veriﬁca la inclusi´on Id ⊂ Rad
(I ). Esta

expresi´on admite la siguiente reescritura:

Para cada i = 1, 2, . . . , dn−2, existe mi ∈ N tal que (H [d,i ])mi ∈ I.

3.6.2. Conjeturas de desplazamiento

Llamaremos desplazamiento de hip´otesis a la transmisi´on del cumplimiento de las hip´otesis

de Casas-Alvero desde un polinomio Pn(X) hasta el producto X e · P(X).

Las n −2 condiciones que conﬁguran las hip´otesis de Casas-Alvero para el polinomio

de partida se convertir´ıan esta vez en e + n −2 para el polinomio X e · P(X). Signiﬁca

3.6 Conjeturas de transmisi´on de hip´otesis 63

entonces que la transmisi´on de las hip´otesis —en caso de producirse— ir´ıa acompa˜nada

del incremento (en e unidades) del n´umero de ´ıtems que comprenden; sin embargo este

incremento es solo aparente y queda anulado en la pr´actica, pues para el nuevo polinomio

las e primeras condiciones devienen triviales y solamente son signiﬁcativas las que se

reﬁeren a las n −2 derivadas de orden m´as alto. El t´ermino desplazamiento alude este

efecto, y tambi´en reﬂeja el hecho de que la multiplicaci´on por X e simplemente desplaza

solidariamente e posiciones a todos los coeﬁcientes del polinomio original.

Para nuestros ﬁnes resultar´ıa de utilidad el desplazamiento de hip´otesis que tuviera

lugar en una de las dos circunstancias ya indicadas anteriormente, y que son:

(i) N = e + n es de la forma p r + 1 o 2p r + 1;

(ii) Se sabe cierta la conjetura de Casas-Alvero de grado N = e + n.

Observemos que, cualquiera que sea el entero n, se dispone de inﬁnitos valores e tales

que N = e + n sea del tipo p r o 2p r, en cuyo caso —como los corolarios 3.3.2 y 3.5.4

garantizan— se producir´a la circunstancia (ii); as´ı mismo, tomando estos mismos valores

de e incrementados en una unidad se logra producir la circunstancia (i).

A continuaci´on se va a reproducir mutatis mutandis el mismo discurso que en la sub-

secci´on anterior se reﬁri´o a las conjeturas de propagaci´on, referido esta vez a las conjeturas

de desplazamiento. Deliberadamente se ha mantenido casi id´entico al otro, de modo que

sea patente el paralelismo entre ambos desarrollos.

Teorema 3.6.6. Las tres conjeturas que se indica son equivalentes entre s´ı.

(a) Conjetura de Casas-Alvero de grado n.

(b) Conjetura de desplazamiento general de grado n: Si Pn(X) = Xn
+ ∑n-2
i=1 ( n
n-i)bn-i Xi ∈

C[ X] comparte una ra´ız con cada una de sus derivadas de orden menor o igual que

n−2, entonces para todo e ≥ 1 el polinomio X e · P(X) comparte una ra´ız con cada

una de sus derivadas de orden menor o igual que e + n−2.

(c) Conjetura de desplazamiento selectivo de grado n: Existe e ∈ N, e ≥ 1, tal que para

N = e + n se da la circunstancia (i) o la circunstancia (ii), y tal que si el polinomio

Pn(X) = Xn + ∑n-2
i=1 ( n
n-i)bn-i Xi ∈ C[ X] comparte una ra´ız con cada una de sus

derivadas de orden menor o igual que n−2, entonces X e · P(X) comparte una ra´ız

con cada una de sus derivadas de orden menor o igual que e + n−2.

Demostraci´on. (a)⇒(b): Si Pn(X) comparte respectivas ra´ıces con sus derivadas hasta el

orden n−2 entonces, de ser cierta la conjetura de Casas-Alvero en grado n, se cumplir´a

64 Cap´ıtulo 3. Usando esquemas proyectivos

Pn(X) = Xn y, por lo tanto, X e · P(X) = Xe+n,

que ciertamente comparte una ra´ız (siempre la misma, α = 0) con cada una de sus derivadas,

de hecho, hasta el orden e + n−1.

(b)⇒(c): La existencia de inﬁnitos n´umeros primos garantiza que existen inﬁnitos enteros

e ≥ 1 tales que n + e −1 es un n´umero primo (resp., n + e es un n´umero primo) y que

entonces nos sit´uan en la circunstancia (i) (resp., atendiendo al corolario 3.3.2, en la

circunstancia (ii)). Para un valor e que presente estas caracter´ısticas, la conjetura de

desplazamiento general asegura el cumplimiento de las restantes condiciones.

(c)⇒(a): Sea Pn(X) = Xn + ( n
2 )b2 Xn-2 + . . . + ( n
n-1)bn-1 X veriﬁcando las hip´otesis de

Casas-Alvero. La conjetura de desplazamiento selectivo proporciona cierto entero e tal

que el polinomio
 X e · P(X) = X e+n + ( n
2 )b2 X e+n-2 + . . . + ( n
n-1)bn-1 X e+1

satisface todas la hip´otesis de la conjetura de Casas-Alvero de grado N = e + n, sabiendo

efectivamente que dicha conjetura es cierta en grado N o bien, en su defecto, que se tiene

N = p r + 1 o 2p r + 1 , de modo que puede aplicarse el teorema 3.6.2. Cualquiera de estas

opciones excluye la posibilidad de que X e · P(X) sea un contraejemplo a la conjetura de

Casas-Alvero de grado N, luego necesariamente es

X e · P(X) = XN = Xe+d y, por tanto, Pn(X) = Xn,

como se quer´ıa demostrar. □

Observaci´on 3.6.7. Las conjeturas de desplazamiento admiten tambi´en una formulaci´on

en t´erminos algebraicos-geom´etricos an´aloga a la vista en 3.6.5 para las conjeturas de

propagaci´on. En el caso actual, puesto que las e condiciones de que X e · Pn(X) compar-

ta una ra´ız con sus derivadas de orden menor o igual que e se veriﬁcan trivialmente,

bastar´a considerar las resultantes dadas por

H ′[d,k ] := Res
(Pn, ( X ePn)[k ] ) ∈ C[
b2, . . . , bn-1]

para k = e + 1, . . . , e + n−2, y el ideal I ′
e generado por los polinomios H ′[d,k ].

Las conjeturas de desplazamiento aﬁrman, entonces, que —para todo e, o bien para

un e espec´ıﬁco, seg´un el caso—, se tiene la inclusi´on V (I ) ⊂ V (I ′
e ) o, equivalentemente,

que para cada i = e + 1, . . . , e + n −2 existe un exponente mi ∈ N tal que (H ′[d,i ])mi ∈ I.

3.6 Conjeturas de transmisi´on de hip´otesis 65

Observaci´on 3.6.8. Merece la pena observar que, si bien el producto por X e desplaza

los coeﬁcientes de Pn(X), no desplaza en cambio la presentaci´on bin´omica del mismo.

En efecto, el coeﬁciente ( n
n−i) bn−i de Xi en Pn(X) se desplaza para ser el coeﬁciente de

X e +i en X e·Pn(X), pero en la presentaci´on bin´omica propia de este polinomio el coeﬁciente

de X e +i debe ser del tipo (e+n
n−i) b ′
n−i. La diﬁcultad de probar la conjetura de Casas-Alvero

se puede interpretar como la de probar las conjeturas de desplazamiento, cuyo enunciado

anal´ıtico tiene una visible fuerte dependencia del manejo y de las propiedades de los

n´umeros combinatorios.

3.6.3. Enunciado transversal al grado

Cada vez que hemos expresado el enunciado de la conjetura de Casas-Alvero en cualquiera

de sus formas equivalentes, incluso bajo las modalidades de conjetura de propagaci´on o

conjetura de desplazamiento, ha sido preciso hacer alguna referencia expl´ıcita al grado n.

Esto es, en realidad no estamos hablando de una conjetura, sino de inﬁnitas conjeturas

—una por cada entero n ∈ N— algunas de las cuales han dejado de serlo, puesto que ya

han sido demostradas.

Como consecuencia inmediata del teorema 3.6.6 obtenemos un enunciado independien-

te de n que equivale a la que propiamente cabr´ıa llamar la conjetura de Casas-Alvero —por

contemplar la totalidad de los grados—. El nuevo enunciado ya no se formula por grados y

no admite ning´un tipo de discriminaci´on basada en el grado, esto es, que pueda ser cierta

en algunos grados pero no en otros; por el contrario, expresa la transferencia de ciertas

propiedades entre polinomios de grados sucesivos.

Corolario 3.6.9. Las siguientes aﬁrmaciones son equivalentes:

(a) La conjetura de Casas-Alvero de grado n es cierta para todo entero positivo n.

(b) Si P(X) ∈ C es un polinomio que carece de t´ermino vicel´ıder y comparte una ra´ız con

cada una de sus derivadas de grado positivo entonces el polinomio X·P(X) comparte

una ra´ız con cada una de sus derivadas de grado positivo.

Demostraci´on. (a)⇒(b): Es inmediato, pues siendo cierto (a) y bajo las hip´otesis de (b),

no puede sino ser P(X) = Xn (para cierto n) y, por tanto, X · P(X) = Xn+1.

(b)⇒(a): Dado Pn(X) = Xn + ∑n-2
i=1 ( n
n-i)bn-i Xi ∈ C[ X] satisfaciendo las hip´otesis de la

conjetura de Casas-Alvero de grado n, y ﬁjado e ∈ N, podemos aplicar (b) sucesivamente a

los polinomios P(X), X·P(X), X2·P(X), . . . , Xe−1·P(X) para obtener que X e·P(X) com-

parte una ra´ız con cada una de sus derivadas, de hecho, hasta el orden n + e −1. Concluimos

66 Cap´ıtulo 3. Usando esquemas proyectivos

de aqu´ı que es verdadera la conjetura de desplazamiento —general o espec´ıﬁca, seg´un se

quiera— de grado n, equivalente, tal como establece 3.6.6, a la conjetura de Casas-Alvero

de ese mismo grado. □

Cap´ıtulo 4

Condensaci´on y expansi´on

La primera proposici´on recogida en esta Memoria, ya en la secci´on 1.1, consisti´o en re-

ducir la conjetura de Casas-Alvero —sin ninguna p´erdida de generalidad— al conjunto

de los polinomios sin t´ermino vicel´ıder. Consecuentemente con ello, en todos los desarro-

llos posteriores y, en particular, en la construcci´on del esquema Yn, se ha trabajado bajo

ese supuesto, que nos libraba de dos indeterminadas y de una ecuaci´on. Tiene sentido

plantearse cu´al ser´ıa el comportamiento del esquema Yn
′′, an´alogo a Yn , que prescindiendo

de la preparaci´on de Tschirnhausen partiera del polinomio general de grado n presentado

en forma bin´omica,

Pn(X) = Xn + ( n
1 )b1 Xn-1 + ( n
2 )b2 Xn-2 + · · · + ( n
n-2)bn-2 X2 + ( n
n-1)bn-1 X + ( n
n )bn

y, empleando las resultantes H [i] := Res(P n, P n
[i]) ∈ Z[b1, b2, . . . , bn], quedara deﬁnido

como subesquema de P n−1
1,2,. . . ,n por las n−1 ecuaciones H [1] = H [2] = . . . = H [n-1] = 0.

Pues bien: con este esquema, la respuesta aﬁrmativa al problema de Casas-Alvero

no se caracteriza por que Y ′′
n(C) sea vac´ıo, sino por poseer Y ′′
n(C) ´unicamente un pun-

to, [˜α] = [
(−α, α2, −α3, . . . , (−α)
n)
]
, correspondiente a los inﬁnitos polinomios de la forma
(X − α)n con α ̸= 0 que no cumplen b1 = b2 = . . . = bn = 0 pero que no contradicen a la

conjetura de Casas-Alvero. La presencia de este punto resulta un inconveniente que se

logra evitar imponiendo a Pn(X) la condici´on de que una de sus ra´ıces sea nula, esto es,

que sea nulo el t´ermino independiente bn.

4.1. El supraesquema Yn
′

Se considera el polinomio gen´erico de grado n y t´ermino independiente nulo

Pn(X) = Xn + ( n
1 )b1 Xn-1 + ( n
2 )b2 Xn-2 + · · · + ( n
n-2)bn-2 X2 + ( n
n-1)bn-1 X

68 Cap´ıtulo 4. Condensaci´on y expansi´on

y, para cada i = 1, . . . , n−1, se deﬁne H [i]:=Res(P n, P n
[i]) ∈ Z
[
b1, b2, . . . , bn-1]
. Denotamos

por Yn
′ al subesquema del espacio proyectivo pesado P n−2
1,2,. . . ,n-1 deﬁnido por las ecuaciones

H [1] = H [2] = . . . = H [n-1] = 0.

Observaci´on 4.1.1. Suprimida por construcci´on la posibilidad de tener Pn(X) = (X − α)n

con α ̸= 0, ahora s´ı que se veriﬁca la equivalencia que se expresa como sigue:

Yn
′(C) = ̸O si y solo si es verdadera la conjetura de Casas-Alvero de grado n.

Por otra parte, dado que es

Pn
[k ](X) = Xn-k + (n-k
1 )b1 Xn-1-k + (n-k
2 )b2 Xn-2-k + . . . + (n-k
n-k)bn-k,

la condici´on bn-k = 0 garantiza que Pn(X) y Pn
[k ](X) comparten la ra´ız α = 0 ; esto es,

haciendo bn-k = 0 se satisface autom´aticamente la ecuaci´on k-´esima del sistema, H [k ] = 0.

Tambi´en de esta interesante cualidad carece el esquema Yn
′′ mencionado anteriormente,

por lo que renunciamos a utilizarlo en lo sucesivo.

Observaci´on 4.1.2. En el contexto del cap´ıtulo 3 no se contemplaba a b1 como variable, y

tanto Yn como todos los dem´as esquemas Z n,I eran vistos como subesquemas de P n−3
2,. . . ,n-1.

Sin m´as que introducir a b1 = 0 como la ecuaci´on (n−1)-´esima del sistema que lo deﬁne,

cada uno de estos esquemas pasa a ser considerado subesquema del espacio proyectivo

pesado P n−2
1,2,. . . ,n-1.

En este escenario, Yn
′ se incorpora de forma natural a esta familia de esquemas al

identiﬁcarse con Z n,J ′ para J ′ = {1, 2, . . . , n−1
}. Su relaci´on con todos ellos responde a

la misma l´ogica que ya conocemos, incluido el abuso de notaci´on que supone denominar

a las resultantes de forma indiferenciada como H [i] aunque est´en ligadas a conjuntos de

exponentes distintos. Es claro que tanto Yn = Z n,J como los restantes esquemas Z n,I son

subesquemas de Yn
′ , de modo que este ejerce como un supraesquema que encabeza toda

la jerarqu´ıa.

La proposici´on 1.1.2, seg´un la cual existen contraejemplos a la conjetura de Casas-

Alvero de grado n si y solo si existe alg´un contraejemplo de grado n sin t´ermino vicel´ıder,

se traduce en la siguiente equivalencia:

Yn
′( C) = ̸O ⇐⇒ Yn( C) = ̸O.

Ser´a de gran utilidad establecer el resultado an´alogo a este que, en lugar de al cuerpo C, se

reﬁera a los cuerpos Fp . Como paso previo necesitamos el siguiente lema, donde se muestra

4.1 El supraesquema Yn
′ 69

c´omo, en caracter´ıstica p, la derivaci´on neta y el cambio de variable correspondiente a una

traslaci´on son operaciones que conmutan. Esto no es ninguna trivialidad: en el comentario

3.2.4 ya se puso de maniﬁesto el peculiar comportamiento de la derivaci´on neta en carac-

ter´ıstica p, que de hecho solo queda bien deﬁnida cuando se aplica, no ya a polinomios que

admitan una presentaci´on bin´omica, sino a lo que llamamos polinomios presentados, esto

es, los que vienen acompa˜nados de una presentaci´on bin´omica expl´ıcitamente ﬁjada.

Lema 4.1.3 (Regla de la cadena para la derivada neta en caracter´ıstica p). Se

considera un polinomio presentado de grado n y coeﬁcientes en Fp ,

Pn(X) = c0 Xn + ( n
1 )c1 Xn-1 + ( n
2 )c2 Xn-2 + · · · + ( n
n-2)cn-2 X2 + ( n
n-1)cn-1 X + ( n
n )cn,

y se considera asimismo el cambio de variable X = ̃X −a. En estas condiciones,

(a) El polinomio Pn( ̃X−a) ∈ Fp[ ̃X ] viene dado como un polinomio presentado, con una

presentaci´on inducida por la de Pn(X).

(b) Si se considera, para cada j = 1, 2, . . . , n−1, la derivada neta de orden j del polinomio

presentado Pn(X),

Pn
[j ](X) = c0 Xn-j + (n-j
1 )c1 Xn-1-j + (n-j
2 )c2 Xn-2-j + · · · + (n-j
n-j)cn-j,

entonces, para todo j = 1, 2, . . . , n−1 se veriﬁca: (Pn( ̃X−a))[j ] = Pn
[j ]( ̃X−a).

Demostraci´on. Al realizar en Pn(X) el cambio de variable X = ̃X −a, se obtiene

Pn(X) = Pn( ̃X−a) =

= ( n
0 )c0( ̃X−a)n + ( n
1 )c1( ̃X−a)n-1 + . . . + ( n
i )ci( ̃X−a)n-i + . . . + ( n
n ) cn = (4.1)

= B0 ̃X n + B1 ̃X n-1 + . . . + Bk ̃X n-k + . . . + Bn.

El desarrollo de (4.1) proporciona, expresado en t´erminos de los ci, el coeﬁciente de ̃X n-k,

Bk = ( n
0 ) c0( n
k )(−a)k + ( n
1 ) c1(n-1
k-1)(−a)k-1 + . . . + ( n
i ) ci(n-i
k-i)(−a)k-i + . . . + ( n
k ) ck(n-k
0 ).

(4.2)

En este momento vuelve a ser de aplicaci´on la igualdad (2.13) sobre la que trata el co-

mentario 2.3.5; en este caso y para los n´umeros i ≤ k < n nos conviene expresarla bajo la

forma ( n
i
 )( n−i
k −i
 ) = ( n
k
 )( k
i
 ),

70 Cap´ıtulo 4. Condensaci´on y expansi´on

la cual nos permite sustituir el producto de los dos n´umeros combinatorios presentes en

cada uno de los t´erminos de (4.2) por otro producto en el que siempre ﬁgura el factor ( n
k ).

De este modo, sacando factor com´un, resulta

Bk = ( n
k
 )[ k∑

i=0
 ( k
i
 ) ci (−a)k-i ]
. (4.3)

Esto demuestra el primer apartado del lema, ya que, sin m´as que denotar por bk al con-

tenido del corchete en la expresi´on (4.3), se tiene

Pn( ̃X−a) = ( n
0 )b0 ̃X n + ( n
1 )b1 ̃X n-1 + . . . + ( n
i )bi ̃X n-i + . . . + ( n
n ) bn,

donde cada bi ∈ Fp est´a perfectamente determinado a partir de los datos c0, c1, . . . ,cn-1, a ∈

Fp. Observemos que, en consecuencia, tambi´en est´an deﬁnidas las derivadas netas del

polinomio presentado Pn( ̃X−a); en efecto,

(Pn( ̃X−a) )[j ]
= (n-j
0 )b0 ̃X n-j + (n-j
1 )b1 ̃X n-j -1 + . . . + (n-j
i )bi ̃X n-j -i + . . . + (n-j
n-j) bn-j.

(4.4)

Por otra parte, si el cambio de variable se efect´ua en Pn
[j ](X), resulta

Pn
[j ](X) = P [j ]
n ( ̃X−a) =

= (n-j
0 )c0( ̃X−a)n-j + (n-j
1 )c1( ̃X−a)n-j -1 + . . . + (n-j
i )ci( ̃X−a)n-j -i + . . . + (n-j
n-j) cn-j =

= D0 ̃X n-j + D1 ̃X n-j -1 + . . . + Dk ̃X n-j -k + . . . + Dn-j .
(4.5)

Igual que antes, del desarrollo de las potencias en la l´ınea central de (4.5) se obtiene el

coeﬁciente del t´ermino de grado n−j −k, que es

Dk = (n-j
0 )c0(n-j
k )(−a)k + (n-j
1 )c1(n-j-1
k-1 )(−a)k-1 + . . . + (n-j
i )ci(n-j-i
k-i )(−a)k-i + . . . + (n-j
k )ck(n-j-k
0 ).

De nuevo, el uso de la identidad (2.13), ahora bajo la forma (n-j
i )(n-j -i
k-i ) = (n-j
k )( k
i ) ,

permite reescribir Dk , y el resultado es

Dk = ( n-j
k
 )[ k∑

i=0
 ( k
i
 ) ci (−a)k-i ]
.

Observamos que el contenido del corchete es justo el mismo que aparec´ıa en (4.3), al que

hab´ıamos denotado bk; de modo que, para todo k = 0, 1, . . . , n−j, se cumple la igualdad

Dk = ( n-j
k
 )
bk. Transladando estas igualdades a (4.5) y confrontando el resultado con (4.4)

resulta evidente que es, en efecto,

(Pn( ̃X−a))[j ] = Pn
[j ]( ̃X−a)

4.1 El supraesquema Yn
′ 71

tal como aﬁrma el segundo apartado del lema. □

Si el lema 4.1.3 ha validado en caracter´ıstica p la regla de la cadena para la derivaci´on

neta, otro tanto hab´ıa hecho el lema 3.2.1 con la posibilidad de seguir identiﬁcando cada

soluci´on del sistema H [1] = . . . = H [n−1] = 0 con un polinomio Pn que comparta ra´ıces con

los sucesivos Pn
[i], incluso cuando el cuerpo base es Fp. Ambos lemas son esenciales en la

demostraci´on del siguiente teorema.

Teorema 4.1.4 (Eliminaci´on del vicel´ıder en caracter´ıstica p). Dado n ≥ 3 se con-

sideran los esquemas proyectivos Yn
′ = Z n,J ′ e Yn = Z n,J . Para todo n´umero primo p se

veriﬁca la equivalencia Yn
′( Fp ) = ̸O ⇐⇒ Yn( Fp ) = ̸O.

Demostraci´on. (⇒) Es una obviedad, pues se tiene la inclusi´on Yn( Fp ) ⊂ Yn
′( Fp ).

(⇐) Esta implicaci´on se va a demostrar bajo su forma contrarrec´ıproca,

Yn
′( Fp ) ̸= ̸O =⇒ Yn( Fp ) ̸= ̸O.

Supongamos que existe alg´un punto [c] = [
(c1, . . . , cn-1)
] ∈ Yn
′( Fp ).

• Si es c1 = 0, entonces [c] pertenece, de hecho, a Yn( Fp ), y hemos terminado.

• Si es c1 ̸=0, entonces, tomando por ejemplo a (c1, . . . , cn-1)∈F n-1
p ∖{(0, . . . , 0)} como re-

presentante ﬁjo de [c] tendremos un polinomio presentado, Pn(X) = Xn
+
∑n-1
i=1 ( n
i )ci Xn-i ∈

Fp[ X], que comparte una ra´ız en Fp con cada una de sus derivadas netas; as´ı pues

Para cada j = 1, . . . , n −1, existe αj ∈ Fp cumpliendo Pn(αj) = Pn [j ](αj) = 0

Mediante el cambio de variable X = ̃X −c1, obtenemos el polinomio presentado

Q( ̃X ) = Pn( ̃X −c1) = ̃X n + ( n
1 )b1 ̃X n-1 + . . . + + ( n
n-1)bn-1 ̃X + ( n
n ) bn ∈ Fp[ ̃X ]; (4.6)

seg´un la f´ormula (4.3), el coeﬁciente de ̃X n-1 es ( n
1 )[−c1 + c1] = ( n
1 ) · 0 , de modo que se

tiene b1 = 0 .

Por otra parte, para cada j = 1, . . . , n −1, el elemento βj = αj + c1 ∈ Fp va a ser una ra´ız

compartida por los polinomios Q( ̃X ) y Q
[j ]( ̃X ), pues se cumple

Q(βj) = Pn(βj −c1) = Pn(αj) = 0

Q[j ](βj) = P [j ]
n (βj −c1) = P [j ]
n (αj) = 0.

(la l´ınea anterior hace uso de la igualdad Q[j ]( ̃X ) = (Pn( ̃X −c1)
)[j ] = Pn
[j ]( ̃X −c1) ,

obtenida mediante el lema 4.1.3)

Observemos que, en particular, el hecho de que Q( ̃X ) y Q[n-1]( ̃X ) = ̃X + b1 = ̃X

compartan una ra´ız signiﬁca que es, necesariamente, bn = 0 .

72 Cap´ıtulo 4. Condensaci´on y expansi´on

Se concluye que los coeﬁcientes bi del polinomio presentado dado en (4.6) conﬁguran

una soluci´on sobre Fp del sistema homog´eneo H [1] = . . . = H [n−1] que tiene b1 = bn = 0, pero

que no puede ser la soluci´on trivial. En efecto, si lo fuera, entonces tendr´ıamos Q( ̃X ) = ̃X n,

con lo cual quedar´ıa

Pn(X) = Pn( ̃X −c1) = Q( ̃X ) = ( X + c1)
n = Xn + · · · + c n
1 , con c n
1 ̸= 0, por serlo c1;

cosa absurda puesto que Pn(X) carec´ıa de t´ermino independiente.

Hemos hallado un punto, b = [(0, b2, . . . , bn-1)] ∈ P n−2
1,2,. . . ,n-1(Fp), que sin duda pertenece

a Yn( Fp ); queda as´ı probado que este conjunto no es vac´ıo. □

4.2. El m´etodo de condensaci´on

El teorema que a continuaci´on se expone constituye en s´ı mismo una propuesta de

actuaci´on frente al problema de Casas-Alvero. Su demostraci´on describe un proceso, que

llamaremos de condensaci´on, mediante el cual cierto enunciado en grado n = hpr se trans-

forma en el enunciado an´alogo en grado h, con el sorprendente resultado de que ambos

enunciados son equivalentes. Es destacable el decisivo papel desempe˜nado aqu´ı por el

teorema (4.1.4) de eliminaci´on del vicel´ıder en caracter´ıstica p.

Teorema 4.2.1 (Resoluci´on por condensaci´on). Sea p un n´umero primo, y sean h

y r dos n´umeros naturales con h ≥ 3 y r > 0. Se veriﬁca la equivalencia

Yhpr ( Fp ) = ̸O ⇐⇒ Yh( Fp ) = ̸O.

Demostraci´on. Sea n = hp r. Consideramos el polinomio

Pn(X) = Xn + ( n
2 )b2 Xn-2 + · · · + ( n
n-1)bn-1 X .

Utilizaremos los resultados sobre congruencias recogidos en la proposici´on 3.4.1. Por de

pronto, se sabe que solo es ( hpr

j
 ) ̸≡ 0 mod p para j = 0, pr, 2pr, . . . , hpr, de modo que es

Jp = {p r, 2p r, · · · , (h−1)p r}. Entonces, la reducci´on m´odulo p nos deja

Pn(X) = Xhpr + ( hpr

pr ) bpr X(h-1)pr + ( hpr

2pr ) b2pr X(h-2)pr + . . . + ( hpr

(h-1) pr ) b(h-1)pr Xpr

y, adem´as, para cada k = i · p r con i = 1, . . . , h−1,

Pn
[k ](X) = Pn
[ipr ](X) = X(h-i)pr+ ( (h-i)pr

pr ) bpr X(h-i-1)pr+ ( (h-i)pr

2pr ) b2pr X(h-i-2)pr +

+ . . . + ( (h-i)pr

(h-i + 1) pr ) b(h-i + 1)pr Xpr + ( (h-i)pr

(h-i) pr ) b(h-i)pr .

4.2 El m´etodo de condensaci´on 73

Sabemos asimismo que es ( hpr

j pr ) ≡ ( h
j
 ) mod p, y tambi´en ( (h-i)pr

j pr ) ≡ ( h-i
j
 ) mod p ,

y podemos observar que en todas las potencias de X que aparecen en los anteriores poli-

nomios reducidos el exponente es un m´ultiplo de p r; entonces, si introducimos una nueva

variable Y = Xpr , en caracter´ıstica p ser´a v´alido escribir

Pn(X) = Y h + ( h
1
 ) bpr Y h-1 + . . . + ( h
h-1
) b(h-1)pr Y (4.7)

y, para cada i = 1, . . . , h−1,

Pn
[ipr ](X) = Y h-i + ( h-i
1
 ) bpr Y h-i-1 + . . . + ( h-i
h-i
 ) b(h-i)pr . (4.8)

Si denotamos por Qh(Y ) al polinomio en (4.7) se observa que, para cada i = 1, . . . , h−1,
el polinomio en (4.8) es justo Q[i]
h (Y ). El hecho que Pn(X) y Pn
[ipr ](X) compartan una
ra´ız α ∈ Fp, traducido en que se veriﬁquen las igualdades

α hpr + h-1∑

j=1
 ( h
j
 ) bj pr α(h-j)pr = 0

α(h-i)pr + h-i∑

j=1
 ( h-i
j
 ) bj pr α(h-i-j)pr = 0 ,

admite ahora la lectura alternativa —y equivalente— de que Qh(Y ) y Q[i]
h (Y ) compartan

en Fp la ra´ız β = α pr .

As´ı pues, acerca de una (h-1)-upla (bpr , b2pr , . . . , b(h-1)pr ) ̸= (0, 0, . . . , 0) de elementos

de Fp , es indistinto aﬁrmar

P
hpr(X) = Xhpr+
 h-1∑

j=1
 ( hpr
jpr ) bjpr X(h-j)pr comparte la ra´ız αi ∈ Fp con Phpr
[ipr ]
(X) ∀i = 1, . . . , h-1,

(4.9)
que aﬁrmar

Q
h(Y ) = Y h +
 h-1∑

j=1
 ( h
j ) bjpr Y (h-j) comparte la ra´ız α pr

i ∈ Fp con Q
h

[i](Y ) ∀i = 1, . . . , h-1,

(4.10)
luego la existencia de un polinomio P
hpr(X) distinto de Xhpr que satisfaga (4.9) es solidaria

con la existencia de un polinomio Q
h(Y ) distinto de Y h que satisfaga (4.10). En otros

t´erminos (confrontar con el lema 3.2.1 y comentario 3.2.4), existe sobre Fp una soluci´on

no trivial del sistema homog´eneo de hpr−1 ecuaciones y otras tantas inc´ognitas

que deﬁne al esquema Z hpr,{pr,2pr,...,(h-1)pr} = Z n,Jp , a saber,

H [pr ] = H [2pr ] = . . . = H [(h-1)pr ] = 0, bn-j = 0 ∀j ̸= pr, 2pr . . . , (h−1)pr,

si y solo si existe sobre Fp una soluci´on no trivial del sistema de h−1 ecuaciones en las

74 Cap´ıtulo 4. Condensaci´on y expansi´on

inc´ognitas cj = bjpr , j = 1, 2, . . . , h−1 que deﬁne al esquema Z h, {1, 2, . . . , h-1} = Y h
′ ,

H[1] = H[2] = · · · = H[h-1] = 0.

—se emplea diferente graf´ıa porque las ecuaciones corresponden a un sistema distinto del

anterior—. Hemos demostrado as´ı que se veriﬁca

Zn,Jp( Fp ) = ̸O ⇐⇒ Y h
′( Fp ) = ̸O,

implicaci´on que ocupa la posici´on central en la siguiente cadena:

Yhpr ( Fp ) = Zhpr,J ( Fp ) = ̸O ⇔ Zhpr,Jp( Fp ) = ̸O ⇔ Y h
′( Fp ) = ̸O ⇔ Y h( Fp ) = ̸O.

Pero primera implicaci´on de la cadena viene justiﬁcada por el teorema (3.3.5) de resoluci´on

por elevaci´on, y la ´ultima es justamente el teorema (4.1.4) de eliminaci´on de vicel´ıder en

caracter´ıstica p. La demostraci´on est´a, por tanto, completa. □

Corolario 4.2.2. La conjetura de Casas-Alvero es verdadera para todo n´umero de la forma

n = 4p r, siendo p ̸= 3, 5, 7.

Demostraci´on. La proposici´on 3.1.4 garantiza la veracidad de la conjetura de Casas-Alvero

para todos aquellos n´umeros de la forma n = 4p r tales que sea Y4pr ( Fp ) = ̸O; ahora bien,

seg´un el teorema de condensaci´on 4.2.1, esto ´ultimo sucede si y solo si es Y4( Fp ) = ̸O.

Al ser P4(X) = X4 + ( 4
2
 )b2 X2 + ( 4
3
 )b3 X un polinomio con solo dos t´erminos adi-

cionales al l´ıder, resulta que el conjunto completo de exponentes a considerar es J = {1, 2},
de modo que el esquema Y4 es simplemente Z 4,{1,2}. En estas condiciones podemos
aplicar el teorema 3.5.1, apartado b), teniendo en cuenta que es i = 1, j = 2 y, por tanto:

a = ( 4
1
 ) = 4; b = ( 4
2
 ) = 6; c = ( 3
2
 ) = 3; d = m.c.d.
(2, 1) = 1; ρ = 2

1 = 2, σ = 1

1 = 1.

Dicha proposici´on aﬁrma que Y4( Fp ) = Z4,{1,2}( Fp ) es vac´ıo si y s´olo si se cumple la terna

de condiciones

(i) 4 ̸≡ 1 mod p

(ii) 6 ̸≡ 1 mod p

(iii) 42 (6 − 3
)2(6 − 12)1 − (−1)1(4 −1
)3(6 −1
)2 = − 33 · 7 ̸≡ 0 mod p.

Los ´unicos primos que incumplen alguna de estas condiciones son p = 3, p = 5 y p = 7;

para todos los restantes es Y4( Fp ) = ̸O, tal como se quer´ıa demostrar. □

4.2 El m´etodo de condensaci´on 75

Ejemplo. El problema de Casas-Alvero en grado n = 4 · 11
3 = 5324 nos hace considerar

el polinomio P5324(X) = X5324 + ∑5323
i=2 (5324
i
 ) bi X5324 - i, as´ı como sus 5322 primeras

derivadas.

Puesto que es 11
3 = 1331, tenemos J11 = {1331, 2662, 3993
}, por lo que, al reducir

m´odulo 11, basta considerar tan solo los polinomios

P5324(X) = X5324 + ( 5324
1331
) b1331 X3993 + ( 5324
2662
) b2662 X2662 + ( 5324
3993
) b3993 X1331,

P5324
[ 1331 ](X) = X3993 + ( 3993
1331
) b1331 X2662 + ( 3993
2662
) b2662 X1331 + b3993 ,

P5324
[ 2662 ](X) = X2662 + ( 2662
1331
) b1331 X1331 + b2662 ,

P5324
[ 3993 ](X) = X1331 + b1331 ;

los cuales, mediante el cambio X1331 = Y , y siendo ( h · 11
3

k · 11
3 ) ≡ ( h
k
 ) mod 11, se reescriben

simplemente como

Q4(Y ) = Y 4 + ( 4
1
 ) b1331 Y 3 + ( 4
2
 ) b2662 Y 2 + ( 4
3
 ) b3993 Y ,

Q
4
[1](Y ) = Y 3 + ( 3
1
 ) b1331 Y 2 + ( 3
2
 ) b2662 Y + b3993 ,

Q
4
[2](Y ) = Y 2 + ( 2
1
 ) b1331 Y + b2662 ,

Q
4
[3](Y ) = Y + b1331 .

(Aqu´ı, si se preﬁere, se puede denotar b1331·i como ci). Obs´ervese que, a diferencia de

P5324(X), el polinomio Q4(Y ) s´ı que cuenta con t´ermino vicel´ıder.

Las condiciones acerca de P5324(X) que identiﬁcan cu´ando un punto [(0, b2 , . . ., b5323 )]

que tenga nulas todas las componentes de sub´ındice distinto de 1331, 2662, 3993, pertenece

a Y5324( F11 ), coinciden exactamente con las condiciones acerca de Q4(Y ) que caracterizan

cu´ando el punto [( b1331 , b2661 , b3993 )] = [(c1, c2, c3)] pertenece a Y 4
′( F11 ).

As´ı pues, existe un punto en Z5324,{1331,2662,3993}( F11 ) si y solo si existe un punto en

Y 4
′( F11 ). Sab´ıamos ya que lo primero equivale a que sea distinto de vac´ıo el conjunto

Y5324( F11 ) (teorema de elevaci´on), y que lo segundo equivale a que sea distinto de vac´ıo

el conjunto Y4( F11 ) (teorema de eliminaci´on del vicel´ıder en caracter´ıstica p).

En deﬁnitiva, se tiene la equivalencia: Y5324( F11 ) ̸= ̸O si y solo si Y4( F11 ) ̸= ̸O.

Pero la cuesti´on de si existen o no puntos en Y4( Fp ) ya la tenemos resuelta, de hecho,

para todo p (ver la demostraci´on del corolario 4.2.2), y sabemos que es Y4( F11 ) = ̸O. De

modo que tambi´en es Y5324( F11 ) = ̸O , lo cual garantiza que es verdadera la conjetura de

Casas-Alvero de grado 5324.

76 Cap´ıtulo 4. Condensaci´on y expansi´on

4.3. El principio de expansi´on

Dado un n´umero n, el inter´es en disponer de un primo p tal que sea

Yn( Fp ) = ̸O (4.11)

se debe a la proposici´on 3.1.4, seg´un la cual (4.11) constituye una condici´on suﬁciente para

que el problema de Casas-Alvero de grado n reciba respuesta aﬁrmativa. Para expresar

que n y p veriﬁcan tan ventajosa condici´on diremos que p es un primo eﬁcaz con n, y

tambi´en que el par (n, p) es un par eﬁcaz .

Vamos a indagar acerca de c´omo son los pares eﬁcaces, y de qu´e modo pueden obtenerse.

Comenzamos por enunciar un resultado que en realidad ya conocemos, y que presenta como

´unica novedad el ´enfasis en una determinada perspectiva.

Principio de Expansi´on. Si h es un n´umero natural con h ≥ 3, y p es un primo,

siendo p > h, entonces para todo r > 0 se veriﬁca

Yh( Fp ) = ̸O =⇒ Yhpr ( Fp ) = ̸O.

En efecto, el reci´en bautizado principio no es otra cosa que la lectura de derecha a

izquierda del teorema de condensaci´on, 4.2.1, para el caso particular de que sea h < p. En

la terminolog´ıa reci´en introducida, el principio de expansi´on dice lo siguiente:

Principio de Expansi´on. Si (h, p) es un par eﬁcaz, siendo 3 ≤ h < p, entonces los in-

ﬁnitos pares de la forma (hp r, p) con r ∈ N son tambi´en pares eﬁcaces.

A un par eﬁcaz (h, p) cumpliendo h < p lo llamaremos par eﬁcaz b´asico; al conjunto

formado por los inﬁnitos pares eﬁcaces de la forma (hp r, p) con r ∈ N lo denominaremos

estela de (h, p). Dado que todo par de la forma (p r, p) o (2p r, p) es siempre eﬁcaz —

corolarios 3.3.2 y 3.5.4, respectivamente—, convendremos en considerar a los pares (1, p)

y (2, p) como pares eﬁcaces b´asicos, y escribiremos Y1( Fp ) = ̸O e Y2( Fp ) = ̸O recurriendo

a unos esquemas Y1 e Y2 carentes de entidad geom´etrica (ver nota 3.0.5). De este modo,

tanto el teorema 4.2.1 como el principio de expansi´on resultan v´alidos tambi´en para h = 1

y h = 2, lo que permite eliminar la restricci´on h ≥ 3.

Veremos a continuaci´on c´omo cada par eﬁcaz (n, p) remite a un ´unico par b´asico (h, p),

a cuya estela pertenece.

Teorema 4.3.1. Sea (n, p) un par eﬁcaz con n ≥ p. Existe un ´unico h ∈ N tal que

(i ) Es h < p,

(ii ) n = hp r, para alg´un r > 0,

(iii ) Yh( Fp ) = ̸O;

4.3 El principio de expansi´on 77

de modo que (h, p) es un par eﬁcaz b´asico, y (n, p), un elemento de su estela.

Demostraci´on. Supongamos que el primo p no divide a n , y tomemos el resto k de la
divisi´on eucl´ıdea de n entre p, de modo que es n = c·p + k con 0 < k < p < n. Maniﬁesta-
mente, ( n
k
 ) = (c · p + k) · (c · p + k −1) · · · · · · · · (c · p + 2) · (c · p + 1)

k · (k −1) · · · · · · · · 2 · 1 ≡ 1 mod p

—pues cada factor del numerador es congruente m´odulo p con el factor del denominador

que est´a en la misma posici´on relativa—. Puesto que k pertenece al conjunto completo

de exponentes, J, (por ser 0 < k ≤ n −2), podemos aplicar el teorema 3.5.1, apartado (a),

y obtenemos ̸O ̸= Zn,{k}( Fp ) ⊂ Yn( Fp ),

en contra de que el par (n, k) era eﬁcaz.

Asumimos, pues, que p s´ı divide a n, y por tanto podemos escribir n = h·p r con r > 0

y m.c.d.
(h, p) = 1. Suponemos ahora que h es estrictamente mayor que p, y procedemos

como antes: Al ser h = a·p + k con 0 < k < p < h, —en particular, 0 < kpr < hpr— resulta

( h
k
 ) = (a · p + k) · (a · p + k −1) · · · · · · · · (a · p + 2) · (a · p + 1)

k · (k −1) · · · · · · · · 2 · 1 ≡ 1 mod p

y, por tanto, tambi´en ( hpr

kpr ) ≡ 1 mod p —en aplicaci´on de 3.4.1—; en consecuencia, se

tiene ̸O ̸= Zhpr,{kpr}( Fp ) ⊂ Yn( Fp ),

lo cual de nuevo contradice que el par (n, k ) sea eﬁcaz. Queda as´ı probado que en todo

par eﬁcaz (n, p) en el que sea p < n ha de cumplirse: n = h · p r con r > 0 y h < p, seg´un

aﬁrman los apartados (i) y (ii).

Para probar el apartado (iii) basta aplicar el teorema 4.2.1 de resoluci´on por conden-

saci´on, seg´un el cual, si fuera Yh( Fp ) ̸= ̸O entonces tambi´en habr´ıa de ser Yhpr ( Fp ) ̸= ̸O,

en contra de la hip´otesis. □

Dados n y p, diremos que p es el primo dominante de n si es n = hp r con h < p.

Esto es, si p es un factor primo de n que supera estrictamente al producto h de todos

los factores diferentes de p presentes en la factorizaci´on prima de n. Del teorema anterior

extraemos una conclusi´on inmediata:

Corolario 4.3.2. Para que el par (n, p) , con p ≤ n, pueda ser un par eﬁcaz, es condici´on

necesaria que p sea el primo dominante de n. □

78 Cap´ıtulo 4. Condensaci´on y expansi´on

Observaci´on 4.3.3. (1.) Si es p < n y p no divide a n, o bien si lo divide pero no

es dominante, entonces (n, p) no puede ser un par eﬁcaz. Esto reduce dr´asticamente el

n´umero de pares a tomar en consideraci´on.

(2.) Hay mir´ıadas de n´umeros n que carecen de primo dominante. El primo domi-

nante, si lo hay, debe coincidir con el mayor de los factores primos de n (siendo, por tanto,

´unico), pero no basta con que supere uno a uno a los dem´as factores primos: se pide que

supere al producto de todos ellos, multiplicidades incluidas. Cualquier primo p que ﬁjemos

dominar´a solamente en los n´umeros de la forma n = hp r con h ∈ {1, 2, . . . , p−1}; sin embar-

go, existen inﬁnitos valores de h mayores que p —producto de potencias tan altas como

se quiera de primos peque˜nos— de forma que n = hp r no es dominado, ni por p, ni por

ning´un otro primo . As´ı por ejemplo, salvo que (a, b, c) sea una de las seis conﬁguraciones

para las cuales resulta 2 a · 3 b · 5c ≤ 6, el n´umero n = (2 a · 3 b · 5c) · 7 r carece de primo

dominante sean cuales sean los exponentes a, b, c, r.

(3.) Existen n´umeros que poseen primo dominante, pero con los cuales el primo

dominante resulta no ser eﬁcaz. Por ejemplo, los n´umeros de la forma n = 4·5r, que tienen

al 5 como primo dominante, encuentran que es Y4( F5 ) ̸= ̸O (ver corolario 4.2.2) y por

tanto, en aplicaci´on del teorema 4.2.1, Y4·5r ( F5 ) ̸= ̸O, de modo que ning´un par de la

forma (4 · 5r, 5) es eﬁcaz. Podr´ıamos decir que el par ineﬁcaz b´asico (4, 5) nos deja toda

una estela de pares ineﬁcaces.

(4.) El teorema 3.5.1 caracteriza en t´erminos aritm´eticos cu´ando Zh,{i}( Fp ) e

incluso Zh,{i,j}( Fp ) son diferentes de vac´ıo. Puesto que estos conjuntos de puntos son

subconjuntos del correspondiente Yh( Fp ), cuando aquello ocurra, se tendr´a Yh( Fp ) ̸= ̸O,

y sabremos que tanto (h, p) como todos los dem´as pares de su estela son ineﬁcaces.

(5.) Saber si un n´umero n posee o no primo dominante y, en su caso, encontrarlo, es

sencillo (supuesta la capacidad de factorizar n, claro est´a): basta para ello separar toda la

potencia de su m´aximo factor primo p, y mirar si el correspondiente cofactor h es superado

o no por p.

En caso aﬁrmativo, para saber si p es eﬁcaz con n se necesita determinar si el conjunto

Yn( Fp ) es o no vac´ıo, problema que, gracias al teorema de condensaci´on, queda reducido

a averiguar si lo es Yh( Fp ). La realidad es que, aun tras esta simpliﬁcaci´on, la respuesta

queda en la mayor´ıa de los casos fuera de nuestro alcance.

En esta Memoria, hasta el momento solo para h = 1, 2, 3 y 4 hemos obtenido el listado

espec´ıﬁco de todos los primos p tal que el par (h, p) es eﬁcaz; de inmediato lo obtendremos

para h = 5 y, en el pr´oximo cap´ıtulo, tambi´en para h = 6. Por ahora, para mayores valores

de h, a la pregunta de si el par si (h, p) es eﬁcaz solamente estamos en condiciones dar

4.3 El principio de expansi´on 79

respuesta (negativa, naturalmente) en el eventual caso de que Yh( Fp ) contenga puntos con

solo una o dos componentes no nulas, caso comentado en el apartado anterior; en cambio,

si Yh( Fp ) no contiene tal tipo de puntos, faltar´a todav´ıa por averiguar si es que posee

alg´un punto con 3 o m´as componentes distintas de cero (respuesta negativa a la pregunta),

o si tampoco tiene puntos de esta clase y es, por tanto, vac´ıo (respuesta aﬁrmativa).

En la literatura [CLO-2] se ha comunicado el c´omputo de todos los primos ineﬁ-

caces para h = 7, realizado mediante el empleo de muy soﬁsticados m´etodos y medios

inform´aticos.

Comentario 4.3.4. De acuerdo con las anteriores consideraciones, podemos encuadrar a

cada n´umero natural n en uno de los siguientes tipos (identiﬁcados por sus acr´onimos):

DEf (N´umeros con Dominante Ef icaz): Aquellos cuyo primo dominante p se ha compro-

bado que es eﬁcaz con n, esto es, que satisface Yn( Fp ) = ̸O.

DIn (N´umeros con Dominante Ineﬁcaz): Aquellos de cuyo primo dominante p se tiene

constancia de que veriﬁca Yn( Fp ) ̸= ̸O.

SPD (N´umeros Sin Primo Dominante): Los que carecen de primo dominante.

DSC (Dominante Sin Contrastar): N´umeros poseedores de primo dominante p para los

que se desconoce si Yn( Fp ) contiene alg´un punto o es, por el contrario, vac´ıo.

As´ı, por el momento podemos aﬁrmar:

Son del tipo DEf todos los n´umeros de la forma

• p r, para todo primo p. [Corolario 3.3.2]

• 2p r, para todo primo p. [Corolario 3.5.4]

• 3p r, para todo primo p ̸= 2. [Corolario 3.5.6]

• 4p r, para todo primo p ̸= 3, 5, 7. [Corolario 4.2.2]

Son del tipo DIn todos los n´umeros de la forma 4 · 5 r, 4 · 7 r. [Corolario 4.2.2]
En particular: 20, 28, 100 y 196.

Entre los 100 primeros n´umeros, son del tipo SPD los diecis´eis n´umeros siguientes:

12, 24, 30, 36, 40, 45, 48, 56, 60, 63, 70, 72, 80, 84, 90, 96

y hay otros veintitr´es n´umero del tipo SPD comprendidos entre 101 y 200, que son:

105, 108, 112, 120, 126, 132, 135, 140, 144, 150, 154, 160, 165,
168, 175, 176, 180, 182, 189, 192, 195, 198, 200

80 Cap´ıtulo 4. Condensaci´on y expansi´on

El n´umero 296 = 8 · 37 y todos los dem´as n´umeros de la forma n = 8 · 37r se encuentran

inicialmente en el tipo DSC puesto que desconocemos si su primo dominante, p = 37,

es o no eﬁcaz con ellos, es decir, si es o no vac´ıo el conjunto Y8( F37 ). Sabemos que el

sistema homog´eneo en las seis inc´ognitas b2, · · · , b7 que deﬁne al esquema Y8 no posee

sobre F37 ninguna soluci´on con solo una o dos componentes no nulas, pues sometiendo

cada una de las 15 posibles combinaciones {i, j} ⊂ J = {1, 2, . . . , 6} al an´alisis indicado

en el teorema 3.5.1 se concluye que en todos los casos es Z8,{i,j}( F37 ) = ̸O, pero ello

no implica que no puedan existir soluciones con tres, cuatro, cinco o seis componentes

no nulas.

La pertenencia a la categor´ıa DSC reviste car´acter provisional : cualquier avance en el

conocimiento de los conjuntos de puntos Yn( Fp ) puede desplazar series enteras de n´umeros

desde DSC hasta DEf o DIn, en donde se instalan con car´acter deﬁnitivo. As´ı por ejemplo:

por efecto del teorema 4.4.3, los n´umeros de la forma n = 5 · 7r y n = 5 · 13r, inicialmente

en situaci´on an´aloga a la referida para n = 8 · 37r, pasar´an inmediatamente a ubicarse en

el tipo DIn y el tipo DEf, respectivamente; de igual modo, por efecto del trabajo [CLO-2],

los n´umeros n = 7 · 19r pasan de DSC a DIn, y los n´umeros n = 7 · 127r, de DSC a DEf. El

n´umero m´as peque˜no cuyo primo dominante no nos consta que haya sido contrastado es

187 = 11 · 17.

Observaci´on 4.3.5. Para los n´umeros n de tipo DEf tenemos garantizada la respuesta

aﬁrmativa al problema de Casas-Alvero de grado n (v´ease el inicio de esta secci´on). Para

los n´umeros n de tipo SPD o DIn se conoce la imposibilidad de que exista un primo

estrictamente menor que sea eﬁcaz con n, pero nada impide que exista un primo p > n

que s´ı sea eﬁcaz con ´el. En ese caso, el par (n, p) ser´ıa un par eﬁcaz b´asico que da inicio

a una estela de pares eﬁcaces; dicho de otro modo, n estar´ıa ocupando el papel que h

desempe˜na en el Principio de Expansi´on, en virtud del cual todos los n´umeros de la forma

npr (para ese n y ese p particulares) ser´ıan del tipo DEf.

4.4. Niveles de ineﬁcacia

Los primos que no son eﬁcaces con un n´umero n dado se distribuyen en estratos o niveles,

seg´un cu´al sea el m´ınimo n´umero de componentes no nulas de un punto cuando se recorre

el conjunto Yn( Fp ), para el primo p de que se trate. Precisemos esto:

Deﬁnici´on 4.4.1. Dado un primo p ineﬁcaz con el n´umero n, esto es, tal que Yn( Fp ) ̸= ̸O,

diremos que p es ineﬁcaz de nivel k con n si el sistema que deﬁne al esquema Yn,

4.4 Niveles de ineﬁcacia 81

H [1] = H [2] = . . . = H [n-2] = 0, posee sobre Fp alguna soluci´on con exactamente k compo-

nentes distintas de cero, pero no posee ninguna soluci´on con un n´umero de componentes

no nulas inferior a k. En otras palabras, si para todo conjunto de exponentes I de car-

dinal menor que k contenido en el conjunto completo de exponentes J = {1, 2, . . . , n−2},

es Zn,I ( Fp ) = ̸O, pero sin embargo se tiene alg´un conjunto {i1, . . . , ik} ⊂ J —de cardinal

k— tal que Zn,{i1,...,ik}( Fp ) ̸= ̸O. El nivel de ineﬁcacia con n del primo p expresa de cu´al

de las n −2 maneras posibles, excluyentes entre s´ı, se realiza el hecho de que el sistema

anterior posea sobre el cuerpo Fp soluciones no nulas:

Nivel 1: Existe alguna soluci´on con una ´unica componente distinta de cero; es decir, para

alg´un i ∈ J = {1, 2, . . . , n−2} ocurre que es Zn,{i}( Fp ) ̸= ̸O.

Nivel 2 : No se tienen sobre Fp soluciones con una ´unica componente no nula, pero

s´ı con dos. Es decir, existe {i, j} ⊂ J = {1, 2, . . . , n−2} tal que Zn,{i,j}( Fp ) ̸= ̸O, pero

Zn,{k}( Fp ) = ̸O para todo k ∈ J.

. . . . . . . . . . . . . . . . . . . . .

Nivel n −2 : Todas las soluciones no triviales que el sistema posee sobre Fp tienen todas

sus componentes diferentes de cero. Es decir, aunque es Zn,J ( Fp ) = Yn( Fp ) ̸= ̸O,

para todo I subconjunto propio de J se tiene Zn,I ( Fp ) = ̸O .

Observaci´on 4.4.2. Los primos ineﬁcaces de niveles 1 y 2 se localizan aplicando el teo-

rema 3.5.1. En concreto,

p es ineﬁcaz de nivel 1 con n si existe i ∈ J tal que ( n
i
 ) ≡ 1 mod n.

p es ineﬁcaz de nivel 2 con n si no lo es de nivel 1 y adem´as existe {i, j} ⊂ J tal que

el n´umero ∆ i,j = a ρ (b − c
)ρ(b − ac
)σ − (−1)σ(a −1)ρ+σ(b −1
)ρ

—donde a = ( n
i ), b = ( n
j ), c = (n- i
n-j) y ρ = n-j
d , σ = j - i
d , con d = m.c.d.
(n - j, j - i
)—

es m´ultiplo de p.

Cabe se˜nalar que en la demostraci´on del teorema 4.3.1 se prob´o, espec´ıﬁcamente, el resul-

tado siguiente: “Si p es un primo menor que n, y p no divide a n o bien lo divide pero no

es dominante, entonces p es ineﬁcaz de nivel 1 con n”.

Nuestro pr´oximo objetivo ser´a determinar qu´e primos son eﬁcaces con h = 5 y cu´ales no;

para ello hemos de estudiar qu´e soluciones posee sobre Fp el sistema H [1] = H [2] = H [3] = 0

que deﬁne al esquema Y5. Esta tarea es todav´ıa abordable de forma directa con los medios

82 Cap´ıtulo 4. Condensaci´on y expansi´on

de que disponemos, aunque ya requiere el uso de algunas t´acticas y una moderada capaci-

dad de c´alculo aritm´etico.

Teorema 4.4.3. El conjunto de puntos Y5( Fp ) es distinto de vac´ıo si y solo si el primo

p es uno de los siguientes: 2, 3, 7, 11, 131, 193, 599, 3541 y 8009.

Demostraci´on. Recordemos que el esquema Y5 se construye al imponer sobre el polinomio

P5(X) = X5 + ( 5
2
 )
b2 X3 + ( 5
3
 )
b3 X2 + ( 5
4
 )
b4 X

la triple condici´on de que se anulen las resultantes

H [1] = Res(P5(X), P5
[1](X)
) , H [2] = Res(P5(X), P5
[2](X)
) , H [3] = Res(P5(X), P5
[3](X)
).

Sabemos que H [1], H [2] y H [3] son polinomios homog´eneos pesados de grados 20, 15 y 10,

respectivamente, del anillo graduado Z
[
b2, b3, b4] (donde cada bi tiene peso i), y que cada

punto [(β2, β3, β4)]∈Y5( Fp ) corresponde a una familia de ternas {(λ2β2, λ3β3, λ4β4)
}λ ∈ Fp -{0}
que son soluciones no triviales del sistema H [1] = H [2] = H [3] = 0.

Los primos ineﬁcaces con n = 5 de niveles 1 y 2 —esto es, tales que Y5( Fp ) posee alg´un

punto con solo una o dos componentes distintas de cero— los encontramos del modo que

se indica en la observaci´on 4.4.2 :

p es ineﬁcaz con 5 de nivel 1 si y solo si
( 5
1
 ) ≡ 1 mod p, o bien ( 5
2
 ) ≡ 1 mod p, o bien ( 5
3
 ) ≡ 1 mod p,

es decir, si y solo si es 4 ≡ 0 mod p o 9 ≡ 0 mod p. Esto nos da: p = 2 o 3.

p es ineﬁcaz con 5 de nivel 2 si es p ̸= 2, 3, y adem´as es m´ultiplo de p alguno de los

tres n´umeros siguientes (obviamos la transcripci´on de los c´alculos):

∆1, 2 = −2
4 · 3
3 · 193; ∆1, 3 = − 2
8; ∆2, 3 = −11 · 3541.

Esto proporciona los primos p = 11, 193, 3541.

Falta solo encontrar los primos ineﬁcaces con 5 de nivel 3. Reproducimos a continuaci´on el
sistema H [1] = H [2] = H [3] = 0 , adoptando por conveniencia la letras a, b y c para signiﬁcar
las inc´ognitas b2, b3 y b4, respectivamente:

16c
2 · (400 a
4 c − 200 a
3 b2 − 160 a
2 c
2 + 360 a b2 c − 135 b4 + 16 c
3) = 0

b · (2205 a
4 c − 980 a
3 b2 − 1050 a
2 c
2 + 2160 a b2 c − 729 b4 + 125 c
3) = 0 (4.12)

a · (81 a
4 − 90 a
2 c + 100 a b2 + 25 c
2) = 0.

Si (α, β, γ) con α ̸= 0 es soluci´on de este sistema, entonces tambi´en lo es (αλ2, β λ3, γ λ4),

en particular, para λ cumpliendo α·λ2 = 1. Nos interesa caracterizar el hecho de que (4.12)

posea alguna soluci´on con sus tres componentes no nulas, la primera de las cuales podemos

ya suponer que es igual a 1.

4.4 Niveles de ineﬁcacia 83

La terna (1, β, γ) con β, γ ̸= 0 es soluci´on del sistema (4.12) si y solo si el par (β, γ)
lo es del siguiente sistema, m´as simple —se ha prescindido del primer factor en cada
uno de los miembros izquierdos— y ya deshomogeneizado —la inc´ognita a ha sido
sustituida por el valor 1:

400 c − 200 b2 − 160 c
2 + 360 b2 c − 135 b4 + 16 c
3 = 0

2205 c − 980 b2 − 1050 c
2 + 2160 b2 c − 729 b4 + 125 c
3 = 0 (4.13)

81 − 90 c + 100 b2 + 25 c
2 = 0.

Lo anterior sucede si y solo si el par (β2, γ) tiene sus dos componentes distintas
de cero y es soluci´on del siguiente sistema en las inc´ognitas m (que sustituye a b2,
aprovechando que b siempre lleva exponente par) y c:

400 c − 200 m − 160 c
2 + 360 m c − 135 m
2 + 16 c
3 = 0

2205 c − 980 m − 1050 c
2 + 2160 m c − 729 m2 + 125 c
3 = 0

81 − 90 c + 100 m + 25 c
2 = 0.

Puesto que la ´ultima ecuaci´on es lineal en m, podemos despejar dicha inc´ognita:

m = −1

100 (25 c
2 − 90 c + 81); (4.14)

y sustituirla en las dos ecuaciones restantes, obteniendo

−1

2000 (16875 c
4 + 26500 c
3 − 99950 c
2 − 250460 c − 146853
) = 0 (4.15)

−1

10000 (455625 c
4 + 869500 c
3 − 2532650 c
2 − 6362820 c − 3155031
) = 0. (4.16)

Estamos buscando los primos p que son ineﬁcaces con 5 de nivel 3, por tanto, distintos de

2, 3, 11, 193, 3541 —ineﬁcaces de niveles 1 y 2 con n = 5— y tambi´en distintos de 5 —eﬁcaz

con n = 5, pues es Y5( F5 ) = ̸O—. Habiendo apartado los primos 2 y 5, los n´umeros 100,

2000 y 10000 (o, mejor, sus im´agenes mediante la aplicaci´on caracter´ıstica ϕ : Z → Fp) son

unidades en Fp, luego su presencia en las igualdades anteriores no resulta problem´atica;

de hecho, en las ecuaciones (4.15) y (4.16) pueden suprimirse sin m´as.

Debemos localizar aquellos primos que cumplen la siguiente condici´on:

sobre el cuerpo Fp , las dos ecuaciones (4.15) y (4.16) tienen en com´un una soluci´on γ

puesto que ella identiﬁca a los primos ineﬁcaces con n = 5 de nivel 3. En efecto, esta

condici´on es necesaria para que existan β, γ ∈ Fp tales que (1, β, γ) satisface el sistema

(4.12), y tambi´en es suﬁciente para ello: considerando el valor µ que (4.14) le asigna a m

cuando c se sustituye por γ, basta tomar β como una de las soluciones que en el cuerpo

Fp siempre posee la ecuaci´on β2 = µ. (En rigor, deber´ıamos tener la cautela de comprobar

84 Cap´ıtulo 4. Condensaci´on y expansi´on

que tanto γ como β sean distintos del elemento 0 ∈ Fp; pero si as´ı no fuera, y dado que,

en todo caso, se tendr´ıa un punto [(1, β, γ)] perteneciente a Y5( Fp ), seguir´ıa siendo cierto

que p es un primo ineﬁcaz con 5 —aunque de nivel inferior a 3— y, por tanto, habr´ıa de

coincidir con alguno de los hallados anteriormente.)

Hemos de considerar, pues, la resultante de los polinomios

16875 c
4 + 26500 c
3 − 99950 c
2 − 250460 c − 146853

455625 c
4 + 869500 c
3 − 2532650 c
2 − 6362820 c − 3155031,

cuyo valor es, exactamente,

− 232 · 37 · 5
16 · 73 · 131 · 5992 · 8009.

Esta resultante es nula en caracter´ıstica p si y solo si es p = 7, 131, 599, 8009 (recordemos

que en este momento no disponemos de 2, ni de 3, ni de 5). Como estos primos no dividen

a los coeﬁcientes directores, 16875 = 3
3 · 54 y 455625 = 3
6 · 5
4, la anulaci´on de la resultante

verdaderamente equivale a que dichos polinomios compartan una ra´ız γ ∈ Fp o, en otros

t´erminos, a que exista γ ∈ Fp soluci´on com´un de las ecuaciones (4.15) y (4.16), lo que era

precisamente la condici´on expresada en el recuadro.

Se concluye que los cuatro primos citados: 7, 131, 599, y 8009, son todos los primos

ineﬁcaces de nivel 3 con n = 5 que existen. Hemos completado as´ı la n´omina de los primos

que son ineﬁcaces con n = 5—esto es, tales que Y5( Fp ) ̸= ̸O—; cualquier primo p que no

ﬁgure en ella es, pues, eﬁcaz con n = 5. □

Corolario 4.4.4. El problema de Casas-Alvero tiene respuesta aﬁrmativa para todos los

n´umeros de la forma n = 5pr con p ̸= 2, 3, 7, 11, 131, 193, 599, 3541, 8009.

Demostraci´on. El teorema anterior garantiza que para todo primo p distinto de los men-

cionados se tiene Y5( Fp ) = ̸O; la lectura hacia la izquierda del teorema de condensaci´on

(4.2.1) expande este resultado y permite asegurar que es Y5pr ( Fp ) = ̸O para todo r ∈ N.

Finalmente, la proposici´on 3.1.4 conduce hasta el resultado enunciado en este corolario. □

Comentario 4.4.5. Todo el trabajo de c´alculo tanto algebraico como aritm´etico que

se ha precisado para localizar los primos ineﬁcaces con n = 5 se ha podido ejecutar sin

diﬁcultad con el auxilio del programa inform´atico DERIVE. Con este antecedente, resulta

l´ogico abordar el mismo problema para el caso n = 6 utilizando el mismo planteamiento,

y explorar hasta qu´e punto podemos avanzar en su resoluci´on y qu´e nuevos obst´aculos se

interponen en el camino.

4.4 Niveles de ineﬁcacia 85

Caso: Fijar Inc´ognitas ´Ultima Ecuaci´on Primos cumpliendo Z6,{i,j,k}( Fp ) ̸= ̸O

I: a = 0 b = 1 c , d grado 3 en c 47, 811, 3209, 3877, 9337, 17 250187

II: b = 0 a = 1 c , d2 lineal en m = d2 257, 1069, 3881, 150203, 547061

III: c = 0 a = 1 b , d cuadr´atica en d 8699, 15823, 2 610767 527031

IV: d = 0 a = 1 b2 , c lineal en m = b2 21379, 7 783207, 40 362599, 7390 044713 023799

Cuadro 4.1: Casu´ıstica en la b´usqueda de primos ineﬁcaces de nivel 3 con n = 6.

Del mismo modo que con n = 5, la b´usqueda de los primos ineﬁcaces con n = 6 se

realiza por niveles, en cada uno de los cuales se investiga cu´ales son las condiciones nece-

sarias y suﬁcientes para que el sistema homog´eneo pesado H [1] = H [2] = H [3] = H [4] = 0 en

las inc´ognitas a, b, c, d (usadas, por simplicidad, en lugar de b2, b3, b4, b5, y con pesos res-

pectivos 2, 3, 4 y 5) posea sobre el cuerpo Fp alguna soluci´on con un determinado n´umero

de componentes distintas de cero. Y esto es lo que ocurre:

Niveles 1 y 2: En estos niveles, la complejidad de la tarea no experimenta ning´un incre-

mento —aunque s´ı, obviamente, su volumen—; todo se reduce a aplicar el procedimiento

recogido en la observaci´on 4.4.2.

Nivel 3: Localizar aquellos primos no surgidos en los niveles anteriores y para los cuales

no sea vac´ıo el conjunto Z6,{1,2,3}
( Fp ) ∪ Z6,{1,2,4}
( Fp ) ∪ Z6,{1,3,4}
( Fp ) ∪ Z6,{2,3,4}
( Fp ) requiere

trabajar con el consabido sistema homog´eneo en cuatro casos particulares, que son, natu-

ralmente: I: a = 0, II: b = 0, III: c = 0 y IV: d = 0. Tenemos as´ı cuatro subproblemas que, si

bien son esencialmente iguales al problema de hallar los primos ineﬁcaces de nivel 3 con

n = 5 —cuya resoluci´on se expuso en la demostraci´on del teorema 4.4.3—, presentan alguna

complicaci´on adicional debida al mayor grado de sus ecuaciones. Baste esbozar la pauta

com´un a todos los casos y se˜nalar los rasgos diferenciales (que se recogen en la tabla 4.1):

En todos los casos, tras anular una de las indeterminadas y asumiendo que las tres

restantes son distintas de cero, imponemos que una de ellas (la de menor peso y, por ello,

portadora de exponentes m´as altos) tome el valor 1. Descargamos tambi´en el factor trivial

de cada resultante. Queda entonces un sistema de tres ecuaciones en dos inc´ognitas, y el

objetivo es encontrar todas aquellas caracter´ısticas p en las que dicho sistema pueda ser

compatible. No se trata de ecuaciones lineales; si tomamos el grado total —en sentido

ordinario, no pesado— de cada una de las ecuaciones del sistema, resultan las siguientes

ternas (respectivamente para los casos I , II , III y IV): (5, 5, 3), (5, 5, 2), (5, 5, 2) y (4, 4, 2).

Los casos II y IV guardan completa similitud con el problema para n = 5 estudiado

en 4.4.3: ocurre que una de las inc´ognitas ﬁgura siempre con exponente par, lo que

permite sustituir por m a su cuadrado; tras hacerlo, la ´ultima ecuaci´on queda lineal

86 Cap´ıtulo 4. Condensaci´on y expansi´on

en m. Es pues inmediato despejar m y sustituirlo en las dos ecuaciones anteriores.

En el caso III, la ´ultima ecuaci´on es de segundo grado en d —tambi´en lo es en b—;

elegimos despejar d y sustituirlo en las dos ecuaciones previas. El proceso, que en

principio ha de efectuarse dos veces, una por cada signo en la f´ormula de las ra´ıces del

trinomio, puede completarse rigurosamente dentro del cuerpo Fp representando las

ra´ıces mediante el uso de s´ımbolos literales deﬁnidos por la identidad que satisfacen

(as´ı, por ejemplo, en lugar de √3i empleamos u ∈ Fp tal que u2 = −3). Procediendo de

este modo, de hecho, es superﬂua la repetici´on, puesto que se cubren simult´aneamente

las dos elecciones del signo.

En el caso I, la m´as sencilla de las ecuaciones del sistema—que, como en los otros

casos, es la que proviene de H [3]— es ya de grado 3 en c, pero con la afortunada

particularidad de que su primer miembro factoriza dentro del anillo Z[d][c] como

producto de un polinomio lineal y otro cuadr´atico. El sistema inicial se desdobla,

pues, en dos sistemas diferentes —seg´un que dicha ecuaci´on se supla por la que

expresa la nulidad de uno u otro factor—; en cada uno de ellos, la situaci´on que se

presenta es an´aloga a la de uno de los ´ıtems previos: tres ecuaciones en dos inc´ognitas,

siendo la tercera ecuaci´on, o bien lineal en una de sus inc´ognitas (como en los casos

II y IV), o bien cuadr´atica en una de ellas (como en el caso III); tanto en una como

en otra tesitura, la inc´ognita en cuesti´on se despeja empleando la ecuaci´on tercera,

para luego sustituirla en las dos anteriores.

En deﬁnitiva, en cada uno de los casos I, II, III y IV, las referidas operaciones han desem-

bocado en la obtenci´on de (al menos) un sistema de dos ecuaciones en una ´unica inc´ognita,

cuya compatibilidad interesa estudiar, por ser condici´on necesaria y suﬁciente para que

sea compatible el sistema de partida que lo sea alguno de estos.

Fij´emonos en uno cualquiera de tales sistemas: Consiste en dos ecuaciones algebraicas

de grado 5 (4, en el caso IV), y lo que se pretende ahora es hallar aquellos valores de p

tales que sobre el cuerpo Fp ambas ecuaciones posean una soluci´on com´un. Dado que ello

equivale a que se anule la resultante de sus correspondientes polinomios, basta con calcular

y factorizar en Z dicha resultante para obtener los primos que busc´abamos (ver tabla 4.1).

Nivel 4: Si el sistema H [1] = H [2] = H [3] = H [4] = 0 admite sobre Fp alguna soluci´on con sus

cuatro componentes no nulas, admitir´a, en particular, una de la forma (−1, β, γ, δ) (elegir

−1 en vez de 1 facilitar´a c´alculos posteriores). Tendremos entonces (β, γ, δ) ∈ F3
p que es

soluci´on del sistema
 F1(b, c, d) = F2(b, c, d) = F3(b, c, d) = F4(b, c, d) = 0,

4.4 Niveles de ineﬁcacia 87

obtenido del anterior al prescindir del factor trivial en cada H [i] y hacer a = − 1. De la

´ultima ecuaci´on, cuadr´atica en b, obtenemos que se cumple b = f1(c, d) = 1
20 (15c − 6d − 14)

o bien b = f2(c, d) = 1
20 (−15c − 6d + 14). Asumiendo —por ejemplo—que para (β, γ, δ) se

cumpla β = f1(γ, δ), tendremos que (γ, δ) satisface el sistema dado por

F 1(f1(c, d), c, d) = F 2(f1(c, d), c, d) = F 3(f1(c, d), c, d) = 0 (4.17)

Cada F i, una vez multiplicado por el entero adecuado, puede ser visto como un polinomio

en la indeterminada c y coeﬁcientes en el anillo Z[ d ]. El grado en c de tales polinomios

es 6, 6 y 5, respectivamente; construyendo S-polinomios adecuados podemos hallar un

sistema equivalente a (4.17) de la forma

G1(c, d) = G2(c, d) = G3(c, d) = 0 (4.18)

donde el grado en la indeterminada c de los polinomios Gi ∈ Z[d][c] sea, respectivamente,

6, 5 y 4. El hecho de que (γ, δ) sea soluci´on de (4.18) se traduce en que γ es una ra´ız

compartida por los tres polinomios

M 1,δ(c) = G1(c, δ), M 2,δ(c) = G2(c, δ)(c), M 3,δ = G3(c, δ),

cuyos coeﬁcientes pertenecen al anillo Z[δ] ⊂ Fp. Para que ello sea posible, es condici´on

necesaria (aunque no suﬁciente) la anulaci´on simult´anea de las tres resultantes

Q1,2(δ) = Res(M 1,δ, M 2,δ), Q1,3(δ) = Res(M 1,δ, M 3,δ), Q2,3(δ) = Res(M 2,δ, M 3,δ) ∈ Z[δ],

es decir, es necesario que exista δ ∈ Fp que sea ra´ız com´un de los tres polinomios

Q1,2(d) = Res(M 1,d, M 2,d), Q1,3(d) = Res(M 1,d, M 3,d), Q2,3(d) = Res(M 1,d, M 3,d) ∈ Z[d],

siendo M i,d(c) = Gi(c, d), para i = 1, 2, 3.

Los primos ineﬁcaces que estamos buscando se encuentran, pues, entre los que cumplen

la siguiente condici´on:

sobre Fp , los tres polinomios Q1,2(d), Q1,3(d) y Q2,3(d), poseen una ra´ız com´un, δ.

para lo cual conocemos una condici´on necesaria (aunque, como antes, no suﬁciente): que en

caracter´ıstica p sean nulas las tres resultantes obtenidas al tomar dos a dos los polinomios

Q1,2(d), Q1,3(d) y Q2,3(d). As´ı pues, si logramos construir y factorizar en Z estas tres

resultantes, entonces el conjunto formado por los factores primos comunes a las tres —que

es ﬁnito— contendr´a todos los primos ineﬁcaces de nivel 4 con n = 6; cabe examinar uno

a uno para tratar de conﬁrmar o descartar que en efecto posean dicha condici´on, pero en

todo caso es seguro que todo primo ausente de este listado (y que no haya aparecido como

ineﬁcaz de un nivel inferior) ser´a eﬁcaz con n = 6.

88 Cap´ıtulo 4. Condensaci´on y expansi´on

Bien, el problema est´a conceptualmente resuelto: la obtenci´on de los tres polinomios

Qi,j(d) es perfectamente factible, y el c´alculo de las tres resultantes no deber´ıa ofrecer diﬁ-

cultad. Sin embargo, el procedimiento es poco viable a causa de la impresionante magnitud

de los datos:

Q1,3(d) tiene grado 30, y coeﬁcientes de un orden comprendido entre 1070 y 1085

Q2,3(d) tiene grado 29, y sus coeﬁcientes de un orden comprendido entre 1062 y 1075

Q1,2(d) tiene grado 32, y el orden de sus coeﬁcientes est´a entre 1039 y 1052

(y esto, una vez descontada la presencia, en cada polinomio, de un factor constante, del

orden de 1024, 1026 y 1028, respectivamente). Otras elecciones posibles—de la inc´ognita a

despejar, de la indeterminada respecto de la cual ordenar. . . —ofrecen resultados similares,

tambi´en con llegada a una v´ıa muerta.

No nos obstinaremos aqu´ı en tratar de resolver este problema siguiendo el camino

iniciado. En el pr´oximo cap´ıtulo dispondremos de un enfoque alternativo, ligado a un

esquema proyectivo diferente, que nos permitir´a el c´alculo efectivo de todos los primos

ineﬁcaces con n = 6.

La siguiente proposici´on no es sino la precisa recopilaci´on de los resultados efectiva-

mente obtenidos en 4.4.5:

Proposici´on 4.4.6. Los primos ineﬁcaces con n = 6 de nivel estrictamente menor que 4

son los siguientes:

Nivel 1: 2, 5, 7, 19.

Nivel 2: 11, 13, 29, 37, 61, 67, 73, 1487, 20771, 23993.

Nivel 3: 47, 257, 811, 1069, 3209, 3877, 3881, 8699, 9337, 15823, 21379, 150 203,

547 061, 7 783 207, 17 250 187, 40 362 599, 2 610 767 527 031, 7390 044 713 023 799. □

El cuadro 4.2, que cierra el cap´ıtulo, ofrece el listado completo de los valores ineﬁcaces

de primer y segundo nivel —calculados seg´un se dijo en 4.4.2— para los n´umeros 7, 8, 9,

10, 11 y 12.

Es ilustrativo observar c´omo para muy peque˜nos valores de n aparecen, ya en el nivel 2

de ineﬁcacia, primos descomunales (del orden de los trillones, para n = 10, de miles de

cuatrillones, para n = 12), y lo r´apidamente que se incrementa tanto su n´umero como

la magnitud que llegan a alcanzar, a medida que crece n. Incluso en los dos primeros

niveles, en los que se dispone de procedimientos sistem´aticos, la selecci´on de los primos

parece responder al m´as puro capricho, del mismo modo en que caprichosa parece la

4.4 Niveles de ineﬁcacia 89

n = 7 Nivel 1 2, 3, 5, 17.

Nivel 2 11, 13, 23, 29, 31, 71, 79, 137, 149, 293, 383, 491, 599, 1373, 2393, 19583, 2 700319, 44 446559.

n = 8 Nivel 1 3, 5, 7, 11, 23.

Nivel 2 13, 17, 19, 29, 31, 41, 53, 59, 61, 71, 73, 109, 193, 283, 449, 457, 491, 691, 821, 1033, 1471,
1747, 1753, 4447, 6047, 70321, 72053, 96851, 100069, 102121, 151787, 3 042997, 15 083609,
133578 667529.

n = 9 Nivel 1 2, 5, 7, 83.

Nivel 2 11, 13, 17, 19, 29, 31, 37, 43, 59, 67, 71, 79, 89, 101, 103, 131, 137, 157, 163,379, 449,
1051, 2069, 3187, 5527, 5849, 17903, 35531, 51329, 178909, 333769, 1 268797, 1 681363,
2 012419, 85 301959, 4152 858113, 7879 713071, 10566 565489, 10628 250767, 31170 485999,
170050 183063, 684178 526303, 9 442649 977903, 18 294891 489449, 78 207719 634491.

n = 10 Nivel 1 2, 3, 7, 11, 17, 19, 251.

Nivel 2 13, 23, 29, 31, 37, 41, 47, 61, 73, 79, 89, 101, 139, 151, 181, 233, 277, 307, 347,
503, 563, 619, 757, 787, 991, 997, 1123, 1171, 1223, 1489, 2731, 2963, 4243, 6143,
10429, 11689, 11933, 17623, 17839, 21661, 25847, 26573, 80933, 112207, 260573, 508159,
1 176239, 1 311733, 3 361639, 6 403181, 36 737209, 40 193311, 67 623761, 114 750589,
285 641119, 1171 604881, 1659 214621, 50882 649709, 94648 571077, 115744 767907,
137495 218381, 201550 614547, 1 938388 976717, 76 317432 445741, 2819 457712 745081,
6271 487438 874901, 6 980592 529231 704811.

n = 11 Nivel 1 2, 3, 5, 7, 41, 47, 461.

Nivel 2 13, 19, 23, 29, 31, 37, 43, 53, 59, 67, 71, 73, 89, 103, 107, 131, 139, 163, 173, 197,
229, 233, 293, 409, 503, 557, 577, 661, 691, 877, 919, 1069, 1091, 1483, 1667, 1733,
1871, 1997, 2011, 2671, 7549, 10289 10631, 10891, 11749, 12611, 13217, 16937, 17957,
27551, 29537, 40933, 41621, 56167, 66529, 75787, 102539, 203659, 233173, 283669,
621017, 727249, 1 381349, 1 469087, 4 907921, 10 803127, 22 551359, 24 438067, 67 903357,
91 580407, 135 356759, 158 210317, 186 674237, 811 306481, 2478 679711, 2691 188471,
10017 222473, 15321 591739, 43129 826189, 107248 950013, 304706 871407, 330889 336223,
4 227618 081473, 6 028006 702481, 51 856639 765607, 53 921320 856779, 71 007003 754523,
328 768690 304689 , 657 320600 102303 , 8118 451553 135971 , 15629 057690 606267 ,
138032 248224 512461 , 4 753874 264034 777383, 2 674461 312915 117968 508667,
7 498690 019676 445564 846049.

n = 12 Nivel 1 2, 3, 5, 7, 11, 13, 19, 71, 73, 113.

Nivel 2 17, 23, 29, 31, 41, 47, 53, 59, 61, 67, 83, 89, 101, 103, 107, 127, 149, 157, 167, 181, 191, 193,
211, 223, 229, 241, 271, 293, 307, 313, 373, 419, 421, 431, 509, 547, 599, 631, 643, 739, 821,
827, 859, 941, 1009, 1193, 1423, 1481, 1489, 1567, 3433, 3697, 3733, 3929, 5437, 5779, 6221,
6269, 6977, 9697, 9851, 13217, 14327, 17911, 18041 18947, 19219, 19993, 20063, 23593,
29983, 32341, 33589, 65831, 126961, 152563, 152639, 161773, 166471, 168281, 183877,
196279 368059, 543593, 1948987, 3079711, 4132151, 6009683, 6531709, 8 502581, 10 058941,
14 378417 , 33 821509 , 114 068599 , 129 769301 , 182 705903 , 361 846721 , 552 843719 ,
1067 538217 , 2541 640561 , 5696 929037 , 7731 840929 , 19023 084637 , 71130 026657 ,
271420 993729 , 336048 035693 , 538228 539671 , 729595 481339, 1 509579 945103 ,
1 807000 523543 , 16 738247 804093 , 21 094483 630223, 41 581475 975341, 45 261742 243997,
81 431483 854691, 155 351610 321851, 198 478256 072773, 266 377988 861953 ,
373 119427 470043 , 832 378889 412121 , 62171 145343 492699 , 172994 176982 555267,
18 534085 940905 810921 , 41 051564 324089 235071 , 221 683353 776645 181007 ,
2377 225815 083191 016081 , 2430 025954 712382 144281 , 206177 862036 793816 019327 ,
219117442609717502451619, 859540281549223625605679, 81542829570379582758908521,
1393 978154 153831 038607 107121 , 3992 883635 832874 870245 154277.

Cuadro 4.2: Primos ineﬁcaces de niveles 1 y 2 para n = 7, . . . , 12

90 Cap´ıtulo 4. Condensaci´on y expansi´on

descomposici´on en factores de un entero tomado al azar. Cabe a´un imaginar c´omo pueden

ser los listados de primos ineﬁcaces de niveles 3 o 4, pero siendo n —tan solo— igual a

12 se antojan ya inimaginables los listados de primos ineﬁcaces de niveles 9 o 10. A´un

nos encontramos casi en el umbral, apenas iniciada la inspecci´on de un territorio que es

doblemente ilimitado —en extensi´on, y en profundidad— y ya se ha constatado el total

desbordamiento que inmediatamente se produce.Cap´ıtulo 5

Esquemas alternativos

El tratamiento del problema de Casas-Alvero seguido hasta el momento utilizaba como

indeterminadas a los coeﬁcientes bi del polinomio gen´erico de grado n, que no son inter-

cambiables entre s´ı. Por el contrario, la estrategia de expresar el polinomio como producto

de n binomios de la forma X−xi, cede el protagonismo a las propias ra´ıces del mismo, x1,

x2, . . . , xn. Puesto que estas pueden permutarse libremente sin que el producto indicado

sufra ninguna alteraci´on, emplear a las ra´ıces x1, x2, . . . , xn como las inc´ognitas del sistema

que plasma el problema de Casas-Alvero proporciona una simetr´ıa inicial que se rentabi-

liza durante la construcci´on del esquema proyectivo. Como ventaja adicional, la condici´on

sobre Pn(X) de compartir una ra´ız con su primera derivada —la m´as inc´omoda de las

ecuaciones en el esquema Yn— encuentra ahora su expresi´on m´as simple y conveniente,

pues supone tan s´olo la igualdad entre dos de las ra´ıces del polinomio.

5.1. El esquema de ra´ıces

En primera instancia, podemos escribir:

Conjetura de Casas-Alvero. Si el polinomio

Pn(X) = ( X − x1) · ( X − x2) · · · · · ( X − xn), con (x1, x2, . . . , xn) ∈ Cn (5.1)

comparte una ra´ız con cada uno de los polinomios Pn
′(X), Pn
′′(X), . . . , Pn
(n-1)(X), entonces

se veriﬁca: x1 = x2 = . . . = xn.

De existir alg´un polinomio que sirva de contraejemplo a esta conjetura, admitir´ıa la

reordenaci´on de sus factores y, por tanto, cualquier ordenaci´on particular de sus ra´ıces,

(xi1, xi2, . . . , xin) ∈ Cn, ﬁgurar´ıa como manifestaci´on del contraejemplo en cuesti´on; en

consecuencia, para su rastreo podemos —sin p´erdida de generalidad— concretar el objeto

92 Cap´ıtulo 5. Esquemas alternativos

de la b´usqueda, estableciendo de antemano en qu´e orden esperamos encontrar dispuestas

a las ra´ıces.

Por otra parte, ya la proposici´on 1.1.2 permiti´o circunscribir el problema de Casas-

Alvero a aquellos polinomios que carecen de t´ermino vicel´ıder, en cuyo caso, tal como se

observ´o en su momento, la (n−1)-´esima condici´on sobre Pn(X) signiﬁca exactamente que

es nulo su t´ermino independiente o, equivalentemente, que el cero es una de las ra´ıces de

Pn(X). En esa situaci´on restringida nos mantendremos en lo sucesivo.

Cuando se desarrolla el polinomio indicado en (5.1), queda :

Pn(X) = Xn + (−1) s1 Xn-1 + (−1)
2 s2 Xn-2 + · · · + (−1)i si Xn-i + · · · + (−1)
n sn (5.2)

donde cada si es la llamada funci´on sim´etrica elemental de orden i:

s1 =
 n∑

i=1 xi, s2 = ∑

i<j xi xj, s3 = ∑

i<j<kxi xj xk, . . . , sn = x1 x2 · · · xn (5.3)

y, por tanto, establecer que el t´ermino vicel´ıder tenga coeﬁciente nulo supone asumir:

(1) que s1 es nulo, esto es, se veriﬁca x1 + x2 + · · · + xn = 0.

(2) que sn es nulo—amortizando as´ı la condici´on sobre Pn
(n-1)(X)—, de modo que alguna

de las ra´ıces es igual a cero. Convenimos en ﬁjar esta ra´ız nula en la primera posici´on,

haciendo que sea x1 = 0.

Abordamos ahora la caracterizaci´on de la condici´on relativa a Pn
′(X). La resultante

tiene un comportamiento multiplicativo, y es particularmente sencilla cuando uno de los

polinomios es de grado 1 (pues se cumple: Res(P ( X), X −α) = (−1)
nP (α), siendo n el grado

de P ( X)). Puesto que es

Pn
′(X) = ( n∏

i=1 ( X −xi)
)′ =
 n∑

k=1
 ( ∏

j̸=k ( X −xj)
)

se tiene:

Res(Pn(X), Pn
′(X)
) = Res( n∏

i=1( X −xi) ,
 n∑

k=1
 ( ∏

j̸=k( X −xj)
)) =
 n∏

i=1
 [ n∑

k=1
 ( ∏

j̸=k (xi −xj)
)]
.

Todos los sumandos contenidos en el corchete llevan un factor igual a xi −xi, a excepci´on,

justamente, de aquel en que k toma el valor coincidente con i, as´ı que queda, simplemente,

Res(Pn(X), Pn
′(X)
) =
 n∏

i=1
 [ ∏

j̸=i
 (xi −xj)] = ∏

i<j
 [ −(xi −xj)2 ]

Ha quedado patente el hecho (bien conocido, y ya mencionado al inicio del cap´ıtulo) de

que Pn(X) comparte una ra´ız con su derivada Pn
′(X) —o equivalentemente, es nula la

5.1 El esquema de ra´ıces 93

resultante de ambos— si y solo si dos de las ra´ıces de Pn(X) son iguales entre s´ı. Aplicado

al polinomio en (5.1), que por hip´otesis veriﬁca dicha propiedad, si elegimos ubicar en la

segunda posici´on, denomin´andola x2, a una ra´ız del polinomio que sea id´entica a otra de las

ra´ıces xi, entonces necesariamente habr´a de cumplirse una de estas dos alternativas: o bien

x2 coincide precisamente con x1 (y por tanto es, como ella, nula), o bien esto no sucede, y

entonces coincide con una tercera ra´ız que no es nula y a la que podemos identiﬁcar como

x3. El enunciado de la conjetura adopta entonces la siguiente forma:

Conjetura de Casas-Alvero. Si el polinomio Pn(X) = ( X−x1)( X−x2) · · · ( X−xn),

con x1, x2, . . . , xn ∈ C, satisface las condiciones:

(1 ) x1 + x2 + · · · + xn = 0, y adem´as x1 = 0.

(2 ) Es x2 = 0, o bien es x2 = x3 ̸= 0.

(3 ) Para cada i = 2, . . . , n−2, Pn(X) comparte una ra´ız con su derivada i-´esima, Pn
(i)(X),

entonces se veriﬁca: x1 = x2 = . . . = xn = 0.

Escribamos el polinomio anterior bajo la forma Pn(X) = Xn + a2 Xn-2 + . . . + an-1 X.

Sabemos que Pn(X) compartir´a una ra´ız en C con su derivada ordinaria i-´esima si y solo

si la comparte con la derivada de Hasse del mismo orden,

Pn
< i >(X) = 1

i ! Pn
(i)(X) =

= ( n
i ) Xn-i + (n-2
i )a2 Xn-2-i +. . . + (n-k
i )ak Xn-k-i +. . . + ( i
i )an-i,

esto es, si se anula la resultante

G< i > := Res(Pn , Pn
< i >) ∈ Z[a2, . . . , an-1]. (5.4)

A la vista de (5.2) y (5.3) es claro que las sustituciones

ak := (−1)k sk = (−1)k · ∑

i1<i2<...<ikxi1 xi2 . . . xik, para k = 2, . . . n−1, (5.5)

reexpresan el polinomio Pn(X) en funci´on de sus ra´ıces, mientras que efectuadas en cada

G< i > expresan la resultante entre Pn(X) y su i-´esima derivada de Hasse mediante un

polinomio K < i > perteneciente a Z[x1, . . . , xn]. Cuando este anillo se grad´ua en el modo

usual —esto es, dando peso igual a 1 a cada indeterminada xi— cada ak es un polinomio

homog´eneo de grado k y, en consecuencia, cada resultante K < i > es homog´enea de grado

n(n−i), puesto que ese es el grado del polinomio homog´eneo pesado G< i > en el anillo

Z[a2, . . . , an-1] cuando precisamente se le atribuye peso k a cada indeterminada ak.

En conclusi´on, empleando los polinomios K < i > que acabamos de introducir, el enun-

ciado de la conjetura puede reformularse como sigue:

94 Cap´ıtulo 5. Esquemas alternativos

Conjetura de Casas-Alvero. Si (x2, x3, . . . , xn) ∈ Cn-1 satisface las condiciones:

(1 ) x2 + x3 + · · · + xn = 0.

(2 ) Es x2 (x2 −x3) = 0.

(3 ) Es K < 2 > = K < 3 > = · · · = K < n-2 > = 0 (seg´un deﬁniciones previas),

entonces necesariamente se veriﬁca: x2 = x3 = . . . = xn = 0.

El esquema proyectivo que denotaremos Rn y que deﬁnimos mediante las n−1 ecuaciones

homog´eneas en las n−1 inc´ognitas x2, . . . , xn:

x2 + x3 + · · · + xn = x2 (x2 −x3) = K < 2 > = K < 3 > = · · · = K < n-2 > = 0,

proporciona una traducci´on inmediata del enunciado anterior:

Proposici´on 5.1.1. La conjetura de Casas-Alvero de grado n es verdadera si y solo si es

Rn(C) = ̸O. □

En el manejo pr´actico de este esquema, aparte de la obvia eliminaci´on de una variable

gracias a la primera ecuaci´on, encontraremos tres aspectos muy ventajosos:

• La segunda ecuaci´on divide en realidad el problema en dos casos m´as sencillos.

• Las ecuaciones K < i >= 0 han servido para demostrar que en efecto se tiene un esquema

proyectivo, pero no necesitaremos resolverlas. Lo que ellas expresan puede reducirse a un

juego combinatorio con un n´umero ﬁnito de variaciones.

• Precisamente por saber que todas las ecuaciones son homog´eneas, podemos ﬁjar a 1 el

valor de alguna componente no nula durante el rastreo de eventuales soluciones no triviales

del sistema.

Estos aspectos, que aqu´ı han sido apenas apuntados, podr´an apreciarse m´as adelante

con ocasi´on del empleo efectivo del esquema Rn para diversos valores de n.

5.2. El esquema de coeﬁcientes ordinarios

Como mero puente para la construcci´on del esquema de ra´ıces, en la secci´on anterior

hab´ıamos expresado el polinomio Pn(X) de nuestro inter´es bajo la forma que suele consi-

derarse usual, y que nosotros llamaremos ordinaria:

Pn(X) = Xn + a2 Xn-2 + a3 Xn-3 + . . . + an-1 X. (5.6)

5.2 El esquema de coeﬁcientes ordinarios 95

En efecto, bast´o efectuar en cada polinomio G< i > = Res(Pn , Pn
< i >) las sustituciones (5.5)

para obtener los polinomios K < i > ∈ Z[x2, . . . , xn] empleados en la deﬁnici´on de Rn. En

esta ocasi´on obviaremos dichas sustituciones.

Llamaremos esquema de coeﬁcientes ordinarios, y denotaremos por Xn, al esquema

proyectivo en las n−2 variables a2, . . . , an-1 deﬁnido por los polinomios homog´eneos G< 1 >,

G< 2 >, . . . , G< n-2 >. Mediante argumentos id´enticos a los que conduc´ıan a la proposici´on

3.1.2(a), se obtiene esta vez:

Proposici´on 5.2.1. La conjetura de Casas-Alvero de grado n es verdadera si y solo si es

Xn(C) = ̸O. □

Estos dos nuevos esquemas, Xn y Rn, suponen, en relaci´on con la conjetura de Casas-

Alvero de grado n, una alternativa al esquema Yn utilizado en cap´ıtulos anteriores — y

al que, a partir de ahora, llamaremos esquema de coeﬁcientes presentados—. Cada uno

de ellos caracteriza la validez de dicha conjetura mediante el hecho de no poseer ning´un

punto sobre el cuerpo C. Por otra parte, tambi´en a cada uno de ellos le es aplicable la

proposici´on 3.0.3, de modo que el hallazgo de un primo p para el que se tenga Xn( Fp ) = ̸O

o Rn( Fp ) = ̸O garantiza que es, respectivamente, Xn(C) = ̸O o Rn(C) = ̸O, y por tanto

demuestra la conjetura para el grado n.

Por dicha raz´on, y en analog´ıa con el concepto de par eﬁcaz (n, p) deﬁnido en la secci´on

4.3 para el esquema Yn, diremos que el par (n, p) es Xn-eﬁcaz o que es Rn-eﬁcaz si se

veriﬁca Xn( Fp ) = ̸O o Rn( Fp ) = ̸O, respectivamente. El siguiente resultado demuestra que

los tres conceptos son en realidad equivalentes.

Teorema 5.2.2. Dados un grado n ≥ 3 y un primo p, se veriﬁcan las equivalencias:

(1) Rn( Fp ) = ̸O si y solo si Xn( Fp ) = ̸O.

(2) Xn( Fp ) = ̸O si y solo si Yn( Fp ) = ̸O.

Demostraci´on. (1 ) Tomemos α2, . . . , αn-1, γ2, . . . , γn ∈ Fp, con γ2 + · · · + γn = 0, tales que

los coeﬁcientes ordinarios αi y las ra´ıces γj dan lugar —en cada caso, de la forma que le

es propia— a un mismo polinomio, esto es, se tiene

Xn + α2 Xn-2 + · · · + αn-1 X = X ( X −γ2) · · · ( X −γn).

En consecuencia, los valores αi y los valores γj guardan entre s´ı la misma relaci´on que

(5.5) establec´ıa entre las ai y las xj:

αk = (−1)k · ∑

i1<i2<...<ikγi1 γi2 . . . γik, para k = 2, . . . n−1.

96 Cap´ıtulo 5. Esquemas alternativos

Es claro entonces que α = (α2, . . . , αn-1) cumple G< i >= 0 si y solo si γ = (γ2, . . . , γn)

cumple K < i >= 0, para todo i = 1, . . . , n−2. Ciertamente, la condici´on K < 1 >= 0 es m´as

d´ebil que la condici´on x2(x2 −x3) exigida por el esquema Rn; pero ocurre que γ satisface

K < 1 >= 0 si y solo si una adecuada reordenaci´on de sus componentes, γ ∗ = (γj1, . . . , γjn-1),

satisface x2(x2 −x3), de modo que la existencia de alg´un α ∈ Xn( Fp ) equivale en efecto a

la existencia de alg´un γ ∗ ∈ Rn( Fp ).

(2 ) Tomemos α2, . . . , αn-1, β 2, . . . , β n-1 ∈ Fp, y consideremos el polinomio

Pn, α(X) = Xn + α2 Xn-2 + · · · + αl Xn-l + · · · + αn-1 X,

as´ı como el polinomio presentado

Pn, β(X) = Xn + ( n
2
 )β 2 Xn-2 + · · · + ( n
l
 )β l Xn-l + · · · + ( n
n-1
)β n-1 X.

Los sub´ındices α, β expresan aqu´ı, respectivamente, la especializaci´on de los coeﬁcientes
ak del polinomio Pn(X) en los valores αk, y de los coeﬁcientes bk del polinomio presen-
tado llamado igualmente Pn(X) —en un abuso de notaci´on que se repite con Pn, β(X) y
Pn, β(X)— en los valores β k. Entonces, las especializaciones de las respectivas derivada de
Hasse y derivada neta est´an dadas, para cada i = 1, 2, . . . , n−2, por

Pn, α

< i >(X) =
( n
i
 ) X n-i + (n-2
i
 )α2 X n-i-2
+ · · · +
(n-l
i
 )αl X n-l-i
+· · · +
(i + 1
i
 )αn-i+1 X + αn-i ; (5.7)

Pn, β
[ i ] (X) = X n-i + ( n-i
2
 )β 2 X n-i-2 + · · · + ( n-i
l
 )β l X n-i-l + · · · + ( n- i
n- i-1
)β n- i -1 X + β n-i . (5.8)

Si β = (β 2, . . ., β n-1) representa a un punto [β ] ∈ Yn( Fp ), y tomamos α = (α2, . . ., αn-1) con

αl = ( n
l )β l, entonces podremos probar que α es un punto de Xn( Fp ). Para ello:

• En primer lugar, es obvio que para dichos α, β se tiene la igualdad Pn, α(X) = Pn, β(X).

• En segundo lugar, α verdaderamente deﬁne un punto [α] del correspondiente espacio

proyectivo pesado. En efecto, si todas las componentes de α fueran nulas signiﬁcar´ıa que

son nulos m´odulo p todos los factores ( n
l ) que acompa˜nan a los β l ̸= 0, o, en t´erminos del

cap´ıtulo 3, que para el conjunto de grados I = { n−l | β l ̸= 0} se tiene Ip = ̸O. Entonces,

por el teorema 3.3.1 de resoluci´on por interpretaci´on, se tendr´ıa Zn,I ( Fp ) = ̸O, en contra

de que es [β ] ∈ Zn,I ( Fp ).

• En tercer lugar, aplicando en (5.7) la sustituci´on αl = ( n
l )β l, multiplicando en ambos

miembros de en (5.8) por ( n
i ), y teniendo en cuenta las igualdades

( n−l
i
 ) · ( n
l
 ) = ( n
i
 ) · ( n−i
l
 ), l = 2, . . . , n−i

se obtiene para cada i = 1, . . . , n−2 la igualdad Pn, α
< i >(X) = ( n
i ) Pn,β
[ i ] (X).

• En cuarto y ´ultimo lugar: Sabemos que la anulaci´on de la resultante entre dos polinomios

equivale a la existencia de una ra´ız compartida siempre que al menos uno de los dos

5.2 El esquema de coeﬁcientes ordinarios 97

polinomios tenga un grado verdadero coincidente con el atribuido(v´ease la secci´on 1.3;

esto es v´alido aun cuando uno de ellos sea el polinomio cero, de quien cualquier ρ ∈ Fp
es ra´ız. As´ı, como se dijo al demostrar el lema 3.2.1, la ecuaci´on H [i] = 0 vinculada al

esquema Yn expresa sobre el cuerpo Fp la condici´on de que Pn(X) y Pn
[i](X) compartan

una ra´ız. Aunque las derivadas de Hasse ya no son m´onicas y por ello en caracter´ıstica p

su verdadero grado puede ser inferior al atribuido, Pn(X) queda libre de esa eventualidad;

por tanto, la ecuaci´on G< i > = 0 vinculada al esquema Xn tambi´en equivale sobre Fp a que

Pn(X) y Pn
< i >(X) compartan una ra´ız.

Por hip´otesis, para cada i = 1, . . . , n−2, y puesto que β veriﬁca la ecuaci´on H [i] = 0,

Existe ρi ∈ Fp tal que P n,β(ρi ) = 0 = P [i]
n,β(ρi ).

De las igualdades Pn, α(X) = Pn, β(X) y P < i >
n,α ( X) = ( n
i ) P [i]
n,β( X) se desprende que, en-

tonces, P n,α(ρi ) = 0 = P < i >
n,α (ρi ).

Queda as´ı probado que α veriﬁca todas las ecuaciones G< i > = 0, y por tanto, que en efecto

el punto [α] pertenece a Xn( Fp ), como se quer´ıa demostrar.

Rec´ıprocamente, dado [α] = [α2, . . . , αn-1] ∈ Xn( Fp ) mostraremos que se tiene β tal

que se cumple ( n
l )β l = αl para todo l = 2, . . . , n−1, y adem´as, [β ] ∈ Yn( Fp ). La existencia

de β no es obvia: cuando ( n
l ) es nulo m´odulo p, no se hallar´a ning´un β l v´alido a menos

que el correspondiente αl sea igual a cero. Y eso es exactamente lo que sucede, como se

demuestra a continuaci´on procediendo por recurrencia sobre el ´ındice l.

Para l = 2, consideramos la derivada de Hasse de orden n−2, que est´a dada por

Pn,α
< n-2 >(X) = ( n
n-2
 ) X2 + α2

y, como sabemos, posee una ra´ız ρn-2∈Fp compartida con Pn,α(X); se cumple, en particular,

−
( n
n-2
 )ρ2
n-2 = α2.

Determinamos β 2 de la siguiente manera:

β 2 =
 



 ( n
n-2)−1 · α2 = − ρ2
n-2, si ( n
n-2) ̸≡ 0 mod p,

0 , si ( n
n-2)≡ 0 mod p. (5.9)

Por recurrencia, si β k est´a construido para k = 2, . . . , l −1 con la propiedad ( n
k )β k = αk,

consideramos la derivada de Hasse de orden n−l, que est´a dada por

Pn,α
< n-l >(X) = ( n
n-l
 ) Xl + ( n-2
n- l
 )α2 Xl-2 + . . . + ( n-k
n- l
 )αk Xl-k + . . . + ( n- l + 1
n- l
 )αl-1 X + αl.

98 Cap´ıtulo 5. Esquemas alternativos

Si, empleando los β k anteriormente construidos, sustituimos en esta expresi´on cada αk por
( n
k )β k, y adem´as tenemos en cuenta las igualdades

( n−k
n−l
 ) · ( n
k
 ) = ( n
n−l
 ) · ( l
k
 ), k = 2, . . . , l −1

entonces se obtiene

Pn,α
< n-l >(X) = ( n
n−l
 )[
 Xl + ( l
2
 )β 2 Xl-2 + · · · + ( l
k
 )β k Xl-k + · · · + ( l
l -1
 )β l-1 X]
 + αl

Por hip´otesis, existe una ra´ız ρn-l ∈ Fp que Pn,α
< n-l >(X) comparte con Pn,α(X); tenemos,

pues
 −
( n
n−l
 )[ ρl
n-l + ( l
2
 )β 2 ρl-2
n-l + · · · + ( l
k
 )β k ρl-k
n-l + · · · + ( l
l -1
 )β l-1 ρn-l
 ] = αl, (5.10)

as´ı que construimos β l de la forma siguiente:

β l =
 



 ( n
n-l )−1 · αl = −
[ ρl
n-l + ( l
2
 )β 2 ρl-2
n-l + · · · + ( l
l-1
 )β l-1 ρn-l
 ]
, si ( n
n-l )̸≡ 0 mod p

0, si ( n
n-l )≡ 0 mod p. (5.11)

Es importante observar en (5.10) que, cuando para l ≥ 2 se tiene ( n
n-l
 )≡ 0 mod p, es

necesariamente nula αl, y por ello tiene sentido imponer que entonces sea β l = 0, indepen-

dientemente del valor contenido en el corchete. L´ogicamente, cuando ( n
l ) no es m´ultiplo

de p, el valor de β l est´a perfectamente determinado y se obtiene por mera divisi´on en el

cuerpo Fp, lo que hace en realidad innecesaria la segunda expresi´on en la primera l´ınea de

(5.9) y (5.11).

Una vez construido β cumpliendo la relaci´on esperada con α es ya posible considerar

el polinomio Pn,β(X) que, como se ha mostrado anteriormente, es id´entico a Pn,α(X) y

adem´as satisface, para cada i = 1, . . . , n−2, la relaci´on P < i >
n,α ( X) = ( n
i ) P [i]
n,β( X); de este

modo, las igualdades
 P n,α(ρi) = 0 = P < i >
n,α (ρi)

se reescriben en la forma
 P n,β(ρi) = 0 = ( n
i
 )P [i]
n,β(ρi).

De aqu´ı puede deducirse que ρi es, tambi´en, una ra´ız com´un a P n,β y P [i]
n,β —y, por

tanto, β anula la resultante H [i]— para todos aquellos i tales que ( n
i ) sea inversible en

Fp; evidentemente, este argumento no es aplicable para los i tales que sea ( n
i )≡ 0 mod p,

pero en este caso, y por construcci´on, se tiene β n-i = 0, de modo que β satisface la ecuaci´on

bn-i = 0, lo cual vimos —ya en la observaci´on 2.1.1— que es suﬁciente para que se cumpla

H [i] = 0. Ha quedado probado que es [β ] ∈ Yn( Fp ). □

5.3 Los supraesquemas X ′
n y R ′
n 99

Observaci´on 5.2.3. El punto [β ] ∈ Yn( Fp ) que acabamos de construir a partir de un

punto [α] ∈ Xn( Fp ) cumple β l = 0 en todos los casos en que es αl = 0, seg´un se desprende

de (5.9) y (5.11). En la construcci´on rec´ıproca, de [α] ∈ Xn( Fp ) a partir de [β ] ∈ Yn( Fp ),

es a´un m´as evidente que se cumple el enunciado an´alogo.

De lo anterior se deduce que, ﬁjado un conjunto de grados I⊂{2, . . . , n−1}, y si se deﬁne

el subesquema proyectivo Xn,I del esquema de coeﬁcientes ordinarios Xn por analog´ıa a

como, en el cap´ıtulo 3, se hab´ıa deﬁnido el subesquema proyectivo Z n,I del esquema Yn,

entonces, cualquiera que sea el primo p se tiene la equivalencia:

Xn,I ( Fp ) = ̸O ⇐⇒ Zn,I ( Fp ) = ̸O.

De acuerdo con la proposici´on 3.0.3, de aqu´ı se deduce la equivalencia

Xn,I (C) = ̸O ⇐⇒ Zn,I (C) = ̸O,

que no puede sorprendernos por cuanto que cada una de estas dos igualdades caracteriza

independientemente la respuesta aﬁrmativa para el I-problema parcial de Casas-Alvero en

grado n; el hecho destacable es que los primos que resultan eﬁcaces para garantizar (en el

sentido de la proposici´on 3.0.3) dicha respuesta aﬁrmativa son los mismos ya sea Xn,I o

Z n,I el esquema que utilicemos, de modo que podemos consistentemente hablar de primos

I-eﬁcaces para el grado n.

5.3. Los supraesquemas X ′
n y R ′
n

Las ecuaciones del esquema Yn expresan las hip´otesis de la conjetura de Casas-Alvero de

grado n y los puntos que dicho esquema pudiera poseer sobre C revelar´ıan los eventuales

contraejemplos a la misma, por construcci´on, siempre bajo la premisa de que α = 0 es la ra´ız

que Pn(X) comparte con su derivada de orden n−1. Relajando esta premisa de modo que

solamente suponga que α = 0 es una de las ra´ıces de Pn(X), en el cap´ıtulo 4 se construy´o un

nuevo esquema proyectivo que denotamos Y ′
n. Pasar de Yn a Y ′
n signiﬁc´o incorporar a b1
como una indeterminada m´as, y a˜nadir H [n-1] = 0 como ecuaci´on adicional. Una vez hecho

esto, el propio Yn se recupera como el subesquema de Y ′
n obtenido al sustituir por b1 = 0

a dicha ecuaci´on H [n-1] = 0 (m´as d´ebil que aquella),

La construcci´on de los esquemas Xn y Rn parte de aquella misma premisa, traducida

ahora en que sea a1 = an = 0 y x1 = ∑ xi = 0, respectivamente. Denotaremos por X ′
n y R ′
n
a los esquemas proyectivos que aparecen tras la relajaci´on de la premisa de partida; es

sencillo identiﬁcar las novedades: en el primer caso, se introduce la variable a1 y la nueva

ecuaci´on G< n-1 >= 0; en el segundo caso, la restricci´on ∑ xi = 0 se ve sustituida por la

ecuaci´on K < n-1 >= 0.

100 Cap´ıtulo 5. Esquemas alternativos

Otra vez, los esquemas Xn y Rn se recuperan bajo la forma de subesquemas de X ′
n y

R ′
n cuando se impone que el cumplimiento de las ecuaciones G< n-1 >= 0 y K < n-1 >= 0 se

concrete en el de las antiguas y m´as exigentes a1 = 0 y ∑ xi = 0. Es en este sentido en el

que empleamos la denominaci´on de supraesquema para cada uno de los esquemas Y ′
n, X ′
n
y R ′
n respecto del correspondiente esquema Yn, Xn y Rn.

La demostraci´on del teorema 5.2.2 se puede adaptar sin ning´un cambio signiﬁcativo

al caso de los esquemas X ′
n, R ′
n y Y ′
n, obteniendo que, para n y p dados, se tiene la

equivalencia entre las tres aﬁrmaciones siguientes:

(i ) X ′
n( Fp ) = ̸O, (ii ) R′
n( Fp ) = ̸O, (iii ) Y ′
n( Fp ) = ̸O.

Aplicando resultados del cap´ıtulo 4, el teorema siguiente prueba que, de hecho, los pares

eﬁcaces para cada uno de los seis esquemas proyectivos Xn , X ′
n , Rn, R ′
n, Yn y Y ′
n son

exactamente los mismos.

Teorema 5.3.1. Para un grado n y un primo p dados, las seis aﬁrmaciones siguientes

son equivalentes entre s´ı:

(i ) Xn( Fp ) = ̸O,

(ii ) Rn( Fp ) = ̸O,

(iii ) Yn( Fp ) = ̸O,
 (iv ) X ′
n( Fp ) = ̸O,

(v ) R ′
n( Fp ) = ̸O,

(vi ) Y ′
n( Fp ) = ̸O .

En particular, cada una de las anteriores igualdades constituye una condici´on suﬁciente

para que el problema de Casas-Alvero de grado n ≥ 3 posea respuesta aﬁrmativa.

Demostraci´on. Para n = 1 o n = 2 la equivalencia resulta obvia, pues las seis igualdades

son verdaderas por carecer todos estos esquemas de entidad geom´etrica (ver Nota 3.0.5):

En efecto, cuando es n = 1, as´ı como en el caso de X2, R2 e Y2, son esquemas que no

involucran ninguna variable; X ′
2, R′
2 e Y ′
2, por su parte, involucran cada uno una sola

variable, obligada a anularse por la ecuaci´on que deﬁne al esquema ( −a2
1 = 0, −b2
1 = 0 y

−x2
2 = 0, respectivamente), cualquiera que sea el cuerpo considerado.

En el caso n ≥ 3, las tres condiciones de la terna (i ), (ii ), (iii ) equivalen entre s´ı por

el teorema 5.2.2 y, seg´un acabamos de aﬁrmar, el resultado an´alogo se veriﬁca para los

supraesquemas, esto es, las tres condiciones de la terna (iv ), (v ), (vi ) tambi´en equivalen

entre s´ı. La cadena de equivalencias se cierra con la existente entre las condiciones (iii ) y

(vi ), establecida por el teorema 4.1.4 de eliminaci´on del t´ermino vicel´ıder.

Para concluir, basta apelar a la proposici´on 3.1.4. □

5.4 Aplicaci´on del esquema de ra´ıces 101

Corolario 5.3.2. El teorema de condensaci´on (4.2.1) y, en consecuencia, el principio de

expansi´on, as´ı como el teorema 4.3.1 que sit´ua a todo par eﬁcaz dentro de una estela, se

veriﬁcan igualmente para los esquemas Xn, R n, Y ′
n , X ′
n y R ′
n

Observaci´on 5.3.3. Dado que los seis esquemas considerados en 5.3.1 disponen de los

mismos pares eﬁcaces, podemos elegir cualquiera de ellos para trabajar en la pr´actica. As´ı,

en la Memoria se ha utilizado principalmente el esquema Yn, mientras que en [BLSW] el

esquema empleado es X ′, que involucra una variable m´as que Yn. En el pr´oximo aparta-

do, y usando el esquema de ra´ıces, Rn —con el mismo n´umero de variables que Yn— se

recuperar´an con notable econom´ıa de esfuerzo los resultados de cap´ıtulos anteriores co-

rrespondientes a h = 3, 4 y 5; adem´as —como ya se ha anunciado— se realizar´an c´alculos

concluyentes tambi´en para h = 6, y se mostrar´a asimismo que son viables para n = 7. Se ob-

serva que, mientras que el esquema Yn ha facilitado desarrollos de mayor valor conceptual,

el esquema Rn parece m´as operativo cuando se trata de llevar a cabo c´alculos efectivos

orientados a nuestros ﬁnes.

5.4. Aplicaci´on del esquema de ra´ıces a la determinaci´on de

los primos eﬁcaces

Nos proponemos a continuaci´on, ﬁjado un grado n ≥ 3, hallar el modo de discriminar los

primos ineﬁcaces con n, es decir, aquellos primos p tales que sobre el cuerpo Fp existan

soluciones no triviales del sistema de n−1 ecuaciones en las n−1 inc´ognitas x2, . . . , xn:

x2 + x3 + · · · + xn = x2 (x2 −x3) = K < 2 > = K < 3 > = · · · = K < n-2 > = 0 (5.12)

que deﬁne al esquema proyectivo Rn. Ello equivale a preguntarse por las condiciones que

hacen posible la existencia de un polinomio Pn(X) = ( X−x1) ( X−x2) · · · ( X−xn), con

ra´ıces no todas nulas x1, x2, . . . , xn pertenecientes a Fp , y tal que se cumpla:

(1 ) x1 = 0; x2 + x3 + · · · + xn-1 + xn = 0.

(2 ) La ra´ız x2 coincide, o bien con la ra´ız x1 = 0, o bien con una tercera ra´ız x3 ̸= 0.

(3 ) Para cada i = 2, . . . , n−2, Pn
< i >(X) tiene una ra´ız en com´un con Pn(X).

Supongamos que exista un polinomio como el descrito. Podemos asumir que la ra´ız

de Pn(X) ubicada en la posici´on de x3 es distinta de cero: Si es x2 ̸= 0, porque entonces

habr´a de ser x3 = x2; y si, por el contrario, se veriﬁca x2 = 0, porque entonces podremos

elegir en tercer lugar una ra´ız no nula que en todo caso posee Pn(X), ya que no ﬁgura

como x1 ni como x2. M´as a´un: por ser (5.12) un sistema homog´eneo, podemos suponer

102 Cap´ıtulo 5. Esquemas alternativos

que el valor de x3 es exactamente igual a 1, pues, de no ser as´ı, bastar´ıa cambiar la

soluci´on de partida por otra de su misma clase de equivalencia. Por otra parte, gracias a la

existencia de dos modos alternativos (aunque no excluyentes mediando una permutaci´on

de las ra´ıces) de satisfacer la condici´on (2), el problema se escinde de forma natural en

dos subproblemas independientes, correspondientes a cada uno de estos dos casos:

Caso I, abreviado [C- I]: Es x2 = 0 ; las ra´ıces de Pn(X) son, por tanto:

0, 0, 1, x4, x5, . . . , xn-1, xn, con x4 = − ( 1 + ∑

5≤j≤n
xj).

Caso II, abreviado [C-II]: Es x2 = x3 = 1 ; y las ra´ıces de Pn(X) son:

0, 1, 1, x4, x5, . . . , xn-1, xn, con x4 = − ( 2 + ∑

5≤j≤n
xj).

Obs´ervese que, en virtud de la condici´on (1), cada uno de estos subproblemas requiere

el uso de tan solo n−4 variables, pues x4 viene dada por el valor de las restantes. En

cuanto a la condici´on (3 ), es obvio que Pn

< i >(X) comparte alguna ra´ız con Pn(X) si y solo

si ocurre:

P n
< i >(0) = 0, o bien P n
< i >(1) = 0, o bien P n
< i >(x4) = 0, . . . o bien P n
< i >(xn) = 0,

de modo que (3 ) se materializa en un n´umero ﬁnito de casos particulares —en principio,

(n−1)n - 3, tantos como formas de adjudicar a cada derivada P n
< 2 >,. . . , P n
< n-2 >, una ra´ız

elegida entre 0, 1, x4, . . . , xn; si bien, en la pr´actica, el n´umero de casos distinguibles

ser´a mucho menor debido a las simetr´ıas que se aprecian entre algunas conﬁguraciones—.

Para n = 3, las ra´ıces son simplemente [ 0, 0, 1 ], en el caso I, y [ 0, 1, 1 ], en el caso II. La

condici´on (3) es vac´ıa; as´ı pues, solamente precisamos que se cumpla (1), es decir,

que sea nula la suma de las tres ra´ıces. Pero,

[C- I ] 0 + 0 + 1 = 0 , nunca ocurre;

[C-II ] 0 + 1 + 1 = 0 , ocurre si y solo si es p = 2.

Este an´alisis recupera de forma elemental el hecho de que el primo 2 sea el ´unico

ineﬁcaz para n = 3.

Para n = 4, la condici´on (1) obliga a que las ra´ıces sean [ 0, 0, 1, −1 ] en el caso I, y

[ 0, 1, 1, −2 ] en el caso II. Imponemos ahora la condici´on (3):

[C- I ] P4

< 2 >(X) = 6X 2 −1 ; por tanto: P4
< 2 >(0) = −1, P4
< 2 >(1) = P4
< 2 >(−1) = 5.

Ninguno de ellos se anula, a menos que sea p = 5.

[C-II ] P4

< 2 >(X) = 6X 2 −3 ; por tanto: P4
< 2 >(0) = − 3, P4
< 2 >(1) = 3, P4
< 2 >(−2) = 21.

Solamente para p = 3 o p = 7 se anula alguno de los tres.

Recuperamos as´ı el hecho de que 3, 5 y 7 son los ´unicos primos ineﬁcaces para n = 4.

5.4 Aplicaci´on del esquema de ra´ıces 103

A partir de aqu´ı se introduce la variable u = x5 + x6 + · · · + xn, con lo cual la condici´on (1)

deja x4 = −u −1 en el caso I, y x4 = −u −2 en el caso II. Esta expresi´on de x4 la em-

plearemos para la ra´ız que nos interese singularizar en cuarta posici´on —que puede ser

cualquiera de las ra´ıces que quedan una vez apartadas x1, x2 y x3 pues, a diferencia de

estas, no han sido marcadas a priori siendo, por tanto, intercambiables—.

Para n = 5, en particular, la variable u da forma concreta a las dos ´unicas ra´ıces que no

necesariamente son 0 o 1, y se tiene

[C- I ] P5(X) = X 2(X −1)(X + u + 1)(X − u)

[C-II ] P5(X) = X(X −1)
2(X + u + 2)(X − u).

La condici´on (3) impone esta vez que, para respectivos valores x e y coincidentes con

alguna de las ra´ıces de P5(X), se veriﬁquen las igualdades P5
< 3 >(x) = 0, P5
< 2 >(y) = 0.

Calculamos las derivadas de Hasse de ´ordenes 3 y 2 del polinomio P5(X) y obtenemos

la expresi´on expl´ıcita de este par de igualdades:

[C- I ] 10x2 −u2 −u −1 = 0; −10y2 + 3y (u2 + u + 1) −u(u + 1) = 0,

[C-II ] 10x2 −u2 −2u −3 = 0; −10y3 + 3y (u2 + 2u + 3) −2(u + 1)2 = 0.

La simetr´ıa entre las ra´ıces −1−u y u reduce a tan solo 20 (10 en cada caso) las

posibilidades distinguibles de adjudicar valores a x e y. Se detalla a continuaci´on,

para cada una ellas, el par de polinomios [f (u), g(u)] = [P5
< 3 >(x), P5
< 2 >(y)], y el valor

de su resultante, R.

Caso I : x = y = 0, [ −u2 −u −1, −u2 −u]
, R = 1

x = 0, y = 1, [ −u2 −u −1, 2u2 + 2u −7]
, R = 34

x = 0, y = u, [ −u2 −u −1, −7u3 + 2u2 + 2u] R = 34

x = 1, y = 0, [ −u2 −u + 9, −u2 −u]
, R = 34

x = y = 1, [ −u2 −u + 9, 2u2 + 2u −7]
, R = 112

x = 1, y = u, [ −u2 −u + 9, −7u3 + 2u2 + 2u]
, R = 32 · 3541

x = u, y = 0, [
9u2 −u −1, −u2 −u] R = −3
2

x = u, y = 1, [
9u2 −u −1, 2u2 + 2u −7] R = 3541

x = y = u, [
9u2 −u −1, −7u3 + 2u2 + 2u] R = 112

x = u, y = −u −1, [ 9u2 −u −1, 7u3 + 23u2 + 23u + 7]
, R = 3
2 · 3541

Caso II: x = y = 0, [ −u2 −2u −3, −2u2 −4u −2
]
, R = 24

x = 0, y = 1, [ −u2 −2u −3, u2 + 2u −3
]
, R = 22 · 32

x = 0, y = u, [ −u2 −2u −3, −7u3 + 4u2 + 5u −2]
, R = −22 · 3 · 193

x = 1, y = 0, [ −u2 −2u + 7, −2u2 −4u −2
]
, R = 28

x = y = 1, [ −u2 −2u + 7, u2 + 2u −3
]
, R = 24

(contin´ua)

104 Cap´ıtulo 5. Esquemas alternativos

(C-II) (continuaci´on)

x = 1, y = u, [ −u2 −2u + 7, −7u3 + 4u2 + 5u −2]
, R = 2
4 · 599

x = u, y = 0, [ 9u2 −2u −3, −2u2 −4u −2
]
, R = 2
8

x = u, y = 1, [ 9u2 −2u −3, u2 + 2u −3
]
, R = 24 · 3 · 7

x = y = u, [ 9u2 −2u −3, −7u3 + 4u2 + 5u −2]
, R = −2
4 · 131

x = u, y = −u −2, [ 9u2 −2u −3, 7u3 + 46u2 + 95u + 60]
, R = 2
4 · 3 · 7 · 8009

Un valor u ∈ Fp que haga anularse a los dos polinomios de una misma pareja pro-

porciona inmediatamente un polinomio P5(X) cumpliendo todas las condiciones re-

queridas, y viceversa; as´ı pues, el que la resultante R sea nula m´odulo p es condici´on

necesaria y (a menos que los respectivos coeﬁcientes l´ıder sean ambos m´ultiplos de p)

tambi´en suﬁciente para que se cumpla R5(Fp)̸= ̸O. De este modo, los primos ineﬁcaces

con n = 5 se encontrar´an entre los divisores de los diferentes R as´ı obtenidos.

Los resultados anteriores proporcionan otra demostraci´on del corolario 4.4.4. En

efecto, puesto que los coeﬁcientes l´ıder de los dos polinomios en cada corchete han

resultado ser primos entre s´ı, se cumple que R5(Fp) ̸= ̸O si y solo si p divide a alguno

de los valores de R que ﬁguran en la tabla anterior. Se deduce por tanto que los

primos ineﬁcaces para n = 5 son 2, 3, 7, 11, 131, 193, 599, 3541 y 8009.

Para n = 6 introduciremos una nueva variable v = x5 x6, que tomada junto con u = x5 + x6
encierra la misma informaci´on que el par no ordenado formado por x5 y x6. Se tiene

as´ı X2 −u X + v = ( X −x5)( X −x6), y podemos escribir:

[C- I ] P6(X) = X2( X −1)( X + u + 1)( X2 −u X + v)

[C-II ] P6(X) = X ( X −1)2 ( X + u + 2)( X2 −u X + v)

Como una alternativa al procedimiento usado con n = 5, esta vez impondremos en

primer lugar que el polinomio P6
< 4 >
(X) comparta una ra´ız con P6(X), esto es, que

se veriﬁque la igualdad P6 < 4 >(x) = 0 para alguno de los valores x ∈ {0, 1,−u−1} en el

caso I; o bien x ∈ {0, 1,−u−2} en el caso II —recordemos que las dos ra´ıces restantes,

x5 y x6, son intercambiables con x4— dejando para un segundo momento el uso

de las condiciones Res(P6, P6 < 3 >) = 0, Res(P6, P6 < 2 >) = 0. El inter´es de esta forma

de proceder radica en que la condici´on P6 < 4 >(x) = 0 impuesta de partida permite

despejar (para cada x de los citados) v en funci´on de u, gracias a que P6 < 4 > es un

polinomio de grado 1 en la variable v:

[C- I ] P6
< 4 >(X) = 15 X2 −u2 −u + v

[C-II ] P6
< 4 >(X) = 15 X2 −u2 −2u −3 + v

5.4 Aplicaci´on del esquema de ra´ıces 105

Obtenido por este procedimiento el valor v = v(u), al sustituirlo en las resultantes

Res(P6, P6 < 3 >) y Res(P6, P6 < 2 >) se consiguen dos polinomios en la variable u, R1(u)

y R2(u), respectivamente; la existencia de una ra´ız com´un a ambos ser´a condici´on

necesaria y suﬁciente para que exista un polinomio P6(X) como el buscado, lo que

equivale a una soluci´on no trivial del sistema que deﬁne a R6. Interesa entonces hallar

el valor del entero R = Res(R1(u), R2(u)
) para cada uno de los seis subcasos que se

presentan —tres por cada caso—, pues en la reuni´on de sus divisores se encuentran

todos los primos ineﬁcaces para n = 6 (y quiz´a tambi´en alguno que no lo sea). La

tabla que aparece a continuaci´on resume el desarrollo de esta casu´ıstica.

Caso I x = 0 R1(u) = 3456 u21 + (t
os menor grado), R2(u) = 6859 u18 + (t
os menor grado)

R = 272 · 724 · 13
12 · 1927 · 6712 · 20771
12

x = 1 R1(u) = 3456 u21 + (t
os menor grado), R2(u) = 6859 u18 + (t
os menor grado)

R = 272 · 751 · 11
36 · 139 · 199 · 61
12 · 213793 · 239939·

· 77832073 · 403625993 · 7390044713023799
3

x = -1-u R1(u) = 517856746176 u21 + (t
os m.g.), R2(u) = 47929184576 u18 + (t
os m.g.)

R = 254 · 739 · 11
36 · 136 · 1918 · 61
12 · 213793 · 239936·

· 77832073 · 403625993 · 73900447130237993

Caso II x = 0 R1(u) = 3456 u21 + (t
os menor grado), R2(u) = 6859 u18 + (t
os menor grado)

R = 272 · 5
108 · 76 · 29
3 · 373 · 476 · 73
6 · 8119 · 14873 · 3209
6·

· 3877
3 · 93373 · 172501873

x = 1 R1(u) = 216 u21 + (t
os menor grado), R2(u) = 6859 u18 + (t
os menor grado)

R = 254 · 5
108 · 79 · 19
3 · 373 · 739 · 976 · 10693 · 14993 · 4019
9·

· 685177
3 · 700167574073

x = -2-u R1(u) = 517856746176 u21 + (t
os m.g.), R2(u) = 47929184576 u18 + (t
os m.g.)

R = 254 · 5
108 · 729 · 11 · 19
2 · 23
16 · 372 · 674 · 2573 · 983 · 1087 · 1187·

· 1901 · 2287 · 3881 · 4019
3 · 4943 · 5471 · 6983 · 8699 · 15131 · 15823
2·

· 150203 · 2665873 · 547061 · 885061 · 10309512 · 9348983563·

· 2610767527031 · 225833117528659
2 · 51313000813080529

Cuadro 5.1: T´erminos l´ıder y resultante com´un de R1 y R2, en los seis casos distinguibles

106 Cap´ıtulo 5. Esquemas alternativos

Teorema 5.4.1. Los primos ineﬁcaces con n = 6 son los 53 siguientes, dados por
niveles:

Nivel 1: 2, 5, 7, 19.

Nivel 2: 11, 13, 29, 37, 61, 67, 73, 1487, 20771, 23993.

Nivel 3: 47, 257, 811, 1069, 3209, 3877, 3881, 8699, 9337, 15823, 21379, 150 203,
547 061, 7 783 207, 17 250 187, 40 362 599, 2 610 767 527 031, 7390 044 713 023 799.

Nivel 4: 23, 97, 983, 1087, 1187, 1499, 1901, 2287, 4019, 4943, 5471, 6983, 15131,
266 587, 685 177, 885 061, 1 030 951, 9348983563, 70016757407,
225 883 117 528 659, 51 313 000 813 080 529.

En consecuencia, la conjetura de Casas-Alvero es cierta para los enteros de la forma

n = 6p r siempre que p sea un primo diferente de los que ﬁguran en este listado.

Demostraci´on. En cada uno de los seis subcasos contenidos en la tabla 5.1, es v´alido

el siguiente razonamiento: Si el primo p divide a R pero no es un divisor com´un de los

coeﬁcientes l´ıder de R1 y R2, entonces R6(Fp) ̸= ̸O. Usando la informaci´on contenida

en dicha tabla puede comprobarse que, salvo en los subcasos tercero y sexto, los

mencionados coeﬁcientes l´ıder son primos entre s´ı, mientras que en el tercer y el

sexto subcaso los primos divisor com´un de ambos coeﬁcientes l´ıder son ´unicamente

p = 2 y p = 7, quienes se obtienen sin ninguna complicaci´on desde los otros subcasos.

Se concluye que cada uno de los primos aparecidos como factor de R en alguno de

los seis subcasos es en efecto ineﬁcaz con n = 6.

Para n = 7, un m´etodo combinado de los utilizados para n = 5 y n = 6 puede reproducirse

sin apenas cambios y m´ınimas complicaciones de procedimiento, si bien con un con-

siderable incremento de la capacidad de c´omputo requerida para llevarlo a t´ermino.

En este caso, la variable u se complementa con v = x5 x6 + x5 x7 + x6 x7 y w = x5 x6 x7,

dando lugar a las expresiones:

[C- I ] P7(X) = X2( X −1)( X + u + 1)( X3 −u X2 + v X − w)

[C-II ] P7(X) = X ( X −1)2 ( X + u + 2)( X3 −u X2 + v X − w)

En una primera etapa impondremos que P7
<5 >(X) tenga una ra´ız x que tome uno de

los valores 0, 1, −1−u, en el caso I; 0, 1, −2−u, en el caso II. En una segunda etapa,

imponemos a P7
<4 >(X) que tenga una ra´ız y coincidente con uno de los valores

0, 1, −1−u, en el caso I; 0, 1, −2−u, t (siendo t una ra´ız de X 3 −u X 2 + v X − w), en

el caso II.

Se obtienen nueve posibilidades distintas de combinar los valores de x e y en el

caso I, y diez posibilidades en el caso II; estas ´ultimas son, en concreto, las nueve

5.5 Esquemas sint´eticos 107

que corresponden a que tanto x como y sean 1, 2 o −2−u, m´as una posibilidad especial

que corresponde a x = −2−u, y = t. Excluida esta ´ultima posibilidad, que seguiremos

llamando especial, en las dieciocho restantes se veriﬁca lo siguiente: La condici´on

P 7
<5 >(x) = 0 es lineal en w, lo cual permite despejar w como funci´on de (u, v) y

sustituirla luego en la condici´on P 7
<4 >(y) = 0, y la expresi´on que se obtiene entonces

resulta ser lineal en v. En deﬁnitiva, en cada una de estas dieciocho posibilidades,

del par de condiciones
 P 7
<5 >(x) = 0, P 7
<4 >(y) = 0

se logra despejar v = v(u) , w = w(u, v(u)
). (5.13)

Las condiciones de que P7
<3 >(X) y P7
<2 >(X) compartan respectivas ra´ıces con P7(X)

se incorporar´an a trav´es de los polinomios

Res(P7(X), P7
<3 >(X)
) , Res(P7(X), P7
<2 >(X)
) ∈ Z[u, v, w]

quienes, mediante la sustituci´on (5.13), dan lugar a dos polinomios

R3(u) , R2(u) ∈ Z[u];

se precisa que R3(u) y R2(u) se anulen simult´aneamente, esto es, que compartan una

ra´ız en Fp. Las dieciocho resultantes de la forma R = Res(R3(u), R2(u)
) son n´umeros

enteros cuyos divisores primos son ineﬁcaces para h = 7.

En el caso especial, la expresi´on para despejar w es igualmente lineal, pero la ex-

presi´on para despejar v es cuadr´atica en v; no obstante, mediante algunas argu-

mentaciones adicionales, esta complicaci´on puede a´un tratarse de forma adecuada,

de modo que se llegue a obtener tambi´en los primos ineﬁcaces aportados por dicho

caso, completando el conjunto de todos los primos ineﬁcaces con h = 7.

Puesto que el procedimiento descrito, seg´un hemos comprobado, excede la capacidad

de c´omputo del programa DERIVE, no presentamos el listado de resultados que

podr´ıa obtenerse del mismo; por otra parte, la lista de primos ineﬁcaces con h =7 ya

ha sido proporcionada por Castryck et al. y puede consultarse en [CLO-2]. Consta

de 661 primos, denominados por los autores ‘primos malos Casas-Alvero’ (CA-bad

primes).

5.5. Esquemas sint´eticos

De entre los esquemas de aplicaci´on al problema total de Casas-Alvero de grado n que

hemos ido utilizando (Yn, Xn y Rn, as´ı como sus respectivos supraesquemas Y ′
n, X ′
n y R ′
n)

es el esquema de ra´ıces el que mayor simplicidad conﬁere a los c´alculos, como consecuencia

108 Cap´ıtulo 5. Esquemas alternativos

de haber asignado selectivamente los valores de 0 o de 1 a las tres primeras ra´ıces del

polinomio. Para manejar los problemas parciales disponemos hasta el momento de los

subesquemas de Yn denotados como Zn,I , as´ı como de los an´alogos subesquemas de Xn
denotados por Xn,I .

En esta secci´on describiremos nuevos esquemas, que llamaremos esquemas sint´eticos,

para su aplicaci´on en los problemas parciales de Casas-Alvero. Nos referiremos en concreto

al I-problema parcial de Casas-Alvero donde I tiene cardinal r ≥ 1 y sus elementos son los

enteros kr, kr−1, . . . , k1, con

0 < kr < kr-1 < . . . < k2 < k1 < n −1 < n.

Sin alteraci´on signiﬁcativa del desarrollo posterior, podr´ıamos dejar que la desigualdad

k1 < n−1 fuera no estricta, pero en consonancia con el resto de la Memoria prescindimos

del innecesario grado n−1.

Puesto que el polinomio Pn(X) comparte la ra´ız de valor 0 con cada una las derivadas

cuyo orden no se encuentra en I, bastar´a con introducir variables sr, sr-1, . . . , s1 cuyos

valores, en cada supuesto particular, sean los de las ra´ıces de Pn(X) compartidas con sus

derivadas de orden kr, kr-1, . . . , k1, respectivamente.

Seg´un se se˜nal´o en la observaci´on 5.2.3 —inmediatamente despu´es de probar que Yn
y Xn tienen los mismos primos eﬁcaces—, siendo K cualquiera de los cuerpos Fp o C se

veriﬁca la equivalencia entre las dos condiciones Zn,I (K) = ̸O y Xn,I (K) = ̸O, de modo

que podemos utilizar indistintamente, o bien derivadas netas y coeﬁcientes presentados, o

bien derivadas de Hasse y coeﬁcientes ordinarios para determinar la existencia de contra-

ejemplos sobre K del problema parcial.

En esta secci´on consideraremos derivadas de Hasse y coeﬁcientes ordinarios; en parti-

cular, a las r variables anteriores les a˜nadiremos las r variables an-k1, an-k2, . . . , an-kr que

ﬁguran como coeﬁcientes del polinomio

Pn,I ( X) = Xn + an-k1 X k1 + an-k2 X k2 + · · · + an-kr X kr .

Entonces se tiene que Xn,I (K) ̸= ̸O si y solo si existe una soluci´on

(αn-k1 , αn-k2 , . . . , αn-kr , σr , σr-1, . . . , σ1) ∈ K2r,

con no todas las componentes αn-l nulas, para el sistema de ecuaciones

Pn,I (sr) = Pn,I (sr-1) = . . . = Pn,I (s1) = 0

Pn,I

< kr >(sr) = Pn,I

< kr-1 >(sr-1) = . . . = Pn,I

< k1 >(s1) = 0. (5.14)

Dado que se tiene Pn,I

< kl >( X) = ( n
kl ) Xn-kl + ( k1
kl ) an-k1 Xk1 -kl + . . . + an-kl, la condici´on

de que no sean nulas todas las componentes αn-k1, αn-k2, . . . , αn-kr es equivalente a que

5.5 Esquemas sint´eticos 109

no sean nulas todas las ra´ıces compartidas σr, σr-1, . . . , σ1. Podemos observar que las

2r ecuaciones del sistema anterior son lineales en las variables an-k1, an-k2, . . . , an-kr y

que, si consideramos ´unicamente las r ´ultimas ecuaciones, entonces la matriz ampliada de

tal subsistema de ecuaciones lineales en dichas variables es la matriz r × (r + 1) siguiente

(donde, por conveniencia, se ha puesto k0 = n):




















 ( k0
kr )sk0 -kr
r ( k1
kr )sk1 -kr
r . . . . . . . . . (kr-1
kr )skr-1 -kr
r 1
( k0
kr-1)s
k0 -kr-1
r-1 ( k1
kr-1)s
k1 -kr-1
r-1 . . . . . . . . . 1
( k0
kr-2)s
k0 -kr-2
r-2 ( k1
kr-2)s
k1 -kr-2
r-2 . . . . . . 1

... ... 1
... ... 1

( k0
k1 )s
k0 -k1
1 1
 


















 (5.15)

habida cuenta de que la primera columna corresponde a los t´erminos independientes (en

realidad, con signo opuesto). Podemos apreciar que el t´ermino general es de la forma
( kl
km)skl -km
m , con 1 ≤ m ≤ r y 0 ≤ l ≤ r, entendiendo que ( kl
km) = 0 si m < l. En particular, la

matriz de coeﬁcientes del subsistema es triangular con unos en la diagonal; por tanto, se

trata de un subsistema de Cramer cuya ´unica soluci´on proporciona expresiones precisas

an-kl = an-kl(s1, . . . , sl), 1 ≤ l ≤ r (5.16)

que son polinomios homog´eneos con coeﬁcientes enteros y de grado igual al respectivo

sub´ındice. Estas expresiones de las am en t´erminos de las sm se pueden sustituir en las r

primeras ecuaciones del sistema 5.14, convirtiendo la condici´on Pn,I (sl) = 0 en una expre-

si´on Ml(s1, . . . , sr) = 0 , donde Ml es un polinomio homog´eneo de grado n en las variables

s1, . . . , sr.

Deﬁnici´on 5.5.1. Llamaremos esquema sint´etico correspondiente al conjunto de grados I,

y denotaremos por Sn,I , al esquema proyectivo deﬁnido por el ideal del anillo Z[s1, . . . , sr]

generado por los polinomios homog´eneos Ml(s1, . . . , sr), para 1 ≤ l ≤ r.

Teorema 5.5.2. Siendo K cualquiera de los cuerpos Fp o C, son equivalentes:

(i ) Zn,I ( K) ̸= ̸O

(ii ) Sn,I ( K) ̸= ̸O.

En particular, el I-problema parcial de Casas-Alvero en grado n tiene respuesta aﬁrmativa

si y solo si Sn,I ( Fp ) = ̸O para alg´un primo p.

110 Cap´ıtulo 5. Esquemas alternativos

Demostraci´on. La segunda parte es consecuencia inmediata de la primera, seg´un las

proposiciones 3.1.2 y 3.0.3. Para probar la equivalencia entre (i ) y (ii ) utilizaremos el

hecho de que (i ) equivale a su vez a que sea X n,I ( K) ̸= ̸O (ver observaci´on 5.2.3).

Si se tiene X n,I ( K)̸= ̸O, bastar´a tomar un representante cualquiera de uno de sus pun-

tos para obtener los coeﬁcientes de un I-polinomio que comparte ra´ıces en K con todas sus

derivadas de grado positivo; considerando r ra´ıces σr, . . . , σ1 compartidas respectivamente

con las derivadas de orden kr, . . . , k1 se completa la 2r-upla (αn-k1 , . . . , αn-kr , σr , . . . , σ1)

que es soluci´on no nula (y con alg´un σl ̸= 0) del sistema (5.14); en particular, la r-upla

(σ1, σ2, . . . , σr) ∈ K r es soluci´on de las ecuaciones Ml(s1, . . . , sr) = 0 , 1 ≤ l ≤ r, que deﬁnen

al esquema Sn,I .

Rec´ıprocamente, la existencia de alg´un punto en Sn,I ( K) supone la existencia de

alguna soluci´on no trivial (σ1, σ2, . . . , σr) ∈ K r del sistema Ml(s1, . . . , sr) = 0 , 1 ≤ l ≤ r; bas-

ta ahora aplicar las f´ormulas (5.16) para completar una soluci´on del sistema (5.14), la

cual describe un I-polinomio —distinto de Xn— cuyos coeﬁcientes determinan un punto

perteneciente a X n,I ( K). □

Observaci´on 5.5.3. En el problema total de Casas-Alvero de grado n (asociado al con-

junto completo de exponentes, J = {1, 2, . . . , n−2}), el concepto de primo p ineﬁcaz con n

de nivel m introducido en 4.4.1 expresa la doble condici´on de ser Yn( Fp ) = Zn,J ( Fp ) ̸= ̸O

y de ser m el m´ınimo cardinal entre los subconjuntos I ⊂ J tales que Zn,I ( Fp ) ̸= ̸O. El

teorema anterior y la observaci´on 5.2.3 muestran que, a efectos de determinar el nivel de

ineﬁcacia de p, los esquemas Xn,I y Sn,I pueden intercambiarse con Zn,I .

Los esquemas sint´eticos son una opci´on alternativa para estudiar la conjetura de Casas-

Alvero cuando se tiene informaci´on acerca del conjunto I en que se encuadra un hipot´etico

contraejemplo. A continuaci´on supondremos que conocemos I y que consideramos contra-

ejemplos en los cuales sea an-kr ̸= 0. Necesitamos para ello la carta af´ın del esquema

sint´etico Sn,I dada por sr ̸= 0 y denotaremos por Un,I ( K) el subconjunto de Sn,I ( K) for-

mado por los puntos del esquema sint´etico tales que sus coordenadas homog´eneas pueden

elegirse del tipo (s1, . . . , sr-1, 1), de modo que s1, . . . , sr-1 sirvan como coordenadas aﬁnes

para dicha carta. Asumiremos en adelante r ≥ 2 y, por motivos pr´acticos, reformulare-

mos m´ınimamente la notaci´on escribiendo q = r −2, kr = i, kr-1 = j, sr-1 = t. En particular,

las coordenadas aﬁnes ser´an (s1, . . . , sq, t) a partir de ahora, y mantendremos siempre la

restricci´on sr = 1. El sistema (5.14) adopta la siguiente forma:

Pn,I (1) = Pn,I (t) = Pn,I (sq) = . . . = Pn,I (s1) = 0

Pn,I

< i >(1) = Pn,I

< j >(t) = Pn,I

< kq >(sq) = . . . = Pn,I

< k1 >(s1) = 0; (5.17)

5.5 Esquemas sint´eticos 111

y de aqu´ı, tomando la primera de cada uno de los dos grupos de q + 2 condiciones, extraemos

el sistema lineal 1 +
 q∑

l = 1 an-kl + an-j + an-i = 0

( n
i ) +
 q∑

l = 1
 ( kl
i ) an-kl + ( j
i ) an-j + an-i = 0,

a partir del cual se obtienen las expresiones
(1 −( j
i )) an-i = (( j
i ) −( n
i )) +
 q∑

l = 1
 (( j
i ) −( kl
i )) an-kl

− (1 −( j
i )) an-j = (1 −( n
i )) +
 q∑

l = 1
 (1 −( kl
i )) an-kl

que permiten despejar an-i, an-j siempre que sea 1 −( j
i ) ̸= 0 en K, es decir, cuando sea

K ̸= Fp para aquellos primos p divisores de 1 −( j
i ); si este es el caso, podemos sustituir las

expresiones obtenidas en las 2q + 2 ecuaciones restantes de (5.17) dando lugar a otras tantas

condiciones lineales en an-k1, . . . , an-kq cuyos coeﬁcientes son polinomios no homog´eneos en

las variables s1, . . . , sq, t. De estas condiciones, las que se obtienen a partir de las ´ultimas

q + 1 ecuaciones del primer grupo se expresan respectivamente en la forma siguiente:

Cn( t ) +
 q∑

l = 1 Ckl( t ) an-kl = 0

Cn(sm) +
 q∑

l = 1 Ckl(sm) an-kl = 0, m = 1, . . . , q, (5.18)

siendo Ch( X) = (1 −( j
i )) ( Xh − Xi) − (1 −( h
i )) ( Xj − Xi) para h ≥ j. Adem´as, del

segundo grupo de ecuaciones en (5.17), la segunda condici´on est´a dada por

Cn

<j >( t ) +
 q∑

l = 1 Ckl

<j >( t ) an-kl = 0, (5.19)

y las q condiciones ´ultimas forman un sistema de Cramer de ecuaciones lineales en las

inc´ognitas an-k1, . . . , an-kq ,

Cn

<km >(sm) +
 m∑

l = 1 Ckl

<km >(sm) an-kl = 0, m = 1, . . . , q,

cuya matriz ampliada es la submatriz obtenida de (5.15) al suprimir las dos primeras ﬁlas

y las dos ´ultimas columnas. En particular, la soluci´on ´unica de este sistema de Cramer

vuelve a proporcionar para estas q indeterminadas las mismas expresiones

an-kl = an-kl(s1, . . . , sl)

que se ten´ıan en (5.16). Las sustituci´on de estas an-kl en las q + 1 ecuaciones (5.18) y en la

ecuaci´on (5.19) da lugar a expresiones polin´omicas no homog´eneas en Z
[
s1, . . . , sq, t]

112 Cap´ıtulo 5. Esquemas alternativos

N(s1, . . . , sq, t) = 0

Nm(s1, . . . , sq) = 0, 1 ≤ m ≤ q,

N ′(s1, . . . , sq, t) = 0 ,
 (5.20)

de las cuales, las q intermedias no involucran a la variable t; la primera es de grado n

en t y coeﬁciente inicial 1 −( j
i ), y la ´ultima es de grado n−j en t y coeﬁciente inicial
(1 −( j
i ))(n
j ). Deﬁnimos ﬁnalmente

R(s1, . . . , sq) = Rest(N(s1, . . . , sq, t) , N ′(s1, . . . , sq, t)
) ∈ Z[s1, . . . , sq],

y consideramos las q + 1 condiciones en las variables s1, . . . , sq dadas por

R(s1, . . . , sq) = 0

Nm(s1, . . . , sq) = 0 , 1 ≤ m ≤ q. (5.21)

Proposici´on 5.5.4. Sea K = C o Fp. Si se cumple 1 −( j
i ) ̸= 0 en K, entonces son condi-

ciones equivalentes:

(i ) Un,I ( K) = ̸O

(ii ) El sistema (5.20) no tiene soluci´on en K q + 1.

(iii ) El sistema (5.21) no tiene soluci´on en K q.

Demostraci´on. La equivalencia entre (i ) y (ii ) se debe a que (5.20) expresa la condici´on

necesaria y suﬁciente para que [
(s1, . . . , sq, t, 1)
] se encuentre en Sn,I ( K) —perteneciendo,

de hecho, a la carta local adecuada para ser un elemento de Un,I ( K)—. La implicaci´on

(iii )⇒(ii ) tambi´en es evidente, ya que si (σ1, . . . , σq, τ ) ∈ K q + 1 es soluci´on de (5.20) en-

tonces (σ1, . . . , σq)∈K q es soluci´on de (5.21). Rec´ıprocamente, si (σ1, . . . , σq)∈K q es soluci´on

de (5.21) entonces se tiene, en particular, R(σ1, . . . , σq) = 0. Dado que este valor num´eri-

co es la resultante de los polinomios N(σ1, . . . , σq, t) y N ′(σ1, . . . , σq, t) pertenecientes a

K[ t ], y que el coeﬁciente de grado n del primero es 1 −(j
i ) —por hip´otesis, no nulo— ello

signiﬁca que existe τ ∈ K cumpliendo N(σ1, . . . , σq, τ ) = N ′(σ1, . . . , σq, τ ) = 0, de modo que

la (q + 1)-upla formada es soluci´on de (5.20); esto prueba la implicaci´on (ii )⇒(iii ). □

5.6. Discriminantes

Con las notaciones anteriores, denotaremos por J (n, I ) y J (n, I )K a los ideales respecti-

vamente de Z[s1, . . . , sq] y de K[s1, . . . , sq] generados por los q + 1 polinomios R(s1, . . . , sq)

y Nm(s1, . . . , sq), 1 ≤ m ≤ q. De igual modo, denotaremos por Jo(n, I ) y Jo(n, I )K a los

ideales respectivamente de Z[s1, . . . , sq, t] y de K[s1, . . . , sq, t] generados por los q + 2

polinomios N(s1, . . . , sq, t), N ′(s1, . . . , sq, t) y Nm(s1, . . . , sq), 1 ≤ m ≤ q.

5.6 Discriminantes 113

Deﬁnici´on 5.6.1. Llamaremos discriminante asociado a los datos (n, I) a un generador

∆(n, I ) del ideal principal de Z dado por J (n, I ) ∩ Z, y llamamos discriminante primitivo

asociado a (n, I) a un generador ∆o(n, I ) del ideal principal de Z dado por Jo(n, I ) ∩ Z.

El discriminante y el discriminante primitivo —siempre que sean no nulos— est´an bien

deﬁnidos salvo el signo; por esta raz´on en las igualdades de las expresiones que les afecten

obviaremos siempre el signo. Dado que R(s1, . . . , sq) pertenece al ideal generado por

N(s1, . . . , sq, t) y N ′(s1, . . . , sq, t) (ver nota 1.3.1) se tiene que ∆o(n, I ) divide a ∆(n, I ).

El teorema siguiente muestra en particular que ∆(n, I ) es no nulo si y solo si lo es

tambi´en ∆o(n, I ), puesto que ambas condiciones equivalen a la existencia de alg´un con-

traejemplo a la conjetura de Casas-Alvero de un determinado tipo.

Teorema 5.6.2. Para un grado n y un conjunto de exponentes I dados, son condiciones

equivalentes las siguientes:

(i ) Un,I ( C) = ̸O

(ii ) ∆(n, I ) ̸= 0

(iii ) ∆o(n, I ) ̸= 0.

Demostraci´on. Seg´un la proposici´on 5.5.4, Un,I ( C) = ̸O equivale a que el sistema

R(s1, . . . , sq) = N1 (s1, . . . , sq) = · · · = Nq (s1, . . . , sq) = 0

carezca de soluciones sobre C. Por el teorema de los ceros de Hilbert, ello equivale a su

vez a que el ideal J (n, I )C coincida con C[s1, . . . , sq], esto es, a que se tenga

1 = B0 R +
 q∑

l = 1 Bl Nl, con Bl ∈ C[s1, . . . , sq] para l = 0, 1, . . . , q. (5.22)

Argumentando de igual modo que se hizo en la demostraci´on de 3.0.3 se concluye que,

en caso de darse una igualdad como la anterior, los polinomios Bl involucrados pueden

elegirse con todos sus coeﬁcientes racionales; entonces, tomando el m´ınimo com´un m´ultiplo

m de todos sus denominadores y multiplicando por ´el, (5.22) se reescribe como

m = (mB0) R +
 q∑

l = 1 (mBl) Nl, con mB l ∈ Z[s1, . . . , sq] para l = 0, 1, . . . , q.

La existencia de un entero m ̸= 0 que responda a la expresi´on anterior caracteriza que

J (n, I ) ∩ Z no sea el ideal nulo o, equivalentemente, que su generador ∆(n, I ) sea diferente

de cero.

Hemos demostrado (i ) ⇔ (ii ); la prueba de (i ) ⇔ (iii ) es totalmente paralela, em-

pleando esta vez el sistema (5.20) y los ideales Jo(n, I )C y Jo(n, I ). □

114 Cap´ıtulo 5. Esquemas alternativos

Corolario 5.6.3. Para un grado n y un conjunto de exponentes I dados, se veriﬁcan

las condiciones equivalentes del teorema anterior si y solo si, al aplicar el algoritmo de

Buchberger al sistema de generadores {R, N1, . . . , Nq} del ideal J (n, I )Q —cualquiera que

sea el orden monomial considerado—, se obtiene en alguna de las etapas un polinomio m

con multigrado nulo, esto es, m ∈ Q-{0}.

Demostraci´on. Se desprende de la demostraci´on del teorema anterior. Cabe destacar que,

si la aplicaci´on del algoritmo de Buchberger se atiene a la descripci´on dada en la subsecci´on

1.3.3, entonces el n´umero racional m que —en su caso— ha de obtenerse es, de hecho, un

entero. Se sigue que m pertenece al ideal J (n, I ) ∩ Z y que, por tanto, es un m´ultiplo del

discriminante ∆(n, I ). □

Observaci´on 5.6.4. La eventual existencia de un primo p tal que ∆(n, I ) ̸≡ 0 mod p

garantizar´ıa, no solo que es Un,I ( C) = ̸O (por el teorema anterior), sino tambi´en que es

Un,I ( Fp ) = ̸O. En efecto, tambi´en para el cuerpo K = Fp el teorema de los ceros de Hilbert

proporciona la equivalencia entre las condiciones Un,I ( K) = ̸O y 1 ∈ J (n, I )K. Entonces,

basta tomar una igualdad del tipo

∆(n, I ) = C0 R +
 q∑

l=1 Cl Nl, con C0, Cl ∈ Z[s1, . . . , sq]

—cuya existencia viene garantizada por la deﬁnici´on de ∆(n, I )— y reducirla m´odulo p,

obteniendo ∆(n, I ) = C0 R +
 q∑

l=1 Cl Nl, con C0, Cl ∈ Fp[s1, . . . , sq].

Puesto que, por hip´otesis, ∆(n, I ) ∈ J (n, I )
Fp es un elemento no nulo de Fp, se concluye

que 1 pertenece a J (n, I )
Fp y que, por tanto, es Un,I ( Fp ) = ̸O.

Deﬁnici´on 5.6.5. Para un conjunto de cardinal 1, I = {i}, deﬁnimos el discriminante

asociado a los datos (n, I) como el n´umero entero ∆(n, I ) = 1 −( n
i ). Observemos que la

condici´on ∆(n, I ) ̸≡ 0 mod p es necesaria y suﬁciente para que Un,I ( Fp ) = Sn,I ( Fp ) sea

vac´ıo, puesto que el esquema sint´etico Sn,{i} (cuyos puntos, si los tiene, cumplir´an nece-

sariamente s1 ̸= 0) viene deﬁnido por la ecuaci´on (
1 −( n
i ))
sn
1 = 0. La imposibilidad de que

ocurra ∆(n, I ) = 0 se corresponde con el hecho de que Sn,{i}( C) es vac´ıo para todo par de

grados n, i.

Si existiera un contraejemplo a la conjetura de Casas-Alvero de grado n, para el conjun-

to I de los grados de los t´erminos distintos del l´ıder con coeﬁciente no nulo se cumplir´ıa

Sn,I ( C) ̸= ̸O y tambi´en Un,I ( C) ̸= ̸O. M´as a´un, siendo i el m´ınimo de tales grados y

5.6 Discriminantes 115

considerando el conjunto de exponentes Ii = {i, i + 1, . . . , n−2}, se tendr´ıa Un,Ii( C) ̸= ̸O.

En consecuencia, el problema de Casas-Alvero en grado n tiene respuesta aﬁrmativa si

y solo si se cumple Un,Ii( C) = ̸O para todo i = 1 . . . , n−2. El teorema que acabamos de

probar traduce esta condici´on en que sean no nulos todos los discriminantes ∆(n, Ii) para

i = 1, . . . , n−2, esto es, que no se anule el producto de todos ellos. En consecuencia, es v´alida

la siguiente formulaci´on:

Conjetura de Casas-Alvero. Para cada n se veriﬁca Dn ̸= 0, siendo Dn = n−2∏

i=1 ∆(n, Ii),

seg´un deﬁniciones previas.

Queda as´ı demostrado, en particular, lo siguiente:

Teorema 5.6.6. La conjetura de Casas-Alvero admite una formulaci´on en t´erminos de

naturaleza aritm´etica. □

Nota 5.6.7. El producto de los n−2 discriminantes, Dn, puede ser llamado superdiscri-

minante, o discriminante absoluto. Puesto que sabemos, por 2.2.3 y 2.3.4, que no existen

contraejemplos a la conjetura con menos de tres t´erminos adicionales al l´ıder, tenemos

garant´ıa de que ∆(n, In -2) y ∆(n, In -3) son siempre distintos de cero. Siendo n ≥ 5 tambi´en

es inmediato probar que es ∆(n, In -4)̸=0, pues siempre existe un primo p tal que (In-4)
p = ̸O,

deduci´endose entonces del teorema de resoluci´on por interpretaci´on 3.3.1 que tampoco se

tienen contraejemplos para i = n−4. El primo que nos sirve a este ﬁn es cualquier p ≥ 5 que

divida, bien a n, bien a n−1, si es que existe; en caso contrario servir´a p = 2 o bien p = 3,

pues entonces n habr´a de ser de la forma 2a o 3a, dado que necesita ser primo con n −1,

a su vez de la forma 3b o 2b.

Por otra parte, si n es de la forma p r+ 1 o 2p r+ 1, se desprende del teorema 3.6.2 que

entonces la sola condici´on ∆(n, I1) ̸= 0 equivale a que la conjetura de Casas-Alvero sea

cierta, pues no son viables contraejemplos sin t´ermino de grado 1.

Quiere esto decir que, en general, el rango de valores i para los que la condici´on

∆(n, Ii) ̸= 0 es necesaria para asegurar la conjetura es mucho m´as peque˜no que el del inter-

valo de n´umeros naturales [1, n−5], y se reduce para n general o espec´ıﬁco en funci´on del

avance de los resultados sobre la conjetura. Con los de esta Memoria se puede, por ejem-

plo, mejorar tambi´en la cota general n −5, de modo que el anterior enunciado en t´erminos

del superdiscriminante Dn puede aﬁnarse empleando un valor ̃Dn con bastantes factores

menos. De hecho, un superdiscriminante din´amico ̃Dn podr´ıa deﬁnirse en cada momen-

to como el resultado de suprimir en Dn aquellos factores de quienes hayamos obtenido

constancia, por cualquier v´ıa, de que son distintos de cero.

116 Cap´ıtulo 5. Esquemas alternativos

Independientemente de esta posibilidad, el ´enfasis recae ahora en el hecho de haber

descrito para cada n un n´umero cuyo c´alculo es en principio factible y tal que su anulaci´on

o no equivale a la existencia o no de contraejemplos a la conjetura de Casas-Alvero.

Revisi´on del caso r = 2. En el segundo cap´ıtulo de esta Memoria se encuentran los

resultados 2.2.2 y 2.3.3, que reducen la resoluci´on del I-problema parcial para r = 1 y r = 2

a veriﬁcar respectivamente que se cumplen las condiciones 1−a ̸= 0 y (1−a)(1−b) ∆ ̸= 0,

donde ∆ = a ρ (b −c)ρ(b −ac)σ − (−1)σ(a −1)ρ+σ(b −1)ρ (5.23)

para los enteros a, b, c, ρ, σ en 2.3.3 asociados a la terna n, i, j. Recordemos que la prueba

de ∆ ̸= 0 es existencial; consiste en demostrar que existen primos p tales que ∆ ̸≡ 0 mod p.

A continuaci´on se muestra la relaci´on entre este ∆ de (5.23) y el discriminante ∆(n; {i, j})

cuya no anulaci´on caracteriza, en virtud de 5.6.2 y 5.5.4, la no existencia de soluciones

para el sistema de ecuaciones N(t) = N ′(t) = 0 que proporciona las coordenadas aﬁnes de

aquellos puntos de la variedad proyectiva Sn,{i,j}( C) ubicados en la carta local s2 ̸= 0; esto

es, la no existencia de {i, j}-contraejemplos con an-i ̸= 0 para el problema de Casas-Alvero

de grado n.

Teorema 5.6.8. Para I = {i, j} se tiene la igualdad

∆(n, I ) = (a −1)i (e −1)n-j ∆d,

donde e = ( j
i ), d = m.c.d.
(n−j, j −i
), y ∆ obedece a la expresi´on (5.23).

Demostraci´on. Siendo en este caso q = 0, se tiene J (n, I ) = ⟨R ⟩ con R = Res(N(t), N ′(t)
)∈Z,

de modo que el discriminante ∆(n, I ) no es otro que el n´umero R. Como puede compro-

barse, se cumple

N (t) = t i · ̃N (t), con ̃N (t) = (1 −e) t n-i + (a −1) t j -i + (e −a);

mientras que es N ′(t) = b(1 −e) t n-j + (a −1) (debe advertirse que este polinomio no es la

derivada del anterior). As´ı pues,

R = Res(t, N ′(t)
)i · Res( ̃N (t), N ′(t)
) = (a −1)i · Res( ̃N (t), N ′(t)
).

El c´alculo Res( ̃N (t), N ′(t)
) se conduce, mediante la sustracci´on de las n−j primeras ﬁlas

multiplicadas por b a las n−j ﬁlas siguientes en la matriz correspondiente, y el desarrollo

del determinante por las primeras n−j columnas (ya con un ´unico elemento no nulo) a

una situaci´on en la que procede aplicar el lema 2.3.1. Teniendo en cuenta que (−1)ρσ+ρ

coincide necesariamente con (−1)σ+1 (pues solo diferir´ıan en caso de ser pares tanto ρ

como σ, algo imposible por ser primos entre s´ı) se obtiene de inmediato

5.6 Discriminantes 117

Res( ̃N (t), N ′(t)
) = (e −1)n-j ∆d,

tal como se requiere para la veriﬁcaci´on del teorema. □

Caso particular r = 3. Para un conjunto de exponentes I = {i, j , k} se tiene q = r−2 = 1,

y el sistema (5.21) toma la forma N1(s1) = R(s1) = 0. Podemos comprobar que es

N1(s1) = (1−( j
i ))(1−( n
k ))s1
n + (t´erminos de menor grado),

R(s1) = Rest(N(s1, t) , N ′(s1, t)
),

donde, a su vez,

N(s1, t) = (1−( j
i )) tn + (t´erminos de menor grado en t) ∈ Z[s1][ t ]

N ′(s1, t) = (1−( j
i ))( n
j ) tn-j + (t´erminos de menor grado en t) ∈ Z[s1][ t ].

Adem´as del discriminante ∆(n, I ), generador del ideal principal 〈N1(s1), R(s1)
〉 ∩ Z, nos

interesar´a considerar el valor
δ (n, I ) = Ress1(R(s1), N1(s1)
).

Observaci´on 5.6.9. Las desigualdades ∆(n, I ) ̸= 0 y δ (n, I ) ̸= 0 son dos caracterizaciones

independientes de la inexistencia de {i, j , k}-contraejemplos al problema de Casas-Alvero

de grado n. As´ı lo establecen las proposiciones 5.6.2 y 5.5.4 (pues δ (n, I ) ̸= 0 equivale a

que N1(s1) = R(s1) = 0 carezca de soluciones en C), y el hecho de que Sn,I ( C) no admita

puntos que queden fuera de Un,I ( C), ya que corresponder´ıan a contraejemplos con solo

dos t´erminos adicionales al l´ıder.

En particular, ∆(n, I ) ser´a nulo si y solo si lo es δ (n, I ). A diferencia de lo que ocurre

con ∆(n, I ), para calcular δ (n, I ) disponemos de una f´ormula expl´ıcita.

Dados cualesquiera dos polinomios f (s), g(s) ∈ Z[s] de grado positivo, los enteros ∆f,g
y δf,g deﬁnidos por 〈∆f,g〉 = 〈f (s), g(s)
〉 ∩ Z y δf,g = Res(f (s), g(s)
) no son necesariamente

iguales, aunque sabemos por 1.3.1 que ∆f,g siempre divide a δf,g; as´ı por ejemplo, siendo

f (s) = 3s + 2, g(s) = 3s + 4 se tiene ∆f,g = 2 ya que 2 = −f (s) + g(s), mientras que es δf,g = 6.

En general se veriﬁca, adem´as, el resultado siguiente:

Lema 5.6.10. Sea µ el m´aximo com´un divisor de los coeﬁcientes l´ıderes de f (s) y de g(s),

y sea p un primo arbitrario. Se cumple la doble implicaci´on

p | δf,g ⇐⇒ p | µ o bien p | ∆f,g

Demostraci´on. Por simplicidad se omiten los sub´ındices f, g en la escritura de esta prueba.

La implicaci´on hacia la izquierda es obvia; veamos su rec´ıproca. Por la deﬁnici´on de ∆

118 Cap´ıtulo 5. Esquemas alternativos

existen h(s), q(s) ∈ Z[s] tales que ∆ = f (s) h(s) + g(s) q(s). Sean n, m, u, v los respectivos

grados de f , g, h y q, y sean a0 y b0 los coeﬁcientes l´ıderes de f y de g, de modo que

sobre el cuerpo adecuado se puede escribir f (s) = a0 ∏ n
i=1(s −αi) y g(s) = b0 ∏ m
i=1(s − βi).

Empleando esta factorizaci´on, y gracias al comportamiento multiplicativo de la resultante,

se obtiene

Res(f (s) · h(s), g(s)
) = Res(∆−g(s) q(s), g(s)
) = bn+u
0
 m∏

i=1 Res(∆ −g(s) q(s), s − βi) =

= bn+u
0
 m∏

i = 1
 [
∆ −g(βi) q(βi)
]
;

esto es, en deﬁnitiva,

δ · Res(h(s), g(s)
) = bn + u
0 ∆m y, de forma sim´etrica,

δ · Res(q(s, f (s)
) = am + v
0 ∆n. (5.24)

Sea p un divisor primo de δ; si p no divide a µ entonces no divide a a0, o bien no divide a

b0. De (5.24) se deduce que entonces p divide a ∆, como se quer´ıa probar. □

Teorema 5.6.11. Sea I = {i, j , k}; sean ∆(n, I ) y δ (n, I ) seg´un deﬁniciones previas. Entonces,

para todo primo p se veriﬁca

δ (n, I ) ̸≡ 0 mod p ⇐⇒ ∆(n, I ) ̸≡ 0 mod p y µ ̸≡ 0 mod p,

siendo µ el m´aximo com´un divisor de los coeﬁcientes de los t´erminos l´ıder de R(s1) y N1(s1).

Demostraci´on. Es aplicaci´on directa del lema anterior a los polinomios R(s1) y N1(s1). □

Siguiendo la misma t´actica que en 2.3.4, para probar que δ (n, I ) es distinto de cero

bastar´ıa demostrar la existencia de un n´umero primo p tal que δ (n, I ) ̸≡ 0 mod p, y lo

mismo puede decirse respecto de ∆(n, I ). El teorema anterior garantiza que el conjunto

de primos ´utiles a dicho ﬁn es el mismo en ambos casos, excepci´on hecha de los divisores

primos de µ (quienes, por otra parte, no est´an incontrolados pues son, en particular,

divisores de (
1 −( j
i )) · (
1 −( n
k ))
, coeﬁciente l´ıder de N1(s1)).

Observaci´on 5.6.12. El teorema anterior permite encontrar de modo efectivo los primos

ineﬁcaces de nivel 3 para valores asequibles de h. En efecto, con la ´unica posible excepci´on

de aquellos primos que dividan a 1 −( j
i ) (los dem´as divisores de µ, por serlo de 1 −( n
k )

se encontrar´ıan en el nivel 1), son primos ineﬁcaces de nivel m´aximo —si no lo fueran ya

5.6 Discriminantes 119

de nivel uno o dos— justamente los divisores primos de ∆(n, I ), o equivalentemente, de
δ (n, I ), el cual es computable a trav´es de la f´ormula de la resultante. Con este criterio, y

si se requiere, las tablas que siguen a la proposici´on 4.4.6 pueden completarse con el nivel

3 para los primeros valores de h.

Ejemplo. Tomamos n = 5, I = {1, 2, 3}. Entonces se tiene

∆(5; {3}
) = ( 5
3 ) −1 = 3
2 , por la deﬁnici´on 5.6.5,

∆(5; {2, 3}
) = 22 · 3
2 · 11 · 3541, por el teorema 5.6.8, y

δ(5; {1, 2, 3}
) = 2
24 · 3
6 · 7
3 · 131 · 193 · 599
2 · 8009, resultante de R y N1.

Los polinomios R y N1 en cuesti´on son

R(s1) = 64 · (1 −5s
2
1) · (5s
2
1 −3) · (2450s
4
1 −1445s
2
1 + 193)

N1(s1) = −s1 (s1 −1)
2 · (9s
2
1 −2s1 −3),

y, por tanto, el valor de µ es 1. Del teorema anterior se deduce, pues, que los primos que

dividen al discriminante ∆(5; {1, 2, 3}
) son exactamente los divisores de δ(5; {1, 2, 3}), es

decir, 2, 3, 7, 131, 193, 599, 8009. Se trata de siete de los nueve primos ineﬁcaces para n = 5.

Los otros dos primos ineﬁcaces con n = 5, que son 11 y 3541, aparecen en ∆(5; {2, 3}).

En el ejemplo anterior hemos podido observar la coincidencia entre el conjunto de

los primos ineﬁcaces con 5 y el conjunto de los primos que dividen al superdiscriminante

D5 = ∆(5; {3}) · ∆(5; {2, 3}
) · ∆(5; {1, 2, 3}
), comportamiento que tambi´en se produce con

n = 3 y n = 4. Un resultado general, en este sentido, es el que garantiza una de las dos

inclusiones. Est´a dado con el siguiente teorema, con el cual concluye esta Memoria.

Teorema 5.6.13. Sea n ≥ 3 un n´umero entero, y sea p ≥ n un n´umero primo.

(a) Si p no divide a Dn, entonces p es eﬁcaz para n, y la conjetura de Casas-Alvero es

cierta para los grados np r, con r ≥ 0.

(b) Si p no divide a ̃Dn, entonces la conjetura de Casas-Alvero es cierta en grado n.

Demostraci´on. (a): Como p no divide a Dn, tampoco divide al discriminante ∆(n, Ii ) para

ning´un i = 1, . . . , n −2, lo cual implica que todos los conjuntos Un,Ii( Fp ) son igual al vac´ıo

(ver observaci´on 5.6.4, y reparar en que, siendo 1 −( j
i ) = i < p, no hay obstrucci´on a la

aplicaci´on de este criterio).

120 Cap´ıtulo 5. Esquemas alternativos

Queda as´ı probado que es Sn,J ( Fp ) =
 n-2⋃

i = 1 Un,Ii( Fp ) = ̸O y, por tanto, que p es eﬁcaz

para n; basta ahora aplicar el principio de expansi´on enunciado en 4.3.

(b): El valor de ̃Dn que estemos considerando en determinado momento es el producto,

justamente, de aquellos factores ∆(n, Ii ) presentes en Dn para los que no se hubiera estable-

cido previamente la igualdad Un,Ii( C) = ̸O, esto es, para los que no se hubiera demostrado

que el correspondiente discriminante ∆(n, Ii ) sea un entero distinto de cero. Pero al saber

que el primo p no divide a ninguno de tales discriminantes, concluimos que, efectivamente,

tambi´en para todos ellos es ∆(n, Ii ) ̸= 0, de donde resulta Sn,J ( C) =
 n-2⋃

i = 1 Un,Ii( C) = ̸O ; esto

prueba Casas-Alvero para el grado n. Obs´ervese que, sin embargo, pudiera ocurrir que

alguno de los discriminantes ∆(n, Ii ) que estaban ausentes del producto ̃Dn fuera m´ultiplo

de p; no podemos por tanto, con estas hip´otesis, garantizar que p sea un primo eﬁcaz para

el grado n. □

Bibliograf´ıa

[A-M] Atiyah, M.F.; Macdonald, I.G.: Introducci´on al ´Algebra Conmutativa. Re-

vert´e (1969)

[BLSW] Bothmer, H.-C.; Labs, O.; Schicho, J.; Woestijne, C.: The Casas-Alvero

Conjecture for inﬁnitely many degrees. J. Algebra 366, 224 - 230 (2007).

[Cas] Casas-Alvero, E.: Higher order polars. J. of Algebra 240, 326-377 (2001).

[C-S] Chellali, M.; Salinier, A.: La conjecture de Casas-Alvero pour degree 5e.

Preprint 2012.

[CLO-1] Castryck, W.; Lauterveer, R.; Ouna¨ıes, M: Constraints on counterexamples

to the Casas-Alvero conjecture, and veriﬁcation on degree 12. ArXiv 1208. 5404v1

[Math.AG]. August 27, 2012.

[CLO-2] Castryck, W.; Lauterveer, R.; Ouna¨ıes, M: CA bad primes for degree 7.

Avalaible at https://perswww.kuleuven.be./˜u0040935/badprimes7.txt

[CLS] Cox, D.; Little, J.; O’Shea, D.: Ideals, Varieties and Algorithms. Springer-

Verlag (1992)

[C-S] Chellali, M.; Salinier, A.: La conjecture de Casas-Alvero pour degree 5e.

Preprint 2012.

[D-G] D´ıaz-Toca, G.; Gonz´alez-Vega, L.: On analyzing a conjecture about uni-

variable polynomials and their roots by using Maple. Proceedings on the Maple

Conference 2006. Waterloo (Canada), July 23-26 (2006).

[D-J] Draisma, J.; Jong, J.P.: On the Casas-Alvero conjecture. Fea-

ture. EMS Newsletter 80, 29 - 33, June 2011. Erratum avalaible at

http://www.win.tue.nl/˜jdraisma/

122 BIBLIOGRAF´IA

[Fru1] Frutos-Mar´ın, R. : Sobre polinomios que comparten una ra´ız con cada una de

sus derivadas. Trabajo presentado para obtener el Diploma de Estudios Avanzados

del programa de doctorado en Matem´aticas. Universidad de Valladolid (2005)

[Fru2] Frutos-Mar´ın, R. : Polynomials sharing roots with its derivatives. Conferen-

cias en “Thematic Seminar on Singularities, Algebraic Geometry, Computing and

Information”. Segovia 15/10/2009, y en “Seminario de Geometr´ıa T´orica, VI”,

Jarandilla de la Vera, 14/11/2009.

[Jon] Jong, J.P. : Het Casas-Alvero conjecture. 19 - 04 - 2010.

[Lan] Lang, S.: Algebra. Graduate texts in Mathematics. Springer (2002).

[L-O] Lauterveer, R.; Ouna¨ıes, M : Constraints on hypothetical counterexamples to

the Casas-Alvero conjecture. ArXiv 1204.0450 [mathCV] (2012).

[Sam] Samuel, P.: Th´eorie Alg´ebrique des Nombres. Herrmann, Paris (1997).

[Ser] Serre, J.P.: Cours d’Arithmetique. Presses Universitaires de France, Paris

(1995).

[Ver] Verhoeck, H.: Some remarks about a polynomial conjecture of Casas-Alvero.

Seminaire Bourbakettes, Paris (2009).

[Woe] Woestijne, C. Czech and Slovak International Conference on

Number Theory. Slar´a Lesn´a, September 6, 2011. Avalaible at

http://www.opt.math.tugraz.at/˜cvdwoest/maths/talk-lesna.pdf

´Indice alfab´etico

∆(n, I ) , discriminante, 113

Ip , 46

Rn , esquema de ra´ıces, 91

Sn,I , esquema sint´etico, 107

Un,I , carta local de Sn,I , 110

Xn , esquema de coef. ordinarios, 94

Yn , esquema de coef. presentados, 39

Zn,I , subesquema de Yn , 40

R ′
n , supraesquema de Rn , 99

X ′
n , supraesquema de Xn , 99

Y ′
n , supraesquema de Yn , 67

algoritmo de Buchberger, 11

base de Gr¨obner, 11, 30

derivada

de Hasse, Pn
< i >(X) , 4

neta, Pn
[ i ](X) , 4

discriminante, 113

esquema

de coeﬁcientes ordinarios, 94

de coeﬁcientes presentados, 39

de ra´ıces, 91

proyectivo, 33

sint´etico, 107

hip´otesis

desplazamiento de, 62

propagaci´on de, 60
 I -contraejemplo, 16

I -polinomio, 16

I -problema, 17

nivel de ineﬁcacia, 80

par eﬁcaz, 76

b´asico, 76

polinomio presentado, 45

presentaci´on bin´omica, 3

primo

dominante de n, 77

eﬁcaz con n, 76

ineﬁcaz de nivel k, 80

principio de expansi´on, 76

problema parcial, v´ease I -problema

regla de la cadena para la derivada neta

en caracter´ıstica p, 69

resoluci´on

por condensaci´on, 72

por elevaci´on, 49

por interpretaci´on, 45

resultante, 5

supraesquema

de coef. ordinarios, 99

de coef. presentados, 67

de ra´ıces, 99

vicel´ıder, t´ermino, 2

eliminaci´on del, 71
