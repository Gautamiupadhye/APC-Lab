user_string = input("Enter a string: ")
no_space_string = ""

for char in user_string:
  if char != " ":
    no_space_string += char

print("String without spaces:", no_space_string)