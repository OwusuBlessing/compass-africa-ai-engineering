# Variables and data types

> **Status:** Drafted from live session — see `live_sessions/02/variables.py`.

## Learning objectives
- Explain what a variable is and how it stores a value
- Identify core Python data types: `int`, `float`, `str`, `bool`, and `None`
- Inspect values with `type()` and object identity with `id()`
- Convert between types when needed (e.g. `str()`)
- Model simple AI API settings with variables (model, temperature, tokens, stream, key)

## Explanation

### Variables
A **variable** is a name that points to a value:

```python
name = "Samuel"  # name is the variable; "Samuel" is the value
```

You can reassign a variable later. The name then points to a new value:

```python
a = 10
a = a + 1  # a is now 11
```

### Core data types
| Type | Example | Notes |
|------|---------|--------|
| `int` | `age = 60` | Whole numbers |
| `float` | `length = 5.6`, `temperature = 0.7` | Decimal numbers |
| `str` | `name = "Samuel"` | Text in quotes |
| `bool` | `True`, `False` | Often used like on/off flags (`stream = False`) |
| `NoneType` | `nothing = None` | Means “no value” (e.g. missing `api_key`) |

Large integers can use underscores for readability:

```python
million = 1_000_000
```

### Strings and quotes
Strings can use single quotes, double quotes, or triple quotes for multi-line text:

```python
name = 'Samuel'
name = "Samuel"

article = '''
My name is Sam
I love arsenal
'''
```

### Inspecting values
- `type(value)` — what kind of data it is
- `id(value)` — identity of the object in memory

```python
name = "Samuel"
print(id(name))
print(type(name))
```

### Type conversion
Convert a value to another type when you need a different representation:

```python
age = "25"
age = str(age)  # ensure it is a string
print(type(age))
```

### Concatenation
Strings combine with `+`:

```python
print("a" + "b")  # "ab"
```

## Worked example

AI-style configuration variables (as covered live):

```python
model = "gpt-6.1-sol"  # string
temperature = 0.7      # float
max_tokens = 1024      # int
stream = False         # bool
api_key = None         # no key set yet

print(type(model))
print(type(temperature))
print(type(max_tokens))
print(type(stream))
print(type(api_key))
```

Live session code: `lessons/live_sessions/02/variables.py`.

## Practice
See the module's `exercises/` folder and the weekly assignment in `CURRENT_WEEK.md`.

## Summary
- Variables name values; reassignment updates what the name points to
- Common types: `int`, `float`, `str`, `bool`, `None`
- Use `type()` and `id()` to inspect values
- Convert types explicitly (e.g. `str()`) when needed
- AI configs are naturally modeled as typed variables (model name, temperature, tokens, stream, API key)
