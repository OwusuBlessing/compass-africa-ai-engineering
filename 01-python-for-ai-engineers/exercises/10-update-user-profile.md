# Exercise 10 — Update user profile

**Lessons:** `06-dictionaries`  
**Difficulty:** Medium

## Goal
Add, change, merge, and remove keys in a mutable dictionary.

## Starter input
```python
person = {
    "name": "Sam",
    "age": 99,
    "country": "Nigeria",
}
```

## Tasks
1. Add `"email": "sam@gmail.com"`.
2. Change `"name"` to `"Joe"`.
3. Merge `{"name": "Jay", "age": 100}` with `.update()` and print `person`.
4. Remove `"name"` with `.pop()` and print the removed value and the remaining `person`.

## Expected output
After step 3, your dict should match (key order may vary on older Python):

```text
{'name': 'Jay', 'age': 100, 'country': 'Nigeria', 'email': 'sam@gmail.com'}
Jay
{'age': 100, 'country': 'Nigeria', 'email': 'sam@gmail.com'}
```

## Hints
- `person["email"] = ...` adds a key.
- `.update()` overwrites existing keys.
- `.pop("name")` returns the value and deletes the key.

## Stretch
Use `del person["email"]` and print `person` again.
