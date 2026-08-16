<!-- source: https://github.com/bsubercaseaux/automatic-symmetries | converted from HTML -->

GitHub - bsubercaseaux/automatic-symmetries: Code associated to CICM'2025 submission "Automated Symmetric Constructions in Discrete Geometry". · GitHub

Skip to content

You signed in with another tab or window. [Reload][1] to refresh your session. You signed out in another tab or window. [Reload][1] to refresh your session. You switched accounts on another tab or window. [Reload][1] to refresh your session. Dismiss alert

{{ message }}

[bsubercaseaux][2] /**[automatic-symmetries][3]**Public

- [Notifications][4] You must be signed in to change notification settings
- [Fork 0][4]
-

[Star 2][4]

[3]

main

[Branches][5] [Tags][6]

[5] [6]

Go to file

Code

Open more actions menu

## Folders and files

Name | Name |

Last commit message

 |

Last commit date

 |

## Latest commit

## History

[6 Commits][7]

[7] 6 Commits

 |

[encoders][8]

 |

[encoders][8]

 |

 |

 |

[experiments][9]

 |

[experiments][9]

 |

 |

 |

[formulas][10]

 |

[formulas][10]

 |

 |

 |

[orientations][11]

 |

[orientations][11]

 |

 |

 |

[realizations][12]

 |

[realizations][12]

 |

 |

 |

[scripts][13]

 |

[scripts][13]

 |

 |

 |

[solutions][14]

 |

[solutions][14]

 |

 |

 |

[.gitignore][15]

 |

[.gitignore][15]

 |

 |

 |

[README.md][16]

 |

[README.md][16]

 |

 |

 |

View all files

 |

## Repository files navigation

# Automated Symmetric Constructions in Discrete Geometry

Code corresponding to our CICM'2025 submission "Automated Symmetric Constructions in Discrete Geometry". This is joint work of Bernardo Subercaseaux, Ethan Mackey, Long Qian, and Marijn Heule.

## Requirements

For SAT encodings in Python, we use the `eznf`and `PySAT`libraries. They can be installed by

```
pip install eznf
pip install python-sat
```

For enumerating solutions, we use `allsat-cadical`( [https://github.com:jreeves3/allsat-cadical][17]). When we refer to the `allsat`executable, we mean the file `cadical`in the `build`directory of the `allsat-cadical`repository after running `./configure && make`in that directory.

For the realizability problem we use the `Localizer`solver ( [https://github.com/bsubercaseaux/localizer][18]). We will assume that `localizer`is the executable in your path.

## Symmetries in the Erdős-Szekeres problem

To generate the 66 pointsets with 16 points and no 6-point convex subset that are 4-fold symmetric, run

```
sh experiments/16-6-4sym.sh <path to allsat> <path to localizer>
```

This should take no more than a couple of minutes, and should leave the realizations in the `realizations`folder. The filenames indicate the number of convex 4-gons, convex 5-gons, and convex 6-gons in the pointset, and then the index, respectively.

For the 932 solutions with a 5-fold symmetry, run

```
sh experiments/16-6-5sym.sh <path to allsat> <path to localizer>
```

This should take under 20 minutes.

## Symmetries in the Everywhere-unbalanced-points problem

To generate an s-fold symmetric pointset with n points and an unbalance of k, run

```
python3 encoders/everywhere_unbalanced.py -n <n> -k <k> -s <s>
```

For example, running `python3 encoders/everywhere_unbalanced.py -n 21 -k 2 -s 3`will encode the existence of a set of 15 points with an unbalance of 2 and a 3-fold symmetry, as depicted in the paper. The solver ( [https://github.com/arminbiere/kissat][19]) can solve this instance in about 10 seconds. In turn, the instance resulting from `python3 encoders/everywhere_unbalanced.py -n 21 -k 2 -s 1`, where no non-trivial symmetries are enforced (any pointset has a 1-fold symmetry), is much harder to solve.

In terms of the minimality, we use a different encoder for obtaining UNSAT results. Namely, `python3 encoders/everywhere_unbalanced_unsat.py -n 11 -k 2 `will generate an instance which can be proved unsatisfiable in under a second, while `-n 13`takes a few seconds. The instance for `-n 15`takes under a minute, while `-n 17`takes about 20 minutes. The instance for `-n 19`took 110 CPU hours with `kissat`.

## Automated proof of Proposition 4.2

The file `scripts/axiom_proof.py`generates the SAT instance described in the proof of Proposition 4.2, which is unsatisfiable. To generate it simply run

```
python3 scripts/axiom_proof.py
```

after which the file `axiom_proof_5.cnf`will be created.

## About

Code associated to CICM'2025 submission "Automated Symmetric Constructions in Discrete Geometry".

### Resources

Readme

[Activity][20]

### Stars

**2**stars

### Watchers

**0**watching

### Forks

****[0 forks][21]

[Report repository][22]

## Releases

## Packages

## Contributors

## Languages

You can’t perform that action at this time.


## Links

[1]: 
[2]: /bsubercaseaux
[3]: /bsubercaseaux/automatic-symmetries
[4]: /login?return_to=%2Fbsubercaseaux%2Fautomatic-symmetries
[5]: /bsubercaseaux/automatic-symmetries/branches
[6]: /bsubercaseaux/automatic-symmetries/tags
[7]: /bsubercaseaux/automatic-symmetries/commits/main/
[8]: /bsubercaseaux/automatic-symmetries/tree/main/encoders
[9]: /bsubercaseaux/automatic-symmetries/tree/main/experiments
[10]: /bsubercaseaux/automatic-symmetries/tree/main/formulas
[11]: /bsubercaseaux/automatic-symmetries/tree/main/orientations
[12]: /bsubercaseaux/automatic-symmetries/tree/main/realizations
[13]: /bsubercaseaux/automatic-symmetries/tree/main/scripts
[14]: /bsubercaseaux/automatic-symmetries/tree/main/solutions
[15]: /bsubercaseaux/automatic-symmetries/blob/main/.gitignore
[16]: /bsubercaseaux/automatic-symmetries/blob/main/README.md
[17]: https://github.com:jreeves3/allsat-cadical
[18]: https://github.com/bsubercaseaux/localizer
[19]: https://github.com/arminbiere/kissat
[20]: /bsubercaseaux/automatic-symmetries/activity
[21]: /bsubercaseaux/automatic-symmetries/forks
[22]: /contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fbsubercaseaux%2Fautomatic-symmetries&amp;report=bsubercaseaux+%28user%29
