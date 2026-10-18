# Exercise 04 — Doc queue list

**Lessons:** `04-lists`  
**Difficulty:** Beginner

## Goal
Build and update an ordered, mutable list of documents and messages — the same patterns used when preparing AI inputs.

## Starter input
```python
docs = ["intro.txt", "api.md", "faq.md"]
messages = ["tell me about ai"]
scores = [72, 91, 65, 88]
```

## Tasks
1. Print the first document (`docs[0]`).
2. Change `docs[1]` to `"api-guide.md"` and print `docs`.
3. Append `"notes.md"` to `docs`.
4. Extend `messages` with `["summarize docs", "rewrite this email"]`.
5. Remove the last item from `docs` with `.pop()` and print the removed value.
6. Sort `scores` descending in place, then print `scores`, `max(scores)`, `min(scores)`, and `sum(scores)`.

## Expected output
```text
intro.txt
['intro.txt', 'api-guide.md', 'faq.md']
['intro.txt', 'api-guide.md', 'faq.md', 'notes.md']
['tell me about ai', 'summarize docs', 'rewrite this email']
notes.md
[91, 88, 72, 65]
91
65
316
```

## Hints
- Lists are mutable: `docs[1] = "..."` changes the list in place.
- One item → `.append()`; multiple items → `.extend([...])`.
- `.pop()` returns the removed item.
- Descending sort: `scores.sort(reverse=True)`.

## Stretch
Copy `docs` with `.copy()` into `backup_docs`, then clear or change `docs` and show that `backup_docs` is unchanged. Also split `"Sam,Jack,Fred"` into a list with `.split(",")` and loop over it with `for` to print each name.
