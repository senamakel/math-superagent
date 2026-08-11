> **Excerpt only — read this first.** The complete text is one level down at `research/L0/plackett_luce_model_wikipedia.full.full.md`; open that only when this file does not answer the question, because it is large. Replace this excerpt with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://en.wikipedia.org/wiki/Plackett%E2%80%93Luce_model | converted from HTML -->

Bradley–Terry model - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

(Redirected from [Plackett–Luce model][1])

Statistical model for pairwise comparisons

The **Bradley–Terry model**is a [probability model][2] for the outcome of pairwise comparisons between items, teams, or objects. Given a pair of items i and j drawn from some [population][3], it estimates the probability that the [pairwise comparison][4] ''j''"}},"i":0}}]}'/>*i*> *j*turns out true, as

\\Pr(i > j) = \\frac{p_i}{p_i + p_j},</math>"},"3":{"wt":"{{EquationRef|1}}"}},"i":0}}]}'>

j) = \\frac{p_i}{p_i + p_j},"}}'> j)={\frac {p_{i}}{p_{i}+p_{j}}},}"> Pr ( i > j) = p i p i + p j, {\displaystyle \Pr(i>j)={\frac {p_{i}}{p_{i}+p_{j}}},} j)={\frac {p_{i}}{p_{i}+p_{j}}},}"/> |  | 1 |

where i</sub>"}},"i":0}}]}'/> p i is a positive [real-valued][5] score assigned to individual i. The comparison ''j''"}},"i":0}}]}'/>*i*> *j*can be read as " i is preferred to j ", " i ranks higher than j ", or " i beats j ", depending on the application.

For example, i</sub>"}},"i":0}}]}'/> p i might represent the skill of a team in a sports tournament and j)"}}'> j)}"> Pr ( i > j) {\displaystyle \Pr(i>j)} j)}"/> the probability that i wins a game against j. [1] [2] Or i</sub>"}},"i":0}}]}'/> p i might represent the quality or desirability of a commercial product and j)"}}'> j)}"> Pr ( i > j) {\displaystyle \Pr(i>j)} j)}"/> the probability that a consumer will prefer product i over product j.

The Bradley–Terry model can be used in the forward direction to predict outcomes, as described, but is more commonly used in reverse to infer the scores i</sub>"}},"i":0}}]}'/> p i given an observed set of outcomes. [2] In this type of application i</sub>"}},"i":0}}]}'/> p i represents some measure of the strength or quality of i {\displaystyle i}[image: {\displaystyle i}] and the model lets us estimate the strengths from a series of pairwise comparisons. In a survey of wine preferences, for instance, it might be difficult for respondents to give a complete ranking of a large set of wines, but relatively easy for them to compare sample pairs of wines and say which they feel is better. Based on a set of such pairwise comparisons, the Bradley–Terry model can then be used to derive a full ranking of the wines.

Once the values of the scores i</sub>"}},"i":0}}]}'/> p i have been calculated, the model can then also be used in the forward direction, for instance to predict the likely outcome of comparisons that have not yet actually occurred. In the wine survey example, for instance, one could calculate the probability that someone will prefer wine i {\displaystyle i}[image: {\displaystyle i}] over wine j {\displaystyle j}[image: {\displaystyle j}], even if no one in the survey directly compared that particular pair.

## History and applications

[[edit][6]]

The model is named after [Ralph A. Bradley][7] and Milton E. Terry, [3] who presented it in 1952, [4] although it had already been studied by [Ernst Zermelo][8] in the 1920s. [1] [5] [6] Applications of the model include the ranking of competitors in sports, [chess][9], and other competitions, [7] the ranking of products in paired comparison surveys of [consumer choice][10], analysis of [dominance hierarchies][11] within animal and human communities, [8] ranking of [journals][12], ranking of AI models, [9] and is foundational to the field of training reward models in [reinforcement learning from human feedback][13]. [10] It also plays a role in the estimation of the relevance of documents in [machine-learned][14] [search engines][15]. [11]

## Definition

[[edit][16]]


*[excerpt ends; 28749 characters not shown — see `research/L0/plackett_luce_model_wikipedia.full.full.md`]*
