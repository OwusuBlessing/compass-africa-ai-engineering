# Exercise 08 — Dictionary lookup

**Lessons:** `06-dictionaries`  
**Difficulty:** Simple

## Goal
Read values from a dictionary by key and use `.get()` when a field might be missing.

## Starter input
```python
user = {
    "name": "Sam",
    "age": 99,
    "country": "Nigeria",
}
```

## Tasks
1. Print `user["name"]` and `user["age"]`.
2. Print `user.get("country")`.
3. Print `user.get("email")` and `user.get("email", "not given")`.
4. Print whether `"name" in user` and whether `"Sam" in user`.

## Expected output
```text
Sam
99
Nigeria
None
not given
True
False
```

## Hints
- `in` checks **keys**, not values.
- `.get("email", "not given")` supplies a default when the key is missing.

## Stretch
Print `type(user)` and the number of keys with `len(user)`.
