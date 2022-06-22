




def show_homepage():
    
    print("\n===  KING BANKING APP Homepage  ===\n")
    print("-----------------------------------")
    print("|1.   YE OLDE Login    |2.    YE OLDE Register     |")
    print("-----------------------------------")
    print("|3.    YE OLDE Donate   |4. SHOW YE OLDE Donations |")
    print("-----------------------------------")
    print("| 5.Leave once you Donate enough money.|")
    print("-----------------------------------")


def login(database, username, password):
    if username in database and database[username] == password:
        print("Welcome! ", username)
        return username
    elif username in database.keys() and password not in database.values():
        print("Wrong Password")
        return ""
    else:
        print("User not found. Please register.")
        return ""


def register(database, username):
    if username in database:
        print("Username already registered.")
        return ""
    else:
        print("Username has been registered.")
        return username




def donate(username):
    donation_amt = int(input("Enter amount to donate: "))
    donation_string = donation_amt
    print("Thank you for the donation! :)")
    return donation_string


def show_donations(donations):
    print("\n---All Donations---")
    if donations == []:
        print("Currently, there are no donations.")
    else:
        for x in donations:
            print(x)




def app():
    database = {"admin": "password123"}
    donations = []
    authorized_user = ""
    
    
    while True:

        show_homepage()
        if authorized_user == "":
            print("You must be logged in to donate.")
            
        else:
            print("Logged in as: ", authorized_user)

        user_input = input("Choose an Option: ")

        if user_input == "1":
            username = input("What is your user name? ")
            password = input("What is your password? ")
            authorized_user = login(database, username, password)
            continue
        elif user_input == "2":
            username = input("What is your username? ")
            password = input("What is your password? ")
            authorized_user = register(database, username)
            if authorized_user != "":
                database[username] = password
            continue
        elif user_input == "3":
            if authorized_user == "":
                print("You are not logged in.")
            else:
                donation_string = donate(authorized_user)
                donations.append(donation_string)
               
                
            continue
        elif user_input == "4":
            show_donations(donations)
        elif user_input == "5":
            donation_amt = donations[-1]
            if donation_amt  >= 20000:
                print("You have Donated enough to the greedy King Banking App and are free to go,\n")
                break
            if donation_amt  < 20000:
                print("You Need to Donate More Money!")

