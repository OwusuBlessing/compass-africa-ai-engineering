# Strings

> **Status:** Drafted from live session — see `live_sessions/03/strings.py`.

## Learning objectives
- Create strings and nest quotes correctly
- Access characters with indexing and extract parts with slicing
- Reverse a string with slice step syntax
- Measure length with `len()` and test membership with `in`
- Join strings with concatenation (`+`)
- Use basic string methods such as `.lower()`

## Explanation

### Creating strings
Strings hold text. You can nest quotes by mixing quote styles:

```python
text = 'Bola said she "AI IS DEAD" '
```

### Indexing
Each character has a position starting at `0`:

```python
some_string = "SAMUEL"
# S A M U E L
# 0 1 2 3 4 5

print(some_string[0])  # "S"
```

### Slicing
Slicing uses `start:end` — the end index is **not** included (think “up to, but not including”):

```python
print(some_string[0:3])  # "SAM"
```

### Reverse
A step of `-1` walks the string backwards:

```python
print(some_string[::-1])  # "LEUMAS"
```

### Length and membership
```python
text = "python"
print(len(text))      # 6
print("SA" in text)   # False
print("Py" in text)   # False (case-sensitive; "py" would be True)
```

### Concatenation
Combine strings with `+`:

```python
first = "AI"
second = "Engineer"
print(first + " " + second)  # "AI Engineer"
```

### String methods
Methods are called on a string and return a **new** string (strings are immutable):

```python
name = "ENGINEER"
print(name.lower())  # "engineer"
```

## Worked example

Putting the live-session ideas together:

```python
some_string = "SAMUEL"

print(some_string[0])       # indexing
print(some_string[0:3])     # slicing → "SAM"
print(some_string[::-1])    # reverse → "LEUMAS"
print(len(some_string))     # 6
print("SAM" in some_string) # True

first = "AI"
second = "Engineer"
print(first + " " + second)

print("ENGINEER".lower())
```

Live session code: `lessons/live_sessions/03/strings.py`.

## Practice
See the module's `exercises/` folder and the weekly assignment in `CURRENT_WEEK.md`.

## Summary
- Index from `0`; slice with `start:end` (end exclusive)
- Reverse with `[::-1]`
- `len()` and `in` work on strings; membership is case-sensitive
- Concatenate with `+`
- Methods like `.lower()` return new strings and do not change the original
