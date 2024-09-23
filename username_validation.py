# Validate user input exercise
# 1 - Username is not longer than 12 characters
# 2 - username must not contain spaces
# 3 - username must not contain digits

username = input("Enter your username: ")

if username.__len__() > 12:
    print("Username cannot be longer than 12 characters long.")
elif username.find(" ") != -1:
    print("Username cannot contain spaces")
elif username.isalnum() == 0:
    print("Username cannot contain digits.")
else:
    print("The username is valid. good stuff.")