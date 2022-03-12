print("\nRegister\n")
while True: 
    user = str(input("Username: "))
    if len(user) > 0 and len(user) < 20:
        break
    print("Enter a valid username")
while True:
    pwd = str(input("Password: "))
    if len(pwd) > 5 and len(pwd) < 16:
        break
    print("Enter a valid password.")

print("\nLogin\n")
while True:
    user_login = str(input("Username: "))
    if user_login == user:
        break
    print("Usernames does not match")
while True:
    pwd_login = str(input("Password: "))
    if pwd_login == pwd:
        break 
    print("Passwords does not match")