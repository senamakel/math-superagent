<!-- source: http://abel.math.umu.se/~klasm/Data/cubicavoid.html | converted from HTML -->

Cubic graphs without given cycles

---

#### Cubic graphs avoiding cycles of given lengths

- All graphs are stored in the Graph6-format, see Brendan Mackay's webpage for documentation on this format. The graphs were constructed by an exahustive search for each number of vertices using a modified version of Gunnar Brinkmann's generator for cubic graphs minibaum.
For small N the search was laso done by using an unmodified version of minibaum together with a Fortran90-program which filtered out graphs with unwanted cycles.
- In a file named
cubic_noX_Y_Z_..._nN.g6
you will find all 3-connected cubic graphs on N vertices which do not contain cycles of length X, Y, Z...
- I have done a complete search for these graphs up to the largest N given here for each given combination of cycle lengths. So if there is no file for a given N this means that there are no 3-connected cubic graphs on that many vertices avoiding the given cycles.
- I have looked for cubic graphs with no cycles of lengths 4,8,16. If have found no such graphs and have searched all N this paper for more information. Geoff Exoo has found a [graph][1] of this kind with 78 vertices.
- I have done a search for the smallest graphs with no cycles of lengths 4,6,8,10,12. I have searched up to N Geoff Exoo has also found [several][1] other graphs avoiding certain cycles length, some of which are now known to be the smallest of their kind by this exhaustive search.

The [graphs][2].

---


## Links

[1]: http://isu.indstate.edu/ge/COMBIN/CYCLES/index.html
[2]: cubicavoidcycle/
