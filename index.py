import csv
import hashlib
import os

isAuthenticated = False

def hash_password(pwd):
    pwd = pwd.encode('utf-8')
    hashed_pwd = hashlib.sha256(pwd).hexdigest()
    return hashed_pwd


def authenticate(usr, pw):
    with open('db.csv', 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            if line[0] == usr:
                if line[1] == pw:
                    return True
        return False
            

def addAccount(usrnam, passw):
    with open('db.csv', 'a') as file:
        writer = csv.writer(file)
        hash_passw = hash_password(passw)
        writer.writerow([usrnam, hash_passw])


def checkUsername(username):
    with open('db.csv', 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            if line[0] == username:
                return True
        return False

def Register():
    print(f"Register your account\n")
    username = input(f"Enter Username: ")
    if checkUsername(username):
        print(f"You already have an account. Please login.")
    else:
        password = input(f"Enter password: ")
        addAccount(username, password)
        print(f"Account has been created. Please login now.")


def Login():
    username = input(f"Enter Username: ")
    if checkUsername(username):
        password = input(f"Enter password: ")
        hashpassword = hash_password(password)
        if authenticate(username, hashpassword):
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