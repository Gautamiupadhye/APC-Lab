sentence = input("Enter a sentence: ")
word = input("Enter word to count: ")
words = sentence.split()
count = 0

for w in words:
  if w == word:
    count += 1

print(f"The word '{word}' appears {count} times.")