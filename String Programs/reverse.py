user_string = input("Enter a string: ")

reversed_string = ""

for char in user_string:
  reversed_string = char + reversed_string

print("The reversed string is:", reversed_string)