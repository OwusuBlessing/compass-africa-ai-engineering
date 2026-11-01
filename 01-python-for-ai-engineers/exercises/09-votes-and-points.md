# Exercise 09 — Votes and points

**Lessons:** `05-tuples`  
**Difficulty:** Medium

## Goal
Use `count` and `index`, then change tuple data by converting through a list.

## Starter input
```python
votes = ("yes", "yes", "no", "no", "yes")
points = (3, 4)
```

## Tasks
1. Print how many `"yes"` and `"no"` votes there are.
2. Print the index of the first `"yes"`.
3. Convert `points` to a list, set the second value to `5`, convert back to a tuple, and print it.
4. Without using a list, build a new tuple `(3, 5)` from `points` and print it.

## Expected output
```text
yes: 3
no: 2
0
(3, 5)
(3, 5)
```

## Hints
- `votes.count("yes")` and `votes.index("yes")`.
- `list(points)` → change → `tuple(...)`.
- Or `new = (points[0], 5)`.

## Stretch
Print `votes[::-1]` and whether `"maybe" in votes`.
