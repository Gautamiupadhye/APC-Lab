text = input("Enter a string: ")
unique_chars = ""
for char in text:
    if char not in unique_chars:
        unique_chars += char

if len(unique_chars) < 2:
    print("Not enough unique characters.")
else:
    counts = []
    for char in unique_chars:
        counts.append((text.count(char), char))
    counts.sort(reverse=True)
    print("Second most frequent character:", counts[1][1])