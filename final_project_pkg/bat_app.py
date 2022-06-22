
def show_homepage():
    print("\n===  GIANT FRUIT BAT'S DONATION APP Homepage  ===\n")
    print("-----------------------------------")
    print("|1.   Login    |2.   Register     |")
    print("-----------------------------------")
    print("|3.   Donate   |4. Show Donations |")
    print("-----------------------------------")
    print("| 5.Leave once you Donate all the fruits.|")
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
    donation_amt = str(input("Enter fruit to donate: "))
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




def bat_app():
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
            if donation_amt  == 'MANGOES' :
                print("You have Donated MANGOES to the Giant Fruit Bat and it is happy,\nYou hop on the back of the Fruit Bat and it flys you out of the cave!")
                break
            elif donation_amt  != "MANGOES":
                print("You Need to Donate MANGOES!")
