<!-- source: https://arxiv.org/pdf/1908.10410 | converted from PDF -->

1

Visualization of Very Large High-Dimensional Data Sets as
Minimum Spanning Trees

Daniel Probst1,* and Jean-Louis Reymond1,*

1Department of Chemistry and Biochemistry, National Center for Competence in Research
NCCR TransCure, University of Berne, Freiestrasse 3, 3012 Berne, Switzerland

*e-mail: daniel.probst@dcb.unibe.ch, jean-louis.reymond@dcb.unibe.ch

Abstract

The chemical sciences are producing an unprecedented amount of large, high-dimensional

data sets containing chemical structures and associated properties. However, there are

currently no algorithms to visualize such data while preserving both global and local features

with a sufficient level of detail to allow for human inspection and interpretation. Here, we

propose a solution to this problem with a new data visualization method, TMAP, capable of

representing data sets of up to millions of data points and arbitrary high dimensionality as a

two-dimensional tree (http://tmap.gdb.tools). Visualizations based on TMAP are better suited

than t-SNE or UMAP for the exploration and interpretation of large data sets due to their tree-

like nature, increased local and global neighborhood and structure preservation, and the

transparency of the methods the algorithm is based on. We apply TMAP to the most used

chemistry data sets including databases of molecules such as ChEMBL, FDB17, the Natural

Products Atlas, DSSTox, as well as to the MoleculeNet benchmark collection of data sets. We

also show its broad applicability with further examples from biology, particle physics, and

literature.
 2

Introduction

The recent development of new and often very accessible frameworks and powerful hardware

has enabled the implementation of computational methods to generate and collect large high

dimensional data sets and created an ever increasing need to explore as well as understand

these data.1–9 Generally, large high-dimensional data sets are matrices where rows are samples

and columns are measured variables, each column defining a dimension of the space which

contains the data. Visualizing such data sets is challenging because reducing the

dimensionality, which is required in order to make the data visually interpretable for humans,

is both lossy and computationally expensive.10

  Large high-dimensional data sets are frequently used in the chemical sciences. For

instance the ChEMBL database (𝑛 = 1,159,881) of bioactive molecules from the scientific

literature and their associated biological assay data are used daily in the area of drug

discovery.11 Further examples of large databases containing molecules include FDB17 (𝑛 =

10,101,204), a fragment-like subset of the enumerated database GDB17 listing theoretically

possible molecules up to 17 atoms,
12–14 and DSSTox (𝑛 = 848,816), containing molecules

investigated for toxicity.15 Examples of smaller data sets include the Natural Products Atlas

(𝑛 = 24,594), collecting microbially-derived natural products;16 Drugbank (𝑛 = 9,300),

listing molecules marketed or investigated as drugs;17 and the MoleculeNet benchmark,

containing a collection of 16 data sets of small organic molecules.18

To visualize such databases, simple linear dimensionality reduction methods such as

principal component analysis and similarity mapping readily produce 2D- or 3D-

representations of global features.19–25 However, local features defining the relationships

between close or even nearest neighbor (NN) molecules, which are very important to

understand the structure of data, are mostly lost, limiting the applicability of linear
 3

dimensionality reduction methods for visualization. The important NN relationships are much

better preserved using non-linear manifold learning algorithms, which assume that the data

lies on a lower-dimensional manifold embedded within the high-dimensional space.

Algorithms such as nonlinear principal component analysis (NLPCA or autoencoders), t-

distributed stochastic neighbor embedding (t-SNE), and more recently uniform manifold

approximation and projection (UMAP) are based on this assumption.26–28 Other techniques

used are probabilistic generative topographic maps (GTM) and self-organizing maps (SOM),

which are based on artificial neural networks.29,30 However, these algorithms have time

complexities between at least 𝑂(𝑛1.14) and 𝑂(𝑛5), limiting the size of to be visualized data

sets.31 The same limitations in terms of data set size apply when distributing data in a tree by

implementing the neighbor joining algorithm or similar methods used to create phylogenetic

trees.32,33 This limiting behavior has been documented by the ChemTreeMap tool, which can

only visualize up to approximately 10,000 data points (molecules or clusters of molecules).34

Due to the described challenges, large scientific data sets are generally visualized in

aggregated or reduced form.35,36

Here we present an algorithm, named TMAP (Tree MAP), to generate and distribute

intuitive visualizations of large data sets in the order of up to 107 with arbitrary

dimensionality in a tree. Our method is based on a combination of locality sensitive hashing,

graph theory, and modern web technology which also integrates into established data analysis

and plotting workflows. This tree-based layout facilitates visual inspection of the data with a

high resolution by explicitly visualizing the closest distance between clusters and the detailed

structure of clusters through branches and sub-branches. We demonstrate the performance of

TMAP with toy data sets from computer graphics and with ChEMBL subsets of different size

and composition, and show that it surpasses comparable algorithms such as t-SNE and UMAP

in terms of time and space complexity. We further exemplify the use of TMAP for visualizing

4

large high-dimensional data sets from chemistry as well as from further scientific fields

(Table 1).

Table 1 Data sets visualized using TMAP.

Data Set  Description  Data Type  Size

Toy Data Sets
COIL20  Gray-scale images of 20 objects, each rotated 72x at 5° intervals.  Images  1,440
MNIST  Gray-scale images of handwritten digits.  Images  70,000
Fashion MNIST  Gray-scale images of fashion items from 10 classes.  Images  70,000
Chemical Compound Databases and PDB
ChEMBL  Bioactive molecules with drug-like properties.  SMILES  1,159,881
FDB17 & ChEMBL  Fragment database (up to 17 atoms) and ChEMBL.  SMILES  11,261,085
Natural Products Atlas  Bacterial and fungal natural products.  SMILES  24,594
DSSTox  U.S. EPA information on toxicity of chemicals.  SMILES  848,816
PDB  Information on the 3D structures of proteins and nucleic acids.  Atomic coordinates  131,236
Drugbank  Approved, investigational, experimental, and withdrawn drugs.  SMILES  9,300
MoleculeNet Benchmark Data Sets
QM8  Subset of GDB-13 with associated QM properties.  SMILES  21,786
QM9  Subset of GDB-13 with associated QM properties.  SMILES  133,885
ESOL  Common organic small molecules with solubility information.  SMILES  1,128
FreeSolv  Calculated and experimental hydration free energy of molecules.  SMILES  642
Lipophilicity  Experimental results of logD for organic small molecules.  SMILES  4,200
PCBA  PubChem subset with biological activities.  SMILES  437,929
MUV  PubChem subset for virtual screening validation.  SMILES  93,087
HIV  Experimental results for HIV replication inhibition.  SMILES  41,127
PDBind  Binding affinities for ligands in biomolecular complexes.  SMILES  11,908
BACE  IC50 values against BACE-1 (human β-secretase 1).  SMILES  1,513
BBBP  Ability of organic molecules to cross the blood-brain barrier.   SMILES  2,039
Tox21  Toxicity measurements on 12 targets.  SMILES  7,831
ToxCast  Toxicity measurements on more than 600 targets.  SMILES  8,575
SIDER  Adverse drug reactions of a selection of marketed drugs.  SMILES  1,427
ClinTox  FDA approved drugs that failed clinical trials for toxicity reasons.  SMILES  1,478
Other Data Sets
PubMed Central  Full-text archive of biomedical and life sciences journal literature.  Text  327,628
Gutenberg  A subset of public domain Project Gutenberg eBooks.  Text  3,036
NIPS  Abstracts of NIPS conference papers from 1987-2015.  Text  7,241
RNA Sequencing  A subset of the PANCAN database.  Gene expression  801
ProteomeHD  Human proteome co-regulation data.  Co-regulation scores  5,013
Flowcytometry  Data gathered from a flow cytometry experiment.  Signal intensity  436,877
MiniBooNE  Data gathered by the MiniBooNE particle physics experiment.  Particle ID  130,065

.
 5

Methods

Given an arbitrary data set as an input, TMAP encompasses four phases: (I) LSH forest

indexing,37,38 (II) construction of a 𝑐-approximate 𝑘-nearest neighbor graph, (III) calculation

of a minimum spanning tree (MST) of the 𝑐-approximate 𝑘-nearest neighbor graph,39 and (IV)

generation of a layout for the resulting MST.40

During phase I, the input data are indexed in an LSH forest data structure, enabling 𝑐-

approximate 𝑘-nearest neighbor (k-NN) searches with a time complexity sub-linear in 𝑛. Text

and binary data are encoded using the MinHash algorithm, while integer and floating-point

data are encoded using a weighted variation of the algorithm.41–43 The LSH Forest data

structure for both MinHash and weighted MinHash data is initialized with the number of hash

functions 𝑑 used in encoding the data, and the number of prefix trees 𝑙. An increase in the

values of both parameters led to an increase in main memory usage; however, higher values

for 𝑙 also decrease query speed. The effect of parameters 𝑑 and 𝑙 on the final visualization is

shown in Fig. S1. The use of a combination of (weighted) MinHash and LSH Forest, which

supports fast estimation of the Jaccard distance between two binary sets, has been shown to

perform very well for molecules.44 Note that other data structures and algorithms

implementing a variety of different distance metrics may show better performance on other

data and can be used as drop-in replacements of phase I.

  In phase II, an undirected weighted 𝑐-approximate 𝑘-nearest neighbor graph (𝑐-𝑘-

NNG) is constructed from the data points indexed in the LSH forest, where an augmented

variant of the LSH forest query algorithm we previously introduced for virtual screening tasks

is used to increase efficiency.45 The 𝑐-𝑘-NNG construction phase takes two arguments,

namely 𝑘, the number of nearest-neighbors to be searched for, and 𝑘𝑐, the factor used by the

augmented query algorithm. The variant of the query algorithm increases the time complexity

6

of a single query from 𝑂(log 𝑛) to 𝑂(𝑘 ∙ 𝑘𝑐 + log 𝑛), resulting in an overall time complexity

of 𝑂(𝑛(𝑘 ∙ 𝑘𝑐 + log 𝑛)), where practically 𝑘 ∙ 𝑘𝑐 > log 𝑛, for the 𝑐-𝑘-NNG construction. The

edges of the 𝑐-𝑘-NNG are assigned the Jaccard distance of their incident vertices as their

weight. Depending on the distribution and the hashing of the data, the 𝑐-𝑘-NNG can be

disconnected (1) if outliers exist which have a Jaccard distance of 1.0 to all other data points

and are therefore not connected to any other nodes or (2) if, due to highly connected clusters

of size ≥ 𝑘 in the Jaccard space, connected components are created. However, the following

phases are agnostic to whether this phase yields a disconnected graph. The effect of

parameters 𝑘 and 𝑘𝑐 on the final visualization is shown in Fig. S2. Alternatively, an arbitrary

undirected graph can be supplied to the algorithm as a (weighted) edge list.

  During phase III, a minimum spanning tree (MST) is constructed on the weighted 𝑐-𝑘-

NNG using Kruskal’s algorithm, which represents the central and differentiating phase of the

described algorithm. Whereas comparable algorithms such as UMAP or t-SNE attempt to

embed pruned graphs, TMAP removes all cycles from the initial graph using the MST

algorithm, significantly lowering the computational complexity of a low dimensional

embedding. The algorithm reaches a globally optimal solution by applying a greedy approach

of selecting locally optimal solutions at each stage—properties which are also desirable in

data visualization. The time complexity of Kruskal’s algorithm is 𝑂(𝐸 + log 𝑉), rendering

this phase negligible compared to phase II in terms of execution time. In the case of a

disconnected 𝑐-𝑘-NNG, a minimum spanning forest is created.

  Phase IV lays out the tree on the Euclidean plane. As the MST is unrooted and to keep

the drawing compact, the tree is not visualized by applying a tree but a graph layout

algorithm. In order to draw MSTs of considerable size (millions of vertices), a spring-

electrical model layout algorithm with multilevel multipole-based force approximation is

applied. This algorithm is provided by the open graph drawing framework (OGDF), a
 7

modular C++ library.40 In addition, the use of the OGDF allows for effortless adjustments to

the graph layout algorithm in terms of both aesthetics and computational time requirements.

Whereas several parameters can be configured for the layout phase, only parameter 𝑝 must be

adjusted based on the size of the input data set (Fig. S3). This phase constitutes the bottleneck

regarding computational complexity.

Results and Discussion

TMAP performance assessment with Toy Data Sets and ChEMBL Subsets

The quality of our TMAP algorithm is first assessed by comparing TMAP and UMAP to

visualize the common benchmarking data sets MNIST, FMNIST, and COIL20 (Fig. 1).

UMAP generally represents clusters as tightly packed patches and tries to reach maximal

separation between them. On the other hand, TMAP visualizes the relations between, as well

as within, clusters as branches and sub-branches. While UMAP can represent the circular

nature of the COIL20 subsets, TMAP cuts the circular clusters at the edge of largest

difference and joins subsets through one or more edges of smallest difference (Fig. 1a, b).

However, the plot shows that this removal of local connectivity leads to an untangling of

highly similar data (shown in dark green, orange, dark red, dark purple, and light blue). This

behavior has been assessed and compared to UMAP in Figures S4 and S5, where it is shown

that both TMAP and UMAP have to sacrifice locality preservation for more complex

examples. For the MNIST and FMNIST data sets, the tree structure results in a higher

resolution of both variances and errors within clusters as it becomes apparent how sub clusters

(branches within clusters) are linked and which true positives connect to false positives (Fig

1c, d, e, f).

 8

Fig. 1. Comparison between TMAP and UMAP on benchmark data sets. Please use the interactive versions
of the TMAP visualizations at http://tmap.gdb.tools to see images associated with each point on the map. TMAP
explicitly visualizes the relations between as well as within clusters. (a, b) While UMAP represents the circular
nature of the COIL20 subsets, TMAP cuts the circular clusters at the edge of largest difference and joins clusters
through an edge of smallest difference. (c, d, e, f) For the MNIST and FMNIST data sets, the tree structure
allows for a higher resolution of both variances and errors within clusters as it becomes apparent how sub
clusters (branches within clusters) are linked and which true positives connect to false positives. The image data
of all three sets was binarized using the average intensity per image as a threshold.

 9

In a second, more applied comparison example, we visualize data from ChEMBL using

TMAP and UMAP. For this analysis molecular structures are encoded using ECFP4

(extended connectivity fingerprint up to 4 bonds, 512-D binary vector), a molecular

fingerprint encoding circular substructures and which performs well in virtual screening and

target prediction.46–48 We consider a subset 𝑆𝑡 of the top 10,000 ChEMBL compounds by

insertion date, as well as a random subset 𝑆𝑟 of 10,000 ChEMBL molecules.

  Taking the more homogeneous set 𝑆𝑡 as an input, the 2D-maps produced by each

representation, plotted using the Python library matplotlib, illustrate that TMAP, which

distributes clusters in branches and subbranches of the MST, produces a much more even

distribution of compounds on the canvas compared to UMAP, thus enabling better visual

resolution (Fig. 2a, b). Furthermore, in a visualization of the heterogeneous set 𝑆𝑟, nearest

neighbor relationships (locality) are better preserved in TMAP compared to UMAP, as

illustrated by the positioning of the 20 structurally nearest neighbors of compound

CHEMBL3701602,49 reported as a potent inhibitor of human tyrosine-protein kinase SYK.

The 20 structurally similar nearest neighbors are defined as 20 nearest neighbors in the

original 512-dimensional fingerprint space. TMAP directly connects the query compound to

three of the 20 nearest neighbors, CHEMBL3701630, CHEMBL3701611, and

CHEMBL38911457, its nearest, second nearest, and 15th nearest neighbor respectively. The

nearest neighbors 1 through 7 are all within a topological distance of 3 around the query (Fig.

2c). In contrast, UMAP has positioned nearest neighbors 2, 3, 9, and 18, among several even

more distant data points, closer to the query than the nearest neighbor from the original space

(Fig. 2d). Indeed, TMAP preserves locality in terms of retaining 1-nearest neighbor

relationships much better than UMAP, applying both topological and Euclidean metrics (Fig.

2e, f; Fig. S6). The quality of the preservation of locality largely depends on parameter 𝑑,

with adjustments to parameters 𝑘 and 𝑘𝑐 only having a minor influence (Fig. S7). Moreover,

10

TMAP yields reproducible results when running on identical parameters and input data,

whereas results of comparable algorithms such as UMAP change considerably with every run

(Fig. S8).26

  In terms of calculation times, TMAP and UMAP have comparable running time 𝑡 and

memory usage 𝑎 for small random subsets of the 512-D ECFP-encoded ChEMBL data set

with sizes 𝑛 = 10,000 and 𝑛 = 100,000, TMAP significantly outperforms UMAP for larger

random subsets (𝑛 = 500,000 and 𝑛 = 1,000,000)  (Fig. 2h, i). Further insight into the

computational behavior of TMAP is provided by analyzing running times for the different

phases based on a larger subset (𝑛 = 1,000,000) of the ECFP4-encoded ChEMBL data set

(Fig. 2g). During phase I of the algorithm, which accounts for 180s of the execution time and

approximately 5GB of main memory usage, data is loaded and indexed in the LSH Forest data

structure in chunks of 100,000, as expressed by 10 distinct jumps in memory consumption.

The construction of the 𝑐-𝑘-NNG during phase II requires a negligible amount of main

memory and takes approximately 110s. During 10 seconds of execution time, MST creation

(phase III) occupies a further 2GB of main memory of which approximately 1GB is retained to

store the tree data structure. The graph layout algorithm (phase IV) requires 2GB throughout

55s, after which the algorithm completes with a total wall clock run time of 355s and peak

main memory usage of 8.553GB.

  Note that TMAP supports Jaccard similarity estimation through MinHash and

weighted MinHash for binary and weighted sets, respectively. While the Jaccard metric is

very suitable for chemical similarity calculations based on molecular fingerprints, the metric

may not be the best option available to problems presented by other data sets. However, there

exists a wide range of LSH families supporting distance and similarity metrics such as

Hamming distance, 𝑙𝑝 distance, Levenshtein distance, or cosine similarity, which are
 11

compatible with TMAP.50,51 Furthermore, the modularity of TMAP allows to plug in arbitrary

nearest-neighbor-graph creation techniques or load existing graphs from files.

Fig. 2 Comparing TMAP and UMAP for visualizing ChEMBL. The first 𝑛 compounds 𝑆𝑡 (a, b, e) and a
random sample 𝑆𝑟 (c, d, f), each of size 𝑛 = 10,000, were drawn from the 512-D ECFP-encoded ChEMBL data
set to visualize the distribution of biological entity classes and k-nearest neighbors respectively. (a) TMAP lays
out the data as a single connected tree, whereas (b) UMAP draws what appears to be a highly disconnected
graph, with the connection between components becoming impossible to assert. TMAP keeps the intra- and
inter-cluster distances at the same magnitude, increasing the visual resolution of the plot. (c, d) The 20 nearest
neighbors of a randomly selected compound from a random sample. (c) TMAP directly connects the query
compound to three of the 20 nearest neighbors (1, 2, 15); nearest neighbors 1 through 7 are all within a
topological distance of 3 around the query compound. (d) The closest nearest neighbors of the same query
compound in the UMAP visualization are true nearest neighbors 2, 3, 18, 9, and 1, with 1 being the farthest of
the five. (e, f) Ranked distances from true nearest neighbor in original high dimensional space after embedding
based on topological and Euclidean distance for data sets 𝑆𝑡 and 𝑆𝑟 respectively. (g) Computing the coordinates
for a random sample (𝑛 = 1,000,000) highlights the running time behavior of TMAP and allows an inspection
of the time and space requirements of the different phases of the algorithm. Four random samples increasing in
size (𝑛 = 10,000, 𝑛 = 100,000, 𝑛 = 500,000, and 𝑛 = 1,000,000) detail the differences in memory usage (h)
and running time (i) between TMAP and UMAP (𝑡𝑇𝑀𝐴𝑃 = 4.865s, 𝑎𝑇𝑀𝐴𝑃 = 0.223GB; 𝑡𝑈𝑀𝐴𝑃 = 20.985s,
𝑎𝑈𝑀𝐴𝑃 = 0.383GB and 𝑡𝑇𝑀𝐴𝑃 = 33.485s, 𝑎𝑇𝑀𝐴𝑃 = 1.12GB; 𝑡𝑈𝑀𝐴𝑃 = 115.661s, 𝑎𝑈𝑀𝐴𝑃 = 2.488GB
respectively)  (𝑡𝑇𝑀𝐴𝑃 = 175.89s, 𝑎𝑇𝑀𝐴𝑃 = 4.521GB; 𝑡𝑈𝑀𝐴𝑃 = 3,577.768s, 𝑎𝑈𝑀𝐴𝑃 = 18.854GB and 𝑡𝑇𝑀𝐴𝑃 =
354.682s, 𝑎𝑇𝑀𝐴𝑃 = 8.553GB; 𝑡𝑈𝑀𝐴𝑃 = 41,325.944s, 𝑎𝑈𝑀𝐴𝑃 = 48.507GB  respectively).

 12

TMAPs of small molecule data sets: ChEMBL, FDB17, DSSTox, and the Natural

Products Atlas

The high performance and relatively low memory usage of TMAP, as well as the ability to

generate highly detailed and interpretable representations of high-dimensional data sets, is

illustrated here by interactive visualization of a series of small molecule data sets available in

the public domain. In these examples we use MHFP6 (512 MinHash permutations), a

molecular fingerprint related to ECFP4 but with better performance for virtual screening tasks

and the ability to be directly indexed in an LSH Forest data structure, which considerably

speeds up computation for large data sets.45

  As a first example, we discuss the TMAP of the full data set of the ChEMBL database

containing the 1.13 million ChEMBL compounds associated with biological assay data.

TMAP completes the calculation within 613 seconds with a peak memory usage of 20.562

GB. Note that approximately half of the main memory usage is accounted for by SMILES,

activities, and biological entity classes which are loaded for later use in the visualization. To

facilitate data analysis, the coordinates computed by TMAP are exported as an interactive

portable HTML file using Faerun, where molecules are displayed using the JavaScript library

SmilesDrawer (Fig. 3a).25,52

  Analyzing the distribution of molecules on the tree shows that TMAP groups

molecules according to their structure and their biological activity, accurately reflecting

similarities calculated in the high-dimensional MHFP6 space. This is well illustrated for a

subset of the map (Fig. 3a, insert). In this area of the map, data points in cyan indicate

molecules with a high binding affinity for serotonin, norepinephrine, and dopamine

neurotransmitters in two connected branches (right side of inset), while data points in orange

show inhibitors of the phenylethanolamine N-methyltransferase (PNMT) (left side of inset),

13

and red and dark blue data points indicate nicotinic acetylcholine receptor (nAChRs) ligands

and cytochrome p450s (CYPs) inhibitors, respectively.

Fig. 3 TMAP visualization of ChEMBL, FDB17, DSSTox, and the Natural Products Atlas in the MHFP6
chemical space. Please use the interactive versions at https://tmap.gdb.tools to visualize molecular structures
associated with each point. (a) Visualization of all ChEMBL compounds associated with biological assay data
(𝑛 = 1,159,881) colored by target class. The inset shows molecules with a high binding affinity for serotonin,
norepinephrine, and dopamine neurotransmitters (cyan); inhibitors of the phenylethanolamine N-
methyltransferase (orange); and structurally related compounds with high binding affinities for nicotinic
acetylcholine receptors and inhibitory effects on cytochrome p450s (red, dark blue). (b) The ChEMBL data set
was merged with fragment database (FDB17) compounds (𝑛 = 11,261,085) and visualized. FDB17 molecules
are shown in light gray. The inset shows a branch of steroid and steroid-like ChEMBL compounds, as well as
dominantly FDB17 branches which are sparsely populated by ChEMBL molecules. (c) Visualization of DSSTox
compounds colored by reported toxicity level. The inset shows a subtree containing a high number of toxic
compounds structurally similar or related to naphthalenes and other polycyclic aromatic hydrocarbons. (d) The
Natural Products Atlas chemical space colored by origin genus of the 9 largest groups. The inset shows that
structurally similar compounds are grouped into distinct branches and subbranches and are usually produced by
plants and fungi from the same genus.
 14

 As a second example, we visualize the ChEMBL set merged with FDB17 (𝑛 =

10,101,204) into a superset of size 𝑛 = 11,261,085 (Fig. 3b), which corresponds to the

largest data set that TMAP can successfully handle. As above, the TMAP 2D-layout

accurately reflects structural and functional similarities computed in the high-dimensional

MHFP6 space. In this TMAP visualization, the majority of ChEMBL compounds accumulate

in closely connected clusters (branches) due to the prevalence of aromatic carbocycles. A

notable exception is a relatively sizable branch of steroids and steroid-like compounds, which

is connected to a branch of FDB17 molecules containing non-aromatic 5-membered

carbocycles and ketones (Fig. 3b, insert). Many more detailed insights can be gained by

inspecting the interactive map in Faerun (http://tmap-fdb.gdb.tools).

  Further examples include MHFP6-encoded compounds from the Distributed Structure-

Searchable Toxicity (DSSTox) Database (𝑛 = 848,816) and the Natural Products Atlas (𝑛 =

24,594). Visualizing DSSTox and coloring the resulting tree by toxicity rating, TMAP creates

several subtrees and branches representing structural regions with a high incidence of highly

toxic compounds (shown in red, Fig. 3c). An example of such a subtree contains naphthalenes

and other polycyclic aromatic hydrocarbons (Fig. 3c, insert). The TMAP tree of the Natural

Products Atlas was colored according to origin genus and reveals that branches and

subbranches containing distinct substructures usually correlate with a certain genus such as

various combinations of phenols, fused cyclopentanes, lactones and steroids produced by the

fungi genus Ganoderma (colored purple in Fig. 3d, inset).

Visualization of the MoleculeNet Benchmark Data Sets

We further illustrate TMAP to visualize the MoleculeNet, a benchmark for molecular

machine learning which has found wide adaption in cheminformatics and encompasses 16

data sets ranging in size and composition (Table 1).18  As for the other small molecule data

sets above, we computed MHFP6 fingerprints of the associated molecules and the
 15

corresponding TMAPs, which we then color-coded according to various numerical values

available in the benchmarks. The procedure was applied with all MoleculeNet data sets except

for QM7/b, where no SMILES have been provided.

  The resulting TMAP representations, accessible at the TMAP website

(http://tmap.gdb.tools), reveal the detailed structure of the data sets as well as the behaviour of

methods applied to these data sets as a function of the chemical structures of the molecules.

For example, TMAPs of the QM8 and QM9 (𝑛 = 21,786 and 𝑛 = 133,885), which contain

small molecules and DFT-modelled parameters, reveal relationships between molecular

structures and the various computed physico-chemical values. For instance the TMAP of the

QM8 data set color-coded by the oscillator strengths of the lowest two singlet electronic

states reveals how the value correlates with molecular structure and explains the performance

differences in machine learning models trained on Coulomb matrices versus those trained on

structure-sensitive molecular fingerprints.53 In the case of the ESOL data set containing

measured and calculated water solubility values of common small molecules  (𝑛 = 1,128), its

TMAP color-coded with the difference between computed and measured values reveals the

limitation of the ESOL model when estimating solubility of polycyclic aromatic

hydrocarbons and compounds containing pyridines. For the FreeSolv data set (𝑛 = 642)

containing small molecules and their measured and calculated hydration free energy in water,

the TMAP visualization hints at possible limitations of the method when calculating hydration

free energies of sugars. Finally, for the MUV data set (𝑛 = 93,087), which contains active

small drug-like molecules against 17 different protein targets mixed in each case with inactive

decoy molecules, the various TMAPs reveal differences in the structural distribution of

actives among decoys. Actives are usually well distributed but appear to form clusters in

certain subsets (e.g. MUV-548 and MUV-846), explaining the generally higher performance

of fingerprint benchmarks for these subsets.47

 16

Application to other scientific data sets

We further illustrate the general applicability of TMAP to visualize data sets from the fields

of linguistics, biology, and particle physics. All produced maps are available as interactive

Faerun plots on the TMAP website (http://tmap.gdb.tools).

  Our first example concerns visualization of the RCSB Protein Data Bank, which

contains experimental 3D-structures of proteins and nucleic acids (𝑛 = 131,236).54 The PDB

files were extracted from the Protein Data Bank and encoded using the protein shape

fingerprint 3DP (136-D integer vector, 256 weighted MinHash samples) 3DP encodes the

structural shape of large molecules stored as PDB files based on through-space distances of

atoms.22 Processing data extracted from the PDB and indexed using a weighted variant of

MinHash, demonstrates the ability of TMAP to visualize both global and local structure,

improving on previous efforts on the visualization of the database.22,55 The global structure of

the 3DP-encoded PDB data is dominated by the size (heavy atom count) of the proteins (Fig.

5a), on the other hand, the local structure is defined by properties such as the fraction of

negative charges (Fig. 5b).

  As an additional example from biology, we consider the PANCAN data set (𝑛 = 800,

𝑑 = 20,531), which consists of gene expressions of patients having different types of tumors

(PRAD, KIRC, LUAD, COAD, and BRCA), randomly extracted from the cancer genome

atlas database.56 Here we index the PANCAN data directly using the LSH Forest data

structure and weighted MinHash. The output produced by processing the PANCAN data set

displays the successful differentiation of tumor types based on RNA sequencing data by the

algorithm (Fig. 5c). We also visualize the ProteomeHD data set using TMAP.57 This data set

consists of co-regulation scores of 5,013 proteins, annotated with their respective cellular

location. In addition to the ProteomeHD data set, Kustatscher et al. also released an R script

to create a map of the set using t-SNE which took a total of 400s to complete; in contrast,
 17

TMAP visualized the data set within 32 seconds (Fig. 5d), successfully clustering proteins by

their cellular location based on co-regulation scores. As a further biology example, our TMAP

webpage also features flow cytometry measurements (𝑛 = 436,877, 𝑑 = 14), exemplifying

the methods application for the visualization of relatively low dimensional data.17,58

Fig. 5 TMAP visualizations of the RCSB Protein Data Bank (PDB), PANCAN, and ProteomeHD data. For
(a) and (b), please use the interactive versions at http://pdb-tmap.gdb.tools to visualize protein structures
associated with each point. 3DP-encoded PDB entries visualized using TMAP with weighted MinHash indexing,
the color bars show the log-log distribution of the property values. (a) Colored according to the macromolecular
size (heavy atom count). The resulting map reflects the size-sensitivity of the 3DP fingerprint. (b) Colored
according to the fraction of negative charges in the molecules. Macromolecules with a high fraction of
negatively charged atoms, predominantly nucleic acids, are visible as clusters of red branches. (c) The PANCAN
data set (n=801, d=20,531) consists of gene expressions data of five types of tumors (PRAD, KIRC, LUAD,
COAD, and BRCA) and was indexed using a weighted variant of the MinHash algorithm. (d) Visualization of
the ProteomeHD data set (n=5,013, d=5,013) based on co-regulation scores of proteins. The data points have
been colored according to the associated cellular location.
 18

  As an example from physics, we represent the MiniBooNE data set (𝑛 = 130,065,

𝑑 = 50), which consists of measurements extracted from Fermilab’s MiniBooNE experiment

and contains the detection of signal (electron neutrinos) and background (muon neutrinos)

events
59. As the attributes in MiniBooNE are real numbers, we use the Annoy indexing library

which supports the cosine metric in phase I of the algorithm to index the data for 𝑘-NNG

construction, which demonstrates the modularity of TMAP.60 This example reflects the

independence of the MST and layout phases of the algorithm from the input data, displaying

the distribution of the signal over the background data (Fig. 6a).

  Outside of the natural sciences, we exemplify TMAP to visualize the GUTENBERG

set as an example of a data set from linguistics. This data set features a selection of 𝑛 = 3,036

books by 142 authors written in English.61 To analyze this data, we define a book fingerprint

as a dense-form binary vector indicating which words from the universe of all words extracted

from all books occurred at least once in a given book (yielding a dimensionality of 𝑑 =

1,217,078), and index this book fingerprint using the LSH Forest data structure with

MinHash. The visualization of the GUTENBERG data set exemplifies the ability of TMAP to

handle input with extremely high dimensionality (𝑑 = 1,217,078) efficiently (Fig. 6b). The

works of different authors tend to populate specific branches, with notable expected

exceptions such as the autobiography of Charles Darwin, which does not lie on the same

branch as all his other works. Meanwhile, the works of Alfred Russel Wallace are found on

subbranches of the Darwin branch.

  Related to linguistics, the TMAP webpage further features a map of the distribution of

different scientific journals (Nature, Cell, Angewandte Chemie, Science, the Journal of the

American Chemical Society, and Demography) over the entire PubMed article space (𝑛 =

327,628, 𝑑 = 1,633,762), perceiving specialization, diversification, and overlaps; as well as

a TMAP of the NeurIPS conference papers (𝑛 = 7,241, 𝑑 = 225,423), visualizing the
 19

increase in occurrence of the word “deep” in conference paper abstracts over time (1987-

2016).

Fig. 6 Visualizing linguistics, RNA sequencing, and particle physics data sets. (a) The MiniBooNE data set
(𝑛 = 130,065,  𝑑 = 50)  consists  of  measurements  extracted  from  Fermilab’s  MiniBooNE  experiment.  TMAP
visualizes the distribution of the signal data among the background. (b) The GUTENBERG data set is a selection
of books by 142 authors (𝑛 = 3,036, 𝑑 = 1,217,078). The works of five different authors are shown to occupy
distinct branches. Interactive version of these maps and further examples can be found at http://tmap.gdb.tools.

Conclusion

In this study, we introduced TMAP as a visualization method for very large, high-dimensional

data sets enabling high data interpretability by preserving and visualizing both global and

local features. By using TMAP in combination with the MHFP6 fingerprint, we can visualize

databases of millions of organic small molecules and the associated property data with a high

degree of resolution, which was not possible with previous methods. TMAP is also well-

suited to visualize arbitrary data sets such as images, text, or RNA-seq data, hinting at its

usefulness in a wide range of fields including computational linguistics or biology.

  TMAP excels with its low memory usage and running time, with performance superior

to other visualization algorithms such as t-SNE, UMAP or PCA. By adjusting the available
20

parameters and leveraging output quality and memory usage, TMAP does not require

specialized hardware for high-quality visualizations of data sets containing millions of data

points. Most importantly, TMAP generates visualizations with an empirical sub-linear time

complexity of 𝑂(𝑛0.931), allowing to visualize much larger high dimensional data sets than

previous methods.

  All the TMAP visualizations presented, including installation and usage instructions,

are available as interactive online versions (http://tmap.gdb.tools). The source code for TMAP

is available on GitHub (https://github.com/reymond-group/tmap) and a Python package can

be obtained using the conda package manager.

Acknowledgments. This work was supported financially by the Swiss National Science

Foundation, NCCR TransCure.

Conflict of interest statement. The authors declare no conflict of interest.

Author contributions. DP designed and realized the study and wrote the paper. JLR

supervised the study and wrote the paper.

References

1.  Callahan, S. P. et al. VisTrails: Visualization Meets Data Management. in Proceedings of

the 2006 ACM SIGMOD International Conference on Management of Data 745–747

(ACM, 2006). doi:10.1145/1142473.1142574.

2.  Fox, P. & Hendler, J. Changing the Equation on Scientific Data Visualization. Science 331,

705–708 (2011).

3.  Michel, J.-B. et al. Quantitative Analysis of Culture Using Millions of Digitized Books.

Science 331, 176–182 (2011).

4.  Keim, D., Qu, H. & Ma, K. Big-Data Visualization. IEEE Computer Graphics and

Applications 33, 20–21 (2013).
 21

5.  Costa, F. F. Big data in biomedicine. Drug Discovery Today 19, 433–440 (2014).

6.  Stephens, Z. D. et al. Big Data: Astronomical or Genomical? PLOS Biology 13, e1002195

(2015).

7.  Bikakis, N. & Sellis, T. Exploration and Visualization in the Web of Big Linked Data: A

Survey of the State of the Art. arXiv:1601.08059 [cs] (2016).

8.  Kahles, A. et al. Comprehensive Analysis of Alternative Splicing Across Tumors from

8,705 Patients. Cancer Cell 34, 211-224.e6 (2018).

9.  Arús-Pous, J. et al. Exploring the GDB-13 chemical space using deep generative models.

Journal of Cheminformatics 11, 20 (2019).

10.  Maaten, L. van der, Postma, E. O. & Herik, H. J. van den. Dimensionality Reduction :

A Comparative Review. J Mach Learn Res 10, 66–71 (2009).

11.  Gaulton, A. et al. The ChEMBL database in 2017. Nucleic Acids Research 45, D945–

D954 (2017).

12.  Ruddigkeit, L., van Deursen, R., Blum, L. C. & Reymond, J.-L. Enumeration of 166

Billion Organic Small Molecules in the Chemical Universe Database GDB-17. J. Chem.

Inf. Model 52, 2864–2875 (2012).

13.  Visini, R., Awale, M. & Reymond, J.-L. Fragment Database FDB-17. J. Chem. Inf.

Model. 57, 700–709 (2017).

14.  Awale, M., Visini, R., Probst, D., Arús-Pous, J. & Reymond, J.-L. Chemical Space:

Big Data Challenge for Molecular Diversity. Chimia 71, 661–666 (2017).

15.  Richard, A. M. & Williams, C. R. Distributed structure-searchable toxicity (DSSTox)

public database network: a proposal. Mutation Research/Fundamental and Molecular

Mechanisms of Mutagenesis 499, 27–52 (2002).

16.  Natural Products Atlas. https://www.npatlas.org/joomla/.

17.  Wishart, D. S. et al. DrugBank 5.0: a major update to the DrugBank database for

2018. Nucleic Acids Res. 46, D1074–D1082 (2018).
 22

18.  Wu, Z. et al. MoleculeNet: A Benchmark for Molecular Machine Learning.

arXiv:1703.00564 [physics, stat] (2017).

19.  Oprea, T. I. & Gottfries, J. Chemography: the art of navigating in chemical space. J

Comb Chem 3, 157–166 (2001).

20.  Awale, M., van Deursen, R. & Reymond, J.-L. MQN-Mapplet: Visualization of

Chemical Space with Interactive Maps of DrugBank, ChEMBL, PubChem, GDB-11, and

GDB-13. J. Chem. Inf. Model 53, 509–518 (2013).

21.  Awale, M. & Reymond, J.-L. Similarity Mapplet: Interactive Visualization of the

Directory of Useful Decoys and ChEMBL in High Dimensional Chemical Spaces. J.

Chem. Inf. Model 55, 1509–1516 (2015).

22.  Jin, X. et al. PDB-Explorer: a web-based interactive map of the protein data bank in

shape space. BMC Bioinformatics 16, 339 (2015).

23.  Awale, M. & Reymond, J.-L. Web-based 3D-visualization of the DrugBank chemical

space. J. Cheminformatics 8, (2016).

24.  Awale, M., Probst, D. & Reymond, J.-L. WebMolCS: A Web-Based Interface for

Visualizing Molecules in Three-Dimensional Chemical Spaces. J. Chem. Inf. Model 57,

643–649 (2017).

25.  Probst, D. & Reymond, J.-L. FUn: a framework for interactive visualizations of large,

high-dimensional datasets on the web. Bioinformatics 34, 1433–1435 (2018).

26.  McInnes, L., Healy, J. & Melville, J. UMAP: Uniform Manifold Approximation and

Projection for Dimension Reduction. arXiv:1802.03426 [cs, stat] (2018).

27.  Maaten, L. van der & Hinton, G. Visualizing Data using t-SNE. Journal of Machine

Learning Research 9, 2579–2605 (2008).

28.  Hinton, G. E. & Salakhutdinov, R. R. Reducing the Dimensionality of Data with

Neural Networks. Science 313, 504–507 (2006).
 23

29.  Bishop, C. M., Svensén, M. & Williams, C. K. I. GTM: The Generative Topographic

Mapping. Neural Computation 10, 215–234 (1998).

30.  Kohonen, T. Exploration of very large databases by self-organizing maps. in

Proceedings of International Conference on Neural Networks (ICNN’97) vol. 1 PL1-PL6

vol.1 (1997).

31.  Dong, W., Moses, C. & Li, K. Efficient k-nearest neighbor graph construction for

generic similarity measures. in Proceedings of the 20th international conference on World

wide web - WWW ’11 577 (ACM Press, 2011). doi:10.1145/1963405.1963487.

32.  Saitou, N. & Nei, M. The neighbor-joining method: a new method for reconstructing

phylogenetic trees. Mol Biol Evol 4, 406–425 (1987).

33.  Zhou, Z. et al. GrapeTree: visualization of core genomic relationships among 100,000

bacterial pathogens. Genome Res. 28, 1395–1404 (2018).

34.  Lu, J. & Carlson, H. A. ChemTreeMap: an interactive map of biochemical similarity

in molecular datasets. Bioinformatics 32, 3584–3592 (2016).

35.  P’ng, C. et al. BPG: Seamless, automated and interactive visualization of scientific

data. BMC Bioinformatics 20, 42 (2019).

36.  Idreos, S., Papaemmanouil, O. & Chaudhuri, S. Overview of Data Exploration

Techniques. in Proceedings of the 2015 ACM SIGMOD International Conference on

Management of Data 277–281 (ACM, 2015). doi:10.1145/2723372.2731084.

37.  Andoni, A., Razenshteyn, I. & Nosatzki, N. S. LSH Forest: Practical Algorithms Made

Theoretical. in Proceedings of the Twenty-Eighth Annual ACM-SIAM Symposium on

Discrete Algorithms 67–78 (Society for Industrial and Applied Mathematics, 2017).

doi:10.1137/1.9781611974782.5.

38.  Bawa, M., Condie, T. & Ganesan, P. LSH forest: self-tuning indexes for similarity

search. in Proceedings of the 14th international conference on World Wide Web  - WWW

’05 651 (ACM Press, 2005). doi:10.1145/1060745.1060840.
 24

39.  Kruskal, J. B. On the shortest spanning subtree of a graph and the traveling salesman

problem. Proc. Amer. Math. Soc. 7, 48–48 (1956).

40.  Chimani, M. et al. The Open Graph Drawing Framework (OGDF). Handbook of

Graph Drawing and Visualization 2011, 543–569 (2013).

41.  Broder, A. Z. On the resemblance and containment of documents. in Proceedings.

Compression and Complexity of SEQUENCES 1997 (Cat. No.97TB100171) 21–29 (1997).

doi:10.1109/SEQUEN.1997.666900.

42.  Manber, U. Finding Similar Files in a Large File System. in Usenix Winter 1994

Technical Conference 1–10 (1994).

43.  Wu, W., Li, B., Chen, L., Zhang, C. & Yu, P. S. Improved Consistent Weighted

Sampling Revisited. arXiv:1706.01172 [cs] (2017).

44.  Bajusz, D., Rácz, A. & Héberger, K. Why is Tanimoto index an appropriate choice for

fingerprint-based similarity calculations? Journal of Cheminformatics 7, 20 (2015).

45.  Probst, D. & Reymond, J.-L. A probabilistic molecular fingerprint for big data

settings. Journal of Cheminformatics 10, 66 (2018).

46.  Rogers, D. & Hahn, M. Extended-Connectivity Fingerprints. J. Chem. Inf. Model 50,

742–754 (2010).

47.  Riniker, S. & Landrum, G. A. Open-source platform to benchmark fingerprints for

ligand-based virtual screening. J. Cheminform. 5, 26 (2013).

48.  Awale, M. & Reymond, J.-L. Polypharmacology Browser PPB2: Target Prediction

Combining Nearest Neighbors with Machine Learning. J. Chem. Inf. Model. 59, 10–17

(2019).

49.  BindingDB. BindingDB Entry 6310: Compounds and compositions as Syk kinase

inhibitors. (2014) doi:10.7270/q24q7sns.

50.  Wang, J., Shen, H. T., Song, J. & Ji, J. Hashing for Similarity Search: A Survey.

arXiv:1408.2927 [cs] (2014).
 25

51.  Marcais, G., DeBlasio, D., Pandey, P. & Kingsford, C. Locality sensitive hashing for

the edit distance. http://biorxiv.org/lookup/doi/10.1101/534446 (2019)

doi:10.1101/534446.

52.  Probst, D. & Reymond, J.-L. SmilesDrawer: Parsing and Drawing SMILES-Encoded

Molecular Structures Using Client-Side JavaScript. J. Chem. Inf. Model 58, 1–7 (2018).

53.  Ramakrishnan, R., Hartmann, M., Tapavicza, E. & Lilienfeld, O. A. von. Electronic

spectra from TDDFT and machine learning in chemical space. The Journal of Chemical

Physics 143, 084111 (2015).

54.  Berman, H. M. et al. The Protein Data Bank. Nucleic Acids Res 28, 235–242 (2000).

55.  Awale, M. & Reymond, J.-L. Atom Pair 2D-Fingerprints Perceive 3D-Molecular

Shape and Pharmacophores for Very Fast Virtual Screening of ZINC and GDB-17. J.

Chem. Inf. Model 54, 1892–1907 (2014).

56.  The Cancer Genome Atlas Research Network et al. The Cancer Genome Atlas Pan-

Cancer analysis project. Nature Genetics 45, 1113–1120 (2013).

57.  Kustatscher, G. et al. Co-regulation map of the human proteome enables identification

of protein functions. Nat Biotechnol 37, 1361–1371 (2019).

58.  Hanley, M. B., Lomas, W., Mittar, D., Maino, V. & Park, E. Detection of Low

Abundance RNA Molecules in Individual Cells by Flow Cytometry. PLOS ONE 8, e57002

(2013).

59.  Roe, B. P. et al. Boosted Decision Trees as an Alternative to Artificial Neural

Networks for Particle Identification. Nuclear Instruments and Methods in Physics Research

Section A: Accelerators, Spectrometers, Detectors and Associated Equipment 543, 577–

584 (2005).

60.  Bernhardsson, E. Annoy (Approximate Nearest Neighbors Oh Yeah).

https://github.com/spotify/annoy.
 26

61.  Lahiri, S. Complexity of Word Collocation Networks: A Preliminary Structural

Analysis. arXiv:1310.5111 [physics] (2013).

 27

Supplementary Information

Fig. S1 Influence of LSH Forest parameters 𝒅 and 𝒍 on visualization of MNIST. While phase I of the algorithm
mainly  influences  the  preservation  of locality  (Fig.  S6), extreme  values  where  𝑑 ≈ 𝑙  lead  to  a  deterioration  of
visualization quality.

 28

Fig.  S2  Influence  of  LSH  Forest  parameters  𝒌  and  𝒌𝒄  on  visualization  of  MNIST.  Whereas  parameter  𝑘
directly influences the average degree of the 𝑘-nearest neighbor graph, 𝑘𝑐 increases the quality of the returned 𝑘
nearest neighbors. Both parameters only marginally influence the aesthetics and quality of the visualization.

 29

Fig. S3 Influence of parameter 𝒑 on visualization of MNIST. The point size parameter 𝑝 has major influence
on the aesthetics of the visualization, as it controls the sparseness of the drawn tree. Decreasing the point size and
thus the repulsive force between two points, allows the layout algorithm to draw points closer to their respective
(sub) branches.

 30

Fig. S4 Examples of 2D embeddings of points sampled from the surface of 2-spheres by TMAP and
UMAP. (a, b, c) Colored by the points x-components in the original 3-dimensional Euclidean space, (d, e, f)
colored by longitude. (a) Randomly distributed points picked from the surface of a 2-sphere were embedded on
the two-dimensional plane by TMAP (b) and UMAP (c) using an angular metric in 0.859s and 2.96s wall-clock
time respectively. Both algorithms were run with their respective nearest neighbor parameters set to 10. The
results clarify the intrinsic need to break locality when embedding unbounded closed surfaces. (d) The location
of cities with a population higher than 1,000 (𝑛 = 47980) mapped to a sphere. (e) TMAP and (f) UMAP
embeddings of the city-representing points in a 2D plane. The colors roughly represent Europe and Africa
(green), India and central Asia (yellow), east Asia (orange), Oceania (red), and the Americas (blue). Using a
Euclidean metric, the execution time of the algorithms was 18.566s and 218.528s, respectively. A detailed view
of the Bering Strait (white arrows) in original 3D space with TMAP edges added (g) embedded by TMAP (h)
and UMAP (i) highlights the differences between the two approaches. As laying out a graph is vastly more
complex than laying out a tree, UMAP produces embedding errors such as the placement of Sardinian cities
surrounded by North American cities (red arrow).

 31

Fig. S5 Locality-preservation in 2D embeddings of 𝒏-spheres by TMAP and UMAP. Random points were
uniformly picked from the surface of (𝑛 − 1)-spheres with 𝑛 ∈ {3, 10, 100, 1000}. In addition, the number of
points were varied between 100 and 1,000. These examples represent edge cases due to the nature of high
dimensional hyperspheres. For each point, the 10 nearest neighbors in the original 𝑛-dimensional space were
compared to their ranked distance in the 2-dimensional plane. As the topological distance cannot be directly
compared to the two Euclidean distances given the very high likeliness of collisions at any given (topological)
distance due to branching, the average topological distance between any two points was included (blue dashed
line).The quality in locality preservation of both TMAP and UMAP degenerates quickly in higher dimensions,
however, TMAP tends to preserve the two nearest neighbors even when embedding very high dimensional data.

 32

Fig. S6 Ranked distance from true nearest neighbor when visualizing the MNIST data set. Ranked
distances from true nearest neighbor in original high dimensional space after projection based on topological and
Euclidean distance for the MNIST data set. Whereas UMAP preserves less than 10% of true 1-nearest neighbors,
TMAP preserves more than 80% based on topological and more than 35% based on Euclidean distance.

Fig. S7 Influence of TMAP parameters on locality preserving performance. Ranked distances from true
nearest neighbor in original high dimensional space after projection based on topological and Euclidean distance
for the MNIST data set. While, parameters 𝑑 and 𝑙 (a, b) have a major influence on both, the topological and
Euclidean measure of locality preserving performance, parameters 𝑘 and 𝑘𝑐 have only marginal influence (c, d).
The point size 𝑝 does not influence topological distances; however, it has a minor effect on the Euclidean
distance-based metric, as higher values increase the sparsity of the drawn tree.

 33

Fig. S8 Stability of TMAP. Algorithms TMAP (a, c) and UMAP (b, d) have been repeatedly (𝑛 = 4) run on the
same data sets with the same parameters. Whereas the output of TMAP is perceived as identical in all instances,
the results yielded by UMAP show considerable differences between each run.
