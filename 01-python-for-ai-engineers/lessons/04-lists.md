# Lists

> **Status:** Drafted from live session — see `live_sessions/04/list.py`.

## Learning objectives
- Create ordered lists that can hold many values (including mixed types)
- Contrast lists (mutable) with strings (immutable)
- Index, slice, measure length, and check membership — the same ideas as strings
- Add items with `.append()` and `.extend()`, and join lists with `+`
- Remove items with `.pop()` (and know `.remove()` exists)
- Find, sort, and reverse list data; use `max()`, `min()`, and `sum()` on numbers
- Copy a list safely and build lists from strings with `.split()`
- Loop over list items with `for`

## Explanation

### What a list is
A **list** stores many values in order. Unlike strings, lists are **mutable** — you can change them in place.

```python
names = ["Sam", "Jack", "Joe"]
scores = [50, 90, 45, True, "SAM"]  # mixed types are allowed
empty = []
```

AI-flavored examples from the session:

```python
messages = ["tell me about ai", "summarize docs"]
docs = ["doc1.txt", "doc2.txt", "doc3.txt"]
results = []
```

### Ordered and indexable
Positions start at `0`, same pattern as strings:

```python
names = ["Sam", "Jack", "Joe"]
# Sam → 0, Jack → 1, Joe → 2
print(names[0])  # "Sam"
```

Membership, slicing, and `len()` work similarly to strings.

### Mutable
You can replace an item by index. The list object can keep the same `id` while its contents change:

```python
names = ["Sam", "Jack", "Joe"]
print(id(names))
names[0] = "GIG"
print(id(names))  # often the same identity
print(names)      # ["GIG", "Jack", "Joe"]
```

### Adding items
```python
names.append("SAMSON")           # add one item
names.extend(["BOLA", "David"])  # add multiple items

a = [1, 2]
b = [3, 4]
c = a + b  # [1, 2, 3, 4] — join into a new list
```

### Removing items
```python
last = names.pop()     # remove and return the last item
second = names.pop(1)  # remove and return item at index 1
# names.remove("SAMSON")  # remove by value (first match)
```

### Find, sort, reverse
```python
scores = [45, 60, 90]
print(scores.index(90))  # 2

scores = [90, 67, 100]
scores.sort(reverse=True)  # sorts in place → [100, 90, 67]

new_scores = [3, 1, 5]
latest_scores = sorted(new_scores)  # new list; original unchanged

new_scores.reverse()  # reverse in place
```

### Aggregates on numbers
```python
numbers = [4, 6, 1, 9]
print(max(numbers))
print(min(numbers))
print(sum(numbers))
```

### Copying and splitting
```python
a = [1, 2, 3, 4]
b = a.copy()  # independent copy (not just another name for `a`)

names = "Sam,Jack,Fred"
names_list = names.split(",")  # ["Sam", "Jack", "Fred"]
```

### Looping
```python
for item in names_list:
    print(item)
```

## Worked example

```python
messages = ["tell me about ai", "summarize docs"]
docs = ["doc1.txt", "doc2.txt", "doc3.txt"]
results = []

messages.append("rewrite this email")
docs.extend(["notes.md", "faq.md"])

scores = [90, 67, 100]
scores.sort(reverse=True)
print(scores)
print(max(scores), min(scores), sum(scores))

csv_names = "Sam,Jack,Fred"
for name in csv_names.split(","):
    print(name)
```

Live session code: `lessons/live_sessions/04/list.py`.

## Practice
See the module's `exercises/` folder and the weekly assignment in `CURRENT_WEEK.md`.

## Summary
- Lists are ordered and mutable; good for collections like messages, docs, and results
- Indexing/slicing/membership/`len()` mirror string patterns
- Grow with `.append()` / `.extend()` / `+`; shrink with `.pop()` (or `.remove()`)
- Sort in place with `.sort()`, or get a new list with `sorted()`
- Use `.copy()` to avoid shared-reference bugs; `.split()` turns text into a list
