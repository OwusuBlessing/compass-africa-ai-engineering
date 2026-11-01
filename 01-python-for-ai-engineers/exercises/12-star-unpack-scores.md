# Exercise 12 — Star unpack scores

**Lessons:** `05-tuples`  
**Difficulty:** Medium

## Goal
Take the first score and collect the rest with `*`, and ignore trailing values with `_`.

## Starter input
```python
scores = (20, 30, 40, 60, 20)
person = ("John", "Nigeria", 67)
```

## Tasks
1. Unpack `scores` into `first` and `rest` using `first, *rest = scores`.
2. Print `first` and `rest`.
3. Unpack only the name from `person` using `name, *_ = person` and print `name`.
4. Print `sum(rest)` and `len(rest)`.

## Expected output
```text
20
[30, 40, 60, 20]
John
150
4
```

## Hints
- `*rest` always becomes a **list**.
- `name, *_` throws away the other values.

## Stretch
Convert `rest` back to a tuple with `tuple(rest)` and print it.
