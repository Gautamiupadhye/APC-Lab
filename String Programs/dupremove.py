user_string = input("Enter a string: ")
result = ""

for char in user_string:
  if char not in result:
    result += char

print("Without duplicates:", result)