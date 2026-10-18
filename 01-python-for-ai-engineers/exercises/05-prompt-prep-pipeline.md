# Exercise 05 — Prompt prep pipeline

**Lessons:** `02-variables-and-data-types`, `03-strings`, `04-lists`  
**Difficulty:** Beginner → early intermediate

## Goal
Combine variables, strings, and lists into a tiny “prompt prep” script — similar to cleaning text and assembling chat messages before calling an AI API.

## Starter input
```python
model = "gpt-4.1-mini"
temperature = 0.3
max_tokens = 512

raw_user_text = "  EXPLAIN lists vs strings for AI engineers  "
docs = "intro.txt,api.md,faq.md"
messages = []
```

## Tasks
1. Clean `raw_user_text` into `user_text` by stripping whitespace and lowercasing.
2. Split `docs` on commas into `doc_list`.
3. Append these three strings to `messages` (in order):
   - `"system: You are a helpful AI engineering tutor."`
   - `"context: " + ", ".join(doc_list)`
   - `"user: " + user_text`
4. Print `model`, `temperature`, and `max_tokens` (with their types).
5. Print `len(messages)` and each message on its own line (use a `for` loop).
6. Print whether `"lists"` is in `user_text`.

## Expected output
```text
model: gpt-4.1-mini <class 'str'>
temperature: 0.3 <class 'float'>
max_tokens: 512 <class 'int'>
3
system: You are a helpful AI engineering tutor.
context: intro.txt, api.md, faq.md
user: explain lists vs strings for ai engineers
True
```

## Hints
- Chain methods: `raw_user_text.strip().lower()`.
- `", ".join(doc_list)` builds one string from a list.
- `.append()` adds one message at a time.
- Membership check: `"lists" in user_text`.

## Stretch
Reverse `doc_list` in place with `.reverse()` and rebuild the context message. Then create `backup_messages = messages.copy()`, append one more message to `messages`, and show that `backup_messages` did not get the new item.
