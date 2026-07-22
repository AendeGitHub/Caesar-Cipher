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


def crack(text: str) -> None:
    for shift in range(1, 26):
        print(f"{shift:2}: {caesar(text, -shift)}")


def main():
    mode = input("encode / decode / crack: ").strip().lower()
    if mode not in ("encode", "decode", "crack"):
        print("Only 'encode', 'decode' or 'crack'")
        return

    text = input("Text: ")

    if mode == "crack":
        crack(text)
        return

    try:
        shift = int(input("Shift: "))
    except ValueError:
        print("Shift must be an integer")
        return

    if mode == "decode":
        shift = -shift

    print(caesar(text, shift))


if __name__ == "__main__":
    main()