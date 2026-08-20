sentence = input("Enter a sentence: ")
words = sentence.split()

if words:
  shortest = words[0]
  for w in words:
    if len(w) < len(shortest):
      shortest = w
  print("Shortest word:", shortest)
else:
  print("No words entered.")