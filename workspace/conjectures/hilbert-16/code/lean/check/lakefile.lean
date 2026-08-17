import Lake
open Lake DSL

package LuH14Check where
  require mathlib from "/opt/mathlib4"

-- the LuH14.Generated data module lives at code/lean/LuH14/Generated.lean
@[default_target]
lean_lib LuH14

-- the checker lives at code/lean/Lib/BautinRecurrence.lean
@[default_target]
lean_lib Lib