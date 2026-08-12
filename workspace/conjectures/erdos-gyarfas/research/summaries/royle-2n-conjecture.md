<!-- source: https://web.archive.org/web/2020/http://www.cs.uwa.edu.au/~gordon/remote/erdosconj.html | converted from HTML -->

The 2^n conjecture

# The 2^n conjecture

## Conjecture

Every graph with minimum degree at least 3 contains a cycle whose length is a power of 2.

### Source

This is supposedly due to Erdos, who is also reputed to offer a cash prize for its resolution. Bert Randerath has kindly supplied me with the information that this conjecture is in fact due to Erdos and Gyarfas, and was presented by Erdos at the 1995 South-Eastern conference at Boca Raton. Erdos offered $100 for a proof and $50 for a counterexample.

---

## Negative results

I have checked this conjecture for graphs on up to 15 vertices. Brendan McKay's graph generating program makeg was altered to only construct graphs X with the following properties:

- Minimum degree of X is three.
- No edges join two vertices of degree greater than three.
- There are no 4-cycles in X

The graphs so constructed are then examined for 8-cycles. In addition to this it is clear that the condition minimum degree three can be relaxed to allow at most one vertex of minimum degree two, because then a 1-connected counterexample can be constructed by using three copies of X joined to a single central vertex.

The following table shows the number of graphs satisfying the conditions. All contain an abundance of 8-cycles.

Vertices  | Number with
minimum degree 3  | Number with
at most one vertex
of degree two  |

9 | 0 | 1 |

10 | 4 | 8 |

11 | 5 | 31 |

12 | 27 | 158 |

13 | 138 | 987 |

14 | 775 | 6281 |

15 | 5369 | ? |

---

## Comments

Maybe its true after all. More likely any counterexample will have to be very large and probably not accessible to a simple-minded computer search. Maybe I just shouldn't waste time with Erdos conjectures. Who knows?
