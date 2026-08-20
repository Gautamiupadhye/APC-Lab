user_string = input("Enter a string: ")
checked = ""

for char in user_string:
  if char not in checked:
    count = 0
    for c in user_string:
      if c == char:
        count += 1
    print(f"{char}: {count}")
    checked += char