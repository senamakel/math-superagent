> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/arjunbalaji-cegar-sat.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://raw.githubusercontent.com/ArjunBalaji79/erdos-gyarfas-min-degree-3/main/erdos_gyarfas/sat/cegar.py | converted from plain text -->

"""The CEGAR loop.

    loop:
        model = SAT(base & min3 & structural(a) & lex_canon & refinements)
        if UNSAT: return UNSAT
        G = decode(model)
        bad = power_of_2_cycle_detector(G)   # the sole certifier
        if bad is None: return SAT, G        # a real counterexample
        refinements &= forbid(bad)

The detector is never weakened: a model that survives it is a genuine
counterexample and the search halts loudly.
"""
from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

from pysat.solvers import Solver

from .base import add_min3, base_cnf, decode
from .detector import find_power_of_2_cycle
from .encoding import edge_var
from .structural import add_c4_free, add_lex_canon, add_property_a

@dataclass
class SearchResult:
    n: int
    status: str                       # "UNSAT" | "SAT" | "WALL"
    refinements: int = 0
    elapsed: float = 0.0
    counterexample: Optional[List[Tuple[int, int]]] = None
    config: Dict = field(default_factory=dict)
    # Verification artefacts (populated when requested):
    certificate: Optional[List[Tuple[int, List[Tuple[int, int]]]]] = None
    # each entry = (cycle_length, [edges]) of a forbidden power-of-2 cycle
    recheck: Optional[str] = None     # independent second-solver verdict on UNSAT

def build_formula(
    n: int,
    use_property_a: bool = True,
    use_lex: bool = True,
    use_c4free: bool = False,
) -> Tuple[List[List[int]], Dict[int, List[int]]]:
    """Assemble the static part of the formula (everything except refinements)."""
    cnf, incident, pool = base_cnf(n)
    add_min3(cnf, incident, n, pool)
    if use_property_a:
        add_property_a(cnf, incident, n, pool)
    if use_c4free:
        add_c4_free(cnf, n)
    if use_lex:
        add_lex_canon(cnf, n, pool)
    return cnf, incident

def recheck_unsat(
    n: int,
    certificate,
    use_property_a: bool = True,
    use_lex: bool = True,
    use_c4free: bool = False,
    solver_name: str = "glucose42",
) -> str:
    """Independently re-prove UNSAT from a recorded certificate.

    Rebuilds the static formula and re-adds one forbidding clause per certificate
    cycle, then solves with a DIFFERENT backend. Returns "UNSAT" (agrees) or
    "SAT(!)" (disagreement -- would mean the primary solver erred). Decoupled from
    ``search`` so the primary result can be persisted *before* this runs.
    """
    cnf, _ = build_formula(n, use_property_a, use_lex, use_c4free)
    s = Solver(name=solver_name, bootstrap_with=cnf)
    for _length, edges in certificate:
        s.add_clause([-edge_var(u, v, n) for (u, v) in edges])
    verdict = "UNSAT" if not s.solve() else "SAT(!)"
    s.delete()
    return verdict

def search(
    n: int,
    use_property_a: bool = True,
    use_lex: bool = True,
    use_c4free: bool = False,
    time_budget: Optional[float] = None,
    max_refinements: Optional[int] = None,
    solver_name: str = "cadical195",
    record_certificate: bool = False,
    recheck_solver: Optional[str] = None,
    recheck_max_refinements: int = 60000,
) -> SearchResult:
    """Run CEGAR for a single order n.

    ``time_budget`` (seconds) and ``max_refinements`` are stopping rules; if
    either is hit before resolution the status is "WALL". ``solver_name`` selects
    the PySAT backend (e.g. "glucose4", "glucose42", "cadical195", "minisat22").

    Verification:
    * ``record_certificate`` collects every forbidden cycle (length + edges) so
      each refinement is an auditable lemma (see ``verify.verify_result``).
    * ``recheck_solver`` (e.g. "glucose42") re-solves the final accumulated
      formula with an independent backend to confirm an UNSAT verdict is not a
      single-solver artefact.
    """
    config = dict(

*[excerpt ends; 2170 characters not shown — see `research/sources/arjunbalaji-cegar-sat.full.md`]*
