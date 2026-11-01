# Exercise 07 — Unpack a person

**Lessons:** `05-tuples`  
**Difficulty:** Simple

## Goal
Unpack a tuple into named variables — the same pattern used for coordinates, scores, and API return values.

## Starter input
```python
person = ("Ada", "Accra", 25)
```

## Tasks
1. Unpack `person` into `name`, `city`, and `age`.
2. Print each variable on its own line.
3. Build one string `summary` as `"Ada from Accra, age 25"` using the three variables (not hard-coded names).
4. Print `summary`.

## Expected output
```text
Ada
Accra
25
Ada from Accra, age 25
```

## Hints
- One line: `name, city, age = person`.
- Build the string with `+` or an f-string.

## Stretch
Swap two variables `a = 1` and `b = 2` using tuple unpacking (`a, b = b, a`) and print them.
