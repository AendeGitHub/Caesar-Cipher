# Caesar Cipher

A simple command-line Caesar cipher written in Python. You type a word, choose a shift number, and the program encrypts or decrypts it.

This is one of my first Python projects — I built it while learning the basics of loops, strings, and how characters are stored as numbers (ASCII).

## What it does

The Caesar cipher is one of the oldest known encryption methods. Each letter is replaced by another letter a fixed number of positions further down the alphabet.

```
a -> d   (shift 3)
b -> e
z -> c   (wraps around the end of the alphabet)
```

- Handles both **uppercase and lowercase** letters correctly
- **Spaces, punctuation, and numbers** are left unchanged
- Supports **any shift number**, not just 3
- Two modes: **encrypt** and **decrypt**

## Example

```
Encrypt or Decrypt? (e/d): e
Word: Hello, World!
Shift number: 3
Khoor, Zruog!

Encrypt or Decrypt? (e/d): d
Word: Khoor, Zruog!
Shift number: 3
Hello, World!
```

## How it works

The program reads a word and goes through it letter by letter:

1. Ask the user to choose encrypt (`e`) or decrypt (`d`)
2. Convert each letter to a number with `ord()`
3. Shift it forward or backward using `% 26` so the alphabet wraps around
4. Convert the number back to a letter with `chr()`
5. Leave spaces and punctuation unchanged

```python
mode = input("Encrypt or Decrypt? (e/d): ")
Caesar = input("Word: ")
j = int(input("Shift number: "))
result = ""

for char in Caesar:
    if char.isupper():
        shifted = (ord(char) - ord('A') + (j if mode == 'e' else -j)) % 26 + ord('A')
        result += chr(shifted)
    elif char.islower():
        shifted = (ord(char) - ord('a') + (j if mode == 'e' else -j)) % 26 + ord('a')
        result += chr(shifted)
    else:
        result += char

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
- The difference between uppercase (`ord('A')`) and lowercase (`ord('a')`) in ASCII
- Using `isupper()` and `islower()` to handle different cases
- Reading input from the command line with `input()`

---

*Made while learning Python.*
