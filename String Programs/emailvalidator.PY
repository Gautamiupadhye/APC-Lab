email = input("Enter email address: ")
if email.count("@") == 1 and email.endswith(".com") and len(email) > 5:
    print("Valid email format.")
else:
    print("Invalid email format.")