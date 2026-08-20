user_string = input("Enter a sentence: ")
words = user_string.split()
count = 0

for w in words:
  count += 1

print("Total words:", count)