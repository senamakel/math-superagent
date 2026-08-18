<!-- source: https://www.imo.universite-paris-saclay.fr/~jean.ecalle/ecadulac.html | converted from HTML -->

ecadulqc

# Dulac: resummation-theoretic proof.

### Dulac: constructive proof.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

**
- Avant-propos. **(janvier 1991).

Le pr�sent ouvrage, qui dans sa conception originelle devait se limiter � la preuve de la "conjecture de Dulac'' (finitude des cycles-limite pour un champ de vecteurs polynomial sur [image: \mathbb{R}^2]), a chang� de nature en cours de r�daction et s'est mu� en quelque chose de nettement plus ample. Sous sa forme actuelle, le livre illustre plusieurs techniques-clef de resommation. Surtout, il introduit deux nouvelles classes de fonctions: les *fonctions analysables *et les *fonctions coh�sives *, qui semblent promises � de nombreuses applications. Quant � la preuve proprement dite de la conjecture de Dulac, elle est d�lib�r�ment trait�e comme un *exercice de resommation *et n'occupe plus que deux chapitres sur un total de dix. Les deux chapitres en question sont particuli�rement longs, mais leur longueur tient pour une part aux �-cot�s et aux compl�ments qu'ils comportent.

Les *fonctions analysables *(r�elles) sont grosso modo la cloture naturelle de l'alg�bre des germes (en [image: +\infty], par commodit� technique) de *fonctions analytiques *(r�elles) relativement aux op�rations [image: \{ +, \times, \partial, \circ  \}] et � *leurs inverses *( [image: partial] d�signe la d�rivation et [image: \circ] la composition). Les fonctions analysables [image: varphi] ont la distinction d' etre enti�rement formalisables, c'est-�-dire r�ductibles � des *transs�ries formelles *[image: \widetilde{\varphi}], qui se pr�sentent comme des sommes bien ordonn�es de *transmonomes *, qui sont eux-memes des �chafaudages irr�ductibles de coefficients r�els et de symboles [image: \{ +, \times, \partial, \circ, \exp, \log \}]. La trig�bre des fonctions analysables est meme, en un certain sens, la plus grande famille de germes qui soient totalement formalisables et donc totalement "transparents''. Toutefois, les transs�ries [image: \widetilde{\varphi}] qui leur correspondent sont g�n�riquement divergentes, si bien que la reconstitution de l'objet g�om�trique [image: \varphi(z)] � partir de l'objet formel [image: \widetilde{\varphi}(z)] implique un d�licat processus d'*acc�l�ro-sommation *, qui consiste � passer par un nombre fini de "mod�les'' interm�diaires [image: \widehat{\varphi}_i(\zeta_i)] reli�s les uns aux autres par des *op�rateurs d'acc�l�ration *, transmut�s par Borel-Laplace des changements de variable [image: \widetilde{\varphi}_i(z_i)  \mapsto   \widetilde{\varphi}_{i+1}(z_{i+1}) := \widetilde{\varphi}_i \circ {F}(z_{i+1})]. Notons que Dubois Reymond et surtout Hardy semblent avoir pressenti l'existence d'une classe de fonctions analogue � celle des fonctions analysables, de taille et de stabilit� maximales, mais que l'absence d'une th�orie sommatoire ad�quate les a empech�s d'aller jusqu'au bout de leur intuition.

Selon la nature de l'acc�l�ration ("faible" ou non) reliant les deux mod�les cons�cutifs [image: \widehat{\varphi}_i(\zeta_i)] et [image: \widehat{\varphi}_{i+1}(\zeta_{i+1})],l'acc�l�r�e [image: \widehat{\varphi}_{i+1}(\zeta_{i+1})] se pr�sente comme un germe de fonction *coh�sive *ou *analytique *, poss�dant toujours un d�veloppement unique (g�n�ralement ramifi�) au-dessus de [image: \mathbb{R}^{+}] La classe des fonctions *coh�sives *englobe les plus "r�guli�res" des classes quasianalytiques de Carleman, mais elle poss�de toutes les propri�t�s de r�gularit� qui faisaient d�faut � ces derni�res. R�trospectivement, ces deux notions d'*analysabilt� *et *coh�sivit� *m'apparaissent comme les id�es-force du livre. Leur imbrication est �troite et n'a rien de fortuit. C'est pr�cis�ment la coh�sivit� des acc�l�r�es qui permet de les prolonger d'une facon unique. Mais il y a plus : non seulement les acc�l�r�es "faibles" sont coh�sives mais, comme on le verra � la fin du livre, toute fonction coh�sive est une acc�l�r�e faible.

