user_string = input("Enter a string: ")
duplicates = ""

for char in user_string:
  if user_string.count(char) > 1 and char not in duplicates:
    duplicates += char

print("Duplicate characters:", duplicates)