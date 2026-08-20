sentence = input("Enter a sentence: ")
words = sentence.split()
title_words = []

for w in words:
  if w:
    title_word = w[0].upper() + w[1:].lower()
    title_words.append(title_word)

print("Title case:", " ".join(title_words))