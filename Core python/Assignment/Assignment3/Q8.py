import random

userid = input("Enter the user ID: ")
password = input("Enter the password: ")

if userid == "Admin" and password == "virat@123":
    captcha = random.randint(1000, 9999)
    print(f"Your captcha = {captcha}")

    chuser = int(input("Enter the captcha: "))

    if chuser == captcha:
        print("User login successfully.")
    else:
        print("Invalid captcha.")
else:
    print("Invalid user ID or password.")