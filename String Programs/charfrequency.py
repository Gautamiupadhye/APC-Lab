user_string = input("Enter a string: ")
target = input("Enter character to find: ")
count = 0

for char in user_string:
  if char == target:
    count += 1

print(f"'{target}' appears {count} times.")