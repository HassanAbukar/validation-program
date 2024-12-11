user_input = input("Enter user name : ")

if len(user_input) > 12:
    print("Username must not be greater than 12 character")
elif not  user_input.find(" ") == -1:
    print("Space is not allowed") 
elif not user_input.isalpha():
    print("digit is not allowed")
else:
    print(f"Welcome {user_input}")