# Dictionaries

> **Status:** Ready to teach  
> **Goal of this lesson:** Students can store and look up data by **name (key)** instead of by position. This is the most important data structure in AI engineering: chat messages, API requests and responses, configs and JSON are all dictionaries.

---

## Learning objectives

By the end of this lesson, students can:

1. Create dictionaries and explain **key → value** pairs
2. Read values with `d[key]` and safely with `d.get(key)`
3. Add, change, and remove items (`d[key] = ...`, `pop`, `del`, `update`)
4. Check if a key exists with `in`
5. Use `keys()`, `values()`, `items()` and loop over a dictionary
6. Work with **nested** data: a list of dictionaries and a dictionary inside a dictionary
7. Explain why keys must be immutable (link back to tuples)
8. Avoid the copy trap (`b = a` vs `a.copy()`)

---

## Reminder from earlier lessons

| Type | Brackets | Find items by… | Mutable? |
|------|----------|----------------|----------|
| `list` | `[ ]` | position (index `0, 1, 2`) | Yes |
| `tuple` | `( )` | position (index `0, 1, 2`) | No |
| `dict` | `{ }` | **key (a name)** | Yes |

**Say:**  
"With lists and tuples, you find things by **position**: item 0, item 1. But what if I ask, 'What is Ada's age?' I don't want to remember that age is at position 1. A dictionary lets you find things by **name**."

**Real-life picture:**  
"Think of a real dictionary: you look up a **word** (key) and get its **meaning** (value). Or your phone contacts: you look up a **name** and get a **number**."

---

## 1. What is a dictionary?

A **dictionary** stores **key: value** pairs.

**Type this live:**

```python
person = {
    "name": "Ada",
    "age": 25,
    "city": "Accra",
}

print(person)         # {'name': 'Ada', 'age': 25, 'city': 'Accra'}
print(type(person))   # <class 'dict'>
```

```text
   key        value
  "name"  →  "Ada"
  "age"   →   25
  "city"  →  "Accra"
```

**Say:**  
"Curly brackets `{}` mean dictionary. Each item is a **key**, a colon, then the **value**. Items are separated by commas."

```python
empty = {}
print(type(empty))   # <class 'dict'>   ← NOT a set, an empty dict
```

### Compare: the same data as a list vs a dict

```python
person_list = ["Ada", 25, "Accra"]
print(person_list[1])        # 25   ← what is 1? you must remember

person_dict = {"name": "Ada", "age": 25, "city": "Accra"}
print(person_dict["age"])    # 25   ← clear and readable
```

**Say:**  
"Same data. But the dictionary version tells you what each value **means**."

---

## 2. Reading values

### With square brackets `[]`

```python
person = {"name": "Ada", "age": 25, "city": "Accra"}

print(person["name"])   # Ada
print(person["age"])    # 25
```

**Show the error live:**

```python
print(person["email"])
```

```text
KeyError: 'email'
```

**Say:**  
"If the key doesn't exist, Python crashes with a `KeyError`. This is like `IndexError` for lists."

### Safely with `.get()`

```python
print(person.get("name"))                 # Ada
print(person.get("email"))                # None   ← no crash
print(person.get("email", "not given"))   # not given   ← default value
```

**Say:**  
"`.get()` is the safe way. If the key is missing, you get `None` or the default you choose. When reading data from an API, always prefer `.get()` for fields that might be missing."

---

## 3. Adding and changing values

The **same syntax** adds a new key or changes an existing one:

```python
person = {"name": "Ada", "age": 25}

person["age"] = 26            # key exists → CHANGE
person["email"] = "ada@x.com" # key is new → ADD

print(person)
# {'name': 'Ada', 'age': 26, 'email': 'ada@x.com'}
```

**Say:**  
"Dictionaries are **mutable**, like lists. If the key is already there, you overwrite it. If not, you create it."

### Keys are unique

```python
d = {"a": 1, "a": 2}
print(d)   # {'a': 2}   ← the last one wins
```

**Say:**  
"A key can only appear **once**. Values can repeat; keys cannot."

### Update many at once with `.update()`

```python
person = {"name": "Ada", "age": 25}
person.update({"age": 30, "city": "Lagos"})
print(person)   # {'name': 'Ada', 'age': 30, 'city': 'Lagos'}
```

---

## 4. Removing items

```python
person = {"name": "Ada", "age": 25, "city": "Accra"}

age = person.pop("age")      # removes AND returns the value
print(age)                   # 25
print(person)                # {'name': 'Ada', 'city': 'Accra'}

del person["city"]           # removes, returns nothing
print(person)                # {'name': 'Ada'}

person.clear()               # removes everything
print(person)                # {}
```

**Say:**  
"`pop` gives you the value back, like list `pop`. `del` just deletes. Both crash if the key doesn't exist."

