text = input("Enter a message: ")
shift = int(input("Enter shift value: "))
cipher_text = ""

for char in text:
    if char.isalpha():
        ascii_offset = ord("A") if char.isupper() else ord("a")
        cipher_text += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
    else:
        cipher_text += char

print("Encrypted/Decrypted message:", cipher_text)