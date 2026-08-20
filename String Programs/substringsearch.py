main_str = input("Enter main string: ")
sub_str = input("Enter substring to search: ")

if sub_str in main_str:
  print("Substring found!")
else:
  print("Substring not found.")