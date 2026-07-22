```markdown
# Caesar Cipher

A command-line Caesar cipher in Python with three modes: encode, decode, and brute-force crack.

Built while learning Python fundamentals — strings, loops, and how characters map to numbers in ASCII.

## What it does

The Caesar cipher shifts each letter a fixed number of positions through the alphabet.

```
a -> d   (shift 3)
b -> e
z -> c   (wraps around)
```

- Handles uppercase and lowercase correctly
- Leaves spaces, punctuation, and digits unchanged
- Works with any shift value, including negative ones
- **Crack mode** — recovers the message without knowing the key

## Why crack mode matters

The Caesar cipher has only 25 possible keys, so trying all of them takes microseconds. Crack mode prints every candidate; the readable one is the answer. This is the reason the cipher is a historical curiosity rather than real encryption — the keyspace is far too small.

## Examples

Encoding:
```
encode / decode / crack: encode
Text: Hello, World!
Shift: 3
Khoor, Zruog!
```

Cracking without the key:
```
encode / decode / crack: crack
Text: Khoor, Zruog!
 1: Jgnnq, Yqtnf!
 2: Ifmmp, Xpsme!
 3: Hello, World!     <- readable
 4: Gdkkn, Vnqkc!
 ...
```

## How it works

A single function handles both directions — decoding is just encoding with a negative shift:

```python
def caesar(text: str, shift: int) -> str:
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char
    return result
```

Each letter is converted to a number with `ord()`, shifted, wrapped with `% 26`, and converted back with `chr()`. Subtracting `ord('A')` or `ord('a')` maps the letter to the range 0–25 first, so the arithmetic works the same for both cases.

Crack mode simply calls this function 25 times with every possible negative shift.

## How to run

Requires Python 3. No dependencies.

```bash
python caesar_cipher.py
```

## What I learned

- ASCII and converting between characters and integers with `ord()` / `chr()`
- Modular arithmetic for wrapping values around a fixed range
- Why one function with a signed parameter beats two near-identical functions
- Handling invalid input without crashing
- That a small keyspace makes a cipher trivially breakable

## Possible improvements

- Automatic key detection via letter frequency analysis instead of manual inspection
- Command-line arguments (`argparse`) instead of interactive prompts
- Unit tests
```
