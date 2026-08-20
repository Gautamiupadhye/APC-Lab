user_string = input("Enter a string: ")

reversed_string = ""
for char in user_string:
  reversed_string = char + reversed_string

if user_string == reversed_string:
  print("The string is a palindrome.")
else:
  print("The string is not a palindrome.")