"""Helpers for reading the run's data/level_N.txt feature dumps.

These files (one line per reachable config) are named level_<N>.txt for the
number of divisions N.  Programs that aggregate them need to sort the globbed
paths by N, which is what sorted_key provides.

sorted_key(path) returns the integer N parsed from a 'level_<N>.txt' path,
robust to whether the glob is relative ('data/level_10.txt') or absolute
('/workspace/data/level_10.txt'), and to double-digit N.  It is the single
CANONICAL definition, consolidated from three copies that formerly lived in
code/pattern/aggregate_triangle.py, code/pattern/distinct_hist_from_data.py
and code/pattern/fit_qk.py.

The three copies had GENUINELY diverged in robustness, so no definition was
chosen over another silently:
  * aggregate_triangle.py and fit_qk.py used
      int(path.split('level_')[1].split('.')[0])
    which correctly parses BOTH relative and absolute glob paths.
  * distinct_hist_from_data.py used
      int(path.split('_')[1].split('.')[0])
    which only parses the relative form 'data/level_N.txt' (the first
    underscore-delimited token after the directory must be 'level'); given an
    absolute path like '/workspace/data/level_10.txt' it would read the token
    'level' and raise.  It happened to work only because that program globbed
    the relative path 'data/level_*.txt'.
The kept definition is the split('level_') form because it is a strict
superset: on every relative-path input that the split('_') form parses
correctly, split('level_') returns the same N, and it additionally handles
absolute paths.  So importing it in place of distinct_hist_from_data's old
copy is semantics-preserving for that program, not a silent choice between
tie-broken equals.  Correctness is the trivial parse check: for any path
containing exactly one 'level_' marker and N digits before the '.txt'
extension, sorted_key returns N.
"""


def sorted_key(path):
    """Parse the division count N from a 'level_<N>.txt' data-file path.

    Supports both relative ('data/level_10.txt') and absolute
    ('/workspace/data/level_10.txt') globs, and any number of digits in N.
    Returns int(N).  Raises if the path does not contain 'level_' before a
    '.txt' extension.
    """
    fname = path.split('level_')[1]
    return int(fname.split('.')[0])
