# Librarian cycle report — reference library

## The problem being supported

Singmaster's conjecture (N(a) bounded by an absolute constant B, for a > 1,
counting both mirrors plus the trivial pair; N(3003)=8 witness set). Goal:
build and maintain the reference library under research/ so the run reasons
from held sources, not from the model's memory.

## State at cycle start

The library was already substantial on disk (60+ full texts under
research/sources/): all the modern primaries (MRSTT 2021 full text, Matveev
2000, BST 1999, BMSST 2008, Blokhuis–Brouwer–de Weger 2017, GRKTU 2020, HPTV
2014, Jenkins 2014, Lind 1968, Singmaster 1975 FQ, AEH 1974, Kane 2004/2007,
Lane Clark 2010, Cassou-Noguès–Płoski 2012 were absent). ROOT.md stated the
minimal-counterexample structure, the verification bound (2^48 primary +
Blokhuis 10^6/10^60), and three restricted settled classes. The consent in
CONTEXT.md said "01+ sources" but the state files' own tally was 37 full
texts; the disk listing showed ~64.

## The gates the state files did not meet

- `research/REQUESTS.md` **did not exist on disk** even though FRONTIER.md and
  the brief reference it — created this cycle with the open gaps laid out.
- `CLAIMS.md` (43 rows) had 20 "load-bearing but unverified" `asserted` rows
  and a `deweger-1995` contradiction cluster; the five "newer speculatives"
  in APPROACHES said no capture/check yet.
- FRONTIER.md's top rows were degraded: OEIS nav links (6×) and the
  corrupt-download "triangulation of smooth fibre bundles" IMPAN rows (3×)
  crowded out genuine leads; the two Monthly primaries were confirmed
  paywalled (JSTOR 2316907, 2319526).

## What this cycle added

**Latest (July 2025 search confirmed)**: no genuine peer-reviewed resolution
of Singmaster exists; recent items are Zenodo crank "proofs" (Okolo 2025,
Keen 2026, Hall 2026 research log), the Stirling-number analogue (Bazsó et al.
2025), and Tian's k=2 factorization conjecture (MDPI 2026). None is a source
for a uniform bound.

**Five primaries + one landing page fetched, filed, summarized, indexed**:

1. **Kiss 1988** (Fibonacci Quart. 26(2) 127–130) — full text readable this
   run. Theorem: for each fixed odd prime p ≥ 3, C(y,p)=C(x,2) has only
   finitely many positive integer solutions, **effectively** via Baker 1969 on
   z² = (8/p!)(x)_p + 1 (degree-p polynomial with only simple roots, Eisenstein
   argument) — per-p effective, **not uniform in k**. Also records Avanesov's
   complete (2,3) list.
2. **Tovey 1985** (Fibonacci Quart. 23(4) 356–358) — full text read. Proves
   completeness of the Fibonacci parametrization of the repeated-coefficient
   family; notes seven small multiple occurrences (3003 only 3-way proper).
   Caveat recorded: displayed equations are images; the exact variable
   dictionary with the run's n,k formulas was NOT re-derived from this scan —
   the family identity stands on the run's own verification and the
   Lind/Singmaster primaries.
3. **Cassou-Noguès–Płoski 2012** (arXiv:1207.1600) — tool reference for the
   live `G-delta-invariant` task: 2δ = μ + r − 1 (Milnor formula), δ computable
   from Newton diagram/Puiseux — the mechanism to prove the genus closed form.
4. **Avanesov 1967** (Acta Arith. 12, 409–420) — landing page held; the PDF is
   a textless 1967 scan (recorded, not retried). The five-pair complete list
   for C(x,3)=C(y,2) is attested via Kiss 1988 (verbatim quote) + GRKTU 2020.
5. **Acta Arith. Volume 12 issue listing** — 104 citations added to the
   frontier (which shifted its top: OEIS nav-links now 6→7, IMPAN penalty).

**Created**: `research/REQUESTS.md` (gap register with falsifiers;
Singmaster-1971 row marked blocked, Avanesov row closed-as-attested, Matveev
constant and delta-invariant rows marked compute-tasks not fetches).

**Stored in Cognee (durable)**: the Kiss-1988 theorem + Avanesov list, the
Tovey completeness + caveat, the Cassou-Noguès–Płoski tool reference, and the
Avanesov-1967 citation + textless-PDF state.

**Honesty corrections made**: my first Tovey summary overstated a "variable
dictionary cross-confirmed via Kiss 1988" — corrected to "NOT re-derived from
the scan"; the family identity itself is independently verified elsewhere.

## Known good URLs used (each seen in a search result or held document)

- FQ archive scans: `https://www.fq.math.ca/Scanned/23-4/tovey.pdf`,
  `https://www.fq.math.ca/Scanned/26-2/kiss.pdf` (worked).
- IMPAN Acta Arith. all-issues and article pages (worked); the freeshare PDF
  download parses as textless (blocked).
- arXiv abs page for 1207.1600 (worked, 39 citations fed).
- MDPI, CiteSeerX, JSTOR/tandfonline (blocked: 403 / connection / paywall).

## Gaps still open, and the angle each closes

- **Singmaster 1971 body** — blocked (paywall). Attested via held 1975 FQ
  primary. Do not re-fetch.
- **Avanesov 1967 body** — blocked (textless scan). List attested via two held
  full texts. Do not re-download.
- **Effective Matveev-2000 constant for a small pair** — a compute task, not a
  fetch (BACKWARD.md `G-matveev-kummer-check`, `G-constant-evaluation`); the
  primaries for it (Matveev 2000, Kiss 1988's Baker-1969 reduction, BMSST
  2008's worked hyperelliptic examples) are all held.
- **Delta-invariant proof** — a compute/proof task (BACKWARD.md
  `G-delta-invariant`); tool reference now held.
- **Tian 2025 / Goetgheluck 1998** — context-only; both blocked or skipped,
  neither load-bearing.

## Recommended next cycle (by the consensus files, not self-invented)

Threads `diophantine-curves` (next: "prove genus formula via involution +
Riemann-Hurwitz + singularity count (directive 10)") and `binary-digit` (next:
"scan odd binomial coefficients for n <= 2^18") are the two live attack
threads. The library now carries what each needs: the genus tool reference
(CN-P) and the k=2-column effective-finiteness primary (Kiss 1988). A
librarian cycle could also, on request, chase the earliest missing primary
still fetchable (e.g. Lind 1968 is held; the original 1971 Monthly's PDF is
paywalled and tombstoned — nothing on the frontier top is actionable).

When a cycle has no open request and no actionable frontier row, the response
is NOTHING FURTHER.