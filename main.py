from users import User
import getpass

while True:
    choice = input("choose a number between (0,1,2): ")
    match choice:
        case "0":
            break
        case "1":
            user_name = input("Enter a usernsme: ")
            password = getpass.getpass("Enter a password: ")
            User.submit(user_name, password)
        case "2":
            user_name = input("Enter your username: ")
            password = getpass.getpass("Enter your password: ")
            user = User(user_name, password)
            valid_profile = User.profile_validator(user, user_name, password)
            if valid_profile:
                while True:
                    choice = input("choose a number between (1,2,3,4): ")
                    match choice:
                        case "1":
                            print(User(user_name, password))
                        case "2":
                            user = User(user_name, password)
                            new_user_name = input("Enter new username: ")
                            new_phone = input("Enter new phone number: ")
                            User.update_profile(user, new_user_name, new_phone)
                        case "3":
                            user = User(user_name, password)
                            password = getpass.getpass("Enter your current password: ")
                            new_pass = getpass.getpass("Enter new password: ")
                            rep_new_pass = getpass.getpass("Repeat new password: ")
                            User.change_pass(user, password, new_pass, rep_new_pass)
                            
                        case "4":
                            print("Log out!")
                            break