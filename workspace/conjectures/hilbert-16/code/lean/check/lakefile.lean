import Lake
open Lake DSL

package LuH14Check where
  require mathlib from "/opt/mathlib4"

-- the checker lives at code/lean/Lib/BautinRecurrence.lean; the P30 data is
-- inline in it (cross-file imports cannot resolve under single-file lean_check)
@[default_target]
lean_lib Lib