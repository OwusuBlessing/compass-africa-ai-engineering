# Exercise 16 — Rows to records

**Lessons:** `05-tuples`, `06-dictionaries`  
**Difficulty:** Hard

## Goal
Turn tuple rows into dictionaries and combine tuple unpacking with dict updates — a miniature ETL step before sending data to an API.

## Starter input
```python
columns = ("name", "score", "country")
rows = [
    ("Ada", 91, "Ghana"),
    ("Sam", 88, "Nigeria"),
    ("Jay", 76, "Kenya"),
]
```

## Tasks
1. Unpack `columns` into `k_name`, `k_score`, `k_country` (use any variable names you like).
2. For each row, unpack `(name, score, country)` and build one dict with keys from step 1 and matching values. Collect all dicts in a list called `students`.
3. Print `students[0]["name"]` and `students[-1]["score"]`.
4. Loop over `students` and print `name: score` for each (three lines).
5. Find the student with the highest score using a loop (no `max()` on dicts required). Print their name and score.

## Expected output
```text
Ada
76
Ada: 91
Sam: 88
Jay: 76
Ada 91
```

## Hints
- One record: `{"name": name, "score": score, "country": country}` or use unpacked key names.
- Track `best_name` and `best_score` while looping.

## Stretch
Add a field `"passed": True` to each student where `score >= 80`, using a loop and `.update()` or subscript assignment.
