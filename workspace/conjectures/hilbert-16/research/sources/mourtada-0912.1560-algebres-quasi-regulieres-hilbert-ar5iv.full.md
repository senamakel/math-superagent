<!-- source: https://ar5iv.labs.arxiv.org/html/0912.1560 | converted from HTML -->

[0912.1560] Université de Bourgogne, I.M.B. U.M.R. 5584 du C.N.R.S., U.F.R. des Sciences et Techniques 9, avenue Alain Savary, B.P. 47 870, 21078 Dijon Cedex. E-mail: mourtada@u-bourgogne.fr

## Université de Bourgogne, I.M.B.
U.M.R. 5584 du C.N.R.S., U.F.R. des Sciences et Techniques
9, avenue Alain Savary, B.P. 47 870, 21078 Dijon Cedex.
E-mail: mourtada@u-bourgogne.fr

Mots-clés: 16ème problème d’Hilbert, cycle limite, cyclicité, polycycle, singularité de champ de vecteurs, application de Dulac, application de retour de Poincaré, structure asymptotique quasi-analytique, action différentielle, idéal différentiel, faisceau différentiel, projection intégrale, multiplicité algébrique.

Classification AMS: 34C07 (Primary) 34C08, 37G15 (Secondary).

Abstract. We study the action of irreducible derivations χ \chi on some Hilbert’s quasi-regular algebras Q ​ R ​ H QR{H} of germs at 0, of real analytic functions on ( U, 0) (U,0), where U U is some semi-algebraic open set. We show that these algebras are χ \chi -finite or locally χ \chi -finite: the degree of the projection π χ \pi_{\chi} restricted to fibers of Q ​ R ​ H QR{H}, is finite and the differential ideals are noetherian or locally noetherian. Moreover, these algebras satisfy to the double inclusion: for every germ f f, there exist an algebraic multiplicity m ​ a χ ​ ( f) ma_{\chi}(f) such that, modulo some algebraic factor which vanishs only on the germ of the boundary ( ∂ U, 0) (\partial U,0), and depends only on m ​ a ma, the differential ideal of f f coincides with the saturation of his transverse ideal. In last, we give an application to the generalised Hilbert’s 16th problem about limit cycles: there is no accumulation of limit cycles on hyperbolic polycycles in compact analytic families of vector fields on the sphere S 2 S^{2}. This is a highly non trivial result, it includes the case of a polycycle that is an accumulation of cycles.

Introduction

Le problème de Dulac ([E], [I]), dit que tout champ de vecteurs analytique sur la sphère réelle S 2 S^{2} a un nombre fini de cycles limites, autrement dit il n’y a pas accumulation de cycles limites sur les polycycles. Le 16ème problème d’Hilbert algébrique ([Hi]), demande d’établir une majoration de ce nombre en fonction du degré pour les champs de vecteurs algébriques du plan réel. Plus généralement ([Ro1]), il s’agit de montrer qu’il n’y a pas accumulation de cycles limites sur les ensembles limites périodiques, dans les familles compactes de champs de vecteurs analytiques sur S 2 S^{2}: c’est le problème d’Hilbert analytique. Soit Γ k \Gamma_{k} un polycycle hyperbolique et monodromique réel, à k k singularités, tangent à un champ de vecteurs analytique réel X 0 X_{0} défini sur un voisinage U 0 U_{0} de Γ k \Gamma_{k}. On suppose, uniquement pour simplifier la présentation, que le rapport des valeurs propres en chaque singularité de Γ k \Gamma_{k} est égal à − 1 -1. Dans la section IVC, on montre le théorème fondamental

###### Théorème 0

Soit X ν X_{\nu} un déploiement analytique de X 0 X_{0} à q q paramètres. Alors il existe des entiers N N et L L et des voisinages Γ k ⊂ U ⊂ U 0 \Gamma_{k}\subset U\subset U_{0} et V ∈ ( ℝ q, 0) V\in(\mathbb{R}^{q},0) tels que

Plusieurs travaux, sur des cas génériques, ont été établis par moi même ([M]), ou par Il’yashenko, Yakovenko et Kaloshin ([I-Y2], [Ka]), où les singularités semi-hyperboliques sont aussi considérées. La démarche adoptée dans ces travaux consiste, d’abord en une préparation générique des singularités (dans une classe de différentiabilité suffisament grande), suivie d’une application de la procédure d’élimi-

nation de Khovanski ([K1]). Dans [M], les conditions génériques sont algébriquement controlées tout au long de cette procédure. Cependant, dans [I-Y2], il semble très difficile de relier les conditions génériques de cette procédure à celles, géométriques provenant du polycycle.

Dans le cas général du théorème 0, et en vue de couvrir les cas les plus dégénérés, l’approche mise en oeuvre peut se résumer ainsi: on prépare localement (dans une subdivision finie), l’application de retour p ν p_{\nu} du polycycle perturbé. Dans cette préparation, les propriétés de finitude de p ν p_{\nu} (le nombre de ses points fixes et leur multiplicité), sont données par celles d’un certain jet fini qui est un fewnomial [K1]. La théorie de Khovanski s’applique aisément à ces jets.

Voici les idées de base de cette approche: soient ( x, α) (x,\alpha) des coordonnées analytiques locales sur ( ( ℝ + ⁣ ∗) k × ℝ q, 0) ((\mathbb{R}^{+*})^{k}\times\mathbb{R}^{q},0), et soit B k = { ∏ j = 1 k x j = 0 } B_{k}=\{\prod_{j=1}^{k}x_{j}=0\}. Soit B ⊃ ℝ ​ { x, α } {B}\supset\mathbb{R}\{x,\alpha\} un anneau local de germes de fonctions analytiques sur ( ( ℝ + ⁣ ∗) k × ℝ q, 0) ((\mathbb{R}^{+*})^{k}\times\mathbb{R}^{q},0), continues sur ( B k, 0) (B_{k},0). Soit χ \chi un germe en 0 de champs de vecteurs à composantes dans B {B}. On s’intéresse aux dérivations qui induisent une action infinitésimale sur B {B}, et plus particulièrement à celles qui satisfont aux conditions suivantes: χ ⁡ ( B) ⊂ B \chi({B})\subset{B}, S ​ i ​ n ​ g ​ ( χ) ⊂ ( B k, 0) Sing(\chi)\subset(B_{k},0) et ( B k, 0) (B_{k},0) est invariant par le flot φ χ \varphi_{\chi} (cf. partie IB). Le but est d’étudier les propriétés de finitude topologiques et algébriques des éléments de l’algèbre B {B} relativement à la distribution induite par la dérivation χ \chi dans ( ( ℝ + ⁣ ∗) k × ℝ q, 0) ((\mathbb{R}^{+*})^{k}\times\mathbb{R}^{q},0).

Les concepts suivants sont développés dans la partie IB. Soit U ∈ ( ( ℝ + ⁣ ∗) k × ℝ q, 0) U\in((\mathbb{R}^{+*})^{k}\times\mathbb{R}^{q},0) un ouvert sur lequel est réalisée la dérivation χ \chi. Soit φ χ, U \varphi_{\chi,U} le flot de χ \chi dans U U, et soit π χ, U: U → U ~ = U / φ χ, U \pi_{\chi,U}:\ U\to\ \widetilde{U}=U/\varphi_{\chi,U} la projection intégrale le long des orbites de χ \chi dans U U. Un germe f ∈ B f\in{B} est dit χ \chi -régulier s’il existe un tel ouvert U U tel que le degré de π χ, U \pi_{\chi,U} restreinte aux fibres de f f soit fini. Il est dit χ \chi -fini s’il est χ \chi -régulier et si son idéal différentiel I χ, f I_{\chi,f} est noethérien dans une extension étoilée de B {B}. Il est dit localement χ \chi -fini s’il est χ \chi -régulier et s’il existe une subdivision finie ( U i) (U_{i}) de U U, invariante par χ \chi, telle que chaque idéal restriction I χ, f | U i I_{\chi,f|U_{i}} soit noethérien dans une extension étoilée de l’anneau restriction B | U i {B}_{|U_{i}}. Une sous-algèbre ou une sous-classe de B {B} est dite χ \chi -finie (resp. localement χ \chi -finie) si chacun de ses éléments est χ \chi -fini (resp. localement χ \chi -fini). Un résultat majeur de la partie IB est

###### Lemme de finitude IB1

Soit M {M} l’idéal maximal de B {B} et soit M 0 ⊂ M {M}_{0}\subset{M} un idéal stable par χ \chi. Soit B ′ ⊂ B {B}^{\prime}\subset{B} une sous-algèbre χ \chi -finie et stable par χ \chi. Alors la classe C M 0, B ′ = { f ∈ g + M 0 ​ I χ, g; g ∈ B ′ } {C}_{{M}_{0},{B}^{\prime}}=\{f\in g+{M}_{0}I_{\chi,g};\ g\in{B}^{\prime}\} est χ \chi -finie.

Dans ce cas, on dit que f f est χ \chi -équivalente à g g et plus généralement, on parle d’algèbres ou de classes χ \chi -équivalentes. Ce lemme donne une idée du type de préparation que l’on souhaite établir. Décrivons brièvement les outils pour atteindre cet objectif. Si γ ⊂ U \gamma\subset U est une orbite de χ \chi, le lemme d’isomorphie IB4 dit que les fibres du faisceau différentiel I χ, f ​ [γ] {I}_{\chi,f}[\gamma] sont isomorphes dans les anneaux analytiques locaux ℝ {. } \mathbb{R}\{.\} correspondants. D’où l’existence d’un unique idéal transverse J χ, f, γ J_{\chi,f,\gamma} dans un anneau analytique ℝ ​ { β } \mathbb{R}\{\beta\} dont les coordonnées β \beta sont des intégrales premières de χ \chi le long de γ \gamma. De plus, le lemme de saturation IB5 permet de reconstruire chaque fibre du faisceau différentiel à partir de cet idéal transverse: pour tout m ∈ γ m\in\gamma, I χ, f ​ ( m) = π χ m ∗ ​ ( J χ, f, γ) I_{\chi,f}(m)=\pi_{\chi_{m}}^{*}(J_{\chi,f,\gamma}). La question naturelle qui se pose alors est: si γ \gamma adhère à 0, quel est le lien entre la fibre différentiel en 0 et le saturé de cet idéal transverse? Il est clair que ce lien est d’autant plus fort que l’orbite γ \gamma est principale dans U U, i.e le saturé de toute transversale analytique à γ \gamma est un voisinage de 0 dans U U. L’idéal I ⁡ ( (,,,)) I((B_{k},0)) est principal de générateur θ = ∏ j = 1 k x j \theta=\prod_{j=1}^{k}x_{j}. Alors, ce lien s’exprime en général par une double inclusion qui relaxe l’égalité le long de γ \gamma, et qui s’inspire du Nullstellensatz d’Hilbert

 | ( θ n) π χ ∗ ( J χ, f, γ) ⊂ I χ, f ⊂ π χ ∗ ( J χ, f, γ) ∗ (\theta^{n})\pi_{\chi}^{*}(J_{\chi,f,\gamma})\subset I_{\chi,f}\subset\pi_{\chi}^{*}(J_{\chi,f,\gamma})* |  |  |

Le plus petit de ces entiers n n est la multiplicité m χ ​ ( f) m_{\chi}(f) de f f relativement à χ \chi. Si l’anneau B {B} possède une structure asymptotique, il se trouve que cette multiplicité est intimement liée à la multiplicité algébrique m ​ a χ ​ ( f) ma_{\chi}(f) qui est l’indice de stationnarité d’une suite croissante d’idéaux transverses, qui converge vers J χ, f, γ J_{\chi,f,\gamma}. Ainsi, en étudiant l’action de χ \chi sur les jets finis de f f, et en utilisant la double inclusion ( ∗) (*), on montre que f f est χ \chi -équivalente à son jet d’ordre m ​ a χ ​ ( f) ma_{\chi}(f) (cf. sections II, III, IV). Le lemme de finitude ci-dessus donnera les propriétés de finitude voulues.

La projection π χ \pi_{\chi} est unidimensionnelle. On peut généraliser cette approche du bord ( B k, 0) (B_{k},0), en considérant des projections p p -dimensionnelles le long, par exemple des feuilles d’un feuilletage de dimension p p.

Le germe de l’application de Dulac, et de ses déploiements, appartiennent à certaines algèbres Q ​ R ​ H 1,. QR{H}^{1,.} décrites dans la partie IA. L’algèbre Q R H k,. ( x,.) ⊂ B QR{H}^{k,.}(x,.)\subset{B} est constituée des germes qui sont quasi-analytiques dans les coordonnées x x

 | Q R H ∩ ( ∩ n ∈ ℕ M x n) = { 0 } QR{H}\cap(\cap_{n\in\mathbb{N}}{M}_{x}^{n})=\{0\} |  |

( M x = ⟨ x 1, …, x k ⟩ ⊂ B {M}_{x}=\langle x_{1},\ldots,x_{k}\rangle\subset{B}); et qui possèdent une structure asymptotique élémentaire dans les coordonnées x x: ces ingrédients sont des fonctions élémentaires d’Ecalle-Khovanski. Soit χ ∈ Ξ ​ H k \chi\in\Xi{H}_{k} une dérivation d’Hilbert réalisée sur un ouvert U k ∈ ( ( ℝ + ⁣ ∗) k × ℝ q, 0) U_{k}\in((\mathbb{R}^{+*})^{k}\times\mathbb{R}^{q},0), de dimension de non trivialité k − 1 k-1 (cf. partie IVA). Elle admet une action sur l’algèbre Q ​ R ​ H k,. QR{H}^{k,.} et elle possède une orbite principale γ \gamma incluse dans U k U_{k}. Dans la partie IVC, on montre le théorème général suivant, dont le théorème 0 est une conséquence immédiate

###### Théorème IVC1

L’algèbre Q ​ R ​ H k,. QR{H}^{k,.} est localement χ \chi -finie et satisfait localement à la double inclusion ( ∗) (*).

La dérivation χ \chi n’est pas réduite. Il existe une désingularisation ( π k, N k) (\pi_{k},{N}_{k}) entièrement décrite pas les algèbres Q ​ R ​ H k,. QR{H}^{k,.} (cf. partie IVA), et dans laquelle les singularités réduites de χ \chi sont de la forme

 | χ ℓ = ρ ​ ∂ ∂ ρ − ∑ j = 1 ℓ s j ​ u j ​ ∂ ∂ u j \chi_{\ell}=\rho\frac{\partial}{\partial\rho}-\sum_{j=1}^{\ell}s_{j}u_{j}\frac{\partial}{\partial u_{j}} |  |

pour ℓ = 0, …, k − 1 \ell=0,\ldots,k-1. Le théorème IVC1 est donc une conséquence de l’étude de l’action des dérivations réduites χ ℓ \chi_{\ell} sur les algèbres Q R H p,. ( ρ, ρ ′,.) QR{H}^{p,.}(\rho,\rho^{\prime},.), avec p ≤ k p\leq k. Or, une dérivation χ ℓ \chi_{\ell}, réalisée sur un ouvert U p U_{p}, admet une orbite principale incluse dans U p U_{p} si et seulement si p = 1 p=1. Dans ce cas, on montre les résultats principaux suivants dans les sections II et III

###### Théorème principal II1

L’algèbre Q R H 1,. ( ρ,.) QR{H}^{1,.}(\rho,.) est χ 0 \chi_{0} -finie et satisfait à la double inclusion.

Ce théorème, de démonstration simple et basique est une introduction aux autres théorèmes. Notons Q ​ R ​ H c ​ v ​ g 1,. QR{H}^{1,.}_{cvg} la restriction d’un anneau analytique ℝ {. } \mathbb{R}\{.\} au graphe des fonctions élémentaires de l’algèbre Q ​ R ​ H 1,. QR{H}^{1,.} correspondante. Sa χ ℓ \chi_{\ell} -finitude est une conséquence simple de résultats de géométrie analytique classique et de la théorie de Khovanski-Tougeron ([K1], [T]).

###### Théorème principal IIIA1

Pour tout ℓ \ell, l’algèbre Q ​ R ​ H c ​ v ​ g 1,. QR{H}^{1,.}_{cvg} satisfait à la double inclusion relativement à χ ℓ \chi_{\ell}.

###### Théorème principal IIIB1

Pour tout ℓ \ell, l’algèbre Q ​ R ​ H 1,. QR{H}^{1,.} est localement χ ℓ \chi_{\ell} -finie et satisfait localement à la double inclusion.

Si p > 1 p>1, la dérivation χ ℓ \chi_{\ell} admet une orbite principale γ p \gamma_{p} incluse dans le bord B p B_{p}: le saturé dans U p U_{p} de toute semi-transversale analytique à γ p \gamma_{p} est un voisinage de 0 dans U p U_{p}. Les fibres différentielles le long de γ p \gamma_{p} ne sont pas forcément isomorphes et il n’existe pas forcément d’idéal transverse. Plus généralement, deux questions se posent concernant les anneaux Q ​ R ​ H p,. QR{H}^{p,.}: sont-ils noethériens? et leurs semi-analytiques sont-ils induits par une structure o o -minimale au dessus de ℝ \mathbb{R}?

La preuve du théorème IVC1 s’appuie sur les trois théorèmes principaux ci-dessus, et sur 6 lemmes de base (cf. partie IB). Soit D ¯ k \overline{{D}}_{k} le diviseur exceptionnel du morphisme ( π k, N k) (\pi_{k},{N}_{k}) de désingularisation de χ \chi (cf. IVA). Soit f ∈ Q ​ R ​ H k,. f\in QR{H}^{k,.} et soient f ~ \widetilde{f} et χ ~ \widetilde{\chi} les relevés de f f et χ \chi par π k \pi_{k}. Il s’agit de montrer que le faisceau I χ ~, f ~ ​ [D ¯ k] {I}_{\widetilde{\chi},\widetilde{f}}[\overline{{D}}_{k}] est localement χ ~ \widetilde{\chi} -fini. La dérivation χ ~ \widetilde{\chi} admet une unique singularité a 0 a_{0} sur D k {D}_{k}. Soit γ 1 ⊂ D k \gamma_{1}\subset{D}_{k} une orbite de χ ~ \widetilde{\chi} et soit a 1 = γ ¯ 1 ∩ ∂ D k a_{1}=\overline{\gamma}_{1}\cap\partial{D}_{k}. Par compacité de D ¯ k \overline{{D}}_{k}, il suffit de montrer que le faisceau I χ ~, f ~ ​ [a 0 ​ γ 1 ​ a 1] {I}_{\widetilde{\chi},\widetilde{f}}[a_{0}\gamma_{1}a_{1}] est localement χ ~ \widetilde{\chi} -fini.

L’orbite γ 0 = π k − 1 ​ ( γ) \gamma_{0}=\pi_{k}^{-1}(\gamma) est principale dans un voisinage U 1, a 0 U_{1,a_{0}} de a 0 a_{0}. Le résultat en a 0 a_{0} est donc une conséquence du théorème principal IIIB1. En tout point a ∈ γ 1 a\in\gamma_{1}, un représentant du germe ( γ 1, a) (\gamma_{1},a) est principal dans un voisinage U 1, a U_{1,a} de a a; cependant il est inclus dans le bord de U 1, a U_{1,a}. Grâce au lemme de cohérence IB3, les résultats du théorème principal IIIB1 en a 0 a_{0} se germifient en tout point a ∈ γ 1 a\in\gamma_{1} suffisament proche de a 0 a_{0}: le germe en a a de f ~ \widetilde{f} est χ ~ \widetilde{\chi} -équivalent à un élément g a g_{a} d’une algèbre convergente Q ​ R ​ H c ​ v ​ g 1,. QR{H}_{cvg}^{1,.}, qui elle, satisfait au théorème principal IIIA1. Or, comme f ~ \widetilde{f}, ce germe se prolonge au dessus de γ 1 \gamma_{1} en une fonction g g dont tous les germes appartiennent à une algèbre convergente. Le lemme d’isomorphie s’applique aux faisceaux de cette algèbre le long d’orbites incluses dans le bord. Un recollement des idéaux de g g et de f ~ \widetilde{f} donne le résultat au dessus de γ 1 \gamma_{1}. En a 1 a_{1}, on utilise un argument de récurrence sur la dimension de non trivialité de la dérivation d’Hilbert (cf. lemmes de récurrence, parties IVB et IVC). Sa preuve est elle même construite autour des 6 lemmes de base et des 3 théorèmes principaux

L’application de Dulac de chaque singularité de X ν X_{\nu} est induite par un élément d’une algèbre Q ​ R ​ H 1,. QR{H}^{1,.} (cf. appendice VA). Les cycles limites de X ν X_{\nu} correspondent aux intesections isolées des orbites d’une dérivation d’Hilbert χ ∈ Ξ ​ H k \chi\in\Xi{H}_{k} et des fibres d’un germe f ∈ Q ​ R ​ H k,. f\in QR{H}^{k,.}. Le théorème 0 est alors une conséquence simple du théorème IVC1: la propriété ( i) (i) est équivalente à la χ \chi -régularité de f f, et la propriété ( i ​ i) (ii) est une conséquence de la noethérianité ou la locale noethérianité de l’idéal différentiel I χ, f I_{\chi,f}. Cette approche algébrique et géomètrique est appliquable à tout ensemble limite périodique. Comme dans le problème de Dulac, la seule difficulté réside dans la complexité des structures asymptotiques des meilleures algèbres et dérivations d’Hilbert correspondantes.

L’article est composé de 4 sections I,…,IV et un appendice V. Chaque section est subdivisée en parties A, B,… et chaque partie est subdivisée en paragraphes 1, 2,…

Remerciements. Je remercie vivement mes collègues A. Jebrane, P. Mardesic, R. Moussu, M. Pelletier, C. Rousseau et D. Schlomiuk, pour leur soutien durant ce pénible travail. Je tiens à remercier particulièrement R. Roussarie, qui a apporté d’énormes améliorations à certains résultats de ce travail.

I. Définitions et éléments de base.

A. Définitions des algèbres.

§1. L’algèbre A p, q {A}^{p,q}.

Soit ( x, α) = ( x 1, ⋯, x p, α 1, ⋯, α q) (x,\alpha)=(x_{1},\cdots,x_{p},\alpha_{1},\cdots,\alpha_{q}) des coordonnées sur ℝ p × ℝ q {{\mathbb{\mathbb{R}}}}^{p}\times{{\mathbb{\mathbb{R}}}}^{q}.

###### Définition IA1

On note A p, q ​ ( x, α) {A}^{p,q}(x,\alpha) (ou simplement A p, q {A}^{p,q}) l’algèbre réelle locale des germes analytiques réels de ( ( ℝ + ⁣ ∗) p, 0) × ( ℝ q, 0) (({{{\mathbb{\mathbb{R}}}}}^{+*})^{p},0)\times({{{\mathbb{\mathbb{R}}}}}^{q},0) qui sont continus sur le germe en 0 du bord B p = { x 1 × ⋯ × x p = 0 } B_{p}=\{x_{1}\times\cdots\times x_{p}=0\}.

Sauf mention contraire, toutes les algèbres de référence considérées dans la suite sont des sous-algèbres locales de A p, q {A}^{p,q} qui contiennent l’algèbre analytique ℝ ​ { x, α } \mathbb{R}\{x,\alpha\}. Ces algèbres A p, q {A}^{p,q} ne sont pas stables par les dérivations les plus élémentaires: f = x ​ sin ⁡ ( 1 / x) ∈ A 1, 0 f=x\sin(1/x)\in{A}^{1,0} mais x ​ ∂ f / ∂ x ∉ A 1, 0 x\partial f/\partial x\not\in{A}^{1,0}. Dans le problème d’Hilbert, ces algèbres serviront uniquement d’espaces d’intégrales premières pour les dérivations considérées (voir sections III et IV).

§2. L’algèbre S ​ B p, q SB^{p,q} des germes sectoriellement bornés.

Soit θ = ( θ 1, ⋯, θ p) ∈] 0, π / 2 [p \theta=(\theta_{1},\cdots,\theta_{p})\in]0,\pi/2[^{p} et S θ S_{\theta} le polysecteur

 | S θ = { w = ( w 1, ⋯, w p) ∈ ( ℂ ∗) p; | arg ( w j) | < θ j } S_{\theta}=\{w=(w_{1},\cdots,w_{p})\in({{{\mathbb{\mathbb{C}}}}}^{*})^{p};\quad|\arg(w_{j})|<\theta_{j}\} |  | 1 |

Soit ( S θ, ∞) (S_{\theta},\infty) le germe de S θ S_{\theta} à l’infini.

Pour simplifier la présentation dans toute la suite, nous noterons souvent pareillement les germes, leurs représentants et les relevés de germes de fonctions dans la carte w = − log ⁡ ( x) w=-\log(x).

###### Définition IA2

Les éléments de l’algèbre S ​ B p, q ​ ( x, α) ⊂ A p, q ​ ( x, α) SB^{p,q}(x,\alpha)\subset{A}^{p,q}(x,\alpha) sont les germes f f qui admettent, pour tout θ ∈] 0, π / 2 [p \theta\in]0,\pi/2[^{p}, un prolongement holomorphe et borné sur ( S θ, ∞) × ( ℂ q, 0) (S_{\theta},\infty)\times({{{\mathbb{\mathbb{C}}}}}^{q},0) dans la carte w = ( w j = − log ⁡ ( x j)) j = 1, ⋯, p w=(w_{j}=-\log(x_{j}))_{j=1,\cdots,p}.

Ces algèbres S ​ B p, q SB^{p,q} sont le lieu naturel où vivent les germes d’applications de Dulac des déploiements holomorphes d’équations différentielles du 1 er 1^{\text{er}} ordre, y compris dans le domaine de Poincaré (voir appendice A). Ce sont les anneaux de références dans le problème d’Hilbert (voir sections II, III et IV). Leur intérêt premier réside dans leur structure holomorphe produit. Notons également S ​ B 0 p, q SB^{p,q}_{0} la sous-algèbre de S ​ B p, q SB^{p,q} des germes qui, pour tout θ \theta, tendent vers 0 quand w → ∞ w\to\infty dans ( S θ, ∞) (S_{\theta},\infty), uniformément en α \alpha. Contrairement à l’algèbre A p, q {A}^{p,q}, les algèbres S ​ B p, q SB^{p,q} et S ​ B 0 p, q SB^{p,q}_{0} sont stables par les dérivations naturelles χ j = x j ∂ / ∂ x j ∼ − ∂ / ∂ w j \chi_{j}=x_{j}\partial/\partial x_{j}\sim-\partial/\partial w_{j} (conséquence immédiate des formules de Cauchy dans les secteurs S θ S_{\theta}). Cependant, elles ne sont pas quasi-analytiques (voir ci-dessous).

§3. Algèbres quasi-analytiques Q ​ A p, q QA^{p,q}.

Soit P + = { w = u + i v ∈ ℂ; u ≥ 0 } P^{+}=\{w=u+iv\in{\mathbb{\mathbb{C}}};\ u\geq 0\}. Soient u 0 ≥ 0 u_{0}\geq 0, C > 0 C>0 et K > 1 K>1. Les domaines de P + P^{+} de type puissance sont les domaines de la forme

 | Ω p ​ u ​ i ​ s ​ ( u 0, C, K) = { w ∈ P +; u > u 0, | v | < C ​ u K } \Omega_{puis}(u_{0},C,K)=\{w\in P^{+};\ u>u_{0},\ |v|<Cu^{K}\} |  |

Les domaines de P + P^{+} de type exponentiel sont les domaines de la forme

 | Ω e ​ x ​ p ​ ( u 0, C, K) = { w ∈ P +; u > u 0, | v | < C ⁡ ( exp ⁡ ( u / K) − 1) } \Omega_{exp}(u_{0},C,K)=\{w\in P^{+};\ u>u_{0},\ |v|<C(\exp(u/K)-1)\} |  |

Ces domaines sont stables par addition (opération qui correspond à une multiplication dans la coordonnée x = − log ⁡ w x=-\log w).

###### Définition IA3

Les domaines standards d’Ecalle-Il’yashenko sont les ouverts Ω \Omega de P + P^{+} qui contiennent un domaine de type puissance. On note E ​ I {{E}}{{I}} l’ensemble de tels domaines.

En particulier les domaines de type puissance et les domaines de type exponentiel, sont des domaines standards. Une intersection finie et une union finie de domaines standards est encore un domaine standard. Soit Ω ∈ E ​ I \Omega\in{E}{I}, si t ∈ ℂ t\in{\mathbb{\mathbb{C}}} est tel que t + Ω t+\Omega soit inclus dans l’intérieur de P + P^{+}, alors t + Ω ∈ E ​ I t+\Omega\in{E}{I}, et si t > 0 t>0, alors t ​ Ω ∈ E ​ I t\Omega\in{E}{I} (la translation w ↦ t + w w\mapsto t+w correspond à une homothétie x ↦ a ​ x x\mapsto ax, et l’homothétie w ↦ t ​ w w\mapsto tw correspond à une ramification x ↦ x s x\mapsto x^{s}).

Les domaines de type puissance et les domaines de type exponeniel sont biholomorphiquement conjugués à un ouvert contenant P + P^{+}, par un difféomorphisme ϕ. \phi_{.} strictement réel et qui est équivalent à l’identité à l’infini

 | ϕ p ​ u ​ i ​ s ​ ( w) = w − 1 C 1 / K ​ cos ⁡ ( π / 2 ​ K) ​ w 1 / K − U 0 \phi_{puis}(w)=w-\frac{1}{C^{1/K}\cos(\pi/2K)}w^{1/K}-U_{0} |  |

 | ϕ e ​ x ​ p ​ ( w) = w − K ​ log ⁡ ( w) − U 0 U 0 > 0 \phi_{exp}(w)=w-K\log(w)-U_{0}\qquad U_{0}>0 |  |

Ecalle [E] et Il’yashenko [I] ont exhibé, pour l’application de Dulac d’un col hyperbolique réel, un type de tels domaines: exponentiel pour le premier (et ceci est optimal pour les cols hyperboliques analytiquement normalisables: voir appendice VA), et polynomial pour le deuxième ( K = 2) (K=2).

L’application de Dulac d’une équation différentielle dans le domaine de Poincaré n’est pas bornée sur un domaine de E ​ I {E}{I} (voir appendice VA). Ceci motive la

###### Définition IA4

L’algèbre Q ​ A p, q ​ ( x, α) ⊂ S ​ B p, q ​ ( x, α) QA^{p,q}(x,\alpha)\subset SB^{p,q}(x,\alpha) est l’ensemble des germes f = ∑ f n ​ α n f=\sum f_{n}\alpha^{n} dont les coefficients f n f_{n} admettent un prolongement holomorphe et borné sur un même domaine Ω ∈ E ​ I p \Omega\in{E}{I}^{p} dans les coordonnées w = ( w j = − log ⁡ ( x j)) j = 1, …, p w=(w_{j}=-\log(x_{j}))_{j=1,\ldots,p}.

Ces algèbres sont quasi-analytiques au sens suivant: soit M x = ⟨ x 1, …, x p ⟩ {M}_{x}=\langle x_{1},\ldots,x_{p}\rangle l’idéal de S ​ B p, q SB^{p,q} engendré par les fonctions coordonnées x j x_{j}, alors

 | Q A p, q ∩ ( ∩ n M x n) = { 0 } QA^{p,q}\cap(\cap_{n}{M}_{x}^{n})=\{0\} |  | 2 |

Pour p = 1 p=1 et q = 0 q=0, ce résultat a été démontré par Il’yashenko dans [I], par une double application du principe de Phragmen-Lindelof dans P + P^{+} ([Ru, p.244]), en utilisant le difféomorphisme ϕ p ​ u ​ i ​ s \phi_{puis}. Dans le cas général, notons M x, 0 {M}_{x,0} l’idéal de S ​ B p, 0 ​ ( x) SB^{p,0}(x) engendré par les fonctions coordonnées x j x_{j}; si f = ∑ k f k α k ∈ Q A p, q ∩ ( ∩ n M x n) f=\sum_{k}f_{k}\alpha^{k}\in QA^{p,q}\cap(\cap_{n}{M}_{x}^{n}), alors pour tout multi-indice k k: f k ∈ Q A p, 0 ∩ ( ∩ n M x, 0 n) f_{k}\in QA^{p,0}\cap(\cap_{n}{M}_{x,0}^{n}) (par une simple identification des coefficients des séries en α \alpha). Donc pour p = 1 p=1, on obtient encore l’égalité (2). Supposons p > 1 p>1 et considérons la restriction de f k f_{k} à un voisinage de la diagonale de ( ℝ + ⁣ ∗) p ({\mathbb{\mathbb{R}}}^{+*})^{p}: soit l’application g: ( y, β) ∈ ℝ + ⁣ ∗ × ℝ p − 1 ↦ x = g ⁡ ( y, β) = ( y, y ⁡ ( 1 + β 1), …, y ⁡ ( 1 + β p − 1)) g:(y,\beta)\in{\mathbb{\mathbb{R}}}^{+*}\times{\mathbb{\mathbb{R}}}^{p-1}\mapsto x=g(y,\beta)=(y,y(1+\beta_{1}),\ldots,y(1+\beta_{p-1})). Soit U ∈ ( ( ℝ + ⁣ ∗) p, 0) U\in(({\mathbb{\mathbb{R}}}^{+*})^{p},0) sur lequel est réalisée f k f_{k} (il est indépendant de k k), et soit V ∈ ( ℝ + ⁣ ∗ × ℝ p − 1, 0) V\in({\mathbb{\mathbb{R}}}^{+*}\times{\mathbb{\mathbb{R}}}^{p-1},0) tel que g ⁡ ( V) ⊂ U g(V)\subset U. Soit F k F_{k} le germe en 0 de f k ∘ g | V f_{k}\circ g_{|V}, c’est un élément de l’anneau S ​ B 1, p − 1 ​ ( y, β) SB^{1,p-1}(y,\beta) (car le germe à l’infini du translaté complexe de tout secteur S θ S_{\theta} est inclus dans le germe à l’infini d’un secteur S θ ′ S_{\theta^{\prime}}). Soit M y {M}_{y} l’idéal de S ​ B 1, p − 1 SB^{1,p-1} engendré par la coordonnée y y, par la stabilité des domaines standards par intersection finie et par translation, on a F k ∈ Q A 1, p − 1 ∩ ( ∩ n M y n) F_{k}\in QA^{1,p-1}\cap(\cap_{n}{M}_{y}^{n}) (on a même que F k ∈ Q ​ A 1, 0 ​ ( y) ​ { β } F_{k}\in QA^{1,0}(y)\{\beta\}, la série étant convergente sur un produit Ω 0 × W \Omega_{0}\times W où Ω 0 \Omega_{0} est un domaine standard et W W est un voisinage de 0 dans ℂ p − 1 {\mathbb{\mathbb{C}}}^{p-1}). Le germe F k F_{k} est donc identiquement nul, et il en est de même pour f k f_{k} et pour f f.

Ces algèbres sont stables par les dérivations χ j \chi_{j} (par les formules de Cauchy dans les coordonnées w j w_{j} dans les translatés 1 + Ω j 1+\Omega_{j}). Leur localité est un problème ouvert. Elles sont strictement incluses dans les algèbres S ​ B p, q SB^{p,q}: en effet, le germe f ( x) = x log ⁡ ( − log ⁡ ( x) CLOSE ∈ S B 1, 0 ( x) ∩ ( ∩ n M x n) f(x)=x^{\log(-\log(x)}\in SB^{1,0}(x)\cap(\cap_{n}{M}_{x}^{n}) (pour cela, il suffit de voir que pour tout n ∈ ℕ n\in{\mathbb{N}}, le relevé f n ​ ( w) = exp ⁡ ( − w ⁡ ( log ⁡ ( w) − n)) f_{n}(w)=\exp(-w(\log(w)-n)) est borné sur tout germe ( S θ, ∞) (S_{\theta},\infty) avec θ ∈] 0, π / 2 [\theta\in]0,\pi/2[). Cependant, si p > 0 p>0, la topologie de Krull de l’anneau Q ​ A p, q QA^{p,q} (induite par celle de l’anneau S ​ B p, q SB^{p,q}) n’est pas séparée (pour tout s > 0 s>0, x 1 s ∈ M x_{1}^{s}\in{M}, où M {M} est l’idéal maximal de S ​ B p, q SB^{p,q}). Et les idéaux les plus simples des anneaux Q ​ A p, q QA^{p,q} ne sont pas noethériens (ni dans l’anneau Q ​ A p, q QA^{p,q} ni même dans son extension A p, q {A}^{p,q}): tel est le cas par exemple des idéaux engendrés par les fonctions élémentaires f n = x ​ ( log ⁡ x) n f_{n}=x(\log x)^{n} ou g n = x 1 / n g_{n}=x^{1/n}. Ainsi, une structure asymptotique dans un nombre fini de fonctions élémentaires est souhaitable.

§4. Algèbres quasi-régulières d’Hilbert Q ​ R ​ H p, q QR{H}^{p,q}.

La dernière condition de régularité qu’on impose sur les germes étudiés est l’existence d’une structure asymptotique élémentaire dans les variables quasi-ana-

lytiques x j x_{j}. Pour ( y, β) ∈ ℝ + ⁣ ∗ × ℝ (y,\beta)\in\mathbb{R}^{+*}\times\mathbb{R}, notons Ld (pour L ogarithme d éployé) la fonction

 | Ld ( y, β) = ∫ 1 y t − 1 + β d t = { y β − 1 β pour β ≠ 0 log ⁡ y pour β = 0 \text{Ld}(y,\beta)=\int_{1}^{y}{t^{-1+\beta}}dt=\left\{\begin{aligned} \frac{y^{\beta}-1}{\beta}\quad&\text{ pour }\quad\beta\neq 0\\ \log y\quad&\text{ pour }\quad\beta=0\end{aligned}\right. |  | 3 |

Ceci est simplement le compensateur élémentaire d’Ecalle-Roussarie [E], [Ro2]. La fonction f ⁡ ( y, β) = y ​ L ​ d ​ ( y, β) ∈ Q ​ A 1, 1 ​ ( y, β) f(y,\beta)=yLd(y,\beta)\in QA^{1,1}(y,\beta): soit F ⁡ ( w, β) = f ⁡ ( exp ⁡ ( − w), β) F(w,\beta)=f(\exp(-w),\beta) et soit θ ∈ [0, π / 2 [\theta\in[0,\pi/2[, en faisant le changement de coordonnées t = exp ⁡ ( − z) t=\exp(-z) dans l’intégrale (3), on vérifie facilement que pour | β | |\beta| suffisament petit, on a | F ⁡ ( w, β) | ≤ 1 / cos ⁡ ( θ) |F(w,\beta)|\leq 1/\cos(\theta) sur le secteur S θ S_{\theta}. De plus, F ⁡ ( w, β) = ∑ F n ​ ( w) ​ β n F(w,\beta)=\sum F_{n}(w)\beta^{n} avec

 | F n ​ ( w) = 1 ( n + 1)! ​ ( − w) n + 1 ​ exp ⁡ ( − w) F_{n}(w)=\frac{1}{(n+1)!}(-w)^{n+1}\exp(-w) |  |

chaque fonction F n F_{n} est bornée sur le domaine exponentiel Ω e ​ x ​ p ​ ( 0, 1, n + 2) \Omega_{exp}(0,1,n+2) et sur tout compact de P + P^{+}. Les fonctions F n F_{n} sont donc bornées sur n’importe quel domaine de type puissance (voir appendice VA pour une preuve générale).

Soit q = ( q 1, q 2) ∈ ℕ 2 q=(q_{1},q_{2})\in\mathbb{N}^{2} et α = ( μ, ν) \alpha=(\mu,\nu) des coordonnées sur ℝ q 1 × ℝ q 2 \mathbb{R}^{q_{1}}\times\mathbb{R}^{q_{2}}. Soient les fonctions élémentaires z i, 0 ​ ( x i) = x i ​ log ⁡ x i z_{i,0}(x_{i})=x_{i}\log x_{i} et z i, j z_{i,j} leurs déploiements

 | z i, j ​ ( x i, μ j) = x i ​ Ld ​ ( x i, μ j) z_{i,j}(x_{i},\mu_{j})=x_{i}\text{Ld}(x_{i},\mu_{j}) |  | 4 |

Ces fonctions appartiennent à l’algèbre Q ​ A 1, 1 QA^{1,1}. Dans la suite, certaines notations (de sens clair dans le texte) désignent aussi bien des fonctions que les coordonnées correspondantes. Soient

 | X i = ( x i, z i, 0, z i, 1, ⋯, z i, q 1) et X = ( X 1, …, X p) X_{i}=(x_{i},z_{i,0},z_{i,1},\cdots,z_{i,q_{1}})\quad\text{ et }\quad X=(X_{1},\ldots,X_{p}) |  | 5 |

Notons x ^ i = ( x 1, ⋯, x i − 1, x i + 1, ⋯, x p) \widehat{x}^{i}=(x_{1},\cdots,x_{i-1},x_{i+1},\cdots,x_{p}) et c i c_{i} et c c les immersions

 | c i ​ ( x, α) = ( X i, x ^ i, α) c ⁡ ( x, α) = ( X, α) c_{i}(x,\alpha)=(X_{i},\widehat{x}^{i},\alpha)\quad\quad c(x,\alpha)=(X,\alpha) |  | 6 |

###### Définition IA5

Convenons que Q ​ R ​ H 0, q ​ ( α) = ℝ ⁡ { α } QR{H}^{0,q}(\alpha)=\mathbb{R}\{\alpha\}. Alors, l’algèbre quasi-régulière d’Hilbert Q ​ R ​ H p, q ​ ( x, α) ⊂ Q ​ A p, | q | ​ ( x, α) QR{H}^{p,q}(x,\alpha)\subset QA^{p,|q|}(x,\alpha) est l’ensemble des germes f f ayant un développement asymptotique de ”type Hilbert”: pour tout i = 1, ⋯, p i=1,\cdots,p, il existe une suite ( G i, m) m (G_{i,m})_{m} dans Q ​ R ​ H p − 1, q ​ ( x ^ i, α) ​ [X i] QR{H}^{p-1,q}(\widehat{x}_{i},\alpha)[X_{i}] qui sont des polynômes homogènes de degré m m dans la variable X i X_{i} telle que pour tout n ∈ ℕ n\in{\mathbb{\mathbb{N}}}

 | f ⁡ ( x, α) = ∑ m = 0 n G i, m ∘ c i ​ ( x, α) + x i n ​ h n avec h n ∈ S ​ B 0 p, | q | f(x,\alpha)={\sum}_{m=0}^{n}G_{i,m}\circ c_{i}(x,\alpha)+x_{i}^{n}h_{n}\qquad\text{avec}\qquad h_{n}\in SB^{p,|q|}_{0} |  | 7 |

Les variables analytiques ν \nu n’interviennent pas dans la construction des fonctions élémentaires (4), d’où la distinction faite dans les variables analytiques α \alpha. Dans le problème d’Hilbert, les variables μ \mu sont les paramètres qui déploient les valeurs propres des singularités, et les variables ν \nu sont tout autres paramètres.

L’unicité des séries formelles (7) ainsi que l’injectivité des morphismes série formelle associés sont démontrés dans la section II. On y démontre aussi l’existence et l’injectivité d’un morphisme série formelle f ∈ Q ​ R ​ H p, q ↦ f ^ ∈ c ∗ ​ ( ℝ ⁡ { α } ​ [[X]]) f\in QR{H}^{p,q}\mapsto\widehat{f}\in c^{*}(\mathbb{R}\{\alpha\}[[X]]); ceci implique en particulier que la topologie de Krull des algèbres Q ​ R ​ H p, q QR{H}^{p,q} est séparée. Les germes quasi-analytiques ( ∈ Q ​ A p, | q | \in QA^{p,|q|}) qui possèdent une telle série formelle forment une sur-algèbre de Q ​ R ​ H p, q QR{H}^{p,q} qui ne sera pas étudié dans ce travail. La sous-algèbre Q ​ R ​ H cvg p, q QR{H}_{\text{cvg}}^{p,q} des éléments ”convergents” de l’algèbre Q ​ R ​ H p, q QR{H}^{p,q} est définie par

###### Définition IA6

On note Q ​ R ​ H cvg p, q = c ∗ ​ ( ℝ ⁡ { X, α }) QR{H}_{\text{cvg}}^{p,q}=c^{*}(\mathbb{R}\{X,\alpha\}).

Une conséquence algébrique de la transcendance du graphe de c c est que le morphisme c ∗ c^{*} est un isomorphisme sur son image. Ceci est démontré aussi dans le section II.

B. Quelques généralités et six lemmes de base.

Les anneaux de référence sont les anneaux locaux B {B} telles que ℝ ⁡ { x, α } ⊂ B ⊂ A p, q ​ ( x, α) \mathbb{R}\{x,\alpha\}\subset{B}\subset{A}^{p,q}(x,\alpha) et qui sont stables par les dérivations

 | ∏ j = 1 p x j ​ ∂ ∂ y i avec y = ( x, α) \prod_{j=1}^{p}x_{j}\frac{\partial}{\partial y_{i}}\qquad\text{avec}\quad y=(x,\alpha) |  |

Ce sont des ℝ \mathbb{R} -algèbres. Dans la suite, on parlera indifférement d’anneau ou d’algè-

bre. L’idéal maximal de B {B} est l’idéal des germes nuls en 0. En cas d’ambiguité, on note B ⁡ ( y) {B}(y) pour préciser le choix des coordonnées.

§1. Anneaux restriction et anneaux extension.

Soit U U un représentant de ( ( ℝ + ⁣ ∗) p × ℝ q, 0) (({\mathbb{\mathbb{R}}}^{+*})^{p}\times{\mathbb{\mathbb{R}}}^{q},0) et soit B p = { ∏ j = 1 p x j = 0 } B_{p}=\{\prod_{j=1}^{p}x_{j}=0\} le bord associé de germe ( B p, 0) (B_{p},0) en 0. Soit U O ⊂ U U_{O}\subset U un sous-ensemble quelconque dont l’adhérence contient 0. On note ( U 0, 0) (U_{0},0) le germe de U 0 U_{0} en 0 . On note aussi ∂ 0 U 0 = B p ∩ U 0 ¯ \partial_{0}U_{0}=B_{p}\cap\overline{U_{0}} le bord associé et ∂ 0 ( U 0, 0) \partial_{0}(U_{0},0) son germe en 0. Soit B ⊂ A p, q ​ ( y) {B}\subset{A}^{p,q}(y) un anneau de référence et soit i U 0: ( U 0, 0) → ( U, 0) i_{U_{0}}:(U_{0},0)\to(U,0) le germe de l’injection canonique (qu’on notera aussi i U 0, U i_{U_{0},U} en cas d’ambiguité). On lui associe un morphisme étoilé

 | i U 0 ∗: f ∈ B ↦ i U 0 ∗ ​ ( f) = f ∘ i U 0 i^{*}_{U_{0}}:f\in{B}\mapsto i^{*}_{U_{0}}(f)=f\circ i_{U_{0}} |  |

On généralise ainsi les anneaux de référence B {B} aux anneaux restriction notés B | U 0 {B}_{|U_{0}} et définis comme suit:

 | B | U 0 = i U 0 ∗ ( B) {B}_{|U_{0}}=i^{*}_{U_{0}}({B}) |  |

C’est un anneau local (qui n’est pas forcément intègre). Il ne dépend de U 0 U_{0} que par son germe ( U 0, 0) (U_{0},0). Il est isomorphe à B {B} (par i U 0 ∗ i^{*}_{U_{0}}) si ( U 0, 0) (U_{0},0) est d’intérieur non vide (ie. l’adhérence de l’intérieur de U 0 U_{0} contient 0): en effet, une fonction analytique nulle sur un ouvert connexe est nulle sur la composante connexe de son domaine d’analycité contenant cet ouvert. Le sous-ensemble U 0 U_{0} est dit semi-analytique élémentaire de B {B} (ou décrit par B {B}) s’il existe V ∈ ( U, 0) V\in(U,0) et contenant U 0 U_{0} et des germes f 1, …, f n, g 1, …, g m ∈ B f_{1},\ldots,f_{n},g_{1},\ldots,g_{m}\in{B} et représentés sur V V tels que

 | U 0 = { y ∈ V; f 1 ​ ( y) > 0, …, f n ​ ( y) > 0, g 1 ​ ( y) = 0, …, g m ​ ( y) = 0 } U_{0}=\{y\in V;\ f_{1}(y)>0,\ldots,f_{n}(y)>0,g_{1}(y)=0,\ldots,g_{m}(y)=0\} |  |

Il est dit semi-analytique de B {B} (ou décrit par B {B}) si c’est une union finie de semi-analytiques élémentaires de B {B}. Dans ce cas, le morphisme i U 0 ∗ i^{*}_{U_{0}} est un isomorphisme si et seulement si ( U 0, 0) (U_{0},0) est d’intérieur non vide: en effet, si U 0, 1, …, U 0, ℓ U_{0,1},\ldots,U_{0,\ell} sont les semi-analytiques élémentaires formant U 0 U_{0}, l’un des U 0, j U_{0,j} est un ouvert dont l’adhérence contient 0, sinon il existe g i 1, 1, …, g i ℓ, ℓ ∈ B ∖ { 0 } g_{i_{1},1},\ldots,g_{i_{\ell},\ell}\in{B}\setminus\{0\} tels que g = g i 1, 1 × ⋯ × g i ℓ, ℓ g=g_{i_{1},1}\times\cdots\times g_{i_{\ell},\ell} est nulle sur ( U 0, 0) (U_{0},0); mais par l’isomorphisme i U 0 ∗ i^{*}_{U_{0}}, g g est alors nulle, ce qui contredit l’intégrité de B {B}.

Soit I I un idéal de B {B}. Le morphisme i U 0 ∗ i^{*}_{U_{0}} étant surjectif, le sous-ensemble i U 0 ∗ ​ ( I) i^{*}_{U_{0}}(I) est un idéal de B | U 0 {B}_{|U_{0}} dit idéal restriction. On le note simplement I | U 0 I_{|U_{0}}; il ne dépend de U 0 U_{0} que par son germe ( U 0, 0) (U_{0},0). Inversement, tout idéal J J de B | U 0 {B}_{|U_{0}} est un idéal restriction: I = ( i U 0 ∗) − 1 ​ ( J) I=(i^{*}_{U_{0}})^{-1}(J) est un idéal de B {B} et I | U 0 = J I_{|U_{0}}=J.

Soit B ′ ⊂ A p ′, q ′ ​ ( x ′, α ′) {B}^{\prime}\subset{A}^{p^{\prime},q^{\prime}}(x^{\prime},\alpha^{\prime}) un anneau de référence. Soit U ′ ∈ ( ( ℝ + ⁣ ∗) p ′ × ℝ q ′, 0) U^{\prime}\in((\mathbb{R}^{+*})^{p^{\prime}}\times\mathbb{R}^{q^{\prime}},0) et soit U 0 ′ U^{\prime}_{0} un sous-ensemble de U ′ U^{\prime} dont l’adhérence contient 0. L’anneau B ′ | U ′ 0 {B}^{\prime}_{|U^{\prime}_{0}} est dit anneau extension de l’anneau B | U 0 {B}_{|U_{0}} s’il existe un homomorphisme d’anneaux injectif Ψ: B | U 0 ↪ B ′ | U ′ 0 \Psi:\ {B}_{|U_{0}}\hookrightarrow{B}^{\prime}_{|U^{\prime}_{0}}. Dans ce cas, si J J est un idéal de B | U 0 {B}_{|U_{0}}, on appelle idéal prolongé associé à J J l’idéal de B ′ | U ′ 0 {B}^{\prime}_{|U^{\prime}_{0}} engendré par le sous-ensemble Ψ ⁡ ( J) \Psi(J). On le notera simplement Ψ ⁡ ( J) \Psi(J) si aucune confusion n’est à craindre. Cet idéal prolongé est aussi un idéal restriction.

Soit ψ: U 0 ′ → U 0 \psi:U^{\prime}_{0}\rightarrow U_{0} un morphisme surjectif, continu sur U 0 ′ ∪ { 0 } U^{\prime}_{0}\cup\{0\} et tel que ψ ⁡ ( 0) = 0 \psi(0)=0. On note de la même façon son germe ψ: ( U 0 ′, 0) → ( U 0, 0) \psi:(U^{\prime}_{0},0)\rightarrow(U_{0},0). Ce germe induit un morphisme étoilé ψ ∗ \psi^{*} qui agit sur l’anneau B | U 0 {B}_{|U_{0}} et qui est injectif. On suppose que ψ ∗ ( B | U 0) ⊂ B | U ′ 0 ′ \psi^{*}({B}_{|U_{0}})\subset{B}^{\prime}_{|U^{\prime}_{0}}. Dans ce cas, on dira que l’anneau B ′ | U ′ 0 {B}^{\prime}_{|U^{\prime}_{0}} est une extension étoilée de l’anneau B | U 0 {B}_{|U_{0}} et on la note ( B | U ′ 0 ′, ψ) ({B}^{\prime}_{|U^{\prime}_{0}},\psi). Si g g est un élément de B | U 0 {B}_{|U_{0}}, on a la relation suivante entre les germes en 0 des ensembles de zéros

 | Z ⁡ ( ψ ∗ ​ ( g)) = ψ − 1 ​ ( Z ⁡ ( g)) Z(\psi^{*}(g))=\psi^{-1}(Z(g)) |  | 0 |

Dans toute la suite, on ne considérera que des extensions étoilées.

###### Définition IB1

Soit I I un idéal de B {B}.

Si ( U 0, 0) = ( U, 0) (U_{0},0)=(U,0), on dit simplement que I I est ”noethérien” ou localement ”noethé-

rien”. Dorénavant, on enlève les guillemets au mot ”noethérien”. En cas d’ambigui-

té, on précisera l’anneau de référence pour les idéaux prolongés (qui est aussi l’extension étoilée associée). Soit J ⊂ B | U 0 J\subset{B}_{|U_{0}} un idéal noethérien et soit ( B | U ′ 0 ′, ψ) ({B}^{\prime}_{|U^{\prime}_{0}},\psi) l’extension associée. On sait définir le germe en 0 de l’ensemble des zéros de l’idéal prolongé ψ ∗ ​ ( J) \psi^{*}(J): c’est celui de n’importe quel système fini de générateurs de cet idéal dans l’anneau B ′ | U ′ 0 {B}^{\prime}_{|U^{\prime}_{0}}. Maintenant, si g 1, …, g n ∈ J g_{1},\ldots,g_{n}\in J sont tels que ψ ∗ ​ ( g 1), …, ψ ∗ ​ ( g n) \psi^{*}(g_{1}),\ldots,\psi^{*}(g_{n}) forment un système de générateurs de ψ ∗ ​ ( J) \psi^{*}(J) (il en existe), la relation (0) montre que le germe Z ⁡ ( g 1) ∩ ⋯ ∩ Z ⁡ ( g n) Z(g_{1})\cap\cdots\cap Z(g_{n}) est indépendant du système ainsi choisi, et qu’on a donc une notion d’ensemble des zéros de l’idéal J J, qu’on note Z ⁡ ( J) Z(J) et qui est donné par la formule ( ψ \psi étant surjective)

 | Z ⁡ ( ψ ∗ ​ ( J)) = ψ − 1 ​ ( Z ⁡ ( J)) Z(\psi^{*}(J))=\psi^{-1}(Z(J)) |  | 1 |

En particulier, pour tout g ∈ J g\in J, on a g | Z ( J) = 0 g_{|Z(J)}=0.

§2. Projection unidimensionnelle.

Soit Ξ ​ B \Xi{B} la classe des germes en 0 de champs de vecteurs χ = ∑ j = 1 p + q a j ( y) ∂ / ∂ y j \chi=\sum_{j=1}^{p+q}a_{j}(y)\partial/\partial y_{j} dont les composantes a j a_{j} sont des éléments de B {B}, et qui satisfont aux conditions suivantes

Un ouvert U U satisfaisant aux conditions ( i) (i) et ( i ​ i) (ii) est dit admissible. Soit χ ∈ Ξ ​ B \chi\in\Xi{B} et soit U U un ouvert admissible. Soit φ χ, U \varphi_{\chi,U} le flot de χ \chi dans U U; on note π χ, U: U ↦ U ~ = U / φ χ, U \pi_{\chi,U}:U\mapsto\widetilde{U}=U/\varphi_{\chi,U} la projection le long des orbites de χ \chi dans U U (on l’appelle aussi le morphisme intégral de χ \chi dans U U). L’espace U ~ \widetilde{U} étant muni de la topologie quotient. Cette projection est donc continue et ouverte. Soit S ⊂ ( ℝ + ⁣ ∗) p × ℝ q S\subset(\mathbb{R}^{+*})^{p}\times\mathbb{R}^{q} dont l’adhérence contient 0

###### Définition IB2

Le degré de la projection π χ, U \pi_{\chi,U} restreinte au sous-ensemble S S est

 | d ° ​ π χ, U | S = sup γ ⊂ U b 0 ​ ( γ ∩ S) d^{°}\pi_{\chi,U|S}=\sup_{\gamma\subset U}b_{0}(\gamma\cap S) |  |

où γ \gamma est une orbite de χ \chi dans U U, et b 0 b_{0} est le premier nombre de Betti. On note

 | d ° ​ π χ | ( S, 0) = inf U d ° ​ π χ, U | S d^{°}\pi_{\chi|(S,0)}=\inf_{U}d^{°}\pi_{\chi,U|S} |  |

où la borne inférieure est prise sur tous les ouverts U U admissibles.

La notation π χ \pi_{\chi} dans cette définition, ne désigne pas un germe. En général, il n’existe pas de notion de germe en 0, pour la projection intégrale, qui soit indépendante des ouverts U U (ou du moins d’une base d’ouverts U U). Quand il en existe une, on note ce germe π χ \pi_{\chi}; c’est par exemple le cas quand le champ χ \chi admet une orbite ”principale” dans U U (cf. fin de cette section), ou plus généralement, quand il admet dans U U, ( p + q − 1) (p+q-1) intégrales premières F j F_{j}, analytiques et indépendantes: la (p+q-1)-forme d ​ F 1 ∧ ⋯ ∧ d ​ F p + q − 1 dF_{1}\wedge\cdots\wedge dF_{p+q-1} ne s’annule pas sur U U.

2.1 χ \chi -régularité et χ \chi -finitude.

Soit U 0 ⊂ ( ℝ + ⁣ ∗) p × ℝ q U_{0}\subset(\mathbb{R}^{+*})^{p}\times\mathbb{R}^{q} dont l’adhérence contient 0. On dit que le germe ( U 0, 0) (U_{0},0) (ou simplement U 0 U_{0}) est invariant par χ \chi s’il existe un ouvert U U admissible tel que U 0 ∩ U U_{0}\cap U soit une union d’orbites de χ \chi dans U U.

###### Définition IB3

Soit f ∈ B f\in{B} et Z ⁡ ( f) Z(f) le germe en 0 de son ensemble des zéros. On dit que f f est χ \chi -régulière sur U 0 U_{0} si

 | d ° ​ π χ | Z ⁡ ( f) ∩ ( U 0, 0) < + ∞ d^{°}\pi_{\chi|Z(f)\cap(U_{0},0)}<+\infty |  |

Si ( U 0, 0) = ( U, 0) (U_{0},0)=(U,0) où U U est un ouvert admissible, on dit simplement que f f est χ \chi -régulière. Van Den Dries parle dans l’un de ces travaux ([Dr]) d’une certaine ”propriété de finitude” (qui porte justement sur des projections unidimensionnelles mais linéaires!), qui est équivalente à cette notion de χ \chi -régularité. Soit I χ, f = ⟨ χ n ​ f; n ∈ ℕ ⟩ I_{\chi,f}=\langle\chi^{n}f;\ n\in\mathbb{N}\rangle l’idéal différentiel de f f dans l’anneau B {B}. Si U ′ ⊂ U U^{\prime}\subset U est un ouvert admissible sur lequel est réalisée f f, alors tous les germes χ n ​ f \chi^{n}f sont aussi réalisés sur U ′ U^{\prime}. On note Z ⁡ ( I χ, f CLOSE Z(I_{\chi,f} le germe en 0 de ∩ n ∈ ℕ S n \cap_{n\in\mathbb{N}}S_{n}, où S n S_{n} est un représentant de Z ⁡ ( χ n ​ f) Z(\chi^{n}f) sur U ′ U^{\prime}. Cette définition de l’ensemble des zéros d’un idéal différentiel coincide avec la définition classique en cas de noethérianité. Remarquer que le germe Z ⁡ ( I χ, f) Z(I_{\chi,f}) est invariant par χ \chi.

###### Définition IB4

On suppose que f f est χ \chi -régulière sur U 0 U_{0},

###### Définition IB5

Une classe C ⊂ B {C}\subset{B} est dite χ \chi -finie sur U 0 U_{0} (resp. localement χ \chi -finie sur U 0 U_{0}) si tout f ∈ C f\in{C} est χ \chi -finie sur U 0 U_{0} (resp. localement χ \chi -finie sur U 0 U_{0}). Elle est dite χ \chi -stable si χ ⁡ ( C) ⊂ C \chi({C})\subset{C}.

Si ( U 0, 0) = ( U, 0) (U_{0},0)=(U,0) où U U est un ouvert admissible, on dit simplement que f f (ou la classe C {C}) est χ \chi -finie, ou alors que f f (ou la classe C {C}) est localement χ \chi -finie.

2.2 Six lemmes de base.

Le premier de ces lemmes, qui est un lemme fondamental, donne les propriétés de finitude d’une certaine classe de germes qui sont ”bien préparés” et dans une extension appropriée. On suppose donc dans ce lemme que les anneaux de référence pour la noethérianité, sont les anneaux restriction B | U 0 {B}_{|U_{0}}. Soit M {M} l’idéal maximal de B {B}

###### Lemme IB1 (lemme de $\chi$-finitude)

Soit B 0 ⊂ B {B}_{0}\subset{B} une algèbre χ \chi -finie sur U 0 U_{0} (resp. localement χ \chi -finie sur U 0 U_{0}) et χ \chi -stable. Soit M 0 ⊂ M {M}_{0}\subset{M} un idéal χ \chi -stable. Soit N U 0 ⊂ B {N}_{U_{0}}\subset{B} l’idéal des germes nuls sur ( U 0, 0) (U_{0},0). Alors la classe C B 0, M 0 = { f ∈ g + M 0 ​ I χ, g + N U 0; g ∈ B 0 } ⊂ B {C}_{{B}_{0},{M}_{0}}=\{f\in g+{M}_{0}I_{\chi,g}+{N}_{U_{0}};\ g\in{B}_{0}\}\subset{B} est χ \chi -finie sur U 0 U_{0} (resp. localement χ \chi -finie sur U 0 U_{0}).

Preuve. Il suffit de la faire dans le cas de χ \chi -finitude sur U 0 U_{0}. Soit g ∈ B 0 g\in{B}_{0} et soit

 | f ∈ g + M 0 ​ I χ, g + N U 0 f\in g+{M}_{0}I_{\chi,g}+{N}_{U_{0}} |  | 2 |

Le germe ( U 0, 0) (U_{0},0) étant invariant par la dérivation χ \chi, l’idéal N U 0 {N}_{U_{0}} est χ \chi -stable. La relation (2) implique donc que I χ, f | U 0 ⊂ I χ, g | U 0 I_{\chi,f|U_{0}}\subset I_{\chi,g|U_{0}}. Montrons d’abord que l’idéal I χ, f | U 0 I_{\chi,f|U_{0}} est noethérien dans l’anneau B | U 0 {B}_{|U_{0}}. L’algèbre B 0 {B}_{0} étant χ \chi -finie sur U 0 U_{0}, l’idéal I χ, g | U 0 I_{\chi,g|U_{0}} est noethérien dans l’anneau B | U 0 {B}_{|U_{0}}. Soit ( g | U 0), …, ( ( χ ℓ g) | U 0)) (g_{|U_{0}}),\ldots,((\chi^{\ell}g)_{|U_{0}})) un système de générateurs de l’idéal I χ, g | U 0 I_{\chi,g|U_{0}}. L’idéal maximal de B | U 0 {B}_{|U_{0}} est M ′ = M | U 0 {M}^{\prime}={M}_{|U_{0}} (car les éléments de B ⊂ A p, q {B}\subset{A}^{p,q} sont continues en 0). Comme M 0 ⊂ M {M}_{0}\subset{M}, on a M 0 ′ = ( M 0 | U 0) ⊂ M ′ {M}^{\prime}_{0}=({M}_{0|U_{0}})\subset{M}^{\prime}. En appliquant ℓ \ell fois la dérivation χ \chi à la relation (2), puis en prenant la restriction à ( U 0, 0) (U_{0},0), on obtient

 | I χ, g | U 0 ⊂ I χ, f | U 0 + M 0 ′ ​ I χ, g | U 0 I_{\chi,g|U_{0}}\subset I_{\chi,f|U_{0}}+{M}^{\prime}_{0}I_{\chi,g|U_{0}} |  |

Comme l’idéal I χ, g | U 0 I_{\chi,g|U_{0}} est noethérien, le Lemme de Nakayama (cf. [L]) implique que I χ, g | U 0 ⊂ I ​ χ, f | U 0 I_{\chi,g|U_{0}}\subset I{\chi,f|U_{0}}. On obtient alors I χ, f | U 0 = I χ, g | U 0 I_{\chi,f|U_{0}}=I_{\chi,g|U_{0}}. L’idéal I χ, f | U 0 I_{\chi,f|U_{0}} est donc noethérien dans l’anneau B | U 0 {B}_{|U_{0}}.

Montrons maintenant que f f est χ \chi -régulière sur U 0 U_{0}. Soit F = Z ⁡ ( I χ, f | U 0) ⊂ ( U 0, 0) F=Z(I_{\chi,f|U_{0}})\subset(U_{0},0) l’ensemble des zéros de l’idéal I χ, f | U 0 I_{\chi,f|U_{0}}; il est invariant par χ \chi et d ° ​ π χ | F ≤ 1 d^{°}\pi_{\chi|F}\leq 1. Or, on a aussi F = Z ⁡ ( I χ, g) F=Z(I_{\chi,g}). Soit U U un ouvert admissible tel que U 0 ∩ U U_{0}\cap U soit une union d’orbites de c ​ h ​ i chi dans U U. Soit U ′ ⊂ U U^{\prime}\subset U un ouvert admissible où sont réalisés le germe g g et la relation (2). le sous-ensemble U 0 ∩ U ′ U_{0}\cap U^{\prime} est encore une union d’orbite de χ \chi dans U ′ U^{\prime}. Notons S S le représentant du germe F F sur U ′ U^{\prime} et considérons alors les sous-ensembles

 | S j = { m ∈ U ′ ∩ U 0; | χ j ​ g ​ ( m) | = max i = 0 ℓ ​ | χ i ​ g ​ ( m) | } ∖ S S_{j}=\{m\in U^{\prime}\cap U_{0};\ |\chi^{j}g(m)|=\max_{i=0}^{\ell}|\chi^{i}g(m)|\}\setminus S |  |

Si U ′ U^{\prime} est suffisament petit, une orbite γ \gamma de χ \chi dans U ′ ∩ U 0 U^{\prime}\cap U_{0} rencontre S j S_{j} en un nombre fini d’intervalles σ \sigma de γ \gamma (dont certains peuvent être réduits à un point), et ce nombre est uniformément majoré par un entier n j n_{j} qui ne dépend que de S j S_{j}. En effet, les extrémités m m de ces intervalles σ \sigma qui appartiennent à γ \gamma satisfont des équations du type

 | g i, j ± ​ ( m) = χ j ​ g ​ ( m) ± χ i ​ g ​ ( m) = 0 i ≠ j g_{i,j}^{\pm}(m)=\chi^{j}g(m)\pm\chi^{i}g(m)=0\quad i\neq j |  |

et ces germes g i, j ± g_{i,j}^{\pm} (en nombre fini) sont des éléments de l’algèbre B 0 {B}_{0} qui est χ \chi -stable et χ \chi -finie sur U 0 U_{0}. Si on note S i, j ± S_{i,j}^{\pm} le représentant de Z ⁡ ( g i, j ±) Z(g_{i,j}^{\pm}) sur U ′ U^{\prime}, on peut donc prendre

 | n j = ∑ i ≠ j d ° ​ π χ, U ′ | S i, j ± ∩ U 0 n_{j}=\sum_{i\neq j}d^{°}\pi_{\chi,U^{\prime}|S_{i,j}^{\pm}\cap U_{0}} |  |

Maintenant, sur un de ces intervalles σ \sigma (non réduit à un point!), considérons la fonction f σ ​ ( t) = f ∘ φ χ, U ′ ​ ( t, m) f_{\sigma}(t)=f\circ\varphi_{\chi,U^{\prime}}(t,m) où m m est un point de σ \sigma et t t décrit un intervalle τ \tau de ℝ \mathbb{R} tel que φ χ, U ′ ​ ( τ, m) = σ \varphi_{\chi,U^{\prime}}(\tau,m)=\sigma. Un calcul direct montre que les dérivvées successives de f σ f_{\sigma} sont données par

 | f σ ( i) ​ ( t) = χ i ​ f ∘ φ χ, U ′ ​ ( t, m) f_{\sigma}^{(i)}(t)=\chi^{i}f\circ\varphi_{\chi,U^{\prime}}(t,m) |  |

Et la relation (2) dérivée j j fois par rapport à χ \chi et restreinte à U 0 ∩ σ U_{0}\cap\sigma donne

 | ( χ j f) | U 0 ∩ σ = ( χ j g) | U 0 σ ( 1 + O ( m)) (\chi^{j}f)_{|U_{0}\cap\sigma}=(\chi^{j}g)_{|U_{0}\sigma}(1+O(m)) |  |

Ceci montre que la dérivée j j -ème de f σ f_{\sigma} ne s’annule pas sur l’intervalle τ \tau. Par conséquent et par le Lemme de Rolle appliqué à la fonction f σ f_{\sigma} sur l’intervalle τ \tau, on a

 | d ° ​ π χ, U ′ | S ′ ∩ U 0 ≤ ∑ j = 0 ℓ j ​ n j ≤ ℓ ​ ∑ j = 0 ℓ n j d^{°}\pi_{\chi,U^{\prime}|S^{\prime}\cap U_{0}}\leq\sum_{j=0}^{\ell}jn_{j}\leq\ell\sum_{j=0}^{\ell}n_{j} |  |

où S ′ S^{\prime} est le représentant du germe Z ⁡ ( f) Z(f) sur U ′ U^{\prime}. ∎

L’hypothèse M 0 ⊂ M {M}_{0}\subset{M} du lemme ne peut être affaiblie, comme le montre l’exem-

ple suivant: χ = x ∂ / ∂ x \chi=x\partial/\partial x, g = x g=x, h = − 1 + sin ( 1 / x) exp ( − 1 / x) h=-1+\sin(1/x)\exp(-1/x) et f = g + h ​ g f=g+hg; B {B} étant un anneau χ \chi -stable contenant l’anneau ℝ ​ { x } \mathbb{R}\{x\} et les dérivées successives χ n ​ h \chi^{n}h, et B 0 = ℝ ​ { x } {B}_{0}=\mathbb{R}\{x\}. La ”bonne préparation” du lemme est à rapprocher de celle que l’on rencontre dans l’étude des singularités d’applications différentiables, et qui utilise uniquement ”l’idéal jacobien”. Ce qui consiste en fait à regarder l’action simultanée de plusieurs dérivations. Il faut noter que les algèbres étudiées dans ce travail ne sont pas différentiables en 0.

Notons C χ, B = { f ∈ B; I χ, f ​ noethérien dans ​ B } {C}_{\chi,{B}}=\{f\in{B};\ I_{\chi,f}\text{ noethérien dans }{B}\}. Soit la relation sur C χ, B {C}_{\chi,{B}}: f ​ R ​ g ⇔ f{R}g\Leftrightarrow il existe un idéal M 0 ⊂ M {M}_{0}\subset{M} χ \chi -stable tel que f − g ∈ M 0 ​ I χ, g f-g\in{M}_{0}I_{\chi,g}. D’après la preuve précédente, c’est une relation d’équivalence sur C χ, B {C}_{\chi,{B}} dite χ \chi -équivalence dans B {B}. Soient C 1 {C}_{1} et C 2 {C}_{2} des algèbres ou des classes telles que C 1 ⊂ C 2 ⊂ C χ, B {C}_{1}\subset{C}_{2}\subset{C}_{\chi,{B}}. On dit que C 2 {C}_{2} est χ \chi -équivalente à C 1 {C}_{1} dans B {B} si tout élément de C 2 {C}_{2} est χ \chi -équivalent à un élément de C 1 {C}_{1} dans B {B}. Ainsi, si C 1 {C}_{1} est une algèbre χ \chi -stable et χ \chi -finie, le lemme de finitude dit que la classe C 2 ⊂ ∪ M 0 C M 0, C 1 {C}_{2}\subset\cup_{{M}_{0}}{C}_{{M}_{0},{C}_{1}} est χ \chi -finie (l’union étant prise sur tous les idéaux M 0 ⊂ M {M}_{0}\subset{M} et qui sont χ \chi -stables).

Construction d’algèbre χ \chi -finie. Il en existe un grand nombre d’après la riche littérature sur les propriétés de finitude des sous-ensembles analytiques avec de fortes conditions au bord ([T]), les sous-ensembles pfaffiens et les constructions dérivées de la théorie de l’o-minimalité ([W], [D-M-M], [L-R], [L-S], [D-S], [S]…); malheureusement, la question de la noethérianité est rarement étudiée dans ces derniers travaux. Un exemple simple de construction, déduit des idées originales de Khovanski-Tougeron, est illustré dans la section II par l’étude des sous-algèbres convergentes Q ​ R ​ H c ​ v ​ g p, q QR{H}_{cvg}^{p,q}. Il s’appuie sur les idées suivantes

###### Lemme IB2 (lemme d'extension de Tougeron)

Soit B 0 {B}_{0} une sous-algèbre de B {B} stable par χ \chi. On suppose que

Alors, l’algèbre B 0 {B}_{0} est χ \chi -finie.

Preuve. L’hypothèse ( i) (i) implique en particulier que les idéaux différentiels de B 0 {B}_{0} sont noethériens dans B {B}. Les hypothèses ( i) (i) et ( i ​ i) (ii) impliquent que l’algèbre B 0 {B}_{0} est topologiquement noethérienne (cf. [T]). Si S S est un semi-analytique de B 0 {B}_{0} et γ \gamma une orbite régulière de χ \chi dans U U

 | b 0 ( γ ∩ S) = b 0 ( ( ∩ j = 1 p + q − 1 Γ j) ∩ S) b_{0}(\gamma\cap S)=b_{0}((\cap_{j=1}^{p+q-1}\Gamma_{j})\cap S) |  |

où chaque Γ j \Gamma_{j} est une solution séparante de ω j \omega_{j}. Par l’hypothèse ( i ​ i ​ i) (iii), ces 1 1 -formes sont à coefficients dans B 0 {B}_{0}. Donc, par la théorie de Khovanski -Tougeron ([K1], [K2], [T]), ce nombre est majoré par un entier qui ne dépend que de S S et des ω j \omega_{j}. Et donc, tout f ∈ B 0 f\in{B}_{0} est χ \chi -régulier.∎

Si de plus, B 0 {B}_{0} est un anneau de référence, on peut simplifier l’hypothèse ( i ​ i ​ i) (iii) comme ceci: la dérivation χ \chi admet ( p + q − 1) (p+q-1) intégrales premières indépendantes F j ∈ B 0 F_{j}\in{B}_{0}. Cette hypothèse ne peut être affaiblie, commme le montre l’exemple suivant: prenons p = 1 p=1 et q = 2 q=2, soient B 0 = ℝ ⁡ { x, α 1, α 2 } {B}_{0}=\mathbb{R}\{x,\alpha_{1},\alpha_{2}\} et

 | χ = − x ​ ∂ ∂ x + ( a ​ α 1 − b ​ α 2) ​ ∂ ∂ α 1 + ( b ​ α 1 + a ​ α 2) ​ ∂ ∂ α 2 \chi=-x\frac{\partial}{\partial x}+(a\alpha_{1}-b\alpha_{2})\frac{\partial}{\partial\alpha_{1}}+(b\alpha_{1}+a\alpha_{2})\frac{\partial}{\partial\alpha_{2}} |  |

avec a > 0 a>0 et b ≠ 0 b\neq 0. Il est clair que l’anneau B 0 ⊂ A 1, 2 ​ ( x, α) {B}_{0}\subset{A}^{1,2}(x,\alpha) est un anneau de référence qui est χ \chi -stable et qui satifait aux hypothèses ( i) (i) et ( i ​ i) (ii). Cependant, le germe f = α 1 ∈ B 0 f=\alpha_{1}\in{B}_{0} n’est pas χ \chi -régulier. Et le lemme I2 montre que la dérivation χ \chi n’admet pas de paire d’intégrales premières indépendantes, dans aucun anneau de référence qui satisfait aux hypothèses ( i) (i) et ( i ​ i) (ii). Un calcul direct montre qu’il existe une paire d’intégrales premières indépendantes qui sont linéaires en α \alpha et dont les coefficients sont les fonctions oscillantes x a ​ cos ⁡ ( b ​ log ⁡ ( x)) x^{a}\cos(b\log(x)) et x a ​ sin ⁡ ( b ​ log ⁡ ( x)) x^{a}\sin(b\log(x)), qui appartiennent à l’anneau A 1, 0 ​ ( x) {A}^{1,0}(x) mais pas à l’anneau S ​ B 1, 0 ​ ( x) SB^{1,0}(x).

Faisceau différentiel.

Soient f ∈ B f\in{B} et χ ∈ Ξ ​ B \chi\in\Xi{B}. Soit U U un ouvert admissible pour χ \chi sur lequel f f est réalisée. On note I χ, f ​ [U] {I}_{\chi,f}[U] le faisceau différentiel de f f sur U U: sa fibre I χ, f, m {I}_{\chi,f,m} (qu’on note aussi I χ, f ​ ( m) I_{\chi,f}(m)), en un point m ∈ U m\in U, est l’idéal différentiel I χ m, f m ⊂ B m = ℝ ⁡ { y − y m } I_{\chi_{m},f_{m}}\subset{B}_{m}={\mathbb{\mathbb{R}}}\{y-y_{m}\}; χ m \chi_{m} et f m f_{m} étant les germes de χ \chi et f f en m m, et y − y m y-y_{m} sont les coordonnées locales en m m (les représentants d’éléments de ℝ ​ { y − y m } \mathbb{R}\{y-y_{m}\} étant considérés sur des ouverts connexes). On suppose qu’en tout point m m du bord ∂ 0 U \partial_{0}U, il existe un anneau de référence B m ⊂ A p m, q m ​ ( y − y m) {B}_{m}\subset{A}^{p_{m},q_{m}}(y-y_{m}), qui est stable par χ m \chi_{m} (ainsi χ m ∈ Ξ ​ B m \chi_{m}\in\Xi{B}_{m}) et qui contient les germes en m m d’éléments de B {B} qui sont représentés sur un voisinage de m m ( en général, on choisi B m {B}_{m} comme étant l’anneau de ces germes). Dans ce cas, on prolonge le faisceau I χ, f ​ [U] {I}_{\chi,f}[U] par le faisceau I χ, f ​ [U ∪ ∂ 0 U] {I}_{\chi,f}[U\cup\partial_{0}U], dont les fibres différentielles sur le bord ∂ 0 U \partial_{0}U sont les idéaux différentiels I χ m, f m I_{\chi_{m},f_{m}} des anneaux B m {B}_{m} correspondants. Ce faisceau est donc le faisceau associé au préfaisceau F ⁡ [U ∪ ∂ 0 U] {F}[U\cup\partial_{0}U] muni des morphismes restriction naturels, et dont les sections F ⁡ ( V) {F}(V) (où V V est un ouvert de U ∪ ∂ 0 U U\cup\partial_{0}U) sont les idéaux engendrés par la famille ( χ n ​ f) n ∈ ℕ (\chi^{n}f)_{n\in\mathbb{N}} dans l’anneau des fonctions sur V V dont le germe en tout point m ∈ V m\in V, est un élément de l’anneau local B m {B}_{m}.

On montre deux résultats importants concernant ces faisceaux. Conjointement au lemme de finitude, ces résultats (et leurs conséquences) constituent le socle de ce travail.

###### Lemme IB3 (lemme de cohérence)

Le faisceau I χ, f ​ [U] {I}_{\chi,f}[U] est cohérent: plus précisément, pour tout m ∈ U m\in U, il existe un ouvert V m ⊂ U V_{m}\subset U contenant m m, et un entier ℓ m \ell_{m} tels que en tout point m ′ ∈ V m m^{\prime}\in V_{m}, la fibre I χ, f ​ ( m ′) I_{\chi,f}(m^{\prime}) est engendrée par les germes en m ′ m^{\prime} de ( f, χ ​ f, …, χ ℓ m ​ f) (f,\chi f,\ldots,\chi^{\ell_{m}}f). Si de plus, la fibre en 0 0 I χ, f ​ ( 0) = I χ, f I_{\chi,f}(0)=I_{\chi,f} est noethérienne dans B {B}, alors il existe un ouvert V ∈ ( U, 0) V\in(U,0) et contenu dans U U tel que le faisceau I χ, f ​ [U ∪ ∂ 0 V] {I}_{\chi,f}[U\cup\partial_{0}V] soit cohérent.

Preuve. Si la fibre en 0 est noethérienne et si ( f CLOSE (f, χ ​ f, … \chi f,\ldots, OPEN χ ℓ ​ f) \chi^{\ell}f) est un système de générateurs de I χ, f I_{\chi,f} dans B {B}, alors il existe un voisinage ouvert V V de 0 0 dans U U tel que la division

 | χ l + 1 ​ f = ∑ i = 0 ℓ h i ​ χ i ​ f \chi^{l+1}f=\sum_{i=0}^{\ell}h_{i}\chi^{i}f |  |

soit réalisée sur un voisinage de V ¯ \overline{V} dans U ∪ ∂ 0 U U\cup\partial_{0}U. En dérivant plusieurs fois cette égalité, on obtient que pour tout k k, la division

 | χ k ​ f = ∑ i = 0 ℓ h i, k ​ χ i ​ f \chi^{k}f=\sum_{i=0}^{\ell}h_{i,k}\chi^{i}f |  |

est réalisée sur ce même voisinage. On obtient le résultat en germifiant ces égalités en n’importe quel point de V ∪ ∂ 0 V V\cup\partial_{0}V. Le reste du lemme s’obtient de la même façon, car pour tout m ∈ U m\in U, l’anneau B m = ℝ ⁡ { y − y m } {B}_{m}=\mathbb{R}\{y-y_{m}\} est noethérien.∎

Soit ( χ i, B i) i = 1, 2 (\chi_{i},{B}_{i})_{i=1,2} deux couples tels que B i {B}_{i} est un anneau de référence et χ i \chi_{i} est une dérivation appartenant à Ξ ​ B i \Xi{B}_{i}. Soit U i U_{i} un ouvert admissible pour χ i \chi_{i} et soit φ: U 1 → U 2 \varphi:U_{1}\to U_{2} un difféomorphisme tel que φ ∗ ​ ( χ 1) = χ 2 \varphi_{*}(\chi_{1})=\chi_{2}. On suppose que φ \varphi se prolonge en un homéomorphisme de U 1 ∪ ∂ 0 U 1 U_{1}\cup\partial_{0}U_{1} sur U 2 ∪ ∂ 0 U 2 U_{2}\cup\partial_{0}U_{2} tel que φ ⁡ ( 0) = 0 \varphi(0)=0. On note de la même façon son germe en 0 φ: ( U 1, 0) → ( U 2, 0) \varphi:(U_{1},0)\to(U_{2},0) (ainsi que celui de φ − 1 \varphi^{-1}), et on suppose que φ ∗ ​ ( B 2) = B 1 \varphi^{*}({B}_{2})={B}_{1} (donc φ ∗ \varphi^{*} est un isomorphisme et ( φ ∗) − 1 = ( φ − 1) ∗ (\varphi^{*})^{-1}=(\varphi^{-1})^{*}). Un calcul direct montre que le diagramme suivant est commutatif

 | B 2 → φ ∗ B 1 χ 2 ↓ ↓ χ 1 B 2 → φ ∗ B 1 \begin{CD}{B}_{2}@>{\varphi^{*}}>{}>{B}_{1}\\ @V{\chi_{2}}V{}V@V{}V{\chi_{1}}V\\ {B}_{2}@>{\varphi^{*}}>{}>{B}_{1}\end{CD} |  |

Donc, si f 1 ∈ B 1 f_{1}\in{B}_{1} et f 2 = ( φ − 1) ∗ ​ ( f 1) f_{2}=(\varphi^{-1})^{*}(f_{1}), alors pour tout entier n n

 | χ 1 n ​ f 1 = φ ∗ ​ ( χ 2 n ​ f 2) \chi_{1}^{n}f_{1}=\varphi^{*}(\chi_{2}^{n}f_{2}) |  |

et par conséquent

 | I χ 1, f 1 = φ ∗ ​ ( I χ 2, f 2) I_{\chi_{1},f_{1}}=\varphi^{*}(I_{\chi_{2},f_{2}}) |  |

Ceci est à fortiori vrai aux voisinages de points m 1 ∈ U 1 m_{1}\in U_{1} et m 2 = φ ⁡ ( m 1) ∈ U 2 m_{2}=\varphi(m_{1})\in U_{2}, les anneaux locaux correspondants étant les anneaux de germes de fonctions analytiques en ces points (on les appelle aussi ”anneaux analytiques” pour simplifier). On verra dans la suite des situations plus générales de tels ”transfert”, dont la première est

###### Lemme IB4 (lemme d'isomorphie de Roussarie)

Le faisceau I χ, f ​ [U] {I}_{\chi,f}[U] est compatible avec la projection π χ, U \pi_{\chi,U}. Autrement dit, si γ \gamma est une orbite de χ \chi dans U U, et si m 1, m 2 ∈ γ m_{1},m_{2}\in\gamma, alors les fibres I χ, f, m 1 {I}_{\chi,f,m_{1}} et I χ, f, m 2 {I}_{\chi,f,m_{2}} sont isomorphes, l’isomorphisme étant le germe du flot φ χ, U \varphi_{\chi,U} aux voisinages de m 1 m_{1} et m 2 m_{2}.

Preuve. Soit t 0 t_{0} tel que m 2 = φ χ, U ​ ( t 0, m 1) m_{2}=\varphi_{\chi,U}(t_{0},m_{1}). Soient m 1 ′ ∈ U m^{\prime}_{1}\in U un point voisin de m 1 m_{1}, t t voisin de 0 et m 2 ′ = φ χ, U ​ ( t, m 1 ′) ∈ U m^{\prime}_{2}=\varphi_{\chi,U}(t,m^{\prime}_{1})\in U. Alors, un calcul direct donne

 | f ⁡ ( m 2 ′) = f ⁡ ( φ χ, U ​ ( t, m 1 ′)) = ∑ n ≥ 0 χ n ​ f ​ ( m 1 ′) ​ t n n! f(m^{\prime}_{2})=f(\varphi_{\chi,U}(t,m^{\prime}_{1}))=\sum_{n\geq 0}\chi^{n}f(m^{\prime}_{1})\frac{t^{n}}{n!} |  |

la série étant uniformément convergente sur le produit d’un voisinage de m 1 m_{1} dans U U et d’un voisinage de 0 dans ℝ \mathbb{R} (le flot étant analytique sur ce produit et f f est analytique sur un voisinage de m 1 m_{1}). Les idéaux de germes de fonctions analytiques en un point, sont fermés pour la topologie de la convergence uniforme ([B-M], [H]). Par conséquent, I χ, f, m 1 ⊃ ( φ χ, U ( t,.)) ∗ ( I χ, f, φ χ, U ​ ( t, m 1)) {I}_{\chi,f,m_{1}}\supset(\varphi_{\chi,U}(t,.))^{*}({I}_{\chi,f,\varphi_{\chi,U}(t,m_{1})}), où φ χ, U ( t,.) \varphi_{\chi,U}(t,.) désigne aussi le germe de ce difféomorphisme aux points m 1 m_{1} et φ χ, U ​ ( t, m 1) \varphi_{\chi,U}(t,m_{1}). En considérant le flot inverse ( ( φ χ, U ( t,.)) ∗ (\varphi_{\chi,U}(t,.))^{*} est un isomorphisme entre les anneaux analytiques correspondants), on obtient I χ, f, m 1 = ( φ χ, U ( t,.)) ∗ ( I χ, f, φ χ, U ​ ( t, m 1)) {I}_{\chi,f,m_{1}}=(\varphi_{\chi,U}(t,.))^{*}({I}_{\chi,f,\varphi_{\chi,U}(t,m_{1})}). Et, en utilisant un recouvrement fini du segment d’orbite [m 1, m 2] [m_{1},m_{2}], on obtient

 | I χ, f, m 1 = ( φ χ, U ( t 0,.)) ∗ ( I χ, f, m 2) {I}_{\chi,f,m_{1}}=(\varphi_{\chi,U}(t_{0},.))^{*}({I}_{\chi,f,m_{2}}) |  |

où φ χ, U ( t 0,.) \varphi_{\chi,U}(t_{0},.) désigne aussi le germe aux points m 1 m_{1} et m 2 m_{2} de ce difféomorphisme.∎

Soit U ∈ ( ( ℝ + ⁣ ∗) p × ℝ q, 0) U\in((\mathbb{R}^{+*})^{p}\times\mathbb{R}^{q},0) et soit c: m ∈ U ↦ m ′ ∈ ℝ n c:m\in U\mapsto m^{\prime}\in\mathbb{R}^{n} un morphisme continu sur U ∪ ∂ 0 U U\cup\partial_{0}U tel que c ⁡ ( 0) = 0 c(0)=0. On note de la même façon son germe c: ( U, 0) → ( ℝ n, 0) c:(U,0)\to(\mathbb{R}^{n},0). Soit u u une coordonnée locale sur ( ℝ n, 0) (\mathbb{R}^{n},0). L’anneau B = c ∗ ​ ( ℝ ​ { u }) {B}=c^{*}(\mathbb{R}\{u\}) est dit anneau restriction analytique (ou encore anneau convergent). Il est isomorphe à l’anneau restriction de référence ℝ { u } | c ( U) \mathbb{R}\{u\}_{|c(U)}. Il est clair que c’est un anneau local et noethérien (l’image réciproque par c ∗ c^{*} de tout idéal est un idéal, et l’anneau ℝ ​ { u } \mathbb{R}\{u\} est noethérien). Soit y = ( x, α) y=(x,\alpha) des coordonnées sur U U, on suppose maintenant que le morphisme c c est analytique, et qu’il s’écrit dans les coordonnées y y et u u

 | u = c ⁡ ( y) = ( y, ψ ⁡ ( y)) u=c(y)=(y,\psi(y)) |  |

On suppose aussi que pour tout i = 1, …, n − ( p + q), j = 1, …, p + q i=1,\ldots,n-(p+q),\ j=1,\ldots,p+q, il existe h i, j ∈ ℝ ​ { u } h_{i,j}\in\mathbb{R}\{u\} tel que

 | ∏ k = 1 p x k ​ ∂ ψ i ∂ y j = c ∗ ​ ( h i, j) \prod_{k=1}^{p}x_{k}\frac{\partial\psi_{i}}{\partial y_{j}}=c^{*}(h_{i,j}) |  |

Dans ce cas, on vérifie facilement que l’anneau convergent B {B} est un anneau de référence. Soit

 | χ = ∑ j = 1 p + q a j ​ ∂ ∂ y j ∈ Ξ ​ B \chi=\sum_{j=1}^{p+q}a_{j}\frac{\partial}{\partial y_{j}}\in\Xi{B} |  |

Pour tout i = 1, …, n i=1,\ldots,n, le germe g i ​ ( u) = u i ∈ ℝ ⁡ { u } g_{i}(u)=u_{i}\in\mathbb{R}\{u\}, donc c ∗ ​ ( g i) ∈ B c^{*}(g_{i})\in{B} et par conséquent χ ​ c ∗ ​ ( g i) ∈ B \chi c^{*}(g_{i})\in{B} (en particulier, pour i = 1, …, p + q i=1,\ldots,p+q, on a χ ​ c ∗ ​ ( g i) = a i \chi c^{*}(g_{i})=a_{i}), il existe alors h i ∈ ℝ ​ { u } h_{i}\in\mathbb{R}\{u\} (il n’est pas unique en général!) tel que χ ​ c ∗ ​ ( g i) = c ∗ ​ ( h i) \chi c^{*}(g_{i})=c^{*}(h_{i}). Soit U ′ ⊂ U U^{\prime}\subset U un ouvert admissible pour χ \chi tel que les germes h i h_{i} soient réalisés sur un ouvert U ∈ ( ℝ n, 0) {U}\in(\mathbb{R}^{n},0) et contenant c ⁡ ( U ′) c(U^{\prime}). Soit

 | X = ∑ i = 1 n h i ​ ∂ ∂ u i {X}=\sum_{i=1}^{n}h_{i}\frac{\partial}{\partial u_{i}} |  |

c’est une dérivation analytique réalisée sur U {U}. Le morphisme c c est un difféomorphisme de U ′ U^{\prime} sur la variété analytique c ⁡ ( U ′) c(U^{\prime}) ( c c est une immersion), et par la construction de X {X}, on a

 | c ∗ χ = X | c ( U ′) c_{*}\chi={X}_{|c(U^{\prime})} |  | ∗ |

(on note encore de la même façon le difféomorphisme associé à c c, et son germe en 0). Ainsi, le diagramme suivant est commutatif

 | ℝ ​ { u } → c ∗ B X ↓ ↓ χ ℝ ​ { u } → c ∗ B \begin{CD}\mathbb{R}\{u\}@>{c^{*}}>{}>{B}\\ @V{{X}}V{}V@V{}V{\chi}V\\ \mathbb{R}\{u\}@>{c^{*}}>{}>{B}\end{CD} |  |

Le difféomorphisme c c se prolonge en un homéomorphisme de U ′ ∪ ∂ 0 U ′ U^{\prime}\cup\partial_{0}U^{\prime} sur son image. Soit m ∈ ∂ 0 U ′ m\in\partial_{0}U^{\prime} et m ′ = c ⁡ ( m) m^{\prime}=c(m), on note c m: ( U ′, m) → ( ℝ n, m ′) c_{m}:(U^{\prime},m)\to(\mathbb{R}^{n},m^{\prime}) le germe de c c aux points m m et m ′ m^{\prime}. Soit ℝ ​ { u − u m ′ } \mathbb{R}\{u-u_{m^{\prime}}\} l’anneau analytique local au point m ′ m^{\prime}, et soit B m = c m ∗ ​ ( ℝ ⁡ { u − u m ′ }) {B}_{m}=c_{m}^{*}(\mathbb{R}\{u-u_{m^{\prime}}\}), c’est un anneau restriction analytique qui est un anneau de référence (par les mêmes raisonnements que ci-dessus, en supposant bien sûr que les germes h i, j h_{i,j} sont réalisés sur U {U}). Il est clair qu’il contient les germes en m m d’éléments de B {B} représentés sur un voisinage de m m. De plus, il est stable par la dérivation χ m \chi_{m} (par la commutativité du digramme obtenu à partir de la relation ( ∗) (*) germifiée aux points m m et m ′ m^{\prime}).

Ainsi, pour tout f ∈ B f\in{B} réalisée sur un certain ouvert V ∈ ( U, 0) V\in(U,0) (et V ⊂ U ′ V\subset U^{\prime}), le lemme de cohérence dit que le faisceau I χ, f ​ [V ∪ ∂ 0 V] {I}_{\chi,f}[V\cup\partial_{0}V] est cohérent. Par la continuité de la dérivation χ \chi et du morphisme c c sur le bord ∂ 0 U ′ \partial_{0}U^{\prime}, l’image par c c d’une orbite régulière de χ \chi incluse dans le bord, est une partie connexe d’une orbite régulière de X {X} dans U {U}. Le lemme d’isomorphie s’applique aux faisceaux différentiels I X, g ​ [U g] {I}_{{X},g}[{U}_{g}] le long de toute orbite régulière ( U g ⊂ U {U}_{g}\subset{U} étant un un voisinage ouvert de 0, sur lequel g g est représentée). Ainsi, en transportant par le morphisme c ∗ c^{*}, on obtient que le lemme d’isomorphie s’apllique aussi aux faisceaux I χ, f ​ [V ∪ ∂ 0 V] {I}_{\chi,f}[V\cup\partial_{0}V] le long d’orbites régulières incluses dans le bord. En général dans ce travail, le morphisme c c est une immersion dont l’image est le graphe de fonctions élémentaires (et simples!) de Khovanski. Un exemple, déjà rencontré, de tels anneaux convergents, est l’anneau Q ​ R ​ H c ​ v ​ g p, q QR{H}^{p,q}_{cvg} (pour lequel le morphisme c ∗ c^{*} est un isomorphisme (cf. Section II)).

Si l’une des dérivations X {X} satisfait à l’hypothèse ( i ​ i ​ i) (iii) du lemme d’extension (on bien si elle admet ( n − 1) (n-1) intégrales premières analytiques et indépendantes), alors ce lemme dit que l’algèbre ℝ ​ { u } \mathbb{R}\{u\} est X {X} -finie. Il est clair, dans ce cas, que l’anneau convergent B {B} est aussi χ \chi -fini: si f ∈ B f\in{B} et si g ∈ ℝ ​ { u } g\in\mathbb{R}\{u\} est tel que f = c ∗ ​ ( g) f=c^{*}(g), alors par transport par l’injection c c

 | d ° ​ π χ | Z ⁡ ( f) ≤ d ° ​ π X | Z ⁡ ( g) d^{°}\pi_{\chi|Z(f)}\leq d^{°}\pi_{{X}|Z(g)} |  |

Idéal χ \chi -transverse.

Soit B {B} un anneau de référence. Soient f ∈ B f\in{B} et χ ∈ Ξ ​ B \chi\in\Xi{B}. Soit U U un ouvert admissible sur lequel f f est réalisée. Soit γ \gamma une orbite régulière de χ \chi dans U U. Soient m, m ′ ∈ γ m,m^{\prime}\in\gamma et t 0 > 0 t_{0}>0 tel que φ χ, U ​ ( t 0, m) = m ′ \varphi_{\chi,U}(t_{0},m)=m^{\prime}. Soit σ m ⊂ U \sigma_{m}\subset U une transversale à γ \gamma en m m, analytique. Quitte à réduire σ m \sigma_{m}, on suppose que pour t t dans un voisinage de [0, t 0] [0,t_{0}], l’image de σ m \sigma_{m} par le flot φ χ, U ( t,.) \varphi_{\chi,U}(t,.) est incluse dans U U. Ainsi, σ m ′ = φ χ, U ​ ( t 0, σ m) \sigma_{m^{\prime}}=\varphi_{\chi,U}(t_{0},\sigma_{m}) est une transversale à γ \gamma en m ′ m^{\prime}, analytique. Soient β \beta des coordonnées analytiques locales sur ( σ m, m) (\sigma_{m},m), il est clair que l’anneau restriction de référence ℝ { y − y m } | σ m \mathbb{R}\{y-y_{m}\}_{|\sigma_{m}} est isomorphe à l’anneau analytique ℝ ​ { β } \mathbb{R}\{\beta\} (qui lui même est isomorphe à l’anneau des intégrales premières analytiques locales en m m (cf. ci-dessous)). Par le difféomorphisme analytique φ χ, U ( t 0,.) \varphi_{\chi,U}(t_{0},.), on peut prendre β \beta comme coordonnées analytiques locales sur ( σ m ′, m ′) (\sigma_{m^{\prime}},m^{\prime}). Par cette identification, le lemme d’isomorphie dit alors que i σ m ∗ ​ ( I χ, f, m) = i σ m ′ ∗ ​ ( I χ, f, m ′) i^{*}_{\sigma_{m}}({I}_{\chi,f,m})=i^{*}_{\sigma_{m^{\prime}}}({I}_{\chi,f,m^{\prime}}), d’où

###### Définition IB6

On appelle idéal χ \chi - transverse de f f le long de γ \gamma l’idéal restriction

 | J χ, f, γ = i σ m ∗ ​ ( I χ, f, m) = I χ, f, m | σ m ⊂ ℝ ⁡ { β } ∀ m ∈ γ J_{\chi,f,\gamma}=i^{*}_{\sigma_{m}}({I}_{\chi,f,m})={I}_{\chi,f,m|\sigma_{m}}\subset\mathbb{R}\{\beta\}\quad\forall m\in\gamma |  |

où les coordonnées analytiques β \beta sur σ m \sigma_{m} sont des intégrales premières de χ \chi le long de γ \gamma.

Et inversement, on peut reconstruire toute fibre I χ, f, m {I}_{\chi,f,m} le long de γ \gamma à partir de l’idéal transverse J χ, f, γ J_{\chi,f,\gamma}: soit U m ⊂ U U_{m}\subset U le saturé de σ m \sigma_{m} par le flot φ χ, U ( t,.) \varphi_{\chi,U}(t,.) pour t t dans un voisinage de 0. Il est clair que l’espace quotient U m ~ = U m / φ χ m, U m \widetilde{U_{m}}=U_{m}/\varphi_{\chi_{m},U_{m}} s’identifie à la transversale analytique σ m \sigma_{m}. Ainsi, on peut parler du germe de la projection intégrale π χ m, U m: U m → σ m \pi_{\chi_{m},U_{m}}:U_{m}\to\sigma_{m}, qu’on note simplement π χ m: ( U m, m) → ( σ m, m) \pi_{\chi_{m}}:(U_{m},m)\to(\sigma_{m},m). On lui associe le morphisme étoilé π χ m ∗: ℝ ⁡ { β } → ℝ ⁡ { y − y m } \pi_{\chi_{m}}^{*}:\mathbb{R}\{\beta\}\to\mathbb{R}\{y-y_{m}\} qui est injectif; son image est l’anneau des intégrales premières analytiques locales en m m. Avant de poursuivre, faisons une remarque simple qui sera souvent utilisée dans la suite: soient ψ 1 ∗, ψ 2 ∗ \psi_{1}^{*},\psi_{2}^{*} deux morphismes étoilés, et soit I I un idéal, alors l’idéal prolongé (par ψ 1 ∗ \psi_{1}^{*}) associé à l’idéal prolongé (par ψ 2 ∗ \psi_{2}^{*}) associé à I I, coincide avec l’idéal prolongé (par ( ψ 2 ∘ ψ 1) ∗ (\psi_{2}\circ\psi_{1})^{*}) associé à I I, ce que l’on note ( ψ 2 ∘ ψ 1) ∗ ​ ( I) = ψ 1 ∗ ∘ ψ 2 ∗ ​ ( I) (\psi_{2}\circ\psi_{1})^{*}(I)=\psi_{1}^{*}\circ\psi_{2}^{*}(I).

###### Lemme IB5 (lemme de saturation)

Pour tout m ∈ γ m\in\gamma, on a I χ, f, m = π χ m ∗ ​ ( J χ, f, γ) \quad{I}_{\chi,f,m}=\pi^{*}_{\chi_{m}}(J_{\chi,f,\gamma}).

Preuve. On se place dans un flow-box au voisinage de m m. Quitte à réduire U m U_{m}, soit ψ: ( t, β) ∈ τ × Σ m ↦ m ′ ∈ U m \psi:(t,\beta)\in\tau\times\Sigma_{m}\mapsto m^{\prime}\in U_{m} le difféomorphisme normalisant tel que ψ ⁡ ( { 0 } × Σ m) = σ m \psi(\{0\}\times\Sigma_{m})=\sigma_{m} et ( ψ − 1) ∗ ​ ( χ m) = Y = ∂ / ∂ t (\psi^{-1})_{*}(\chi_{m})={Y}=\partial/\partial t. Notons de la même façon son germe ψ: ( τ × Σ, ( 0, 0)) → ( U m, m) \psi:(\tau\times\Sigma,(0,0))\to(U_{m},m). On a le diagramme commutatif

 | ℝ ​ { y − y m } → ψ ∗ ℝ ​ { t, β } χ m ↓ ↓ Y ℝ ​ { y − y m } → ψ ∗ ℝ ​ { t, β } \begin{CD}\mathbb{R}\{y-y_{m}\}@>{\psi^{*}}>{}>\mathbb{R}\{t,\beta\}\\ @V{\chi_{m}}V{}V@V{}V{{Y}}V\\ \mathbb{R}\{y-y_{m}\}@>{\psi^{*}}>{}>\mathbb{R}\{t,\beta\}\end{CD} |  | ∗ |

où ψ ∗ \psi^{*} est un isomorphisme. L’orbite γ ∩ U m \gamma\cap U_{m} est envoyée sur l’orbite Γ = τ × { 0 } \Gamma=\tau\times\{0\}. Notons ψ 1: Σ m → σ m \psi_{1}:\Sigma_{m}\to\sigma_{m} (et son germe aux points 0 et m m) la restriction de ψ \psi à { 0 } × Σ m \{0\}\times\Sigma_{m}. C’est un difféomorphisme. La projection intégrale π Y, τ × Σ m \pi_{{Y},\tau\times\Sigma_{m}} s’identifie avec la projection canonique π: τ × Σ m → Σ m \pi:\tau\times\Sigma_{m}\to\Sigma_{m}; notons de la même façon son germe π: ( τ × Σ m, ( 0, 0)) → ( Σ m, 0) \pi:(\tau\times\Sigma_{m},(0,0))\to(\Sigma_{m},0). Les diagrammes suivants est commutatifs

 | ( τ × Σ m, ( 0, 0)) → ψ ( U m, m) π ↓ ↓ π χ m ( Σ m, 0) → ψ 1 ( σ m, m) \begin{CD}(\tau\times\Sigma_{m},(0,0))@>{\psi}>{}>(U_{m},m)\\ @V{\pi}V{}V@V{}V{\pi_{\chi_{m}}}V\\ (\Sigma_{m},0)@>{\psi_{1}}>{}>(\sigma_{m},m)\end{CD} |  | ∗ ∗ 1 |

 | ( Σ m, 0) → ψ 1 ( σ m, m) i Σ m ↓ ↓ i σ m ( τ × Σ m, ( 0, 0)) → ψ U m \begin{CD}(\Sigma_{m},0)@>{\psi_{1}}>{}>(\sigma_{m},m)\\ @V{i_{\Sigma_{m}}}V{}V@V{}V{i_{\sigma_{m}}}V\\ (\tau\times\Sigma_{m},(0,0))@>{\psi}>{}>U_{m}\end{CD} |  | ∗ ∗ 2 |

Par le choix des coordonnées β \beta sur Σ m \Sigma_{m} et σ m \sigma_{m}, le morphisme étoilé ψ 1 ∗ \psi_{1}^{*} est l’identité de l’anneau ℝ ​ { β } \mathbb{R}\{\beta\}; on a donc les diagrammes commutatifs

 | ℝ ​ { β } → i ​ d ℝ ​ { β } π χ m ∗ ↓ ↓ π ∗ ℝ ​ { y − y m } → ψ ∗ ℝ ​ { t, β } \begin{CD}\mathbb{R}\{\beta\}@>{id}>{}>\mathbb{R}\{\beta\}\\ @V{\pi_{\chi_{m}}^{*}}V{}V@V{}V{\pi^{*}}V\\ \mathbb{R}\{y-y_{m}\}@>{\psi^{*}}>{}>\mathbb{R}\{t,\beta\}\end{CD} |  | ∗ ∗ ∗ 1 |

 | ℝ ​ { y − y m } → ψ ∗ ℝ ​ { t, β } i σ m ∗ ↓ ↓ i Σ m ∗ ℝ ​ { β } → i ​ d ℝ ​ { β } \begin{CD}\mathbb{R}\{y-y_{m}\}@>{\psi^{*}}>{}>\mathbb{R}\{t,\beta\}\\ @V{i_{\sigma_{m}}^{*}}V{}V@V{}V{i_{\Sigma_{m}}^{*}}V\\ \mathbb{R}\{\beta\}@>{id}>{}>\mathbb{R}\{\beta\}\end{CD} |  | ∗ ∗ ∗ 2 |

Ces deux derniers diagrammes sont aussi valables pour les idéaux prolongés. Soit F = ψ ∗ ​ ( f m) = ∑ a n ​ ( β) ​ t n F=\psi^{*}(f_{m})=\sum a_{n}(\beta)t^{n}, d’après le diagramme ( ∗) (*), on a ψ ∗ ​ ( I χ, f, m) = I Y, F ⊂ ℝ ⁡ { t, β } \psi^{*}({I}_{\chi,f,m})=I_{Y,F}\subset\mathbb{R}\{t,\beta\}. D’après la définition de l’idéal transverse

 | OPEN J Y, F, Γ = i Σ m) ∗ ​ ( I Y, F) = i Σ m ∗ ∘ ψ ∗ ​ ( I χ, f, m) J_{{Y},F,\Gamma}=i_{\Sigma_{m}})^{*}(I_{{Y},F})=i_{\Sigma_{m}}^{*}\circ\psi^{*}({I}_{\chi,f,m}) |  |

Et d’après le diagramme ( ∗ ∗ ∗ 2) (***2), on a J Y, F, Γ = i σ m ∗ ​ ( I χ, f, m) = J χ, f, γ J_{{Y},F,\Gamma}=i_{\sigma_{m}}^{*}({I}_{\chi,f,m})=J_{\chi,f,\gamma}. Donc, d’après le diagramme ( ∗ ∗ ∗ 1) (***1), il suffit de montrer que I Y, F = π ∗ ​ ( J Y, F, Γ) I_{Y,F}=\pi^{*}(J_{{Y},F,\Gamma}). Par sa définition, on vérifie facilement que J Y, F, Γ = ⟨ a n; n ∈ ℕ ⟩ J_{{Y},F,\Gamma}=\langle a_{n};\ n\in\mathbb{N}\rangle (d’où le nom d’ idéal des coefficients attribué par Roussarie à cet idéal). Soit M {M} l’idéal maximal de ℝ ​ { t, β } \mathbb{R}\{t,\beta\}. Notons F n = 𝕛 t n ​ ( F) F_{n}={\mathbb{j}}^{n}_{t}(F). On a F n ∈ π ∗ ​ ( J Y, F, Γ) F_{n}\in\pi^{*}(J_{Y,F,\Gamma}) et F − F n ∈ M n F-F_{n}\in{M}^{n} pour tout n n. Donc, par le théorème d’intersection de Krull ([L]), F ∈ π ∗ ​ ( J Y, F, Γ) F\in\pi^{*}(J_{Y,F,\Gamma}). Comme l’idéal prolongé π ∗ ​ ( J Y, F, Γ) \pi^{*}(J_{{Y},F,\Gamma}) est stable par la dérivation Y {Y}, on obtient I Y, F ⊂ π ∗ ​ ( J Y, F, Γ CLOSE I_{{Y},F}\subset\pi^{*}(J_{{Y},F,\Gamma}. Inversement, pour tout n ∈ ℕ n\in\mathbb{N}, on a Y n ​ F = n! ​ a n + t ​ H n {Y}^{n}F=n!a_{n}+tH_{n} avec H n ∈ π ∗ ​ ( J Y, F, Γ) H_{n}\in\pi^{*}(J_{{Y},F,\Gamma}) (par le même raisonnement que pour F F, en utilisant la série de F F). Donc, pour tout n n, a n ( = π ∗ ​ ( a n)) ∈ I Y, F + M ​ π ∗ ​ ( J Y, F, Γ) a_{n}(=\pi^{*}(a_{n}))\in I_{{Y},F}+{M}\pi^{*}(J_{{Y},F,\Gamma}). Par conséquent

 | π ∗ ​ ( J Y, F, Γ) ⊂ I Y, F + M ​ π ∗ ​ ( J Y, F, Γ) \pi^{*}(J_{{Y},F,\Gamma})\subset I_{{Y},F}+{M}\pi^{*}(J_{{Y},F,\Gamma}) |  |

Et, par le lemme de Nakayama ([L]), on obtient π ∗ ​ ( J Y, F, Γ) ⊂ I Y, F \pi^{*}(J_{{Y},F,\Gamma})\subset I_{{Y},F}.∎

Orbite principale et la double inclusion.

Si l’orbite γ \gamma adhère à 0 0, et s’il existe une notion de germe de la projection intégrale π χ, U \pi_{\chi,U} en 0 (qu’on notera π χ \pi_{\chi}), il se pose alors la question de comparer la fibre en 0 I χ, f I_{\chi,f} et l’idéal π χ ∗ ​ ( J χ, f, γ) \pi^{*}_{\chi}(J_{\chi,f,\gamma}) (dans une extension commune aux anneaux π χ ∗ ​ ( ℝ ⁡ { β }) \pi_{\chi}^{*}(\mathbb{R}\{\beta\}) et B {B}). Intuitivement, il est tout à fait légitime d’espérer établir la double inclusion

 | ( ∏ j = 1 p x j) N ​ π χ ∗ ​ ( J χ, f, γ) ⊂ I χ, f ⊂ π χ ∗ ​ ( J χ, f, γ) (\prod_{j=1}^{p}x_{j})^{N}\pi^{*}_{\chi}(J_{\chi,f,\gamma})\subset I_{\chi,f}\subset\pi^{*}_{\chi}(J_{\chi,f,\gamma}) |  |

qui relaxe l’égalité du lemme de saturation, et qui s’inspire du Nullstelenzats d’Hilbert ([L]). Dans ce cas, il est nécessaire d’avoir l’égalité

 | Z ⁡ ( I χ, f) = π χ − 1 ​ ( Z ⁡ ( J χ, f, γ)) Z(I_{\chi,f})=\pi^{-1}_{\chi}(Z(J_{\chi,f,\gamma})) |  |

(cf. formule (1)). Et pour cela, il suffit que γ \gamma soit ”principale” dans U U

###### Définition IB7

Soit γ \gamma une orbite de χ \chi dans U U. Elle est dite principale dans U U si

Ainsi, l’orbite principale γ \gamma est la seule orbite de χ \chi dans U U qui adhère à 0. C’est donc la seule orbite principale de χ \chi dans U U. Pour σ ⊂ σ 0 \sigma\subset\sigma_{0}, notons U σ = φ χ, U (., σ) U_{\sigma}=\varphi_{\chi,U}(.,\sigma), c’est un voisinage ouvert de 0, qui est une union d’orbites de χ \chi dans U U (c’est un ouvert admissible). L’espace quotient U σ ~ \widetilde{U_{\sigma}} s’identifie donc à un sous-espace de U ~ \widetilde{U}. Par conséquent, le morphisme π χ, U σ: U σ → U σ ~ \pi_{\chi,U_{\sigma}}:U_{\sigma}\to\widetilde{U_{\sigma}} est simplement la restriction à U σ U_{\sigma} du morphisme π χ, U \pi_{\chi,U}. Par la définition de U σ U_{\sigma}, et par la condition ( i ​ i) (ii), l’espace U σ ~ \widetilde{U_{\sigma}} s’identifie à la transversale analytique σ \sigma. Par la condition ( i ​ i ​ i) (iii), le morphisme π χ, U σ \pi_{\chi,U_{\sigma}} se prolonge continûment à U σ ∪ { 0 } U_{\sigma}\cup\{0\} en posant π χ, U σ ​ ( 0) = γ ∩ σ \pi_{\chi,U_{\sigma}}(0)=\gamma\cap\sigma. On peut donc parler du germe en 0 du morphisme π χ, U \pi_{\chi,U} comme étant celui du morphisme π χ, U σ: U σ → σ \pi_{\chi,U_{\sigma}}:U_{\sigma}\to\sigma aux points 0 et γ ∩ σ \gamma\cap\sigma. Ce germe est indépendant de la transversale σ ⊂ σ 0 \sigma\subset\sigma_{0}; on le note π χ \pi_{\chi}. L’existence d’une orbite principale γ \gamma implique en particulier l’existence de ( p + q − 1) (p+q-1) intégrales premières analytiques et indépendantes: si β \beta sont des coordonnées analytiques sur σ 0 \sigma_{0}, et si on pose g j ​ ( β) = β j g_{j}(\beta)=\beta_{j}, les germes G j = π χ ∗ ​ ( g j) G_{j}=\pi_{\chi}^{*}(g_{j}) admettent des représentants F j F_{j} sur U σ 0 U_{\sigma_{0}}, qui sont des intégrales premières de χ \chi, analytiques et indépendantes.

Autre cas de transfert.

On en a vu beaucoup, et on verra beaucoup. La première apparition de chaque nouveau cas sera traîtée en détail. Un cas assez général, et abondamment employé dans la suite est le suivant: pour i = 1, 2 i=1,2, soit B i ⊂ A p i, q i {B}_{i}\subset{A}^{p_{i},q_{i}} un anneau de référence. Soit χ i ∈ Ξ ​ B i \chi_{i}\in\Xi{B}_{i} une dérivation, et U i U_{i} un ouvert admissible pour χ i \chi_{i}. On suppose que chaque dérivation χ i \chi_{i} admet une orbite principale γ i \gamma_{i} dans U i U_{i}. Pour simplifier, supposons que U i U_{i} est le saturé d’une transversale analytique σ i \sigma_{i}, comme ci-dessus (quitte à réduire U i U_{i}). Soit W i ⊂ σ i W_{i}\subset\sigma_{i} une sous-variété analytique contenant le point m i = γ i ∩ σ i m_{i}=\gamma_{i}\cap\sigma_{i}, et soit V i = π χ, U i − 1 ​ ( W i) V_{i}=\pi_{\chi,U_{i}}^{-1}(W_{i}), c’est une sous-variété analytique de U i U_{i}, qui adhère à 0, et qui est invariante par χ i \chi_{i}.

Notons Y i = χ i | ( V i, 0) {Y}_{i}=\chi_{i|(V_{i},0)}. En utilisant le flot de Y i {Y}_{i}, on montre facilement que Y i ​ ( B i | V i) ⊂ B i | V i {Y}_{i}({B}_{i|V_{i}})\subset{B}_{i|V_{i}}. Soit Ψ: V 2 → V 1 \Psi:V_{2}\to V_{1} un difféomorphisme analytique, continue en 0 avec Ψ ⁡ ( 0) = 0 \Psi(0)=0. On note de la même façon son germe Ψ: ( V 2, 0) → ( V 1, 0) \Psi:(V_{2},0)\to(V_{1},0). On suppose que Ψ ∗ ​ Y 2 = Y 1 \Psi_{*}{Y}_{2}={Y}_{1}, et que Ψ ∗ ​ ( B 1 | V 1) ↪ B 2 | V 2 \Psi^{*}({B}_{1|V_{1}})\hookrightarrow{B}_{2|V_{2}}. Dans ce cas, le diagramme suivant est commutatif

 | B 1 | V 1 → Ψ ∗ B 2 | V 2 Y 1 ↓ ↓ Y 2 B 1 | V 1 → Ψ ∗ B 2 | V 2 \begin{CD}{B}_{1|V_{1}}@>{\Psi^{*}}>{}>{B}_{2|V_{2}}\\ @V{{Y}_{1}}V{}V@V{}V{{Y}_{2}}V\\ {B}_{1|V_{1}}@>{\Psi^{*}}>{}>{B}_{2|V_{2}}\end{CD} |  | ∗ |

Une orbite principale étant la seule qui adhère à 0, et Ψ \Psi étant continue en 0, on a Ψ ⁡ ( γ 2) = γ 1 \Psi(\gamma_{2})=\gamma_{1}. Comme Ψ \Psi est un difféomorphisme qui préserve les orbites, on peut supposer, pour simplifier que Ψ ⁡ ( W 2) = W 1 \Psi(W_{2})=W_{1} (quitte à déplacer les transversales σ i \sigma_{i}). Notons ψ: W 2 → W 1 \psi:W_{2}\to W_{1} la restriction de Ψ \Psi à W 2 W_{2}. C’est un difféomorphisme analytique, et on note de la même façon son germe ψ: ( W 2, m 2) → ( W 1, m 1) \psi:(W_{2},m_{2})\to(W_{1},m_{1}). Soit V m i V_{m_{i}} un saturé suffisament petit, de W i W_{i} par le flot de Y i {Y}_{i}, et soit π Y i, m i \pi_{{Y}_{i},m_{i}} le germe en m i m_{i} de la projection intégrale. Le diagramme suivant est commutatif

 | ( V m 2, m 2) → Ψ m 2 ( V m 1, m 1) π C ​ a ​ l ​ Y 2, m 2 ↓ ↓ π Y 1, m 1 ( W 2, m 2) → ψ ( W 1, m 1) \begin{CD}(V_{m_{2}},m_{2})@>{\Psi_{m_{2}}}>{}>(V_{m_{1}},m_{1})\\ @V{\pi_{{CalY}_{2},m_{2}}}V{}V@V{}V{\pi_{{Y}_{1},m_{1}}}V\\ (W_{2},m_{2})@>{\psi}>{}>(W_{1},m_{1})\end{CD} |  | ∗ ⁣ ∗ |

La variété W i W_{i} est analytique en m i m_{i}. Donc, par un bon choix de coordonnées analytiques locales ( β i, β i ′) (\beta_{i},\beta^{\prime}_{i}) sur ( σ i, m i) (\sigma_{i},m_{i}) (dans lesquelles ( W i, m i) (W_{i},m_{i}) est un graphe), on obtient que l’anneau local ℝ { β i, β i ′ } | W i \mathbb{R}\{\beta_{i},\beta^{\prime}_{i}\}_{|W_{i}} sur ( W i, m i) (W_{i},m_{i}), est isomorphe à l’anneau analytique ℝ ​ { β i } \mathbb{R}\{\beta_{i}\}. On obtient alors le diagramme commutatif à partir du diagramme ci-dessus

 | ℝ ​ { β 1 } → ψ ∗ ℝ ​ { β 2 } π Y 1, m 1 ∗ ↓ ↓ π Y 2, m 2 ∗ B 1, m 1 | V m 1 → Ψ m 2 ∗ B 2, m 2 | V m 2 \begin{CD}\mathbb{R}\{\beta_{1}\}@>{\psi^{*}}>{}>\mathbb{R}\{\beta_{2}\}\\ @V{\pi_{{Y}_{1},m_{1}}^{*}}V{}V@V{}V{\pi_{{Y}_{2},m_{2}}^{*}}V\\ {B}_{1,m_{1}|V_{m_{1}}}@>{\Psi_{m_{2}}^{*}}>{}>{B}_{2,m_{2}|V_{m_{2}}}\end{CD} |  | ∗ ∗ ∗ |

Les variétés V i V_{i} étant analytiques en m i m_{i}, les anneaux locaux B i, m i | V m i {B}_{i,m_{i}|V_{m_{i}}} sont aussi isomorphes à des anneaux analytiques.

###### Lemme IB6 (lemme de transfert)

Soit f 1 ∈ B 1 f_{1}\in{B}_{1} et f 2 ∈ B 2 f_{2}\in{B}_{2} tel que f 2 | V 2 = Ψ ∗ ​ ( f 1 | V 1) f_{2|V_{2}}=\Psi^{*}(f_{1|V_{1}}). On a les égalités suivantes

Preuve. Enlevons l’indice i i pour un moment. Pour l’égalité ( a) (a), par définition d’une restriction, on a J χ, f, γ | W = i W, σ ∗ ​ ( J χ, f, γ) J_{\chi,f,\gamma|W}=i_{W,\sigma}^{*}(J_{\chi,f,\gamma}). Et par définition de l’idéal transverse, on a J χ, f, γ = i σ, U m ∗ ​ ( I χ, f, m) J_{\chi,f,\gamma}=i_{\sigma,U_{m}}^{*}({I}_{\chi,f,m}), où U m U_{m} est un saturé suffisament petit, de σ \sigma par le flot de χ \chi. D’un autre côté, on a I χ, f, m | V m = i V m, U m ∗ ​ ( I χ, f, m) {I}_{\chi,f,m|V_{m}}=i_{V_{m},U_{m}}^{*}({I}_{\chi,f,m}). Et, on vérifie facilement que i W, σ ∗ ∘ i σ, U m ∗ = i W, V m ∗ ∘ i V m, U m ∗ i_{W,\sigma}^{*}\circ i_{\sigma,U_{m}}^{*}=i_{W,V_{m}}^{*}\circ i_{V_{m},U_{m}}^{*}.

Pour l’égalité ( b) (b), par le lemme de saturation, on a

 | I χ, f, m | V m = i V m, U m ∗ ∘ π χ m ∗ ​ ( J χ, f, γ) {I}_{\chi,f,m|V_{m}}=i_{V_{m},U_{m}}^{*}\circ\pi_{\chi_{m}}^{*}(J_{\chi,f,\gamma}) |  |

D’un autre côté, on a π Y m ∗ ​ ( J χ, f, γ | W) = π Y m ∗ ∘ i W, σ ∗ ​ ( J χ, f, γ) \pi_{{Y}_{m}}^{*}(J_{\chi,f,\gamma|W})=\pi_{{Y}_{m}}^{*}\circ i_{W,\sigma}^{*}(J_{\chi,f,\gamma}). Et, on vérifie facilement que les morphismes π χ m ∘ i V m, U m: V m → σ \pi_{\chi_{m}}\circ i_{V_{m},U_{m}}:V_{m}\to\sigma et i W, σ ∘ π Y m: V m → σ i_{W,\sigma}\circ\pi_{{Y}_{m}}:V_{m}\to\sigma, coincident.

Notons g i = f i, | V i g_{i}=f_{i,|V_{i}}. Il est clair que I χ i, f i | V i = I Y i, g i I_{\chi_{i},f_{i}|V_{i}}=I_{{Y}_{i},g_{i}}, et ceci est encore vrai germifié en n’importe quel point de V i V_{i}. L’égalité ( c) (c) est donc une conséquence immédiate de la commutativité du diagramme ( ∗) (*). Pour l’égalité ( d) (d), on utilise l’égalité ( a) (a)

 | J χ 2, f 2, γ 2 | W 2 = i W 2, V 2, m 2 ∗ ​ ( I χ 2, f 2, m 2 | V 2, m 2) J_{\chi_{2},f_{2},\gamma_{2}|W_{2}}=i_{W_{2},V_{2,m_{2}}}^{*}({I}_{\chi_{2},f_{2},m_{2}|V_{2,m_{2}}}) |  |

puis la relation ( c) (c) germifiée aux points m 1 m_{1} et m 2 m_{2}

 | ( I χ 2, f 2, m 2 | V 2, m 2 = Ψ m 2 ∗ ​ ( I χ 1, f 1, m 1 | V 1, m 1) CLOSE ({I}_{\chi_{2},f_{2},m_{2}|V_{2,m_{2}}}=\Psi_{m_{2}}^{*}({I}_{\chi_{1},f_{1},m_{1}|V_{1,m_{1}}}) |  |

et enfin, l’égalité ( b) (b) pour obtenir

 | J χ 2, f 2, γ 2 | W 2 = i W 2, V 2, m 2 ∗ ∘ Ψ m 2 ∗ ∘ π Y 1, m 1 ∗ ​ ( J χ 1, f 1, γ 1 | W 1) J_{\chi_{2},f_{2},\gamma_{2}|W_{2}}=i_{W_{2},V_{2,m_{2}}}^{*}\circ\Psi_{m_{2}}^{*}\circ\pi_{{Y}_{1},m_{1}}^{*}(J_{\chi_{1},f_{1},\gamma_{1}|W_{1}}) |  |

La composition de morphismes étoilés passe aux idéaux prolongés. On conclut en utilisant la commutativité du diagramme ( ∗ ∗ ∗) (***), et la relation π Y 2, m 2 ∘ i W 2, V 2, m 2 = i ​ d W 2 \pi_{{Y}_{2},m_{2}}\circ i_{W_{2},V_{2,m_{2}}}=id_{W_{2}}.∎

II. Action de la dérivation χ = x ∂ / ∂ x \chi=x\partial/\partial x et théorème principal 1

Les anneaux de références dans toute la suite sont les anneaux S ​ B p, | q | ​ ( x, α) SB^{p,|q|}(x,\alpha). Leur topologie de Krull n’est pas séparée. Leurs sous-algèbres Q ​ A p, | q | QA^{p,|q|} ne sont pas χ \chi -finies: l’idéal différentiel du germe

 | f = ∑ n > 0 α n ​ x 1 / n f=\sum_{n>0}\alpha^{n}x^{1/n} |  |

n’est pas noethérien dans l’anneau S ​ B 1, 1 ​ ( x, α) SB^{1,1}(x,\alpha): en effet, si tel est le cas, il existe ℓ ∈ ℕ \ell\in\mathbb{N}, et des germes h i ∈ S ​ B 1, 1 h_{i}\in SB^{1,1} tels que

 | ∑ i = 0 ℓ h i ​ χ i ​ f + χ ℓ + 1 ​ f = 0 \sum_{i=0}^{\ell}h_{i}\chi^{i}f+\chi^{\ell+1}f=0 |  | 0 |

Soit h i = ∑ n h n, i ​ ( x) ​ α n h_{i}=\sum_{n}h_{n,i}(x)\alpha^{n} la série de h i h_{i}. Les coefficients h n, i ∈ S ​ B 1, 0 ​ ( x) h_{n,i}\in SB^{1,0}(x); notons a i = h 0, i ​ ( 0) a_{i}=h_{0,i}(0). Par une identification des coefficients des séries en α \alpha dans l’égalité (0), on obtient les relations suivantes pour tout n > 0 n>0

 | ∑ i = 0 ℓ a i ​ ( 1 n) i + ( 1 n) ℓ + 1 = 0 \sum_{i=0}^{\ell}a_{i}(\frac{1}{n})^{i}+(\frac{1}{n})^{\ell+1}=0 |  |

ce qui est impossible (en utilisant un système de Vandermonde adéquat).

Grâce à la propriété de quasi-régularité, la topologie de Krull des algèbres

Q ​ R ​ H p, q QR{H}^{p,q} est séparée et, pour p = 1 p=1, ces algèbres sont χ \chi -finies (cf. théorème II1). La question de leur noethérianité est un problème ouvert.

Plaçons nous dans l’anneau de référence S ​ B 1, | q | ​ ( x, α) SB^{1,|q|}(x,\alpha). Soit U ∈ ( ℝ + ⁣ ∗ × ℝ | q |, 0) U\in({\mathbb{\mathbb{R}}}^{+*}\times{\mathbb{\mathbb{R}}}^{|q|},0) tel que le sous-ensemble γ = { ( x, α) ∈ U; α = 0 } \gamma=\{(x,\alpha)\in U;\ \alpha=0\} soit connexe. Alors γ \gamma est une orbite principale de χ \chi dans U U. Le morphisme intégral de χ \chi dans U U est simplement la projection canonique π: ( x, α) ↦ α \pi:(x,\alpha)\mapsto\alpha (on notera de la même façon son germe en 0). Les idéaux χ \chi -transverses le long de γ \gamma sont donc des idéaux de l’anneau analytique ℝ ​ { α } \mathbb{R}\{\alpha\}. L’anneau ( S ​ B 1, | q | ​ ( x, α), π) (SB^{1,|q|}(x,\alpha),\pi) est une extension étoilée de l’anneau ℝ ​ { α } \mathbb{R}\{\alpha\}.

###### théorème II1 (théorème principal 1)

L’algèbre Q ​ R ​ H 1, q QR{H}^{1,q} est χ \chi -finie et satisfait à la double inclusion: pour tout f ∈ Q ​ R ​ H 1, q f\in QR{H}^{1,q} d’idéal χ \chi -transverse J χ, f, γ J_{\chi,f,\gamma}, il existe n ⁡ ( f) n(f) tel que pour tout ε > 0 \varepsilon>0

 | ( x n ⁡ ( f) + ε) ​ π ∗ ​ ( J χ, f, γ) ⊂ I χ, f ⊂ π ∗ ​ ( J χ, f, γ) (x^{n(f)+\varepsilon})\pi^{*}(J_{\chi,f,\gamma})\subset I_{\chi,f}\subset\pi^{*}(J_{\chi,f,\gamma}) |  | 1 |

De plus, elle est χ \chi -équivalente à la sous-algèbre Q ​ R ​ H c ​ v ​ g 1, q QR{H}_{cvg}^{1,q}.

L’argument principal de la preuve de la χ \chi -finitude est que l’algèbre Q ​ R ​ H 1, q QR{H}^{1,q} satisfait à la double inclusion (1). La deuxième inclusion est une conséquence du

###### Lemme II1 (lemme de division)

Soit f ∈ S ​ B 1, | q | f\in SB^{1,|q|} et J χ, f, γ J_{\chi,f,\gamma} son idéal χ \chi -transverse. Alors I χ, f ⊂ π ∗ ​ ( J χ, f, γ) I_{\chi,f}\subset\pi^{*}(J_{\chi,f,\gamma}).

Preuve. On utilise le théorème de division VB1 de l’appendice B. Soit Δ \Delta le complémentaire du diagramme des exposants initiaux de J χ, f, γ J_{\chi,f,\gamma}. Effectuons la division de f ( x,.) f(x,.) dans J χ, f, γ J_{\chi,f,\gamma} pour tout x ≠ 0 x\neq 0. Soit Q ∈ π ∗ ​ ( J χ, f, γ) Q\in\pi^{*}(J_{\chi,f,\gamma}) telle que

 | Supp ( f ( x,.) − Q ( x,.)) ⊂ Δ pour tout x ≠ 0 \text{Supp}(f(x,.)-Q(x,.))\subset\Delta\quad\text{pour tout}\quad x\neq 0 |  |

Or, d’après le lemme de saturation IB5, on a f ( x,.) ∈ J χ, f, γ f(x,.)\in J_{\chi,f,\gamma} pour tout x ≠ 0 x\neq 0, et donc f − Q ≡ 0 f-Q\equiv 0; d’où le résultat.∎

La première inclusion est basée sur la notion de multiplicité et sur la propriété de quasi-analycité qui se substitue au théorème d’intersection de Krull ([L]) pour le passage à la limite. La mulptiplicité m χ ​ ( f) m_{\chi}(f) est le plus petit des entiers n n tel que ( x n + ε) ​ π ∗ ​ ( J χ, f, γ) ⊂ I χ, f (x^{n+\varepsilon})\pi^{*}(J_{\chi,f,\gamma})\subset I_{\chi,f} pour tout ε > 0 \varepsilon>0. Elle coîncide avec la multiplicité algébrique m ​ a χ ​ ( f) ma_{\chi}(f) qui se lit sur la série asymptotique de f ∈ Q ​ R ​ H 1, q f\in QR{H}^{1,q}, en faisant agir la dérivation χ \chi d’abord sur les composantes élémentaires de cette série qui sont des fewnomials [K2], solutions d’équations différentielles simples.

§1. Operateurs différentiels d’Euler E F E_{F}.

Pour tout multi-indice m = ( m 0, …, m q 1) ∈ ℕ 1 + q 1 m=(m_{0},\ldots,m_{q_{1}})\in{\mathbb{\mathbb{N}}}^{1+q_{1}} et tout q 1 q_{1} -uplet de nombre caractéristiques ( r 1, …, r q 1) (r_{1},\ldots,r_{q_{1}}) avec r j = 1 + μ j r_{j}=1+\mu_{j}, on pose

 | r = ( 1, r 1, …, r q 1) et e m ​ ( μ) = ⟨ m, r ⟩ r=(1,r_{1},\ldots,r_{q_{1}})\quad\text{ et }\quad e_{m}(\mu)=\langle m,r\rangle |  |

A toute famille finie de multi-indices F ⊂ ℕ 1 + q 1 {F}\subset{\mathbb{\mathbb{N}}}^{1+q_{1}}, on associe l’opérateur

 | E F = ∏ m ∈ F ( χ − e m ​ ( μ) ​ I ​ d) E_{F}=\prod_{m\in F}(\chi-e_{m}(\mu)Id) |  | 2 |

et on note P F P_{F} son polynôme caractéristique. On notera aussi

 | F? ​ n = { m ∈ ℕ 1 + q 1; | m |? n }. {F}_{?n}=\{m\in{\mathbb{N}}^{1+q_{1}};\quad|m|?n\}. |  |

où ?? est un opérateur binaire de comparaison. Les solutions de l’équation E F ⋅ = 0 E_{F}\cdot=0 sont les combinaisons sur ℝ ​ { α } \mathbb{R}\{\alpha\} des mônomes x e m x^{e_{m}} pour m ∈ F m\in{F}, et des fonctions élémentaires x e m ​ ( log ⁡ x) p x^{e_{m}}(\log x)^{p} si e m e_{m} est racine multiple de P F P_{F}. Donc, génériquement en μ \mu, les monômes x e m ​ ( μ) x^{e_{m}(\mu)} (pour m ∈ F m\in{F}), forment une base du noyau de l’opérateur E F E_{F}.

Les fonctions élémentaires z j = x ​ L ​ d ​ ( x, μ j) z_{j}=xLd(x,\mu_{j}) satisfont aux équations différentielles

 | χ ​ z j = r j ​ z j + x \chi z_{j}=r_{j}z_{j}+x |  |

donc, un monôme X m = x m 0 z 1 m 1 ⋯ z q 1 m q 1 X^{m}=x^{m_{0}}z_{1}^{m_{1}}\cdots z_{q_{1}}^{m_{q_{1}}} satisfait à l’équation différentielle

 | χ ​ X m = e m ​ X m + monômes ≻ \chi X^{m}=e_{m}X^{m}+\text{mon\^{o}mes}\succ |  | 3 |

où ≺ \prec est un ordre adéquat sur ces monômes (associé à l’ordre lexicographique sur ℕ 1 + q 1 \mathbb{N}^{1+q_{1}}). Par suite, tout monôme X m X^{m} est dans le noyau de l’opérateur E F = | m | E_{{F}_{=|m|}}. D’autre part, de la relation x r j = x + μ j ​ z j x^{r_{j}}=x+\mu_{j}z_{j} on déduit que

 | x e m ​ ( μ) = ∑ | m ′ | = | m | c m ′ ​ ( μ) ​ X m ′ x^{e_{m}(\mu)}=\sum_{|m^{\prime}|=|m|}c_{m^{\prime}}(\mu)X^{m^{\prime}} |  |

donc, pour tout n n, la famille des monômes X m X^{m} de longeur n n est, génériquement en μ \mu, une base du noyau de l’opérateur E F = n E_{{F}_{=n}}.

§2. Le wronskien de l’opérateur E F = n E_{{F}_{=n}} et ses mineurs.

Soit n ∈ ℕ n\in\mathbb{\mathbb{N}} et N ⁡ ( n) = ♯ ​ F = n N(n)=\sharp{F}_{=n}. Notons M n M_{n} la matrice N ⁡ ( n) × N ⁡ ( n) N(n)\times N(n) dont les colonnes sont les dérivées successives par χ \chi des monômes X m X^{m} ( | m | = n |m|=n), et soit

 | Δ n ​ ( x, μ) = det M n \Delta_{n}(x,\mu)=\det M_{n} |  | 4 |

Ces monômes forment une base du noyau de l’opérateur E F = n E_{{F}_{=n}}. Donc, en dérivant les colonnes de M n M_{n}, et en utilisant (3), on obtient

###### Lemme II2

Il existe une fonction algébrique b n ​ ( μ) b_{n}(\mu), non-identiquement nulle telle que

 | Δ n ​ ( x, μ) = b n ​ ( μ) ​ x s n ​ ( μ) avec s n ​ ( μ) = ⟨ ∑ | m | = n m, r ⟩ \Delta_{n}(x,\mu)=b_{n}(\mu)x^{s_{n}(\mu)}\quad\text{avec}\quad s_{n}(\mu)=\langle{\sum}_{|m|=n}m,r\rangle |  | 5 |

Cette fonction algébrique est donnée par b n ​ ( μ) = Δ n ​ ( 1, μ) b_{n}(\mu)=\Delta_{n}(1,\mu). Soit A n ​ ( x, μ) A_{n}(x,\mu) la matrice complémentaire de la matrice M n ​ ( x, μ) M_{n}(x,\mu)

###### Lemme II3

Pour tout x 0 ≠ 0 x_{0}\neq 0 et pour tout ε > 0 \varepsilon>0, les éléments de la matrice M n ​ ( x 0, μ) ​ A n ​ ( x, μ) M_{n}(x_{0},\mu)A_{n}(x,\mu) appartiennent à l’idéal principal de S ​ B 1, q 1 SB^{1,q_{1}} engendré par

x n ​ N ​ ( n) − n − ε ​ b n x^{nN(n)-n-\varepsilon}b_{n}.

Preuve. Ces éléments sont de la forme

 | B i, l ​ ( x, μ) = L i ​ ( x 0, μ) ​ C l ​ ( x, μ) B_{i,l}(x,\mu)=L_{i}(x_{0},\mu)C_{l}(x,\mu) |  | 6 |

oû L i ​ ( x, μ) L_{i}(x,\mu) est la ligne d’indice i i dans la matrice M n M_{n} et C l ​ ( x, μ) C_{l}(x,\mu) est la colonne d’indice l l dans la matrice A n A_{n}. Il est clair, d’après la définition de la matrice A n A_{n} que ces éléments sont divisibles par x n ​ N ​ ( n) − n − ε x^{nN(n)-n-\varepsilon} dans l’anneau S ​ B 1, q 1 SB^{1,q_{1}} (chaque monôme X m X^{m} est divisible par x n − ε / s x^{n-\varepsilon/s} dans cet anneau, pour tout s > 0 s>0). Il suffit donc de montrer que l’idéal χ \chi -transverse J J, de B i, l B_{i,l} le long de γ \gamma est inclus dans l’idéal principal engendré par b n b_{n}. Le lemme de division II1 permettra de conclure.

Pour cela, montrons par une récurrence sur k k, que pour tout ( i, l) ∈ { 1, …, N ⁡ ( n) } 2 (i,l)\in\{1,\ldots,N(n)\}^{2} et pour tout k k

 | L i ​ ( x, μ) ​ χ k ​ C l ​ ( x, μ) ≡ 0 [( b n)] dans ​ S ​ B 1, q 1 L_{i}(x,\mu)\chi^{k}C_{l}(x,\mu)\equiv 0\quad[(b_{n})]\qquad\text{ dans }SB^{1,q_{1}} |  | 7 |

Pour k = 0 k=0, la relation (7) est une conséquence de l’égalité M n ​ A n = Δ n ​ I ​ d M_{n}A_{n}=\Delta_{n}Id.

L’idéal ( b n) (b_{n}) étant stable par χ \chi, une dérivation de (7) donne

 | L i ​ χ k + 1 ​ C l ≡ − ( χ ​ L i) ​ ( χ k ​ C l) [( b n)] L_{i}\chi^{k+1}C_{l}\equiv-(\chi L_{i})(\chi^{k}C_{l})\quad[(b_{n})] |  |

or, pour i ≠ N ⁡ ( n) i\neq N(n) on a χ ​ L i = L i + 1 \chi L_{i}=L_{i+1} d’après la définition de la matrice M n M_{n}. Et en utilisant l’opérateur E F = n E_{{F}_{=n}}, on obtient

 | χ ​ L N ⁡ ( n) = ∑ j = 1 N ⁡ ( n) c j ​ ( μ) ​ L j \chi L_{N(n)}=\sum_{j=1}^{N(n)}c_{j}(\mu)L_{j} |  |

Et ceci prouve la relation (7). Maintenant, d’après la définition IB6 de l’idéal χ \chi -transverse, l’idéal J ⊂ ℝ ​ { μ } J\subset\mathbb{R}\{\mu\} est engendré par les dérivées successives

 | ( χ k ​ B i, l ​ ( x 1, μ)) k ∈ ℕ (\chi^{k}B_{i,l}(x_{1},\mu))_{k\in\mathbb{N}} |  |

pour tout x 1 > 0 x_{1}>0. On prend donc x 1 = x 0 x_{1}=x_{0} et on utilise (7) pour finir la preuve du lemme.∎

§3. Sur les blocs χ \chi -homogènes.

Soit c c l’immersion de la partie IA, et soit H ​ H n H{H}_{n} l’image par c ∗ c^{*} du ℝ ​ { α } \mathbb{R}\{\alpha\} -module ℝ ​ { α } ​ [X] n \mathbb{R}\{\alpha\}[X]_{n}, engendré par les monômes X m X^{m} d’une même longueur n n ( c ∗ ​ ( X) = ( x, ( z j ​ ( x, μ j)) j = 1, …, q 1) c^{*}(X)=(x,(z_{j}(x,\mu_{j}))_{j=1,\ldots,q_{1}})), rappelons qu’on note de la même façon ces fonctions X, z j X,z_{j} et les coordonnées correspondantes). D’après le paragraphe 1, la restriction de c ∗ c^{*} à ce module est un isomorphisme. Les éléments du module H ​ H n H{H}_{n} sont dits blocs χ \chi -homogènes de degré n n. Ces modules sont stables par les opérateurs d’Euler définis ci-dessus.

###### Lemme II4

Tout g ∈ H ​ H n g\in H{H}_{n} satisfait à la double inclusion. Plus précisément, pour tout ε > 0 \varepsilon>0

 | ( x n + ε) ​ π ∗ ​ ( J χ, g, γ) ⊂ I χ, g ⊂ π ∗ ​ ( J χ, g, γ) (x^{n+\varepsilon})\pi^{*}(J_{\chi,g,\gamma})\subset I_{\chi,g}\subset\pi^{*}(J_{\chi,g,\gamma}) |  |

Preuve. La deuxième inclusion est donnée par le lemme de division II1. Un tel g g s’écrit

 | g = ∑ | m | = n a m ​ ( α) ​ X m g=\sum_{|m|=n}a_{m}(\alpha)X^{m} |  | 8 |

il est donc dans le noyau de l’opérateur E F = n E_{{F}_{=n}}. Par conséquent, son idéal différentiel est engendré par la famille { χ j ​ g; j < N ⁡ ( n) } \{\chi^{j}g;\ j<N(n)\}, et donc son idéal χ \chi -transverse le long de γ \gamma est engendré par la famille { χ j g ( x 0,.); j < N ( n) } \{\chi^{j}g(x_{0},.);\ j<N(n)\} pour tout x 0 ≠ 0 x_{0}\neq 0. Plusieurs dérivations de (8) donnent le système

 | M n ​ ( a m) m = ( χ j ​ g) j M_{n}(a_{m})_{m}=(\chi^{j}g)_{j} |  | 9 |

( ( a m) m (a_{m})_{m} et ( χ j ​ g) j (\chi^{j}g)_{j} désignent les vecteurs colonnes associés). En particulier

 | M n ( x 0,.) ( a m) m = ( χ j g ( x 0,.)) j M_{n}(x_{0},.)(a_{m})_{m}=(\chi^{j}g(x_{0},.))_{j} |  | 10 |

Mutiplions (9) par la matrice M n ( x 0,.) A n M_{n}(x_{0},.)A_{n} et utilisons (10)

 | Δ n ( χ j g ( x 0,.)) j = M n ( x 0,.) A n ( χ j g) j \Delta_{n}(\chi^{j}g(x_{0},.))_{j}=M_{n}(x_{0},.)A_{n}(\chi^{j}g)_{j} |  |

Par le lemme II2, on a Δ n = x s n ​ b n \Delta_{n}=x^{s_{n}}b_{n}, et par le lemme II3

 | M n ( x 0,.) A n ∈ ( x n ​ N ​ ( n) − n − ε b n) M_{n}(x_{0},.)A_{n}\in(x^{nN(n)-n-\varepsilon}b_{n}) |  |

Or, s n ​ ( 0) = n ​ N ​ ( n) s_{n}(0)=nN(n). Ce qui finit la preuve du lemme.∎

Remarque II1. Un cas simple, où cette première inclusion peut effectivement être donnée par le Nullstellensatz d’Hilbert, est le suivant: prenons q 1 = 1 q_{1}=1 et supposons J = ℝ ​ { α } J=\mathbb{R}\{\alpha\}. L’immersion c ⁡ ( x, α) = ( x, z ⁡ ( x, μ), α) c(x,\alpha)=(x,z(x,\mu),\alpha) est un difféomorphisme sur la variété image V = c ⁡ ( U) V=c(U), qui se prolonge en un homéomorhisme sur le bord ∂ 0 U = { x = 0 } \partial_{0}U=\{x=0\}. La dérivation sur V V c ∗ ​ ( χ) c_{*}(\chi), se prolonge sur un voisinage W W de 0, en une dérivation analytique

 | X = x ​ ∂ ∂ x + ( r ​ z + x) ​ ∂ ∂ z {X}=x\frac{\partial}{\partial x}+(rz+x)\frac{\partial}{\partial z} |  |

Soit G = ( c ∗) − 1 ​ ( g) G=(c^{*})^{-1}(g). D’après le lemme de transfert IB6 et l’isomorphie de c ∗: ℝ ⁡ { α } ​ [x, z] n → H ​ H n c^{*}:\mathbb{R}\{\alpha\}[x,z]_{n}\to H{H}_{n}, on a I χ, g = c ∗ ​ ( I X, G CLOSE I_{\chi,g}=c^{*}(I_{{X},G} (car ℝ ⁡ { α } ​ [x, z] n | V ≅ ℝ ⁡ { α } ​ [x, z] n \mathbb{R}\{\alpha\}[x,z]_{n|V}\cong\mathbb{R}\{\alpha\}[x,z]_{n}). Plaçons nous dans le complexifié de W W. L’ensemble des zéros de l’idéal différentiel I X, G I_{{X},G} est un sous-ensemble analytique invariant par le flot de X {X}. Or, pour α \alpha fixé générique, les seules feuilles analytiques de X {X} sont { x = 0 } \{x=0\} et { x + μ z = 0 } \{x+\mu z=0\}. Par le Nullstellensatz d’Hilbert, il existe M ∈ ℕ M\in\mathbb{N} tel que

 | ( x ⁡ ( x + μ ​ z)) M ∈ I X, G (x(x+\mu z))^{M}\in I_{{X},G} |  |

et en appliquant c ∗ c^{*}, on obtient x ( 1 + r) ​ M ∈ I χ, g x^{(1+r)M}\in I_{\chi,g}. Ceci est encore valable pour g ∈ Q ​ R ​ H c ​ v ​ g 1, ( 1, q 2) g\in QR{H}^{1,(1,q_{2})}_{cvg}, par la définition de cet anneau. On peut généraliser cette idée à plusieurs fonctions élémentaires ( q 1 > 1 q_{1}>1), seulement l’estimation de l’entier M M optimal semble difficile. Par la démarche adoptée dans ce travail, on obtient une estimation précise et optimal de cet entier, en se plaçant dans des anneaux plus larges.

§4. Sur les fewnomials.

Le passage des blocs χ \chi -homogènes aux fewnomials est basée sur l’inversion des opérateurs E F E_{F}

###### Lemme II5

Soit e ⁡ ( α) e(\alpha) un germe analytique en 0 tel que e ⁡ ( 0) ≠ n e(0)\neq n. Soit l’opérateur E = χ − e ​ I ​ d E=\chi-eId. Alors, pour tout g ∈ H ​ H n g\in H{H}_{n}, I χ, E ​ g = I χ, g I_{\chi,Eg}=I_{\chi,g}.

Preuve. Il est clair que I χ, E ​ g ⊂ I χ, g I_{\chi,Eg}\subset I_{\chi,g}. De la relation χ ​ g = e ​ g + E ​ g \chi g=eg+Eg, on déduit

 | E F = n ​ g ≡ P F = n ​ ( e) ​ g [I χ, E ​ g] E_{{F}_{=n}}g\equiv P_{{F}_{=n}}(e)g\qquad[I_{\chi,Eg}] |  |

Or E F = n ​ g = 0 E_{{F}_{=n}}g=0 et le germe e e n’est pas valeur propre de cet opérateur, on obtient donc g ∈ I χ, E ​ g g\in I_{\chi,Eg}, par conséquent I χ, g ⊂ I χ, E ​ g I_{\chi,g}\subset I_{\chi,Eg}.∎

Soit n ∈ ℕ n\in\mathbb{N} quelconque et soit f = ∑ p = 0 n g p f=\sum_{p=0}^{n}g_{p}, où g p g_{p} est un bloc χ \chi -homogène de degré p p, f f est un fewnomial d’après la terminologie de Khovanski [K1]. Appliquons l’opérateur E F < n E_{{F}_{<n}} à f f

 | E F < n ​ f = E F < n ​ g n ​ 10 ′ E_{{F}_{<n}}f=E_{{F}_{<n}}g_{n}10^{\prime} |  |  |

car deux opérateurs χ − e ​ I ​ d \chi-eId et χ − e ′ ​ I ​ d \chi-e^{\prime}Id commutent, et pour p < n p<n, le bloc g p g_{p} est dans le noyau de l’opérateur E F < n E_{{F}_{<n}}. En appliquant plusieurs fois le lemme II5 à g n g_{n}, on obtient que I χ, E F < n = I χ, g n I_{\chi,E_{{F}_{<n}}}=I_{\chi,g_{n}}, et d’après (10’), I χ, g n ⊂ I χ, f I_{\chi,g_{n}}\subset I_{\chi,f}. De même, I χ, g n − 1 ⊂ I χ, f − g n ⊂ I χ, f I_{\chi,g_{n-1}}\subset I_{\chi,f-g_{n}}\subset I_{\chi,f}, …etc. On obtient donc

###### Lemme II6

I χ, f = ∑ p = 0 n I χ, g p I_{\chi,f}=\sum_{p=0}^{n}I_{\chi,g_{p}}.

Ces idéaux étant des idéaux différentiels, cette égalité est encore vraie germifiée en tout point de γ \gamma voisin de 0. Prenons la restriction à une transversale à γ \gamma, cette égalité donne

 | J χ, f, γ ⊂ ∑ p = 0 n J χ, g p, γ J_{\chi,f,\gamma}\subset\sum_{p=0}^{n}J_{\chi,g_{p},\gamma} |  |

et l’inclusion I χ, g p ⊂ I χ, f I_{\chi,g_{p}}\subset I_{\chi,f} donne J χ, g p, γ ⊂ J χ, f, γ J_{\chi,g_{p},\gamma}\subset J_{\chi,f,\gamma} pour tout p = 0, …, n p=0,\ldots,n. D’où l’égalité

 | J χ, f, γ = ∑ p = 0 n J χ, g p, γ ​ 10 ​ " J_{\chi,f,\gamma}=\sum_{p=0}^{n}J_{\chi,g_{p},\gamma}10" |  |  |

###### Lemme II7

Le germe f f satisfait à la double inclusion. Plus précisément, pour tout ε > 0 \varepsilon>0

 | ( x n + ε) ​ π ∗ ​ ( J χ, f, γ) ⊂ I χ, f ⊂ π ∗ ​ ( J χ, f, γ) (x^{n+\varepsilon})\pi^{*}(J_{\chi,f,\gamma})\subset I_{\chi,f}\subset\pi^{*}(J_{\chi,f,\gamma}) |  |

Preuve. Par les lemmes II4 et II6, on a

 | ∑ p = 0 n ( x p + ε) ​ π ∗ ​ ( J χ, g p, γ) ⊂ I χ, f ⊂ ∑ p = 0 n π ∗ ​ ( J χ, g p, γ) \sum_{p=0}^{n}(x^{p+\varepsilon})\pi^{*}(J_{\chi,g_{p},\gamma})\subset I_{\chi,f}\subset\sum_{p=0}^{n}\pi^{*}(J_{\chi,g_{p},\gamma}) |  |

ou plus simplement

 | ( x n + ε) ​ ∑ p = 0 n π ∗ ​ ( J χ, g p, γ) ⊂ I χ, f ⊂ ∑ p = 0 n π ∗ ​ ( J χ, g p, γ) (x^{n+\varepsilon})\sum_{p=0}^{n}\pi^{*}(J_{\chi,g_{p},\gamma})\subset I_{\chi,f}\subset\sum_{p=0}^{n}\pi^{*}(J_{\chi,g_{p},\gamma}) |  |

L’égalité (10”) permet de conclure.∎

§5. Sur les convergents.

###### Lemme II8

L’algèbre Q ​ R ​ H cvg 1, q QR{H}^{1,q}_{\text{cvg}} est χ \chi -finie et satisfait à la double inclusion. De plus, elle est χ \chi -équivalente à la sous-algèbre des fewnomials.

Preuve. Cette algèbre est clairement stable par χ \chi. Pour la χ \chi -finitude, on utilise le lemme d’extension IB2. L’anneau Q ​ R ​ H cvg 1, q QR{H}^{1,q}_{\text{cvg}} est la restriction d’un anneau analytique, c’st donc un anneau noethérien, d’où l’hypothèse ( i ​ i) (ii) du lemme d’extension. L’hypothèse ( i ​ i ​ i) (iii) est claire: prendre ω j = d ​ α j \omega_{j}=d\alpha_{j}. La preuve de l’hypothèse ( i) (i) est une double application de la théorie de Khovanski et d’un théorème de [T] (elle est aussi une conséquence d’un travail récent et général de Speissegger [S]). Soit X = ( x, z 1, …, z q 1) X=(x,z_{1},\ldots,z_{q_{1}}) et z 0 ​ ( x) = x ​ log ⁡ x z_{0}(x)=x\log x. Soit c 0 c_{0} l’immersion c 0 ​ ( X, α) = ( X, z 0 ​ ( x), α) c_{0}(X,\alpha)=(X,z_{0}(x),\alpha) et B 1 {B}_{1} l’algèbre B 1 = c 0 ∗ ​ ( ℝ ⁡ { X, z 0, α }) {B}_{1}=c^{*}_{0}(\mathbb{R}\{X,z_{0},\alpha\}). Le graphe de la fonction z 0 z_{0} est une solution séparante de l’équation différentielle

 | ω 0 = x ​ d ​ z 0 − ( z 0 + x) ​ d ​ x = 0 \omega_{0}=xdz_{0}-(z_{0}+x)dx=0 |  | 11 |

considérée sur un ouvert connexe U 0 U_{0}, voisinage de 0 dans { x > 0, z 0 < 0 } \{x>0,\ z_{0}<0\}. La 1-forme ω 0 \omega_{0} est à coefficients dans l’anneau analytique ℝ ​ { X, z 0, α } \mathbb{R}\{X,z_{0},\alpha\}. L’algèbre B 1 {B}_{1} est donc topologiquement noethérienne [T]. Soit c 1 c_{1} l’immersion c 1 ​ ( x, α) = ( X ⁡ ( x, α), α) c_{1}(x,\alpha)=(X(x,\alpha),\alpha), alors Q ​ R ​ H c ​ v ​ g 1, q = c 1 ∗ ​ ( B 1) QR{H}^{1,q}_{cvg}=c_{1}^{*}({B}_{1}). les graphes des fonctions z j z_{j} sont des solutions séparantes des équations différentielles

 | ω j = x ​ d ​ z j − ( ( 1 + μ j) ​ z j + x) ​ d ​ x − ( x ​ log ⁡ x ⁡ ( μ j ​ z j + x) − x ​ z j) ​ d ​ μ j μ j = 0 \omega_{j}=xdz_{j}-((1+\mu_{j})z_{j}+x)dx-(x\log x(\mu_{j}z_{j}+x)-xz_{j})\frac{d\mu_{j}}{\mu_{j}}=0 |  | 12 |

considérées sur des ouverts connexes U (? j) U_{(?_{j})}, voisinages de 0 dans { x > 0, z j < 0, μ j ​? j ​ 0 ​ j = 1, …, q 1 } \{x>0,\ z_{j}<0,\ \mu_{j}?_{j}0\ j=1,\ldots,q_{1}\}, où ? j = >, <?_{j}=>,< (si l’un des μ j \mu_{j} est nul, alors z j = z 0 z_{j}=z_{0}). Ces 1-formes sont à coefficients dans l’algèbre B 1 {B}_{1}. L’algèbre Q ​ R ​ H cvg 1, q QR{H}^{1,q}_{\text{cvg}} est donc topologiquement noethérienne. D’où l’hypothèse ( i) (i).

Soit f = ∑ p = 0 ∞ g p ∈ Q ​ R ​ H cvg 1, q f=\sum_{p=0}^{\infty}g_{p}\in QR{H}^{1,q}_{\text{cvg}} et soit f n = ∑ p ≤ n g p f_{n}=\sum_{p\leq n}g_{p}, où g p g_{p} est un bloc χ \chi -homogène de degré p p. D’après le lemme II6, la suite des idéaux ( I χ, f n) (I_{\chi,f_{n}}) est croissante dans l’anneau noethérien Q ​ R ​ H c ​ v ​ g 1, q QR{H}^{1,q}_{cvg}. Elle est donc stationnaire. Soit I I sa limite et soit n 0 n_{0} son indice de stationnarité: c’est le plus petit entier n n tel que I χ, f n = I χ, f n ′ I_{\chi,f_{n}}=I_{\chi,f_{n^{\prime}}} pour tout n ′ ≥ n n^{\prime}\geq n. Soit M X = ⟨ x, z 0, z 1, …, z q 1 ⟩ ⊂ Q ​ R ​ H c ​ v ​ g 1, q {M}_{X}=\langle x,z_{0},z_{1},\ldots,z_{q_{1}}\rangle\subset QR{H}^{1,q}_{cvg}, il est inclus dans l’idéal maximal de Q ​ R ​ H c ​ v ​ g 1, q QR{H}^{1,q}_{cvg}, et il est stable par χ \chi. Pour tout n ∈ ℕ n\in\mathbb{N}, on a f − f n ∈ M X n f-f_{n}\in{M}_{X}^{n} d’après la série de f f. Donc, pour tout n ≥ n 0 n\geq n_{0}, on a

 | I χ, f ⊂ I + M X n et I ⊂ I χ, f + M X n I_{\chi,f}\subset I+{M}_{X}^{n}\quad\text{et}\quad I\subset I_{\chi,f}+{M}_{X}^{n} |  |

Par le théorème d’intersection de Krull, on a I χ, f = I I_{\chi,f}=I. Or I = I χ, f n 0 I=I_{\chi,f_{n_{0}}}, donc en germifiant ces égalités le long de γ \gamma, et en prenant les restrictions à une transversale, on obtient J χ, f, γ = J χ, f n 0, γ J_{\chi,f,\gamma}=J_{\chi,f_{n_{0}},\gamma}. Par conséquent, le lemme II7 appliqué au fewnomial f n 0 f_{n_{0}}, montre que f f vérifie la double inclusion. Soit k k l’exposant d’Artin-Ress de l’idéal M X {M}_{X} dans l’idéal I I ([L]): pour tout entier n n, on a

 | M X n + k ∩ I = M X k ∩ ( M X n ​ I) {M}_{X}^{n+k}\cap I={M}_{X}^{k}\cap({M}_{X}^{n}I) |  |

Prenons n > max ⁡ { n 0, k } n>\max\{n_{0},k\}. On a f − f n ∈ M X n f-f_{n}\in{M}_{X}^{n} et I χ, f − f n ⊂ I I_{\chi,f-f_{n}}\subset I, donc f − f n ∈ M X ​ I f-f_{n}\in{M}_{X}I. Or, par le choix de n n, I = I χ, f n I=I_{\chi,f_{n}}, le germe f f est donc χ \chi -équivalent au fewnomial f n f_{n}, et ceci finit la preuve du lemme.∎

§6. Enfin, sur l’algèbre Q ​ R ​ H 1, q QR{H}^{1,q}.

Soit f ∈ Q ​ R ​ H 1, q f\in QR{H}^{1,q} et soit f ^ = ∑ p = 0 ∞ g p \widehat{f}=\sum_{p=0}^{\infty}g_{p} une série formelle associée à f f. Les sommes finies f n = ∑ p ≤ n g p f_{n}=\sum_{p\leq n}g_{p} sont des fewnomials. La suite des idéaux différentiels ( I χ, f n) (I_{\chi,f_{n}}) est croissante (dans chacun des anneaux Q ​ R ​ H c ​ v ​ g 1, q QR{H}^{1,q}_{cvg}, Q ​ R ​ H 1, q QR{H}^{1,q} ou S ​ B 1, | q | SB^{1,|q|}). Il en est de même de la suite des idéaux χ \chi -transverses ( J χ, f n, γ) (J_{\chi,f_{n},\gamma}) dans l’anneau ℝ ​ { α } \mathbb{R}\{\alpha\}. Soit I I la limite ”différentielle” de la suite ( I χ, f n) (I_{\chi,f_{n}}) dans l’anneau Q ​ R ​ H c ​ v ​ g 1, q QR{H}^{1,q}_{cvg}, et soit J J la limite ” χ \chi -transverse” de la suite ( J χ, f n, γ) (J_{\chi,f_{n},\gamma}) dans l’anneau ℝ ​ { α } \mathbb{R}\{\alpha\}. On va montrer que la limite différentielle I I, prolongée dans l’anneau S ​ B 1, | q | SB^{1,|q|}, coincide avec l’idéal différentiel de f f dans cet anneau (mais pas forcément dans l’anneau Q ​ R ​ H 1, q QR{H}^{1,q}). Par contre, on montre que la limite χ \chi -transverse J J coincide avec l’idéal χ \chi -transverse de f f dans l’anneau ℝ ​ { α } \mathbb{R}\{\alpha\}; et cela grâce à deux arguments principaux: la propriété de quasi-analycité et le théorème de division VB1.

###### Lemme II9

Pour tout n n, on a J χ, g n, γ ⊂ J χ, f, γ \qquad J_{\chi,g_{n},\gamma}\subset J_{\chi,f,\gamma}.

Preuve. Supposons d’abord que f = g n + o ⁡ ( x n) f=g_{n}+o(x^{n}). D’après la définition des séries asymptotiques de f f (cf. Déf. IA5), on peut trouver ε > 0 \varepsilon>0 suffisament petit, et h ∈ S ​ B 1, | q | h\in SB^{1,|q|} tels que

 | f = g n + x n + 2 ​ ε ​ h f=g_{n}+x^{n+2\varepsilon}h |  | 13 |

En germifiant l’égalité x n + 2 ​ ε ​ h = f − g n x^{n+2\varepsilon}h=f-g_{n} en un point de γ \gamma ( x > 0 x>0), et en prenant la retriction à une transversale des dérivées successives, on obtient J χ, h, γ ⊂ J χ, f, γ + J χ, g n, γ J_{\chi,h,\gamma}\subset J_{\chi,f,\gamma}+J_{\chi,g_{n},\gamma}. Donc, d’après le lemme de division II1, appliqué à h h, il existe h 1 ∈ π ∗ ​ ( J χ, f, γ) h_{1}\in\pi^{*}(J_{\chi,f,\gamma}) et h 2 ∈ π ∗ ​ ( J χ, g n, γ) h_{2}\in\pi^{*}(J_{\chi,g_{n},\gamma}) telles que h = h 1 + h 2 h=h_{1}+h_{2}. Maintenant, en considérant les idéaux différentiels et en utilisant l’égalité (13), on obtient

 | I χ, g n ⊂ I χ, f + ( x n + 2 ​ ε) ​ ( I χ, h 1 + I χ, h 2) I_{\chi,g_{n}}\subset I_{\chi,f}+(x^{n+2\varepsilon})(I_{\chi,h_{1}}+I_{\chi,h_{2}}) |  |

soit

 | I χ, g n ⊂ I χ, f + ( x n + 2 ​ ε) ​ ( π ∗ ​ ( J χ, f, γ) + π ∗ ​ ( J χ, g n, γ)) I_{\chi,g_{n}}\subset I_{\chi,f}+(x^{n+2\varepsilon})(\pi^{*}(J_{\chi,f,\gamma})+\pi^{*}(J_{\chi,g_{n},\gamma})) |  |

Le lemme de division II1, appliqué à f f, donne

 | I χ, g n ⊂ π ∗ ​ ( J χ, f, γ) + ( x n + 2 ​ ε) ​ π ∗ ​ ( J χ, g n, γ) I_{\chi,g_{n}}\subset\pi^{*}(J_{\chi,f,\gamma})+(x^{n+2\varepsilon})\pi^{*}(J_{\chi,g_{n},\gamma}) |  |

et le lemme II4 appliqué à g n g_{n} fournit

 | I χ, g n ⊂ π ∗ ​ ( J χ, f, γ) + ( x ε) ​ I χ, g n I_{\chi,g_{n}}\subset\pi^{*}(J_{\chi,f,\gamma})+(x^{\varepsilon})I_{\chi,g_{n}} |  |

L’idéal I χ, g n I_{\chi,g_{n}} étant noethérien, et l’idéal principal ( x ε) (x^{\varepsilon}) étant inclus dans l’idéal maximal de l’anneau S ​ B 1, q SB^{1,q}, le lemme de Nakayama ([L]) donne

 | I χ, g n ⊂ π ∗ ​ ( J χ, f, γ) I_{\chi,g_{n}}\subset\pi^{*}(J_{\chi,f,\gamma}) |  |

En prenant la restriction à une transversale à γ \gamma, on obtient J χ, g n, γ ⊂ J χ, f, γ J_{\chi,g_{n},\gamma}\subset J_{\chi,f,\gamma}. Maintenant, si f ^ = ∑ p ≥ 0 g p \widehat{f}=\sum_{p\geq 0}g_{p}, on montre comme ci-dessus que J χ, g 0, γ ⊂ J χ, f, γ J_{\chi,g_{0},\gamma}\subset J_{\chi,f,\gamma}, puis en supposant que pour tout p < n p<n, on a J χ, g p, γ ⊂ J χ, f, γ J_{\chi,g_{p},\gamma}\subset J_{\chi,f,\gamma}, on montre comme ci-dessus que

 | J χ, g n, γ ⊂ J χ, f − ∑ p < n g p, γ ⊂ J χ, f, γ J_{\chi,g_{n},\gamma}\subset J_{\chi,f-\sum_{p<n}g_{p},\gamma}\subset J_{\chi,f,\gamma} |  |

et ceci finit la preuve du lemme.∎

Ce lemme et la propriété de quasi-analycité impliquent le

###### Lemme II10

Il existe une application série formelle injective

 | f ∈ Q ​ R ​ H 1, q ↦ f ^ = ∑ p ≥ 0 g p ∈ c ∗ ​ ( ℝ ⁡ { α } ​ [[X]]) f\in QR{H}^{1,q}\mapsto\widehat{f}=\sum_{p\geq 0}g_{p}\in c^{*}(\mathbb{R}\{\alpha\}[[X]]) |  |

Preuve. Pour prouver l’existence, il suffit de montrer que le germe nul admet une unique série qui est la série nulle. En effet, si 0 ^ = ∑ p ≥ 0 g p \widehat{0}=\sum_{p\geq 0}g_{p}, le lemme II9 dit que pour tout n n, J χ, g n, γ ⊂ { 0 } J_{\chi,g_{n},\gamma}\subset\{0\}, et le lemme de division II1 dit alors que g n ≡ 0 g_{n}\equiv 0. Pour prouver l’injection, prenons f ∈ Q ​ R ​ H 1, q f\in QR{H}^{1,q} tel que g p ​ ( f) = 0 g_{p}(f)=0 pour tout p p. On a donc f = o ⁡ ( x n) f=o(x^{n}) pour tout n n; comme Q ​ R ​ H 1, q ⊂ Q ​ A 1, | q | QR{H}^{1,q}\subset QA^{1,|q|}, on obtient f ≡ 0 f\equiv 0.∎

Une conséquence de cela est que le morphisme c ∗: ℝ ⁡ { X, α } → Q ​ R ​ H c ​ v ​ g 1, q c^{*}:\mathbb{R}\{X,\alpha\}\to QR{H}^{1,q}_{cvg} est un isomorphisme. En effet, si F = ∑ p ≥ 0 G p ∈ ℝ ⁡ { X, α } F=\sum_{p\geq 0}G_{p}\in\mathbb{R}\{X,\alpha\} (les G p G_{p} étant ses parties homogènes en X X de degré p p), son image f = c ∗ ​ ( F) f=c^{*}(F) admet comme série ∑ p ≥ 0 c ∗ ​ ( G p) \sum_{p\geq 0}c^{*}(G_{p}), et on a vu que la restriction de c ∗ c^{*} aux modules ℝ ​ { α } ​ [X] p \mathbb{R}\{\alpha\}[X]_{p} est un isomorphisme sur les modules H ​ H p H{H}_{p}.

Le résultat clé de cette section est le suivant

###### Lemme II11

J = J χ, f, γ \quad J=J_{\chi,f,\gamma}.

Preuve. D’après le lemme II9 et l’égalité (10”), on a

 | J χ, f n, γ ⊂ J χ, f, γ pour tout ​ n ​ 13 ′ J_{\chi,f_{n},\gamma}\subset J_{\chi,f,\gamma}\quad\text{pour tout}\ n13^{\prime} |  |  |

donc J ⊂ J χ, f, γ J\subset J_{\chi,f,\gamma}. Pour montrer l’autre inclusion, on utilise le théorème de division VB1 (appendice VB), sur les algèbres Q A 1, | q | [.] QA^{1,|q|}[.]. Les fonctions f n f_{n} sont algébriques dans les fonctions élémentaires z j z_{j}; il existe donc Ω ∈ E ​ I \Omega\in{E}{I} tel que f, f n ∈ Q ​ A ​ [Ω] f,\ f_{n}\in QA[\Omega] pour tout n n. Soit φ 1, …, φ l \varphi_{1},\ldots,\varphi_{l} une base de J J. Pour tout F ∈ Q ​ A ​ [Ω] F\in QA[\Omega], on note

 | Q ⁡ ( F) = ∑ i Q i ​ ( F) ​ φ i et R ⁡ ( F) = F − Q ⁡ ( F) Q(F)=\sum_{i}Q_{i}(F)\varphi_{i}\quad\text{ et }\quad R(F)=F-Q(F) |  |

où les fonctions Q i ​ ( F) Q_{i}(F) et R ⁡ ( F) R(F) sont données par le théorème de division VB1. D’après la définition de l’idéal limite transverse J J, on a J χ, f n, γ ⊂ J J_{\chi,f_{n},\gamma}\subset J pour tout n n. Donc, d’après le lemme de division II1, on a R ⁡ ( f n) ≡ 0 R(f_{n})\equiv 0 pour tout n n. Et, par unicité de la division dans le théorème VB1, on a

 | R ⁡ ( f) = R ⁡ ( f − f n) pour tout ​ n R(f)=R(f-f_{n})\quad\text{pour tout}\ n |  |

Or, f − f n = o ⁡ ( x n) f-f_{n}=o(x^{n}). Le lemme VB1 implique que R ⁡ ( f) = o ⁡ ( x n) R(f)=o(x^{n}) pour tout n n. Comme R ⁡ ( f) ∈ Q ​ A ​ [Ω] R(f)\in QA[\Omega], on obtient R ⁡ ( f) ≡ 0 R(f)\equiv 0. Ceci prouve que f ∈ π ( J) f\in\pi^{(}J), et donc (par un raisonnement maintenant classique), que J χ, f, γ ⊂ J J_{\chi,f,\gamma}\subset J.∎

###### Définition II1

L’indice de stationnarité de la suite d’idéaux ( J χ, f n, γ) (J_{\chi,f_{n},\gamma}) est dit multiplicité algébrique de f f relativement à χ \chi le long de γ \gamma. On la note m ​ a χ ​ ( f) ma_{\chi}(f).

§7. Preuve du théorème principal II1.

Soit n ≥ m ​ a χ ​ ( f) n\geq ma_{\chi}(f) et soit h n = f − f n = o ⁡ ( x n + 2 ​ ε) h_{n}=f-f_{n}=o(x^{n+2\varepsilon}) (d’après la série asymptotique de f f). On a J χ, h n, γ ⊂ J J_{\chi,h_{n},\gamma}\subset J d’après le lemme II11. Et, par le lemme de division II1, on a

 | h n ∈ ( x n + 2 ​ ε) ​ π ∗ ​ ( J) h_{n}\in(x^{n+2\varepsilon})\pi^{*}(J) |  |

D’après le lemme II7, on a ( x n + ε) ​ π ∗ ​ ( J) ⊂ I χ, f n (x^{n+\varepsilon})\pi^{*}(J)\subset I_{\chi,f_{n}}. Donc, h n ∈ ( x ε) ​ I χ, f n h_{n}\in(x^{\varepsilon})I_{\chi,f_{n}}. L’idéal ( x ε) (x^{\varepsilon}) est inclus dans l’idéal maximal de S ​ B SB, et il est satble par χ \chi. Comme f n f_{n} est un fewnomial, le lemme de finitude IB1 et le lemme II8 impliquent que l’algèbre Q ​ R ​ H 1, q QR{H}^{1,q} est χ \chi -finie, et qu’elle est χ \chi -équivalente à la sous-algèbre des fewnomials.

Ceci implique en particulier que I χ, f = I χ, f n I_{\chi,f}=I_{\chi,f_{n}} pour tout n ≥ m ​ a χ ​ ( f) n\geq ma_{\chi}(f). En prenant n = m ​ a χ ​ ( f) n=ma_{\chi}(f) et en utilisant la double inclusion du lemme II7, on obtient la double inclusion pour l’algèbre Q ​ R ​ H 1, q QR{H}^{1,q}

 | ( x m ​ a χ ​ ( f) + ε) ​ π ∗ ​ ( J χ, f, γ) ⊂ I χ, f ⊂ π ∗ ​ ( J χ, f, γ) (x^{ma_{\chi}(f)+\varepsilon})\pi^{*}(J_{\chi,f,\gamma})\subset I_{\chi,f}\subset\pi^{*}(J_{\chi,f,\gamma}) |  |

∎

Remarque II2. En fait, cette multiplicité algébrique m ​ a χ ​ ( f) ma_{\chi}(f) est le plus petit entier n n tel que I χ, f ⊃ ( x n + ε) ​ π ∗ ​ ( J χ, f, γ) I_{\chi,f}\supset(x^{n+\varepsilon})\pi^{*}(J_{\chi,f,\gamma}) pour tout ε > 0 \varepsilon>0 (dans l’anneau S ​ B 1, | q | SB^{1,|q|}). En effet, supposons que I χ, f ⊃ ( x m ​ a χ ​ ( f) − 1 + ε) ​ π ∗ ​ ( J χ, f, γ) I_{\chi,f}\supset(x^{ma_{\chi}(f)-1+\varepsilon})\pi^{*}(J_{\chi,f,\gamma}) pour tout ε > 0 \varepsilon>0. On a

 | f − f m ​ a χ ​ ( f) − 1 ∈ ( x m ​ a χ ​ ( f) − 1 + 2 ​ ε) ​ π ∗ ​ ( J χ, f, γ) f-f_{ma_{\chi}(f)-1}\in(x^{ma_{\chi}(f)-1+2\varepsilon})\pi^{*}(J_{\chi,f,\gamma}) |  |

pour ε > 0 \varepsilon>0 suffisament petit (par les mêmes raisonnements que ci-dessus). Donc

 | I χ, f ⊂ I χ, f m ​ a χ ​ ( f) − 1 + ( x m ​ a χ ​ ( f) − 1 + 2 ​ ε) ​ π ∗ ​ ( J χ, f, γ) I_{\chi,f}\subset I_{\chi,f_{ma_{\chi}(f)-1}}+(x^{ma_{\chi}(f)-1+2\varepsilon})\pi^{*}(J_{\chi,f,\gamma}) |  |

et en utilisant l’hypothèse ci-dessus

 | ( x m ​ a χ ​ ( f) − 1 + ε) ​ π ∗ ​ ( J χ, f, γ) ⊂ I χ, f m ​ a χ ​ ( f) − 1 + ( x m ​ a χ ​ ( f) − 1 + 2 ​ ε) ​ π ∗ ​ ( J χ, f, γ) (x^{ma_{\chi}(f)-1+\varepsilon})\pi^{*}(J_{\chi,f,\gamma})\subset I_{\chi,f_{ma_{\chi}(f)-1}}+(x^{ma_{\chi}(f)-1+2\varepsilon})\pi^{*}(J_{\chi,f,\gamma}) |  |

Par le lemme de Nakayama, on obtient

 | ( x m ​ a χ ​ ( f) − 1 + ε) ​ π ∗ ​ ( J χ, f, γ) ⊂ I χ, f m ​ a χ ​ ( f) − 1 (x^{ma_{\chi}(f)-1+\varepsilon})\pi^{*}(J_{\chi,f,\gamma})\subset I_{\chi,f_{ma_{\chi}(f)-1}} |  |

Mais ceci implique (par un raisonnement classique), que J χ, f, γ ⊂ J χ, f m ​ a χ ​ ( f) − 1, γ J_{\chi,f,\gamma}\subset J_{\chi,f_{ma_{\chi}(f)-1},\gamma}, ce qui contredit la définition de la multiplicité algébrique m ​ a χ ​ ( f) ma_{\chi}(f).

§8. Morphismes série formelle des algèbres Q ​ R ​ H p, q QR{H}^{p,q}.

Soit f ∈ Q ​ R ​ H p, q ​ ( x, α) f\in QR{H}^{p,q}(x,\alpha) et soit f ^ i = ∑ n ≥ 0 g i, n \widehat{f}^{i}=\sum_{n\geq 0}g_{i,n} une série formelle de f f relativement à la variable x i x_{i} (cf. Déf. IA5). Montrons qu’elle est unique. Notons f i, n = ∑ ℓ ≤ n g i, n f_{i,n}=\sum_{\ell\leq n}g_{i,n}. Soient h n ∈ S ​ B 0 p, | q | h_{n}\in SB_{0}^{p,|q|} tels que

 | f − f i, n = x i n ​ h n f-f_{i,n}=x_{i}^{n}h_{n} |  |

Soient U i, n ∈ ( ( ℝ + ⁣ ∗) p × ℝ | q |, 0) U_{i,n}\in((\mathbb{R}^{+*})^{p}\times\mathbb{R}^{|q|},0) une suite décroissante d’ouverts telle que f i, n f_{i,n} et h n h_{n} soient réalisées sur U i, n U_{i,n}. Soient x ( n) = ( x 1, n, …, x i − 1, n, 0, x i + 1, n, …, x p, n) x^{(n)}=(x_{1,n},\ldots,x_{i-1,n},0,x_{i+1,n},\ldots,x_{p,n}) tel que x j, n > 0 x_{j,n}>0 et ( x ( n), 0) (x^{(n)},0) appartient à l’intérieur de U ¯ i, n ∩ { x i = 0 } \overline{U}_{i,n}\cap\{x_{i}=0\} dans ℝ p + | q | − 1 \mathbb{R}^{p+|q|-1}. Le germe de f, f i, n f,f_{i,n} et h n h_{n} en ( x ( n), 0) (x^{(n)},0) est un élément d’une algèbre Q ​ R ​ H 1, q ′ ​ ( x i, α ′) QR{H}^{1,q^{\prime}}(x_{i},\alpha^{\prime}) (qui dépend de n n par les coordonnées analytiques α j ′ = x j − x j, n \alpha^{\prime}_{j}=x_{j}-x_{j,n} pour j ≠ i j\neq i). Le germe en ( x ( n), 0) (x^{(n)},0) de g i, ℓ g_{i,\ell} (pour ℓ ≤ n \ell\leq n), est un élément du ℝ ​ { α ′ } \mathbb{R}\{\alpha^{\prime}\} -module correspondant H ​ H ℓ ⊂ Q ​ R ​ H 1, q ′ ​ ( x i, α ′) H{H}_{\ell}\subset QR{H}^{1,q^{\prime}}(x_{i},\alpha^{\prime}). Donc, par le lemme II9, si f ≡ 0 f\equiv 0 alors f i, n ≡ 0 f_{i,n}\equiv 0, et ceci pour tout n n. Par conséquent la série f ^ i \widehat{f}^{i} est identiquement nulle. L’injectivité de ce morphisme série formelle est une conséquence facile de la propriété de quasi-analycité.

En partant de chaque série formelle f ^ i \widehat{f}^{i}, et en utilisant une récurrence sur p p, on construit une série formelle unique

 | f ^ ∈ c ∗ ​ ( ℝ ⁡ { α } ​ [[X]]) \widehat{f}\in c^{*}(\mathbb{R}\{\alpha\}[[X]]) |  |

au sens suivant: pour tout n n

 | f − 𝕛 X n ​ ( f ^) ∈ M x n ​ S ​ B 0 p, | q | f-{\mathbb{j}}^{n}_{X}(\widehat{f})\in{M}^{n}_{x}SB_{0}^{p,|q|} |  |

où M x {M}_{x} est l’idéal de S ​ B p, | q | SB^{p,|q|} engendré par les coordonnées x 1, …, x p x_{1},\ldots,x_{p}. Pour prouver l’unicité de cette série, il suffit de se placer dans n’importe quel carte projective dans la coordonnée x x, par exemple: x 1 = y 1 x_{1}=y_{1} et x i = y i ​ y 1 x_{i}=y_{i}y_{1} pour i ≠ 1 i\neq 1. On utilise alors la méthode de la première partie de ce paragraphe, aux voisinages de points tels que y 1 = 0, α = 0 y_{1}=0,\ \alpha=0 et y i, n > 0 y_{i,n}>0 pour i ≠ 1 i\neq 1. Les formules suivantes (obtenues par un calcul direct)

 | z i, j ​ ( x i, μ j) = z i, j ​ ( y i, μ j) ​ y 1 + ( y i + μ j ​ z i, j ​ ( y i, μ j)) ​ z 1, j ​ ( y 1, μ j) z_{i,j}(x_{i},\mu_{j})=z_{i,j}(y_{i},\mu_{j})y_{1}+(y_{i}+\mu_{j}z_{i,j}(y_{i},\mu_{j}))z_{1,j}(y_{1},\mu_{j}) |  |

montrent que les jets dans les fonctions élémentaires X 1 ​ ( y 1, μ) X_{1}(y_{1},\mu), sont préservés (les fonctions z i, j ​ ( y i, μ j) z_{i,j}(y_{i},\mu_{j}) sont analytiques dans les coordonnées y i − y i, n y_{i}-y_{i,n}). L’injectivité de ce morphisme est encore une conséquence facile de la propriété de quasi-analycité.

III. Action de la dérivation χ = x ∂ / ∂ x − ∑ j = 1 ℓ s j ( α) u j ∂ / ∂ u j \chi=x\partial/\partial x-\sum_{j=1}^{\ell}s_{j}(\alpha)u_{j}\partial/\partial u_{j}

Soient α = ( μ, ν) \alpha=(\mu,\nu) des coordonnées sur ℝ q 1 × ℝ q 2 {\mathbb{\mathbb{R}}}^{q_{1}}\times{\mathbb{\mathbb{R}}}^{q_{2}} et soit u u une coordonnée sur ℝ ℓ {\mathbb{\mathbb{R}}}^{\ell}. Posons α ′ = ( α, u) \alpha^{\prime}=(\alpha,u) et q = ( q 1, q 2 + ℓ) q=(q_{1},q_{2}+\ell). On veut étudier l’action de la dérivation χ \chi sur l’algèbre Q ​ R ​ H 1, q ​ ( x, α ′) QR{H}^{1,q}(x,\alpha^{\prime}). Les germes s j s_{j} sont analytiques et on suppose pour simplifier la présentation que s j ​ ( α) = 1 + μ j s_{j}(\alpha)=1+\mu_{j}. Soit U ∈ ( ℝ + ⁣ ∗ × ℝ | q |, 0) U\in({\mathbb{\mathbb{R}}}^{+*}\times{\mathbb{\mathbb{R}}}^{|q|},0) un ouvert tel que le sous-ensemble γ = { ( x, α ′) ∈ U; α ′ = 0 } \gamma=\{(x,\alpha^{\prime})\in U;\ \alpha^{\prime}=0\} soit connexe. C’est une orbite principale de χ \chi dans U U. Soit π χ \pi_{\chi} (le germe de) la projection intégrale de χ \chi dans U U. Quitte à réduire U U, l’espace π χ ​ ( U) \pi_{\chi}(U) s’identifie à une transversale analytique à γ \gamma: W = { x = x 0 > 0 } W=\{x=x_{0}>0\}. Des coordonnées analytiques naturelles sur W W sont les intégrales premières de χ \chi, c’est à dire la coordonnée α \alpha et les (coordonnées) germes

 | λ j ​ ( x, α ′) = x s j ​ ( α) ​ u j ∈ Q ​ R ​ H 1, q \lambda_{j}(x,\alpha^{\prime})=x^{s_{j}(\alpha)}u_{j}\in QR{H}^{1,q} |  |

Les idéaux χ \chi -transverses le long de γ \gamma sont donc des idéaux de l’anneau ℝ ​ { α, λ } \mathbb{R}\{\alpha,\lambda\}, et on a le morphisme étoilé π χ ∗: ℝ ⁡ { α, λ } → S ​ B 1, | q | ​ ( x, α, u) \pi_{\chi}^{*}:\mathbb{R}\{\alpha,\lambda\}\to SB^{1,|q|}(x,\alpha,u).

La question qui se pose est: l’algèbre Q ​ R ​ H 1, q QR{H}^{1,q} est-elle χ \chi -finie? Le problème est ouvert. Cependant, on montre dans cette section, qu’elle est localement χ \chi -finie.

A. Etude globale et théorème principal 2.

Le germe en 0 de la projection π χ \pi_{\chi} n’est pas isomorphe à celui d’une projection linéaire, d’où des difficultés nouvelles dans l’étude de cette action. La première difficulté apparaît dans l’étude de l’action formelle de χ \chi.

§1. Action formelle.

Notons r = ( 1, ( 1 + μ j)) r=(1,(1+\mu_{j})) et s = ( s j) s=(s_{j}). Les valeurs propres de l’opérateur χ \chi sont

 | e m, n ​ ( α) = ⟨ m, r ⟩ − ⟨ n, s ⟩ e_{m,n}(\alpha)=\langle m,r\rangle-\langle n,s\rangle |  |

Les monômes X m ​ u n X^{m}u^{n} satisfont aux équations différentielles

 | χ ⁡ ( X m ​ u n) = e m, n ​ X m ​ u n + monômes ≻ \chi(X^{m}u^{n})=e_{m,n}X^{m}u^{n}+\text{monômes}\succ |  |

pour un ordre ≺ \prec adéquat sur ces monômes (induit par l’ordre sur les monômes X m X^{m}). Le degré d’un monôme X m ​ u n X^{m}u^{n} relativement à χ \chi est | m | − | n | |m|-|n|. Soit c c l’immersion

 | c ⁡ ( x, α, u) = ( X ⁡ ( x, μ), α, u) c(x,\alpha,u)=(X(x,\mu),\alpha,u) |  |

###### Définition IIIA1

On note H ​ H ^ p ⊂ c ∗ ​ ( ℝ ⁡ { α } ​ [[X, u]]) \widehat{H{H}}_{p}\subset c^{*}(\mathbb{R}\{\alpha\}[[X,u]]) le ℝ ​ { α } \mathbb{R}\{\alpha\} -module des séries de monômes de degré p ∈ ℤ p\in\mathbb{Z}. Ses éléments sont dits blocs χ \chi -homogènes formels de degré p p.

Dans l’action de χ 0 = x ∂ / ∂ x \chi_{0}=x\partial/\partial x (cf. section II), on a montré l’existence d’une application série formelle injective. Par une construction explicite, on en déduit facilement le

###### Lemme IIIA1

Il existe une application série doublement formelle et injective

 | f ∈ Q ​ R ​ H 1, q → f ^ = ∑ p ∈ ℤ g p ​ ( f) ∈ ∑ p ∈ ℤ H ​ H ^ p f\in QR{H}^{1,q}\to\widehat{f}=\sum_{p\in\mathbb{Z}}g_{p}(f)\in\sum_{p\in\mathbb{Z}}\widehat{H{H}}_{p} |  |

Preuve. Soit f ∈ Q ​ R ​ H 1, q ​ ( x, α ′) f\in QR{H}^{1,q}(x,\alpha^{\prime}). Sous l’action du champ χ 0 \chi_{0}, on lui associe une unique série formelle

 | f ^ 0 = ∑ M ≥ 0 g 0, M ​ ( f) \widehat{f}^{0}=\sum_{M\geq 0}g_{0,M}(f) |  | 1 |

où g 0, M g_{0,M} est un bloc χ 0 \chi_{0} -homogène de degré M M, i.e

 | g 0, M = ∑ | m | = M a m ​ ( α ′) ​ X m g_{0,M}=\sum_{|m|=M}a_{m}(\alpha^{\prime})X^{m} |  |

Or g 0, M ​ ( f) ∈ Q ​ R ​ H c ​ v ​ g 1, q ​ ( x, α ′) g_{0,M}(f)\in QR{H}^{1,q}_{cvg}(x,\alpha^{\prime}), on lui associe donc une unique série convergente

 | g 0, M ​ ( f) = ∑ p ≤ M g p ​ ( g 0, M ​ ( f)) g_{0,M}(f)=\sum_{p\leq M}g_{p}(g_{0,M}(f)) |  | 2 |

où g p ​ ( g 0, M ​ ( f)) g_{p}(g_{0,M}(f)) est un bloc χ \chi -homogène convergent de dgré p p. Les blocs formels g p ​ ( f) g_{p}(f) sont donnés par

 | g p ​ ( f) = ∑ M ≥ p g p ​ ( g 0, M ​ ( f)) g_{p}(f)=\sum_{M\geq p}g_{p}(g_{0,M}(f)) |  |

Cette application est injective comme les applications (1) et (2).∎

L’anneau c ∗ ​ ( ℝ ⁡ [[X, α ′]]) ↩ c ∗ ​ ( ℝ ⁡ { α } ​ [[X, u]]) c^{*}(\mathbb{R}[[X,\alpha^{\prime}]])\hookleftarrow c^{*}(\mathbb{R}\{\alpha\}[[X,u]]) est noethérien. Grâce au théorème d’intersection de Krull et au lemme d’Artin-Ress ([L]), on va montrer que toute série f ^ \widehat{f} est χ \chi -équivalente à une somme finie de blocs χ \chi -homogènes (par des raisonnements abondamment employés dans la section II). Là apparaissent les premières difficultés de cette action: ces blocs χ \chi -homogènes g p ​ ( f) g_{p}(f) peuvent être formels, et même en cas de convergence d’un bloc g p g_{p}, les valeurs propres correspondantes e m, n e_{m,n} peuvent avoir des points d’accumulation dans ℤ ∖ { p } {\mathbb{\mathbb{Z}}}\setminus\{p\}.

###### Lemme IIIA2

Soit e ⁡ ( α) e(\alpha) un germe analytique en 0, tel que e ⁡ ( 0) ≠ p e(0)\neq p, et soit l’opérateur E = χ − e ​ Id E=\chi-e\text{Id}. Pour tout g ∈ H ​ H ^ p g\in\widehat{H{H}}_{p}, on a I χ, E ​ g = I χ, g I_{\chi,Eg}=I_{\chi,g} dans l’anneau c ∗ ​ ( ℝ ⁡ [[X, α ′]]) c^{*}(\mathbb{R}[[X,\alpha^{\prime}]]).

Preuve. Il suffit de montrer que I χ, g ⊂ I χ, E ​ g I_{\chi,g}\subset I_{\chi,Eg}. Soit G k = 𝕛 u k ​ ( g) G_{k}={\mathbb{j}}^{k}_{u}(g). Comme la dérivation χ \chi est diagonale dans la coordonnée u u, on a 𝕛 u k ​ ( E ​ g) = E ​ G k {\mathbb{j}}^{k}_{u}(Eg)=EG_{k}. Or le germe G k G_{k} est dans le noyau de l’opérateur

 | ∏ | m | − | n | = p, | n | ≤ k ( χ − e m, n ​ I ​ d) \prod_{|m|-|n|=p,\hskip 8.19447pt|n|\leq k}(\chi-e_{m,n}Id) |  |

comme e ⁡ ( 0) ≠ p e(0)\neq p, on montre par les mêmes arguments que dans le lemme II5 que I χ, E ​ G k = I χ, G k I_{\chi,EG_{k}}=I_{\chi,G_{k}}. Soit M {M} l’idéal maximal de c ∗ ​ ( ℝ ⁡ [[X, α ′]]) c^{*}(\mathbb{R}[[X,\alpha^{\prime}]]). On a donc pour tout k

 | I χ, g ⊂ I χ, E ​ g + M k I_{\chi,g}\subset I_{\chi,Eg}+{M}^{k} |  |

on obtient le résultat par le théorème d’intersection de Krull.∎

###### Lemme IIIA3

Notons f p 1, p 2 = ∑ p 1 ≤ p ≤ p 2 g p ​ ( f) f_{p_{1},p_{2}}=\sum_{p_{1}\leq p\leq p_{2}}g_{p}(f), alors I χ, f p 1, p 2 ⊂ I χ, f p 1, p 2 + 1 I_{\chi,f_{p_{1},p_{2}}}\subset I_{\chi,f_{p_{1},p_{2}+1}}.

Preuve. Le germe 𝕛 u k ​ ( f p 1, p 2) {\mathbb{j}}^{k}_{u}(f_{p_{1},p_{2}}) est dans le noyau de l’opérateur

 | ∏ p 1 ≤ | m | − | n | ≤ p 2; | n | ≤ k ( χ − e m, n ​ I ​ d) \prod_{p_{1}\leq|m|-|n|\leq p_{2};\hskip 8.19447pt|n|\leq k}(\chi-e_{m,n}Id) |  |

et par le lemme IIIA2, on a

 | I χ, g p 2 + 1 ⊂ I χ, f p 1, p 2 + 1 + M k I_{\chi,g_{p_{2}+1}}\subset I_{\chi,f_{p_{1},p_{2}+1}}+{M}^{k} |  |

on conclut par le théorème d’intersection de Krull.∎

###### Lemme IIIA4

Il existe p 1, p 2 ∈ ℤ p_{1},p_{2}\in\mathbb{Z} tels que f ^ ≡ f p 1, p 2 [c ∗ ​ ( M OPEN X, u)) ​ I χ, f p 1, p 2] \widehat{f}\equiv f_{p_{1},p_{2}}\quad[c^{*}({M}_{X,u)})I_{\chi,f_{p_{1},p_{2}}}].

Preuve. D’après le lemme IIIA3, la suite d’idéaux ( I χ, f − p, p) (I_{\chi,f_{-p,p}}) est croissante et par le théorème d’intersection de Krull, sa limite est l’idéal différentiel de f ^ \widehat{f}. Donc pour tout p ∈ ℤ p\in\mathbb{Z}, on a I χ, g p ​ ( f) ⊂ I χ, f ^ I_{\chi,g_{p}(f)}\subset I_{\chi,\widehat{f}}. Soit k 1 k_{1} et k 2 k_{2} les exposants d’Artin-Ress des idéaux M u {M}_{u} et c ∗ ​ ( M X) c^{*}({M}_{X}) dans l’idéal I χ, f ^ I_{\chi,\widehat{f}}. Il suffit de prendre p 1 = − k 1 p_{1}=-k_{1} et p 2 = k 2 p_{2}=k_{2}.∎

§2. Multiplicité algébrique et la double inclusion.

Soit f ∈ Q ​ R ​ H 1, q ​ ( x, α, u) f\in QR{H}^{1,q}(x,\alpha,u). Dans l’action de χ 0 \chi_{0} sur Q ​ R ​ H 1,. QR{H}^{1,.}, la première inclusion est établie grâce à la structure asymptotique de Q ​ R ​ H 1,. QR{H}^{1,.} (bien adaptée à χ 0 \chi_{0}), et à la notion de multiplicité algébrique: c’est le plus petit entier m m tel que pour tout ε > 0 \varepsilon>0, ( x m + ε) ​ π χ 0 ∗ ​ ( J χ 0, f, γ 0) ⊂ I χ 0, f (x^{m+\varepsilon})\pi_{\chi_{0}}^{*}(J_{\chi_{0},f,\gamma_{0}})\subset I_{\chi_{0},f} dans l’anneau S ​ B 1,. SB^{1,.} correspondant. C’est aussi l’indice de stationnarité de la suite des idéaux χ 0 \chi_{0} -transverses des éléments de la série de f f relativement à χ 0 \chi_{0}. D’après l’étude de l’action formelle de χ \chi, cette structure asymptotique n’est plus adaptée à χ \chi et les les sous-espaces stables H ​ H ^ p \widehat{H{H}}_{p} sont formels. Ceci motive la

###### Définition IIIA2

Soit f ^ = ∑ p ∈ ℤ g p ​ ( f) \widehat{f}=\sum_{p\in\mathbb{Z}}g_{p}(f) la série de f f relativement à χ \chi. Le germe f f est dit quasi-convergent si g p ​ ( f) ∈ Q ​ R ​ H c ​ v ​ g 1, q g_{p}(f)\in QR{H}^{1,q}_{cvg} pour tout p p. On note Q ​ R ​ H 𝕢 ​ c ​ v ​ g 1, q QR{H}^{1,q}_{{\mathbb{q}cvg}} le ℝ ​ { α } \mathbb{R}\{\alpha\} -module correspondant.

Soit f ∈ Q ​ R ​ H q ​ c ​ v ​ g 1, q f\in QR{H}^{1,q}_{qcvg}. Les sommes finies correspondantes f p 1, p 2 f_{p_{1},p_{2}} sont des éléments de l’anneau restriction analytique Q ​ R ​ H c ​ v ​ g 1, q QR{H}^{1,q}_{cvg}. Les lemmes IIIA2 et IIIA3 s’appliquent sur cet anneau. Soit I f I_{f} l’idéal limite différentiel de la suite ( I χ, f − p, p) p ∈ ℤ (I_{\chi,f_{-p,p}})_{p\in\mathbb{Z}}, et soit J f J_{f} l’idéal limite transverse de la suite ( J χ, f − p, p, γ) p ∈ ℤ (J_{\chi,f_{-p,p},\gamma})_{p\in\mathbb{Z}}. On obtient (en utilisant les lemmes IIIA2 et IIIA3, et les raisonnements de la section II)

 | I f = ∑ p ∈ ℤ I χ, g p ​ ( f) et J f = ∑ p ∈ ℤ J χ, g p ​ ( f), γ I_{f}=\sum_{p\in\mathbb{Z}}I_{\chi,g_{p}(f)}\quad\text{et}\quad J_{f}=\sum_{p\in\mathbb{Z}}J_{\chi,g_{p}(f),\gamma} |  |

Il s’agit de comparer les idéaux I f I_{f} et I χ, f I_{\chi,f} dans l’anneau S ​ B 1, | q | SB^{1,|q|}, et les idéaux J f J_{f} et J χ, f, γ J_{\chi,f,\gamma} dans l’anneau ℝ ​ { α, λ } \mathbb{R}\{\alpha,\lambda\}. Soit M ′ {M}^{\prime} l’idéal maximal de ℝ ​ { α, λ } \mathbb{R}\{\alpha,\lambda\} et soit K ⁡ ( M λ ′, J f) K({M}^{\prime}_{\lambda},J_{f}) l’exposant d’Artin-Ress de l’idéal M λ ′ = ⟨ λ 1, …, λ ℓ ⟩ ⊂ ℝ ⁡ { α, λ } {M}^{\prime}_{\lambda}=\langle\lambda_{1},\ldots,\lambda_{\ell}\rangle\subset\mathbb{R}\{\alpha,\lambda\}, dans l’idéal J f J_{f}. Soit p 0 p_{0} le plus petit des entiers p ≥ − K p\geq-K tel que J χ, g p, γ ⊄ M ′ ​ J f J_{\chi,g_{p},\gamma}\not\subset{M}^{\prime}J_{f}.

###### Définition IIIA3

La multiplicité algébrique m ​ a χ ​ ( f) ma_{\chi}(f) est l’indice p p de stationnarité de la suite croissante des idéaux ( J χ, f p 0, p, γ) p ≥ p 0 (J_{\chi,f_{p_{0},p},\gamma})_{p\geq p_{0}}. La multiplicité algébrique positive est m ​ a χ + ​ ( f) = max ⁡ { m ​ a χ ​ ( f), 0 } ma^{+}_{\chi}(f)=\max\{ma_{\chi}(f),0\}.

Cette multiplicité algébrique est invariante dans les perturbations de f f dans l’idéal π χ ∗ ​ ( M ′ ​ J f) ∩ Q ​ R ​ H q ​ c ​ v ​ g 1, q \pi_{\chi}^{*}({M}^{\prime}J_{f})\cap QR{H}^{1,q}_{qcvg}. Ceci permet d’étendre Q ​ R ​ H q ​ c ​ v ​ g 1, q QR{H}^{1,q}_{qcvg} en une classe d’éléments possédant la notion de multiplicité algébrique

###### Définition IIIA4

Un germe f ∈ Q ​ R ​ H 1, q f\in QR{H}^{1,q} est dit presque quasi-convergent s’il est limite dans la M ( α, u) {M}_{(\alpha,u)} -topologie de S ​ B 1, | q | SB^{1,|q|}, d’une suite ( f n) n (f_{n})_{n} de germes quasi-convergents, dont la suite des idéaux limites transverses ( J f n) n (J_{f_{n}})_{n} est croissante.

###### Lemme et définition IIIA5

Tout germe f f presque quasi-convergent possède une multiplicité algébrique m ​ a χ ​ ( f) ma_{\chi}(f) qui est la limite de la suite ( m ​ a χ ​ ( f n)) n (ma_{\chi}(f_{n}))_{n}, et un idéal limite transverse J f J_{f} qui est la limite de la suite ( J f n) (J_{f_{n}}).

Preuve. Montrons que les suites ( m ​ a χ ​ ( f n)) (ma_{\chi}(f_{n})) et ( J f n) (J_{f_{n}}) admettent des limites qui ne dépendent que de f f. Soit J J l’idéal limite de la suite ( J f n) (J_{f_{n}}) d’indice de stationnarité n 0 n_{0} et soit K K l’exposant d’Artin-Ress de l’idéal M ( α, λ) ′ {M}^{\prime}_{(\alpha,\lambda)} dans J J. Soit k > K k>K, pour n n assez grand et n ′ > n n^{\prime}>n, on a f n ′ − f n ∈ M ( α, u) k f_{n^{\prime}}-f_{n}\in{M}_{(\alpha,u)}^{k}, et donc g p ​ ( f n ′) − g p ​ ( f n) ∈ M ( α, u) k g_{p}(f_{n^{\prime}})-g_{p}(f_{n})\in{M}_{(\alpha,u)}^{k} pour tout p ∈ ℤ p\in\mathbb{Z}. Par conséquent, si n ≥ n 0 n\geq n_{0}, on a J χ, g p ​ ( f n ′), γ ⊂ J χ, g p ​ ( f n), γ + M ′ ​ J J_{\chi,g_{p}(f_{n^{\prime}}),\gamma}\subset J_{\chi,g_{p}(f_{n}),\gamma}+{M}^{\prime}J et J χ, g p ​ ( f n), γ ⊂ J χ, g p ​ ( f n ′), γ + M ′ ​ J J_{\chi,g_{p}(f_{n}),\gamma}\subset J_{\chi,g_{p}(f_{n^{\prime}}),\gamma}+{M}^{\prime}J. En sommant sur p p la première inclusion par exemple, on obtient

 | J = ∪ p ≤ m ​ a χ ​ ( f n ′) J χ, g p ​ ( f n ′), γ ⊂ ∪ p ≤ m ​ a χ ​ ( f n ′) J χ, g p ​ ( f n), γ + M ′ J J=\cup_{p\leq ma_{\chi}(f_{n^{\prime}})}J_{\chi,g_{p}(f_{n^{\prime}}),\gamma}\subset\cup_{p\leq ma_{\chi}(f_{n^{\prime}})}J_{\chi,g_{p}(f_{n}),\gamma}+{M}^{\prime}J |  |

le lemme de Nakayama et la définition de J = J f n J=J_{f_{n}} donnent m ​ a χ ​ ( f n) ≤ m ​ a χ ​ ( f n ′) ma_{\chi}(f_{n})\leq ma_{\chi}(f_{n^{\prime}}). La deuxième inclusion donne l’inégalité inverse. La suite ( m ​ a χ ​ ( f n)) (ma_{\chi}(f_{n})) est donc stationnaire. Notons m ​ a ma sa limite.

Soit ( f n ′) (f^{\prime}_{n}) une autre suite de germes quasi-convergents qui tend vers f f dans la M ( α, u) {M}_{(\alpha,u)} -topologie et dont la suite des idéaux limites ( J f n ′) (J_{f^{\prime}_{n}}) est croissante. Soit J ′ J^{\prime} son idéal limite d’indice de stationnarité n 0 ′ n^{\prime}_{0} et soit m ​ a ′ ma^{\prime} la limite de la suite ( m ​ a χ ​ ( f n ′)) (ma_{\chi}(f^{\prime}_{n})). Montrons que J ′ = J J^{\prime}=J et m ​ a ′ = m ​ a ma^{\prime}=ma. Pour tout k k et n ≥ max ⁡ ( n 0, n 0 ′) n\geq\max(n_{0},n^{\prime}_{0}) assez grand, on a f n ′ − f n ∈ M ( α, u) k f^{\prime}_{n}-f_{n}\in{M}_{(\alpha,u)}^{k} et donc g p ​ ( f n ′) − g p ​ ( f n) ∈ M ( α, u) k g_{p}(f^{\prime}_{n})-g_{p}(f_{n})\in{M}_{(\alpha,u)}^{k} pour tout p p. Par conséquent, J ′ ⊂ J + ( M ′) k J^{\prime}\subset J+({M}^{\prime})^{k} et J ⊂ J ′ + ( M ′) k J\subset J^{\prime}+({M}^{\prime})^{k} pour tout k k. Par le théorème d’intersection de Krull, on obtient J ′ = J J^{\prime}=J. Notons J f J_{f} cet idéal. En appliquant le raisonnement ci-dessus à f n ′ − f n f^{\prime}_{n}-f_{n} et à J f J_{f}, on obtient m ​ a ′ = m ​ a ma^{\prime}=ma.∎

Soit W 0 ⊂ W W_{0}\subset W un semi-analytique de l’anneau ℝ ​ { α, λ } \mathbb{R}\{\alpha,\lambda\} qui adhère à 0. Soit U 0 = π χ − 1 ​ ( W 0) U_{0}=\pi_{\chi}^{-1}(W_{0}). On définit de la même façon, une multiplicité algébrique restreinte m a χ ( f | U 0) ma_{\chi}(f_{|U_{0}}) en considérant les idéaux χ \chi -transverses et leurs idéaux limites dans l’anneau restriction ℝ { α, λ } | W 0 \mathbb{R}\{\alpha,\lambda\}_{|W_{0}}. On verra dans la partie B que tout f ∈ Q ​ R ​ H 1, q f\in QR{H}^{1,q} admet une localisation finie dans laquelle il est (à extension étoilée près), presque quasi-convergent, et donc possède une multiplicité algébrique restreinte.

§2.1. Exemples de germes quasi-convergents.

Omettons les exposants 1, q 1,q et 1, | q | 1,|q| pour un moment.

(a) La sous-algèbre intégrale-linéaire Λ ∗ ​ ( Q ​ R ​ H 1, q ​ ( x, α, λ)) \Lambda^{*}(QR{H}^{1,q}(x,\alpha,\lambda)).

Soit U 0 ∈ ( ℝ + ⁣ ∗ × ℝ | q |, 0) U_{0}\in(\mathbb{R}^{+*}\times\mathbb{R}^{|q|},0) et soit Λ \Lambda le difféomorphisme sur U U définie par

 | Λ ⁡ ( x, α, u) = ( x, α, λ ⁡ ( x, α, u)) ∈ U 0 \Lambda(x,\alpha,u)=(x,\alpha,\lambda(x,\alpha,u))\in U_{0} |  |

L’image Λ ⁡ ( U) \Lambda(U) étant ouverte, le morphisme Λ ∗: S ​ B 1, | q | ​ ( x, α, λ) → S ​ B 1, | q | ​ ( x, α, u) \Lambda^{*}:SB^{1,|q|}(x,\alpha,\lambda)\to SB^{1,|q|}(x,\alpha,u) est injectif, la sous-algèbre Q ​ R ​ H 1, q ​ ( x, α, λ) QR{H}^{1,q}(x,\alpha,\lambda) est donc isomorphe à la sous-algèbre

 | Λ ∗ ​ ( Q ​ R ​ H 1, q ​ ( x, α, λ) ⊂ Q ​ R ​ H 1, q ​ ( x, α, u) CLOSE \Lambda^{*}(QR{H}^{1,q}(x,\alpha,\lambda)\subset QR{H}^{1,q}(x,\alpha,u) |  |

(l’inclusion s’obtient en remarquant que x s j = x + μ j ​ z ​ ( x, μ j) x^{s_{j}}=x+\mu_{j}z(x,\mu_{j})). Le champ Λ ∗ ​ χ \Lambda_{*}\chi coincide avec la restriction à Λ ⁡ ( U) \Lambda(U) du champ χ 0 \chi_{0} et le diagramme suivant est commutatif

 | S ​ B ​ ( x, α, λ) → Λ ∗ S ​ B ​ ( x, α, u) χ 0 ↓ ↓ χ S ​ B ​ ( x, α, λ) → Λ ∗ S ​ B ​ ( x, α, u) \begin{CD}SB(x,\alpha,\lambda)@>{\Lambda^{*}}>{}>SB(x,\alpha,u)\\ @V{\chi_{0}}V{}V@V{}V{\chi}V\\ SB(x,\alpha,\lambda)@>{\Lambda^{*}}>{}>SB(x,\alpha,u)\end{CD} |  | ∗ |

###### Lemme IIIA6

Λ ∗ ​ ( Q ​ R ​ H ​ ( x, α, λ)) ⊂ Q ​ R ​ H q ​ c ​ v ​ g \Lambda^{*}(QR{H}(x,\alpha,\lambda))\subset QR{H}_{qcvg}.

Preuve. Soit F ∈ Q ​ R ​ H ​ ( x, α, λ) F\in QR{H}(x,\alpha,\lambda) et soit f = Λ ∗ ​ ( F) f=\Lambda^{*}(F). Soit f ^ = ∑ p ∈ ℤ g p ​ ( f) \widehat{f}=\sum_{p\in\mathbb{Z}}g_{p}(f) la série formelle de f f relativement à χ \chi, et soit F ^ = ∑ p ≥ 0 g 0, p ​ ( F) \widehat{F}=\sum_{p\geq 0}g_{0,p}(F) la série formelle de F F relativement à χ 0 \chi_{0}. Prolongeons le morphisme Λ ∗ \Lambda^{*} aux séries formelles: Λ ∗ ​ ( F ^) = ∑ p Λ ∗ ​ ( g 0, p ​ ( F)) \Lambda^{*}(\widehat{F})=\sum_{p}\Lambda^{*}(g_{0,p}(F)). D’après le diagramme ci-dessus, l’image par Λ ∗ \Lambda^{*} d’un sous-espace stable par χ 0 \chi_{0}, est incluse dans un sous-espace stable par χ \chi: plus précisément, pour p ≥ 0 p\geq 0, Λ ∗ ​ ( H ​ H p) ⊂ H ​ H ^ p ∩ Q ​ R ​ H c ​ v ​ g \Lambda^{*}(H{H}_{p})\subset\widehat{H{H}}_{p}\cap QR{H}_{cvg}. Donc, en utilisant les formules (1) et (2) du lemme IIIA1, qui définissent la série de f f, on obtient g p ​ ( f) = Λ ∗ ​ ( g 0, p ​ ( F)) ∈ Q ​ R ​ H c ​ v ​ g g_{p}(f)=\Lambda^{*}(g_{0,p}(F))\in QR{H}_{cvg}, pour p ≥ 0 p\geq 0 et g p ​ ( f) = 0 g_{p}(f)=0 pour p < 0 p<0. En effet, écrivons

 | g 0, p ​ ( F) = ∑ | n | = p, | m | ≥ 0 b n, m ​ ( α) ​ λ m ​ X n g_{0,p}(F)=\sum_{|n|=p,|m|\geq 0}b_{n,m}(\alpha)\lambda^{m}X^{n} |  |

les séries ∑ | m | ≥ 0 b n, m ​ ( α) ​ λ m \sum_{|m|\geq 0}b_{n,m}(\alpha)\lambda^{m} étant convergentes sur un voisinage de 0. Soit

 | ∑ M ≥ 0 F M avec F M = ∑ | n | + | m | = M b n, m ​ ( α) ​ X n ​ λ m \sum_{M\geq 0}F_{M}\quad\text{avec}\quad F_{M}=\sum_{|n|+|m|=M}b_{n,m}(\alpha)X^{n}\lambda^{m} |  |

la série de F F dans les variables ( X, λ) (X,\lambda). Elle est bien définie d’après la série F ^ \widehat{F} et l’analycité dans les coordonnées λ \lambda. Le germe Λ ∗ ​ ( F M) \Lambda^{*}(F_{M}) est un bloc χ 0 \chi_{0} -homogène de degré M M. De plus, on vérifie facilement que pour tout M M

 | Λ ∗ ​ ( F − ∑ M ′ ≤ M F M ′) = o ⁡ ( x M) dans l’anneau ​ S ​ B \Lambda^{*}(F-\sum_{M^{\prime}\leq M}F_{M^{\prime}})=o(x^{M})\quad\text{dans l'anneau}\ SB |  |

Ceci prouve que Λ ∗ ​ ( F M) = g 0, M ​ ( f) \Lambda^{*}(F_{M})=g_{0,M}(f). Or, il est facile de voir que g p ​ ( g 0, M ​ ( f)) = 0 g_{p}(g_{0,M}(f))=0 si p < 0 p<0 ou p > M p>M, et que g p ​ ( g 0, M ​ ( f)) = ∑ | n | = p, | m | = M − p Λ ∗ ​ ( b n, m ​ X n ​ λ m) g_{p}(g_{0,M}(f))=\sum_{|n|=p,|m|=M-p}\Lambda^{*}(b_{n,m}X^{n}\lambda^{m}) pour 0 ≤ p ≤ M 0\leq p\leq M. D’après la formule (2), on a

 | g p ​ ( f) = ∑ M ≥ p g p ​ ( g 0, M ​ ( f)) = ∑ M ≥ p ( ∑ | n | = p, | m | = M − p Λ ∗ ​ ( b n, m ​ X n ​ λ m)) g_{p}(f)=\sum_{M\geq p}g_{p}(g_{0,M}(f))=\sum_{M\geq p}(\sum_{|n|=p,|m|=M-p}\Lambda^{*}(b_{n,m}X^{n}\lambda^{m})) |  |

donc

 | g p ​ ( f) = Λ ∗ ​ ( g 0, p ​ ( F)) g_{p}(f)=\Lambda^{*}(g_{0,p}(F)) |  |

et ceci finit la preuve du lemme.∎

Soit γ 0 = Λ ⁡ ( γ) \gamma_{0}=\Lambda(\gamma), elle est principale dans U 0 U_{0}, et le morphisme Λ \Lambda est un difféomorphisme de U U sur un voisinage de γ 0 \gamma_{0}. En identifiant les intégrales premières de χ \chi et χ 0 \chi_{0}, on obtient le diagramme commutatif

 | U → π χ W Λ ↓ ↓ i ​ d U 0 → π χ 0 W \begin{CD}U@>{\pi_{\chi}}>{}>W\\ @V{\Lambda}V{}V@V{}V{id}V\\ U_{0}@>{\pi_{\chi_{0}}}>{}>W\end{CD} |  | ∗ ⁣ ∗ |

Les idéaux χ \chi -transverse et χ 0 \chi_{0} -transverse coincident (lemme de transfert IB6). Donc si F ∈ Q ​ R ​ H ​ ( x, α, λ) F\in QR{H}(x,\alpha,\lambda) et si f = Λ ∗ ​ ( F) f=\Lambda^{*}(F), on a J χ, f, γ = J χ 0, F, γ 0 J_{\chi,f,\gamma}=J_{\chi_{0},F,\gamma_{0}} ( = J F =J_{F} d’après le théorème principal II1). Or, on a J F = J f J_{F}=J_{f} d’après la définition de l’idéal limite transverse, et les séries de f f et F F. Et donc m ​ a χ ​ ( f) = m ​ a χ 0 ​ ( F) ≥ 0 ma_{\chi}(f)=ma_{\chi_{0}}(F)\geq 0. On a aussi I f = Λ ∗ ​ ( I F) = Λ ∗ ​ ( I χ 0, F) = I χ, f I_{f}=\Lambda^{*}(I_{F})=\Lambda^{*}(I_{\chi_{0},F})=I_{\chi,f} en utilisant le diagramme (*). Par conséquent, en appliquant le morphisme Λ ∗ \Lambda^{*} à la double inclusion

 | ( x m ​ a χ 0 ​ ( F) + ε) ​ π χ 0 ∗ ​ ( J F) ⊂ I χ 0, F ⊂ π χ 0 ∗ ​ ( J F) (x^{ma_{\chi_{0}}(F)+\varepsilon})\pi_{\chi_{0}}^{*}(J_{F})\subset I_{\chi_{0},F}\subset\pi_{\chi_{0}}^{*}(J_{F}) |  |

et en utilisant le diagramme (**), on obtient la généralisation facile du théorème principal II1

###### Lemme IIIA7

L’algèbre Λ ∗ ​ ( Q ​ R ​ H ​ ( x, α, λ)) \Lambda^{*}(QR{H}(x,\alpha,\lambda)) est χ \chi -finie et satisfait à la double inclusion. Elle est χ \chi -équivalente à la sous-algèbre Λ ∗ ​ ( Q ​ R ​ H c ​ v ​ g ​ ( x, α, λ)) \Lambda^{*}(QR{H}_{cvg}(x,\alpha,\lambda)).

(b) La sous-algèbre algébrique Q ​ R ​ H ​ ( x, α) ​ [u] QR{H}(x,\alpha)[u]. Elle est clairement incluse dans Q ​ R ​ H q ​ c ​ v ​ g QR{H}_{qcvg} (les blocs χ \chi -homogènes sont algébriques dans les variales ( X, u) (X,u)). Soit f ∈ Q ​ R ​ H ​ ( x, α) ​ [u] f\in QR{H}(x,\alpha)[u] de degré N ⁡ ( f) N(f) en u u, et soit S ⁡ ( μ) = N ⁡ ( f) ​ ∑ j = 1 ℓ s j S(\mu)=N(f)\sum_{j=1}^{\ell}s_{j}. Alors, f ^ = ∑ p ≥ − N ⁡ ( f) g p ​ ( f) \widehat{f}=\sum_{p\geq-N(f)}g_{p}(f), et le germe

 | h = x S ⁡ ( μ) ​ f h=x^{S(\mu)}f |  |

s’identifie à un élément de l’algèbre Λ ∗ ​ ( Q ​ R ​ H ​ ( x, α) ​ [λ]) \Lambda^{*}(QR{H}(x,\alpha)[\lambda]) (en utilisant les formules x s j ​ u j = λ j x^{s_{j}}u_{j}=\lambda_{j}). De plus, g p ​ ( h) = x S ⁡ ( μ) ​ g p − S ⁡ ( 0) ​ ( f) g_{p}(h)=x^{S(\mu)}g_{p-S(0)}(f) pour tout p ≥ ( ℓ − 1) ​ N ​ ( f) p\geq(\ell-1)N(f), et g p ​ ( h) = 0 g_{p}(h)=0 si p < ( ℓ − 1) ​ N ​ ( f) p<(\ell-1)N(f). La multiplicité algébrique de h h est (par sa définition), m ​ a χ ​ ( h) = m ​ a χ ​ ( f) + ℓ ​ N ​ ( f) ma_{\chi}(h)=ma_{\chi}(f)+\ell N(f). Donc en appliquant les résultats du (a), on obtient

###### Lemme IIIA8

L’algèbre Q ​ R ​ H ​ ( x, α) ​ [u] QR{H}(x,\alpha)[u] est χ \chi -finie et satisfait à la double inclusion

 | ( x m ​ a χ + ​ ( f) + ε) ​ π χ ∗ ​ ( J f) ⊂ I χ, f et ( x ℓ ​ N ​ ( f) + ε) ​ I χ, f ⊂ π χ ∗ ​ ( J f) (x^{ma^{+}_{\chi}(f)+\varepsilon})\pi_{\chi}^{*}(J_{f})\subset I_{\chi,f}\quad\text{et}\quad(x^{\ell N(f)+\varepsilon})I_{\chi,f}\subset\pi_{\chi}^{*}(J_{f}) |  |

Elle est χ \chi -équivalente à la sous-algèbre Q ​ R ​ H c ​ v ​ g ​ ( x, α) ​ [u] QR{H}_{cvg}(x,\alpha)[u].

Le facteur x ℓ ​ N ​ ( f) x^{\ell N(f)} dans la deuxième inclusion, est optimal comme le montre l’exemple suivant: f = u N ​ x ​ log ⁡ x f=u^{N}x\log x ( ℓ = 1 \ell=1 et s = 1 s=1), l’idéal χ \chi -transverse de f f est ( λ N) (\lambda^{N}). l’idéal saturé π χ ∗ ​ ( J χ, f, γ) \pi_{\chi}^{*}(J_{\chi,f,\gamma}) est l’idéal ( x N ​ u N) (x^{N}u^{N}). Le plus petit entier n n tel que x n ​ f ∈ ( x N ​ u N) x^{n}f\in(x^{N}u^{N}) (dans l’anneau S ​ B SB), est N N.

(c) La sous-algèbre convergente Q ​ R ​ H c ​ v ​ g QR{H}_{cvg}. Elle est χ \chi -finie d’après le lemme d’extension IB2 (même démarche que dans la section II). Le lemme IIIA4 s’applique à cette algèbre noethérienne: I f = I χ, f I_{f}=I_{\chi,f} et J f = J χ, f, γ J_{f}=J_{\chi,f,\gamma}. Soit H ​ H p ⊂ Q ​ R ​ H c ​ v ​ g H{H}_{p}\subset QR{H}_{cvg} le ℝ ​ { α } \mathbb{R}\{\alpha\} -module des blocs χ \chi -homogènes de degré p ∈ ℤ p\in\mathbb{Z}. Si ℓ > 0 \ell>0, il est de dimension infinie et la méthode de réduction de la section II est inopérante. Une première approche à la première inclusion est

###### Lemme IIIA9

Soit g ∈ H ​ H p g\in H{H}_{p} d’idéal χ \chi -transverse J g J_{g} et soit p + = max ⁡ ( p, 0) p^{+}=\max(p,0). Pour tout ε > 0 \varepsilon>0 et pour tout N N

 | ( x p + + ε) ​ π χ ∗ ​ ( J g) ⊂ I χ, g + π χ ∗ ​ ( ( M λ ′) N) (x^{p^{+}+\varepsilon})\pi_{\chi}^{*}(J_{g})\subset I_{\chi,g}+\pi_{\chi}^{*}(({M}^{\prime}_{\lambda})^{N}) |  |

Preuve. Par récurrence sur ℓ \ell. Le cas ℓ = 0 \ell=0 est donné par le lemme II4. Supposons ℓ > 0 \ell>0. L’idéal I χ, g I_{\chi,g} étant noethérien dans Q ​ R ​ H c ​ v ​ g QR{H}_{cvg}, g g satisfait à une équation différentielle résolue

 | χ M 0 + 1 ​ g − ∑ i = 0 M 0 h i ​ χ i ​ g = 0 \chi^{M_{0}+1}g-\sum_{i=0}^{M_{0}}h_{i}\chi^{i}g=0 |  |

Son idéal χ \chi -transverse est donc engendré par la restriction de la famille ( g, …, χ M 0 ​ g) (g,\ldots,\chi^{M_{0}}g) à toute transversale { x = x 0 > 0 } \{x=x_{0}>0\}. Quitte à effectuer une homothètie en x x, on peut supposer que le polydisque de convergence de la série de g g (dans les variables X X), contient la transversale { x = 1 } \{x=1\}. Et quitte à effectuer une ramification x ′ = x s ℓ x^{\prime}=x^{s_{\ell}}, et à augmenter le nombre des variables μ \mu, on peut supposer que s ℓ ≡ 1 s_{\ell}\equiv 1. Ordonnons g g en puissances croissantes des fonctions élémentaires z z: g = ∑ | m | ≥ 0 a m ​ z m g=\sum_{|m|\geq 0}a_{m}z^{m} et posons

 | g M = ∑ | m | ≤ M a m ​ z m g_{M}=\sum_{|m|\leq M}a_{m}z^{m} |  |

 | u ′ = ( u 1, …, u ℓ − 1) et λ ′ = ( λ 1, …, λ ℓ − 1) u^{\prime}=(u_{1},\ldots,u_{\ell-1})\quad\text{et}\quad\lambda^{\prime}=(\lambda_{1},\ldots,\lambda_{\ell-1}) |  |

On vérifie facilement (sur les monômes de g M g_{M}), que le germe x M − p ​ g M x^{M-p}g_{M} s’identifie à un élément g M ′ g^{\prime}_{M} de l’algèbre ( Λ ′) ∗ ​ ( Q ​ R ​ H ​ ( x, α, λ ℓ, u ′)) (\Lambda^{\prime})^{*}(QR{H}(x,\alpha,\lambda_{\ell},u^{\prime})) avec

 | Λ ′ ​ ( x, α, u) = ( x, α, λ ℓ, u ′) et λ ℓ = x ​ u ℓ \Lambda^{\prime}(x,\alpha,u)=(x,\alpha,\lambda_{\ell},u^{\prime})\quad\text{et}\quad\lambda_{\ell}=xu_{\ell} |  |

Comme on l’a vu au (a), l’action de χ \chi sur cette algèbre est équivalente à celle de la dérivation

 | χ ′ = x ​ ∂ ∂ x − ∑ j = 1 ℓ − 1 s j ​ u j ​ ∂ ∂ u j \chi^{\prime}=x\frac{\partial}{\partial x}-\sum_{j=1}^{\ell-1}s_{j}u_{j}\frac{\partial}{\partial u_{j}} |  |

sur l’algèbre Q ​ R ​ H ​ ( x, α, λ ℓ, u ′) QR{H}(x,\alpha,\lambda_{\ell},u^{\prime}). Soit G M = ( ( Λ ′) ∗) − 1 ​ ( g M ′) G_{M}=((\Lambda^{\prime})^{*})^{-1}(g^{\prime}_{M}). Il est χ ′ \chi^{\prime} -homogène de degré M M. Par l’hypothèse de récurrence

 | ( x M + ε) ​ π χ ′ ∗ ​ ( J G M) ⊂ I χ ′, G M + π χ ′ ∗ ​ ( ( M λ ′ ′) N) (x^{M+\varepsilon})\pi_{\chi^{\prime}}^{*}(J_{G_{M}})\subset I_{\chi^{\prime},G_{M}}+\pi_{\chi^{\prime}}^{*}(({M}^{\prime}_{\lambda^{\prime}})^{N}) |  |

Or l’idéal χ ′ \chi^{\prime} -transverse de G M G_{M} coincide avec l’idéal χ \chi -transverse de g M g_{M} et le relevé de son idéal différentiel est ( x M − p) ​ I χ, g M (x^{M-p})I_{\chi,g_{M}}. Donc en relevant cette inclusion, on obtient

 | ( x p + + ε) ​ π χ ∗ ​ ( J g M) ⊂ I χ, g M + π χ ∗ ​ ( ( M λ ′) N) (x^{p^{+}+\varepsilon})\pi_{\chi}^{*}(J_{g_{M}})\subset I_{\chi,g_{M}}+\pi_{\chi}^{*}(({M}^{\prime}_{\lambda})^{N}) |  |

Maintenant, si M ≥ M 0 M\geq M_{0} et si on se restreint à la transversale { x = 1 } \{x=1\}, on voit que l’idéal χ \chi -transverse de g M g_{M} contient celui de g g. Et si on prend M ≥ N + p + M\geq N+p^{+}, on a g − g M ∈ π χ ∗ ​ ( ( M λ ′) N) g-g_{M}\in\pi_{\chi}^{*}(({M}^{\prime}_{\lambda})^{N}). D’où le résultat.∎

###### Lemme IIIA10

Soit f ∈ Q ​ R ​ H c ​ v ​ g f\in QR{H}_{cvg}. Pour tout ε > 0 \varepsilon>0 et pour tout N N

 | ( x m ​ a χ + ​ ( f) + ε) ​ π χ ∗ ​ ( J f) ⊂ I f + π χ ∗ ​ ( ( M λ ′) N) (x^{ma^{+}_{\chi}(f)+\varepsilon})\pi_{\chi}^{*}(J_{f})\subset I_{f}+\pi_{\chi}^{*}(({M}^{\prime}_{\lambda})^{N}) |  |

Preuve. Soit p 0 p_{0} comme dans la définition IIIA3, et soient p 1 ≤ p 0 p_{1}\leq p_{0} et p 2 ≥ m ​ a χ + ​ ( f) p_{2}\geq ma^{+}_{\chi}(f) tels que I f = I χ, f p 1, p 2 I_{f}=I_{\chi,f_{p_{1},p_{2}}}. On a

 | I f = ∑ p = p 1 p 2 I χ, g p ⊃ ∑ p = p 1 m ​ a χ + ​ ( f) I χ, g p et J f = ∑ p = p 1 p 2 J g p = ∑ p = p 1 m ​ a χ + ​ ( f) J g p I_{f}=\sum_{p=p_{1}}^{p_{2}}I_{\chi,g_{p}}\supset\sum_{p=p_{1}}^{ma^{+}_{\chi}(f)}I_{\chi,g_{p}}\quad\text{et}\quad J_{f}=\sum_{p=p_{1}}^{p_{2}}J_{g_{p}}=\sum_{p=p_{1}}^{ma^{+}_{\chi}(f)}J_{g_{p}} |  |

on obtient le résultat en appliquant le lemme IIIA9 aux fonctions g p g_{p}.∎

l’anneau S ​ B SB n’étant pas noethérien, on ne peut passer à la limite dans ces inclusions. Comme dans la section II, on contourne cette difficulté grâce au théorème de division VB2 (appendice VB), et grâce au lemme de Nakayama. On obtient le très important résultat suivant

###### Théorème IIIA1 (théorème principal 2)

L’algèbre Q ​ R ​ H c ​ v ​ g QR{H}_{cvg} satisfait globalement à la double inclusion: pour tout f ∈ Q ​ R ​ H c ​ v ​ g f\in QR{H}_{cvg} de multiplicité algébrique m ​ a + ma^{+}, il existe un entier n ⁡ ( f) n(f) tel que pour tout ε > 0 \varepsilon>0

 | ( x m ​ a + + ε) ​ π χ ∗ ​ ( J f) ⊂ I χ, f et ( x n ⁡ ( f)) ​ I χ, f ⊂ π χ ∗ ​ ( J f) (x^{ma^{+}+\varepsilon})\pi_{\chi}^{*}(J_{f})\subset I_{\chi,f}\quad\text{et}\quad(x^{n(f)})I_{\chi,f}\subset\pi_{\chi}^{*}(J_{f}) |  |

Preuve. La difficulté réside dans la transcendance des intégrales premières non triviales de χ \chi. Grâce à la convergence des séries d’éléments de Q ​ R ​ H c ​ v ​ g QR{H}_{cvg}, on montre d’abord que l’action de χ \chi sur cette algèbre est équivalente à celle d’une dérivation d’intégrales premières non triviales algébriques, sur une autre algèbre convergente. Le théorème de division VB2 s’applique à cette nouvelle dérivation.

Généralisons le difféomorphisme Λ \Lambda en les difféomorphismes Λ s \Lambda_{s} suivants: soit s ≥ 0 s\geq 0 et Λ s: ( x, α, u) ∈ U ↦ ( y, α, v) ∈ U s \Lambda_{s}:(x,\alpha,u)\in U\mapsto(y,\alpha,v)\in U_{s} avec

 | y = x 1 s + 1 et v j = x 1 s + 1 + μ j ​ u j y=x^{\frac{1}{s+1}}\quad\text{et}\quad v_{j}=x^{\frac{1}{s+1}+\mu_{j}}u_{j} |  |

Le champ ( s + 1) ​ ( Λ s) ∗ ​ χ (s+1)(\Lambda_{s})_{*}\chi coincide avec la restriction à Λ s ​ ( U) \Lambda_{s}(U) du champ

 | Y s = y ​ ∂ ∂ y − s ​ ∑ j = 1 ℓ v j ​ ∂ ∂ v j {Y}_{s}=y\frac{\partial}{\partial y}-s\sum_{j=1}^{\ell}v_{j}\frac{\partial}{\partial v_{j}} |  |

Le morphisme Λ s ∗: S ​ B ​ ( y, α, v) → S ​ B ​ ( x, α, u) \Lambda_{s}^{*}:SB(y,\alpha,v)\to SB(x,\alpha,u) est un isomorphisme sur son image et le diagramme suivant est commutatif

 | S ​ B ​ ( y, α, v) → Λ s ∗ S ​ B ​ ( x, α, u) 1 s + 1 ​ Y s ↓ ↓ χ S ​ B ​ ( y, α, v) → Λ s ∗ S ​ B ​ ( x, α, u) \begin{CD}SB(y,\alpha,v)@>{\Lambda_{s}^{*}}>{}>SB(x,\alpha,u)\\ @V{{\frac{1}{s+1}{Y}_{s}}}V{}V@V{}V{\chi}V\\ SB(y,\alpha,v)@>{\Lambda_{s}^{*}}>{}>SB(x,\alpha,u)\end{CD} |  | ∗ |

Soit γ s = Λ s ​ ( γ) \gamma_{s}=\Lambda_{s}(\gamma), elle est principale dans U s U_{s} et le morphisme Λ s \Lambda_{s} est un difféomorphisme de U U sur Λ s ​ ( U) \Lambda_{s}(U) qui est un voisinage de γ s \gamma_{s}. En identifiant les intégrales premières de χ \chi et Y s {Y}_{s}, on obtient le diagramme commutatif

 | U → π χ W Λ s ↓ ↓ i ​ d U s → π Y s W \begin{CD}U@>{\pi_{\chi}}>{}>W\\ @V{\Lambda_{s}}V{}V@V{}V{id}V\\ U_{s}@>{\pi_{{Y}_{s}}}>{}>W\end{CD} |  | ∗ ⁣ ∗ |

Les idéaux χ \chi -transverses et Y s {Y}_{s} -transverses coincident.

Si s s est un entier ≥ 2 \geq 2, un calcul simple sur les monômes montre que l’image Λ s ∗ ​ ( S ​ B ​ ( y, α, v)) \Lambda_{s}^{*}(SB(y,\alpha,v)) contient les ℝ ​ { α } \mathbb{R}\{\alpha\} -modules H ​ H p ​ ( x, α, u) H{H}_{p}(x,\alpha,u) pour p ≥ 0 p\geq 0. Et il existe un morphisme linéaire: α ↦ β ⁡ ( α) \alpha\mapsto\beta(\alpha) tel que l’image réciproque ( Λ s ∗) − 1 ​ ( H ​ H p ​ ( x, α, u)) (\Lambda_{s}^{*})^{-1}(H{H}_{p}(x,\alpha,u)) est incluse dans le ℝ ​ { β } \mathbb{R}\{\beta\} -module H ​ H ( s + 1) ​ p ​ ( y, β, v) H{H}_{(s+1)p}(y,\beta,v) des blocs Y s {Y}_{s} -homogènes de degré ( s + 1) ​ p (s+1)p, restreint à l’image β ⁡ ( α) \beta(\alpha). En effet, si z j z_{j} est une fonction élémentaire de l’algèbre Q ​ R ​ H ​ ( x, α, u) QR{H}(x,\alpha,u) qui satisfait à l’équation χ 0 ​ z j = r j ​ z j + x \chi_{0}z_{j}=r_{j}z_{j}+x, la fonction Z j = y − s ​ ( Λ s ∗) − 1 ​ ( z j) Z_{j}=y^{-s}(\Lambda_{s}^{*})^{-1}(z_{j}) satisfait à l’équation Y 0 ​ Z j = ( r j + s ⁡ ( r j − 1)) ​ Z j + ( s + 1) ​ y {Y}_{0}Z_{j}=(r_{j}+s(r_{j}-1))Z_{j}+(s+1)y. Si m m et n n sont des multi-indices tels que | m | − | n | = p ≥ 0 |m|-|n|=p\geq 0

 | ( Λ s ∗) − 1 ​ ( X m ​ u n) = y m 0 + s ​ | m | − 2 ​ | n | ​ ∏ Z j m j ​ ∏ j = 1 ℓ y n j ​ ( 1 − ( s + 1) ​ μ j) ​ v j n j ​ 2 ′ (\Lambda_{s}^{*})^{-1}(X^{m}u^{n})=y^{m_{0}+s|m|-2|n|}\prod Z_{j}^{m_{j}}\prod_{j=1}^{\ell}y^{n_{j}(1-(s+1)\mu_{j})}v_{j}^{n_{j}}2^{\prime} |  |  |

Maintenant, il suffit de remarquer que y 1 − ( s + 1) ​ μ j = y − ( s + 1) ​ μ j ​ y ​ Ld ​ ( y, − ( s + 1) ​ μ j) y^{1-(s+1)\mu_{j}}=y-(s+1)\mu_{j}y\text{Ld}(y,-(s+1)\mu_{j}) et d’utiliser la convergence des séries d’éléments de H ​ H p H{H}_{p}.

Soit f ∈ Q ​ R ​ H c ​ v ​ g ​ ( x, α, u) f\in QR{H}_{cvg}(x,\alpha,u) et soient p 1 p_{1} et p 2 p_{2} comme dans le lemme IIIA10. Quitte à remplacer f f par x − p 1 ​ f x^{-p_{1}}f, on peut supposer que p 1 ≥ 0 p_{1}\geq 0. Soit s s un entier ≥ 2 \geq 2 et F = ( Λ s ∗) − 1 ​ ( f p 1, p 2) F=(\Lambda_{s}^{*})^{-1}(f_{p_{1},p_{2}}). C’est un élément de l’algèbre Q ​ R ​ H ​ ( y, β, v) c ​ v ​ g QR{H}(y,\beta,v)_{cvg} retreinte à l’image β ⁡ ( α) \beta(\alpha). La multiplicité algébrique de F F relativement à Y s {Y}_{s} est ( s + 1) ​ m ​ a χ ​ ( f) (s+1)ma_{\chi}(f). Le lemme IIIA10 s’applique à l’action de Y s {Y}_{s} sur cette algèbre: pour tout ε > 0 \varepsilon>0 et pour tout N N

 | ( y ( s + 1) ​ m ​ a + + ε) ​ π Y s ∗ ​ ( J F) ⊂ I Y s, F + π Y s ∗ ​ ( ( M λ ′) N) (y^{(s+1)ma^{+}+\varepsilon})\pi_{{Y}_{s}}^{*}(J_{F})\subset I_{{Y}_{s},F}+\pi_{{Y}_{s}}^{*}(({M}^{\prime}_{\lambda})^{N}) |  |

Le théorème de division VB2 s’applique à l’action de Y s {Y}_{s} sur l’anneau S ​ B ​ ( y, α, v) SB(y,\alpha,v). Soit n ⁡ ( F) n(F) l’entier donné par ce théorème, il ne dépend que de J F = J f J_{F}=J_{f} et de s s. Le théorème de division VB2 appliqué à F F fournit la deuxième inclusion

 | ( y n ⁡ ( F)) ​ I Y s, F ⊂ π Y s ∗ ​ ( J F) (y^{n(F)})I_{{Y}_{s},F}\subset\pi_{{Y}_{s}}^{*}(J_{F}) |  | 3 |

Soit ( φ 1, …, φ L) (\varphi_{1},\ldots,\varphi_{L}) un système de générateurs de J F J_{F} dans l’anneau ℝ ​ { α, λ } \mathbb{R}\{\alpha,\lambda\} et soit N > ( s + 1) ​ m ​ a + + n ⁡ ( F) + 1 N>(s+1)ma^{+}+n(F)+1. Pour tout i = 1, …, L i=1,\ldots,L l’inclusion ci-dessus montre qu’il existe h i ∈ S ​ B ​ ( y, α, v) h_{i}\in SB(y,\alpha,v) tel que

 | y ( s + 1) ​ m ​ a + + ε ​ π Y s ∗ ​ ( φ i) − y N ​ h i ∈ I Y s, F y^{(s+1)ma^{+}+\varepsilon}\pi_{{Y}_{s}}^{*}(\varphi_{i})-y^{N}h_{i}\in I_{{Y}_{s},F} |  | 4 |

Ceci implique que l’idéal Y s {Y}_{s} -transverse de h i h_{i} est inclus dans J F J_{F}. Donc par le théorème de division VB2, les inclusions (4) donnent

 | ( y ( s + 1) ​ m ​ a + + ε) ​ π Y s ∗ ​ ( J F) ⊂ I Y s, F + ( y ( s + 1) ​ m ​ a + + 1) ​ π Y s ∗ ​ ( J F) (y^{(s+1)ma^{+}+\varepsilon})\pi_{{Y}_{s}}^{*}(J_{F})\subset I_{{Y}_{s},F}+(y^{(s+1)ma^{+}+1})\pi_{{Y}_{s}}^{*}(J_{F}) |  |

et par le lemme de Nakayama, on obtient

 | ( y ( s + 1) ​ m ​ a + + ε) ​ π Y s ∗ ​ ( J F) ⊂ I Y s, F (y^{(s+1)ma^{+}+\varepsilon})\pi_{{Y}_{s}}^{*}(J_{F})\subset I_{{Y}_{s},F} |  | 5 |

On applique alors le morphisme Λ s ∗ \Lambda_{s}^{*} aux inclusions (3) et (5) et la commutativité du diagramme ( ∗) (*) pour obtenir le résultat.∎

Remarque IIIA1. De cette preuve, et du théorème de division VB2, on déduit le résultat suivant: si h ∈ Q ​ R ​ H c ​ v ​ g 1, q h\in QR{H}^{1,q}_{cvg}, et si son idéal χ \chi -transverse est inclus dans celui de f f, alors

 | ( x n ⁡ ( f)) ​ I χ, h ⊂ π χ ∗ ​ ( J χ, f, γ) (x^{n(f)})I_{\chi,h}\subset\pi_{\chi}^{*}(J_{\chi,f,\gamma}) |  |

Remarque IIIA2. Soit W 0 ⊂ W W_{0}\subset W un semi-analytique de l’anneau ℝ ​ { α, λ } \mathbb{R}\{\alpha,\lambda\}, qui adhère à 0. Soit U 0 = π χ − 1 ​ ( W 0) U_{0}=\pi_{\chi}^{-1}(W_{0}). Il est clair que le lemme IIIA9 est vrai sur les restrictions W 0 W_{0} et U 0 U_{0} (la multiplicité algébrique restreinte coincide avec la multiplicité algébrique d’un bloc g p g_{p}). Par conséquent, le lemme IIIA10 et le théorème principal IIIA1, sont encore vrais sur les restrictions W 0 W_{0}, U 0 U_{0}, en utilisant la multiplicité algébrique restreinte m a χ ( f | U 0) ma_{\chi}(f_{|U_{0}}).

§2.2. Exemple de germe presque quasi-convergent.

Soit f ∈ Q ​ R ​ H 1, q ​ ( x, α) f\in QR{H}^{1,q}(x,\alpha) d’idéal χ \chi -transverse J χ, f, γ J_{\chi,f,\gamma}. On dit que f f (ou J χ, f, γ J_{\chi,f,\gamma}) satisfait à l’hypothèse ( H ​ λ) (H\lambda) s’il existe un entier N ⁡ ( f) N(f) tel que

 | J χ, f, γ ⊃ ( M λ ′) N ⁡ ( f) J_{\chi,f,\gamma}\supset({M}^{\prime}_{\lambda})^{N(f)} |  |

On note C λ 1 {C}^{1}_{\lambda} la classe des germes qui satisfont à l’hypothèse ( H ​ λ) (H\lambda). Tout f ∈ C λ 1 f\in{C}^{1}_{\lambda} est presque quasi-convergent: soit f n = 𝕛 u N ⁡ ( f) + n ​ ( f) f_{n}={\mathbb{j}}_{u}^{N(f)+n}(f), il est quasi-convergent et par le lemme IIIA8, J f n = J χ, f n, γ J_{f_{n}}=J_{\chi,f_{n},\gamma}. Par l’hypothèse ( H ​ λ) (H\lambda), on a J χ, f, γ ⊂ J f n + M ′ ​ J χ, f, γ J_{\chi,f,\gamma}\subset J_{f_{n}}+{M}^{\prime}J_{\chi,f,\gamma}. Donc, par le lemme de Nakayama, on a J χ, f, γ = J f n J_{\chi,f,\gamma}=J_{f_{n}}. De plus, la suite ( f n) (f_{n}) converge vers f f dans la M ( α, u) {M}_{(\alpha,u)} -topologie. Par conséquent, f f possède une multiplicité algébrique m ​ a χ ​ ( f) ma_{\chi}(f) et J f = J χ, f, γ J_{f}=J_{\chi,f,\gamma}.

###### Lemme IIIA11

La classe C λ 1 {C}^{1}_{\lambda} est χ \chi -finie et satisfait à la double inclusion

 | ( x m ​ a χ + ​ ( f) + ε) ​ π χ ∗ ​ ( J f) ⊂ I χ, f et ( x ℓ ​ N ​ ( f) + ε) ​ I χ, f ⊂ π χ ∗ ​ ( J f) (x^{ma^{+}_{\chi}(f)+\varepsilon})\pi_{\chi}^{*}(J_{f})\subset I_{\chi,f}\quad\text{et}\quad(x^{\ell N(f)+\varepsilon})I_{\chi,f}\subset\pi_{\chi}^{*}(J_{f}) |  |

De plus, elle est χ \chi -équivalente à la sous-classe Q ​ R ​ H c ​ v ​ g 1, q ∩ C λ 1 QR{H}^{1,q}_{cvg}\cap{C}^{1}_{\lambda}.

Preuve. Par l’hypothèse ( H ​ λ) (H\lambda), x ℓ ​ N ​ ( f) + ε ​ ( f − f 0) ∈ π χ ∗ ​ ( J f) x^{\ell N(f)+\varepsilon}(f-f_{0})\in\pi_{\chi}^{*}(J_{f}). Et par le lemme IIIA8, ( x ℓ ​ N ​ ( f) + ε) ​ I χ, f 0 ⊂ π χ ∗ ​ ( J f) (x^{\ell N(f)+\varepsilon})I_{\chi,f_{0}}\subset\pi_{\chi}^{*}(J_{f}), d’où la deuxième inclusion pour f f. Soit F = 𝕛 X ℓ ​ N ​ ( f) + m ​ a + ​ ( f − f 0) F={\mathbb{j}}_{X}^{\ell N(f)+ma^{+}}(f-f_{0}), on a f − f 0 − F ∈ ( x m ​ a + + ε) ​ π χ ∗ ​ ( J f) f-f_{0}-F\in(x^{ma^{+}+\varepsilon})\pi_{\chi}^{*}(J_{f}), et l’idéal χ \chi -transverse de F F est inclus dans M ′ ​ J f {M}^{\prime}J_{f}. Le germe f 0 f_{0} a la même multiplicité algébrique que f f, et d’après le lemme IIIA8, il est χ \chi -équivalent au germe

 | h = ∑ − N ⁡ ( f) ≤ p ≤ m ​ a + g p ​ ( f 0) h=\sum_{-N(f)\leq p\leq ma^{+}}g_{p}(f_{0}) |  |

De plus on a f 0 − h ∈ ( x m ​ a + + ε) ​ π χ ∗ ​ ( J f) f_{0}-h\in(x^{ma^{+}+\varepsilon})\pi_{\chi}^{*}(J_{f}). Maintenant, le germe h + F ∈ Q ​ R ​ H c ​ v ​ g h+F\in QR{H}_{cvg} a la même multiplicité algébrique que f f, et il est algébrique dans la variable X X, il est donc χ \chi -équivalent à un germe H H algébrique dans les variables ( X, u) (X,u) (cf. (c)). D’après le lemme IIIA8, le germe H H satisfait à la première inclusion. Comme f − ( h + F) ∈ ( x m ​ a + + ε) ​ π χ ∗ ​ ( J f) f-(h+F)\in(x^{ma^{+}+\varepsilon})\pi_{\chi}^{*}(J_{f}), le germe f f satisfait à la première inclusion et il est χ \chi -équivalent à H H.∎

Ce lemme est encore vrai pour la classe C λ, l ​ o ​ c 1 {C}^{1}_{\lambda,loc} des germes f f qui satisfont à l’hypothèse ( H ​ λ) (H\lambda) sur une restriction W 0 ​ ( f) ⊂ W W_{0}(f)\subset W.

B. Etude localisée et théorème principal 3.

Pour ℓ = 0 \ell=0, on a montré dans la section II, que l’algèbre Q ​ R ​ H 1, q QR{H}^{1,q} est χ 0 \chi_{0} -finie, et que tout élément f f se divise dans son idéal χ \chi -transverse J χ 0, f, γ 0 J_{\chi_{0},f,\gamma_{0}}, dans l’anneau Q ​ A 1, | q | ​ [Ω f] QA^{1,|q|}[\Omega_{f}]. La question qui se pose alors est la suivante: f f se divise-t-elle dans J χ 0, f, γ 0 J_{\chi_{0},f,\gamma_{0}} dans un sous-anneau de Q ​ A 1, | q | QA^{1,|q|}, qui possède une structure asymptotique élémentaire? La réponse est oui modulo une désingularisation de J χ 0, f, γ 0 J_{\chi_{0},f,\gamma_{0}} (voir ci-dessous).

Pour ℓ > 0 \ell>0, on a vu dans la partie A que si le germe f f est presque quasi-convergent, il existe un entier n n tel x n ​ f x^{n}f se divise dans son idéal χ \chi -transverse (qu’on note simplement J f J_{f}), disons dans l’anneau S ​ B SB (on peut montrer que la division se fait dans l’anneau Q ​ A QA, mais ceci ne sera pas utilisé). Je pense qu’il est possible de généraliser le théorème de division VB2 à l’action de la dérivation χ \chi (ie. avec valeurs propres s j ​ ( μ) s_{j}(\mu) transcendantes), en utilisant encore les techniques de la référence [B-M]. Cependant, si le germe f f est général, sa série formelle relativement à χ \chi (cf. lemme IIIA1), est doublement formelle. D’où la difficulté de pouvoir approcher son idéal χ \chi -transverse J f J_{f}, par l’intermédiaire d’idéaux χ \chi -transverses de germes simples.

Si cet idéal J f J_{f} était principal et monomial, sa reconnaissance dans la série de f f, serait une simple étude sur les séries Tayloriennes. D’où l’idée du lemme IIIB1 ci-dessous, basé sur une désingularisation d’Hironaka. Grâce à cette désingularisation, on montre le théorème principal suivant

###### Théorème IIIB1 (théorème principal 3)

L’algèbre Q ​ R ​ H 1, q QR{H}^{1,q} est localement χ \chi -finie.

Néanmoins, cette désingularisation donne un caractère fortement technique à la preuve du théorème. Il est donc très souhaitable d’avoir un résultat global (de χ \chi -finitude), par les méthodes algébrico-géométriques des sections II et IIIA.

###### Lemme IIIB1

Soit J J un idéal de l’anneau ℝ ​ { α, λ } \mathbb{R}\{\alpha,\lambda\}. Il existe une désingularisation d’Hironaka ( ψ, N) (\psi,{N}) telle que dans chaque carte ( a, V a) (a,V_{a}), l’idéal ψ a ∗ ​ ( J) \psi_{a}^{*}(J) est principal et monomial. Autrement dit, il existe une coordonnée v v sur V a V_{a}, et un multi-indice n n, tels que ψ a ∗ ​ ( J) = ( v n) \psi_{a}^{*}(J)=(v^{n}).

Preuve. Elle est basée sur une récurrence sur le nombre de générateurs (indépendants) de J J. Soit ( φ 1, …, φ L) (\varphi_{1},\ldots,\varphi_{L}) un système de générateurs de J J. Si L = 1 L=1, par une désingularisation d’Hironaka ([Hir1,2]), le génératuer φ 1 \varphi_{1} se relève localement en un germe qui est équivalent à un monôme. Si L > 1 L>1, on applique une désingularisation d’Hironaka au germe

 | φ 1 × ⋯ × φ L × ( φ L − φ L − 1) \varphi_{1}\times\cdots\times\varphi_{L}\times(\varphi_{L}-\varphi_{L-1}) |  |

s’il est non identiquement nul. Localement dans cette désingularisation, les trois germes φ L − 1 \varphi_{L-1}, φ L \varphi_{L} et φ L − φ L − 1 \varphi_{L}-\varphi_{L-1} sont équivalents à des monômes. Donc, en utilisant l’ordre lexicographique sur les monômes, on a ou bien ( φ L − 1) ⊂ ( φ L) (\varphi_{L-1})\subset(\varphi_{L}), ou bien ( φ L) ⊂ ( φ L − 1) (\varphi_{L})\subset(\varphi_{L-1}) et on applique l’hypothèse de récurrence.∎

Preuve du théorème IIIB1. Pour bien illustrer les étapes cruciales de cette preuve, commençons par le cas ℓ = 0 \ell=0

§1. Cas ℓ = 0 \ell=0.

Soit f ∈ Q ​ R ​ H 1, q ​ ( x, α) f\in QR{H}^{1,q}(x,\alpha) ( q = ( q 1, q 2) q=(q_{1},q_{2})), et soit J f J_{f} son idéal χ \chi -transverse le long de γ \gamma ( χ = χ 0 \chi=\chi_{0} et γ = γ 0 \gamma=\gamma_{0}). Montrons que f f se divise localement dans J f J_{f} dans un sous-anneau de Q ​ A QA qui admet une structure asymptotique élémentaire. Soit f ^ = ∑ n ≥ 0 g n \widehat{f}=\sum_{n\geq 0}g_{n} sa série asymptotique formelle relativement à la dérivation χ \chi (section II). Les fonctions g n g_{n} sont des blocs χ \chi -homogènes de degré n n, autrement dit si

 | Ld ​ ( x, μ j) = x μ j − 1 μ j \text{Ld}(x,\mu_{j})=\frac{x^{\mu_{j}}-1}{\mu_{j}} |  |

z j ​ ( x, μ) = x ​ Ld ​ ( x, μ j) z_{j}(x,\mu)=x\text{Ld}(x,\mu_{j}), z = ( z 1, …, z q 1) z=(z_{1},\ldots,z_{q_{1}}) et X = ( x, z) X=(x,z), alors

 | g n = ∑ | m | = n a m ​ ( α) ​ X m g_{n}=\sum_{|m|=n}a_{m}(\alpha)X^{m} |  |

avec a m ∈ ℝ ​ { α } a_{m}\in\mathbb{R}\{\alpha\}. On a vu dans la section II que si on note f n = ∑ n ′ ≤ n g n ′ f_{n}=\sum_{n^{\prime}\leq n}g_{n^{\prime}}, alors f − f n ∈ ( x n) ​ S ​ B 0 f-f_{n}\in(x^{n})SB_{0} pour tout n n. Soient J g n J_{g_{n}}, J f n J_{f_{n}} et J f J_{f} les idéaux χ \chi -transverses le long de γ \gamma. Ce sont des idéaux de l’anneau ℝ ​ { α } \mathbb{R}\{\alpha\}. La suite ( J f n) (J_{f_{n}}) est croissante et elle converge vers J f J_{f} grâce à la propriété de quasi-analycité dans la coordonnée x x. De plus, pour tout n n, on a f − f n ∈ ( x n) ​ π χ ∗ ​ ( J f) f-f_{n}\in(x^{n})\pi_{\chi}^{*}(J_{f}) dans l’anneau S ​ B 0 SB_{0}. Et, J f n = ∑ n ′ ≤ n J g n ′ J_{f_{n}}=\sum_{n^{\prime}\leq n}J_{g_{n^{\prime}}}. Donc, par unicité de la division (voir ci-dessous), il suffit de montrer que pour tout n n, le bloc g n g_{n} se divise localement dans J f J_{f}, dans un sous-anneau de Q ​ A QA qui possède une structure asymptotique élémentaire (ce sous-anneau étant indépendant de n n!).

Soit ( ψ, N) (\psi,{N}) une désingularisation dans laquelle l’idéal J f J_{f} est principal et monomial (lemme IIIB1), et soit ( a, V a) (a,V_{a}) une carte de coordonnée v v telle que

 | ψ a ∗ ​ ( J f) = ( φ ⁡ ( v)) avec φ ⁡ ( v) = ∏ j = 1 p v j n a, j \psi_{a}^{*}(J_{f})=(\varphi(v))\quad\text{avec}\quad\varphi(v)=\prod_{j=1}^{p}v_{j}^{n_{a,j}} |  |

On peut supposer, sans perte de généralité, que p = | q | p=|q|. Les variables analytiques de grande complexité dans l’algèbre Q ​ R ​ H 1, q ​ ( x, μ, ν) QR{H}^{1,q}(x,\mu,\nu), sont les variables μ \mu. Par une suite d’éclatements sphériques dans la coordonnée v v, on suppose que les relevés μ j, a \mu_{j,a} des fonctions μ j \mu_{j} sont préparées de la façon suivante: pour tout i = 1, …, p i=1,\ldots,p

 | μ j, a ​ ( v) = μ j, p + 1 − i + μ j, p + 1 − i ′ \mu_{j,a}(v)=\mu_{j,p+1-i}+\mu^{\prime}_{j,p+1-i} |  | 1 |

les fonctions μ j, p + 1 − i \mu_{j,p+1-i} étant indépendantes des coordonnées ( v i, …, v p) (v_{i},\ldots,v_{p}) et

 | μ j, p + 1 − i ′ ∈ ( v 1 × ⋯ × v i) \mu^{\prime}_{j,p+1-i}\ \ \in(v_{1}\times\cdots\times v_{i}) |  |

En effet, effectuons un premier éclatement sphérique dans la coordonnée v v: v = t 1 ​ w v=t_{1}w où t 1 t_{1} est une coordonnée locale sur ( ℝ, 0) (\mathbb{R},0), et w ∈ S p − 1 w\in S^{p-1} la sphère de ℝ p \mathbb{R}^{p}. Soit v 1 v^{1} une coordonnée analytique locale sur ( S p − 1, w) ≅ ( ℝ p − 1, 0) (S^{p-1},w)\cong(\mathbb{R}^{p-1},0). Le relevé du germe μ j, a \mu_{j,a} s’écrit

 | ρ 1 + t 1 ​ θ 1 ​ ( t 1, v 1) \rho_{1}+t_{1}\theta_{1}(t_{1},v^{1}) |  |

(avec ρ 1 ≡ 0 \rho_{1}\equiv 0!). Supposons que, après i i éclatements sphériques des coordonnées v j v^{j} ( j = 0, …, i − 1 j=0,\ldots,i-1, v 0 = v v^{0}=v), le relevé du germe μ j, a \mu_{j,a} s’écrive

 | ρ i ( t 1, …, t i − 1) + t 1 × ⋯ × t i θ i ( t i, v i) \rho_{i}(t_{1},\ldots,t_{i-1})+t_{1}\times\cdots\times t_{i}\theta_{i}(t^{i},v^{i}) |  |

où t i = ( t 1, …, t i) t^{i}=(t_{1},\ldots,t_{i}) est une coordonnée analytique sur ( ℝ i, 0) (\mathbb{R}^{i},0), et v i v^{i} est une coordonnée analytique sur ( ℝ p − i, 0) (\mathbb{R}^{p-i},0). On applique alors la première étape au germe θ i ​ ( 0, v i) \theta_{i}(0,v^{i}) (si p − i > 1 p-i>1), et on pose ρ i + 1 = ρ i + t 1 × ⋯ × t i θ i ( t i, 0) \rho_{i+1}=\rho_{i}+t_{1}\times\cdots\times t_{i}\theta_{i}(t^{i},0). On obtient les formules (1) en posant

 | μ j, p + 1 − i = ρ i et μ ′ j, p + 1 − i = t 1 × ⋯ × t i θ i \mu_{j,p+1-i}=\rho_{i}\quad\text{et}\quad\mu^{\prime}_{j,p+1-i}=t_{1}\times\cdots\times t_{i}\theta_{i} |  |

Notons toujours ( ψ, N) (\psi,{N}) la composée de ces deux désingularisations (l’idéal ( φ) (\varphi) est toujours monomial dans cette désingularisation). Notons B {B} l’une des algèbres S ​ B SB, Q ​ A QA ou Q ​ R ​ H QR{H} (sans préciser les exposants). Dans la carte ( a, V a) (a,V_{a}), une extension naturelle de l’anneau B ⁡ ( x, α) {B}(x,\alpha), appropriée à f f, est l’anneau ( B ⁡ ( x, α, v), π) ({B}(x,\alpha,v),\pi), où π \pi est (le germe de) la projection canonique: ( x, α, v) ∈ U × V a ↦ ( x, α) ∈ U (x,\alpha,v)\in U\times V_{a}\mapsto(x,\alpha)\in U ( U ∈ ( ℝ + ⁣ ∗ × ℝ | q |, 0) U\in(\mathbb{R}^{+*}\times\mathbb{R}^{|q|},0) est un ouvert produit). Précisons un peu, dans ce cas simple, les propriétés du transfert par le morphisme π \pi. Notons toujours χ = x ∂ / ∂ x \chi=x\partial/\partial x la dérivation définit sur U × V a U\times V_{a}. Le morphisme π \pi est une submersion, et on a π ∗ ​ χ = χ \pi_{*}\chi=\chi (la coordonnée v v est une intégrale première de χ \chi, et la restriction de π \pi aux fibres { v = c o n s t } \{v=const\} est un difféomorphisme sur son image U U). L’orbite Γ = { ( α, v) = 0 } \Gamma=\{(\alpha,v)=0\} est principale dans U × V a U\times V_{a}, et π ⁡ ( Γ) = γ \pi(\Gamma)=\gamma. Notons π 0 \pi_{0} la restriction de π \pi à une transversale { x = x 0 > 0 } \{x=x_{0}>0\}. L’idéal χ \chi -transverse de π ∗ ​ ( f) = f \pi^{*}(f)=f, est l’idéal prolongé π 0 ∗ ​ ( J f) ⊂ ℝ ⁡ { α, v } \pi_{0}^{*}(J_{f})\subset\mathbb{R}\{\alpha,v\}, il est engendré par un système de générateurs de J f J_{f} dans ℝ ​ { α } \mathbb{R}\{\alpha\}. Le morphisme Ψ a: v ∈ V a ↦ ( ψ a ​ ( v), v) ∈ W a \Psi_{a}:\ v\in V_{a}\mapsto(\psi_{a}(v),v)\in W_{a} est une immersion analytique, qui est un difféomorphisme sur son image W a ⊂ { x = x 0 } W_{a}\subset\{x=x_{0}\}. L’anneau restriction ℝ { α, v } | W a \mathbb{R}\{\alpha,v\}_{|W_{a}} est donc isomorphe à l’anneau ℝ ​ { v } \mathbb{R}\{v\}. Par conséquent, on a π 0 ∗ ( J f) | W a = ( φ) \pi_{0}^{*}(J_{f})_{|W_{a}}=(\varphi).

De même, posons U a = π χ − 1 ​ ( W a) U_{a}=\pi_{\chi}^{-1}(W_{a}), le morphisme Φ a: ( x, v) ∈ ( ℝ + ⁣ ∗, 0) × V a ↦ ( x, Ψ a ​ ( v)) ∈ U a \Phi_{a}:\ (x,v)\in(\mathbb{R}^{+*},0)\times V_{a}\mapsto(x,\Psi_{a}(v))\in U_{a} est une immersion analytique, qui est un difféomorphisme sur son image U a U_{a}. Donc, si B {B} est l’une des algèbres S ​ B SB ou Q ​ A QA, l’anneau restriction B ( x, α, v) | U a {B}(x,\alpha,v)_{|U_{a}} est isomorphe à l’anneau B ⁡ ( x, v) {B}(x,v). La dérivation χ \chi est préservée par ce difféomorphisme. Soit g g un bloc χ \chi -homogène de la série de f f. Notons f a = Φ a ∗ ( f | U a) f_{a}=\Phi_{a}^{*}(f_{|U_{a}}) et g a = Φ a ∗ ( g | U a) g_{a}=\Phi_{a}^{*}(g_{|U_{a}}). D’après le lemme de transfert IB6, l’idéal χ \chi -transverse de f a f_{a} le long de l’orbite { v = 0 } \{v=0\}, est ( φ) (\varphi). On a g ∈ π χ ∗ ​ ( J f) g\in\pi_{\chi}^{*}(J_{f}), donc g a ∈ π χ ∗ ​ ( ( φ)) g_{a}\in\pi_{\chi}^{*}((\varphi)). Il s’agit de montrer que le quotient de la division de g a g_{a} par φ \varphi, est dans un sous-anneau de Q ​ A 1, p ​ ( x, v) QA^{1,p}(x,v) qui possède une structure asymptotique élémentaire. La complexité de cette structure ne dépendra que du germe f f par l’intermédiaire de son idéal χ \chi -transverse J f J_{f}. Pour cela, on va construit une suite de p p extensions Q ​ R ​ H ~ i 1, p ​ ( x, v) \widetilde{QR{H}}_{i}^{1,p}(x,v) de l’algèbre Q R H 1, q + ( 0, p) ( x, α, v) | U a QR{H}^{1,q+(0,p)}(x,\alpha,v)_{|U_{a}} (rappelons que p = | q | p=|q|). La récurrence de cette construction est basée sur la récurrence de construction de nouvelles fonctions élémentaires d’Ecalle-Khovanski z... z^{...}, y … y^{\ldots} à partir des fonctions élémentaires z z de l’algèbre Q ​ R ​ H 1, q QR{H}^{1,q}, et des formules ( 1) (1).

(a) Construction des extensions Q ​ R ​ H ~ i 1, p \widetilde{QR{H}}_{i}^{1,p}.

Pour j = 1, …, q 1 j=1,\ldots,q_{1}, posons r j, 0 ​ ( v) = 1 + μ j, a ​ ( v) r_{j,0}(v)=1+\mu_{j,a}(v) et r j, 1 ( v 1, …, v p − 1) = 1 + μ j, 1 ( v 1, …, v p − 1) r_{j,1}(v_{1},\ldots,v_{p-1})=1+\mu_{j,1}(v_{1},\ldots,\ \ v_{p-1}). D’après (1), le germe τ j, 1 = μ j, a − μ j, 1 = μ j, 1 ′ ∈ r a d ( φ) = ( v 1 × ⋯ × v p) \tau_{j,1}=\mu_{j,a}-\mu_{j,1}=\mu^{\prime}_{j,1}\in rad(\varphi)=(v_{1}\times\cdots\times v_{p}). Pour tout m 1 ∈ ℕ m_{1}\in\mathbb{N}, développons les (relevés des) fonctions z j z_{j} à l’ordre m 1 m_{1} dans la variable τ j, 1 = μ j, a − μ j, 1 \tau_{j,1}=\mu_{j,a}-\mu_{j,1}

 | Φ a ∗ ​ ( z j) = ∑ n = 0 m 1 τ j, 1 n ​ z j, n + τ j, 1 m 1 + 1 ​ y j, m 1 ​ 2 1 \Phi_{a}^{*}(z_{j})=\sum_{n=0}^{m_{1}}\tau_{j,1}^{n}z_{j,n}+\tau_{j,1}^{m_{1}+1}y_{j,m_{1}}2_{1} |  |  |

En utilisant l’équation χ ​ Φ a ∗ ​ ( z j) = r j, 0 ​ Φ a ∗ ​ ( z j) + x \chi\Phi_{a}^{*}(z_{j})=r_{j,0}\Phi_{a}^{*}(z_{j})+x et en identifiant les coefficients des puissances de τ j, 1 \tau_{j,1}, on obtient des équations différentielles simples pour les fonctions z j, n z_{j,n} et y j, m 1 y_{j,m_{1}}

 | χ ​ z j, 0 = r j, 1 ​ z j, 0 + x \chi z_{j,0}=r_{j,1}z_{j,0}+x |  |

 | χ ​ z j, n = r j, 1 ​ z j, n + z j, n − 1 ​ 3 1 \chi z_{j,n}=r_{j,1}z_{j,n}+z_{j,n-1}3_{1} |  |  |

 | χ ​ y j, m 1 = r j, 0 ​ y j, m 1 + z j, m 1 \chi y_{j,m_{1}}=r_{j,0}y_{j,m_{1}}+z_{j,m_{1}} |  |

avec les conditions initiales z j, n | x = 1 ≡ 0 z_{j,n|x=1}\equiv 0 et y j, m 1 | x = 1 ≡ 0 y_{j,m_{1}|x=1}\equiv 0. Comme pour les fonctions élémentaires z j z_{j}, on montre grâce à l’opérateur intégral de Dulac (cf. appendice VA), que z j, n ∈ Q ​ A 1, p − 1 ​ ( x, v 1, …, v p − 1) z_{j,n}\in QA^{1,p-1}(x,v_{1},\ldots,v_{p-1}) et y j, m 1 ∈ Q ​ A 1, p ​ ( x, v) y_{j,m_{1}}\in QA^{1,p}(x,v). Notons z n = ( z 1, n, …, z q 1, n) z^{n}=(z_{1,n},\ldots,z_{q_{1},n}), y m 1 = ( y 1, m 1, …, y q 1, m 1) y^{m_{1}}=(y_{1,m_{1}},\ldots,y_{q_{1},m_{1}}) et X 1, m 1 = ( x, z 0, …, z m 1, y m 1) X_{1,m_{1}}=(x,z^{0},\ldots,z^{m_{1}},y^{m_{1}}). Un germe G 1, n ∈ S ​ B 1, p ​ ( x, v) G_{1,n}\in SB^{1,p}(x,v) est un 1-bloc χ \chi -homogène de degré n n et de complexité m 1 m_{1}, si

 | G 1, n = ∑ | m ′ | = n a m ′ ​ ( v) ​ X 1, m 1 m ′ G_{1,n}=\sum_{|m^{\prime}|=n}a_{m^{\prime}}(v)X_{1,m_{1}}^{m^{\prime}} |  |

avec a m ′ ∈ ℝ ​ { v } a_{m^{\prime}}\in\mathbb{R}\{v\}. Le germe G 1, n G_{1,n} est donc un élément de l’algèbre Q ​ A 1, p ​ ( x, v) QA^{1,p}(x,v). La première extension Q ​ R ​ H ~ 1, m 1 1, p ​ ( x, v) ⊂ Q ​ A 1, p ​ ( x, v) \widetilde{QR{H}}_{1,m_{1}}^{1,p}(x,v)\subset QA^{1,p}(x,v) est l’algèbre des germes qui possèdent une série asymptotique formelle dans les 1-blocs χ \chi -homogènes, de complexité m 1 m_{1}: F ∈ Q ​ A 1, p F\in QA^{1,p} est un élément de Q ​ R ​ H ~ 1, m 1 1, p \widetilde{QR{H}}_{1,m_{1}}^{1,p} s’il existe une suite ( G 1, n) (G_{1,n}) de 1-blocs χ \chi -homogènes de degré n n et de complexité m 1 m_{1}, telle que pour tout n n

 | F − ∑ n ′ ≤ n G 1, n ′ ∈ ( x n) ​ S ​ B 0 1, p F-\sum_{n^{\prime}\leq n}G_{1,n^{\prime}}\in(x^{n})SB_{0}^{1,p} |  |

On note Q ​ R ​ H ~ 1 1, p \widetilde{QR{H}}_{1}^{1,p} la limite inductive de ces algèbres, quand m 1 m_{1} décrit ℕ \mathbb{N}.

Soit r j, 2 = 1 + μ j, 2 r_{j,2}=1+\mu_{j,2}. D’après les formules (1), le germe τ j, 2 = μ j, 1 − μ j, 2 ∈ ( v 1 × ⋯ × v p − 1) \tau_{j,2}=\mu_{j,1}-\mu_{j,2}\in(v_{1}\times\cdots\times v_{p-1}). Soit m 2 ∈ ℕ m_{2}\in\mathbb{N} et soit n 1 ≤ m 1 n_{1}\leq m_{1}. En utilisant les équations ( 3 1) (3_{1}), on vérifie facilement que les coefficients z j, n 1, n 2 z_{j,n_{1},n_{2}} et y j, n 1, m 2 y_{j,n_{1},m_{2}} du développement ( 2 2) (2_{2}) à l’ordre m 2 m_{2} de la fonction z j, n 1 z_{j,n_{1}} dans la variable τ j, 2 \tau_{j,2}, satisfont des équations différentielles ( 3 2) (3_{2}) du même type que les équations ( 3 1) (3_{1}), de valeurs propres r j, 1 r_{j,1} ou r j, 2 r_{j,2}. De plus, ces coefficients vérifient des relations linéaires déduites des équations

 | ∂ n z j, 0 ∂ τ j, 1 n = n! ​ z j, n \frac{\partial^{n}z_{j,0}}{\partial\tau_{j,1}^{n}}=n!z_{j,n} |  |

Comme ci-dessus, on montre que z j, n 1, n 2 ∈ Q ​ A 1, p − 2 ​ ( x, v 1, …, v p − 2) z_{j,n_{1},n_{2}}\in QA^{1,p-2}(x,v_{1},\ldots,v_{p-2}) et y j, n 1, m 2 ∈ Q ​ A 1, p − 1 ​ ( x, v 1, …, v p − 1) y_{j,n_{1},m_{2}}\in QA^{1,p-1}(x,v_{1},\ldots,v_{p-1}). Pour n 1 = 0, …, m 1 n_{1}=0,\ldots,m_{1} et n 2 = 0, …, m 2 n_{2}=0,\ldots,m_{2}, notons z n 1 ​ n 2 = ( z 1, n 1, n 2, …, z q 1, n 1, n 2) z^{n_{1}n_{2}}=(z_{1,n_{1},n_{2}},\ldots,z_{q_{1},n_{1},n_{2}}), y n 1, m 2 = ( y 1, n 1, m 2, …, y q 1, n 1, m 2) y^{n_{1},m_{2}}=(y_{1,n_{1},m_{2}},\ldots,y_{q_{1},n_{1},m_{2}}) et y m 1 ​ m 2 = ( y n 1, m 2) y^{m_{1}m_{2}}=(y^{n_{1},m_{2}}). Soit

 | X 2, m 1, m 2 = ( x, ( z n 1 ​ n 2), y m 1, y m 1 ​ m 2) X_{2,m_{1},m_{2}}=(x,(z^{n_{1}n_{2}}),y^{m_{1}},y^{m_{1}m_{2}}) |  |

Un 2-bloc χ \chi -homogène de degré n n et de complexité ( m 1, m 2) (m_{1},m_{2}), est un germe de la forme

 | G 2, n = ∑ | m ′ | = n a m ′ ​ ( v) ​ X 2, m 1, m 2 m ′ G_{2,n}=\sum_{|m^{\prime}|=n}a_{m^{\prime}}(v)X_{2,m_{1},m_{2}}^{m^{\prime}} |  |

avec a m ′ ∈ ℝ ​ { v } a_{m^{\prime}}\in\mathbb{R}\{v\}. La deuxième extension Q ​ R ​ H ~ 2, m 1, m 2 1, p ​ ( x, v) ⊂ Q ​ A 1, p ​ ( x, v) \widetilde{QR{H}}^{1,p}_{2,m_{1},m_{2}}(x,v)\subset QA^{1,p}(x,v) est l’algèbre des germes qui possèdent un développement asymptotique dans les 2-blocs χ \chi -homogènes de complexité ( m 1, m 2) (m_{1},m_{2}). On note Q ​ R ​ H ~ 2 1, p \widetilde{QR{H}}^{1,p}_{2} la limite inductive de ces algèbres.

En répétant ce procédé p p fois, on obtient l’extension Q ​ R ​ H ~ p 1, p ⊂ Q ​ A 1, p ​ ( x, v) \widetilde{QR{H}}^{1,p}_{p}\subset QA^{1,p}(x,v) qui est la limite inductive d’algèbres Q ​ R ​ H ~ p, m 1, …, m p 1, p ​ ( x, v) \widetilde{QR{H}}^{1,p}_{p,m_{1},\ldots,m_{p}}(x,v) dont les éléments ont une structure asymptotique élémentaire dans les p p -blocs χ \chi -homogènes dans la variable

 | X p, m 1, …, m p = ( x, ( z n 1 ​ … ​ n p), y m 1, y m 1 ​ m 2, …, y m 1 ​ … ​ m p) X_{p,m_{1},\ldots,m_{p}}=(x,(z^{n_{1}\ldots n_{p}}),y^{m_{1}},y^{m_{1}m_{2}},\ldots,y^{m_{1}\ldots m_{p}}) |  |

Le uplet ( m 1, …, m p) (m_{1},\ldots,m_{p}) étant la complexité de ces p p -blocs. Les fonctions z... z^{...} et y... y^{...} satisfont des équations différentielles ( 3 p) (3_{p}) du même type que ( 3 1) (3_{1}), de valeurs propres r j, 0 r_{j,0}, r j, 1 r_{j,1}, … et r j, p ≡ 1 r_{j,p}\equiv 1. Ainsi construites, les fonctions élémentaires OPEN z n 1 ​ … ​ n i ∈ Q ​ A 1, p − i ​ ( x, v 1, …, v p − i)) z^{n_{1}\ldots n_{i}}\in QA^{1,p-i}(x,v_{1},\ldots,v_{p-i})) sont indépendantes des coordonnées v p − i + 1, …, v p v_{p-i+1},\ldots,v_{p}. Un résultat qui généralise le théorème principal II1 est le suivant

###### Lemme IIIB2

Pour tout i = 1, …, p i=1,\ldots,p et pour tout choix d’entiers m 1, …, m i m_{1},\ldots,m_{i}; l’algèbre Q ​ R ​ H ~ i, m 1, …, m i 1, p ​ ( x, v) \widetilde{QR{H}}^{1,p}_{i,m_{1},\ldots,m_{i}}(x,v) est χ \chi -finie et satisfait à la double inclusion. De plus, elle admet un morphisme série formelle f ↦ f ^ i f\mapsto\widehat{f}^{i} qui est injectif, et on a les inclusions

 | Φ a ∗ ( Q R H | U a 1, q + ( 0, p)) ↪ Q ​ R ​ H ~ 1, m 1 1, p ↪ Q ​ R ​ H ~ 2, m 1, m 2 1, p ↪ … ↪ Q ​ R ​ H ~ p, m 1, …, m p 1, p \Phi_{a}^{*}(QR{H}^{1,q+(0,p)}_{|U_{a}})\hookrightarrow\widetilde{QR{H}}^{1,p}_{1,m_{1}}\hookrightarrow\widetilde{QR{H}}^{1,p}_{2,m_{1},m_{2}}\hookrightarrow\ldots\hookrightarrow\widetilde{QR{H}}^{1,p}_{p,m_{1},\ldots,m_{p}} |  |

Preuve. D’après la preuve du théorème principal II1, la χ \chi -finitude, la double inclusion et l’existence d’un morphisme série formelle injectif sont conséquences du théorème de division VB1, de la quasi-analycité: Q ​ R ​ H ~ i, … 1, p ⊂ Q ​ A 1, p ​ ( x, v) \widetilde{QR{H}}^{1,p}_{i,...}\subset QA^{1,p}(x,v), et de l’étude de l’action de χ \chi sur les i i -blocs χ \chi -homogènes.

Pour cela, on se place dans la situation générale: on suppose que les valeurs propres r j, 0 r_{j,0} sont indépendantes et on généralise les valeurs propres r j, 1 r_{j,1} en ( r j, 1, n) n (r_{j,1,n})_{n}, r j, 2 r_{j,2} en ( r j, 2, n 1, n 2) n 1, n 2 (r_{j,2,n_{1},n_{2}})_{n_{1},n_{2}}, …etc. Ainsi le nombre des valeurs propres indépendantes coincide avec le nombre des fonctions élémentaires z... z^{...} et y... y^{...} qui satisfont aux équations différentielles ( 3 i) (3_{i}) et à la condition initiale z... | x = 1 = y... | x = 1 ≡ 0 z^{...}_{|x=1}=y^{...}_{|x=1}\equiv 0. On généralise aussi les germes τ j, i ​ ( v) \tau_{j,i}(v) en des variables indépendantes τ = ( τ j, i) \tau=(\tau_{j,i}). Notons μ... = r... − 1 \mu_{...}=r_{...}-1, μ i = ( μ...) \mu^{i}=(\mu_{...}) et α i = ( μ i, τ, v) \alpha^{i}=(\mu^{i},\tau,v). Soit H ​ H i, n H{H}_{i,n} le ℝ ​ { α i } \mathbb{R}\{\alpha^{i}\} -module des i i -blocs χ \chi -homogènes de degré n n (et de complexité ( m 1, …, m i) (m_{1},\ldots,m_{i})). Il est stable par χ \chi d’après la linéarité du système ( 3 i) (3_{i}). Il s’agit donc de montrer que tout élément de H ​ H i, n H{H}_{i,n} satisfait à la double inclusion, et que sa multiplicité algébrique est n n. Mettons un ordre sur les monômes de H ​ H i, n H{H}_{i,n} compatible avec la triangularité du système ( 3 i) (3_{i}). Pour tout multi-indice m ′ m^{\prime} de longueur n n, posons e m ′ = ∑ m ′... r... e_{m^{\prime}}=\sum m^{\prime}_{...}r_{...}. Alors, d’après le système ( 3 i) (3_{i}), le ℝ ​ { α i } \mathbb{R}\{\alpha^{i}\} -module H ​ H i, n H{H}_{i,n} est inclus dans le noyau de l’opérateur

 | E n = ∏ | m ′ | = n ( χ − e m ′ ​ I ​ d) E_{n}=\prod_{|m^{\prime}|=n}(\chi-e_{m^{\prime}}Id) |  |

Pour pouvoir appliquer les méthodes de la section II à H ​ H i, n H{H}_{i,n}, il suffit de montrer que, génériquement en μ i \mu^{i}, ce module coincide avec le noyau de l’opérateur E n E_{n}. Or, génériquement en μ i \mu^{i}, la famille des monômes x e m ′ x^{e_{m^{\prime}}} forme une base de ce noyau. Or, par une récurrence sur les fonctions z... z^{...} et y... y^{...}, et par la résolution triangulaire du système ( 3 i) (3_{i}), on montre que ces fonctions sont des combinaisons linéaires des fonctions x r... x^{r_{...}}, par un système triangulaire inversible: en effet, si χ ​ f = r ℓ + 1 ​ f + g \chi f=r_{\ell+1}f+g avec f | x = 1 ≡ 0 f_{|x=1}\equiv 0, et si g = ∑ j = 0 ℓ a j ​ ( τ, r 1, …, r ℓ) ​ x r j g=\sum_{j=0}^{\ell}a_{j}(\tau,r_{1},\ldots,r_{\ell})x^{r_{j}} (convention r 0 = 1 r_{0}=1), où les a j a_{j} sont des polynômes en τ \tau dont les coefficients sont des fonctions rationnelles non identiquement nulles, alors

 | f = ∑ j = 0 ℓ a j r j − r ℓ + 1 ​ x r j − ( ∑ j = 0 ℓ a j r j − r ℓ + 1) ​ x r ℓ + 1 f=\sum_{j=0}^{\ell}\frac{a_{j}}{r_{j}-r_{\ell+1}}x^{r_{j}}-(\sum_{j=0}^{\ell}\frac{a_{j}}{r_{j}-r_{\ell+1}})x^{r_{\ell+1}} |  |

Ainsi, f = ∑ j = 0 ℓ + 1 b j ​ ( τ, r 1, …, r ℓ + 1) ​ x r j f=\sum_{j=0}^{\ell+1}b_{j}(\tau,r_{1},\ldots,r_{\ell+1})x^{r_{j}} et les fonctions b j b_{j} sont des polynômes en τ \tau, dont les coefficients sont rationnelles et non identiquement nulles. Par conséquent, les monômes X i, m 1, …, m i m ′ X^{m^{\prime}}_{i,m_{1},...,m_{i}} forment une base du noyau de l’opérateur E n E_{n} pour des valeur génériques de μ i \mu^{i}.

La double inclusion est donc réalisée sur le ℝ ​ { α i } \mathbb{R}\{\alpha^{i}\} -module H ​ H i, n H{H}_{i,n}, et en prenant la restriction au graphe v ↦ α i ​ ( v) = ( μ i ​ ( v), τ ⁡ ( v), v) v\mapsto\alpha^{i}(v)=(\mu^{i}(v),\tau(v),v), elle est réalisée sur le ℝ ​ { v } \mathbb{R}\{v\} -module des i i -blocs χ \chi -homogènes de degré n n. Dés lors, on applique exactement la démarche de la section II à l’algèbre Q ​ R ​ H ~ i, m 1, …, m i 1, p ​ ( x, v) \widetilde{QR{H}}^{1,p}_{i,m_{1},\ldots,m_{i}}(x,v). Si on note c c l’immersion: ( x, v) ↦ ( X i, m 1, …, m i ​ ( x, v), v) (x,v)\mapsto(X_{i,m_{1},\ldots,m_{i}}(x,v),v), cette algèbre est χ \chi -équivalente à la sous-algèbre

 | Q ​ R ​ H ~ i, m 1, …, m i, ( c ​ v ​ g) 1, p = c ∗ ​ ( ℝ ⁡ { X i, m 1, …, m i, v } CLOSE \widetilde{QR{H}}^{1,p}_{i,m_{1},\ldots,m_{i},(cvg)}=c^{*}(\mathbb{R}\{X_{i,m_{1},\ldots,m_{i}},v\} |  |

à laquelle s’applique le lemme d’extension IB2. De plus, on obtient (comme dans la section II) l’existence et l’injectivité du morphisme série formelle f ↦ f ^ i f\mapsto\widehat{f}^{i}.

En substituant les formules ( 2 i) (2_{i}) (linéaires dans les fonctions élémentaires), dans un ( i − 1) (i-1) -bloc, on obtient un i i -bloc de même degré (en convenant qu’un 0-bloc est un bloc χ \chi -homogène dans les variables ( x, z) (x,z)) . Par l’existence et l’injectivité des morphismes séries formelles f ↦ f ^ i − 1 f\mapsto\widehat{f}^{i-1} et f ↦ f ^ i f\mapsto\widehat{f}^{i}, cette application se prolonge injectivement de Q ​ R ​ H ~ i − 1, m 1, …, m i − 1 1, p \widetilde{QR{H}}^{1,p}_{i-1,m_{1},...,m_{i-1}} vers Q ​ R ​ H ~ i, m 1, …, m i 1, p \widetilde{QR{H}}^{1,p}_{i,m_{1},...,m_{i}}. Ceci donne les inclusions du lemme. Ces extensions sont donc des extensions étoilées, les morphismes associés étant simplement l’identité.∎

(b) Division de g a g_{a} dans l’idéal ( φ) (\varphi) dans l’extension Q ​ R ​ H ~ p 1, p \widetilde{QR{H}}^{1,p}_{p}.

Choisissons m 1 ≥ max ⁡ { n a, j; j = 1, …, p } m_{1}\geq\max\{n_{a,j};\ j=1,\ldots,p\}. Soit G 1 G_{1} l’image de g a g_{a} dans l’extension Q ​ R ​ H ~ 1, m 1 1, p \widetilde{QR{H}}^{1,p}_{1,m_{1}}. Il est de même degré n n que g a g_{a}, et son idéal χ \chi -transverse est inclus dans ( φ) (\varphi). D’après les égalités (1), les germes τ j, 1 ​ ( v) \tau_{j,1}(v) appartiennent à l’idéal ( v 1 × ⋯ × v p) = r a d ( ( φ)) (v_{1}\times\cdots\times v_{p})=rad((\varphi)). Donc d’après les formules ( 2 1) (2_{1}) et le choix de m 1 m_{1}, on a la division

 | G 1 = H 1 + φ ​ H 2 G_{1}=H_{1}+\varphi H_{2} |  |

les germes H 1 H_{1} et H 2 H_{2} sont des 1-blocs de degré n n, et les monômes de H 1 H_{1} sont indépendants des fonctions élémentaires y m 1 y^{m_{1}}. D’après les égalités (1) et les équations ( 3 1) (3_{1}), les fonctions élémentaires z. z^{.} sont indépendantes de la coordonnée v p v_{p}. Comme l’idéal χ \chi -transverse de H 1 H_{1} est inclus dans ( φ) (\varphi), un développement taylorien de ses coefficients donne la division

 | H 1 = v p n a, p ​ F 1 H_{1}=v_{p}^{n_{a,p}}F_{1} |  |

le germe F 1 F_{1} étant un 1-bloc de degré n n, dont l’idéal χ \chi -transverse est inclus dans ( φ 1) = ( v 1 n a, 1 × ⋯ × v p − 1 n a, p − 1) (\varphi_{1})=(v_{1}^{n_{a,1}}\times\cdots\times v_{p-1}^{n_{a,p-1}}). Ainsi, par une récurrence sur i i, et en choisissant m 2 = m 1 m_{2}=m_{1}, …, m p = m 1 m_{p}=m_{1}, on obtient que l’image G p G_{p} de g a g_{a} dans l’algèbre Q ​ R ​ H ~ p, m 1, …, m p 1, p \widetilde{QR{H}}^{1,p}_{p,m_{1},...,m_{p}} s’écrit

 | G p = φ ​ H p G_{p}=\varphi H_{p} |  |

le germe H p H_{p} étant un p p -bloc de degré n n.

(c) Division de f a f_{a} dans l’idéal ( φ) (\varphi) dans l’extension Q ​ R ​ H ~ p 1, p \widetilde{QR{H}}^{1,p}_{p}.

Soient ( g n, a ​ ( f a) CLOSE (g_{n,a}(f_{a}) les 0-blocs de la série de f a f_{a}. D’après le théorème de division VB1, il existe un unique Q ∈ Q ​ A 1, p ​ ( x, v) Q\in QA^{1,p}(x,v) tel que f = φ ​ Q f=\varphi Q. D’autre part, pour tout n ∈ ℕ n\in\mathbb{N}, il existe un p p -bloc G p, n G_{p,n} tel que g n, a ​ ( f a) = φ ​ G p, n g_{n,a}(f_{a})=\varphi G_{p,n}. Soit N ∈ ℕ N\in\mathbb{N}, en utilisant le lemme de division II1, appliqué au germe f a − ∑ n ≤ N g n, a f_{a}-\sum_{n\leq N}g_{n,a}, on obtient

 | Q − ∑ n ≤ N G p, n ∈ ( x N) ​ S ​ B 0 1, p Q-\sum_{n\leq N}G_{p,n}\in(x^{N})SB^{1,p}_{0} |  |

Et ceci prouve que Q ∈ Q ​ R ​ H ~ p, m 1, …, m 1 1, p Q\in\widetilde{QR{H}}^{1,p}_{p,m_{1},\ldots,m_{1}}.

Il est clair que l’idéal χ \chi -transverse de Q Q n’est pas propre. Soit m ​ a a ma_{a} sa multilicité algébrique (lemme IIIB2). On a I χ, Q ⊃ ( x m ​ a a + ε) I_{\chi,Q}\supset(x^{ma_{a}+\varepsilon}) pour tout ε > 0 \varepsilon>0. Donc, par la définition de la multiplicité algébrique, on a m ​ a a ≤ m ​ a χ ​ ( f) ma_{a}\leq ma_{\chi}(f) pour tout a a.

Remarque IIIB1. Notons φ i ​ ( v) = ∏ j = 1 i v j n a, j \varphi_{i}(v)=\prod_{j=1}^{i}v_{j}^{n_{a,j}}. Si h ∈ Φ a ∗ ( Q R H | U a 1, q + ( 0, p)) h\in\Phi_{a}^{*}(QR{H}^{1,q+(0,p)}_{|U_{a}}) et si on note h i h_{i} son image dans l’extension Q ​ R ​ H ~ i, m 1, …, m 1 1, p \widetilde{QR{H}}^{1,p}_{i,m_{1},\ldots,m_{1}}, l’étude précédente montre que la série formelle de h i h_{i} est la somme d’une série formelle h ^ i, 1 \widehat{h}_{i,1} indépendante des fonctions élémentaires y... y^{...}, et d’une série formelle h ^ i, 2 \widehat{h}_{i,2} qui se divise par φ i \varphi_{i}, dans l’anneau des séries formelles associé à Q ​ R ​ H ~ i, m 1, …, m 1 1, p \widetilde{QR{H}}^{1,p}_{i,m_{1},\ldots,m_{1}}.

Remarque IIIB2. Une conséquence facile de cette étude est que tout élément d’une algèbre Q ​ R ​ H ~... \widetilde{QR{H}}_{...} se divise dans son idéal χ \chi -transverse dans une extension Q ​ R ​ H ~ ~... \widetilde{\widetilde{QR{H}}}_{...} obtenue en prenant aussi les développements ( 2...) (2_{...}) pour les fonctions élémentaires y... y^{...}. Ces nouvelles algèbres satisfont aussi au lemme IIIB2,…etc.

§2. Cas ℓ > 0 \ell>0.

Reprenons la dérivation χ = x ∂ / ∂ x − ∑ j = 1 ℓ s j ( μ) u j ∂ / ∂ u j \chi=x\partial/\partial x-\sum_{j=1}^{\ell}s_{j}(\mu)u_{j}\partial/\partial u_{j}. Soit

 | f ∈ Q ​ R ​ H 1, q ​ ( x, α, u) f\in QR{H}^{1,q}(x,\alpha,u) |  |

et soit J f ⊂ ℝ ​ { α, λ } J_{f}\subset\mathbb{R}\{\alpha,\lambda\} son idéal χ \chi -transverse le long de γ = { ( α, u) ​ 0 } \gamma=\{(\alpha,u)0\}. Les coordonnées λ = ( λ 1, …, λ ℓ) \lambda=(\lambda_{1},\ldots,\lambda_{\ell}) sont les intégrales premières non triviales de χ \chi: λ j = x s j ​ u j \lambda_{j}=x^{s_{j}}u_{j}. Il s’agit d’abord de diviser localement f f dans l’idéal π χ ∗ ​ ( J f) \pi_{\chi}^{*}(J_{f}), dans un anneau qui possède une structure asymptotique élémentaire. L’idée générale est la suivante: en général, les blocs formels χ \chi -homogènes de la série de f f sont divergents, et leurs idéaux χ \chi -transverses sont dans un anneau formel. Mais, on a vu dans la partie IIIA, que si le germe f f est presque quasi-convergent (bien approché par les germes quasi-convergents dans la M ( α, u) {M}_{(\alpha,u)} -topologie), alors il possède une multiplicité algébrique et un idéal limite transverse. On applique donc à J f J_{f} une désingularisation dans laquelle (ie. localement) le germe f f est presque quasi-convergent, et mieux encore, le quotient de cette division locale par π c ​ h ​ i ∗ ​ ( J f) \pi_{c}hi^{*}(J_{f}), satisfait à lhypothèse ( H ​ λ) (H\lambda) (ou mieux encore, son idéal χ \chi -transverse n’est pas propre!). Ceci nécéssite une préparation des intégrales premières non triviales λ j \lambda_{j}, simlaire à celle des intégrales premières μ j \mu_{j}.

Soit donc ( ψ, N) (\psi,{N}) une désingularisation d’Hironaka dans laquelle l’idéal J f J_{f} est principal et monomial (lemme IIIB1). Soit ( a, V a) (a,V_{a}) une carte de cette désingularisation de coordonnée v v. Soit ( φ) = ψ a ∗ ​ ( J f) (\varphi)=\psi_{a}^{*}(J_{f}) avec φ = ∏ j = 1 p v j n j \varphi=\prod_{j=1}^{p}v_{j}^{n_{j}} et μ j, a \mu_{j,a} et soient λ j, a \lambda_{j,a} les relevés des coordonnées μ j \mu_{j} et λ j \lambda_{j}. Notons s j, 0 = 1 + μ j, a s_{j,0}=1+\mu_{j,a} ( = r j, 0 =r_{j,0}, voir §1). On suppose (pour simplifier les notations!) que p = | q | p=|q| et que les germes μ j, a \mu_{j,a} et λ j, a \lambda_{j,a} sont préparés sphériquement comme dans les formules (1)

 | μ j, a ​ ( v) = μ j, p + 1 − i + μ j, p + 1 − i ′ ​ 4 \mu_{j,a}(v)=\mu_{j,p+1-i}+\mu^{\prime}_{j,p+1-i}4 |  |  |

 | λ j, a = λ j, p + 1 − i + λ j, p + 1 − i ′ ​ 4 ′ \lambda_{j,a}=\lambda_{j,p+1-i}+\lambda^{\prime}_{j,p+1-i}4^{\prime} |  |  |

les fonctions μ j, p + 1 − i \mu_{j,p+1-i} et λ j, p + 1 − i \lambda_{j,p+1-i} étant indépendantes des coordonnées ( v i, …, v p) (v_{i},\ldots,v_{p}) et les fonctions μ j, p + 1 − i ′ \mu^{\prime}_{j,p+1-i} et λ j, p + 1 − i ′ \lambda^{\prime}_{j,p+1-i} appartiennent à l’idéal ( v 1 × ⋯ × v i) (v_{1}\times\cdots\times v_{i}) dans l’anneau ℝ ​ { v } \mathbb{R}\{v\}. Notons toujours ( ψ, N) (\psi,{N}) la composée de ces deux désingularisations.

Comme dans le paragraphe 1, on commence par relever les germes de f f et χ \chi (qu’on note de la même façon), dans l’extension naturelle dans les coordonnées ( x, α, v, u) (x,\alpha,v,u): f ∈ Q ​ R ​ H 1, q + ( 0, p) ​ ( x, α, v, u) f\in QR{H}^{1,q+(0,p)}(x,\alpha,v,u) et v v sont des intégrales premières de χ \chi. On note aussi de la même façon l’idéal χ \chi -transverse J f J_{f}, dans ce relevé. Soient les morphismes analytiques

 | ψ a: v ∈ V a ↦ ( α a ​ ( v), λ a ​ ( v)) ​ et ​ Ψ a: v ∈ V a ↦ ( ψ a ​ ( v), v) ∈ W a = Ψ a ​ ( V a) \psi_{a}:v\in V_{a}\mapsto(\alpha_{a}(v),\lambda_{a}(v))\ \text{et}\ \Psi_{a}:\ v\in V_{a}\mapsto(\psi_{a}(v),v)\in W_{a}=\Psi_{a}(V_{a}) |  |

Le morphisme Ψ a \Psi_{a} étant un difféomorphisme sur son image, les anneaux ℝ ​ { v } \mathbb{R}\{v\} et ℝ { α, λ, v } | W a \mathbb{R}\{\alpha,\lambda,v\}_{|W_{a}} sont isomorphes; donc Ψ a ∗ ​ ( J f | W a) = ( φ) \Psi_{a}^{*}(J_{f|W_{a}})=(\varphi). Soit U a = π χ − 1 ​ ( W a) U_{a}=\pi_{\chi}^{-1}(W_{a}), il contient l’orbite principale γ a = { ( α, v, u) = 0 } \gamma_{a}=\{(\alpha,v,u)=0\}. Par le difféomorphisme Ψ a \Psi_{a}, identifions les variétés analytiques V a V_{a} et W a W_{a}, et les idéaux J f | W a J_{f|W_{a}} et ( φ) (\varphi). Notons π χ | U a: ( U a, 0) → ( V a, 0) \pi_{\chi|U_{a}}:(U_{a},0)\to(V_{a},0) le germe en 0 de la restriction à la variété analytique U a U_{a}, de la projection intégrale π χ \pi_{\chi}. Il s’agit de diviser f a = f | U a f_{a}=f_{|U_{a}} dans l’idéal π χ | U a ∗ ​ ( φ) \pi_{\chi|U_{a}}^{*}(\varphi). La démarche suit et généralise celle du cas ℓ = 0 \ell=0: on construit p p extensions Q ​ R ​ H ~ i ⊂ Q ​ A \widetilde{QR{H}}_{i}\subset QA, de l’algèbre Q R H 1, q + ( 0, p) | U a QR{H}^{1,q+(0,p)}_{|U_{a}}, telles que l’image de f a f_{a} dans la p p -ème extension, se divise par φ \varphi, dans cette p p -ème extension. Ces extensions possèdent bien sûr une structure asymptotique élémentaire.

(a) Division par l’idéal ( v p n p) (v_{p}^{n_{p}}) dans une extension Q ​ R ​ H ~ 1 \widetilde{QR{H}}_{1}.

Reprenons les notations du §1 relatives aux formules (4) (qui remplacent les formules (1)). Soient u ( 1) = ( u 1, 1, …, u ℓ, 1) u^{(1)}=(u_{1,1},\ldots,u_{\ell,1}) des coordonnées analytiques locales sur ( ℝ ℓ, 0) (\mathbb{R}^{\ell},0). La dérivation

 | X 1 = χ − ∑ j = 1 ℓ r j, 1 ​ ( v) ​ u j, 1 ​ ∂ ∂ u j, 1 {X}_{1}=\chi-\sum_{j=1}^{\ell}r_{j,1}(v)u_{j,1}\frac{\partial}{\partial u_{j,1}} |  |

agit sur l’algèbre Q ​ R ​ H 1, q + ( 0, p + ℓ) ​ ( x, α, v, u, u ( 1)) QR{H}^{1,q+(0,p+\ell)}(x,\alpha,v,u,u^{(1)}). Il admet γ 1 = { ( α, v, u, u ( 1)) = 0 } \gamma_{1}=\{(\alpha,v,u,u^{(1)})=0\} comme orbite principale. Notons λ ( 1) = ( λ 1, 1, …, λ ℓ, 1) \lambda^{(1)}=(\lambda_{1,1},\ldots,\lambda_{\ell,1}) des coordonnées sur ( ℝ ℓ, 0) (\mathbb{R}^{\ell},0). Des coordonnées analytiques transverses à γ 1 \gamma_{1} sont ( α, λ, v, λ ( 1)) (\alpha,\lambda,v,\lambda^{(1)}). Soit W 1 = { ( Ψ a ​ ( v), λ ( 1) ​ ( v)); v ∈ V a } {W}_{1}=\{(\Psi_{a}(v),\lambda^{(1)}(v));\ v\in V_{a}\} et U 1 = π X 1 − 1 ​ ( W 1) {U}_{1}=\pi_{{X}_{1}}^{-1}({W}_{1}). Les germes λ j, 1 ​ ( v) \lambda_{j,1}(v) sont donnés par les formules (4’). Sur la variété analytique U 1 {U}_{1} (de dimension p + 1 p+1), on a donc les relations supplémentaires x r j, 1 ​ ( v) ​ u j, 1 = λ j, 1 ​ ( v) x^{r_{j,1}(v)}u_{j,1}=\lambda_{j,1}(v). Comme précédement, on identifie les variétés analytiques W 1 {W}_{1} et V a V_{a} (de dimension p p), et on note π X 1 | U 1: U 1 → V a \pi_{{X}_{1}|{U}_{1}}:{U}_{1}\to V_{a} la restriction associée. On a l’injection canonique

 | Q ​ R ​ H ​ ( x, α, v, u) ↪ Q ​ R ​ H ​ ( x, α, v, u, u ( 1)) QR{H}(x,\alpha,v,u)\hookrightarrow QR{H}(x,\alpha,v,u,u^{(1)}) |  |

par la projection canonique π ′: ( x, α, v, u, u ( 1)) ↦ ( x, α, v, u) \pi^{\prime}:(x,\alpha,v,u,u^{(1)})\mapsto(x,\alpha,v,u). Notons toujours f f son image dans cette extension. Par la définition de U 1 {U}_{1}, la restriction π ′ | U 1: U 1 → U a \pi^{\prime}_{|{U}_{1}}:{U}_{1}\to U_{a} est un difféomorphisme sur son image U a U_{a}. On a donc aussi l’injection canonique

 | Q R H ( x, α, v, u) | U a ↪ Q R H ( x, α, v, u, u ( 1)) | U 1 QR{H}(x,\alpha,v,u)_{|U_{a}}\hookrightarrow QR{H}(x,\alpha,v,u,u^{(1)})_{|{U}_{1}} |  |

L’image de la dérivation restreinte X 1 | U 1 {X}_{1|{U}_{1}} est la dérivation χ \chi, et les idéaux transverses (le long de γ a \gamma_{a} et γ 1 \gamma_{1}, dans la variété V a V_{a}), sont préservés (lemme de transfert IB6). Notons toujours f a f_{a} la restriction de f f à U 1 {U}_{1}.

Soient w ( 1) = ( w 1, 1, …, w ℓ, 1) w^{(1)}=(w_{1,1},\ldots,w_{\ell,1}) des coordonnées sur ( ℝ ℓ, 0) (\mathbb{R}^{\ell},0). Soit le difféomorphisme sur ( ℝ + ⁣ ∗ × ℝ 2 ​ ( p + ℓ), 0) (\mathbb{R}^{+*}\times\mathbb{R}^{2(p+\ell)},0)

 | Φ 1 ​ ( x, α, v, u, u ( 1)) = ( x, α, v, u ( 1), w ( 1)) = ( x, α, v, u ( 1), u − u ( 1)) \Phi_{1}(x,\alpha,v,u,u^{(1)})=(x,\alpha,v,u^{(1)},w^{(1)})=(x,\alpha,v,u^{(1)},u-u^{(1)}) |  |

et soient X 1 ′ = ( Φ 1) ∗ ​ X 1 {X}^{\prime}_{1}=(\Phi_{1})_{*}{X}_{1}, U 1 ′ = Φ 1 ​ ( U 1) {U}^{\prime}_{1}=\Phi_{1}({U}_{1}) et γ 1 ′ = Φ 1 ​ ( γ 1) \gamma^{\prime}_{1}=\Phi_{1}(\gamma_{1}). On a trivialement

 | Φ 1 ∗ ​ ( Q ​ R ​ H ​ ( x, α, v, u ( 1), w ( 1))) = Q ​ R ​ H ​ ( x, α, v, u, u ( 1)) \Phi_{1}^{*}(QR{H}(x,\alpha,v,u^{(1)},w^{(1)}))=QR{H}(x,\alpha,v,u,u^{(1)}) |  |

et

 | Φ 1 ∗ ( Q R H ( x, α, v, u ( 1), w ( 1)) | U ′ 1) = Q R H ( x, α, v, u, u ( 1)) | U 1 \Phi_{1}*(QR{H}(x,\alpha,v,u^{(1)},w^{(1)})_{|{U}^{\prime}_{1}})=QR{H}(x,\alpha,v,u,u^{(1)})_{|{U}_{1}} |  |

Soit f ′ = ( Φ 1 − 1) ∗ ​ ( f) f^{\prime}=(\Phi_{1}^{-1})^{*}(f) et f a ′ f^{\prime}_{a} sa restriction à U 1 ′ {U}^{\prime}_{1}. Pour poursuivre, on a besoin de la définition suivante

###### Définition IIIB1

Soit t t une coordonnée locale sur ( ℝ k, 0) (\mathbb{R}^{k},0) et soit χ 0 = x ∂ / ∂ x \chi_{0}=x\partial/\partial x. L’extension

 | Q ​ R ​ H ~ 1, m 1 1, ( p, k) ​ ( x, v, t) ⊂ Q ​ A 1, p + k ​ ( x, v, t) \widetilde{QR{H}}^{1,(p,k)}_{1,m_{1}}(x,v,t)\subset QA^{1,p+k}(x,v,t) |  |

est l’algèbre des germes qui possèdent une série asymptotique formelle dans les 1-blocs χ 0 \chi_{0} -homogènes de complexité m 1 m_{1}, construits (comme au §1) grâce aux formules ( 4) (4), et dont les coefficients appartiennent à l’anneau ℝ ​ { v, t } \mathbb{R}\{v,t\}.

Remarque IIIB3. Pour toute partition t = ( t ′, t ​ ") ∈ ℝ k 1 × ℝ k 2 t=(t^{\prime},t")\in\mathbb{R}^{k_{1}}\times\mathbb{R}^{k_{2}}

 | Q ​ R ​ H ~ 1, m 1 1, ( p, k) ​ ( x, v, t) ⊂ Q ​ R ​ H ~ 1, m 1 1, ( p, k 1) ​ ( x, v, t ′) ​ { t ​ " } \widetilde{QR{H}}^{1,(p,k)}_{1,m_{1}}(x,v,t)\subset\widetilde{QR{H}}^{1,(p,k_{1})}_{1,m_{1}}(x,v,t^{\prime})\{t"\} |  |

les séries étant convergentes sur un produit, au sens suivant

 | Q ​ R ​ H ~ 1, m 1 1, ( p, k 1) ​ ( x, v, t ′) ​ { t ​ " } ⊂ S ​ B 1, p + k ​ ( x, v, t) \widetilde{QR{H}}^{1,(p,k_{1})}_{1,m_{1}}(x,v,t^{\prime})\{t"\}\subset SB^{1,p+k}(x,v,t) |  |

et pour tout h ∈ Q ​ R ​ H ~ 1, m 1 1, ( p, k 1) ​ ( x, v, t ′) ​ { t ​ " } h\in\widetilde{QR{H}}^{1,(p,k_{1})}_{1,m_{1}}(x,v,t^{\prime})\{t"\}, de série

 | h = ∑ | m | ≥ 0 h m ​ ( t ​ ") m h=\sum_{|m|\geq 0}h_{m}(t")^{m} |  |

il existe un domaine standard Ω \Omega tel que h m ∈ Q ​ A 1, p + k 1 ​ [Ω] h_{m}\in QA^{1,p+k_{1}}[\Omega] pour tout m m.

Soient U 1, a U_{1,a} et U 2, a U_{2,a} les variétés analytiques, images de U 1 ′ {U}^{\prime}_{1} par les projections canoniques

 | ( x, α, v, u ( 1), w ( 1)) ↦ ( x, v, u ( 1)) et ( x, α, v, u ( 1), w ( 1)) ↦ ( x, v, u ( 1), w ( 1)) (x,\alpha,v,u^{(1)},w^{(1)})\mapsto(x,v,u^{(1)})\quad\text{et}\quad(x,\alpha,v,u^{(1)},w^{(1)})\mapsto(x,v,u^{(1)},w^{(1)}) |  |

et soient γ 1, a \gamma_{1,a}, γ 2, a \gamma_{2,a} les images de γ 1 ′ \gamma^{\prime}_{1}. Les restrictions de ces projections à ces variétés sont des difféomorphismes. Par une généralisation facile des résultats du §1, on a l’injection suivante pour tout m 1 m_{1}

 | Q R H 1, q + ( 0, p + ℓ) ( x, α, v, u ( 1), w ( 1)) | U ′ 1 ↪ Q ​ R ​ H ~ 1, m 1 1, ( p, 2 ​ ℓ) ( x, v, u ( 1), w ( 1)) | U 2, a QR{H}^{1,q+(0,p+\ell)}(x,\alpha,v,u^{(1)},w^{(1)})_{|{U}^{\prime}_{1}}\hookrightarrow\widetilde{QR{H}}^{1,(p,2\ell)}_{1,m_{1}}(x,v,u^{(1)},w^{(1)})_{|U_{2,a}} |  | 5 |

La dérivation X 1 ′ {X}^{\prime}_{1} (restreinte à U 1 ′ {U}^{\prime}_{1}) est préservée (par restriction à U 2, a U_{2,a}). Choisissons m 1 > max ⁡ { n j; j = 1, …, p } m_{1}>\max\{n_{j};\ j=1,\ldots,p\}. Soit h ∈ Q ​ R ​ H ~ 1, m 1 1, ( p, 2 ​ ℓ) h\in\widetilde{QR{H}}^{1,(p,2\ell)}_{1,m_{1}} tel que l’image de f a ′ f^{\prime}_{a} dans cette extension soit égale à h a = h | U 2, a h_{a}=h_{|U_{2,a}}. La motivation de ces extensions est la suivante: par la définition de U 1 {U}_{1}, on a

 | x s j, 0 ​ u j | U 1 = λ j, a ​ ( v) et x r j, 1 ​ u j, 1 | U 1 = λ j, 1 ​ ( v) x^{s_{j,0}}u_{j|{U}_{1}}=\lambda_{j,a}(v)\quad\text{et}\quad x^{r_{j,1}}u_{j,1|{U}_{1}}=\lambda_{j,1}(v) |  |

pour tout j = 1, …, ℓ j=1,\ldots,\ell. Par conséquent, par le difféomorphisme Φ 1 \Phi_{1}, un calcul direct donne

 | x s j, 0 + r j, 1 ​ w j, 1 | U 1 ′ = λ j, 1 ′ ​ x r j, 1 + λ j, 1 ​ ( x r j, 1 − x s j, 0) x^{s_{j,0}+r_{j,1}}w_{j,1|{U}^{\prime}_{1}}=\lambda^{\prime}_{j,1}x^{r_{j,1}}+\lambda_{j,1}(x^{r_{j,1}}-x^{s_{j,0}}) |  | 6 |

(voir formules (4’)). Notons δ j ​ ( x, v) = x s j, 0 − x r j, 1 \delta_{j}(x,v)=x^{s_{j,0}}-x^{r_{j,1}}. En utilisant les développements ( 2 1) (2_{1}), on voit que l’image de δ j \delta_{j} dans l’extension (5), est un élément de l’idéal ( τ j, 1 ​ ( v)) ⊂ r ​ a ​ d ​ ( ( φ)) (\tau_{j,1}(v))\subset rad((\varphi)) (plus précisément, dans l’anneau Q ​ R ​ H ~ 1, m 1 1, p ​ ( x, v) \widetilde{QR{H}}^{1,p}_{1,m_{1}}(x,v)). D’après les formules (4’), on a λ j, 1 ′ ∈ r ​ a ​ d ​ ( ( φ)) \lambda^{\prime}_{j,1}\in rad((\varphi)), donc l’image du germe (6) dans l’extension (5), est un élément de l’idéal r ​ a ​ d ​ ( ( φ)) rad((\varphi)) dans l’anneau Q ​ R ​ H ~ 1, m 1 1, p ​ ( x, v) \widetilde{QR{H}}^{1,p}_{1,m_{1}}(x,v)).

Posons donc S 1 = m 1 ​ ∑ j = 1 ℓ ( s j, 0 + r J, 1) S_{1}=m_{1}\sum_{j=1}^{\ell}(s_{j,0}+r_{J,1}) et notons

 | h 1 = 𝕛 w ( 1) m 1 ​ ( x S 1 ​ h) et h 2 = x S 1 ​ h − h 1 h_{1}={\mathbb{j}}_{w^{(1)}}^{m_{1}}(x^{S_{1}}h)\quad\text{et}\quad h_{2}=x^{S_{1}}h-h_{1} |  | 7 |

(en prenant bien sûr l’image du monôme x S 1 x^{S_{1}} dans l’extension (5)). Notons aussi h 1, a h_{1,a} et h 2, a h_{2,a} leurs restrictions à U 2, a U_{2,a}, par la remarque IIIB3, ce sont des éléments de l’extension (5). Et, par la remarque faite sur le germe (6), et par le choix de m 1 m_{1}, le germe h 2, a h_{2,a} se divise dans l’idéal ( φ) ​ M ′ (\varphi){M}^{\prime} dans l’extension (5) ( M ′ {M}^{\prime} étant l’idéal maximal de ℝ ​ { v } \mathbb{R}\{v\}). Comme l’idéal X 1 ′ {X}^{\prime}_{1} -transverse de h a h_{a} est ( φ) (\varphi), il en est de même de celui de h 1, a h_{1,a}.

Le germe h 1 h_{1} est polynomial dans la coordonnée w ( 1) w^{(1)}. L’égalité (6) montre que sa restriction h 1, a h_{1,a} s’identifie à la restriction à U 1, a U_{1,a} d’un élément F 1 F_{1} de l’algèbre Q ​ R ​ H ~ 1, m 1 1, ( p, ℓ) ​ ( x, v, u ( 1)) \widetilde{QR{H}}^{1,(p,\ell)}_{1,m_{1}}(x,v,u^{(1)}). L’image dans cette extension, de la dérivation X 1 ′ {X}^{\prime}_{1} (restreinte à U 2, a U_{2,a}), est la dérivation

 | χ 1 = χ 0 − ∑ j = 1 ℓ r j, 1 ​ u j, 1 ​ ∂ ∂ u j, 1 \chi_{1}=\chi_{0}-\sum_{j=1}^{\ell}r_{j,1}u_{j,1}\frac{\partial}{\partial u_{j,1}} |  |

(restreinte à U 1, a U_{1,a}). Les idéaux transverses sont préservés dans cette extension. Notons F 1, a F_{1,a} la restriction de F 1 F_{1} à U 1, a U_{1,a}. L’idéal χ 1 \chi_{1} -transverse de F 1, a F_{1,a}, le long de γ 1, a \gamma_{1,a}, est ( φ) (\varphi).

Il s’agit maintenant de montrer que F 1, a F_{1,a} appartient à l’idéal ( v p n p) (v_{p}^{n_{p}}) dans l’anneau Q ​ R ​ H ~ 1, m 1 | U 1, a 1, ( p, ℓ) ​ ( x, v, u ( 1)) \widetilde{QR{H}}^{1,(p,\ell)}_{1,m_{1}|U_{1,a}}(x,v,u^{(1)}). Pour cela, on commence par effectuer une division de F 1 F_{1} par v p n p v_{p}^{n_{p}} dans l’anneau Q ​ R ​ H ~ 1, m 1 1, ( p, ℓ) ​ ( x, v, u ( 1)) \widetilde{QR{H}}^{1,(p,\ell)}_{1,m_{1}}(x,v,u^{(1)}). En effet, d’après le théorème de division VB1 dans l’anneau Q ​ A 1, p + ℓ ​ ( x, v, u ( 1)) QA^{1,p+\ell}(x,v,u^{(1)}), il existe f 1 ∈ Q ​ A 1, p + ℓ ​ ( x, v, u ( 1)) f_{1}\in QA^{1,p+\ell}(x,v,u^{(1)}) et R 1, …, R n p ∈ Q ​ A 1, p + ℓ − 1 ​ ( x, v 1, …, v p − 1, u ( 1)) R_{1},\ldots,\ R_{n_{p}}\in QA^{1,p+\ell-1}(x,v_{1},\ldots,v_{p-1},u^{(1)}) tels que

 | F 1 = v p n p ​ f 1 + ∑ j = 0 n p − 1 v p j ​ R j = v p n p ​ f 1 + R F_{1}=v_{p}^{n_{p}}f_{1}+\sum_{j=0}^{n_{p}-1}v_{p}^{j}R_{j}=v_{p}^{n_{p}}f_{1}+R |  |

Par la remarque IIIB3, les opérations de prise de jet fini en w ( 1) w^{(1)}, et d’extension (5) commutent. Donc, d’après la remarque IIIB1, la série formelle F ^ 1 \widehat{F}_{1} relativement à la dérivation χ 0 \chi_{0}, est la somme d’une série formelle F ^ 1, 1 \widehat{F}_{1,1} indépendante des fonctions élémentaires y m 1 y^{m_{1}}, et d’une série formelle F ^ 1, 2 \widehat{F}_{1,2} qui se divise dans l’idéal ( φ) (\varphi) dans l’anneau formel associé à Q ​ R ​ H ~ 1, m 1 1, ( p, ℓ) ​ ( x, v, u ( 1)) \widetilde{QR{H}}^{1,(p,\ell)}_{1,m_{1}}(x,v,u^{(1)}). En divisant dans l’idéal ( v p n p) (v_{p}^{n_{p}}), les 1-blocs χ 0 \chi_{0} -homogènes et les restes de la série F ^ 1 \widehat{F}_{1}, et en utilisant l’unicité de la division de F 1 F_{1}, on voit que f 1 ∈ Q ​ R ​ H ~ 1, m 1 1, ( p, ℓ) ​ ( x, v, u ( 1)) f_{1}\in\widetilde{QR{H}}^{1,(p,\ell)}_{1,m_{1}}(x,v,u^{(1)}) et que pour tout j = 0, …, n p − 1 j=0,\ldots,n_{p}-1, R j ∈ Q ​ R ​ H ~ 1, m 1 1, ( p − 1, ℓ) ​ ( x, v 1, …, v p − 1, u ( 1)) R_{j}\in\widetilde{QR{H}}^{1,(p-1,\ell)}_{1,m_{1}}(x,v_{1},\ldots,v_{p-1},u^{(1)}).

Maintenant, pour montrer que R | U 1, a ≡ 0 R_{|U_{1,a}}\equiv 0, on utilise le lemme de saturation IB5. Soit x 0 > 0 x_{0}>0 suffisament petit, et soit m 0 = ( x 0, 0) ∈ γ 1, a m_{0}=(x_{0},0)\in\gamma_{1,a}. Redressons le champ χ 1 | U 1, a \chi_{1|U_{1,a}} dans un voisinage de m 0 m_{0} inclus dans U 1, a U_{1,a}

 | x = x 0 ​ exp ⁡ ( t), u j, 1 = λ j, 1 ​ ( v) x 0 ​ exp ⁡ ( − r j, 1 ​ ( v) ​ t) x=x_{0}\exp(t),\ u_{j,1}=\frac{\lambda_{j,1}(v)}{x_{0}}\exp(-r_{j,1}(v)t) |  |

D’après le lemme de saturation IB5, le germe de F 1, a F_{1,a} en m 0 m_{0}, appartient au saturé de l’idéal ( φ) (\varphi). Donc, dans les coordonnées locales ( t, v) (t,v) sur ( ℝ p + 1, 0) (\mathbb{R}^{p+1},0), ce germe est divisible par v p n p v_{p}^{n_{p}}. Par conséquent, le germe de R | U 1, a R_{|U_{1,a}} en m 0 m_{0}, est divisible par v p n p v_{p}^{n_{p}}. Or, les germes r j, 1 ​ ( v) r_{j,1}(v) et λ j, 1 ​ ( v) \lambda_{j,1}(v) sont indépendants de la coordonnée v p v_{p} (formules (4) et (4’)). Comme R R est polynomial dans la coordonnée v p v_{p}, de degré ≤ n p − 1 \leq n_{p}-1, il s’ensuit que R | U 1, a ≡ 0 R_{|U_{1,a}}\equiv 0.

On a donc construit f 1 ∈ Q ​ R ​ H ~ 1, m 1 1, ( p, ℓ) ​ ( x, v, u ( 1)) f_{1}\in\widetilde{QR{H}}^{1,(p,\ell)}_{1,m_{1}}(x,v,u^{(1)}) tel que

 | F 1, a = v p n p ​ f 1, a F_{1,a}=v_{p}^{n_{p}}f_{1,a} |  |

(où f 1, a f_{1,a} est la restriction de f 1 f_{1} à U 1, a U_{1,a}). L’idéal χ 1 \chi_{1} -transverse de f 1, a f_{1,a} est donc égal à l’idéal ( φ 1) = ( v 1 n 1 × ⋯ × v p − 1 n p − 1) (\varphi_{1})=(v_{1}^{n_{1}}\times\cdots\times v_{p-1}^{n_{p-1}}) et, toujours par la remarque IIIB1, la série formelle de f 1 f_{1} relativement à χ 0 \chi_{0}, est la somme d’une série formelle f ^ 1, 1 \widehat{f}_{1,1} indépendante des fonctions élémentaires y m 1 y^{m_{1}}, et d’une série formelle f ^ 1, 2 \widehat{f}_{1,2} divisible par l’idéal ( φ 1) (\varphi_{1}), dans l’anneau formel associé à Q ​ R ​ H ~ 1, m 1 1, ( p, ℓ) ​ ( x, v, u ( 1)) \widetilde{QR{H}}^{1,(p,\ell)}_{1,m_{1}}(x,v,u^{(1)}).

En résumé, notons U 1, a {U}_{1,a} l’image de U 1 {U}_{1} par la projection canonique

 | ( x, α, v, u, u ( 1)) ↦ ( x, v, u, u ( 1)) (x,\alpha,v,u,u^{(1)})\mapsto(x,v,u,u^{(1)}) |  |

et Φ 1, 0 \Phi_{1,0} la restriction de Φ 1 \Phi_{1} à { α = 0 } \{\alpha=0\}. Soit H ∈ Q ​ R ​ H ~ 1, m 1 1, ( p, 2 ​ ℓ) ​ ( x, v, u ( 1), w ( 1)) H\in\widetilde{QR{H}}^{1,(p,2\ell)}_{1,m_{1}}(x,v,u^{(1)},w^{(1)}) tel que h 2, a = φ ​ H a h_{2,a}=\varphi H_{a} ( H a H_{a} étant sa restriction à U 2, a U_{2,a}). Notons H 1 = Φ 1, 0 ∗ ​ ( H) H_{1}=\Phi_{1,0}^{*}(H) et H 1, a H_{1,a} sa restriction à U 1, a {U}_{1,a}. L’image de la variété U 1, a {U}_{1,a} par la projection canonique ( x, v, u, u ( 1)) ↦ ( x, v, u ( 1)) (x,v,u,u^{(1)})\mapsto(x,v,u^{(1)}) est la variété U 1, a U_{1,a}, et par une identification triviale, Φ 1, 0 ∗ ​ ( f 1) = f 1 \Phi_{1,0}^{*}(f_{1})=f_{1}. Donc, en composant toutes ces extensions, on obtient une extension

 | ( Q ​ R ​ H ~ 1, m 1 1, ( p, 2 ​ ℓ) ( x, v, u, u ( 1)) | U 1, a, π 1) ↩ Q R H 1, q + ( 0, p) ( x, α, v, u) | U a (\widetilde{QR{H}}^{1,(p,2\ell)}_{1,m_{1}}(x,v,u,u^{(1)})_{|{U}_{1,a}},\pi_{1})\hookleftarrow QR{H}^{1,q+(0,p)}(x,\alpha,v,u)_{|U_{a}} |  |

telle que

 | π 1 ∗ ​ ( x S 1 ​ f a) = v p n p ​ f 1, a + φ ​ H 1, a \pi_{1}^{*}(x^{S_{1}}f_{a})=v_{p}^{n_{p}}f_{1,a}+\varphi H_{1,a} |  |

avec f 1 ∈ Q ​ R ​ H ~ 1, m 1 1, ( p, ℓ) ​ ( x, v, u ( 1)) f_{1}\in\widetilde{QR{H}}^{1,(p,\ell)}_{1,m_{1}}(x,v,u^{(1)}), dont la série formelle relativement à χ 0 \chi_{0} est la somme des deux séries formelles f ^ 1, 1 \widehat{f}_{1,1} et f ^ 1, 2 \widehat{f}_{1,2}, et telle que l’idéal χ 1 \chi_{1} -transverse de f 1, a f_{1,a} est ( φ 1) (\varphi_{1}). L’image dans cette extension, de la dérivation χ \chi (restreinte à U a U_{a}), est la dérivation X 1 {X}_{1} (restreinte à U 1, a {U}_{1,a}).

(b) Division dans l’idéal ( φ) (\varphi) dans une extension Q ​ R ​ H ~ p \widetilde{QR{H}}_{p}.

###### Définition IIIB2

Soient m 1, …, m i ∈ ℕ m_{1},\ldots,m_{i}\in\mathbb{N} ( i ≤ p i\leq p), et soit t t une coordonnée locale sur ( ℝ k, 0) (\mathbb{R}^{k},0). L’extension

 | Q ​ R ​ H ~ i, m 1, …, m i 1, ( p, k) ​ ( x, v, t) ⊂ Q ​ A 1, p + k ​ ( x, v, t) \widetilde{QR{H}}^{1,(p,k)}_{i,m_{1},\ldots,m_{i}}(x,v,t)\subset QA^{1,p+k}(x,v,t) |  |

est l’algèbre des germes qui possèdent une série asymptotique formelle dans les i i -blocs χ 0 \chi_{0} -homogènes de complexité ( m 1, …, m i) (m_{1},\ldots,m_{i}), construits grâce aux formules ( 4) (4), et dont les coefficients appartiennent à l’anneau ℝ ​ { v, t } \mathbb{R}\{v,t\}.

La remarque IIIB3 s’appliquent à ces algèbres.

Choisissons m 2 = ⋯ = m p = m 1 m_{2}=\cdots=m_{p}=m_{1}. On répéte le procédé du §2a, p − 1 p-1 fois, appliqué au germe f 1 f_{1}. On construit une suite de germes f i f_{i}, H i H_{i} (avec f 0 = f f_{0}=f et H 0 = 0 H_{0}=0), et une suite d’extensions

 | ( Q ​ R ​ H ~ i + 1, m 1, …, m i + 1 1, ( p, ( i + 2) ​ ℓ) ( x, v, u, u ( 1), …, u ( i + 1)) | U i + 1, a, π i, i + 1) (\widetilde{QR{H}}^{1,(p,(i+2)\ell)}_{i+1,m_{1},...,m_{i+1}}(x,v,u,u^{(1)},\ldots,u^{(i+1)})_{|{U}_{i+1,a}},\pi_{i,i+1}) |  |

 | ↩ Q ​ R ​ H ~ i, m 1, …, m i 1, ( p, ( i + 1) ​ ℓ) ( x, v, u, u ( 1), …, u ( i)) | U i, a \hookleftarrow\widetilde{QR{H}}^{1,(p,(i+1)\ell)}_{i,m_{1},\ldots,m_{i}}(x,v,u,u^{(1)},\ldots,u^{(i)})_{|{U}_{i,a}} |  |

telles que

 | π i, i + 1 ∗ ​ ( x S i + 1 ​ f i, a) = φ φ i + 1 ​ f i + 1, a + φ ​ H i + 1, a \pi_{i,i+1}^{*}(x^{S_{i+1}}f_{i,a})=\frac{\varphi}{\varphi_{i+1}}f_{i+1,a}+\varphi H_{i+1,a} |  |

avec S i = m i ​ ∑ j = 1 ℓ ( r j, i − 1 + r j, i) S_{i}=m_{i}\sum_{j=1}^{\ell}(r_{j,i-1}+r_{j,i}) pour i = 1, …, p i=1,\ldots,p. Le germe

 | H i ∈ Q ​ R ​ H ~ i, m 1, …, m i 1, ( p, ( i + 1) ​ ℓ) ​ ( x, v, u, u ( 1), …, u ( i)) H_{i}\in\widetilde{QR{H}}^{1,(p,(i+1)\ell)}_{i,m_{1},\ldots,m_{i}}(x,v,u,u^{(1)},\ldots,u^{(i)}) |  |

et le germe f i ∈ Q ​ R ​ H ~ i, m 1, …, m i 1, ( p, ℓ) ​ ( x, v, u ( i)) f_{i}\in\widetilde{QR{H}}^{1,(p,\ell)}_{i,m_{1},\ldots,m_{i}}(x,v,u^{(i)}) (en posant u ( 0) = u u^{(0)}=u). les germes H i, a H_{i,a} et f i, a f_{i,a} dénotent leurs restrictions à U i, a {U}_{i,a}. La série formelle de f i f_{i} relativement à χ 0 \chi_{0}, est la somme d’une série formelle f ^ i, 1 \widehat{f}_{i,1} indépendante des fonctions élémentaires y m 1, y m 1 ​ m 2, …, y m 1 ⋯ m i y^{m_{1}},\ y^{m_{1}m_{2}},\ldots,\ y^{m_{1}\cdots m_{i}}; et d’une série formelle f ^ i, 2 \widehat{f}_{i,2} divisible par φ i \varphi_{i} dans l’anneau formel associé à Q ​ R ​ H ~ i, m 1, …, m i 1, ( p, ℓ) ​ ( x, v, u ( i)) \widetilde{QR{H}}^{1,(p,\ell)}_{i,m_{1},\ldots,m_{i}}(x,v,u^{(i)}). La variété analytique U i, a {U}_{i,a}, de dimension p + 1 p+1, est donnée par les conditions

 | U i, a = { ( x, v, u, …, u ( i)) ∈ U i ∈ ( ℝ + ⁣ ∗ × ℝ p + ( i + 1) ​ ℓ, 0); {U}_{i,a}=\{(x,v,u,\ldots,u^{(i)})\in{U}_{i}\in(\mathbb{R}^{+*}\times\mathbb{R}^{p+(i+1)\ell},0); |  |

 | x r j, k ​ ( v) u j, k = λ j, k ( v), j = 1, …, ℓ; k = 0, …, i } x^{r_{j,k}(v)}u_{j,k}=\lambda_{j,k}(v),\ j=1,\ldots,\ell;\ k=0,\ldots,i\} |  |

L’image de la dérivation

 | X i = χ − ∑ j = 1, …, ℓ, k = 1, …, i r j, k ​ u j, k ​ ∂ ∂ u j, k {X}_{i}=\chi-\sum_{j=1,\ldots,\ell,\ k=1,\ldots,i}r_{j,k}u_{j,k}\frac{\partial}{\partial u_{j,k}} |  |

(restreinte à U i, a {U}_{i,a}), est la dérivation X i + 1 {X}_{i+1} (restreinte à U i + 1, a {U}_{i+1,a}).

Posons S a = S 1 + ⋯ + S p S_{a}=S_{1}+\cdots+S_{p}. On a donc construit une extension

 | ( Q ​ R ​ H ~ p, m 1, …, m p 1, ( p, ( p + 1) ​ ℓ) ( x, v, u, u ( 1), …, u ( p)) | U p, a, π p) ↩ Q R H 1, q + ( 0, p) ( x, α, v, u) | U a (\widetilde{QR{H}}^{1,(p,(p+1)\ell)}_{p,m_{1},...,m_{p}}(x,v,u,u^{(1)},\ldots,u^{(p)})_{|{U}_{p,a}},\pi_{p})\hookleftarrow QR{H}^{1,q+(0,p)}(x,\alpha,v,u)_{|U_{a}} |  |

telle que

 | π p ∗ ​ ( x S a ​ f a) = φ ​ Q a \pi_{p}^{*}(x^{S_{a}}f_{a})=\varphi Q_{a} |  |

avec Q ∈ ( Q ​ R ​ H ~ p, m 1, …, m p 1, ( p, ( p + 1) ​ ℓ) ​ ( x, v, u, u ( 1), …, u ( p)) CLOSE Q\in(\widetilde{QR{H}}^{1,(p,(p+1)\ell)}_{p,m_{1},...,m_{p}}(x,v,u,u^{(1)},\ldots,u^{(p)}) ( Q a Q_{a} étant sa retsriction à U p, a {U}_{p,a}). L’idéal X p {X}_{p} -transverse de Q a Q_{a} le long de γ p = { ( v, u, u ( p)) = 0 } \gamma_{p}=\{(v,u,u^{(p)})=0\}, n’est pas propre. Le germe Q a Q_{a} est donc presque quasi-convergent, car il satisfait à l’hypothèse ( H ​ λ) (H\lambda) (cf. partie IIIA §2.2). Pour finir la preuve du théorème principal IIIB1, il suffit de montrer que le germe Q a Q_{a} est X p {X}_{p} -fini.

Plus généralement, indiquons briévement comment on adapte les principaux résultats de la partie A, à l’action de la dérivation X p {X}_{p} (qu’on notera X {X} pour simplifier), sur l’algèbre étendue Q ​ R ​ H ~ p, m 1, …, m p 1, ( p, ( p + 1) ​ ℓ) ​ ( x, v, u, u ( 1), …, u ( p)) \widetilde{QR{H}}^{1,(p,(p+1)\ell)}_{p,m_{1},...,m_{p}}(x,v,u,u^{(1)},\ldots,u^{(p)}) (qu’on notera simplement Q ​ R ​ H ~ p, m 1, ( p, ℓ ′) ​ ( x, v, u ′) \widetilde{QR{H}}^{1,(p,\ell^{\prime})}_{p,m}(x,v,u^{\prime})). Soit

 | X p, m ( x, v) = ( x, z... ( x, v), y... ( x, v)) X_{p,m}(x,v)=(x,z^{...}(x,v),y^{...}(x,v)) |  |

les fonctions élémentaires de cette algèbre (cf. §1 pour les notations z... z^{...}, y... y^{...}). Les p p -blocs formels X {X} -homogènes de degré k ∈ ℤ k\in\mathbb{Z} (et de complexité m m), sont les séries formelles de la forme

 | G k = ∑ | n | − | n ′ | = k a n, n ′ ​ ( v) ​ X p, m n ​ ( u ′) n ′ G_{k}=\sum_{|n|-|n^{\prime}|=k}a_{n,n^{\prime}}(v)X_{p,m}^{n}(u^{\prime})^{n^{\prime}} |  |

avec a n, n ′ ∈ ℝ ​ { v } a_{n,n^{\prime}}\in\mathbb{R}\{v\}. On définit alors, de la même façon que dans la partie A, les germes quasi-convergents, la multiplicité algébrique relativement à X {X}, et les germes presque quasi-convergents. Soit c p, m c_{p,m} l’immesion

 | c p, m ​ ( x, v) = ( X p, m ​ ( x, v), v, u ′) c_{p,m}(x,v)=(X_{p,m}(x,v),v,u^{\prime}) |  |

et soit la sous-algèbre convergente Q ​ R ​ H ~ p, m, ( c ​ v ​ g) 1, ( p, ℓ ′ CLOSE = c ∗ ​ ( ℝ ⁡ { X p, m, v, u ′ } CLOSE \widetilde{QR{H}}^{1,(p,\ell^{\prime}}_{p,m,(cvg)}=c^{*}(\mathbb{R}\{X_{p,m},v,u^{\prime}\} (ici, X p, m X_{p,m} désignent des variables). Si on généralise les valeurs propres r j, i r_{j,i} (comme dans le lemme IIIB2), on voit que cette algèbre convergente est simplement la restriction d’une algèbre convergente Q ​ R ​ H 1, q ′ ​ ( x, α ′, u ′) c ​ v ​ g QR{H}^{1,q^{\prime}}(x,\alpha^{\prime},u^{\prime})_{cvg} au graphe du germe analytique

 | v ↦ μ ′ ​ ( v) = ( r j, i ​ ( v) − 1) j = 1, …, q 1; i = 0, …, p v\mapsto\mu^{\prime}(v)=(r_{j,i}(v)-1)_{j=1,\ldots,q_{1};\ i=0,\ldots,p} |  |

(Ceci n’est pas le cas pour l’algèbre Q ​ R ​ H ~ p, m 1, ( p, ℓ ′) ​ ( x, v, u ′) \widetilde{QR{H}}^{1,(p,\ell^{\prime})}_{p,m}(x,v,u^{\prime}): un élément de cette algèbre n’est pas forcément une restriction d’un élément d’une algèbre Q ​ R ​ H QR{H}). Donc, par une vérification aisée des formules (2’) (partie A), appliquées aux fonctions élémentaires z... z^{...}, y... y^{...}, et utilisant uniquement les équations différentielles ( 3 p) (3_{p}) (partie A), et par le lemme IIIB1, on obtient

###### Lemme IIIB3

L’algèbre Q ​ R ​ H ~ p, m, ( c ​ v ​ g) 1, ( p, ℓ ′) \widetilde{QR{H}}^{1,(p,\ell^{\prime})}_{p,m,(cvg)} est X {X} -finie, et elle satisfait globalement à la double inclusion.

On définit de la même façon que dans la partie A, la classe C ~ λ 1 \widetilde{{C}}^{1}_{\lambda} des germes qui satisfont à l’hypothèse ( H ​ λ) (H\lambda). Donc, en utilisant le lemme IIIB1, qui remplace le théorème principal II1, et le lemme IIIB3, qui remplace le théorème principal IIIA1, on obtient

###### Lemme IIIB4

La classe C ~ λ 1 \widetilde{{C}}^{1}_{\lambda} est X {X} -finie, et satisfait à la double inclusion.

Ce lemme est encore vrai sur la restriction U p, a ⊂ U p {U}_{p,a}\subset{U}_{p}, ce qui finit la preuve du théorème.∎

Cette preuve suggère la définition suivante de la multiplicité algébrique relativement à χ \chi, pour tout f ∈ Q ​ R ​ H 1, q f\in QR{H}^{1,q}: soit D {D} le diviseur exeptionnel de la désingularisation ( ψ, N) (\psi,{N}), alors on pose

 | m ​ a χ ​ ( f) = inf ( ψ, N) sup a ∈ D ( m ​ a X ​ ( Q a) − S a ​ ( 0)) ma_{\chi}(f)=\inf_{(\psi,{N})}\sup_{a\in{D}}(ma_{{X}}(Q_{a})-S_{a}(0)) |  |

et ce nombre est fini, car D {D} est compact, et la multiplicité algébrique des germes d’idéal transverse non propre (et même des germes presque quasi-convergents), est semi-continue supérieurement, comme fonction des variables v v (ceci est étudié en détail dans l’article [M’]).

IV. Démonstration du théorème 0.

A. Désingularisation de la dérivation d’Hilbert.

Soit Ξ ⁡ [Q ​ R ​ H p, q] \Xi[QR{H}^{p,q}] le Q ​ R ​ H p, q QR{H}^{p,q} -module de germes en 0 0 de champs de vecteurs à composantes dans Q ​ R ​ H p, q QR{H}^{p,q} et qui laissent invariant l’algèbre Q ​ R ​ H p, q QR{H}^{p,q}. Ce module contient le sous-module engendré par les dérivations élémentaires x j ∂ / ∂ x j x_{j}\partial/\partial x_{j} pour j = 1, …, p j=1,\ldots,p. On s’intéresse plus particulièrement à une sous-classe de Ξ ⁡ [Q ​ R ​ H p, q] \Xi[QR{H}^{p,q}] qui apparait dans le problème d’Hilbert hyperbolique, et qui a la propriété d’être stable dans une certaine désingularisation. Cette désingularisation est inspirée de la géométrie du polycycle déployé. On note cette classe Ξ ​ H ​ [Q ​ R ​ H p, q] \Xi{H}[QR{H}^{p,q}] et elle est définie de la façon suivante: soit k ≤ p k\leq p; posons r j = 1 + μ j r_{j}=1+\mu_{j} pour j = 1, …, k − 1 j=1,\ldots,k-1, x = ( x 1, ⋯, x k) x=(x_{1},\cdots,x_{k}) et x ′ = ( x k + 1, ⋯, x p) x^{\prime}=(x_{k+1},\cdots,x_{p}). Les éléments de Ξ ​ H k ​ [Q ​ R ​ H p, q] \Xi{H}_{k}[QR{H}^{p,q}] sont les germes en 0, de champs de vecteurs χ \chi qui satisfont aux conditions suivantes

L’entier k − 1 k-1 est appelé dimension de non trivialité de χ \chi, et les germes g j g_{j} sont dits ses intégrales premières non triviales. On pose

 | Ξ H [Q R H p, q] = ∪ k = 1 p Ξ H k [Q R H p, q] \Xi{H}[QR{H}^{p,q}]=\cup_{k=1}^{p}\Xi{H}_{k}[QR{H}^{p,q}] |  |

1§. Réduction de certains éléments de Ξ ⁡ [Q ​ R ​ H p, q] \Xi[QR{H}^{p,q}] à des éléments de

Ξ ​ H ​ [Q ​ R ​ H p, q] \Xi{H}[QR{H}^{p,q}].

Soit χ ∈ Ξ ⁡ [Q ​ R ​ H p, q] \chi\in\Xi[QR{H}^{p,q}] tel que χ ​ x 1 = ∏ j = 1 k x j \chi x_{1}=\prod_{j=1}^{k}x_{j} et qui admet comme intégrales premières la coordonnée α ′ \alpha^{\prime} et ( k − 1) (k-1) germes g j ​ ( x j, x j + 1, α ′) = a j ​ ( α ′) ​ d j ​ ( x j, α ′) − f j + 1 ​ ( x j + 1, α ′) g_{j}(x_{j},x_{j+1},\alpha^{\prime})=a_{j}(\alpha^{\prime})d_{j}(x_{j},\alpha^{\prime})-f_{j+1}(x_{j+1},\alpha^{\prime}) tels que d j d_{j} a la même structure que dans le cas (b) ci-dessus et f j = b j ​ ( α ′) ​ x j ​ ( 1 + O ⁡ ( x j)) ∈ Q ​ R ​ H p − k, q + ( 0, 1) ​ ( α ′, x j) f_{j}=b_{j}(\alpha^{\prime})x_{j}(1+O(x_{j}))\in QR{H}^{p-k,q+(0,1)}(\alpha^{\prime},x_{j}). Les fonctions a j a_{j} et b j b_{j} appartiennent à l’algèbre ∈ Q ​ R ​ H p − k, q \in QR{H}^{p-k,q} avec a j ​ ( 0) > 0 a_{j}(0)>0 et b j ​ ( 0) > 0 b_{j}(0)>0. Par le théorème d’inversion VB4 (appendice VB), il existe un difféomorphisme

 | H ⁡ ( x, α ′) = ( h 1 ​ ( x 1, α ′), …, h k ​ ( x k, α ′), α ′) H(x,\alpha^{\prime})=(h_{1}(x_{1},\alpha^{\prime}),\ldots,h_{k}(x_{k},\alpha^{\prime}),\alpha^{\prime}) |  |

où les germes h j h_{j} ont la même structure que les germes f j f_{j} et tel que le champ H ∗ ​ χ H_{*}\chi soit équivalent à un élément de Ξ ​ H k ​ [Q ​ R ​ H p, q] \Xi{H}_{k}[QR{H}^{p,q}].

§2. Désingularisation d’éléments de Ξ ​ H \Xi{H}.

Soit 1 < k ≤ p 1<k\leq p et χ ∈ Ξ ​ H k ​ [Q ​ R ​ H p, q] \chi\in\Xi{H}_{k}[QR{H}^{p,q}] représenté sur U ∈ ( ( ℝ + ⁣ ∗) p × ℝ | q |, 0) U\in((\mathbb{R}^{+*})^{p}\times\mathbb{R}^{|q|},0) qu’on choisit de la forme U = U 1 × U 2 U=U_{1}\times U_{2} de coordonnées ( x, α ′) (x,\alpha^{\prime}).

2.1. Premier éclatement de χ \chi.

Posons r k = 1 r_{k}=1 et pour i ≤ j i\leq j, r i, j = r i × ⋯ × r j r_{i,j}=r_{i}\times\cdots\times r_{j}. Soit χ p ​ r ∈ Ξ ​ H k {\chi}_{pr}\in\Xi{H}_{k} le champ dont ( k − 1) (k-1) intégrales premières non triviales, sont les parties principales des g j g_{j}: g j, p ​ r = x j r j − x j + 1 g_{j,pr}=x_{j}^{r_{j}}-x_{j+1}. Ces intégrales premières sont invariantes sous l’action du sous-groupe du groupe linéaire G ​ L ​ ( ℝ, k) GL(\mathbb{R},k), constitué des transformations de matrice T k, ( ρ, α ′) = D ​ i ​ a ​ g ​ ( ρ, ρ r 1, 1, …, ρ r 1, k − 1) T_{k,(\rho,\alpha^{\prime})}=Diag(\rho,\rho^{r_{1,1}},\ldots,\rho^{r_{1,k-1}}) avec ρ > 0 \rho>0. En utilisant l’action de χ p ​ r \chi_{pr} sur x 1 x_{1}, on obtient ( T k, ( ρ, α ′)) ∗ − 1 ​ χ p ​ r = ρ s k ​ Y p ​ r (T_{k,(\rho,\alpha^{\prime})})^{-1}_{*}\chi_{pr}=\rho^{s_{k}}{Y}_{pr}, avec s k = ∑ j = 1 k − 1 r 1, j s_{k}=\sum_{j=1}^{k-1}r_{1,j} et le champ Y p ​ r {Y}_{pr} a la même expression que χ p ​ r \chi_{pr} dans la coordonnée y = T k, ( ρ − 1, α ′) ​ ( x) y=T_{k,(\rho^{-1},\alpha^{\prime})}(x). La désingularisation adaptée au problème est donc quasi-sphérique dans la coordonnée x x et est fibrée dans la coordonnée α ′ \alpha^{\prime}. Soit la fonction

 | Q ⁡ ( y, α ′) = ∑ j = 1 k y j r j, k Q(y,\alpha^{\prime})=\sum_{j=1}^{k}y_{j}^{r_{j,k}} |  |

et pour ε > 0 \varepsilon>0, les quasi-sphères

 | S k + ⁣ ∗ ( ε) = { ( y, α ′) ∈ ( ℝ + ⁣ ∗) k × U 2; Q ( y, α ′) = ε } S_{k}^{+*}(\varepsilon)=\{(y,\alpha^{\prime})\in({\mathbb{\mathbb{R}}}^{+*})^{k}\times U_{2};\quad Q(y,\alpha^{\prime})=\varepsilon\} |  |

on note S k + ⁣ ∗ ​ ( α ′, ε) S_{k}^{+*}(\alpha^{\prime},\varepsilon) leurs sections par les fibres α ′ = constante \alpha^{\prime}=\text{constante}. Le morphisme d’éclatement est

 | T k: ( ρ, y, α ′) ∈ ℝ + ⁣ ∗ × S k + ⁣ ∗ ​ ( 1) ↦ ( x, α ′) = ( T k, ( ρ, α ′) ​ ( y), α ′) T_{k}:(\rho,y,\alpha^{\prime})\in{\mathbb{\mathbb{R}}}^{+*}\times S_{k}^{+*}(1)\mapsto(x,\alpha^{\prime})=(T_{k,(\rho,\alpha^{\prime})}(y),\alpha^{\prime}) |  |

Soit Y {Y} le champ de vecteurs tel que ρ s k ​ Y = ( T k) ∗ − 1 ​ χ \rho^{s_{k}}{Y}=(T_{k})^{-1}_{*}\chi. Il admet comme intégrales premières, outre la coordonnée α ′ \alpha^{\prime}, les ( k − 1) (k-1) germes G j = g j ∘ T k G_{j}=g_{j}\circ T_{k} et on vérifie facilement que G j = ρ r 1, j ​ L j G_{j}=\rho^{r_{1,j}}L_{j} avec L j ​ ( ρ, y, α ′) = y j r j ​ ( 1 + O ⁡ ( ρ)) − y j + 1 L_{j}(\rho,y,\alpha^{\prime})=y_{j}^{r_{j}}(1+O(\rho))-y_{j+1}, et elle est localement induite par un élément de l’algèbre Q ​ R ​ H p ′ ​ ( 0), q ′ ​ ( 0) QR{H}^{p^{\prime}(0),q^{\prime}(0)} avec p ′ ​ ( 0) = p − k + 1 p^{\prime}(0)=p-k+1 et q ′ ​ ( 0) = ( k ​ q 1 + k − 1, q 2 + k − 1) q^{\prime}(0)=(kq_{1}+k-1,q_{2}+k-1). Soit l’application L = ( L 1, …, L k − 1) L=(L_{1},\ldots,L_{k-1}) et u u une coordonnée sur ℝ k − 1 {\mathbb{R}}^{k-1}. Pour simplifier l’expression du champ Y {Y}, il est naturel d’introduire le morphisme suivant

 | L k ​ ( ρ, y, α ′) = ( ρ, L ⁡ ( ρ, y, α ′), α ′) = ( ρ, u, α ′) {L}_{k}(\rho,y,\alpha^{\prime})=(\rho,L(\rho,y,\alpha^{\prime}),\alpha^{\prime})=(\rho,u,\alpha^{\prime}) |  |

Soit L k, ( ρ, α ′) {L}_{k,(\rho,\alpha^{\prime})} ses fibres par ( ρ, α ′) = constante (\rho,\alpha^{\prime})=\text{constante} et D k ​ ( α ′) = L k, ( 0, α ′) ​ ( S k + ⁣ ∗ ​ ( α ′, 1)) {D}_{k}(\alpha^{\prime})={L}_{k,(0,\alpha^{\prime})}(S_{k}^{+*}(\alpha^{\prime},1)). Notons simplement D k {D}_{k} au lieu de D k ​ ( 0) {D}_{k}(0).

###### Proposition IVA1

Preuve. ( i) (i) Les ( k − 1) (k-1) germes L j ( 0,.,.) L_{j}(0,.,.) sont des intégrales premières du champ Y p ​ r {Y}_{pr} qui est transverse aux sphères S k + ⁣ ∗ ​ ( ε) S_{k}^{+*}(\varepsilon) car Y p ​ r ​ Q > 0 {Y}_{pr}Q>0. Donc, L k, 0 {L}_{k,0} est un difféomorphisme de S k + ⁣ ∗ ​ ( 0, 1) S_{k}^{+*}(0,1) sur D k {D}_{k} qui se prolonge continument à S k + ⁣ ∗ ​ ( 0, 1) ¯ \overline{S_{k}^{+*}(0,1)}. Comme r j ​ ( 0) = 1 r_{j}(0)=1 pour tout j j, le système

 | Q ⁡ ( y, 0) = 1 + u 0, y j − y j + 1 = u j Q(y,0)=1+u_{0},\quad y_{j}-y_{j+1}=u_{j} |  |

est linéaire inversible, et ceci prouve que L k, 0 {L}_{k,0} est une bijection de S k + ⁣ ∗ ​ ( 0, 1) ¯ \overline{S_{k}^{+*}(0,1)} sur D k ¯ \overline{{D}_{k}}.

( i ​ i) (ii) C’est une conséquence du ( i) (i), par transversalité et par la relative compacité de K K. La structure des composantes de l’inverse est conséquence du théorème des fonctions implicites dérivé du théorème de division VB3.

( i ​ i ​ i) (iii) Etudions l’action de Y {Y} sur la coordonnée ρ \rho. On a ρ r 1, k = Q ⁡ ( x, α ′) = Q ∘ T k ​ ( ρ, y, α ′) \rho^{r_{1,k}}=Q(x,\alpha^{\prime})=Q\circ T_{k}(\rho,y,\alpha^{\prime}) et donc ρ s k ​ ( Y ​ ρ r 1, k) = ( χ ​ Q) ∘ T k \rho^{s_{k}}({Y}\rho^{r_{1,k}})=(\chi Q)\circ T_{k}. Les sections de cette dérnière fonction par ( ρ, α ′) = (\rho,\alpha^{\prime})= constante, sont ( χ ​ Q α ′) ∘ T k, ( ρ, α ′) (\chi Q_{\alpha^{\prime}})\circ T_{k,(\rho,\alpha^{\prime})}. Or pour y ∈ ( ℝ + ⁣ ∗) k y\in({\mathbb{\mathbb{R}}}^{+*})^{k} quelconque, on a Q α ′ ∘ T k, ( ρ, α ′) ​ ( y) = ρ r 1, k ​ Q α ′ ​ ( y) Q_{\alpha^{\prime}}\circ T_{k,(\rho,\alpha^{\prime})}(y)=\rho^{r_{1,k}}Q_{\alpha^{\prime}}(y), et donc

 | ( χ p ​ r ​ Q α ′) ∘ T k, ( ρ, α ′) = ρ s k + r 1, k ​ ( Y p ​ r ​ Q α ′) (\chi_{pr}Q_{\alpha^{\prime}})\circ T_{k,(\rho,\alpha^{\prime})}=\rho^{s_{k}+r_{1,k}}({Y}_{pr}Q_{\alpha^{\prime}}) |  |

La condition (b) sur la dérivation d’Hilbert χ \chi donne

 | ( ( χ − χ p ​ r) ​ Q) ∘ T k = ρ s k + r 1, k ​ O ​ ( ρ) ((\chi-\chi_{pr})Q)\circ T_{k}=\rho^{s_{k}+r_{1,k}}O(\rho) |  |

et donc

 | Y ​ ρ = ρ ​ F k ​ ( ρ, y, α ′) avec F k = 1 r 1, k ​ ( Y p ​ r ​ Q) + O ⁡ ( ρ) {Y}\rho=\rho F_{k}(\rho,y,\alpha^{\prime})\quad\text{avec}\quad F_{k}=\frac{1}{r_{1,k}}({Y}_{pr}Q)+O(\rho) |  |

Soit χ ^ = ( L k) ∗ ​ Y \widehat{\chi}=({L}_{k})_{*}{Y} défini sur U ~ k \widetilde{U}_{k}. On a χ ^ ​ ρ = ρ ⁡ ( F k ∘ L k − 1) \widehat{\chi}\rho=\rho(F_{k}\circ{L}_{k}^{-1}). Or, les fonctions G j ∘ L k − 1 = ρ r 1, j ​ u j G_{j}\circ{L}_{k}^{-1}=\rho^{r_{1,j}}u_{j} sont des intégrales premières de χ ^ \widehat{\chi}. Par conséquent χ ^ ​ u j = − r 1, j ​ u j ​ ( F k ∘ L k − 1) \widehat{\chi}u_{j}=-r_{1,j}u_{j}(F_{k}\circ{L}_{k}^{-1}), et le champ recherché est

 | χ ~ = 1 F k ∘ L k − 1 ​ χ ^ \widetilde{\chi}=\frac{1}{F_{k}\circ{L}_{k}^{-1}}\widehat{\chi} |  |

∎

2.2. Sur le bord de S k + ⁣ ∗ ​ ( 0, 1) S_{k}^{+*}(0,1).

Ce bord est une union finie de sous-ensembles B k ′, i B_{k^{\prime},i} isomorphes chacun à l’un des sous-ensembles

 | { 0 } × S k − k ′, i + ⁣ ∗ ​ ( 0, 1) ⊂ ( ℝ +) k ′ × ( ℝ + ⁣ ∗) k − k ′ \{0\}\times S_{k-k^{\prime},i}^{+*}(0,1)\subset({\mathbb{\mathbb{R}}}^{+})^{k^{\prime}}\times({\mathbb{\mathbb{R}}}^{+*})^{k-k^{\prime}} |  |

avec k ′ < k k^{\prime}<k, l’indice i i étant énumératif

###### Proposition IVA2

Soit y 0 ∈ B k ′, i y^{0}\in B_{k^{\prime},i}. Il existe un voisinage V k ′, i V_{k^{\prime},i} de ( 0, y 0, 0) (0,y^{0},0) dans ℝ + ⁣ ∗ × S k + ⁣ ∗ ​ ( 1) {\mathbb{\mathbb{R}}}^{+*}\times S_{k}^{+*}(1) et un difféomorphisme L k ′, i {L}_{k^{\prime},i} de V k ′, i V_{k^{\prime},i} sur son image U ~ k ′, i \widetilde{U}_{k^{\prime},i} tels que le champ ( L k ′, i) ∗ ​ Y ({L}_{k^{\prime},i})_{*}{Y} soit équivalent à un élément de Ξ ​ H k ′ ​ [Q ​ R ​ H p ′ ​ ( k ′), q ′ ​ ( k ′)] \Xi{H}_{k^{\prime}}[QR{H}^{p^{\prime}(k^{\prime}),q^{\prime}(k^{\prime})}] avec p ′ ​ ( k ′) = p − k + k ′ + 1 p^{\prime}(k^{\prime})=p-k+k^{\prime}+1 et q ′ ​ ( k ′) = ( k ​ q 1 + k − 1, q 2 + k − k ′ − 1) q^{\prime}(k^{\prime})=(kq_{1}+k-1,q_{2}+k-k^{\prime}-1). Ce morphisme L k ′, i {L}_{k^{\prime},i} se prolonge continument et bijectivement sur V ¯ k ′, i ∩ { 0 } × S k + ⁣ ∗ ​ ( 0, 1) ¯ \overline{V}_{k^{\prime},i}\cap\{0\}\times\overline{S_{k}^{+*}(0,1)}. Ces composantes et celles de son inverse sont induits par des éléments de l’algèbre Q ​ R ​ H p ′, q ′ QR{H}^{p^{\prime},q^{\prime}}.

Preuve. Posons y 0 = ( y 1, 0, …, y k, 0) y^{0}=(y_{1,0},\ldots,y_{k,0}) et supposons d’abord que y 0, 1 = 0 y_{0,1}=0. Soit j 0 j_{0} le plus petit des entiers j j tels que y j, 0 = 0 y_{j,0}=0 et y j + 1, 0 > 0 y_{j+1,0}>0. La preuve consiste à trivialiser le champ Y {Y} dans la coordonnée ρ \rho en utilisant l’intégrale première G j 0 G_{j_{0}} puis, on le trivialise de la même façon dans les coordonnées y j y_{j} telles que y j, 0 > 0 y_{j,0}>0 et on utilise une récurrence sur le nombre d’intégrales premières non triviales. On a G j 0 = ρ r 1, j 0 ​ L j 0 G_{j_{0}}=\rho^{r_{1,j_{0}}}L_{j_{0}} et L j 0 ​ ( ρ, y 0, α ′) = − y j 0 + 1, 0 < 0 L_{j_{0}}(\rho,y^{0},\alpha^{\prime})=-y_{j_{0}+1,0}<0, par conséquent

 | G j 0 ​ ( ρ, y, α ′) = − y j 0 + 1, 0 ​ ρ r 1, j 0 ​ ( 1 + O ⁡ ( ‖ y − y 0 ‖)) G_{j_{0}}(\rho,y,\alpha^{\prime})=-y_{j_{0}+1,0}\rho^{r_{1,j_{0}}}(1+O(||y-y^{0}||)) |  |

Soit G = ( − G j 0) 1 / r 1, j 0 = c ​ ρ ​ ( 1 + O ⁡ ( ‖ y − y 0 ‖)) G=(-G_{j_{0}})^{1/r_{1,j_{0}}}=c\rho(1+O(||y-y^{0}||)) avec c > 0 c>0 et soit le morphisme

 | E k ′, i ​ ( ρ, y, α ′) = ( G ⁡ ( ρ, y, α ′), T k, ( ρ / G, α ′) ​ ( y), α ′) = ( ρ ′, y ′, α ′) E_{k^{\prime},i}(\rho,y,\alpha^{\prime})=(G(\rho,y,\alpha^{\prime}),T_{k,(\rho/G,\alpha^{\prime})}(y),\alpha^{\prime})=(\rho^{\prime},y^{\prime},\alpha^{\prime}) |  |

par le théorème d’inversion VB4, généralisé à plusieurs variables, il existe un voisinage V k ′, i V_{k^{\prime},i} tel que le morphisme E k ′, i E_{k^{\prime},i} soit un difféomorphisme de V k ′, i V_{k^{\prime},i} sur son image V ′ V^{\prime} qui est une sous-variété de ( ℝ + ⁣ ∗) p ′ × ℝ | q ′ | ({{\mathbb{R}}}^{+*})^{p^{\prime}}\times{{\mathbb{R}}}^{|q^{\prime}|} de codimension 1 1. De plus, il se prolonge continument en une bijection de V ¯ k ′, i ∩ { 0 } × S ¯ k + ⁣ ∗ ​ ( 0, 1) \overline{V}_{k^{\prime},i}\cap\{0\}\times\overline{S}_{k}^{+*}(0,1) sur V ′ ¯ ∩ { ( ρ ′, α ′) = 0 } \overline{V^{\prime}}\cap\{(\rho^{\prime},\alpha^{\prime})=0\}. Soit Y ′ = ( E k ′, i) ∗ ​ Y {Y}^{\prime}=(E_{k^{\prime},i})_{*}{Y}, G G étant une intégrale première de Y {Y}, on a Y ′ ​ ρ ′ = 0 {Y}^{\prime}\rho^{\prime}=0. Soit le morphisme T k ′ ​ ( ρ ′, y ′, α ′) = ( T k, ( ρ ′, α ′) ​ ( y ′), α ′) T^{\prime}_{k}(\rho^{\prime},y^{\prime},\alpha^{\prime})=(T_{k,(\rho^{\prime},\alpha^{\prime})}(y^{\prime}),\alpha^{\prime}) défini sur V ′ V^{\prime}. D’après la définition du morphisme E k ′, i E_{k^{\prime},i}, on a le diagramme commutatif

 | V k ′, i → E k ′, i V ′ T k ↓ ↓ T k ′ U k ′, i → i ​ d U k ′, i \begin{CD}V_{k^{\prime},i}@>{E_{k^{\prime},i}}>{}>V^{\prime}\\ @V{T_{k}}V{}V@V{}V{T^{\prime}_{k}}V\\ U_{k^{\prime},i}@>{id}>{}>U_{k^{\prime},i}\end{CD} |  | ∗ |

et donc les fonctions G j ′ = g j ∘ T k ′ G^{\prime}_{j}=g_{j}\circ T^{\prime}_{k} sont des intégrales premières de Y ′ {Y}^{\prime}. Or G j ′ = ( ρ ′) r 1, j ​ L j ′ G^{\prime}_{j}=(\rho^{\prime})^{r_{1,j}}L^{\prime}_{j}, donc les fonctions L j ′ L^{\prime}_{j} sont des intégrales premières de Y ′ {Y}^{\prime} et la sous-variété V ′ V^{\prime} est donnée par l’equation L j 0 ′ ​ ( ρ ′, y ′, α ′) = − 1 L^{\prime}_{j_{0}}(\rho^{\prime},y^{\prime},\alpha^{\prime})=-1 qui est un graphe: y j 0 + 1 ′ = f ⁡ ( ρ ′, y j 0 ′, α ′) = 1 + ( y j 0 ′) r j 0 ​ ( 1 + O ⁡ ( y j 0 ′)) y^{\prime}_{j_{0}+1}=f(\rho^{\prime},y^{\prime}_{j_{0}},\alpha^{\prime})=1+(y^{\prime}_{j_{0}})^{r_{j_{0}}}(1+O(y^{\prime}_{j_{0}})). Soit la projection canonique π ′: ( ρ ′, y ′, α ′) ∈ V ′ ↦ ( ρ ′, y ′ ^ j 0 + 1, α ′) ∈ V 1 ′ \pi^{\prime}:(\rho^{\prime},y^{\prime},\alpha^{\prime})\in V^{\prime}\mapsto(\rho^{\prime},\widehat{y^{\prime}}^{j_{0}+1},\alpha^{\prime})\in V^{\prime}_{1}, le champ Y 1 ′ = π ∗ ′ ​ Y ′ {Y}^{\prime}_{1}=\pi^{\prime}_{*}{Y}^{\prime} a pour intégrales premières les fonctions L j ′ L^{\prime}_{j} pour j ∉ { j 0, j 0 + 1 } j\not\in\{j_{0},j_{0}+1\} et la fonction

 | L j 0 + 1 ′ ​ ( ρ ′, f, y j 0 + 2 ′, α ′) − L j 0 + 1 ′ ​ ( ρ ′, 1, 0, α ′) = a ⁡ ( ρ ′, α ′) ​ ( y j 0 ′) r j 0 ​ ( 1 + O ⁡ ( y j 0 ′)) − y j 0 + 2 ′ L^{\prime}_{j_{0}+1}(\rho^{\prime},f,y^{\prime}_{j_{0}+2},\alpha^{\prime})-L^{\prime}_{j_{0}+1}(\rho^{\prime},1,0,\alpha^{\prime})=a(\rho^{\prime},\alpha^{\prime})(y^{\prime}_{j_{0}})^{r_{j_{0}}}(1+O(y^{\prime}_{j_{0}}))-y^{\prime}_{j_{0}+2} |  |

avec a ⁡ ( 0) > 0 a(0)>0. D’après le diagramme ( ∗) (*), on a ( T k ′) ∗ − 1 ​ χ = ( ρ ′) s k ​ Y ′ (T^{\prime}_{k})^{-1}_{*}\chi=(\rho^{\prime})^{s_{k}}{Y}^{\prime} et en utilisant l’action de χ \chi sur x 1 x_{1}, on obtient Y ′ ​ y 1 ′ = ∏ j = 1 k y j ′ {Y}^{\prime}y^{\prime}_{1}=\prod_{j=1}^{k}y^{\prime}_{j}. Donc si k − k ′ = 1 k-k^{\prime}=1, le champ Y 1 ′ {Y}^{\prime}_{1} est équivalent à un élément de Ξ ​ H k ′ \Xi{H}_{k^{\prime}} par la réduction du paragraphe 1. Supposons k − k ′ > 1 k-k^{\prime}>1 et réindéxons les coordonnées y j ′ y^{\prime}_{j} et les intégrales premières L j ′ L^{\prime}_{j}. Il existe j 1 ≥ j 0 j_{1}\geq j_{0} tel que y j 1, 0 ′ = 0 y^{\prime}_{j_{1},0}=0 et y j 1 + 1, 0 ′ > 0 y^{\prime}_{j_{1}+1,0}>0. Soit le morphisme

 | L 1 ′: ( ρ ′, y ′, α ′) ∈ V 1 ′ ↦ ( ρ ′, y ′ ^ j 1 + 1, α ′, L j 1 ′) = ( ρ ′, y ′ ^ j 1 + 1, α ′, u j 1 ′) ∈ V 2 ′ {L}^{\prime}_{1}:(\rho^{\prime},y^{\prime},\alpha^{\prime})\in V^{\prime}_{1}\mapsto(\rho^{\prime},\widehat{y^{\prime}}^{j_{1}+1},\alpha^{\prime},L^{\prime}_{j_{1}})=(\rho^{\prime},\widehat{y^{\prime}}^{j_{1}+1},\alpha^{\prime},u^{\prime}_{j_{1}})\in V^{\prime}_{2} |  |

L’équation L j 1 ′ = u j 1 ′ L^{\prime}_{j_{1}}=u^{\prime}_{j_{1}} est un graphe: y j 1 + 1 ′ = f 1 ​ ( ρ ′, y j 1 ′, α ′, u j 1 ′) y^{\prime}_{j_{1}+1}=f_{1}(\rho^{\prime},y^{\prime}_{j_{1}},\alpha^{\prime},u^{\prime}_{j_{1}}). Par la méthode ci-dessus, on montre que le morphisme L 1 ′ {L}^{\prime}_{1} est un difféomorphisme sur son image et que le champ Y 2 ′ = ( L 1 ′) ∗ ​ Y 1 ′ {Y}^{\prime}_{2}=({L}^{\prime}_{1})_{*}{Y}^{\prime}_{1} admet pour intégrales premières la coordonnée u j 1 ′ u^{\prime}_{j_{1}}, les fonctions L j ′ L^{\prime}_{j} pour j ∉ { j 1, j 1 + 1 } j\not\in\{j_{1},j_{1}+1\} et la fonction L j 1 + 1 ′ ​ ( ρ ′, f 1, y j 1 + 2 ′, α ′) − L j 1 + 1 ′ ​ ( ρ ′, y j 1 + 1, 0 ′, 0, α ′) = a 1 ​ ( ρ ′, α ′, u j 1 ′) ​ ( y j 1 ′) r j 1 ​ ( 1 + O ⁡ ( y j 1 ′)) − y j 1 + 2 ′ L^{\prime}_{j_{1}+1}(\rho^{\prime},f_{1},y^{\prime}_{j_{1}+2},\alpha^{\prime})-L^{\prime}_{j_{1}+1}(\rho^{\prime},y^{\prime}_{j_{1}+1,0},0,\alpha^{\prime})=a_{1}(\rho^{\prime},\alpha^{\prime},u^{\prime}_{j_{1}})(y^{\prime}_{j_{1}})^{r_{j_{1}}}(1+O(y^{\prime}_{j_{1}}))-y^{\prime}_{j_{1}+2}. Par l’hypothèse de récurrence, il est équivalent à un élément de Ξ ​ H k ′ \Xi{H}_{k^{\prime}}.

Supposons y 1, 0 > 0 y_{1,0}>0 et soit j 0 j_{0} le plus petit des entiers j j tels que y j, 0 > 0 y_{j,0}>0 et y j + 1, 0 = 0 y_{j+1,0}=0. On trivialise le champ Y {Y} dans la coordonnée ρ \rho en utilisant l’intégrale première G j 0 G_{j_{0}} et le morphisme E k ′, i E_{k^{\prime},i} associé. Puis, on trivialise le champ Y ′ {Y}^{\prime} dans les coordonnées y 1 ′, …, y j 0 ′ y^{\prime}_{1},\ldots,y^{\prime}_{j_{0}} en utilisant les intégrales premières L 1 ′, …, L j 0 ′ L^{\prime}_{1},\ldots,L^{\prime}_{j_{0}} par l’intérmédiaire du morphisme

 | L 0 ′ ​ ( ρ ′, y ′, α ′) = ( ρ ′, y j 0 + 1 ′, …, y k ′, L 1 ′, …, L j 0 − 1 ′, α ′) {L}^{\prime}_{0}(\rho^{\prime},y^{\prime},\alpha^{\prime})=(\rho^{\prime},y^{\prime}_{j_{0}+1},\ldots,y^{\prime}_{k},L^{\prime}_{1},\ldots,L^{\prime}_{j_{0}-1},\alpha^{\prime}) |  |

le système d’équations

 | L 1 ′ = u 1 ′, …, L j 0 − 1 ′ = u j 0 − 1 ′, L j 0 ′ = 1 L^{\prime}_{1}=u^{\prime}_{1},\ldots,\quad L^{\prime}_{j_{0}-1}=u^{\prime}_{j_{0}-1},\quad L^{\prime}_{j_{0}}=1 |  |

dont les inconnues sont y 1 ′, …, y j 0 ′ y^{\prime}_{1},\ldots,y^{\prime}_{j_{0}}, s’inverse ligne par ligne dans l’ algèbre Q ​ R ​ H p ′, q ′ QR{H}^{p^{\prime},q^{\prime}}. Le champ Y 0 ′ = ( L 0 ′) ∗ ​ Y ′ {Y}^{\prime}_{0}=({L}^{\prime}_{0})_{*}{Y}^{\prime} admet pour intégrales premières la coordonnée u ′ u^{\prime} et les fonctions L j 0 + 1 ′, …, L k ′ L^{\prime}_{j_{0}+1},\ldots,L^{\prime}_{k}. D’après l’action de χ \chi sur x j 0 + 1 x_{j_{0}+1}, on a

 | Y ′ y j 0 + 1 ′ = r 1, j 0 ( y 1 ′) r 1 × ⋯ × ( y j 0 ′) r j 0 ∏ j > j 0 y j ′ ( 1 + O ( ρ ′)) {Y}^{\prime}y^{\prime}_{j_{0}+1}=r_{1,j_{0}}(y^{\prime}_{1})^{r_{1}}\times\cdots\times(y^{\prime}_{j_{0}})^{r_{j_{0}}}\prod_{j>j_{0}}y^{\prime}_{j}(1+O(\rho^{\prime})) |  |

et on conclut en utilisant la première partie de la preuve.∎

On note ( π k, N k) (\pi_{k},{N}_{k}) cette première étape de la désingularisation de χ \chi de diviseur exceptionnel D k ¯ \overline{{D}_{k}}. Soit f ∈ Q ​ R ​ H p, q f\in QR{H}^{p,q} et f ~ \widetilde{f} son relevé par π k \pi_{k}. Si a ∈ D k a\in{D}_{k}, f ~ a \widetilde{f}_{a} est induit par un élément de Q ​ R ​ H p ′ ​ ( 0), q ′ ​ ( 0) QR{H}^{p^{\prime}(0),q^{\prime}(0)} et si a ∈ ∂ D k a\in\partial{D}_{k} tel que χ ~ a \widetilde{\chi}_{a} soit de dimension de non trivialité k ′ − 1 k^{\prime}-1, f ~ a \widetilde{f}_{a} est induit par un élément de Q ​ R ​ H p ′ ​ ( k ′), q ′ ​ ( k ′) QR{H}^{p^{\prime}(k^{\prime}),q^{\prime}(k^{\prime})}.

B. L’hypothèse ( H ​ λ) (H\lambda) et le lemme de récurrence 1.

Considérons une dérivation χ ∈ Ξ ​ H k ​ [Q ​ R ​ H k, q] \chi\in\Xi{H}_{k}[QR{H}^{k,q}] réalisée sur un voisinage U U de 0. Soient ( g j) (g_{j}) ses ( k − 1) (k-1) intégrales premières non triviales. Son morphisme intégral est π χ ​ ( x, α) = ( α, ( g j ​ ( x, α))) = ( α, λ) \pi_{\chi}(x,\alpha)=(\alpha,(g_{j}(x,\alpha)))=(\alpha,\lambda). D’après les propositions IVA1 et IVA2, l’orbite γ = { α = 0, g 1 = ⋯ = g k − 1 = 0 } \gamma=\{\alpha=0,g_{1}=\cdots=g_{k-1}=0\} est principale dans U U. Soit W W une transversale à γ \gamma, analytique de coordonnées ( α, λ) (\alpha,\lambda). On définit de la même façon que dans la partie IIIA, les classes C λ k {C}^{k}_{\lambda} et C λ, l ​ o ​ c k {C}^{k}_{\lambda,loc} des germes f ∈ Q ​ R ​ H k, q f\in QR{H}^{k,q} qui satisfont globalement ou localement à l’hypothèse ( H ​ λ) (H\lambda).

###### Théorème IVB1

La classe C λ, l ​ o ​ c k {C}^{k}_{\lambda,loc} est localement χ \chi -finie.

La preuve est basée sur les théorèmes principaux II1 et IIIA2, et sur un argument de récurrence sur la dimension de non trivialité de la dérivation d’Hilbert. Définissons d’abord les anneaux des intégrales premières qui apparaîtront dans cette partie

###### Définition IVB1

Soit t = ( t 1, …, t n) t=(t_{1},\ldots,t_{n}) des coordonnées sur ℝ n \mathbb{R}^{n}. Notons A 0 n ​ ( t) = ℝ ⁡ { t } {A}_{0}^{n}(t)=\mathbb{R}\{t\}. Soit V 0 V_{0} un semi-analytique de l’anneau A 0 n ​ ( t) {A}_{0}^{n}(t) qui est ouvert et qui adhère à 0. On note A 1 n ​ ( V 0) {A}_{1}^{n}(V_{0}) l’anneau des germes analytiques et bornés sur (un germe en 0 de) V 0 V_{0}. Supposons défini l’anneau A i n (.) {A}_{i}^{n}(.) et soit V i V_{i} un semi-analytique de cet anneau qui est ouvert et qui adhère à 0. On note A i + 1 n ​ ( V i) {A}_{i+1}^{n}(V_{i}) l’anneau des germes analytiques et bornés sur (un germe en 0 de) V i V_{i}.

L’argument de récurrence.

Soit x = ( x 1, …, x k) x=(x_{1},\ldots,x_{k}), ρ = ( ρ 1, …, ρ p) \rho=(\rho_{1},\ldots,\rho_{p}) avec p > 0 p>0 et α = ( μ, ν, ν ′) \alpha=(\mu,\nu,\nu^{\prime}) des coordonnées sur ℝ q 1 × ℝ q 2 × ℝ q 3 \mathbb{R}^{q_{1}}\times\mathbb{R}^{q_{2}}\times\mathbb{R}^{q_{3}}. Soit q = ( q 1, q 2 + q 3) q=(q_{1},q_{2}+q_{3}) et soit une dérivation χ ∈ Ξ ​ H k ​ [Q ​ R ​ H p + k, q] \chi\in\Xi{H}_{k}[QR{H}^{p+k,q}] réalisée sur un ouvert U U et d’intégrales premières non-triviales g j = x j r j ​ ( 1 + D j) − x j + 1 g_{j}=x_{j}^{r_{j}}(1+D_{j})-x_{j+1}. Toujours d’après les propositions IVA1 et IVA2, la dérivation χ \chi admet une orbite principale dans U U incluse dans le bord de U U: γ = { ( ρ, α, ( g j) j) = 0 } \gamma=\{(\rho,\alpha,(g_{j})_{j})=0\}. Son morphisme intégral est π χ: ( x, ρ, α) ∈ U ↦ ( ρ, α, λ) = ( ρ, α, ( g j ​ ( x, ρ, α)) j) ∈ W \pi_{\chi}:(x,\rho,\alpha)\in U\mapsto(\rho,\alpha,\lambda)=(\rho,\alpha,(g_{j}(x,\rho,\alpha))_{j})\in W où W W est isomorphe à une semi-transversale à γ \gamma.

( t k) (t_{k}) Soit V V un semi analytique d’un anneau A i q 2 (.) {A}^{q_{2}}_{i}(.) qui est ouvert et qui adhère à 0 et soit

 | i m: ν ∈ V ↦ ( ρ ( ν), μ ( ν), ν, ν ′ ( ν), λ ( ν))) ∈ W im:\nu\in V\mapsto(\rho(\nu),\mu(\nu),\nu,\nu^{\prime}(\nu),\lambda(\nu)))\in W |  |

une immersion dont les composantes appartiennent à l’anneau A i + 1 q 2 ​ ( V) {A}_{i+1}^{q_{2}}(V).

Soit W 0 = i ​ m ​ ( V) ⊂ W W_{0}=im(V)\subset W et soit U 0 = π χ − 1 ​ ( W 0) U_{0}=\pi_{\chi}^{-1}(W_{0}). Notons U 0, m U_{0,m} et π χ, m \pi_{\chi,m} les germes de U 0 U_{0} et π χ \pi_{\chi} en tout point m ∈ γ m\in\gamma. Soit les morphismes π χ ∗: S ​ B p, | q | + k − 1 → S ​ B p + k, | q | \pi_{\chi}^{*}:SB^{p,|q|+k-1}\to SB^{p+k,|q|} et π χ, m ∗: S ​ B p, | q | + k − 1 → S ​ B p, | q | + k \pi_{\chi,m}^{*}:SB^{p,|q|+k-1}\to SB^{p,|q|+k}

###### Lemme IVB1 (lemme de récurrence 1)

Soit f ∈ Q ​ R ​ H k + p, q f\in QR{H}^{k+p,q}, on suppose que

Alors f f est localement χ \chi -finie sur U 0 U_{0}.

Remarque. Ce lemme est encore vrai dans des situations plus générales pour le sous-ensemble W 0 W_{0}. On garde cette formulation simple pour plus de cohérence avec le deuxième lemme de récurrence et parce qu’elle est suffisante pour la preuve du théorème.

Preuve du lemme. Par récurrence sur k k. Le cas k = 1 k=1 est une conséquence de la première partie de la preuve avec χ ~ = χ \widetilde{\chi}=\chi. Soit k > 1 k>1 et ( π k, N k) (\pi_{k},{N}_{k}) le premier éclatement de χ \chi donné par les propositions IVA1 et IVA2, et soit D ¯ k \overline{{D}}_{k} son diviseur exceptionnel. Soient χ ~ \widetilde{\chi} et f ~ \widetilde{f} les relevés de χ \chi et f f par π k \pi_{k}. Soit γ 0 = π k − 1 ​ ( γ) \gamma_{0}=\pi_{k}^{-1}(\gamma). D’après la proposition IVA1, la semi-transversale W W est isomorphe à une semi-transversale à γ 0 \gamma_{0} de même coordonnée. Soit U ~ 0 = π k − 1 ​ ( U 0) \widetilde{U}_{0}=\pi_{k}^{-1}(U_{0}), c’est aussi le saturé de W 0 W_{0} par le flot de χ ~ \widetilde{\chi} dans N k {N}_{k}. Il s’agit de montrer que le faisceau I χ ~, f ~ ​ [D ¯ k ∩ U ~ ¯ 0] {I}_{\widetilde{\chi},\widetilde{f}}[\overline{{D}}_{k}\cap\overline{\widetilde{U}}_{0}] est localement χ ~ \widetilde{\chi} -fini.

(a) Au dessus de D k {D}_{k}.

Le désingularisé de χ \chi est

 | χ ~ = ρ 0 ​ ∂ ∂ ρ 0 − ∑ j = 1 k − 1 r 1, j ​ u j ​ ∂ ∂ u j \widetilde{\chi}=\rho_{0}\frac{\partial}{\partial\rho_{0}}-\sum_{j=1}^{k-1}r_{1,j}u_{j}\frac{\partial}{\partial u_{j}} |  |

soit a 0 a_{0} son unique singularité sur D k {D}_{k}. D’après l’hypothèse ( i ​ i k) (ii_{k}), il existe une fonction g g définie au dessus de tout relativement compact de D k {D}_{k} telle que pour tout a ∈ D k a\in{D}_{k}, le germe g a g_{a} est induit par un élément de Q R H c ​ v ​ g 1,. ( ρ 0,.) QR{H}^{1,.}_{cvg}(\rho_{0},.) sur un semi-analytique de Q R H c ​ v ​ g p,. ( ρ,.) QR{H}_{cvg}^{p,.}(\rho,.) et

 | f ~ a − g a ∈ ( ρ N 1) \widetilde{f}_{a}-g_{a}\in(\rho^{N_{1}}) |  | 1 |

Soit X ⁡ ( ρ, μ) X(\rho,\mu) les fonctions élémentaires de l’algèbre Q R H p ( ρ,.) QR{H}^{p}(\rho,.) et soit l’immersion c ⁡ ( ρ 0, ρ, α, u) = ( ρ 0, α, X, u) c(\rho_{0},\rho,\alpha,u)=(\rho_{0},\alpha,X,u). Soit G ∈ Q R H c ​ v ​ g 1,. ( ρ 0,.) G\in QR{H}^{1,.}_{cvg}(\rho_{0},.) tel que g a 0 = c ∗ ​ ( G) g_{a_{0}}=c^{*}(G) et soit m ​ a + ​ ( G) ma^{+}(G) sa multiplicité algébrique positive relativement à χ ~ a 0 \widetilde{\chi}_{a_{0}} le long de γ 0 \gamma_{0}. Soit U 0 = c ⁡ ( U ~ 0, a 0) {U}_{0}=c(\widetilde{U}_{0,a_{0}}), Le point clé est que la multiplicité algébrique restreinte m a + ( G | U 0) ≤ m a + ( G) ma^{+}(G_{|{U}_{0}})\leq ma^{+}(G) est indépendante des représentants convergents de f f et D j D_{j} dans les quotients S ​ B / ( ρ N 1) SB/(\rho^{N_{1}}). En effet, d’après la proposition IVA1, on a ρ 0 s k ​ χ ~ ∼ ( π k − 1) ∗ ​ ( χ) \rho_{0}^{s_{k}}\widetilde{\chi}\sim(\pi_{k}^{-1})_{*}(\chi), par conséquent les fibres différentielles le long de γ \gamma et γ 0 \gamma_{0} sont isomorphes et d’après l’hypothèse ( i k) (i_{k}), les fibres I χ ~ a 0, f ~ a 0, m 0 | U ~ 0, m 0 {I}_{\widetilde{\chi}_{a_{0}},\widetilde{f}_{a_{0}},m_{0}|\widetilde{U}_{0,m_{0}}} contiennent l’idéal π χ ~ a 0 | U ~ 0, m 0 ∗ ​ ( ρ N 0) \pi_{\widetilde{\chi}_{a_{0}}|\widetilde{U}_{0,m_{0}}}^{*}(\rho^{N_{0}}) pour tout m 0 ∈ γ 0 m_{0}\in\gamma_{0}. D’après (1), il en est de même des fibres de g a 0 g_{a_{0}} le long de γ 0 \gamma_{0} restreintes à U ~ 0, a 0 \widetilde{U}_{0,a_{0}}. Or le germe g a 0 g_{a_{0}} et les intégrales premières de χ ~ \widetilde{\chi} sont des éléments d’un anneau restriction analytique; le lemme d’isomorphie I4 s’applique: les fibres différentielles de g a 0 g_{a_{0}} le long de γ 0 \gamma_{0} sont isomorphes et il en est de même de celles de f ~ a 0 \widetilde{f}_{a_{0}} restreintes à U ~ 0, a 0 \widetilde{U}_{0,a_{0}}.

Il s’ensuit deux choses: d’une part, f ~ a 0 | U ~ 0, a 0 \widetilde{f}_{a_{0}|\widetilde{U}_{0,a_{0}}} possède un idéal χ ~ a 0 \widetilde{\chi}_{a_{0}} -transverse le long de γ 0 \gamma_{0}, qui coincide avec celui de g a 0 | U ~ 0, a 0 g_{a_{0}|\widetilde{U}_{0,a_{0}}} et qui contient l’idéal ( ρ N 0) (\rho^{N_{0}}) (Il en est donc de même pour f | U 0 f_{|U_{0}} le long de γ \gamma, par l’isomorphisme π k \pi_{k}). D’autre part, la relation (1) et le lemme IIIA5 montrent que f ~ a 0 | U ~ 0, a 0 \widetilde{f}_{a_{0}|\widetilde{U}_{0,a_{0}}} est presque quasi-convergente, et possède donc une multiplicité algébrique restreinte, qui conicide avec celle de g a 0 | U ~ 0, a 0 g_{a_{0}|\widetilde{U}_{0,a_{0}}} et qui ne dépend donc pas du choix de g g. Notons simplement m ​ a + ma^{+} cette multiplicité.

Soit J G J_{G} l’idéal χ ~ a 0 \widetilde{\chi}_{a_{0}} -transverse de G G le long de c ⁡ ( γ 0) c(\gamma_{0}) et W 0 = c ⁡ ( W 0) {W}_{0}=c(W_{0}). Le théorème principal IIIA1 s’applique à l’action de χ ~ a 0 \widetilde{\chi}_{a_{0}} sur G G par restriction à U 0 {U}_{0}

 | I χ ~ a 0, G | U 0 ⊃ ( ρ 0 m ​ a + + 1) ​ π χ ~ a 0 | U 0 ∗ ​ ( J G | W 0) I_{\widetilde{\chi}_{a_{0}},G|{U}_{0}}\supset(\rho_{0}^{ma^{+}+1})\pi_{\widetilde{\chi}_{a_{0}}|{U}_{0}}^{*}(J_{G|{W}_{0}}) |  |

et en appliquant le morphisme c ∗ c^{*}, on obtient

 | I χ ~ a 0, g a 0 | U ~ 0, a 0 ⊃ ( ρ 0 m ​ a + + 1) ​ π χ ~ a 0 | U ~ 0, a 0 ∗ ​ ( J g a 0 | W 0) I_{\widetilde{\chi}_{a_{0}},g_{a_{0}}|\widetilde{U}_{0,a_{0}}}\supset(\rho_{0}^{ma^{+}+1})\pi_{\widetilde{\chi}_{a_{0}}|\widetilde{U}_{0,a_{0}}}^{*}(J_{g_{a_{0}}|W_{0}}) |  | 2 |

Un plongement de f f et χ \chi est alors nécessaire. Soit f ′ f^{\prime} et D j ′ D^{\prime}_{j} des représentants convergents de f f et D j D_{j} dans les quotients S ​ B / ( ρ N 1) SB/(\rho^{N_{1}}). Soit X ⁡ ( x, μ) X(x,\mu) les fonctions élémentaires de l’algèbre Q R H k,. ( x,.) QR{H}^{k,.}(x,.) et soient f ​ " = 𝕛 X m ​ a + + 3 ​ ( f − f ′) f"={\mathbb{j}}_{X}^{ma^{+}+3}(f-f^{\prime}) et D ​ " j = 𝕛 X m ​ a + + 3 ​ ( D j − D j ′) D"_{j}={\mathbb{j}}_{X}^{ma^{+}+3}(D_{j}-D^{\prime}_{j}). Les germes f ​ " f" et D ​ " j D"_{j} appartiennent à l’idéal ( ρ N 1) (\rho^{N_{1}}) et sont induits par des éléments de l’algèbre Q R H c ​ v ​ g k,. ( x,.) QR{H}^{k,.}_{cvg}(x,.) sur un semi-analytique de Q R H p,. ( ρ,.) QR{H}^{p,.}(\rho,.). En effet, soit ( a m ​ ( ρ, α)) (a_{m}(\rho,\alpha)) la famille des coefficients de f ​ " f" et des D ​ " j D"_{j} dans leur développement en série de X X. Notons v = ( a m − a m ​ ( 0)) v=(a_{m}-a_{m}(0)) ces nouvelles coordonnées, les fonctions v ⁡ ( ν) v(\nu) appartiennent aussi à l’anneau A i + 1 q 2 ​ ( V) {A}^{q_{2}}_{i+1}(V). Remplaçons les coordonnées α \alpha par α ′ = ( α, v) \alpha^{\prime}=(\alpha,v) et gardons les mêmes notations pour i ​ m im, W 0 W_{0}, U 0 U_{0} ….

Ainsi, quitte à remplacer f ′ f^{\prime} par f ′ + f ​ " f^{\prime}+f" et D j ′ D^{\prime}_{j} par D j ′ + D ​ " j D^{\prime}_{j}+D"_{j}, on peut supposer que f f et D j D_{j} admettent des représentants convergents dans les quotients S ​ B / ( ρ N 1) ​ M x m ​ a + + 3 SB/(\rho^{N_{1}}){M}_{x}^{ma^{+}+3}. La relation (1) est donc remplacée par

 | f ~ a − g a ∈ ( ρ 0 m ​ a + + 2 ​ ρ N 1) \widetilde{f}_{a}-g_{a}\in(\rho_{0}^{ma^{+}+2}\rho^{N_{1}}) |  | 3 |

et la relation (2) est encore satisfaite par l’invariance de la multiplicité algébrique restreinte m ​ a + ma^{+}.

Soit D 0 = D k ∩ U ~ ¯ 0 D_{0}={D}_{k}\cap\overline{\widetilde{U}}_{0}. Montrons que pour tout a ∈ D 0 a\in D_{0}, le germe f ~ a \widetilde{f}_{a} est χ ~ a \widetilde{\chi}_{a} -équivalent à g a g_{a} sur U ~ 0, a \widetilde{U}_{0,a}. Le théorème de finitude IB1 permettera de conclure. Soit γ 1 \gamma_{1} une trajectoire incluse dans D 0 D_{0}. Etudions le faisceau I χ ~, f ~ ( { a 0 } ∪ γ 1) | U 0 ~ {I}_{\widetilde{\chi},\widetilde{f}}(\{a_{0}\}\cup\gamma_{1})_{|\widetilde{U_{0}}}. En a 0 a_{0}, on a J g a 0 | W 0 ⊃ ( ρ N 0) J_{g_{a_{0}}|W_{0}}\supset(\rho^{N_{0}}) et d’après (2)

 | I χ ~ a 0, g a 0 | U ~ 0, a 0 ⊃ ( ρ 0 m ​ a + + 1 ​ ρ N 0) I_{\widetilde{\chi}_{a_{0}},g_{a_{0}}|\widetilde{U}_{0,a_{0}}}\supset(\rho_{0}^{ma^{+}+1}\rho^{N_{0}}) |  | 4 |

donc d’après (3), on a ( f ~ a 0 − g a 0) | U ~ 0, a 0 ∈ M I χ ~ a 0, g a 0 | U ~ 0, a 0 (\widetilde{f}_{a_{0}}-g_{a_{0}})_{|\widetilde{U}_{0,a_{0}}}\in{M}I_{\widetilde{\chi}_{a_{0}},g_{a_{0}}|\widetilde{U}_{0,a_{0}}}. Par conséquent, f ~ a 0 \widetilde{f}_{a_{0}} est χ ~ a 0 \widetilde{\chi}_{a_{0}} -finie sur U ~ 0, a 0 \widetilde{U}_{0,a_{0}}.

Soit b ∈ γ 1 b\in\gamma_{1} suffisament proche de a 0 a_{0}. D’après (4) et le lemme de cohérence IB3, on a

 | I χ ~, g, b | U ~ 0, b ⊃ ( ρ 0 m ​ a + + 1 ​ ρ N 0) {I}_{\widetilde{\chi},g,b|\widetilde{U}_{0,b}}\supset(\rho_{0}^{ma^{+}+1}\rho^{N_{0}}) |  |

et donc d’après (3), f ~ b \widetilde{f}_{b} est χ ~ b \widetilde{\chi}_{b} -finie sur U ~ 0, b \widetilde{U}_{0,b}. Soit a a un point quelconque de γ 1 \gamma_{1}, d’après le lemme d’isomorphie IB4, les fibres I χ ~, g, b | U ~ 0, b {I}_{\widetilde{\chi},g,b|\widetilde{U}_{0,b}} et I χ ~, g, a | U ~ 0, a {I}_{\widetilde{\chi},g,a|\widetilde{U}_{0,a}} sont isomorphes par le flot de χ ~ \widetilde{\chi} qui préserve l’idéal ( ρ 0 m ​ a + + 1 ​ ρ N 0) (\rho_{0}^{ma^{+}+1}\rho^{N_{0}}). Par conséquent, f ~ a \widetilde{f}_{a} est χ ~ a \widetilde{\chi}_{a} -finie sur U ~ 0, a \widetilde{U}_{0,a} et on a

 | I χ ~, f ~, a | U ~ 0, a ⊃ ( ρ 0 m ​ a + + 1 ​ ρ N 0) {I}_{\widetilde{\chi},\widetilde{f},a|\widetilde{U}_{0,a}}\supset(\rho_{0}^{ma^{+}+1}\rho^{N_{0}}) |  | 5 |

(b) Sur le bord de D k {D}_{k}.

Soit a 1 = γ ¯ 1 ∩ ∂ D k a_{1}=\overline{\gamma}_{1}\cap\partial{D}_{k}. Soit χ ~ a 1 \widetilde{\chi}_{a_{1}} le désingularisé de χ \chi en a 1 a_{1}. D’après la proposition IVA2, c’est une dérivation d’Hilbert de dimension de non trivialité k ′ − 1 < k − 1 k^{\prime}-1<k-1. Montrons d’abord la propriété ( t k ′) (t_{k^{\prime}}). Dans la réduction de χ \chi au voisinage de a 1 a_{1}, on trivialise dans la coordonnée ρ 0 \rho_{0} en posant par exemple ρ 0 ′ = ρ 0 r 1, 1 ​ | u 1 | = | λ 1 | \rho^{\prime}_{0}=\rho_{0}^{r_{1,1}}|u_{1}|=|\lambda_{1}| si u 1 ​ ( a 1) ≠ 0 u_{1}(a_{1})\neq 0. Les intégrales premières non triviales λ j ′ \lambda^{\prime}_{j} au voisinage de a 1 a_{1} sont des fonctions régulières des rapports

 | u j ′ = λ j ( ρ 0 ′) r 1, j u^{\prime}_{j}=\frac{\lambda_{j}}{(\rho^{\prime}_{0})^{r_{1,j}}} |  |

des intégrales premières non triviales en a 0 a_{0}. Notons w w ces nouvelles coordonnées germifiées autour de γ 1 \gamma_{1} et V ′ V^{\prime} le semi-analytique de A i + 1 q 2 ​ ( V) {A}^{q_{2}}_{i+1}(V) correspondant. On obtient ainsi la propriété ( t k ′) (t_{k^{\prime}}).

Montrons que f ~ a 1 \widetilde{f}_{a_{1}} et χ ~ a 1 \widetilde{\chi}_{a_{1}} satisfont aux hypothèses ( i k ′) (i_{k^{\prime}}) et ( i ​ i k ′) (ii_{k^{\prime}}) du lemme. Soit a ∈ γ 1 a\in\gamma_{1} suffisament proche de a 1 a_{1}. D’après la proposition IVA2, les germes en a ∈ γ 1 a\in\gamma_{1} des champs χ ~ \widetilde{\chi} et χ ~ a 1 \widetilde{\chi}_{a_{1}} sont équivalents. Donc, d’après (5) et l’expression de π k \pi_{k} en a 1 a_{1}, on a

 | I χ ~ a 1, f ~ a 1, a | U ~ 0, a ⊃ ( ( ρ 0 ′) m ​ a + + 1 ​ ρ N 0) {I}_{\widetilde{\chi}_{a_{1}},\widetilde{f}_{a_{1}},a|\widetilde{U}_{0,a}}\supset((\rho^{\prime}_{0})^{ma^{+}+1}\rho^{N_{0}}) |  |

ceci prouve l’hypothèse ( i k ′) (i_{k^{\prime}}) avec N 0 ′ = ( m ​ a + + 1, N 0) N^{\prime}_{0}=(ma^{+}+1,N_{0}). Soient g j ′ = ( y ′) j r j ​ ( 1 + D j ′) − y j + 1 ′ g^{\prime}_{j}=(y^{\prime})_{j}^{r_{j}}(1+D^{\prime}_{j})-y^{\prime}_{j+1} les intégrales premières non triviales de χ ~ a 1 \widetilde{\chi}_{a_{1}}. Les germes f f et D j D_{j} admettent des représentants convergents dans les quotients S ​ B / ( ρ N 1) ​ M x m ​ a + + 3 SB/(\rho^{N_{1}}){M}_{x}^{ma^{+}+3}. Donc, d’après l’expression de π k \pi_{k}, les germes f ~ a 1 \widetilde{f}_{a_{1}} et D j ′ D^{\prime}_{j} admettent des représentants convergents dans les quotients S ​ B / ( ( ρ 0 ′) m ​ a + + 2 ​ ρ N 1) SB/((\rho^{\prime}_{0})^{ma^{+}+2}\rho^{N_{1}}). Ceci prouve l’hypothèse ( i ​ i k ′) (ii_{k^{\prime}}) avec N 1 ′ = ( m ​ a + + 2, N 1) N^{\prime}_{1}=(ma^{+}+2,N_{1}).∎

Preuve du théorème.

Soit f ∈ C λ, l ​ o ​ c k f\in{C}^{k}_{\lambda,loc} et soit W 0 ⊂ W W_{0}\subset W un semi-analytique de ℝ ​ { α, λ } \mathbb{R}\{\alpha,\lambda\} et N 0 N_{0} tels que

 | J χ, f, γ | W 0 ⊃ M λ | W 0 N 0 J_{\chi,f,\gamma|W_{0}}\supset{M}_{\lambda|W_{0}}^{N_{0}} |  | 6 |

En utilisant la stratification analytique de W 0 W_{0}, on peut supposer que c’est un graphe analytique, d’où la propriété ( t k) (t_{k}). Notons que la preuve ci-dessous s’applique encore à des sous-ensembles W 0 W_{0} plus généraux.

Soit U 0 = π χ − 1 ​ ( W 0) U_{0}=\pi_{\chi}^{-1}(W_{0}). La preuve reprend certains arguments de la preuve du lemme de récurrence IVB1 dont on reprend les notations. Soit ( π k, N k) (\pi_{k},{N}_{k}) le premier éclatement de χ \chi de diviseur exceptionnel D k ¯ \overline{{D}_{k}} et soit U ~ 0 = π k − 1 ​ ( U 0) \widetilde{U}_{0}=\pi_{k}^{-1}(U_{0}).

(a) Au dessus de D k {D}_{k}. Soit

 | χ ~ = ρ ​ ∂ ∂ ρ − ∑ j = 1 k − 1 r 1, j ​ u j ​ ∂ ∂ u j \widetilde{\chi}=\rho\frac{\partial}{\partial\rho}-\sum_{j=1}^{k-1}r_{1,j}u_{j}\frac{\partial}{\partial u_{j}} |  |

le désingularisé de χ \chi et f ~ \widetilde{f} le relevé de f f par π k \pi_{k}. Soit γ 0 = π k − 1 ​ ( γ) \gamma_{0}=\pi_{k}^{-1}(\gamma) et a 0 a_{0} l’unique singularité de χ ~ \widetilde{\chi} sur D k {D}_{k}. La relation (6) est équivalente à

 | J χ ~ a 0, f ~ a 0, γ 0 | W 0 ⊃ M λ | W 0 N 0 J_{\widetilde{\chi}_{a_{0}},\widetilde{f}_{a_{0}},\gamma_{0}|W_{0}}\supset{M}_{\lambda|W_{0}}^{N_{0}} |  | 7 |

le germe f ~ a 0 \widetilde{f}_{a_{0}} est donc presque quasi-convergent sur U ~ 0, a 0 \widetilde{U}_{0,a_{0}} et possède une multiplicité algébrique restreinte m ​ a + ma^{+}. D’après le lemme IIIA11, il est χ ~ a 0 \widetilde{\chi}_{a_{0}} -fini sur U ~ 0, a 0 \widetilde{U}_{0,a_{0}} et

 | I χ ~ a 0, f ~ a 0 | U ~ 0, a 0 ⊃ ( ρ m ​ a + + 1) ​ π χ ~ a 0 | U ~ 0, a 0 ∗ ​ ( J χ ~ a 0, f ~ a 0, γ 0 | W 0) I_{\widetilde{\chi}_{a_{0}},\widetilde{f}_{a_{0}}|\widetilde{U}_{0,a_{0}}}\supset(\rho^{ma^{+}+1})\pi_{\widetilde{\chi}_{a_{0}}|\widetilde{U}_{0,a_{0}}}^{*}(J_{\widetilde{\chi}_{a_{0}},\widetilde{f}_{a_{0}},\gamma_{0}|W_{0}}) |  |

Donc d’après (7), on a pour tout j j

 | I χ ~ a 0, f ~ a 0 | U ~ 0, a 0 ⊃ ( ρ m ​ a + + 1 ( ρ r 1, j u j) N 0) | U ~ 0, a 0 I_{\widetilde{\chi}_{a_{0}},\widetilde{f}_{a_{0}}|\widetilde{U}_{0,a_{0}}}\supset(\rho^{ma^{+}+1}(\rho^{r_{1,j}}u_{j})^{N_{0}})_{|\widetilde{U}_{0,a_{0}}} |  | 8 |

Soit b ∈ γ 1 b\in\gamma_{1} proche de a 0 a_{0}. L’une des coordonnées u j ​ ( b) u_{j}(b) est non nulle. Le lemme de cohérence IB3 appliqué à (8) donne

 | I χ ~, f ~, b | U ~ 0, b ⊃ ( ρ N 1) {I}_{\widetilde{\chi},\widetilde{f},b|\widetilde{U}_{0,b}}\supset(\rho^{N_{1}}) |  | 9 |

Soit X ⁡ ( ρ, μ) X(\rho,\mu) les fonctions élémentaires de l’algèbre Q R H 1,. ( ρ,.) QR{H}^{1,.}(\rho,.) et soit g = 𝕛 X N 1 + 1 ​ ( f ~) g={\mathbb{j}}_{X}^{N_{1}+1}(\widetilde{f}). Son germe en tout a ∈ D k a\in{D}_{k} est induit par un élément de Q R H c ​ v ​ g 1,. ( ρ,.) QR{H}^{1,.}_{cvg}(\rho,.) et f ~ a − g a ∈ ( ρ N 1 + 1) \widetilde{f}_{a}-g_{a}\in(\rho^{N_{1}+1}). D’après (9) et le lemme de Nakayama, les fibres en b b de f ~ \widetilde{f} et g g coincident, et par le lemme d’isomorphie IB4, leurs faisceaux le long de γ 1 \gamma_{1} coincident, et on a

 | I χ ~, f ~, a | U ~ 0, a ⊃ ( ρ N 1) {I}_{\widetilde{\chi},\widetilde{f},a|\widetilde{U}_{0,a}}\supset(\rho^{N_{1}}) |  | 10 |

(b) Sur le bord de D k {D}_{k}.

On utilise le lemme de récurrence IVB1. D’après (10), les fibres de f ~ \widetilde{f} le long de γ 1 \gamma_{1} satisfont à l’hypothèse ( i k ′) (i_{k^{\prime}}). L’hypothèse ( i ​ i k ′) (ii_{k^{\prime}}) est une conséquence de la structure du morphisme π k \pi_{k}.∎

C. Cas général et lemme de récurrence 2.

Soient x = ( x 1, …, x k) x=(x_{1},\ldots,x_{k}), α = ( μ, ν) \alpha=(\mu,\nu) et χ ∈ Ξ ​ H k \chi\in\Xi{H}_{k}. Grâce au théorème principal IIIB1, on généralise le théorème IVB1 dans le

###### Théorème IVC1

L’algèbre Q ​ R ​ H k,. ​ ( x, α) QR{H}^{k,.}(x,\alpha) est localement χ \chi -finie.

Preuve. Soit f ∈ Q ​ R ​ H k,. f\in QR{H}^{k,.}. Nous allons montrer que f f est localement χ \chi -finie sur un voisinage U U de 0. Soit ( π k, N k) (\pi_{k},{N}_{k}) le premier éclatement de la désingularisation de χ \chi de diviseur exceptionnel D ¯ k \overline{{D}}_{k} et soit χ ~ \widetilde{\chi} et f ~ \widetilde{f} les relevés par π k \pi_{k} de χ \chi et f f. Montrons que f ~ \widetilde{f} est localement χ ~ \widetilde{\chi} -finie sur un voisinage dans N k {N}_{k} de tout point de D ¯ k \overline{{D}}_{k}.

§1. Au dessus de D k {D}_{k}.

Soit u = ( u 1, …, u k − 1) u=(u_{1},\ldots,u_{k-1}) la coordonnée globale sur D k {D}_{k} et ( ρ, α, u) (\rho,\alpha,u) les coordonnées sur N k {N}_{k} au dessus de D k {D}_{k}. D’après la partie A, on a

 | χ ~ = ρ ​ ∂ ∂ ρ − ∑ j = 1 k − 1 s j ​ u j ​ ∂ ∂ u j \widetilde{\chi}=\rho\frac{\partial}{\partial\rho}-\sum_{j=1}^{k-1}s_{j}u_{j}\frac{\partial}{\partial u_{j}} |  |

et f ~ a ∈ Q ​ R ​ H 1,. ​ ( ρ, α, u − u a) \widetilde{f}_{a}\in QR{H}^{1,.}(\rho,\alpha,u-u_{a}) pour tout a ∈ D k a\in{D}_{k}. Soit a 0 a_{0} l’unique singularité de χ ~ \widetilde{\chi} sur D k {D}_{k} et γ 0 = { α = 0, u = 0 } \gamma_{0}=\{\alpha=0,\ \ u=0\} la trajectoire principale de χ ~ a 0 \widetilde{\chi}_{a_{0}} dans un voisinage U a 0 U_{a_{0}} de a 0 a_{0}. Soit π χ ~ a 0: ( ρ, α, u) ∈ U a 0 ↦ ( α, λ) ∈ W \pi_{\widetilde{\chi}_{a_{0}}}:\ (\rho,\alpha,u)\in U_{a_{0}}\mapsto(\alpha,\lambda)\in W le morphisme intégral de χ ~ a 0 \widetilde{\chi}_{a_{0}}.

1.1. En a 0 a_{0}. Le résultat est une conséquence immédiate du théorème principal IIIB1.

1.2. En dehors de a 0 a_{0}.

Soit J ⊂ ℝ ​ { α, λ } J\subset\mathbb{R}\{\alpha,\lambda\} l’idéal χ ~ a 0 \widetilde{\chi}_{a_{0}} -transverse de f ~ a 0 \widetilde{f}_{a_{0}} le long de γ 0 \gamma_{0}. L’idée générale est la suivante: on veut préparer f ~ \widetilde{f} dans J J globalement au dessus de D k {D}_{k}. Ceci repose sur une préparation de l’idéal J + M λ J+{M}_{\lambda} en vue de la détermination de la perte d’analycité dans J J à la traversée de l’ensemble singulier { ρ = 0, u = 0 } \{\rho=0,\ \ u=0\}. En effet, l’ensemble limite du saturé du sous-ensemble Z ( J) ∩ { λ = 0 } Z(J)\cap\{\lambda=0\} est inclus dans le bord { ρ = 0 } \{\rho=0\}. Soit donc ( ψ, N) (\psi,{N}) une désingularisation dans laquelle l’idéal J + M λ J+{M}_{\lambda} est principal, monomial et ordonné (lemme IIIB1). Soit ( c, V c) (c,V_{c}) une carte de cette désingularisation de coordonnée v = ( v 1, …, v p) v=(v_{1},\ldots,v_{p}). Notons J c = ( φ) = ψ c ∗ ​ ( J) J_{c}=(\varphi)=\psi_{c}^{*}(J) avec φ = ∏ j = 1 p v j n j \varphi=\prod_{j=1}^{p}v_{j}^{n_{j}}. Soient μ j, c = ψ c ∗ ​ ( μ j) \mu_{j,c}=\psi_{c}^{*}(\mu_{j}), s j, c = 1 + μ j, c s_{j,c}=1+\mu_{j,c} et λ j, c = ψ c ∗ ​ ( λ j) \lambda_{j,c}=\psi_{c}^{*}(\lambda_{j}). Quitte à réindéxer, on suppose que

 | ( λ k − 1, c) ⊂ ⋯ ⊂ ( λ 1, c) (\lambda_{k-1,c})\subset\cdots\subset(\lambda_{1,c}) |  | 1 |

La perte d’analycité dans cette carte est alors l’image dans W W du sous-ensemble { λ 1, c = 0 } \{\lambda_{1,c}=0\}. Deux cas se présentent:

(a) ( λ 1, c) ⊂ rad ​ ( φ) (\lambda_{1,c})\subset\text{rad}(\varphi). Dans ce cas, la perte d’analycité est totale: l’idéal J c J_{c} satisfait à l’hypothèse ( H ​ λ) (H\lambda) relativement à l’idéal ψ c ∗ ​ ( M λ) \psi_{c}^{*}({M}_{\lambda}). Le résultat est donc une conséquence du théorème IVB1.

(b) Dans le cas contraire, soit p ′ < p p^{\prime}<p tel que λ 1, c = v 1 n 1 ′ × ⋯ × v p ′ n p ′ ′ ( 1 + O ( v)) \lambda_{1,c}=v_{1}^{n^{\prime}_{1}}\times\cdots\times v_{p^{\prime}}^{n^{\prime}_{p^{\prime}}}(1+O(v)) avec n j ′ ≤ n j n^{\prime}_{j}\leq n_{j}. Soit φ = φ ′ ​ φ ​ " \varphi=\varphi^{\prime}\varphi" l’unique factorisation de φ \varphi telle que rad ​ ( φ ′) = rad ​ ( λ 1, c) \text{rad}(\varphi^{\prime})=\text{rad}(\lambda_{1,c}) et φ ′ ∧ φ ​ " = 1 \varphi^{\prime}\wedge\varphi"=1. Pour obtenir une division globale (au dessus de D k {D}_{k}) de f ~ \widetilde{f} par φ " = v p ′ + 1 n p ′ + 1 × ⋯ × v p n p \varphi"=v_{p^{\prime}+1}^{n_{p^{\prime}+1}}\times\cdots\times v_{p}^{n_{p}}, il faut plutôt étudier les intégrales premières ramifiées | λ j, c | 1 / s j, c |\lambda_{j,c}|^{1/s_{j,c}} (cf. (3) ci-dessous). Pour cela, une deuxième préparation des intégrales premières λ j, c \lambda_{j,c} et μ j, c \mu_{j,c} est nécessaire.

Pour simplifier la présentation, on notera toujours s j s_{j} les relevés des fonctions s j, c s_{j,c} dans cette préparation. Soient p ​ " = p − p ′ p"=p-p^{\prime}, v 0 ′ = ( v j, 0 ′) = ( v 1, …, v p ′) v^{\prime}_{0}=(v^{\prime}_{j,0})=(v_{1},\ldots,v_{p^{\prime}}), et v ​ " 0 = ( v ​ " j, 0) = ( v p ′ + 1, …, v p) v"_{0}=(v"_{j,0})=(v_{p^{\prime}+1},\ldots,v_{p}). Plaçons nous dans un quadrant dans les coordonnées v 0 ′ v^{\prime}_{0}, par exemple v j, 0 ′ > 0 v^{\prime}_{j,0}>0 pour tout j j. Effectuons une désingularisation dans les coordonnées v ​ " 0 v"_{0}, et prenons par exemple la carte

 | v ​ " j, 0 = v ​ " 1, 0 ​ v ^ j v"_{j,0}=v"_{1,0}\widehat{v}_{j} |  | 2 |

puis faisons un éclatement dans le couple ( v ​ " 1, 0, λ 1, c) (v"_{1,0},\lambda_{1,c}). Deux cas se présentent:

(b.1) | v ​ " 1, 0 | < ϵ ​ λ 1, c |v"_{1,0}|<\epsilon\lambda_{1,c}. Dans ce cas, on pose

 | v ​ " 1, 0 = v ​ " 1, 1 ​ λ 1, c, v ​ " j, 1 = v ^ j ​ pour ​ j > 1, v ​ " 1 = ( v ​ " j, 1) ​ et ​ v 1 ′ = v 0 ′ v"_{1,0}=v"_{1,1}\lambda_{1,c},\ v"_{j,1}=\widehat{v}_{j}\ \text{pour}\ j>1,\ v"_{1}=(v"_{j,1})\ \text{et}\ v^{\prime}_{1}=v^{\prime}_{0} |  |

(b.2) λ 1, c < ( 2 / ϵ) ​ | v ​ " 1, 0 | \lambda_{1,c}<(2/\epsilon)|v"_{1,0}|. Cette situation est couverte par un nombre fini de cartes qui sont de deux types: pour l’un, il existe j 0 j_{0} tel que ( v j 0, 0 ′) n j 0 ′ < ( 2 / ϵ) ​ | v ​ " 1, 0 | (v^{\prime}_{j_{0},0})^{n^{\prime}_{j_{0}}}<(2/\epsilon)|v"_{1,0}|. Dans ce cas, on pose

 | v j 0, 0 ′ = v j 0, 1 ′ ​ ( ( 2 / ϵ) ​ | v ​ " 0, 1 |) 1 / n j 0 ′, v j, 1 ′ = v j, 0 ′ ​ pour ​ j ≠ j 0, v^{\prime}_{j_{0},0}=v^{\prime}_{j_{0},1}((2/\epsilon)|v"_{0,1}|)^{1/n^{\prime}_{j_{0}}},\ v^{\prime}_{j,1}=v^{\prime}_{j,0}\ \text{pour}\ j\neq j_{0}, |  |

 | v p ′ + 1, 1 ′ = | v ​ " 0, 1 | 1 / n j 0 ′, v 1 ′ = ( v j, 1 ′) ​ et ​ v ​ " 1 = ( v ^ 2, …, v ^ p ​ ") = ( v ​ " j, 1) v^{\prime}_{p^{\prime}+1,1}=|v"_{0,1}|^{1/n^{\prime}_{j_{0}}},\ v^{\prime}_{1}=(v^{\prime}_{j,1})\ \text{et}v"_{1}=(\widehat{v}_{2},\ldots,\widehat{v}_{p"})=(v"_{j,1}) |  |

Pour l’autre type, on a ( v j, 0 ′) n j ′ ≥ ( 2 / ϵ) ​ | v ​ " 1, 0 | (v^{\prime}_{j,0})^{n^{\prime}_{j}}\geq(2/\epsilon)|v"_{1,0}| pour tout j j. Dans ce cas, on pose

 | v j, 0 ′ = v p ′ + 1, 1 ′ ​ v j, 1 ′ ​ avec ​ ∏ j = 1 p ′ ( v j, 1 ′) n j ′ = ( 2 / ϵ) ​ | v ​ " 0, 1 |, v^{\prime}_{j,0}=v^{\prime}_{p^{\prime}+1,1}v^{\prime}_{j,1}\ \text{avec}\ \prod_{j=1}^{p^{\prime}}(v^{\prime}_{j,1})^{n^{\prime}_{j}}=(2/\epsilon)|v"_{0,1}|, |  |

 | v 1 ′ = ( v j, 1 ′) ​ et ​ v ​ " 1 = ( v ^ 2, …, v ^ p ​ ") = ( v ​ " j, 1) v^{\prime}_{1}=(v^{\prime}_{j,1})\ \text{et}\ v"_{1}=(\widehat{v}_{2},\ldots,\widehat{v}_{p"})=(v"_{j,1}) |  |

Dans les deux cas, notons v ~ 1 \widetilde{v}_{1} les coordonnées locales au voisinage des coordonnées v ′. v^{\prime}_{.} ou v ". v"_{.} qui ne sont pas voisines de 0. Soient μ j, 1 \mu_{j,1}, λ j, 1 \lambda_{j,1} et φ 1 \varphi_{1} les relevés des fonctions μ j, c \mu_{j,c}, λ j, c \lambda_{j,c} et φ \varphi dans les coordonnées

 | v 1 ′ = ( v 1, 1 ′, …, v p 1 ′, 1 ′), v ​ " 1 = ( v ​ " 1, 1, …, v ​ " p ​ " 1, 1) ​ et ​ v ~ 1 = ( v ~ 1, 1, …, v ~ p ~ 1, 1) v^{\prime}_{1}=(v^{\prime}_{1,1},\ldots,v^{\prime}_{p^{\prime}_{1},1}),\ v"_{1}=(v"_{1,1},\ldots,v"_{p"_{1},1})\ \text{et}\ \widetilde{v}_{1}=(\widetilde{v}_{1,1},\ldots,\widetilde{v}_{\widetilde{p}_{1},1}) |  |

On a ( φ 1) = ( φ 1 ′ ​ ( v 1 ′)) ​ ( φ ​ " 1 ​ ( v ​ " 1)) (\varphi_{1})=(\varphi^{\prime}_{1}(v^{\prime}_{1}))(\varphi"_{1}(v"_{1})) avec rad ​ ( φ 1 ′) = rad ​ ( λ 1, 1) \text{rad}(\varphi^{\prime}_{1})=\text{rad}(\lambda_{1,1}). On répète alors ce procédé au plus p ​ " p" fois appliqué aux cartes (b.2). A une certaine étape i i de ce procédé, on obtient p ​ " i = 0 p"_{i}=0, auquel cas la perte d’analycité est totale et on est dans la situation de l’hypothèse ( H ​ λ) (H\lambda). Le résultat est alors une conséquence du théorème IVB1.

Plaçons nous maintenant dans une carte (b.1) à une certaine étape i i. Soient μ j, i \mu_{j,i}, λ j, i \lambda_{j,i} et φ i \varphi_{i} les relevés des fonctions μ j, c \mu_{j,c}, λ j, c \lambda_{j,c} et φ \varphi dans les coordonnées

 | v i ′ = ( v 1, i ′, …, v p i ′, i ′), v ​ " i = ( v ​ " 1, i, …, v ​ " p ​ " i, i) ​ et ​ v ~ i = ( v ~ 1, i, …, v ~ p ~ i, i) v^{\prime}_{i}=(v^{\prime}_{1,i},\ldots,v^{\prime}_{p^{\prime}_{i},i}),\ v"_{i}=(v"_{1,i},\ldots,v"_{p"_{i},i})\ \text{et}\ \widetilde{v}_{i}=(\widetilde{v}_{1,i},\ldots,\widetilde{v}_{\widetilde{p}_{i},i}) |  |

On a ( φ i) = ( φ i ′ ​ ( v i ′)) ​ ( φ ​ " i ​ ( v ​ " i)) (\varphi_{i})=(\varphi^{\prime}_{i}(v^{\prime}_{i}))(\varphi"_{i}(v"_{i})) avec rad ​ ( φ i ′) = rad ​ ( λ 1, i) \text{rad}(\varphi^{\prime}_{i})=\text{rad}(\lambda_{1,i}). Soit ( c i, V i) (c_{i},V_{i}) cette carte de coordonnées v i = ( v i ′, v ~ i, v ​ " i) v_{i}=(v^{\prime}_{i},\widetilde{v}_{i},v"_{i}) avec V i = V i ′ × V ~ i × V ​ " i V_{i}=V^{\prime}_{i}\times\widetilde{V}_{i}\times V"_{i} et V i ′ V^{\prime}_{i} est un voisinage de 0 dans un quadrant, par exemple v j, i ′ > 0 v^{\prime}_{j,i}>0 pour tout j j. Soit W i ⊂ W W_{i}\subset W l’image de cette carte et soit U i U_{i} le saturé de W i W_{i} par le flot de χ ~ \widetilde{\chi}. Il s’agit de diviser f ~ \widetilde{f} par φ ​ " i \varphi"_{i} globalement au dessus de D i = U i ¯ ∩ D k D_{i}=\overline{U_{i}}\cap{D}_{k}.

Supposons que les fonctions μ j, i \mu_{j,i} et λ j, i \lambda_{j,i} sont préparées sphériquement dans les coordonnées v ​ " i v"_{i} comme dans le théorème principal IIIB1, dont on reprend les notations. Divisons ρ S ​ f ~ a 0 | U i, a 0 \rho^{S}\widetilde{f}_{a_{0}|U_{i,a_{0}}} par φ ​ " i \varphi"_{i} dans une extension adaptée ( Q ​ R ​ H ~ p ​ " i | U 0, p ​ " i, π p ​ " i) (\widetilde{QR{H}}_{p"_{i}|{U}_{0,p"_{i}}},\pi_{p"_{i}}) sur laquelle agit la dérivation X p ​ " i {X}_{p"_{i}}. Soit U p ​ " i {U}_{p"_{i}} le saturé de U 0, p ​ " i {U}_{0,p"_{i}} par le flot de X p ​ " i {X}_{p"_{i}} au dessus de D k p ​ " i + 1 {D}_{k}^{p"_{i}+1} et soit Δ i = U ¯ p ​ " i ∩ D k p ​ " i + 1 \Delta_{i}=\overline{{U}}_{p"_{i}}\cap{D}_{k}^{p"_{i}+1}. Les séries de ρ S ​ f ~ \rho^{S}\widetilde{f} dans les variables w ( n) = u ( n − 1) − u ( n) w^{(n)}=u^{(n-1)}-u^{(n)} sont convergentes sur un voisinage de 0 uniformément au dessus de tout compact de la diagonale de D k p ​ " i + 1 {D}_{k}^{p"_{i}+1}. Donc, la division en a 0 a_{0} est globale au dessus de D i D_{i} si Δ i \Delta_{i} est inclus dans cette diagonale.

Or, en tout point a ∈ D i ∖ { a 0 } a\in D_{i}\setminus\{a_{0}\}, il existe ℓ \ell tel que u ℓ ​ ( a) ≠ 0 u_{\ell}(a)\neq 0. Sur un voisinage de a a, les fonctions

 | | u j | 1 / s j | u ℓ | 1 / s ℓ = | λ j | 1 / s j | λ ℓ | 1 / s ℓ \frac{|u_{j}|^{1/s_{j}}}{|u_{\ell}|^{1/s_{\ell}}}=\frac{|\lambda_{j}|^{1/s_{j}}}{|\lambda_{\ell}|^{1/s_{\ell}}} |  | 3 |

sont des intégrales premières de χ ~ \widetilde{\chi}. Notons τ j, ℓ ​ ( v i) \tau_{j,\ell}(v_{i}) ces derniers rapports écrits dans la carte V i V_{i} pour des indices j, ℓ < k j,\ell<k. Soit V ℓ, i = { v i ∈ V i; τ j, ℓ ​ ( v i) < 3 ​ pour tout ​ j } V_{\ell,i}=\{v_{i}\in V_{i};\ \tau_{j,\ell}(v_{i})<3\ \text{pour tout}\ j\}. D’après (1) et l’éclatement (b.1)

 | λ j, i ∈ M v ​ " i ⟹ λ j, i ∈ ( λ 1, i 2) ​ M v ​ " i \lambda_{j,i}\in{M}_{v"_{i}}\Longrightarrow\lambda_{j,i}\in(\lambda_{1,i}^{2}){M}_{v"_{i}} |  | 4 |

Soit k i k_{i} le plus grand indice j j tel que λ j, i ∉ M v ​ " i \lambda_{j,i}\not\in{M}_{v"_{i}}. D’après (1) et (4), les sous-ensembles V ℓ, i V_{\ell,i} sont vides pour tout ℓ = k i + 1, …, k − 1 \ell=k_{i}+1,\ldots,k-1.

Plaçons nous dans l’un des sous-ensembles V ℓ, i V_{\ell,i}, par exemple V 1, i V_{1,i} et soient W 1, i W_{1,i}, U 1, i U_{1,i}, U 1, p ​ " i {U}_{1,p"_{i}}, D 1, i D_{1,i} et Δ 1, i \Delta_{1,i} les sous-ensembles correspondants. D’après l’éclatement (b.1)

 | μ j, i − μ j, i ​ ( v i ′, v ~ i, 0) ∈ ( λ 1, i) ​ M v ​ " i \mu_{j,i}-\mu_{j,i}(v^{\prime}_{i},\widetilde{v}_{i},0)\in(\lambda_{1,i}){M}_{v"_{i}} |  | 5 |

Donc les rapports τ j, 1 \tau_{j,1} tendent vers τ j, 1 ​ ( v i ′, v ~ i, 0) \tau_{j,1}(v^{\prime}_{i},\widetilde{v}_{i},0) quand v ​ " i v"_{i} tend vers 0 uniformément en ( v i ′, v ~ i) (v^{\prime}_{i},\widetilde{v}_{i}). De plus, le sous-ensemble V 1, i V_{1,i} contient un produit V 1, i ′ × V ​ " 1, i V^{\prime}_{1,i}\times V"_{1,i} où V 1, i ′ = { ( v i ′, v ~ i) ∈ V i ′ × V ~ i; τ j, 1 ​ ( v i ′, v ~ i) < 2 ​ pour tout ​ j } V^{\prime}_{1,i}=\{(v^{\prime}_{i},\widetilde{v}_{i})\in V^{\prime}_{i}\times\widetilde{V}_{i};\ \tau_{j,1}(v^{\prime}_{i},\widetilde{v}_{i})<2\ \text{pour tout}\ j\} et V ​ " 1, i V"_{1,i} est un voisinage de 0.

Soit n ≤ p ​ " i n\leq p"_{i}. Sur D 1, i D_{1,i} privé d’un voisinage de 0, la coordonnée u 1 u_{1} ne s’annule pas. Et d’après (5), | u 1, n | 1 / s 1, n / | u 1 | 1 / s 1 |u_{1,n}|^{1/s_{1,n}}/|u_{1}|^{1/s_{1}} tend vers 1 quand v i v_{i} tend vers 0 (et même uniformément en ( v i ′, v ~ i) (v^{\prime}_{i},\widetilde{v}_{i})). Donc, sur Δ 1, i \Delta_{1,i} on a u 1, n = u 1 u_{1,n}=u_{1}. De même, en utilisant les rapports

 | τ j, 1, n ′ = | u j, n | | u 1, n | s j, n / s 1, n \tau^{\prime}_{j,1,n}=\frac{|u_{j,n}|}{|u_{1,n}|^{s_{j,n}/s_{1,n}}} |  |

et la relation (5), on montre que sur Δ 1, i \Delta_{1,i} on a u j, n = u j u_{j,n}=u_{j} pour tout j j et pour tout n n. Le sous-ensemble Δ 1, i \Delta_{1,i} est donc inclus dans la diagonale de D k p ​ " i + 1 {D}_{k}^{p"_{i}+1}.

Soit h h le quotient de la division de ρ S ​ f ~ \rho^{S}\widetilde{f} par φ ​ " i \varphi"_{i} au dessus de Δ 1, i \Delta_{1,i}. Pour tout A ∈ Δ 1, i A\in\Delta_{1,i}, on a h A ∈ Q ​ R ​ H ~ p ​ " i ​ ( ρ, v i, u − u ⁡ ( A), u ( 1) − u ( 1) ​ ( A), ⋯, u ( p ​ " i) − u ( p ​ " i) ​ ( A)) h_{A}\in\widetilde{QR{H}}_{p"_{i}}(\rho,v_{i},u-u(A),u^{(1)}-u^{(1)}(A),\cdots,u^{(p"_{i})}-u^{(p"_{i})}(A)). Soit A 0 = { ρ = 0, v i = 0, u = u ( 1) = ⋯ = u ( p ​ " i) = 0 } A_{0}=\{\rho=0,\ v_{i}=0,\ u=u^{(1)}=\cdots=u^{(p"_{i})}=0\} la singularité principale de X p ​ " i {X}_{p"_{i}}. L’idéal transverse de h A 0 | U 1, p ​ " i h_{A_{0}|{U}_{1,p"_{i}}} est ( φ i ′) (\varphi^{\prime}_{i}) qui satisfait à l’hypothèse ( H ​ λ) (H\lambda). On conclut donc au résultat par les méthodes de la partie B appliquées au faisceau I X p ​ " i, h ​ [Δ 1, i] {I}_{{X}_{p"_{i}},h}[\Delta_{1,i}].

§2. Sur le bord de D k {D}_{k}.

On utilise le lemme de récurrence 2 ci-dessous, qu’on a choisi de présenter au §3 pour deux raisons: d’une part, ses idées généralisent simplement celles des §1 et 2 et celles du lemme de récurrence 1, et d’autre part sa présentation est beaucoup plus difficile essentiellement à cause des notations. Soit γ ⊂ D 1, i \gamma\subset D_{1,i} une trajectoire de χ ~ \widetilde{\chi}, a = ∂ D k ∩ γ ¯ a=\partial{D}_{k}\cap\overline{\gamma} et k ′ k^{\prime} la dimension de non trivialité de la dérivation d’Hilbert χ ~ a \widetilde{\chi}_{a}. Il s’agit de prouver les hypothèses algébriques ( i k ′) (i_{k^{\prime}}) et ( i ​ i k ′) (ii_{k^{\prime}}) et la propriété topologique ( t k ′) (t_{k^{\prime}}) au voisinage de a a.

Soit C k ′ C_{k^{\prime}} le sous-ensemble de ∂ D k \partial{D}_{k} constitué des points où la dimension de non trivialté de la dérivation d’Hilbert est k ′ − 1 k^{\prime}-1. Quitte à réduire les rapports τ j, 1 \tau_{j,1} dans un voisinage de leurs valeurs sur γ \gamma, on suppose que l’adhérence de D 1, i D_{1,i} ne rencontre qu’une seule composante connexe de C k ′ C_{k^{\prime}}. Soit Γ ⊂ Δ 1, i \Gamma\subset\Delta_{1,i} l’orbite du champ X p ​ " i {X}_{p"_{i}} correspondante à γ \gamma et soit A A le point de Γ ¯ \overline{\Gamma} correspondant à a a. D’après le §1.2, pour tout point B B de Γ \Gamma voisin de A A, les fibres I X p ​ " i, h, B | U 1, p ​ " i {I}_{{X}_{p"_{i}},h,B|{U}_{1,p"_{i}}} sont noethériennes et satisfont, par restriction à U 1, p ​ " i {U}_{1,p"_{i}} à l’inclusion

 | ( ρ n 0) ⊂ I X p ​ " i, h, B (\rho^{n_{0}})\subset{I}_{{X}_{p"_{i}},h,B} |  |

Or si b b est le point de γ \gamma correspondant à B B, les germes X p ​ " i, B {X}_{p"_{i},B} et χ ~ b \widetilde{\chi}_{b} sont réguliers et donc ”équivalents”: plus précisément, les fonctions

 | u j, n ′ = u j, n | u 1 | s j, n / s 1 u^{\prime}_{j,n}=\frac{u_{j,n}}{|u_{1}|^{s_{j,n}/s_{1}}} |  |

sont des intégrales premières analytiques de X p ​ " i {X}_{p"_{i}} le long de Γ \Gamma. Soit u j, n ′ ​ ( Γ) u^{\prime}_{j,n}(\Gamma) leurs valeurs sur Γ \Gamma. Dans le changement de coordonnées ν j, n ′ = u j, n ′ − u j, n ′ ​ ( Γ) \nu^{\prime}_{j,n}=u^{\prime}_{j,n}-u^{\prime}_{j,n}(\Gamma) germifié au dessus de Γ \Gamma, le champ X p ​ " i {X}_{p"_{i}} est transformé dans le champ χ ~ \widetilde{\chi}. Donc, dans une extension évidente de S B | U 1, i, b SB_{|U_{1,i,b}} obtenue par adjonction des coordonnées ν j, n ′ \nu^{\prime}_{j,n}, les fibres I χ ~, ρ S ​ f ~, b {I}_{\widetilde{\chi},\rho^{S}\widetilde{f},b} sont noethériennes et satisfont à la double inclusion

 | ( ρ n 0) ​ π χ ~, b ∗ ​ ( φ ​ " i) ⊂ I χ ~, ρ S ​ f ~, b ⊂ π χ ~, b ∗ ​ ( φ ​ " i) (\rho^{n_{0}})\pi^{*}_{\widetilde{\chi},b}(\varphi"_{i})\subset{I}_{\widetilde{\chi},\rho^{S}\widetilde{f},b}\subset\pi^{*}_{\widetilde{\chi},b}(\varphi"_{i}) |  |

et ceci prouve l’hypothèse ( i k ′) (i_{k^{\prime}}) car le germe en b b de la dérivation d’Hilbert χ ~ a \widetilde{\chi}_{a} est équivalent à la dérivation χ ~ b \widetilde{\chi}_{b}. L’hypothèse ( i ​ i k ′) (ii_{k^{\prime}}) est une conséquence de la structure du morphisme de désingularisation π k \pi_{k}.

Dans la réduction de la dérivation d’Hilbert χ \chi au voisinage de a a, on trivialise dans la coordonnée ρ \rho en posant ( ρ ′) s 1 = ρ s 1 ​ | u 1 | = | λ 1, i | (\rho^{\prime})^{s_{1}}=\rho^{s_{1}}|u_{1}|=|\lambda_{1,i}|. Les intégrales premières non triviales λ j ′ \lambda^{\prime}_{j} au voisinage de a a sont des fonctions régulières des rapports ν j ′ = λ j, i / ( ρ ′) s j \nu^{\prime}_{j}=\lambda_{j,i}/(\rho^{\prime})^{s_{j}} d’intégrales premières en a 0 a_{0}. On obtient donc la propriété ( t k ′) (t_{k^{\prime}}) en posant

 | ρ ( 1) = v i ′, L ′ = L, ν ~ = v ~ i, ν = v ​ " i, ν ′ = ( ( ν j ′), ( ν j, n ′)), V ′ = V 1, i ′ ​ et ​ V = V ​ " 1, i \rho^{(1)}=v^{\prime}_{i},\ L^{\prime}=L,\ \widetilde{\nu}=\widetilde{v}_{i},\ \nu=v"_{i},\ \nu^{\prime}=((\nu^{\prime}_{j}),(\nu^{\prime}_{j,n})),\ V^{\prime}=V^{\prime}_{1,i}\ \text{et}\ V=V"_{1,i} |  |

∎

§3. L’argument de récurrence.

Définissons d’abord les espaces des intégrales premières correspondants à cette situation et qui généralisent ceux de la partie B

###### Définition IVC1

Soit ( x, α) (x,\alpha) des coordonnées sur ℝ k × ℝ n \mathbb{R}^{k}\times\mathbb{R}^{n}. Notons

 | A 0 k, n ​ ( x, α) = A k, n ​ ( x, α) {A}_{0}^{k,n}(x,\alpha)={A}^{k,n}(x,\alpha) |  |

Soit V V un semi-analytique ouvert de A 0 k, n ​ ( x, α) {A}_{0}^{k,n}(x,\alpha) qui adhère à 0. On note A 1 k, n ​ ( V) {A}_{1}^{k,n}(V) l’anneau des germes de fonctions analytiques et bornées sur (un germe en 0 de) V V. Supposone définis les anneaux A i k, n (.) {A}_{i}^{k,n}(.). Soit V V un semi-analytique ouvert de A i k, n (.) {A}_{i}^{k,n}(.) qui adhère à 0. On note A i + 1 k, n ​ ( V) {A}_{i+1}^{k,n}(V) l’anneau des germes de fonctions analytiques et bornées sur (un germe en 0 de) V V.

###### Définition IVC2

Soient ( x, α, β) (x,\alpha,\beta) des coordonnées sur ℝ k × ℝ n × ℝ m \mathbb{R}^{k}\times\mathbb{R}^{n}\times\mathbb{R}^{m}. Notons

 | A 0 k, ( n, m) ​ ( x, α, β) = A k, n + m ​ ( x, α, β) {A}_{0}^{k,(n,m)}(x,\alpha,\beta)={A}^{k,n+m}(x,\alpha,\beta) |  |

Soit V ′ V^{\prime} un semi-analytique ouvert d’un anneau A i k, n (.) {A}_{i}^{k,n}(.) qui adhère à 0, et soit V V un voisinage de 0 dans ℝ m \mathbb{R}^{m}. On note A i k, ( n, m) ​ ( V ′ × V) {A}_{i}^{k,(n,m)}(V^{\prime}\times V) l’anneau des germes de fonctions analytiques et bornées sur (le germe en 0 de) V ′ × 𝕍 V^{\prime}\times{\mathbb{V}} où 𝕍 {\mathbb{V}} est le complexifié de V V.

Remarque IVC1. Tout f ∈ A i k, ( n, m) ​ ( V ′ × V) f\in{A}_{i}^{k,(n,m)}(V^{\prime}\times V) est la somme d’une série

 | f = ∑ N f N ​ ( x, α) ​ β N f=\sum_{N}f_{N}(x,\alpha)\beta^{N} |  | 6 |

convergente sur le produit d’un représentant V f ′ V^{\prime}_{f} de V ′ V^{\prime} et d’un polydisque de ℂ m \mathbb{C}^{m} et dont les coefficients f N f_{N} appartiennent à l’anneau A i + 1 k, n ​ ( V ′) {A}_{i+1}^{k,n}(V^{\prime}) et sont tous réalisés sur V f ′ V^{\prime}_{f}.

Soient x = ( x 1, …, x k) x=(x_{1},\ldots,x_{k}), ρ = ( ρ 1, …, ρ L) \rho=(\rho_{1},\ldots,\rho_{L}) avec L > 0 L>0 et α = ( μ, ν, ν ~, ν ′) \alpha=(\mu,\nu,\widetilde{\nu},\nu^{\prime}) une coordonnée sur ℝ q 1 × ℝ q 2 × ℝ q 3 × ℝ q 4 \mathbb{R}^{q_{1}}\times\mathbb{R}^{q_{2}}\times\mathbb{R}^{q_{3}}\times\mathbb{R}^{q_{4}}. Soient q = ( q 1, q 2 + q 3 + q 4) q=(q_{1},q_{2}+q_{3}+q_{4}) et χ ∈ Ξ ​ H k ​ [Q ​ R ​ H k + L, q] \chi\in\Xi{H}_{k}[QR{H}^{k+L,q}]. Soit U U un voisinage de 0 sur lequel χ \chi est réalisée et soient g j = x j r j ​ ( 1 + D j) − x j + 1 g_{j}=x_{j}^{r_{j}}(1+D_{j})-x_{j+1} ces intégrales premières non triviales. Posons g = ( g 1, …, g k − 1) g=(g_{1},\ldots,g_{k-1}) et soit γ = { ( ρ, α, g) = 0 } \gamma=\{(\rho,\alpha,g)=0\} l’orbite principale dans U U. Soit π χ: ( x, ρ, α) ∈ U ↦ ( ρ, α, λ) = ( ρ, α, g) ∈ W \pi_{\chi}:(x,\rho,\alpha)\in U\mapsto(\rho,\alpha,\lambda)=(\rho,\alpha,g)\in W le morphisme intégral de χ \chi. Soit ρ ( 1) = ( ρ 1, ⋯, ρ L ′) \rho^{(1)}=(\rho_{1},\cdots,\rho_{L^{\prime}}), ρ ( 2) = ( ρ L ′ + 1, ⋯, ρ L) \rho^{(2)}=(\rho_{L^{\prime}+1},\cdots,\rho_{L}), β = ( ρ ( 1), ν ~) \beta=(\rho^{(1)},\widetilde{\nu}) et soit

 | i ​ m: ( β, ν) ∈ V ′ × V ↦ ( ρ ( 1), ρ ( 2) ​ ( β), μ ⁡ ( β, ν), ν, ν ~, ν ′ ​ ( β, ν), λ ⁡ ( β, ν)) ∈ W im:(\beta,\nu)\in V^{\prime}\times V\mapsto(\rho^{(1)},\rho^{(2)}(\beta),\mu(\beta,\nu),\nu,\widetilde{\nu},\nu^{\prime}(\beta,\nu),\lambda(\beta,\nu))\in W |  |

une immersion telle que

( t k) (t_{k}) V ′ V^{\prime} est un semi-analytique ouvert d’un anneau A. L ′, q 3 (.) {A}_{.}^{L^{\prime},q_{3}}(.) et V V est un voisinage de 0 dans ℝ q 2 \mathbb{R}^{q_{2}}. De plus, les fonctions composantes de ρ ( 2) \rho^{(2)} appartiennent à un anneau A. L ′, q 3 ( V ′) {A}_{.}^{L^{\prime},q_{3}}(V^{\prime}) et les fonctions composantes de μ \mu, ν ′ \nu^{\prime} et λ \lambda appartiennent à un anneau A. L ′, ( q 3, q 2) ( V ′ × V) {A}_{.}^{L^{\prime},(q_{3},q_{2})}(V^{\prime}\times V).

Soit W 0 = i ​ m ​ ( V ′ × V) W_{0}=im(V^{\prime}\times V) et soit U 0 = π χ − 1 ​ ( W 0) U_{0}=\pi_{\chi}^{-1}(W_{0}). Si m ∈ γ m\in\gamma, on note U 0, m U_{0,m} le germe de U 0 U_{0} en m m.

###### Lemme IVC1 (lemme de récurrence 2)

Soit f ∈ Q ​ R ​ H k + L, q f\in QR{H}^{k+L,q}. On suppose que

Alors f f est localement χ \chi -finie sur U 0 U_{0}.

Preuve. Elle est basée sur une récurrence sur la dimension de non-trivialité k − 1 k-1 et sur les arguments de l’algorithme de finitude utilisés dans le lemme de récurrence IVB1. L’étape k = 1 k=1 est une conséquence de ce qui suit. L’idée générale est la suivante: après désingularisation de χ \chi si nécessaire, on divise le relevé de f f dans l’idéal J 0 J_{0}. Par l’hypothèse ( i k) (i_{k}), le quotient de cette division satisfait alors aux hypothèses du lemme de récurrence IVB1.

Soit ( π k, N k) (\pi_{k},{N}_{k}) le premier éclatement de la désingularisation de χ \chi de diviseur exceptionnel D ¯ k \overline{{D}}_{k} et soit χ ~ \widetilde{\chi} et f ~ \widetilde{f} les relevés par π k \pi_{k} de χ \chi et f f. En identifiant W 0 W_{0} à son image par π k − 1 \pi_{k}^{-1}, soit U ~ 0 \widetilde{U}_{0} le saturé de W 0 W_{0} par le flot de χ ~ \widetilde{\chi}. Montrons que f ~ \widetilde{f} est localement χ ~ \widetilde{\chi} -finie sur un voisinage dans U ~ 0 \widetilde{U}_{0} de tout point de D ¯ k ∩ U ~ ¯ 0 \overline{{D}}_{k}\cap\overline{\widetilde{U}}_{0}.

3.1. Au dessus de D k {D}_{k}.

Soit u = ( u 1, …, u k − 1) u=(u_{1},\ldots,u_{k-1}) la coordonnée globale sur D k {D}_{k} et ( ρ 0, ρ, α, u) (\rho_{0},\rho,\alpha,u) les coordonnées sur N k {N}_{k} au dessus de D k {D}_{k}. On a

 | χ ~ = ρ 0 ​ ∂ ∂ ρ 0 − ∑ j = 1 k − 1 s j ​ u j ​ ∂ ∂ u j \widetilde{\chi}=\rho_{0}\frac{\partial}{\partial\rho_{0}}-\sum_{j=1}^{k-1}s_{j}u_{j}\frac{\partial}{\partial u_{j}} |  |

et f ~ a ∈ Q ​ R ​ H 1 + L,. ​ ( ρ 0, ρ, α, u − u a) \widetilde{f}_{a}\in QR{H}^{1+L,.}(\rho_{0},\rho,\alpha,u-u_{a}) pour tout a ∈ D k a\in{D}_{k}. Soit a 0 a_{0} l’unique singularité de χ ~ \widetilde{\chi} sur D k {D}_{k} et γ 0 = { ρ = 0, α = 0, u = 0 } \gamma_{0}=\{\rho=0,\ \alpha=0,\ \ u=0\} la trajectoire principale de χ ~ a 0 \widetilde{\chi}_{a_{0}} dans un voisinage de a 0 a_{0}.

3.1.1. En a 0 a_{0}.

La preuve reprend, en la généralisant, la méthode du théorème principal IIIB1. Soit ( ψ, N) (\psi,{N}) une désingularisation (dans les coordonnées ν \nu) dans laquelle l’idéal J 0 J_{0} est principal et monomial. En utilisant (6), on suppose que les fonctions μ j \mu_{j} et λ j \lambda_{j} sont préparées sphériquement dans cette désingularisation. Soit donc ( c, V c) (c,V_{c}) une carte de cette désingularisation de coordonnée v v et soit W c ⊂ W 0 W_{c}\subset W_{0} et U c ⊂ U ~ 0 U_{c}\subset\widetilde{U}_{0} les ensembles correspondants. Soit J c = ( φ) = ψ c ∗ ​ ( J 0) J_{c}=(\varphi)=\psi_{c}^{*}(J_{0}), avec φ = ∏ j = 1 p v j n j \varphi=\prod_{j=1}^{p}v_{j}^{n_{j}}. Soient μ j, c = ψ c ∗ ​ ( μ j) \mu_{j,c}=\psi_{c}^{*}(\mu_{j}) et λ j, c = ψ c ∗ ​ ( λ j) \lambda_{j,c}=\psi_{c}^{*}(\lambda_{j}) avec

 | μ j, c = μ j, p + 1 − i + μ j, p + 1 − i ′ et λ j, c = λ j, p + 1 − i + λ j, p + 1 − i ′ \mu_{j,c}=\mu_{j,p+1-i}+\mu^{\prime}_{j,p+1-i}\quad\text{et}\quad\lambda_{j,c}=\lambda_{j,p+1-i}+\lambda^{\prime}_{j,p+1-i} |  | 7 |

les fonctions μ j, p + 1 − i \mu_{j,p+1-i} et λ j, p + 1 − i \lambda_{j,p+1-i} sont indépendantes des coordonnées ( v i, …, v p) (v_{i},\ldots,v_{p}). Les fonctions μ j, p + 1 − i ′ \mu^{\prime}_{j,p+1-i} et λ j, p + 1 − i ′ \lambda^{\prime}_{j,p+1-i} appartiennent à l’idéal ( v 1 × ⋯ × v i) (v_{1}\times\cdots\times v_{i}) dans l’anneau A ⁡ ( V ′ × V c) {A}(V^{\prime}\times V_{c}).

Dans la division de ρ 0 S 0 ​ f ~ a 0 \rho_{0}^{S_{0}}\widetilde{f}_{a_{0}} par φ \varphi, les nouvelles fonctions élémentaires des extensions Q ​ R ​ H ~ \widetilde{QR{H}} portent sur les coordonnées ( ρ 0, ρ) (\rho_{0},\rho) de l’algèbre Q ​ R ​ H 1 + L,. QR{H}^{1+L,.}. De plus les (fonctions) coordonnées ( μ, ν ′) (\mu,\nu^{\prime}) analytiques de cette algèbre et les intégrales premières λ \lambda donnent lieu, dans cette division, à des (fonctions) coordonnées analytiques de l’extension qu’on notera ( ν ′) ( 0) (\nu^{\prime})^{(0)}.

Soit donc ( Q ​ R ​ H ~ p 1 + L ( ρ 0, ρ, v, ν ~, ( ν ′) ( 0), ( u 0 ( j))) | U p, π p) (\widetilde{QR{H}}^{1+L}_{p}(\rho_{0},\rho,v,\widetilde{\nu},(\nu^{\prime})^{(0)},(u_{0}^{(j)}))_{|{U}_{p}},\pi_{p}) l’extension dans laquelle la division de π p ∗ ​ ( ρ 0 S 0 ​ f ~ a 0) \pi_{p}^{*}(\rho_{0}^{S_{0}}\widetilde{f}_{a_{0}}) par φ \varphi est réalisée. Cette extension est définie par les formules sphériques (7), et par une induction sur L L comme pour les algèbres Q ​ R ​ H 1 + L,. QR{H}^{1+L,.}. Soit h 0 h_{0} le quotient de cette division. Soit X p {X}_{p} la dérivation qui relève χ ~ a 0 \widetilde{\chi}_{a_{0}} sur U c, 0 U_{c,0} germe de U c U_{c} en a 0 a_{0}. Soit Γ 0 \Gamma_{0} son orbite principale, et A 0 A_{0} sa singularité principale. On a ρ 0 ≠ 0 \rho_{0}\neq 0 le long de γ 0 \gamma_{0}. Donc en appliquant le morphisme π p ∗ \pi_{p}^{*} ( π p \pi_{p} étant germifié le long de Γ 0 \Gamma_{0}) à la double inclusion ( i k) (i_{k}), on obtient que les fibres de h 0 h_{0} le long de Γ 0 \Gamma_{0} contiennent ρ N 0 \rho^{N_{0}} (par restriction à U p {U}_{p}).

Dés lors, on applique la méthode du lemme de récurrence IVB1. Soit m ​ a + ma^{+} la multiplicité algébrique d’un représentant convergent de h 0 h_{0} modulo ( ρ N 1) (\rho^{N_{1}}), il en existe un d’après l’hypothèse ( i ​ i k) (ii_{k}). Ce représentant satisfait globalement à la double inclusion en A 0 A_{0} d’après le théorème principal IIIA1. Donc, en prenant un plongement de f f et des fonctions D j D_{j} à un ordre quelconque n 0, 1 > m ​ a + n_{0,1}>ma^{+} (cf. lemme de récurrence IVB1), on obtient que h 0 h_{0} est X p {X}_{p} -finie sur une restriction U p, n 0, 1 {U}_{p,n_{0,1}} de ce plongement (et il en est de même pour f ~ a 0 \widetilde{f}_{a_{0}} sur U c, 0, n 0, 1 U_{c,0,n_{0,1}} germe en a 0 a_{0} d’une restriction U c, n 0, 1 U_{c,n_{0,1}} de ce plongement). De plus on a la double inclusion par restriction à U p, n 0, 1 {U}_{p,n_{0,1}}

 | ( ρ 0 m ​ a + + 1 ​ ρ N 0 ​ φ) ⊂ I X p, π p ∗ ​ ( ρ 0 S 0 ​ f ~ a 0) ⊂ ( φ) (\rho_{0}^{ma^{+}+1}\rho^{N_{0}}\varphi)\subset I_{{X}_{p},\pi_{p}^{*}(\rho_{0}^{S_{0}}\widetilde{f}_{a_{0}})}\subset(\varphi) |  | 8 |

3.1.2 En dehors de a 0 a_{0}.

Comme dans le paragraphe 1.2, on veut déterminer la factorisation J c = ( φ ′) ​ ( φ ​ ") J_{c}=(\varphi^{\prime})(\varphi") telle que le sous-ensemble image dans W c W_{c} de { φ ′ = 0 } \{\varphi^{\prime}=0\} représente la perte d’analycité à la traversée des singularités a 0 ​ ( α) a_{0}(\alpha) et telle que la division de f ~ \widetilde{f} par φ ​ " \varphi" soit globale au dessus du sous-ensemble correspondant D c ⊂ D k D_{c}\subset{D}_{k}. On généralise la préparation du paragraphe 1.2 aux anneaux A ⁡ ( V ′ × V c) {A}(V^{\prime}\times V_{c}) de la façon suivante: soit λ j, c ′ ​ ( β) = λ j, c ​ ( β, 0) \lambda^{\prime}_{j,c}(\beta)=\lambda_{j,c}(\beta,0) et λ ​ " j, c = λ j, c − λ j, c ′ \lambda"_{j,c}=\lambda_{j,c}-\lambda^{\prime}_{j,c}. D’après (2), on a λ ​ " j, c ∈ ( v 1) \lambda"_{j,c}\in(v_{1}). Donc, l’ensemble limite du saturé par le flot de χ ~ \widetilde{\chi} de l’image dans W c W_{c} du sous-ensemble { ( λ j, c ′) = 0, v 1 = 0 } \{(\lambda^{\prime}_{j,c})=0,\ v_{1}=0\} est inclus dans l’ensemble singulier de χ ~ \widetilde{\chi} au dessus de a 0 a_{0}. Considérons donc les ensembles V ℓ, c ′ = { | λ j, c ′ | < 2 ​ | λ ℓ, c ′ |; pour tout ​ j } V^{\prime}_{\ell,c}=\{|\lambda^{\prime}_{j,c}|<2|\lambda^{\prime}_{\ell,c}|;\ \text{pour tout}\ j\} pour ℓ = 1, …, k − 1 \ell=1,\ldots,k-1 et V k, c ′ = { | λ j, c ′ | < 2 ​ | v 1 |, pour tout ​ j } V^{\prime}_{k,c}=\{|\lambda^{\prime}_{j,c}|<2|v_{1}|,\ \text{pour tout}\ j\}. La préparation (pr) est la suivante

(pr1) Sur V k, c ′ V^{\prime}_{k,c}, on pose

 | v 1 ′ = v 1 = ( v 1, 1 ′), v ​ " 1 = ( v 2, …, v p) = ( v ​ " 1, 1, …, v ​ " p ​ " 1, 1) ​ et ​ β 1 = ( β, v 1 ′) v^{\prime}_{1}=v_{1}=(v^{\prime}_{1,1}),\ v"_{1}=(v_{2},\ldots,v_{p})=(v"_{1,1},\ldots,v"_{p"_{1},1})\ \text{et}\ \beta_{1}=(\beta,v^{\prime}_{1}) |  |

Remarquons que p ​ " 1 < p p"_{1}<p. Les fonctions λ j, c \lambda_{j,c} se relèvent dans les fonctions λ j, 1 = v 1, 1 ′ ​ ( λ j, 1 ′ ​ ( β 1) + O ⁡ ( v ​ " 1)) \lambda_{j,1}=v^{\prime}_{1,1}(\lambda^{\prime}_{j,1}(\beta_{1})+O(v"_{1})).

(pr2) Sur V 1, c ′ V^{\prime}_{1,c} par exemple, deux cas se présentent:

(pr2.1) | v 1 | ≤ ϵ ​ | λ 1, c ′ | |v_{1}|\leq\epsilon|\lambda^{\prime}_{1,c}|. On pose alors

 | v 1 = v ​ " 1, 1 ​ λ 1, c ′, v 1 ′ = λ 1, c ′ = ( v 1, 1 ′), β 1 = ( β, v 1 ′) ​ et ​ v ​ " 1 = ( v ​ " 1, 1, v 2, …, v p) = ( v ​ " j, 1) v_{1}=v"_{1,1}\lambda^{\prime}_{1,c},\ v^{\prime}_{1}=\lambda^{\prime}_{1,c}=(v^{\prime}_{1,1}),\ \beta_{1}=(\beta,v^{\prime}_{1})\ \text{et}\ v"_{1}=(v"_{1,1},v_{2},\ldots,v_{p})=(v"_{j,1}) |  |

Les fonctions λ j, c \lambda_{j,c} se relèvent dans les fonctions λ j, 1 = v 1, 1 ′ ​ ( λ j, 1 ′ ​ ( β 1) + O ⁡ ( v ​ " 1)) \lambda_{j,1}=v^{\prime}_{1,1}(\lambda^{\prime}_{j,1}(\beta_{1})+O(v"_{1})). Remarquons que λ 1, 1 ′ ≡ 1 \lambda^{\prime}_{1,1}\equiv 1.

(pr2.2) ϵ ​ | λ 1, c ′ | < | v 1 | < 2 ​ | λ 1, c ′ | \epsilon|\lambda^{\prime}_{1,c}|<|v_{1}|<2|\lambda^{\prime}_{1,c}|. Ce cas se traîte comme le cas (pr1).

On répète ce procédé au plus p p fois appliqué aux cartes (pr1). A une certaine étape, on obtient p ". = 0 p"_{.}=0. La perte d’analycité est alors totale.

Plaçons nous dans une carte (pr2.1) à une étape i i. Les relevés des fonctions λ j, c \lambda_{j,c} s’écrivent

 | λ j, i = ∏ ℓ = 1 p i ′ v ℓ, i ′ ​ ( λ j, i ′ ​ ( β i) + O ⁡ ( v ​ " i)) ​ avec ​ λ 1, i ′ ≡ 1 \lambda_{j,i}=\prod_{\ell=1}^{p^{\prime}_{i}}v^{\prime}_{\ell,i}(\lambda^{\prime}_{j,i}(\beta_{i})+O(v"_{i}))\ \text{avec}\ \lambda^{\prime}_{1,i}\equiv 1 |  |

D’après (7), on a O ⁡ ( v ​ " i) = O ⁡ ( v ​ " 1, i) O(v"_{i})=O(v"_{1,i}). Dans ce cas, on applique la méthode préparatoire (pr) ci-dessus aux (fonctions) coordonnées λ j, i ′ ≢ 1 \lambda^{\prime}_{j,i}\not\equiv 1 et à la coordonnée v ​ " 1, i v"_{1,i}. Puis, on applique la méthode du paragraphe 1.2 (cas (b)) au couple constitué du facteur dominant de la préparation (pr) et de la (fonction) coordonnée λ 1, i \lambda_{1,i} qui représente la perte d’analycité. On répète ce procédé au plus ( k − 2 + p ​ " i) (k-2+p"_{i}) fois appliqué aux cartes (b.2). A une certaine étape de cette préparation, on obtient p ". = 0 p"_{.}=0.

Dans tous les cas, notons v ~ i \widetilde{v}_{i} les coordonnées locales au voisinage des coordonnées v ". v"_{.} qui ne sont pas voisines de 0. Posons v i = ( v i ′, v ~ i, v ​ " i) v_{i}=(v^{\prime}_{i},\widetilde{v}_{i},v"_{i}) et β ~ i = ( β i, v ~ i) \widetilde{\beta}_{i}=(\beta_{i},\widetilde{v}_{i}). On obtient la factorisation du relevé ( φ i) = ( φ i ′ ​ ( v i ′)) ​ ( φ ​ " i ​ ( v ​ " i)) (\varphi_{i})=(\varphi^{\prime}_{i}(v^{\prime}_{i}))(\varphi"_{i}(v"_{i})) et la préparation des relevés

 | λ 1, i = ∏ j = 1 p i ′ ( v j, i ′) n 1, j, i ′ ​ ( 1 + O ⁡ ( v ​ " i)) \lambda_{1,i}=\prod_{j=1}^{p^{\prime}_{i}}(v^{\prime}_{j,i})^{n^{\prime}_{1,j,i}}(1+O(v"_{i})) |  |

et pour ℓ ≠ 1 \ell\neq 1

 | λ ℓ, i = ∏ j = 1 p i ′ ( v j, i ′) n ℓ, j, i ′ ​ ( λ j, i ′ ​ ( β ~ i) + O ⁡ ( v ​ " i)) ​ avec ​ n ℓ, j, i ′ ≥ n 1, j, i ′ \lambda_{\ell,i}=\prod_{j=1}^{p^{\prime}_{i}}(v^{\prime}_{j,i})^{n^{\prime}_{\ell,j,i}}(\lambda^{\prime}_{j,i}(\widetilde{\beta}_{i})+O(v"_{i}))\ \text{avec}\ n^{\prime}_{\ell,j,i}\geq n^{\prime}_{1,j,i} |  |

D’après cette double préparation, il existe une partition v i ′ = ( ρ i ′, ρ ​ " i) v^{\prime}_{i}=(\rho^{\prime}_{i},\rho"_{i}) telle que les coordonnées ρ ​ " i \rho"_{i} soient des fonctions des coordonnées β i ′ = ( β, ρ i ′, v ~ i) \beta^{\prime}_{i}=(\beta,\rho^{\prime}_{i},\widetilde{v}_{i}) appartenant à un anneau A. ( V i ′) {A}_{.}(V^{\prime}_{i}) où V i ′ V^{\prime}_{i} est un semi-analytique ouvert d’un anneau A. (.) {A}_{.}(.) donné par la préparation ci-dessus. Comme dans le paragraphe 1, on utilise (7) pour montrer que les rapports τ j, ℓ ​ ( β i ′, v ​ " i) \tau_{j,\ell}(\beta^{\prime}_{i},v"_{i}) convergent vers τ j, ℓ ​ ( β i ′, 0) \tau_{j,\ell}(\beta^{\prime}_{i},0) quand v ​ " i v"_{i} tend vers 0 uniformément en β i ′ \beta^{\prime}_{i} sur les sous-ensembles non vides V ℓ, i = { ( β i ′, v ​ " i) ∈ V i ′ × V i; τ j, ℓ < 3 ​ pour tout ​ j } V_{\ell,i}=\{(\beta^{\prime}_{i},v"_{i})\in V^{\prime}_{i}\times V_{i};\ \tau_{j,\ell}<3\ \text{pour tout}\ j\} où V i V_{i} est un voisinage de 0 dans ℝ p ​ " i \mathbb{R}^{p"_{i}} donné par la préparation ci-dessus. De plus ce sous-ensemble V ℓ, i V_{\ell,i} contient le produit de V ℓ, i ′ = { β i ′ ∈ V i ′; τ i, ℓ < 2 ​ pour tout ​ j } V^{\prime}_{\ell,i}=\{\beta^{\prime}_{i}\in V^{\prime}_{i};\ \tau_{i,\ell}<2\ \text{pour tout}\ j\} qui est un semi-analytique ouvert de A. ( V i ′) {A}_{.}(V^{\prime}_{i}), et d’un voisinage V ​ " ℓ, i V"_{\ell,i} de 0.

Plaçons nous dans l’un des sous-ensembles non vides V ℓ, i V_{\ell,i}, par exemple V 1, i V_{1,i} et supposons que les fonctions μ j, i \mu_{j,i} et λ j, i \lambda_{j,i} sont préparées sphériquement dans les coordonnées v ​ " i v"_{i}. Soit h h le quotient de la division de ρ 0 S 1 ​ f ~ \rho_{0}^{S_{1}}\widetilde{f} par φ ​ " i \varphi"_{i} en a 0 a_{0} (si p ​ " i = 0 p"_{i}=0, on prend h = f ~ h=\widetilde{f}). Soit n i ′ n^{\prime}_{i} le plus petit entier tel que λ 1, i n i ′ ∈ ( φ i ′) \lambda_{1,i}^{n^{\prime}_{i}}\in(\varphi^{\prime}_{i}). Choisissons un ordre n 0, 1 n_{0,1} de plongement de f f et des fonctions D j D_{j} (cf. §3.1.1) tel que

 | n 0, 1 > n 0, 0 = m ​ a + + 1 + S 1 ​ ( 0) + 2 ​ n i ′ n_{0,1}>n_{0,0}=ma^{+}+1+S_{1}(0)+2n^{\prime}_{i} |  |

Soit ( Q ​ R ​ H ~ p ​ " i | U p ​ " i 1 + L, π p ​ " i) (\widetilde{QR{H}}^{1+L}_{p"_{i}|{U}_{p"_{i}}},\pi_{p"_{i}}) l’extension associée à cette division. Soient W 1, i W_{1,i}, U 1, i ⊂ U c, n 0, 1 U_{1,i}\subset U_{c,n_{0,1}}, U 1, p ​ " i {U}_{1,p"_{i}}, D 1, i D_{1,i} et Δ 1, i \Delta_{1,i} les sous-ensembles correspondants à V 1, i V_{1,i}. Comme dans le paragraphe 1, on montre que Δ 1, i \Delta_{1,i} est inclus dans la diagonale de D k p ​ " i + 1 {D}_{k}^{p"_{i}+1}. Donc cette division est globale au dessus de Δ 1, i \Delta_{1,i} et pour tout A ∈ Δ 1, i A\in\Delta_{1,i}, on a h A ∈ Q ​ R ​ H ~ p ​ " i 1 + L ​ ( ρ 0, ρ, v i, ν ~, ( ν ′) ( 1), u − u ⁡ ( A), u ( 1) − u ( 1) ​ ( A), ⋯, u ( p ​ " i) − u ( p ​ " i) ​ ( A)) h_{A}\in\widetilde{QR{H}}^{1+L}_{p"_{i}}(\rho_{0},\rho,v_{i},\widetilde{\nu},(\nu^{\prime})^{(1)},u-u(A),u^{(1)}-u^{(1)}(A),\cdots,u^{(p"_{i})}-u^{(p"_{i})}(A)). Les coordonnées ( v ′) ( 1) (v^{\prime})^{(1)} sont définies comme les coordonnées ( v ′) ( 0) (v^{\prime})^{(0)}.

En tout point b ∈ D 1, i ∖ { a 0 } b\in D_{1,i}\setminus\{a_{0}\}, les champs χ ~ b \widetilde{\chi}_{b} et X p, B {X}_{p,B} (cf. §3.1.1) sont équivalents. Comme dans le paragraphe 1, dont on reprend les notations, on construit une extension de S B | U 1, i, b SB_{|U_{1,i,b}} par adjonction de (fonctions) coordonnées ( ν ′) ( 2) (\nu^{\prime})^{(2)} qui appartiennent à un anneau A. ( V 1, i ′ × V " 1, i) {A}_{.}(V^{\prime}_{1,i}\times V"_{1,i}) d’après (7) et la préparation ci-dessus. Et d’après (8) et le lemme de cohérence I3, si en plus b ∈ U ¯ c, 0, n 0, 1 b\in\overline{U}_{c,0,n_{0,1}}, on a la double inclusion dans cette extension

 | ( ρ 0 m ​ a + + 1 ​ ρ N 0 ​ φ i) ⊂ I χ ~, ρ 0 S 0 ​ f ~, b ⊂ ( φ i) (\rho_{0}^{ma^{+}+1}\rho^{N_{0}}\varphi_{i})\subset{I}_{\widetilde{\chi},\rho_{0}^{S_{0}}\widetilde{f},b}\subset(\varphi_{i}) |  | 9 |

De même, en tout point b ∈ D 1, i ∖ { a 0 } b\in D_{1,i}\setminus\{a_{0}\}, les champs χ ~ b \widetilde{\chi}_{b} et X p ​ " i, B {X}_{p"_{i},B} sont équivalents. On construit donc une extension de cette dernière extension par adjonction de (fonctions) coordonnées ( ν ′) ( 3) ∈ A. ( V 1, i ′ × V " 1, i) (\nu^{\prime})^{(3)}\in{A}_{.}(V^{\prime}_{1,i}\times V"_{1,i}) et on note H H l’image de h h dans cette extension. On a donc sur une restriction adéquate au dessus de D 1, i ∖ { a 0 } D_{1,i}\setminus\{a_{0}\}

 | ρ 0 S 1 ​ f ~ = φ ​ " i ​ H \rho_{0}^{S_{1}}\widetilde{f}=\varphi"_{i}H |  | 10 |

et si b b est voisin de a 0 a_{0}, la double inclusion (9) donne

 | ( ρ 0 S 1 + m ​ a + + 1 ​ ρ N 0 ​ φ i ′) ⊂ I χ ~, H, b (\rho_{0}^{S_{1}+ma^{+}+1}\rho^{N_{0}}\varphi^{\prime}_{i})\subset{I}_{\widetilde{\chi},H,b} |  | 11 |

Or sur D 1, i ∖ { a 0 } D_{1,i}\setminus\{a_{0}\}, la coordonnée u 1 u_{1} ne s’annule pas et on a λ 1, i n i ′ ∈ ( φ i ′) \lambda_{1,i}^{n^{\prime}_{i}}\in(\varphi^{\prime}_{i}). Donc l’inclusion (11) donne

 | ( ρ 0 n 0, 0 ​ ρ N 0) ⊂ I χ ~, H, b (\rho_{0}^{n_{0,0}}\rho^{N_{0}})\subset{I}_{\widetilde{\chi},H,b} |  | 12 |

et par le plongement ci-dessus à l’ordre n 0, 1 n_{0,1}, le germe de H H en tout point de D 1, i D_{1,i} est convergent modulo ( ρ 0 n 0, 1 ​ ρ N 1) (\rho_{0}^{n_{0,1}}\rho^{N_{1}}). Pour conclure, on applique la méthode du lemme de récurrence IVB1 à H H au dessus de D 1, i D_{1,i} et on utilise (10).

3.2 Sur le bord de D k {D}_{k}.

Soit a ∈ D ¯ 1, i ∩ ∂ D k a\in\overline{D}_{1,i}\cap\partial{D}_{k} et k ′ − 1 k^{\prime}-1 la dimension de non trivialitéde la dérivation d’Hilbert en a a. Il reste simplement à nommer les données du lemme en fonction de k ′ k^{\prime}. On pose ρ k ′ ( 1) = ( ρ ( 1), ρ i ′) \rho_{k^{\prime}}^{(1)}=(\rho^{(1)},\rho^{\prime}_{i}), ν ~ k ′ = ( ν ~, v ~ i) \widetilde{\nu}_{k^{\prime}}=(\widetilde{\nu},\widetilde{v}_{i}), ν k ′ = v ​ " i \nu_{k^{\prime}}=v"_{i}, ρ k ′ ( 2) = ( ρ ( 2), ρ ​ " i) \rho_{k^{\prime}}^{(2)}=(\rho^{(2)},\rho"_{i}), ν k ′ ′ = ( ( ( ν ′) ( j)) j = 0, … ​ 4, ( ν j ′)) \nu^{\prime}_{k^{\prime}}=(((\nu^{\prime})^{(j)})_{j=0,\ldots 4},(\nu^{\prime}_{j})) où les (fonctions) coordonnées ( ν ′) ( 4) (\nu^{\prime})^{(4)} proviennent du plongement à l’ordre n 0, 1 n_{0,1} et les ν j ′ \nu^{\prime}_{j} sont déterminés par les rapports τ j, 1 \tau_{j,1} comme dans le paragraphe 2. On pose aussi V k ′ ′ = V 1, i ′ V^{\prime}_{k^{\prime}}=V^{\prime}_{1,i}, V k ′ = V ​ " 1, i V_{k^{\prime}}=V"_{1,i}, N 0, k ′ = ( n 0, 0, …, n 0, 0, N 0) N_{0,k^{\prime}}=(n_{0,0},\ldots,n_{0,0},N_{0}) et N 1, k ′ = ( n 0, 1, …, n 0, 1, N 1) N_{1,k^{\prime}}=(n_{0,1},\ldots,n_{0,1},N_{1}), n 0, 0 n_{0,0} et n 0, 1 n_{0,1} étant répétés p i ′ p^{\prime}_{i} fois. Le reste de la preuve est maintenant classique!∎

Preuve du théorème 0.

Soit ( X ν, Γ k) (X_{\nu},\Gamma_{k}) un déploiement analytique de X 0 X_{0} à q 0 q_{0} paramètres. D’après le théorème VA1 (appendice VA), il existe des transversales analytiques σ j \sigma_{j} et τ j \tau_{j} au voisinage de chaque sommet P j P_{j} tels que l’application de Dulac du coin P j P_{j} soit induite par un élément d j ∈ Q ​ R ​ H 1, ( 1, q 0) ​ ( x j, μ j, ν) d_{j}\in QR{H}^{1,(1,q_{0})}(x_{j},\mu_{j},\nu). Posons α = ( μ 1, …, μ k, ν) = ( μ, ν) \alpha=(\mu_{1},\ldots,\mu_{k},\nu)=(\mu,\nu) et q = ( q 1, q 2) = ( k, q 0) q=(q_{1},q_{2})=(k,q_{0}). Soient λ j ​ ( ν) \lambda_{j}(\nu) les germes qui déploient les connexions γ j, j + 1 \gamma_{j,j+1}. Les cycles du champ X ν X_{\nu} proches de Γ k \Gamma_{k} rencontrent les transversales σ j \sigma_{j} aux points dont les abscisses x j x_{j} sont solutions du système

 | d 1 ​ ( x 1, α ⁡ ( ν)) − f 2 ​ ( x 2, α ⁡ ( ν)) = λ 1 ​ ( ν), …, d k ​ ( x k, α ⁡ ( ν)) − f 1 ​ ( x 1, α ⁡ ( ν)) = λ k ​ ( ν) d_{1}(x_{1},\alpha(\nu))-f_{2}(x_{2},\alpha(\nu))=\lambda_{1}(\nu),\ldots,d_{k}(x_{k},\alpha(\nu))-f_{1}(x_{1},\alpha(\nu))=\lambda_{k}(\nu) |  | 13 |

les germes f j f_{j} étant des difféomorphismes analytiques dans la variable x j x_{j} qui préservent l’origine et l’orientation. Par la réduction de la partie A, le système (13) est équivalent au système

 | d 1 ​ ( x 1, α ⁡ ( ν)) − x 2 = λ 1 ​ ( ν), …, d k ​ ( x k, α ⁡ ( ν)) − x 1 = λ k ​ ( ν) d_{1}(x_{1},\alpha(\nu))-x_{2}=\lambda_{1}(\nu),\ldots,d_{k}(x_{k},\alpha(\nu))-x_{1}=\lambda_{k}(\nu) |  |

Posons x = ( x 1, …, x k) x=(x_{1},\ldots,x_{k}) et λ = ( λ 1, …, λ k − 1) \lambda=(\lambda_{1},\ldots,\lambda_{k-1}). Soit χ ∈ Ξ ​ H k ​ [Q ​ R ​ H k, q] \chi\in\Xi{H}_{k}[QR{H}^{k,q}] dont ( k − 1) (k-1) intégrales non triviales sont g j ​ ( x j, x j + 1, α) = d j ​ ( x j, α) − x j + 1 g_{j}(x_{j},x_{j+1},\alpha)=d_{j}(x_{j},\alpha)-x_{j+1}. Soit W 0 W_{0} l’image d’un voisinage de 0 0 dans ℝ q 0 \mathbb{R}^{q_{0}} par l’immersion ν ↦ ( α ⁡ ( ν), λ ⁡ ( ν)) \nu\mapsto(\alpha(\nu),\lambda(\nu)) et soit U 0 = π χ − 1 ​ ( W 0) U_{0}=\pi_{\chi}^{-1}(W_{0}). Soit f ⁡ ( x, α) = d k ​ ( x k, α) − x 1 − λ k ​ ( ν) f(x,\alpha)=d_{k}(x_{k},\alpha)-x_{1}-\lambda_{k}(\nu). Alors la partie ( i) (i) du théorème est équivalente à la χ \chi -régularité de f f sur U 0 U_{0} et la partie ( i ​ i) (ii) est vérifiée si l’idéal différentiel I χ, f I_{\chi,f} est localement noethérien sur U 0 U_{0} (à extensions étoilées près). Le théorème 0 est donc une conséquence simple du théorème IVC1 ci-dessus.∎

Appendice V.

A. Déploiements d’applications de Dulac.

Il est connu ( [E] et [I] ) que l’application de Dulac d’une singularité hyperbolique réelle est un élément de Q ​ A 1, 0 QA^{1,0}. Un théorème de [M-M] dit que l’application de Dulac est ”convergente” si et seulement si la singularité est analytiquement normalisable. Ceci limite considérablement le champ d’application des arguments classiques de la géométrie analytique et justifie l’approche quasi-analytique adoptée qui prolonge celles d’Ecalle et d’Il’yashenko.

On se limitera au cas d’une équation différentielle résonnante de nombre caractéristique r = 1 r=1; le cas r = n / m r=n/m s’en déduit par une double ramification et le cas quasi-résonnant présente moins de difficulté. Soit ω ν = x ​ d ​ y + y ⁡ ( 1 + μ ⁡ ( ν) + a ⁡ ( x, y, ν)) ​ d ​ x \omega_{\nu}=xdy+y(1+\mu(\nu)+a(x,y,\nu))dx un déploiement analytique à q q paramètres ν = ( ν 1, …, ν q) \nu=(\nu_{1},\ldots,\nu_{q}) d’une 1-forme analytique réelle résonnante. Ce déploiement est induit par le déploiement

 | ω α = x ​ d ​ y + y ⁡ ( 1 + μ + a ⁡ ( x, y, ν)) ​ d ​ x \omega_{\alpha}=xdy+y(1+\mu+a(x,y,\nu))dx |  |

avec α = ( μ, ν) ∈ W 1 × W q ∈ ( ℝ, 0) × ( ℝ q, 0) \alpha=(\mu,\nu)\in W_{1}\times W_{q}\in({{\mathbb{\mathbb{R}}}},0)\times({{\mathbb{\mathbb{R}}}}^{q},0). On pose r = 1 + μ r=1+\mu. L’objet de cette partie est le

###### Théorème VA1

Soit d (., α) d(.,\alpha) l’application de Dulac de ω α \omega_{\alpha}, alors il existe D ∈ Q ​ R ​ H 1, ( 1, q) D\in QR{H}^{1,(1,q)} tel que d = x r ​ ( 1 + D) d=x^{r}(1+D) et D ⁡ ( 0) = 0 D(0)=0.

La propriété de quasi-analycité a été démontrée dans [E-M-R] sur des domaines de E ​ I {E}{I} de type puissance

 | { w = u + i v; | v | < C u n; u ≫ 1 }, C > 0, n ≥ 2 \{w=u+iv;\quad|v|<Cu^{n};\quad u\gg 1\},\quad C>0,\quad n\geq 2 |  | 1 |

en utilisant l’idée géomètrique d’Il’yashenko [I] basée sur la structure de l’holonomie de l’une des séparatrices. Or les domaines de E ​ I {E}{I} qui s’imposent naturellement dans le problème sont les domaines qui sont optimaux pour les formes normales; i.e les domaines d’Ecalle [E] de type exponentiel

 | { w = u + i v; | v | < C exp ( u / K) − 1; u ≫ 1 }, C > 0, K > 1 \{w=u+iv;\quad|v|<C\exp(u/K)-1;\quad u\gg 1\},\quad C>0,\quad K>1 |  | 2 |

On adopte une démarche qui combine l’idée géomètrique d’Il’yashenko en modifiant les chemins d’intégration, et celle de Dulac [D] qui consiste à construire une intégrale première analytique dans l’une des variables. On suppose que ω α \omega_{\alpha} est préparée à l’ordre 1

 | a = x ​ y ​ ∑ n ≥ 1 a n ​ ( x, ν) ​ y n − 1 a=xy\sum_{n\geq 1}a_{n}(x,\nu)y^{n-1} |  | 3 |

et qu’on a la majoration suivante

 | ∑ n ≥ 1 ‖ a n ‖ D ¯ ​ ( 0, 1) × 𝕎 q ≤ 1 / 4 \sum_{n\geq 1}\|a_{n}\|_{\overline{D}(0,1)\times{{\mathbb{W}}}_{q}}\leq 1/4 |  | 4 |

où 𝕎 q {{\mathbb{W}}}_{q} est le complexifié de W q W_{q}. Soit

 | f ⁡ ( x, y, α) = ∑ n ≥ 1 f n ​ ( x, α) ​ y n f(x,y,\alpha)=\sum_{n\geq 1}f_{n}(x,\alpha)y^{n} |  | 5 |

l’intégrale première de ω α \omega_{\alpha} telle que f ⁡ ( 1, y, α) ≡ y f(1,y,\alpha)\equiv y. L’application de Dulac de ω α \omega_{\alpha} est analytiquement conjuguée à

 | d ⁡ ( x, α) = f ⁡ ( x, 1 / 2, α) d(x,\alpha)=f(x,1/2,\alpha) |  | 6 |

et le théorème est conséquence de la

###### Proposition VA1

Il existe F ∈ Q ​ R ​ H 1, ( 1, q + 1) F\in QR{H}^{1,(1,q+1)} tel que f = x r ​ y ​ ( 1 + F) ​ et ​ F ​ ( 0) = 0 f=x^{r}y(1+F)\text{ et }F(0)=0.

§1. Opérateur intégral de Dulac.

Notons P + = { w ∈ ℂ; Re ( w) > 0 } P^{+}=\{w\in{{\mathbb{\mathbb{C}}}};\quad\text{Re}(w)>0\}. Soit Ω \Omega un ouvert simplement connexe de P + P^{+} tel que 0 ∈ Ω ¯ 0\in\overline{\Omega} et H c ​ ( Ω) H_{c}(\Omega) l’espace des fonctions holomorphes sur Ω \Omega et continues sur Ω ¯ \overline{\Omega}. Pour tout s ∈ ℂ ∗ s\in{{{\mathbb{\mathbb{C}}}}}^{*}, on définit sur H c ​ ( Ω) H_{c}(\Omega) l’opérateur L s {L}_{s} par

 | L s ​ ( f) ​ ( w) = s ​ exp ⁡ ( − s ​ w) ​ ∫ γ w exp ⁡ ( ( s − 1) ​ z) ​ f ​ ( z) ​ 𝑑 z {L}_{s}(f)(w)=s\exp(-sw)\int_{\gamma_{w}}\exp((s-1)z)f(z)dz |  | 7 |

où γ w ⊂ Ω \gamma_{w}\subset\Omega est un chemin C 1 {C}^{1} régulier joignant 0 0 et w w. Pour s s fixé, l’ensemble L s = { w ∈ P +; Re ( s w) = 0 } L_{s}=\{w\in P^{+};\quad\text{Re}(sw)=0\} est dit direction singulière de l’operateur L s {L}_{s} et Ω s = { w ∈ P +; Re ​ ( s ​ w) > 0 } \Omega_{s}=\{w\in P^{+};\text{ Re}(sw)>0\} est dit domaine non-singulier de L s {L}_{s}. On montre que, sous une certaine condition géomètrique sur le chemin γ w \gamma_{w}, et donc sur l’ouvert Ω \Omega, l’opérateur L s {L}_{s} est 2-lipschitzien.

###### Lemme VA1

Si Ω ⊂ Ω s \Omega\subset\Omega_{s} et si le long du chemin γ w \gamma_{w} la condition suivante est satisfaite

 | | tan ⁡ ( arg ⁡ ( s ​ d ​ z d ​ t)) | ≤ | exp ⁡ ( z) | |\tan(\arg(s\frac{dz}{dt}))|\leq|\exp(z)| |  | 8 |

alors pour tout f ∈ H c ​ ( Ω) f\in H_{c}(\Omega)

 | | L s ​ ( f) ​ ( w) | ≤ 2 ​ ‖ f ‖ γ w |{L}_{s}(f)(w)|\leq 2\|f\|_{\gamma_{w}} |  | 9 |

Preuve. Soit t 0 t_{0} tel que z ⁡ ( t 0) = w z(t_{0})=w. Grâce à (8), on a la majoration

 | | L s ( f) ( w) | ≤ 2 ∥ f ∥ γ w | exp ( − s w) | ∫ 0 t 0 | Re ( s z ′) | exp ( Re ( s z)) d t |{L}_{s}(f)(w)|\leq 2\|f\|_{\gamma_{w}}|\exp(-sw)|\int_{0}^{t_{0}}|\text{Re}(sz^{{}^{\prime}})|\exp(\text{Re}(sz))dt |  |

le chemin γ w \gamma_{w} étant C 1 {C}^{1} -régulier, la condition (8) implique que la fonction Re ​ ( s ​ z ′) \text{Re}(sz^{\prime}) ne s’annule pas sur γ w \gamma_{w}. Et comme Ω ⊂ Ω s \Omega\subset\Omega_{s}, le résultat en découle facilement.∎

§2. Preuve de la proposition.

C’est une conséquence du lemme VA1 et des lemmes ci-dessous. Les coefficients f n f_{n} de la série de f f vérifient les équations différentielles

 | x ​ ∂ f n ∂ x − n ​ r ​ f n = x ​ ∑ p = 1 n − 1 p ​ a n − p ​ f p et f 1 = x r x\frac{\partial f_{n}}{\partial x}-nrf_{n}=x{\sum}_{p=1}^{n-1}pa_{n-p}f_{p}\quad\text{ et }\quad f_{1}=x^{r} |  |

Il est clair que chaque fonction f n f_{n} est holomorphe, mais n’est pas forcément bornée sur P + × 𝕎 q + 1 P^{+}\times{\mathbb{W}}_{q+1}. Pour n > 1 n>1, posons

 | h n = − 1 n ​ r ∑ p = 1 n − 1 p a n − p f p h_{n}=-\frac{1}{nr}{\sum}_{p=1}^{n-1}pa_{n-p}f_{p} |  |

alors, les coefficients f n f_{n} sont donnés par

 | f n = L n ​ r ​ ( h n) f_{n}={L}_{nr}(h_{n}) |  |

et d’après (4) on obtient

 | ‖ h n ‖ ∗ ≤ 1 2 ​ max 1 ≤ p ≤ n − 1 ​ ‖ f p ‖ ∗ \|h_{n}\|_{*}\leq\frac{1}{2}\max_{1\leq p\leq n-1}\|f_{p}\|_{*} |  |

où ∗ *est un domaine qui dépendra du contexte. De même, soit F n = f n / f 1 F_{n}=f_{n}/f_{1} les coefficients de la série de 1 + F 1+F et

 | H n = − 1 ( n − 1) ​ r ∑ p = 1 n − 1 p a n − p F p H_{n}=-\frac{1}{(n-1)r}\sum_{p=1}^{n-1}pa_{n-p}F_{p} |  |

alors, on a

 | F n = L ( n − 1) ​ r ​ ( H n) F_{n}={L}_{(n-1)r}(H_{n}) |  |

En particulier, la fonction élémentaire z ⁡ ( x, μ) = x ​ Ld ​ ( x, μ) z(x,\mu)=x\text{Ld}(x,\mu) est donnée par

 | z = L r ​ ( − 1 r) z={L}_{r}(-\frac{1}{r}) |  |

###### Lemme VA2

Les germes de f f et F F sont des éléments de S ​ B 1, q + 2 SB^{1,q+2}.

Preuve. Le domaine non-singulier de l’opérateur L n ​ r {L}_{nr} coincide avec Ω r \Omega_{r}. Soit θ ∈] 0, π / 2 [\theta\in]0,\pi/2[et S θ = { w ∈ P +; | arg ( w) | ≤ θ } S_{\theta}=\{w\in P^{+};\quad|\arg(w)|\leq\theta\}. Si arg ⁡ ( r) \arg(r) est suffisament petit, le secteur S θ S_{\theta} est inclus dans Ω r \Omega_{r}. Soit u 0 > 0 u_{0}>0 tel que

 | exp ⁡ ( u 0) ≫ tan ⁡ ( θ) \exp(u_{0})\gg\tan(\theta) |  | 10 |

et w 0 ∈ S θ w_{0}\in S_{\theta} tel que

 | arg ⁡ ( w 0) = θ et arg ⁡ ( w 0 − u 0) ∼ θ \arg(w_{0})=\theta\quad\text{ et }\quad\arg(w_{0}-u_{0})\sim\theta |  | 11 |

Soit S 0, θ = S θ ∩ ( S arg ⁡ ( w 0 − u 0) + u 0) S_{0,\theta}=S_{\theta}\cap(S_{\arg(w_{0}-u_{0})}+u_{0}). On joint w ∈ S 0, θ w\in S_{0,\theta} à 0 0 par un chemin C 1 {C}^{1} -régulier voisin du chemin γ w = [0, u 0] ∪ [u 0, w] \gamma_{w}=[0,u_{0}]\cup[u_{0},w] qui satisfait à la condition (8) du lemme VA1 grâce à (10) et (11). D’où le résultat.∎

Chemins exponentiels. Pour tout u 0 ≥ 1 u_{0}\geq 1 et K ≥ 1 K\geq 1, notons

 | V u 0, K = { w = u 0 + u + i v ∈ P +; u ≥ 0, | v | ≤ exp ( u / K) − 1 } V_{u_{0},K}=\{w=u_{0}+u+iv\in P^{+};\quad u\geq 0,\quad|v|\leq\exp(u/K)-1\} |  |

On joint un élément w ∈ V u 0, K w\in V_{u_{0},K} à 0 0 par le chemin

 | γ w = [0, u 0] ∪ { z = u 0 + u + i C ( exp ( u / K) − 1); u ∈ [0, Re ( w) − u 0] } \gamma_{w}=[0,u_{0}]\cup\{z=u_{0}+u+iC(\exp(u/K)-1);\quad u\in[0,\text{ Re}(w)-u_{0}]\} |  |

où C ∈ [− 1, 1] C\in[-1,1] est une constante qui ne dépend que de w w. Par un calcul simple, il existe M ⁡ ( K) > 0 M(K)>0 tel que pour tout u 0 ≥ 1 u_{0}\geq 1 et sur tout chemin exponentiel

 | | z ′ ​ ( u) z ⁡ ( u) | ≤ M ⁡ ( K) |\frac{z^{\prime}(u)}{z(u)}|\leq M(K) |  | 12 |

###### Lemme VA3

Le germe de f f est un élément de Q ​ A OPEN 1, q + 2) QA^{1,q+2)}.

Preuve. Montrons que f f satisfait à la condition de quasi-analycité. Remarquons d’abord que si r r est réel, le domaine non-singulier de l’opérateur L n ​ r {L}_{nr} est P + P^{+}. Les chemins γ w \gamma_{w} de V 1, 1 V_{1,1} satisfont clairement à la condition (8) du lemme VA1.

Soit φ 0 \varphi_{0} le morphisme d’éclatement du point ( ∞, 0) (\infty,0) de P + × ℂ P^{+}\times{{\mathbb{\mathbb{C}}}} dans la direction réelle 0 0 de ℝ ​ P 1 {{\mathbb{\mathbb{R}}}}P^{1}

 | φ 0: ( w, μ ~) ↦ μ = μ ~ w + 1 \varphi_{0}:\quad(w,\widetilde{\mu})\mapsto\mu=\frac{\widetilde{\mu}}{w+1} |  | 13 |

et soit Φ 0 \Phi_{0} l’application

 | Φ 0 ​ ( w, y, μ ~, ν) = ( w, y, φ 0 ​ ( w, μ ~), ν). \Phi_{0}(w,y,\widetilde{\mu},\nu)=(w,y,\varphi_{0}(w,\widetilde{\mu}),\nu). |  | 14 |

Soit K > 1 K>1. Si 𝕎 ~ 1 ∈ ( ℂ, 0) \widetilde{{{\mathbb{W}}}}_{1}\in({{\mathbb{\mathbb{C}}}},0) est suffisament petit, les projections sur [0, 1] ∪ V 1, K [0,1]\cup V_{1,K} des fibres φ 0 − 1 ​ ( μ) \varphi^{-1}_{0}(\mu) de ( [0, 1] ∪ V 1, K) × 𝕎 ~ 1 ([0,1]\cup V_{1,K})\times\widetilde{{{\mathbb{W}}}}_{1} contiennent les sous-ensembles

 | Δ μ ( w) = { z ∈ [0, 1] ∪ V 1, K; Re ( z) ≤ Re ( w), | z | ≤ | w | } \Delta_{\mu}(w)=\{z\in[0,1]\cup V_{1,K};\quad\text{ Re}(z)\leq\text{ Re}(w),\quad|z|\leq|w|\} |  | 15 |

qui sont inclus dans le domaine non-singulier Ω r \Omega_{r} des opérateurs L n ​ r {L}_{nr}. En effet, si z ∈] 0, 1] z\in]0,1], on a Re ​ ( r ​ z) = z ​ Re ​ ( r) > 0 \text{Re}(rz)=z\text{Re}(r)>0 et si z ∈ V 1, K z\in V_{1,K}

 | Re ​ ( r ​ z) = Re ​ ( z) + Re ​ ( μ ~ w + 1 ​ z) > 0 \text{Re}(rz)=\text{Re}(z)+\text{Re}(\frac{\widetilde{\mu}}{w+1}z)>0 |  |

Soit u 0 > 1 u_{0}>1. Les chemins γ w \gamma_{w} de [0, u 0] ∪ V u 0, K [0,u_{0}]\cup V_{u_{0},K} sont inclus dans Δ μ ​ ( w) \Delta_{\mu}(w) et satisfont à la condition (8) du lemme VA1 si u 0 u_{0} est suffisament grand. En effet, elle est clairement satisfaite sur le segment réel. Sur le chemin exponentiel

 | r ​ z ′ = z ′ + μ ​ z ​ z ′ z rz^{\prime}=z^{\prime}+\mu z\frac{z^{\prime}}{z} |  |

et d’après (12)

 | | Im ​ ( r ​ z ′) Re ​ ( r ​ z ′) | ≤ exp ⁡ ( u 0 + u) |\frac{\text{Im}(rz^{\prime})}{\text{Re}(rz^{\prime})}|\leq\exp(u_{0}+u) |  |

Soit D ⁡ ( 0, ρ) ¯ \overline{D(0,\rho)} un disque de 𝕎 ~ 1 \widetilde{{\mathbb{W}}}_{1}. Soit f ~ \widetilde{f}, F ~ \widetilde{F} et f ~ 1 \widetilde{f}_{1} les relevés par Φ 0 \Phi_{0} de f f, F F et f 1 f_{1}. On a donc

 | ‖ 1 + F ~ ‖ V u 0, K × D ⁡ ( 0, 1 / 2) ¯ × D ⁡ ( 0, ρ) ¯ × 𝕎 q ≤ C 0 ||1+\widetilde{F}||_{V_{u_{0},K}\times\overline{D(0,1/2)}\times\overline{D(0,\rho)}\times{\mathbb{W}}_{q}}\leq C_{0} |  |

et

 | | | f ~ 1 ( w,.) | | D ⁡ ( 0, ρ) ¯ ≤ C 1 | exp ( − w) | ||\widetilde{f}_{1}(w,.)||_{\overline{D(0,\rho)}}\leq C_{1}|\exp(-w)| |  |

par conséquent

 | | | f ~ ( w,.) | | D ⁡ ( 0, 1 / 2) ¯ × D ⁡ ( 0, ρ) ¯ × 𝕎 q ≤ C 2 | exp ( − w) | ||\widetilde{f}(w,.)||_{\overline{D(0,1/2)}\times\overline{D(0,\rho)}\times{\mathbb{W}}_{q}}\leq C_{2}|\exp(-w)| |  |

Par les formules intégrales de Cauchy sur D ⁡ ( 0, ρ) ¯ \overline{D(0,\rho)}, les coefficients de la série f ~ = ∑ k ≥ 0 c ~ k ​ μ ~ k \widetilde{f}={\sum}_{k\geq 0}\widetilde{c}_{k}\widetilde{\mu}^{k} admettent les majorations

 | | | c ~ k ( w,.) | | D ⁡ ( 0, 1 / 2) ¯ × 𝕎 q ≤ C k | exp ( − w) | ||\widetilde{c}_{k}(w,.)||_{\overline{D(0,1/2)}\times{\mathbb{W}}_{q}}\leq C_{k}|\exp(-w)| |  |

Soit maintenant f = ∑ k ≥ 0 c k ​ μ k f={\sum}_{k\geq 0}c_{k}\mu^{k} la série de f f. On a c k = ( w + 1) k ​ c ~ k c_{k}=(w+1)^{k}\widetilde{c}_{k} et donc chaque coefficient c k c_{k} est borné sur le domaine V u 0, k + 1 V_{u_{0},k+1}. On conclut en remarquant que le complémentaire de ces domaines dans n’importe quel domaine de type puissance, est une partie relativement compact.∎

###### Lemme VA4

Le germe de F F est un élément de Q ​ R ​ H 1, ( 1, q + 1) QR{H}^{1,(1,q+1)}.

Preuve. La démarche est classique ([I-Y], [M], [Ro2] ) pour la partie concernant la structure asymptotique formelle de type Hilbert. Elle utilise les formes prénormales de ω α \omega_{\alpha}. Les propriétés du reste découlent d’une deuxième application des opérateurs intégrals de Dulac.

On prépare analytiquement ω α \omega_{\alpha} à un certain ordre 2 ​ N > 1 2N>1 par un difféomorphisme qui préserve la coordonnée x x

 | a ( x, y, α) = ∑ n ≥ 1 a n ( x, α) y n avec a n = { x n ​ a ~ n ​ ( α) pour n ≤ 2 ​ N x 2 ​ N + 1 ​ a ~ n ​ ( x, α) pour n > 2 ​ N a(x,y,\alpha)=\sum_{n\geq 1}a_{n}(x,\alpha)y^{n}\quad\text{avec}\quad a_{n}=\left\{\begin{aligned} x^{n}\widetilde{a}_{n}(\alpha)&\text{ pour}\quad n\leq 2N\\ x^{2N+1}\widetilde{a}_{n}(x,\alpha)&\text{ pour}\quad n>2N\end{aligned}\right. |  |

Soit f 1, N f_{1,N} l’intégrale première de la forme prénormale

 | ω α, N = x ​ d ​ y + y ⁡ ( 1 + μ + ∑ n = 1 2 ​ N a n ​ ( x, α) ​ y n) ​ d ​ x \omega_{\alpha,N}=xdy+y(1+\mu+{{\sum}}_{n=1}^{2N}a_{n}(x,\alpha)y^{n})dx |  | 16 |

telle que f 1, N ​ ( 1, y, α) ≡ y f_{1,N}(1,y,\alpha)\equiv y. Il est connu ([I-Y] par exemple) qu’il existe F 1, N ∈ Q ​ R ​ H cvg 1, ( 1, q + 1) F_{1,N}\in QR{H}^{1,(1,q+1)}_{\text{cvg}} telle que

 | f 1, N = x r ​ y ​ ( 1 + F 1, N) et F 1, N ​ ( 0) = 0 f_{1,N}=x^{r}y(1+F_{1,N})\quad\text{ et }\quad F_{1,N}(0)=0 |  |

En effet, dans le morphisme Φ α ​ ( x, y) = ( x 1, y 1) = ( x ​ y, z ⁡ ( x, μ) ​ y) \Phi_{\alpha}(x,y)=(x_{1},y_{1})=(xy,z(x,\mu)y), la 1-forme ω α, N \omega_{\alpha,N} se désingularise en

 | ω ~ α, N = ( μ + ∑ n = 1 N a ~ n ​ x 1 n) ​ d ​ y 1 + ( 1 − y 1 ​ ∑ n = 1 N a ~ n ​ x 1 n − 1) ​ d ​ x 1 \widetilde{\omega}_{\alpha,N}=(\mu+{{\sum}}_{n=1}^{N}\widetilde{a}_{n}x_{1}^{n})dy_{1}+(1-y_{1}{{\sum}}_{n=1}^{N}\widetilde{a}_{n}x_{1}^{n-1})dx_{1} |  |

et cette 1-forme admet une intégrale première analytique g g qui vérifie g ⁡ ( x 1, 0, α) = x 1 g(x_{1},0,\alpha)=x_{1}. Soit g 0 = x 1 + μ ​ y 1 g_{0}=x_{1}+\mu y_{1} l’intégrale première de la partie linéaire. Par un calcul simple

 | d ​ g 0 ∧ ω ~ α, N = g 0 ​ ∑ n = 1 N a ~ n ​ x 1 n − 1 ​ d ​ x 1 ∧ d ​ y 1 dg_{0}\wedge\widetilde{\omega}_{\alpha,N}=g_{0}\sum_{n=1}^{N}\widetilde{a}_{n}x_{1}^{n-1}dx_{1}\wedge dy_{1} |  |

et ceci montre que g g est divisible par g 0 g_{0}.

Soit Ψ α ​ ( x, y) = ( X, Y) \Psi_{\alpha}(x,y)=(X,Y) le changement de coordonnées ramifié

 | { X = x Y = y ⁡ ( 1 + F 1, N) \left\{\begin{aligned} X&=x\\ Y&=y(1+F_{1,N})\end{aligned}\right. |  | 17 |

la fonction f 1, N f_{1,N} étant une intégrale première de ω α, N \omega_{\alpha,N}, la 1-forme ramifiée η α = ( Ψ α − 1) ∗ ​ ω α \eta_{\alpha}=(\Psi_{\alpha}^{-1})^{*}\omega_{\alpha} s’écrit

 | η α = X ​ d ​ Y + Y ⁡ ( r + ( X ​ Y) 2 ​ N + 1 ​ b ​ ( X, Y, α)) ​ d ​ X \eta_{\alpha}=XdY+Y(r+(XY)^{2N+1}b(X,Y,\alpha))dX |  |

avec b ∈ Q ​ R ​ H cvg 1, ( 1, q + 1) b\in QR{H}^{1,(1,q+1)}_{\text{cvg}}. Soit f 2, N f_{2,N} l’intégrale première de η α \eta_{\alpha} telle que f 2, N ​ ( 1, Y, α) ≡ Y f_{2,N}(1,Y,\alpha)\equiv Y. Soit Ψ ⁡ ( x, y, α) = ( Ψ α ​ ( x, y), α) \Psi(x,y,\alpha)=(\Psi_{\alpha}(x,y),\alpha). L’intégrale première f f de ω α \omega_{\alpha} est donnée par

 | f = f 2, N ∘ Ψ f=f_{2,N}\circ\Psi |  |

Or il est facile de voir que f 2, N f_{2,N} s’écrit

 | f 2, N = X r ​ Y ​ ( 1 + X N ​ H N) f_{2,N}=X^{r}Y(1+X^{N}H_{N}) |  | 18 |

On montre alors que H N = ∑ n > 2 ​ N h n ​ Y n H_{N}=\sum_{n>2N}h_{n}Y^{n} est un élément de S ​ B 1, q + 2 SB^{1,q+2} (et même de Q ​ A 1, q + 2 QA^{1,q+2}), en appliquant la méthode des lemmes précédents aux coefficients h n h_{n} par l’intermédiaire des opérateurs L ( n − 1) ​ r − N {L}_{(n-1)r-N} sur le domaine non-singulier Ω 2 ​ r − 1 \Omega_{2r-1}. Ceci implique en particulier que F ∈ Q ​ A 1, q + 2 F\in QA^{1,q+2} (pour un bon choix de N N), et donc que F ∈ Q ​ R ​ H 1, ( 1, q + 1) F\in QR{H}^{1,(1,q+1)} ∎

§3. Remarque VA1.

On peut construire des chemins sur les feuilles de ω α \omega_{\alpha} qui ne quittent pas un certain voisinage de 0 0, par exemple D ⁡ ( 0, 1) × D ⁡ ( 0, 1) D(0,1)\times D(0,1), et qui rencontrent une seule fois chacune des transversales { x = 1 } \{x=1\} et { y = 1 } \{y=1\}. En effet, soit Y = y ⁡ ( 1 + F) Y=y(1+F). D’après l’étude précédente

 | c 1 | y | ≤ | | Y (., y,.) | | V × W 1 × 𝕎 q ≤ c 2 | y | c_{1}|y|\leq||Y(.,y,.)||_{V\times W_{1}\times{\mathbb{W}}_{q}}\leq c_{2}|y| |  | 19 |

Soit y 0 < c 1 / c 2 y_{0}<c_{1}/c_{2}. L’intégration réelle au dessus du segment [1, y 0] [1,y_{0}] est presque une translation réelle dans la coordonnée w w. Maintenant, en utilisant (19) et l’intégrale première x r ​ Y x^{r}Y de la partie linéaire de ω α \omega_{\alpha}, on montre que l’intégration au dessus des chemins γ w \gamma_{w} ne quitte pas le voisinage D ⁡ ( 0, 1) × D ⁡ ( 0, 1) D(0,1)\times D(0,1).

B. Les théorèmes de division.

Ils sont basés sur l’algorithme de division d’Hironaka [B-M]. Rappelons quelques résultats de ce travail: soit a ∈ ℝ ​ { α } a\in{\mathbb{\mathbb{R}}}\{\alpha\} avec α = ( α 1, …, α q) \alpha=(\alpha_{1},\ldots,\alpha_{q}). On note e L ​ ( a) e_{L}(a) le plus petit indice m ∈ ℕ q m\in{\mathbb{\mathbb{N}}}^{q} de coefficient non nul dans la série

 | a = ∑ m a m ​ α m a=\sum_{m}a_{m}\alpha^{m} |  |

les éléments de ℕ q {\mathbb{\mathbb{N}}}^{q} étant ordonnés par l’ordre lexicographique ( L ⁡ ( m), m 1, …, m q) (L(m),m_{1},\ldots,m_{q}) où L ⁡ ( m) = ∑ j λ j ​ m j L(m)=\sum_{j}\lambda_{j}m_{j} est une forme linéaire positive. Soit J J un idéal de ℝ ​ { α } {\mathbb{\mathbb{R}}}\{\alpha\} et N ( J) = { e L ( a); a ∈ J } N(J)=\{e_{L}(a);\quad a\in J\} son diagramme des exposants initiaux. Il existe une liste minimale m 1, …, m l ∈ ℕ q m^{1},\ldots,m^{l}\in{\mathbb{\mathbb{N}}}^{q} telle que

 | N ( J) = ∪ i = 1 l { m i + ℕ q } N(J)=\cup_{i=1}^{l}\{m^{i}+{\mathbb{\mathbb{N}}}^{q}\} |  |

On définit une partition de ℕ q {\mathbb{\mathbb{N}}}^{q} par

 | Δ 1 = m 1 + ℕ q Δ i = m i + ℕ q − ∪ k = 1 i − 1 Δ k et Δ = ℕ q − ∪ i = 1 l Δ i \Delta_{1}=m^{1}+{\mathbb{\mathbb{N}}}^{q}\quad\Delta_{i}=m^{i}+{\mathbb{\mathbb{N}}}^{q}-\cup_{k=1}^{i-1}\Delta_{k}\quad\text{et}\quad\Delta={\mathbb{\mathbb{N}}}^{q}-\cup_{i=1}^{l}\Delta_{i} |  |

alors

 | f = ∑ i = 1 l Q i ​ a i + R Q i, R ∈ ℝ ⁡ { α } f=\sum_{i=1}^{l}Q_{i}a_{i}+R\qquad Q_{i},\ R\in{\mathbb{\mathbb{R}}}\{\alpha\} |  |

 | m i + Supp ​ ( Q i) ⊂ Δ i et Supp ​ ( R) ⊂ Δ m^{i}+\text{Supp}(Q_{i})\subset\Delta_{i}\quad\text{et}\quad\text{Supp}(R)\subset\Delta |  |

La partie analytique de cette algorithme fournit des estimations précises: soit L L une forme linéaire positive, σ > 0 \sigma>0 et

 | ℝ { α } L, σ = { f = ∑ m f m α m; | | f | | L, σ < ∞ } avec | | f | | L, σ = ∑ | f m | σ L ⁡ ( m) {\mathbb{\mathbb{R}}}\{\alpha\}_{L,\sigma}=\{f=\sum_{m}f_{m}\alpha^{m};\quad||f||_{L,\sigma}<\infty\}\quad\text{avec}\quad||f||_{L,\sigma}=\sum|f_{m}|\sigma^{L(m)} |  |

alors il existe L L et ε > 0 \varepsilon>0 tels que si f ∈ ℝ ​ { α } L, σ f\in{\mathbb{\mathbb{R}}}\{\alpha\}_{L,\sigma} et σ ≤ ε \sigma\leq\varepsilon

 | ‖ Q i ​ ( f) ‖ L, σ ≤ 2 σ L ⁡ ( m i) | | f | | L, σ et ‖ R ⁡ ( f) ‖ L, σ ≤ 2 | | f | | L, σ ||Q_{i}(f)||_{L,\sigma}\leq\frac{2}{\sigma^{L(m^{i})}}||f||_{L,\sigma}\quad\text{et}\quad||R(f)||_{L,\sigma}\leq 2||f||_{L,\sigma} |  |

Soit Ω ∈ E ​ I \Omega\in{E}{I} un domaine quasi-analytique et Q ​ A 1, q ​ [Ω] ⊂ Q ​ A 1, q QA^{1,q}[\Omega]\subset QA^{1,q} l’algèbre des germes f = ∑ f m ​ ( x) ​ α m f=\sum f_{m}(x)\alpha^{m} dont les coefficients f m f_{m} admettent un prolongement holomorphe et borné sur Ω \Omega. Pour l’action de χ 0 = x ∂ / ∂ x \chi_{0}=x\partial/\partial x sur ces algèbres, on a le

###### Théorème VB1 (théorème de de division 1)

Soit B = Q ​ A 1, q ​ [Ω] {B}=QA^{1,q}[\Omega] ou S ​ B 1, q SB^{1,q} et J J un idéal de ℝ ​ { α } {\mathbb{\mathbb{R}}}\{\alpha\}. Soit a 1, …, a l a_{1},\ldots,a_{l} une base de J J. Alors pour tout f ∈ B f\in{B}, il existe de manière unique Q i, R ∈ B Q_{i},\ R\in{B} tels que

 | f = ∑ i Q i ​ a i + R f=\sum_{i}Q_{i}a_{i}+R |  |

 | m i + Supp ( Q i ( x,.)) ⊂ Δ i Supp ( R ( x,.)) ⊂ Δ m^{i}+\text{Supp}(Q_{i}(x,.))\subset\Delta_{i}\qquad\text{Supp}(R(x,.))\subset\Delta |  |

La partie formelle de cet algorithme implique le

###### Lemme VB1

Soit f = ∑ m f m ​ α m ∈ B f=\sum_{m}f_{m}\alpha^{m}\in{B}. Si pour tout m m, on a f m = o ⁡ ( x n) f_{m}=o(x^{n}) (dans l’anneau S ​ B 1, q SB^{1,q}), alors il en est de même pour les séries des Q i Q_{i} et de R R.

Soit s ∈ ℕ ∗ s\in\mathbb{N}^{*} et soit la dérivation

 | χ = x ​ ∂ ∂ x − s ​ ∑ j = 1 ℓ u j ​ ∂ ∂ u j \chi=x\frac{\partial}{\partial x}-s\sum_{j=1}^{\ell}u_{j}\frac{\partial}{\partial u_{j}} |  |

Quitte à effectuer une ramification en x x, on peut supposer que s = 1 s=1. La dérivation χ \chi agit sur l’anneau S ​ B 1,. ​ ( x, α, u) SB^{1,.}(x,\alpha,u). Soit π χ: ( x, α, u) ∈ U ↦ ( α, ( λ j)) = ( α, ( x ​ u j)) ∈ W \pi_{\chi}:(x,\alpha,u)\in U\mapsto(\alpha,(\lambda_{j}))=(\alpha,(xu_{j}))\in W son morphisme intégral. Les idéaux χ \chi -transverses le long de γ = { ( α, u) = 0 } \gamma=\{(\alpha,u)=0\} sont des idéaux de l’anneau ℝ ​ { α, λ } \mathbb{R}\{\alpha,\lambda\}.

###### Théorème VB2 (théorème de division 2)

Soit J J un idéal de ℝ ​ { α, λ } \mathbb{R}\{\alpha,\lambda\}. Il existe un entier n ⁡ ( J) n(J) tel que pour tout f ∈ S ​ B ​ ( x, α, u) f\in SB(x,\alpha,u) dont l’idéal χ \chi -transverse est inclus dans J J, alors ( x n ⁡ ( J)) ​ I χ, f ⊂ π χ ∗ ​ ( J) (x^{n(J)})I_{\chi,f}\subset\pi_{\chi}^{*}(J).

Preuve. Soit S θ S_{\theta} un secteur dans la coordonnée x x et P ε P_{\varepsilon} un polydisque dans les coordonnées ( α, u) (\alpha,u) tels que la série f = ∑ c n, m ​ ( x) ​ α n ​ u m f=\sum c_{n,m}(x)\alpha^{n}u^{m} soit convergente sur S θ × P ε S_{\theta}\times P_{\varepsilon}. Soit F = ∑ x − | m | ​ c n, m ​ α n ​ λ m F=\sum x^{-|m|}c_{n,m}\alpha^{n}\lambda^{m}. On a π χ ∗ ​ ( F) = f \pi_{\chi}^{*}(F)=f et pour tout x ∈ S θ x\in S_{\theta}, la série de F ( x,.) F(x,.) est convergente sur le produit de polydisques P ε × P ε ​ | x | P_{\varepsilon}\times P_{\varepsilon|x|}. De plus, l’idéal χ 0 \chi_{0} -transverse de F F est inclus dans J J. Soit ( φ j) (\varphi_{j}) une base de l’idéal J J dans l’anneau ℝ ​ { α, λ } \mathbb{R}\{\alpha,\lambda\}. D’après le théorème de division VB1

 | F = ∑ Q j ​ φ j F=\sum Q_{j}\varphi_{j} |  | 1 |

Ce théorème se généralise facilement aux produits de polydisques: soit L ⁡ ( n, m) = L 1 ​ ( n) + L 2 ​ ( m) L(n,m)=L_{1}(n)+L_{2}(m) une forme linéaire positive et soit σ = ( σ 1, σ 2) \sigma=(\sigma_{1},\sigma_{2}) avec σ i > 0 \sigma_{i}>0. Notons

 | ℝ { α, λ } L, σ = { g = ∑ g n, m α n λ m, | | g | | L, σ = ∑ | g n, m | σ 1 L 1 ​ ( n) σ 2 L 2 ​ ( m) < ∞ } \mathbb{R}\{\alpha,\lambda\}_{L,\sigma}=\{g=\sum g_{n,m}\alpha^{n}\lambda^{m},\ ||g||_{L,\sigma}=\sum|g_{n,m}|\sigma_{1}^{L_{1}(n)}\sigma_{2}^{L_{2}(m)}<\infty\} |  |

alors il existe L L, des entiers ℓ 1, j \ell_{1,j}, ℓ 2, j \ell_{2,j} et ε 0 > 0 \varepsilon_{0}>0 tels que si σ i < ε 0 \sigma_{i}<\varepsilon_{0}

 | | | Q j ( x,.) | | L, σ < 2 σ 1 ℓ 1, j ​ σ 2 ℓ 2, j | | F ( x,.) | | L, σ ||Q_{j}(x,.)||_{L,\sigma}<\frac{2}{\sigma_{1}^{\ell_{1,j}}\sigma_{2}^{\ell_{2,j}}}||F(x,.)||_{L,\sigma} |  |

Soit n ⁡ ( J) = max ⁡ { ℓ 2, j } n(J)=\max\{\ell_{2,j}\}, on a | | x n ⁡ ( J) Q j ( x,.) | | L, σ < c j | | F ( x,.) | | L, σ ||x^{n(J)}Q_{j}(x,.)||_{L,\sigma}<c_{j}||F(x,.)||_{L,\sigma}, par conséquent si ε \varepsilon est suffisament petit, on a q j = π χ ∗ ​ ( x n ⁡ ( J) ​ Q j) ∈ S ​ B ​ ( x, α, u) q_{j}=\pi_{\chi}^{*}(x^{n(J)}Q_{j})\in SB(x,\alpha,u). On obtient le résultat en relevant la relation (1)

 | x n ⁡ ( J) ​ f = ∑ q j ​ π χ ′ ∗ ​ ( φ j) ∎ x^{n(J)}f=\sum q_{j}\pi_{\chi^{\prime}}^{*}(\varphi_{j})\qed |  |

Soit ν = ( ν 1, …, ν p) \nu=(\nu_{1},\ldots,\nu_{p}), ν ′ = ( ν 1 ′, …, ν p ′ ′) \nu^{\prime}=(\nu^{\prime}_{1},\ldots,\nu^{\prime}_{p^{\prime}}), α = ( μ, ν ′) \alpha=(\mu,\nu^{\prime}) et α ′ = ( α, ν) \alpha^{\prime}=(\alpha,\nu). L’algèbre Q ​ R ​ H ​ ( x, α ′) QR{H}(x,\alpha^{\prime}) s’identifie à une sous-algèbre de B = Q ​ R ​ H ​ ( x, α) ​ { ν } {B}=QR{H}(x,\alpha)\{\nu\}. Les séries d’éléments de B {B} sont convergentes sur un voisinage produit. Soit f = ∑ f m ​ ν m ∈ B f=\sum f_{m}\nu^{m}\in{B}, l’algèbre Q ​ R ​ H ​ ( x, α) QR{H}(x,\alpha) étant locale de topologie de Krull séparée, on peut définir, comme dans [B-M], un ordre sur les monômes de B {B}: soit M {M} l’idéal maximal de Q ​ R ​ H ​ ( x, α) QR{H}(x,\alpha), l’ordre e ⁡ ( f m) e(f_{m}) de f m f_{m} est le plus grand entier e e tel que f m ∈ M e f_{m}\in{M}^{e}. Soit L ⁡ ( m) = ∑ λ j ​ m j L(m)=\sum\lambda_{j}m_{j} une forme linéaire positive et soit ( L ⁡ ( m), m 1, …, m p) (L(m),m_{1},\ldots,m_{p}) l’ordre lexicographique sur les monômes ν m \nu^{m}. Pour tout entier ℓ \ell, l’application L ′ ​ ( f m ​ ν m) = ( ℓ ​ e ​ ( f m), L ⁡ ( m), m) L^{\prime}(f_{m}\nu^{m})=(\ell e(f_{m}),L(m),m) est un ordre sur les monômes de B {B}.

Soit I = ⟨ g 1, …, g q ⟩ I=\langle g_{1},\ldots,g_{q}\rangle un idéal de B {B} et soit g j = ∑ g j, m ​ ν m g_{j}=\sum g_{j,m}\nu^{m} la série de g j g_{j}. On suppose que pour tout j j, il existe un coefficient g j, m g_{j,m} d’ordre 0. Soit m j m^{j} le plus petit de ces entiers et ( Δ j, Δ) (\Delta_{j},\Delta) la partition de ℕ p \mathbb{N}^{p} associée. On définit le support de f ∈ B f\in{B} par supp ( f) = { m; f m ≠ 0 } \text{supp}(f)=\{m;\quad f_{m}\neq 0\}. Les algorithmes formel et analytique de [B-M] s’adaptent à I I et à B {B} et on obtient

###### Lemme VB2

Il existe L L et ℓ \ell tels que tout f ∈ B f\in{B} se divise de manière unique dans I I sous la forme

 | f = ∑ j = 1 q Q j ​ g j + R Q j, R ∈ B f=\sum_{j=1}^{q}Q_{j}g_{j}+R\quad\quad Q_{j},\ R\in{B} |  |

 | m j + supp ​ ( Q j) ⊂ Δ j et supp ​ ( R) ⊂ Δ m^{j}+\text{supp}(Q_{j})\subset\Delta_{j}\quad\text{et}\quad\text{supp}(R)\subset\Delta |  |

L’algèbre Q ​ R ​ H ​ ( x, α ′) QR{H}(x,\alpha^{\prime}) est isomorphe à une sous-algèbre B ∗ {B}_{*} de B {B} définie comme suit: Soit X ⁡ ( x, μ) X(x,\mu) les fonctions élémentaires de Q ​ R ​ H QR{H}. Alors f ∈ B ∗ f\in{B}_{*} si et seulement si pour tout n n, la série τ n ​ ( f) = ∑ 𝕛 X n ​ ( f m) ​ ν m \tau_{n}(f)=\sum{\mathbb{j}}_{X}^{n}(f_{m})\nu^{m} est un élément de Q ​ R ​ H c ​ v ​ g QR{H}_{cvg}. Si I I est un idéal de B ∗ {B}_{*} satisfaisant aux mêmes hypothèses que ci-dessus, alors

###### Théorème VB3 (théorème de division 3)

Tout f ∈ B ∗ f\in{B}_{*} se divise de manière unique dans I I sous la forme

 | f = ∑ j = 1 q Q j ​ g j + R Q j, R ∈ B ∗ f=\sum_{j=1}^{q}Q_{j}g_{j}+R\quad\quad Q_{j},\ R\in{B}_{*} |  |

 | m j + supp ​ ( Q j) ⊂ Δ j et supp ​ ( R) ⊂ Δ m^{j}+\text{supp}(Q_{j})\subset\Delta_{j}\quad\text{et}\quad\text{supp}(R)\subset\Delta |  |

Preuve. D’après la partie formel de l’algorithme (lemme VB1), si f m = o ⁡ ( x n) f_{m}=o(x^{n}) pour tout m m, il en est de même des séries des Q j Q_{j} et de R R. Soit Q j ​ ( f) Q_{j}(f) et R ⁡ ( f) R(f) donnés par le lemme VB2. Par l’unicité de la division, Q j ​ ( f) = Q j ​ ( τ n ​ ( f)) + Q j ​ ( f − τ n ​ ( f)) Q_{j}(f)=Q_{j}(\tau_{n}(f))+Q_{j}(f-\tau_{n}(f)) et R ⁡ ( f) = R ⁡ ( τ n ​ ( f)) + R ⁡ ( f − τ n ​ ( f)) R(f)=R(\tau_{n}(f))+R(f-\tau_{n}(f)). Par conséquent τ n ​ ( Q j ​ ( f)) = τ n ​ ( Q j ​ ( τ n ​ ( f))) \tau_{n}(Q_{j}(f))=\tau_{n}(Q_{j}(\tau_{n}(f))) et τ n ​ ( R ⁡ ( f)) = τ n ​ ( R ⁡ ( τ n ​ ( f))) \tau_{n}(R(f))=\tau_{n}(R(\tau_{n}(f))). Soit l’idéal I n = ⟨ τ n ​ ( g 1), …, τ n ​ ( g q) ⟩ {I}_{n}=\langle\tau_{n}(g_{1}),\ldots,\tau_{n}(g_{q})\rangle, la partition de ℕ p \mathbb{N}^{p} qui lui est associée est la même que celle de I I. Soit Q j, n ​ ( τ n ​ ( f)) Q_{j,n}(\tau_{n}(f)) et R n ​ ( τ n ​ ( f)) R_{n}(\tau_{n}(f)) donnés par le lemme VB2 appliqué à I n I_{n}, ce sont des éléments de Q ​ R ​ H c ​ v ​ g QR{H}_{cvg} d’après la partie analytique de l’algorithme. Or chaque coefficient de la série de ∑ Q j, n ​ ( τ n ​ ( f)) ​ ( g j − τ n ​ ( g j)) \sum Q_{j,n}(\tau_{n}(f))(g_{j}-\tau_{n}(g_{j})) est un o ⁡ ( x n) o(x^{n}), donc par l’unicité de la division, τ n ​ ( Q j ​ ( τ n ​ ( f))) = 𝕛 X n ​ ( Q j, n ​ ( τ n ​ ( f))) \tau_{n}(Q_{j}(\tau_{n}(f)))={\mathbb{j}}_{X}^{n}(Q_{j,n}(\tau_{n}(f))) et τ n ​ ( R ⁡ ( τ n ​ ( f))) = 𝕛 X n ​ ( R n ​ ( τ n ​ ( f))) \tau_{n}(R(\tau_{n}(f)))={\mathbb{j}}_{X}^{n}(R_{n}(\tau_{n}(f))).∎

D’après [B-M], une conséquence de ce théorème est le théorème des fonctions implicites pour les applications régulières dans la coordonnée ν \nu. Une autre conséquence est

###### Théorème VB4 (théorème d'inversion)

Soit f = x ⁡ ( 1 + O ⁡ ( x)) ∈ Q ​ R ​ H ​ ( x, α) f=x(1+O(x))\in QR{H}(x,\alpha). Il existe un unique g = y ⁡ ( 1 + O ⁡ ( y)) ∈ Q ​ R ​ H ​ ( y, α) g=y(1+O(y))\in QR{H}(y,\alpha) qui inverse f f.

Preuve. Posons f = x ⁡ ( 1 + F) f=x(1+F) avec F ∈ Q ​ R ​ H F\in QR{H}. Il existe un unique inverse en classe C 1 {C}^{1}. Cherchons G ∈ Q ​ R ​ H G\in QR{H} tel que g = y ⁡ ( 1 + G) g=y(1+G) soit un inverse. La condition f ∘ g = I ​ d f\circ g=Id donne l’équation G + ( 1 + G) ​ F ​ ( y ⁡ ( 1 + G), α) = 0 G+(1+G)F(y(1+G),\alpha)=0 qui est analytique en G G et régulière d’ordre 1. Le théorème des fonctions implicites permet de conclure.∎

Références.

[◄][1][image: ar5iv homepage] [2]
[Feeling lucky?][3] [4]
[Conversion report][5]
[Report an issue][6]
[View original on arXiv][7] [►][8]


## Links

[1]: /html/0912.1559
[2]: /
[3]: /feeling_lucky
[4]: /land_of_honey_and_milk
[5]: /log/0912.1560
[6]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+0912.1560
[7]: https://arxiv.org/pdf/0912.1560
[8]: /html/0912.1561
