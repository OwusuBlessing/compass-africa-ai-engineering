# Exercise 14 — Nested API config

**Lessons:** `06-dictionaries`  
**Difficulty:** Hard

## Goal
Read and update **nested** dictionaries — common in API clients and JSON configs.

## Starter input
```python
request = {
    "model": "gpt-4.1-mini",
    "parameters": {
        "temperature": 0.7,
        "max_tokens": 1024,
    },
    "stream": False,
}
```

## Tasks
1. Print the model name and `max_tokens` (two separate prints).
2. Change `temperature` to `0.2` inside `parameters`.
3. Add `"top_p": 1.0` inside `parameters`.
4. Print the full `parameters` dict.
5. Print whether `"temperature" in request` and `"temperature" in request["parameters"]`.

## Expected output
```text
gpt-4.1-mini
1024
{'temperature': 0.2, 'max_tokens': 1024, 'top_p': 1.0}
False
True
```

## Hints
- Nested access: `request["parameters"]["max_tokens"]`.
- Assign nested: `request["parameters"]["temperature"] = 0.2`.

## Stretch
Add a top-level key `"metadata": {"source": "exercise"}` and print `request["metadata"]["source"]`.
