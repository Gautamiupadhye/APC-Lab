s = input("Enter string: ")
encoded = ""
count = 1

for i in range(1, len(s)):
  if s[i] == s[i - 1]:
    count += 1
  else:
    encoded += s[i - 1] + str(count)
    count = 1

if s:
  encoded += s[-1] + str(count)

if len(encoded) < len(s):
  print("Compressed:", encoded)
else:
  print("Original:", s)