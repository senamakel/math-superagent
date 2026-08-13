<!-- source: https://github.com/michaelmross/Gilbreath | converted from HTML -->

GitHub - michaelmross/Gilbreath · GitHub

Skip to content

You signed in with another tab or window. [Reload][1] to refresh your session. You signed out in another tab or window. [Reload][1] to refresh your session. You switched accounts on another tab or window. [Reload][1] to refresh your session. Dismiss alert

{{ message }}

[michaelmross][2] /**[Gilbreath][3]**Public

- [Notifications][4] You must be signed in to change notification settings
- [Fork 0][4]
-

[Star 0][4]

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

[21 Commits][7]

[7] 21 Commits

 |

[data][8]

 |

[data][8]

 |

 |

 |

[plots][9]

 |

[plots][9]

 |

 |

 |

[src][10]

 |

[src][10]

 |

 |

 |

[LICENSE][11]

 |

[LICENSE][11]

 |

 |

 |

[README.md][12]

 |

[README.md][12]

 |

 |

 |

[requirements.txt][13]

 |

[requirements.txt][13]

 |

 |

 |

View all files

 |

## Repository files navigation

# Empirical Structure of the Gilbreath Decay Constants

Companion repository for the note *Empirical Structure of the Gilbreath Decay Constants*(M. M. Ross, July 2026, [zenodo.21326025][14]), a computational study of open questions raised by Chase, Hunter, and Tao (CHT), *Gilbreath's conjecture: a Cramér random model and a deterministic analysis*( [arXiv:2607.08712][15]). OEIS: [A397880][16] and [A395556][17].

[image: DOI] [18]

## Findings

For the CHT stationary model (iid Exp(1) top row, `c_i = E a(i,j)`):

1. **Digit-sum law.**`c_i ≈ C·λ^{s₂(i)}/i`, where `s₂(i)`is the binary digit sum. The `1/i`envelope holds within fixed digit-sum classes; the effective `λ`drifts through ≈1.14–1.20 at accessible depths, so no closed-form constant is claimed. At extreme digit sums the modulation saturates below its geometric extrapolation.
2. **New exact values.**`c₄ = 778959731701/1447295850000`, plus exact `c₅`and `c₆`(see `data/exact_values.json`), extending the exactly computed values of CHT (which ends at `c₃ = 227/288`). Certified by an exact partition-of-unity identity and independent Monte Carlo.
3. **Growth threshold.**For `a_j ~ Unif[0, R(j)]`, every tested polynomial rate is subcritical at accessible depths while every tested exponential rate (down to `2^{j/64}`) is supercritical — probing the linear-vs-exponential gap CHT describe as difficult to narrow. This is a family-specific finding, not a worst-case one.
4. **Transient laws.**Full-row grind-down time `τ(G) ≍ G^{0.63–0.66}`(not logarithmic); a spike of amplitude `G`in a diverse background decays at ≈1 unit per column and survives to distance `d*(G) ≈ G`.

## Layout

```
plots/    generated figures
src/      all generating code
data/     raw Monte Carlo data, figure data, exact-value certificates
```

### Source files

file | purpose |

`src/exact_ci.py` | exact rational `c_i`by sign-cone decomposition (needs GMP-enabled pycddlib) |

`src/lambda_analysis.py` | digit-sum law analysis on the Monte Carlo datasets |

`src/cht_experiments.py` | deep `c_i`Monte Carlo + growth-threshold scan |

`src/grind_down.py` | transient experiments: τ(G), spike decay, d*(G), conservation classes |

`src/make_figures.py` | regenerates all three manuscript figures from `data/` |

## Reproducing

```
pip install -r requirements.txt

# smoke tests (exact pipeline must reproduce CHT's values)
python3 src/exact_ci.py 2        # -> 7/9
python3 src/exact_ci.py 3        # -> 227/288

# new exact constants
python3 src/exact_ci.py 4
python3 src/exact_ci.py 5
python3 src/exact_ci.py 6 --workers 8    # ~2M sign patterns

# analyses and figures from the shipped data
python3 src/lambda_analysis.py           # run from data/ or adjust paths
python3 src/make_figures.py

# regenerate raw experiments (stochastic; seeds fixed in-script)
python3 src/cht_experiments.py
python3 src/grind_down.py
```

**Note on `exact_ci.py`:**it requires pycddlib built with GMP (`import cdd.gmp`must succeed). Official Windows wheels lack GMP; use WSL/Linux (`apt install libcdd-dev libgmp-dev && pip install pycddlib`) or a conda environment providing it. Without GMP the script refuses to run unless `--allow-float`is passed, and results are then approximate.

The exact `c₄`–`c₆`runs print a `volume check: 1`line — an exact partition-of-unity identity over all sign cones that serves as the correctness certificate for each value.

## Related

- Companion note on the parity mechanism: **[Is Gilbreath's conjecture garden-variety numerology?][19]
- Z. Chase, *A random analogue of Gilbreath's conjecture*, Math. Ann. **388**(2024), 2611–2625.

## License

MIT (see `LICENSE`).

## About

No description, website, or topics provided.

### Resources

Readme

MIT license

[Activity][20]

### Stars

**0**stars

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
[2]: /michaelmross
[3]: /michaelmross/Gilbreath
[4]: /login?return_to=%2Fmichaelmross%2FGilbreath
[5]: /michaelmross/Gilbreath/branches
[6]: /michaelmross/Gilbreath/tags
[7]: /michaelmross/Gilbreath/commits/main/
[8]: /michaelmross/Gilbreath/tree/main/data
[9]: /michaelmross/Gilbreath/tree/main/plots
[10]: /michaelmross/Gilbreath/tree/main/src
[11]: /michaelmross/Gilbreath/blob/main/LICENSE
[12]: /michaelmross/Gilbreath/blob/main/README.md
[13]: /michaelmross/Gilbreath/blob/main/requirements.txt
[14]: https://doi.org/10.5281/zenodo.21326025
[15]: https://arxiv.org/abs/2607.08712
[16]: https://oeis.org/A397880
[17]: https://oeis.org/A395556
[18]: https://doi.org/10.5281/zenodo.21536389
[19]: https://michaelmross.github.io/gilbreath-parity-note.html
[20]: /michaelmross/Gilbreath/activity
[21]: /michaelmross/Gilbreath/forks
[22]: /contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fmichaelmross%2FGilbreath&amp;report=michaelmross+%28user%29
