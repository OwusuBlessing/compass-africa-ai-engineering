# Exercise 01 — Run and print

**Lessons:** `01-python-prerequisites`  
**Difficulty:** Beginner

## Goal
Confirm your Python setup works, write a short script, and print values to the terminal.

## Starter input
Create a file named `hello_ai.py` (in your own practice folder or notebook) and use these values:

```python
course = "Compass Africa AI Engineering"
module = 1
ready = True
```

## Tasks
1. Print a welcome line that includes the course name.
2. Print the module number.
3. Print whether you are ready (`ready`).
4. Print the type of each of the three variables using `type()`.

## Expected output
Your output should look like this (wording can vary slightly, types must match):

```text
Welcome to Compass Africa AI Engineering
Module: 1
Ready: True
<class 'str'>
<class 'int'>
<class 'bool'>
```

## Hints
- Run a file with `python hello_ai.py` (or `python3 hello_ai.py`).
- `print()` can take multiple arguments: `print("Module:", module)`.
- `type(course)` returns the data type object; printing it shows `<class 'str'>`.

## Stretch
Add a multi-line string (triple quotes) called `notes` with two short lines about why you are learning AI engineering, then print it.
