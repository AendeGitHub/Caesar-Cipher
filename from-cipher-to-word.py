Caesar = input("Caesar-Cipher to convert Word: ")
j = int(input("number: "))
result = ""

for char in Caesar:
    if char.isupper():  
        shifted = (ord(char) - ord('A') - j) % 26 + ord('A')
        result += chr(shifted)
    elif char.islower():  
        shifted = (ord(char) - ord('a') - j) % 26 + ord('a')
        result += chr(shifted)
    else: 
        result += char

print(result)