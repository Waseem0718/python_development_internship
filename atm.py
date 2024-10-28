from cardholder import cardholder

def print_menu():
    print("please choose from any one of the following option...")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. balance")
    print("4. Exit")

def deposit(cardholder):
    try:
        deposit = float(input("How much amount would you like to deposit: "))
        cardholder.set_balance(cardholder.get_balance() + deposit)
        print("Thank you for your money, your new balance is ",str(cardholder.get_balance()))
    except:
        print("Invlid input")
def withdraw(cardholder):
    try:
        withdraw = float(input("How much money you want to withdraw: "))
        ## check user has enough money
        if withdraw > cardholder.get_balance():
            print("Insufficient Balance :( ")
        else:
            cardholder.set_balance(cardholder.get_balance() - withdraw)
            print("you are good to go, your current balance is ",cardholder.get_balance())
            print("Enjoy your money :)")
    except:
        print("Invlid input")

def checkbalance(cardholder):
    print("Your current balance is ",cardholder.get_balance())

if __name__ ==  "__main__" :

    current_user = cardholder("","","","","")

    list_of_cardholder = []
    list_of_cardholder.append(cardholder("5678123434566789",1234, "joe", "root", 345.54))
    list_of_cardholder.append(cardholder("7462831234724482",4334, "steve", "job", 212.19))
    list_of_cardholder.append(cardholder("8466272948281232",8834, "aman", "nisham", 34.54))
    list_of_cardholder.append(cardholder("9463272548281236",1211, "jai", "guru", 451.94))
    list_of_cardholder.append(cardholder("1146322448281233",1255, "thor", "gue", 735.50))

#prompt uder for debit card number
    debitcardnum = ""
    while True:
        try:
            debitcardnum = input("please insert your Debit card: ")
            debitmatch = [holder for holder in list_of_cardholder if holder.cardnum == debitcardnum]
            if (len(debitmatch) > 0):
                current_user = debitmatch[0]
                break
            else:
                print("card number not recognized.Please try again")

        except:
            print("card number not recognized.Please try again")
    
    #prompt for pin
    while True:
        try:
            userPIN = int(input("Enter the PIN: ".strip()))
            if(current_user.get_pin() == userPIN):
                break
            else:
                print("invalid PIN!, please try again")
        except:
            print("invalid PIN!, please try again")

#selection of options
    print("Welcome ",current_user.get_firstname(), ":)")
    option = 0
    while(True):
        print_menu()
        try:
           option = int(input()) 
        except:
            print("Invalid input, pleas try again.")

        if(option == 1):
            deposit(current_user)
        elif (option == 2):
            withdraw(current_user)
        elif (option == 3):
            checkbalance(current_user)
        elif (option == 4):
            break
        else:
            option = 0

    print("Thank you, have a nice day :)")

        