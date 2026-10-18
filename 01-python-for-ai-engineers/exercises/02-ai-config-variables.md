# Exercise 02 — AI config variables

**Lessons:** `02-variables-and-data-types`  
**Difficulty:** Beginner

## Goal
Model a small AI API configuration with the correct data types, inspect them, and convert a value when needed.

## Starter input
Use these settings (assign them to variables):

| Variable | Value |
|----------|--------|
| `model` | `"gpt-4.1-mini"` |
| `temperature` | `0.7` |
| `max_tokens` | `1024` |
| `stream` | `False` |
| `api_key` | `None` |

Also start with this string that looks like a number:

```python
token_limit_text = "2048"
```

## Tasks
1. Create the five config variables above with the correct types.
2. Print each variable and its `type()`.
3. Convert `token_limit_text` to an integer and store it in `token_limit`.
4. Print `token_limit` and `type(token_limit)`.
5. Reassign `temperature` to `0.2` and print the new value.

## Expected output
Types should match this pattern:

```text
model: gpt-4.1-mini <class 'str'>
temperature: 0.7 <class 'float'>
max_tokens: 1024 <class 'int'>
stream: False <class 'bool'>
api_key: None <class 'NoneType'>
token_limit: 2048 <class 'int'>
temperature: 0.2
```

## Hints
- `None` is not the string `"None"`.
- Convert with `int(token_limit_text)`.
- Reassignment is just writing `temperature = 0.2` again.

## Stretch
Create a readable large number variable `daily_request_budget = 1_000_000` and print it. Then concatenate `"Model: "` with `model` using `+` and print the result.
