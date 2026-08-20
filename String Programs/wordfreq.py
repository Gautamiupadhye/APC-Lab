paragraph = input("Enter a paragraph: ")
words = paragraph.split()
word_freq = {}

for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

print("Word Frequencies:")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")