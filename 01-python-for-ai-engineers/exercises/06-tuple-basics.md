# Exercise 06 — Tuple basics

**Lessons:** `05-tuples`  
**Difficulty:** Simple

## Goal
Create tuples, access items by index, and confirm tuples are ordered and immutable in behavior.

## Starter input
```python
point = (3, 4)
person = ("Sam", 99, "Nigeria")
single = (5,)
not_a_tuple = (5)
```

## Tasks
1. Print `point` and `type(point)`.
2. Print the first item of `person` and the last item using negative indexing.
3. Print `len(person)` and whether `"Sam" in person`.
4. Print `type(single)` and `type(not_a_tuple)`.

## Expected output
```text
(3, 4)
<class 'tuple'>
Sam
Nigeria
3
True
<class 'tuple'>
<class 'int'>
```

## Hints
- Last item: `person[-1]`.
- A one-item tuple needs a trailing comma: `(5,)`.
- `(5)` is just an `int` in parentheses.

## Stretch
Slice `person[0:2]` and print the result and its type.
