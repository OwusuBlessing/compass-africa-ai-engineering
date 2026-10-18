# Exercise 03 — String surgery

**Lessons:** `03-strings`  
**Difficulty:** Beginner

## Goal
Practice indexing, slicing, reversing, membership checks, concatenation, and a basic string method.

## Starter input
```python
prompt = "Summarize this document for an AI engineer"
label = "ENGINEER"
```

## Tasks
1. Print the first character of `prompt`.
2. Print a slice of the first word only (`"Summarize"`).
3. Print `prompt` reversed.
4. Print `len(prompt)`.
5. Check whether `"AI"` is in `prompt` and print the result (`True`/`False`).
6. Build `full_label` by concatenating `"AI "` and `label.lower()`, then print it.

## Expected output
```text
S
Summarize
reenigne IA na rof tnemucod siht ezirammuS
42
True
AI engineer
```

> Note: If your `prompt` length differs because of extra spaces, adjust until `len(prompt)` is `42` with the starter string above.

## Hints
- Indexing starts at `0`: `prompt[0]`.
- Slicing end is exclusive: `"Summarize"` is `prompt[0:9]`.
- Reverse with `prompt[::-1]`.
- Membership: `"AI" in prompt`.
- Methods return a new string: `label.lower()` does not change `label`.

## Stretch
Using only slicing (no loops), print the last 8 characters of `prompt`. Then print whether `prompt` starts with `"Sum"` using `.startswith()`.
