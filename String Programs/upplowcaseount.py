user_string = input("Enter a string: ")

uppercase_count = 0
lowercase_count = 0

for char in user_string:
  if char >= "A" and char <= "Z":
    uppercase_count += 1
  elif char >= "a" and char <= "z":
    lowercase_count += 1

print("Uppercase letters:", uppercase_count)
print("Lowercase letters:", lowercase_count)