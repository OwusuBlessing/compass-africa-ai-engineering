# Exercise 15 — Config copy trap

**Lessons:** `06-dictionaries`  
**Difficulty:** Hard

## Goal
See why `b = a` shares one dict, and use `.copy()` for an independent snapshot.

## Starter input
```python
config = {
    "model": "gpt-4.1-mini",
    "temperature": 0.7,
}
```

## Tasks
1. Assign `alias = config` and change `alias["temperature"]` to `0.0`.
2. Print `config["temperature"]` (shows both names point to the same dict).
3. Reset `config["temperature"]` to `0.7`.
4. Create `snapshot = config.copy()`, set `snapshot["model"]` to `"backup-model"`.
5. Print `config` and `snapshot` on separate lines.

## Expected output
```text
0.0
{'model': 'gpt-4.1-mini', 'temperature': 0.7}
{'model': 'backup-model', 'temperature': 0.7}
```

## Hints
- `alias = config` does not copy; it adds another name for the same object.
- `.copy()` is a shallow copy — fine for flat dicts like this.

## Stretch
Explain in one comment in your code why nested dicts need `copy.deepcopy()` (no code required for deep copy unless you want to try it).
