db = {}
isAuthenticated = False

def checkUsername(username):
    return username in db.keys()

def Register():
    print(f"Register your account\n")
    username = input(f"Enter Username: ")
    if checkUsername(username):
        print(f"You already have an account. Please login.")
    else:
        password = input(f"Enter password: ")
        db[username] = password
        print(f"Account has been created. Please login now.")


def Login():
    username = input(f"Enter Username: ")
    if checkUsername(username):
        password = input(f"Enter password: ")
        if db[username] == password:
            global isAuthenticated
            isAuthenticated = True
            print(f"You are logged in.")
        else:
            print(f"Wrong password. Try again")
            return
    else:
        print(f"Wrong Username. Try again.")
        return
        

def Logout():
    global isAuthenticated
    if isAuthenticated:
        isAuthenticated = False
        print(f"You successfully logged out.")
    else:
        print(f"You were never logged in .")

def main():
    while True:
        usr_choice = int(input(f"Enter your choice (Register[1], Login[2], Logout[3], Quit[4]): "))
        if usr_choice == 1:
            Register()
        elif usr_choice == 2:
            Login()
        elif usr_choice == 3:
            Logout()
        elif usr_choice == 4:
            print(f"You will not be missed !!")
            break
        else:
            print(f"Choice invalid, please retry.")

if __name__ == '__main__':
    main()