```python
person = {"name": "Ada"}
print(person.pop("age", "no age"))   # no age   ← safe pop with default
```

---

## 5. Checking keys, length

```python
person = {"name": "Ada", "age": 25}

print("name" in person)    # True
print("email" in person)   # False
print("Ada" in person)     # False   ← `in` checks KEYS, not values!

print(len(person))         # 2   ← number of key-value pairs
```

**Say:**  
"Careful: `in` checks the **keys** only. `"Ada"` is a value, so it's `False`."

---

## 6. `keys()`, `values()`, `items()`

```python
person = {"name": "Ada", "age": 25, "city": "Accra"}

print(person.keys())     # dict_keys(['name', 'age', 'city'])
print(person.values())   # dict_values(['Ada', 25, 'Accra'])
print(person.items())    # dict_items([('name', 'Ada'), ('age', 25), ('city', 'Accra')])
```

**Say:**  
"Look at `items()`: each pair is a **tuple**! `('name', 'Ada')`. That's why we learned tuples and unpacking right before this."

```python
print(list(person.keys()))   # ['name', 'age', 'city']   ← convert to a normal list
```

---

## 7. Looping over a dictionary

```python
person = {"name": "Ada", "age": 25, "city": "Accra"}

# Loop over keys (default)
for key in person:
    print(key)
# name
# age
# city

# Loop over values
for value in person.values():
    print(value)

# Loop over BOTH ⭐ (most common)
for key, value in person.items():
    print(key, "→", value)
```

```text
name → Ada
age → 25
city → Accra
```

**Say:**  
"`items()` gives tuples, and we unpack each tuple into `key, value`. Same trick as last lesson's `for filename, score in results`."

---

## 8. What can be a key? (link to tuples)

**Values** can be anything. **Keys** must be **immutable**: `str`, `int`, `float`, `bool`, `tuple`.

```python
locations = {
    (5.6, -0.2): "Accra",
    (6.5, 3.4): "Lagos",
}
print(locations[(5.6, -0.2)])   # Accra   ← tuple as key ✅
```

**Show the error live:**

```python
bad = {[1, 2]: "nope"}
```

```text
TypeError: unhashable type: 'list'
```

**Say:**  
"Remember I said tuples can be dictionary keys but lists can't? Here it is. Keys must never change, otherwise Python would lose track of them. Lists can change, so they're not allowed."

---

## 9. Nested data ⭐ (this is real AI code)

### A list of dictionaries: chat messages

This is **exactly** the format used to send messages to LLM APIs (Claude, OpenAI, etc.):

```python
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is Python?"},
    {"role": "assistant", "content": "Python is a programming language."},
]

print(messages[1])              # {'role': 'user', 'content': 'What is Python?'}
print(messages[1]["content"])   # What is Python?

# add a new message
messages.append({"role": "user", "content": "Give me an example."})
print(len(messages))   # 4

for msg in messages:
    print(msg["role"], ":", msg["content"])
```

**Say:**  
"A **list** because the conversation grows. Each message is a **dictionary** because it has named parts: role and content. When we call an AI model later in the course, *this* is what we'll send."

### A dictionary inside a dictionary: an API response

```python
response = {
    "model": "claude-sonnet",
    "content": "Hello! How can I help?",
    "usage": {
        "input_tokens": 12,
        "output_tokens": 8,
    },
}

print(response["content"])                  # Hello! How can I help?
print(response["usage"]["output_tokens"])   # 8
```

**Say:**  
"Read it step by step: `response["usage"]` gives the inner dictionary, then `["output_tokens"]` reaches inside it. API responses look like this, and so does JSON (lesson 17)."

---

## 10. The copy trap (same as lists)

```python
config = {"model": "small", "temperature": 0.7}

b = config            # ❌ NOT a copy, same dictionary
b["model"] = "large"
print(config)         # {'model': 'large', 'temperature': 0.7}   ← changed too!

config = {"model": "small", "temperature": 0.7}
c = config.copy()     # ✅ real copy
c["model"] = "large"
print(config)         # {'model': 'small', 'temperature': 0.7}   ← safe
```

**Say:**  
"Exactly like lists: `b = a` gives the same dictionary a second name. Use `.copy()` for a real copy."

---

## 11. Worked example: counting words

**Live-code this from scratch:**

```python
text = "ai is fun and ai is powerful and ai is the future"

words = text.split()     # string → list (lesson 03/04)
counts = {}

for word in words:
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1

print(counts)
```

```text
{'ai': 3, 'is': 3, 'fun': 1, 'and': 2, 'powerful': 1, 'the': 1, 'future': 1}
```

**Say:**  
"For each word: if we've seen it, add 1. If not, start at 1. This idea, counting words, is the very beginning of how language models learned about text."

