# Tuples

> **Status:** Ready to teach  
> **Goal of this lesson:** Students can create and use tuples, explain why they are **immutable**, and use **unpacking**, which they will see constantly in AI code (model results, coordinates, (text, score) pairs).

---

## Learning objectives

By the end of this lesson, students can:

1. Create tuples and explain that tuples are **ordered** and **immutable**
2. Access items with indexing and slicing (same as lists and strings)
3. Create a one-item tuple correctly (`(5,)` not `(5)`)
4. Use the two tuple methods: `count` and `index`
5. **Unpack** a tuple into variables (and swap two variables)
6. Use `*` in unpacking to collect "the rest"
7. Convert between lists and tuples (`list()` / `tuple()`)
8. Decide **when to use a tuple vs a list**

---

## Reminder from earlier lessons

| Type | What it stores | Brackets | Mutable? |
|------|----------------|----------|----------|
| `str` | text | `" "` | No |
| `list` | many values in order | `[ ]` | Yes |
| `tuple` | many values in order | `( )` | **No** |

**Say:**  
"Last lesson we learned lists: an ordered box we can change. Today's tuple is also an ordered box, but once you close it, it's **sealed**. You can look inside, but you can't change what's in it."

---

## 1. What is a tuple?

A **tuple** is an ordered collection of items that **cannot be changed** after it is created.

**Type this live:**

```python
point = (3, 4)
person = ("Ada", 25, "Accra")
rgb = (255, 128, 0)
empty = ()

print(point)          # (3, 4)
print(type(point))    # <class 'tuple'>
```

**Say:**  
"Round brackets `()` mean tuple. Items are separated by commas, same as a list."

### The comma is what makes a tuple

```python
a = 1, 2, 3
print(a)          # (1, 2, 3)
print(type(a))    # <class 'tuple'>
```

**Say:**  
"Here's a surprise: Python doesn't need the brackets. **The comma makes the tuple.** The brackets just make it easier to read."

---

## 2. The one-item tuple trap ⚠️

**Type this live and ask the class to predict the output first:**

```python
x = (5)
print(type(x))    # <class 'int'>   ← NOT a tuple!

y = (5,)
print(type(y))    # <class 'tuple'>
```

**Say:**  
"`(5)` is just the number 5 in brackets, like in maths: `(2 + 3) * 4`. To make a one-item tuple you **must** add a trailing comma: `(5,)`. This catches everyone at least once."

---

## 3. Tuples are ordered (indexing & slicing)

Everything you learned about indexing in strings and lists still works.

```text
 ("Ada", "Bolo", "Chidi")
    0       1       2
   -3      -2      -1
```

```python
names = ("Ada", "Bolo", "Chidi")

print(names[0])      # Ada
print(names[-1])     # Chidi
print(names[0:2])    # ('Ada', 'Bolo')   ← a slice of a tuple is a tuple
print(names[::-1])   # ('Chidi', 'Bolo', 'Ada')

print(len(names))         # 3
print("Bolo" in names)    # True
```

**Say:**  
"Nothing new to learn here. Strings, lists and tuples all index the same way. Learn it once, use it everywhere."

---

## 4. Tuples are immutable (the key idea)

**Type this live and let the error happen in front of the class:**

```python
point = (3, 4)
point[0] = 10
```

```text
TypeError: 'tuple' object does not support item assignment
```

**Say:**  
"Same error idea as strings. You **cannot** change, add, or remove items in a tuple."

Show what's **missing** compared to lists:

```python
point = (3, 4)

# point.append(5)   → AttributeError: no append
# point.remove(3)   → AttributeError: no remove
# point.sort()      → AttributeError: no sort
```

### "But I need to change it!" Make a new one

```python
point = (3, 4)
point = (10, point[1])     # build a NEW tuple, reuse the name
print(point)               # (10, 4)

colors = ("red", "green")
colors = colors + ("blue",)   # + makes a new tuple
print(colors)                 # ('red', 'green', 'blue')
```

**Say:**  
"We didn't change the old tuple; we built a new one and pointed the variable at it. Exactly like strings."

### Why would anyone want something they can't change?

**Say (key talking points):**  
1. **Safety:** "Some data should never change by accident: a model's config, GPS coordinates, the shape of a dataset. A tuple protects it."  
2. **Meaning:** "When another engineer sees a tuple, they know: this is a fixed record, not a growing collection."  
3. **Speed / memory:** "Tuples are slightly lighter and faster than lists."  
4. **Can be dictionary keys:** "Next lesson (dictionaries), you'll see tuples can be used as keys; lists can't."

---

## 5. Tuple methods (only two!)

```python
votes = ("yes", "no", "yes", "yes", "no")

print(votes.count("yes"))   # 3
print(votes.index("no"))    # 1   ← position of the FIRST "no"
```

Functions that work on lists also work on tuples:

