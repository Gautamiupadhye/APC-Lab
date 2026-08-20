text = input("Enter a string: ")
max_char = ""
max_count = 0

for char in text:
    count = text.count(char)
    if count > max_count:
        max_count = count
        max_char = char

print(f"Most frequent character: '{max_char}'")