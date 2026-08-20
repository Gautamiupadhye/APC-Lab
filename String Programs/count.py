user_string = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0
special_chars = 0

user_string = user_string.lower()

for char in user_string:
  if (
      char == 'a'
      or char == 'e'
      or char == 'i'
      or char == 'o'
      or char == 'u'
  ):
    vowels += 1

  elif char >= 'a' and char <= 'z':
    consonants += 1

  elif char >= '0' and char <= '9':
    digits += 1

  elif char == ' ':
    spaces += 1

  else:
    special_chars += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special Characters:", special_chars)