**Shorter version with `.get()`** (show after the first one works):

```python
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
```

**Say:**  
"`counts.get(word, 0)`: 'give me the current count, or 0 if it's new', then add 1. Same result, one line."

---

## 12. Worked example: building a chat history

```python
messages = [
    {"role": "system", "content": "You are a friendly tutor."},
]

# the user asks something
messages.append({"role": "user", "content": "What is a dictionary?"})

# pretend the AI replied
reply = {"role": "assistant", "content": "A dictionary stores key-value pairs."}
messages.append(reply)

# print the conversation nicely
for msg in messages:
    print(msg["role"].upper() + ":", msg["content"])

print("Total messages:", len(messages))
```

```text
SYSTEM: You are a friendly tutor.
USER: What is a dictionary?
ASSISTANT: A dictionary stores key-value pairs.
Total messages: 3
```

**Say:**  
"Congratulations: this is the data structure behind every chatbot. Strings, lists, tuples and dictionaries all come together here."

---

## Quick-check questions (ask the class)

1. How do you get `"Ada"` from `p = {"name": "Ada"}`? → `p["name"]`
2. What does `p["email"]` do if `"email"` isn't a key? → `KeyError`
3. What's the safe way? → `p.get("email")` → `None`
4. `d = {"x": 1}; d["x"] = 5`: does this add or change? → **change**
5. `"Ada" in {"name": "Ada"}`: True or False? → **False** (`in` checks keys)
6. Can a list be a key? → **No**. Can a tuple? → **Yes**
7. What does `.items()` give you in each step of a loop? → a **tuple** `(key, value)`

---

## Mini practice (5–10 min in class)

```python
# 1. Create a dict `student` with keys: name, country, score.
#    Print each value using the keys.

# 2. Change the score, add a new key "passed" with value True,
#    then remove "country". Print the dict after each step.

# 3. Use .get() to read a key "email" with default "no email".

# 4. Loop over `student` with .items() and print "key: value".

# 5. Given:
messages = [
    {"role": "user", "content": "Hi"},
    {"role": "assistant", "content": "Hello!"},
    {"role": "user", "content": "Tell me a joke"},
]
#    Print only the content of messages where role is "user".

# 6. Count the letters in "banana" using a dictionary.
#    Expected: {'b': 1, 'a': 3, 'n': 2}
```

---

## Cheat sheet

```text
key → value, mutable, keys unique

d = {"a": 1, "b": 2}     create
d = {}                   empty dict

d["a"]                   read (KeyError if missing)
d.get("a")               safe read → None if missing
d.get("a", 0)            safe read with default

d["c"] = 3               add (new key) / change (existing key)
d.update({"a": 9})       add/change many

d.pop("a")               remove + return value
del d["a"]               remove
d.clear()                empty it

"a" in d                 checks KEYS
len(d)                   number of pairs

d.keys()   d.values()   d.items()

for k in d:                    keys
for v in d.values():           values
for k, v in d.items():         both ⭐

keys must be immutable: str, int, tuple ✅   list ❌

b = d            NOT a copy
b = d.copy()     real copy

messages = [{"role": "user", "content": "..."}]   ← LLM chat format
response["usage"]["output_tokens"]                ← nested access
```

---

## Teaching order (use this sequence)

1. Reminder table: list / tuple / dict  
2. Real-life picture (word → meaning, contact → number)  
3. Create a dict + `{}` syntax, list vs dict comparison  
4. Read with `[]` → show `KeyError` live  
5. Safe read with `.get()` + default  
6. Add / change with `d[key] = value`, keys are unique  
7. `.update()`  
8. `pop` / `del` / `clear`  
9. `in` (keys only!) + `len`  
10. `keys()` / `values()` / `items()` → point out the tuples  
11. Looping, especially `for k, v in d.items()`  
12. What can be a key (tuple ✅, list ❌ live error)  
13. ⭐ Nested: list of dicts (chat messages)  
14. ⭐ Nested: dict in dict (API response)  
15. Copy trap  
16. Worked example: word counter  
17. Worked example: chat history  
18. Quick-check questions → mini practice  

---

## Summary

- A **dictionary** stores **key: value** pairs in `{}`; you look things up by **name**, not position
- Read with `d[key]` (can crash) or `d.get(key)` (safe)
- `d[key] = value` adds **or** changes; keys are unique
- `in` checks **keys**; `.items()` gives `(key, value)` **tuples**
- Keys must be immutable (strings, numbers, tuples)
- **List of dicts** = chat messages; **dict in dict** = API responses. This is the shape of almost all AI data
- `b = a` is not a copy; use `a.copy()`

## Practice location

See the module's `exercises/` folder and the weekly assignment in `CURRENT_WEEK.md`.
