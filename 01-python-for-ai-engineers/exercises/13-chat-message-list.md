# Exercise 13 — Chat message list

**Lessons:** `06-dictionaries`  
**Difficulty:** Hard

## Goal
Build and extend a **list of message dictionaries** — the same shape used for LLM chat APIs (`role` + `content`).

## Starter input
```python
messages = [
    {"role": "system", "content": "You are a helpful tutor."},
    {"role": "user", "content": "What is a tuple?"},
]
```

## Tasks
1. Append a new dict: `role` `"assistant"`, `content` `"An ordered, immutable sequence."`.
2. Append another user message asking `"What is a dict?"`.
3. Print `len(messages)`.
4. Loop over `messages` and print each line as `role: content` (four lines).
5. Build a list `roles` containing only the `"role"` value from each message (in order) and print it.

## Expected output
```text
4
system: You are a helpful tutor.
user: What is a tuple?
assistant: An ordered, immutable sequence.
user: What is a dict?
['system', 'user', 'assistant', 'user']
```

## Hints
- Append a whole dict: `messages.append({"role": "...", "content": "..."})`.
- Use `.get("role")` or `msg["role"]` inside the loop.

## Stretch
Print the **last** message's content using negative indexing on the list, then dict key access.
