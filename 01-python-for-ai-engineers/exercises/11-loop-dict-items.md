# Exercise 11 — Loop dictionary items

**Lessons:** `06-dictionaries`  
**Difficulty:** Medium

## Goal
Inspect keys, values, and items, then loop over key–value pairs (each item is a tuple).

## Starter input
```python
config = {
    "model": "gpt-4.1-mini",
    "temperature": 0.7,
    "max_tokens": 1024,
}
```

## Tasks
1. Print `list(config.keys())` (order may vary; all three keys must appear).
2. Print `list(config.values())`.
3. Loop over `config.items()` and print each pair as `key=value` on one line (three lines total).
4. Print only keys whose values are numbers (`int` or `float`).

## Expected output
```text
['model', 'temperature', 'max_tokens']
['gpt-4.1-mini', 0.7, 1024]
model=gpt-4.1-mini
temperature=0.7
max_tokens=1024
temperature
max_tokens
```

> Line order for keys/values may differ; include all three keys and values.

## Hints
- `for key, value in config.items():`
- Check type: `isinstance(value, (int, float))`.

## Stretch
Build a new dict `safe = {k: config.get(k) for k in ["model", "stream"]}` using `.get()` and print `safe`.
