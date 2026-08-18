import Mathlib

#eval do
  let content ← IO.FS.readFile "/workspace/problem.md"
  IO.println content
