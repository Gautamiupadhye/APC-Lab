pwd = input("Enter password: ")
has_upper = False
has_lower = False
has_digit = False
has_special = False

if len(pwd) >= 8:
  for char in pwd:
    if char >= "A" and char <= "Z":
      has_upper = True
    elif char >= "a" and char <= "z":
      has_lower = True
    elif char >= "0" and char <= "9":
      has_digit = True
    else:
      has_special = True

  if has_upper and has_lower and has_digit and has_special:
    print("Password is valid.")
  else:
    print("Password is invalid (missing required character types).")
else:
  print("Password must be at least 8 characters long.")