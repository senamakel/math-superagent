# Race dynamics specification (for implementation)

Boats indexed j=1..n, j=1 lowest/downstream, j=n highest/upstream.
Start positions p_j = 40*(j-1). Finish line at L (coordinate).
Boat j speed v_j sampled iid Exp(1). Higher coordinate = upstream (toward finish).

A boat rows at constant speed v_j from its start until it either reaches the
finish line (position L) or draws level with ("bumps") the next ROWING boat
ahead (nearest boat with larger index that is still actively rowing). When it
bumps, the bumping boat stops and is OUT (takes no further part; boats behind
pass it freely). The bumped boat continues rowing.

Chronological event simulation:

State per boat: position pos_j, status in {ROWING, OUT, FINISHED}.
FINISHED = sits at position L. OUT = stopped at its bump position (transparent
to boats behind).

Each simulation step, consider every ROWING boat j:
  - finish time  ft_j = (L - pos_j)/v_j
  - let k = nearest boat with index > j that is ROWING (skip OUT and FINISHED).
    If v_j > v_k: catch time  ct_j = (pos_k - pos_j)/(v_j - v_k). (both moving)
    If no such k, no catch.
Next event = min over all ROWING boats of (ft_j, ct_j). Process the earliest.
(Continuous speeds -> no ties in measure; break ties deterministically.)

Event handling:
  - If the event is ft_j (boat j reaches finish): set status FINISHED, pos=L.
  - If the event is ct_j (boat j catches k): record bump (j bumped k),
    set j status OUT at its current position, k stays ROWING (position updated).
After an event, recompute and continue until no ROWING boats remain (all
FINISHED or OUT).

Note: when a boat passes OUT boats, those are ignored as targets; when a boat
reaches the finish at L it stops there regardless of any boat ahead that
already finished (they're all at L).

Final order / permutation:
  For i<j (i started lower): i is placed higher than j in the new order iff
  there is a bump chain i -> ... -> j (i.e., i is "above" j). Otherwise i stays
  below j.
  Compute the ranking: place_i (1 = highest) = 1 + #{ j : j is above i }.
  "j above i" for j>i means chain i->j exists; for j<i means chain j->i does
  NOT exist.
  Starting order listing (ascending place, i.e. lowest place first) is
  1,2,...,n. The new-order listing (ascending place) is the boats sorted so
  that higher place = higher rank. The permutation is the map from starting
  list to new list; parity even/odd is the sign of that permutation (0 = even,
  1 = odd, sign = (-1)^inversions).

Referenced example (n=3,L=160): outcomes and probabilities as in goal.md.
