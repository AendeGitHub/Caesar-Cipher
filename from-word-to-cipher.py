Caesar = input("Word to convert Caesar-Cipher: ")
result = ""

for char in Caesar:
    shifted = (ord(char) - ord('a') + 3) % 26 + ord('a')
    result += chr(shifted)

print(result)