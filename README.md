# Caesar Cipher

A simple command-line Caesar cipher written in Python. You type a word, and the program shifts each letter forward by 3 positions in the alphabet.

This is one of my first Python projects — I built it while learning the basics of loops, strings, and how characters are stored as numbers (ASCII).

## What it does

The Caesar cipher is one of the oldest known encryption methods. Each letter is replaced by another letter a fixed number of positions further down the alphabet. This version uses a shift of **+3**, the same one Julius Caesar is said to have used.

```
a -> d
b -> e
x -> a   (wraps around the end of the alphabet)
```

## Example

```
Word to convert Caesar-Cipher: khussein
nkxvvhlq
```

## How it works

The program reads a word and goes through it letter by letter:

1. Convert each letter to a number with `ord()`
2. Shift it forward by 3, using `% 26` so the alphabet wraps around (`z` becomes `c`)
3. Convert the number back to a letter with `chr()`

```python
Caesar = input("Word to convert Caesar-Cipher: ")
result = ""

for char in Caesar:
    shifted = (ord(char) - ord('a') + 3) % 26 + ord('a')
    result += chr(shifted)

print(result)
```

## How to run

Make sure you have Python 3 installed, then run:

```bash
python caesar_cipher.py
```

## What I learned

- How characters map to numbers (ASCII), and converting between them with `ord()` and `chr()`
- Looping through the characters of a string in Python
- Using the modulo operator `%` to wrap values around a fixed range
- Reading input from the command line with `input()`


---

*Made while learning Python.*
