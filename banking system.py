class User:
    def __init__(self, first_name, last_name, gender, street_address, city,
                 email, cc_number, cc_type, balance, account_no):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.street_address = street_address
        self.city = city
        self.email = email
        self.cc_number = cc_number
        self.cc_type = cc_type
        self.balance = balance
        self.account_no = account_no
        userList.append(self)

    def displayInfo(self):
        print("**********************************************")
        print("User infomation:")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        if self.gender == "M":
            print(f"Gender: Male")
        else:
            print(f"Gender: Female")
        print(f"Address: {self.street_address}")
        print(f"City: {self.city}")
        print(f"Email: {self.email}")
        print(f"Credit Card Number: {self.cc_number}")
        print(f"Credit Card Type: {self.cc_type}")
        print(f"Balance: {self.balance}")
        print(f"Account Number: {self.account_no}")
        print("**********************************************")
        True


def generateUsers():
    import csv
    with open('bankUsers.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar="'")
        for line in filereader:
            User(line[0], line[1], line[2], line[3], line[4], line[5], line[6],
                 line[7], float(line[8]), line[9])


def findUser(user_list):
    # TO COMPLETE
    error = True
    user_name = input("Search by user's first name\n: ").title()
    for user in user_list:
        if user.first_name == user_name:
            user.displayInfo()
            error = False
    if error == True:
        print("")
        print("Error, user not found.")

    True


def overdrafts(user_list):
    num_of_overdrafts = 0
    overdraft_amount = 0
    print("**********************************************")
    print("Overdraft accounts:")
    print("")
    for user in user_list:
        if user.balance < 0:
            print(user.first_name, user.last_name)
            num_of_overdrafts += 1
            overdraft_amount += user.balance
    print("**********************************************")
    print(f"The number of overdraft accounts is {num_of_overdrafts}")
    print(f"The total amount overdraft is ${overdraft_amount:.2f}")
    print("**********************************************")
    True


def missingEmails(user_list):
    missing_emails = 0
    for user in user_list:
        if user.email == "":
            print(user.first_name, user.last_name)
            missing_emails += 1
    print("**********************************************")
    print(f"The number of users with missing emails is {missing_emails}")
    print("**********************************************")
    True


def bankDetails(user_list):
    bank_users = 0
    bank_total = 0
    lowest = 0
    highest = 0
    highest_first_name = ""
    highest_last_name = ""
    lowest_first_name = ""
    lowest_last_name = ""
    for user in user_list:
        bank_users += 1
        bank_total += user.balance
        if user.balance > highest:
            highest_first_name = user.first_name
            highest_last_name = user.last_name
            highest = user.balance
        if user.balance < lowest:
            lowest_first_name = user.first_name
            lowest_last_name = user.last_name
            lowest = user.balance
    print("**********************************************")
    print(f"The number of bank users is {bank_users} users")
    print(f"The Bank's total worth is ${bank_total:.2f}")
    print(f"The user with the highest balance is "
          f"{highest_first_name} {highest_last_name}"
          f"\nWith a total of ${highest}")
    print(f"The user with the lowest balance is "
          f"{lowest_first_name} {lowest_last_name}\nWith a total of ${lowest}")
    print("**********************************************")
    True


def transfer(user_list):
    acc_number = 0
    first_balance = 0
    second_balance = 0
    one_first_name = ""
    one_last_name = ""
    tran_amount = 0
    acc_transferred = 0
    repeat = 0
    acc_number = input("What is the account number: ")
    for user in user_list:
        if acc_number == user.account_no:
            print(f"Name: {user.first_name} {user.last_name}")
            print(f"Balance: {user.balance}")
            one_first_name = user.first_name
            one_last_name = user.last_name
            first_balance = user.balance
            while repeat != 1:
                tran_amount = float(input("How much would you like to transfer?\n$ "))
                if 0 < tran_amount <= user.balance:
                    acc_transferred = input("What is the account number to "
                                            "transfer to:")
                    repeat += 1
                else:
                    print("Sorry, that is not a valid amount")
            for user in user_list:
                if acc_transferred == user.account_no:
                    print(f"Name: {user.first_name} {user.last_name}")
                    print(f"Balance: {user.balance}")
                    yes_no = input("Confirm the transfer? (y) for yes, (n)"
                                   " for no \n: ").upper()
                    if yes_no == "Y":
                        second_balance = user.balance + tran_amount
                        first_balance -= tran_amount
                        print(f"Transfer complete. {one_first_name} has "
                              f"transferred ${tran_amount} to "
                              f"{user.first_name}")
                        print("**********************************************")
                        print(f"Name: {one_first_name} {one_last_name}")
                        print(f"New Balance: {first_balance}")
                        print("**********************************************")
                        print(f"Name: {user.first_name} {user.last_name}")
                        print(f"New Balance: {second_balance}")
                        print("**********************************************")



    True


userList = []
generateUsers()
userChoice = ""
print("Welcome")

while userChoice != "Q":
    print("What function would you like to run?")
    print("Type 1 to find a user")
    print("Type 2 to print overdraft information")
    print("Type 3 to print users with missing emails")
    print("Type 4 to print bank details")
    print("Type 5 to transfer money")
    print("Type Q to quit")
    userChoice = input("Enter choice: ")
    print()

    if userChoice == "1":
        findUser(userList)
    elif userChoice == "2":
        overdrafts(userList)
    elif userChoice == "3":
        missingEmails(userList)
    elif userChoice == "4":
        bankDetails(userList)
    elif userChoice == "5":
        transfer(userList)
    print()