```python
scores = (70, 85, 90, 60)

print(len(scores))      # 4
print(sum(scores))      # 305
print(min(scores))      # 60
print(max(scores))      # 90
print(sorted(scores))   # [60, 70, 85, 90]   ← returns a LIST
```

**Say:**  
"Lists have lots of methods because they can change. Tuples only have `count` and `index` because they only let you *look*. Notice `sorted()` gives back a **list**, because it creates something new."

---

## 6. Unpacking ⭐ (the most useful part)

**Say:**  
"This is the feature you'll use every single day as an AI engineer."

```python
person = ("Ada", 25, "Accra")

name, age, city = person

print(name)   # Ada
print(age)    # 25
print(city)   # Accra
```

**Say:**  
"Python takes each item out of the tuple and puts it into a variable, in order. The number of variables must match the number of items."

**Show the error:**

```python
name, age = person
```

```text
ValueError: too many values to unpack (expected 2)
```

### Swapping two variables

```python
a = 1
b = 2

a, b = b, a

print(a, b)   # 2 1
```

**Say:**  
"In other languages you need a temporary variable. In Python, the right side builds a tuple `(2, 1)` and then unpacks it. One line."

### Collecting "the rest" with `*`

```python
scores = (95, 88, 72, 65, 50)

first, *rest = scores
print(first)   # 95
print(rest)    # [88, 72, 65, 50]   ← a list

top, *middle, last = scores
print(top)     # 95
print(middle)  # [88, 72, 65]
print(last)    # 50
```

**Say:**  
"The star means 'grab everything left over'. Useful when you only care about the first or last item."

### Ignoring values with `_`

```python
name, _, city = ("Ada", 25, "Accra")
print(name, city)   # Ada Accra
```

**Say:**  
"`_` is a convention that means 'I don't need this one'."

### Built-ins that return tuples

```python
result = divmod(17, 5)
print(result)          # (3, 2)

quotient, remainder = divmod(17, 5)
print(quotient, remainder)   # 3 2
```

**Say:**  
"Many Python functions give back more than one value, and they do it with a tuple. When we write our own functions in lesson 10, we'll `return` tuples the same way."

---

## 7. Looping over tuples

```python
models = ("gpt-small", "llama", "mistral")

for model in models:
    print("Testing:", model)
```

### Looping over a list of tuples (very common!)

```python
results = [
    ("doc1.txt", 0.92),
    ("doc2.txt", 0.75),
    ("doc3.txt", 0.40),
]

for filename, score in results:
    print(filename, "→", score)
```

```text
doc1.txt → 0.92
doc2.txt → 0.75
doc3.txt → 0.40
```

**Say:**  
"See how we unpack *inside* the `for`? Each item is a tuple `(filename, score)` and we split it straight into two variables. You will see this pattern everywhere in AI code."

---

## 8. Converting between lists and tuples

```python
nums_list = [3, 1, 2]
nums_tuple = tuple(nums_list)
print(nums_tuple)   # (3, 1, 2)

back = list(nums_tuple)
back.append(4)
print(back)         # [3, 1, 2, 4]
```

**Say:**  
"Need to change a tuple? Turn it into a list, change it, and turn it back if needed."

```python
print(tuple("abc"))   # ('a', 'b', 'c')
```

---

## 9. Small gotcha: a tuple can hold a list

```python
t = ("Ada", [70, 85])
t[1].append(90)
print(t)   # ('Ada', [70, 85, 90])
```

**Say:**  
"The tuple itself didn't change; it still holds the same two things. But the **list inside** is mutable, so it can change. Tuples are only fully 'frozen' if everything inside them is immutable too. Don't worry too much about this, just know it exists."

---

## 10. Tuple vs list: when to use which?

| Use a **list** when… | Use a **tuple** when… |
|---|---|
| The collection will grow or shrink | The data is a fixed record |
| All items are the same *kind* of thing | Each position has its own *meaning* |
| e.g. chat messages, files to process | e.g. `(x, y)`, `(name, age)`, `(text, score)` |

**Say:**  
"Simple rule: **list = many of the same thing, tuple = one thing with several parts.** A list of students; a tuple for one student's (name, age)."

---

## 11. Why tuples matter for AI engineering

```python
# Image / tensor shapes are tuples
image_shape = (224, 224, 3)      # height, width, colour channels
height, width, channels = image_shape

# Search / retrieval results: (document, similarity score)
hits = [("refund policy", 0.91), ("shipping info", 0.67)]
best_doc, best_score = hits[0]

# Fixed model settings you don't want changed by accident
SUPPORTED_MODELS = ("claude-sonnet", "claude-haiku", "claude-opus")
print("claude-haiku" in SUPPORTED_MODELS)   # True
```

**Say:**  
"When you use NumPy or PyTorch, `.shape` gives you a tuple. When you search a vector database, results are often (text, score) pairs. Tuples are everywhere."

---

## 12. Worked example: ranking retrieval results

**Live-code this from scratch, explaining each line:**