Venons-en maintenant � la conjecture de Dulac. Cette conjecture, que Dulac avait d'ailleurs pr�sent�e comme un th�or�me, mais en l'�tayant par des arguments qui n'avaient que l'apparence d'une d�monstration, affirme qu'un champ de vecteurs *X*sur [image: \mathbb{R}^2] � coefficients polynomiaux poss�de au plus un nombre fini de cycles-limite, i.e. de trajectoires analytiques closes et isol�es. Il suffit de montrer que ces cycles-limite ne peuvent pas s'accumuler et, comme l'accumulation ne pourrait se produire que sur un polycycle [image: \mathcal{C}] (�ventuellement r�duit � un point ou � un cycle), tout revient � �tudier l'application [image: {F}], dite de (premier) retour, associ�e au polycycle [image: \mathcal{C}], et � montrer la finitude de ses points fixes isol�s, puisque ceux-ci correspondent aux cycles-limite. Il n'est d'ailleurs pas n�cessaire de supposer le champ *X*polynomial : il suffit de le supposer d�fini et analytique au voisinage de [image: \mathcal{C}].

La m�thode suivie consiste � d�composer l'application de retour [image: {F}= {G}_r \circ \dots {G}_2 \circ {G}_1] en un produit de facteurs [image: {G}_i], qui sont les applications de passage associ�es � chacun des sommets du polycycle, puis � envisager la contrepartie formelle [image: \widetilde{F}=  \widetilde{G}_r \circ \dots  \widetilde{G}_2 \circ  \widetilde{G}_1] de ces applications. Selon les sommets, les facteurs [image: \widetilde{G}_i] se pr�sentent soit comme des s�ries formelles, soit comme des transs�riesw assez �l�mentaires. La compos�e [image: \widetilde{F}], au contraire, revet la forme d'une transs�rie g�n�rale, avec des empilements d'exponentielles-logarithmes de complexit� potentiellement maximale. Toutefois, cette transs�rie [image: \widetilde{F}] est toujours *acc�l�ro-sommable *. Sa somme [image: {F}] est donc une fonction analysable qui, si elle diff�re de l'application identique, ne peut poss�der que des points fixes isol�s.

La d�monstration est r�partie sur deux chapitres. Le chapitre 3, qui est une �tude locale, d�crit minutieusement les facteurs [image: \widetilde{G}_i] et [image: {G}_i] associ�s aux diff�rents sommets. Le chapitre 4, qui est une �tude globale, int�gre toute cette information pour aboutir � une description exhaustive de l'application de retour [image: {F}] et du passage de [image: \widetilde{F}] � [image: {F}]. Ainsi qu'on l'a signal�, ces deux chapitres se veulent une d�fense et illustration de la *th�orie de la resommation *. Ils mettent en oeuvre une bonne dizaine de m�thodes, d'outils et de concepts nouveaux : *r�surgence, d�riv�es �trang�res, acc�l�rations, m�dianisation, compensateurs, �manation, transmonomes et transs�ries, analysabilit�, coh�sivit�, singularit�s coh�sives, quartage, douceur *etc ..., qui toutes trouvent � s'appliquer � ce probl�me particulier, mais dont la port�e est beaucoup plus g�n�rale. Ajoutons que la pr�sente �tude a �t� �crite sans aucun souci du 16�me probl�me de Hilbert, meme si celui-ci parait etre l'objectif, pour ne pas dire l'obsession, de la plupart des math�maticiens qui s'int�ressent au probl�me de Dulac.

