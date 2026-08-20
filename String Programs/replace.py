user_string = input("Enter a string: ")
old_char = input("Character to replace: ")
new_char = input("New character: ")

new_string = ""
for char in user_string:
  if char == old_char:
    new_string += new_char
  else:
    new_string += char

print("Updated string:", new_string)