```python
# Each result is a tuple: (document_title, similarity_score)
results = [
    ("Refund policy", 0.82),
    ("Shipping times", 0.45),
    ("Return a product", 0.91),
    ("Contact support", 0.60),
]

# 1. Print every result
print("All results:")
for title, score in results:
    print("-", title, score)

# 2. Find the best one
best = results[0]
for item in results:
    if item[1] > best[1]:
        best = item

best_title, best_score = best
print("\nBest match:", best_title, "with score", best_score)

# 3. Keep only good matches (score >= 0.6)
good = []
for title, score in results:
    if score >= 0.6:
        good.append((title, score))   # note the double brackets: we append a tuple

print("\nGood matches:", good)
print("Number of good matches:", len(good))
```

```text
All results:
- Refund policy 0.82
- Shipping times 0.45
- Return a product 0.91
- Contact support 0.6

Best match: Return a product with score 0.91

Good matches: [('Refund policy', 0.82), ('Return a product', 0.91), ('Contact support', 0.6)]
Number of good matches: 3
```

**Say:**  
"Notice the combination: a **list** (because results can grow) of **tuples** (because each result is a fixed pair). That's the pattern to remember."

> The `if` here is a sneak preview of control flow (lesson 08). Keep it simple and just read it aloud: "if the score is bigger than the best so far…"

---

## Quick-check questions (ask the class)

1. What's the output of `type((7))`? → `int`
2. How do you make a tuple containing just `"hi"`? → `("hi",)`
3. What happens with `t = (1, 2); t[0] = 9`? → `TypeError`
4. After `a, b = 10, 20` then `a, b = b, a`, what is `a`? → `20`
5. `first, *rest = (1, 2, 3, 4)`: what is `rest`? → `[2, 3, 4]` (a list)
6. Would you store a user's chat history in a list or tuple? → **List** (it grows)
7. Would you store an image size `(width, height)` in a list or tuple? → **Tuple** (fixed record)

---

## Mini practice (5–10 min in class)

```python
# 1. Create a tuple called `location` with a city name, latitude, longitude.
#    Unpack it into three variables and print them.

# 2. Given:
colors = ("red", "blue", "red", "green", "red")
#    Print how many times "red" appears and the index of "green".

# 3. Swap these two variables in ONE line:
x = "left"
y = "right"

# 4. Given:
scores = (88, 92, 79, 65, 95)
#    Use unpacking with * to get the first score and the rest.
#    Print the max, min and sum of the scores.

# 5. Given:
pairs = [("apple", 3), ("banana", 5), ("mango", 2)]
#    Loop and print: "apple: 3", "banana: 5", ...
```

---

## Cheat sheet

```text
ordered + IMMUTABLE

t = (1, 2, 3)       tuple
t = 1, 2, 3         also a tuple (comma makes it)
t = (5,)            one-item tuple (comma required!)
t = ()              empty tuple

t[0]  t[-1]  t[1:3]  t[::-1]
len(t)  sum(t)  min(t)  max(t)  x in t
sorted(t)           → returns a LIST

t.count(x)          how many times
t.index(x)          position of first x

a, b, c = t         unpacking
a, b = b, a         swap
first, *rest = t    star collects the rest (as a list)
name, _, city = t   _ ignores a value

for a, b in list_of_pairs:   unpack in loops

tuple(my_list)      list  → tuple
list(my_tuple)      tuple → list

t[0] = 9            ✗ TypeError
t.append(9)         ✗ no such method
```

---

## Teaching order (use this sequence)

1. Reminder table: str / list / tuple  
2. What a tuple is + `()` syntax  
3. "The comma makes the tuple"  
4. One-item tuple trap `(5)` vs `(5,)`  
5. Indexing / slicing / `len` / `in` (quick, same as lists)  
6. **Immutable** demo (let the `TypeError` happen live)  
7. "Make a new one" instead of changing  
8. Why immutability is useful  
9. `count` / `index` + `sum` `min` `max` `sorted`  
10. ⭐ Unpacking → error when counts don't match  
11. Swap trick  
12. `*rest` and `_`  
13. `divmod` (functions returning tuples)  
14. Looping over a list of tuples  
15. `list()` / `tuple()` conversion  
16. Tuple-containing-a-list gotcha (short)  
17. List vs tuple decision table  
18. AI examples (shapes, search results)  
19. Worked example: ranking retrieval results  
20. Quick-check questions → mini practice  

---

## Summary

- A **tuple** stores ordered items in `()`; **the comma** is what really makes it
- Tuples are **immutable**: no changing, adding, or removing
- One-item tuples need a trailing comma: `(5,)`
- Indexing and slicing work just like strings and lists
- Only two methods: `count` and `index`
- **Unpacking** (`a, b = t`) is the superpower: swap, `*rest`, loops over pairs
- Rule of thumb: **list = many of the same thing, tuple = one thing with several parts**

## Practice location

See the module's `exercises/` folder and the weekly assignment in `CURRENT_WEEK.md`.