Tachons maintenant de r�pondre � deux question qu'on peut l�gitimement se poser concernant la preuve de la conjecture de Dulac pr�sent�e dans ce livre. Cette preuve est-elle la seule possible ? Et quelle est sa longueur v�ritable ? La longueur d'abord. Si l'on admet (c'est-�-dire si l'on consid�re comme *ext�rieurs � la preuve *) les �l�ments de la th�orie des fonctions analysables et en particulier la stabilit� de ces fonctions par composition, tout se ram�ne � d�montrer l'analysabilit� des facteurs [image: {G}_i] pris isol�ment, ce qui ne demande pas plus d'une dizaine de pages. Si on contraire, comme nous l'avons fait dans ce livre, on tient � construire la notion de fonction analysable � partir de z�ro et � �tablir les principaux r�sultats de stabilit�, on a �videmment une d�monstration beaucoup plus longue (peut-etre cent pages incompressibles) mais riche en retomb�es puisqu'on �difie, � son propos, une th�orie susceptible de tr�s nombreuses applications (notamment en th�orie des �quations diff�rentielles ou fonctionnelles). Voyons maintenant la question de l'unicit� de la preuve. Les fonctions analysables vraiment g�n�rales ne peuvent pas s'�tudier autrement que par les m�thodes de ce livre. Mais l'application de retour [image: {F}] est une fonction analysable tr�s particuli�re, puisqu'elles se d�compose en facteurs [image: {G}_i] eux-memes tr�s �l�mentaires, car ne poss�dant chacun qu'un seul "temps critique'' et par suite sommables par Borel-Laplace, sans recours � l'acc�l�ration. On peut dire sans exag�rer que [image: {F}] est aux "vraies'' fonctions analysables ce que les superpositions fines [image: \sum \varphi_i(\alpha_i\,z_1 +\beta_i\,z_2)] sont aux "vraies" fonctions analytiques de deux variables. Ce caract�re tr�s sp�cial et passablement �l�mentaire de [image: {F}] fait qu'il existe d'autres moyens d'en aborder l'�tude, notamment la m�thode, g�om�tique et non-constructive, de Yu. S. Ilyashenko � paraitre dans [Il.2] et bas�e sur une extension du principe de Lindel f. Il y a aussi les m�thodes esquiss�es au �4.6 de ce livre et bas�es sur des propri�t�s d'ind�pendance (ce sont les "lemmes d'immiscibilit�", dont l'unreste encore � prouver --- mais ceux qui sont acquis suffisent d�j� simplifier grandement la preuve de la non-oscillation de [image: {F}]). Il y a donc plusieurs mani�res, authentiquement diff�rentes, de prouver la conjecture de Dulac ou, si l'on pr�f�re, la non-oscillation de [image: {F}]. Il me semble toutefois que la m�thode expos�e dans ce livre soit la seule *qui aille au fond de la question, en formalisant totalement l'objet g�om�trique [image: {F}]. *Plus p�cis�ment, je suis convaincu de trois choses:

1) Le seul *objet formel � coefficients r�els *qu'on puisse sens�ment associer � [image: {F}] et qui en rec�le toute l'information, est la *transs�rie m�diane *[image: \widetilde{F}] construite dans ce livre.

2) La seule m�thode explicite et constructive permettant de reconstituer [image: {F}] � partir de [image: \widetilde{F}], est la m�thode d'acc�l�ro-sommation m�diane, expos�e dans ce livre.

3) Seule la formalisation totale de [image: {F}], c'est-�-dire sa r�duction � l'objet formel [image: \widetilde{F}], peut offrir une compr�hension compl�te de [image: {F}] et de tout ce qu'on peut fabriquer � partir de [image: {F}] (par exemple, la non-oscillation des d�riv�es succesives de [image: {F}]).

La seconde moiti� du livre (chapitres 5 � 10) comprend des compl�ments qui �clairent et prolongent les m�thodes mises en oeuvre pour la r�solution du probl�me de Dulac. Le chapitre 5 d�gage deux transformations purement formelles sous-jacentes aux transformations fonctionnelles de Borel et de Laplace ("quartage" et "formules cryptolin�aires"). Le chapitre 6 �tablit l'identit� entre les *fonctions coh�sives *et les *acc�l�r�es faibles*, puis en tire les cons�quences pratiques. Les chapitres 7,8,9 montrent que les fonctions analysables marquent en quelque sorte l' *l'ultime limite *de la *formalisabilit� des germes *, et qu'au-del� il n'y a plus rien qui leur ressemble. En effet, du fait de l' *asymptotique universelle *des germes *lents *ou *rapides *et du th�or�me d'*indiscernabilit� *, il n'existe plus, au-del� de l'�chelle des exponentielles et des logarithmes it�r�s, de fonctions-rep�re authentiquement canonique et susceptibles de servir de "base" � une tentative de formalisation des germes. Toutefois, ainsi qu'il arrive souvent en math�matiques, ce r�sultat "n�gatif" poss�de une contrepartie "positive" et fort inattendue, � savoir le caract�re essentiellement "discret" et "fractal" de l'*�chelle naturelle de croissance *. Tout ceci d�bouche sur une notion tr�s naturelle d'*it�ration transfinie *et sur le *"Grand Cantor" *, obtenu par �limination des "zones de croissances" qui regroupes tous les "germes indiscernables".

---

---

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

**
- Update: well-behaved averages. **
xxx

---

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

---

---

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

**
- Update: J. van der Hoeven's and V. Bagayoko's work on hyperseries. **
xxx

---

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

---

---

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

**
- The non-accumulation theorem thirty years on. **
xxx

---

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

---

[Source][1] par Jean Ecalle  | [WIMS][2] @ [wims.auto.u-psud.fr][3] |

Derni�re modif. 20041112  |


## Links

[1]: http://wims.auto.u-psud.fr/wims/wims.cgi?session=JCD2D6BB26.4&amp;+lang=fr&amp;+module=adm/doc.fr&amp;+cmd=reply&amp;+job=source
[2]: http://wims.auto.u-psud.fr/wims/wims.cgi?session=JCD2D6BB26.4&amp;+lang=fr&amp;+module=home
[3]: http://wims.auto.u-psud.fr/
