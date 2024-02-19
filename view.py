from os import name, system
import pickle
import datetime
import time
from mudels import *

def deletpage():
    if name == "nt":
        system("cls")
    else:
        system("clear")


ids = []
passwords = []
manager_id = []
manager_password = []
def chose_1():
        passwords.append(int(input("pleas enter your password bank: ")))
        ids.append(int(input("pleas enter your ID: ")))
        name = input("pleas enter the your name: ")
        age = int(input("pleas enter the your age: "))
        gender = input("pleas enter the your gender: ")

        #pickle user in file users.pk
        string = f"name is: {name} age is: {age} and gender is: {gender}"
        pickled = pickle.dumps(string)
        file = open("users.pk", "ab")
        file.write(pickled)
        file.close()

        #delet the page
        time.sleep(1)
        deletpage()
        
        #show information the user
        
        print(colored(f"name is: {name} age is: {age} and gender is: {gender}", "green"))
        for i in ids:
            ide = i
        for  j in passwords:
            passworde = j

        print(colored(f"your id is {ide}", "blue"))
        print(colored(f"your password is {passworde}", "blue"))


def chose_2():
        id_bank = int(input("pleas enter the youe ID bank: "))
        balance = int(input("pleas enter your account balance: "))
        money = int(input("pleas enter your money: "))
        password = int(input("pleas enter the your password: "))
        print("1)money_out\n2)show balance")
        choice = int(input("select any option:"))
        if choice == 1:
                if id_bank in ids and password in passwords:
                    if money > balance:
                        print(colored("insufficient funds => your balance is: ","blue"),balance)
                    else:
                        balance -= money
                        print(colored("account balance has been update: ","red"),balance)
                
                else:
                    print(colored("your password and id is wrong...","yellow"))
        
        elif choice == 2:
            if id_bank in ids and password in passwords:
                print(colored("account balance is: ","green"),balance)


            else:
                print(colored("youe password and id is wrong...","yellow"))


        else:
            print("your chose is wrong pleas try again...")
        


def chose_3():
        amount_single = 0
        balance_credit = 0
        balance_time = 0
        cost = 3500
        id_user = int(input("pleas enter your id: "))
        balance = int(input("pleas enter the balance: "))
        if id_user in ids:
            print("1)single\n2)credit\n3)time_credit")
            chose_card = input("pleas chose the card: ")

            if chose_card == "1":
                password = int(input("pleas enter the bank password: "))
                if password in passwords:
                    balance -= 3500
                    amount_single += 3500
                    print(colored("account balance has been update: ","red"),balance)
                    print(colored("your balance card is: ", "blue"), amount_single)

                    #pickle the single cards
                    string = f"single card and the balance is {balance_time}"
                    pickled = pickle.dumps(string)
                    file = open("cards.py", "ab")
                    file.write(pickled)
                    file.close()


                else:
                    print("your password is wrong pleas try again...")
                

                time.sleep(3)
                deletpage()
                
            elif chose_card == "2":
                print(colored(f"your balance is {balance} Please charge your card", "green"))
                money_card = int(input("Please select the amount you want to deposit to the card: "))
                password = int(input("pleas enter the bank password: "))
                if password in passwords:
                    balance -= money_card
                    balance_credit += money_card
                    print(colored("account balance has been update: ","red"),balance)
                    print(colored("your balance card is: ", "blue"), balance_credit)

                    #pickle the credit cards
                    string = f"credit card and the balance is {balance_credit}"
                    pickled = pickle.dumps(string)
                    file = open("cards.pk", "ab")
                    file.write(pickled)
                    file.close()

                    if balance_credit > cost:
                        balance_credit -= cost
                        return True
                    else:
                        return False
                
                else:
                    print("your password is wrong pleas try again...")

                
                time.sleep(3)
                deletpage()

            elif chose_card == "3":
                print(colored(f"your balance is {balance} Please charge your card", "green"))
                money_card = int(input("Please select the amount you want to deposit to the card: "))
                password = int(input("pleas enter the bank password: "))
                if password in passwords:
                    current_day = datetime.now()
                    expiration_date = 2044
                    balance -= money_card
                    balance_time += money_card
                    print(colored("account balance has been update: ","red"),balance)
                    print(colored("your balance card is: ", "blue"), balance_time)
                    print("your expiration catd is: ", expiration_date)

                    #pickle the credit_time cards
                    string = f"credit_time card and the balance is {balance_time}"
                    pickled = pickle.dumps(string)
                    file = open("cards.pk", "ab")
                    file.write(pickled)
                    file.close()

                    if balance_time > cost:
                        if current_day < expiration_date:
                            balance_time -= cost
                            return True
                        else:
                            if current_day > expiration_date:
                                return False
                
                else:
                    print("your password is wrong pleas try again...")


                time.sleep(3)
                deletpage()
            
            else:
                print("your chose is wrong pleas try again...")

        else:
            print("your id is wrong pleas try again...")
            

def chose_4():
        print("your dier manager pleas login the sistem")
        manager()
        print(colored("your login in the sistem:)", "blue"))
        time.sleep(2)
        deletpage()
        id_manager = int(input("pleas enter your id manager: "))
        password = int(input("pleas enter the manager password: "))
        deletpage()
        if id_manager in manager_id and password in manager_password:
            chose = input("1)add a trip\n2)change trip\n3)delet trip\n4)show the cards\npleas chose a number: ")
            
            if chose == "1":
                for i in cost_matrix.items():
                    print(i)
                new_trip = dict(input("pleas enter your new trip: "))
                cost_matrix.update(new_trip)


            elif chose == "2":
                for i in cost_matrix.items():
                    print(i)
                ChangeTrip.change_trip()


            elif chose == "3":
                for i in cost_matrix.items():
                    print(i)
                DeletTrip.delet_trip()


            elif chose == "4":
                #read the file 
                file = open("cards.pk", "rb")
                file = pickle.load(file)
                print(file)


def manager():
    fullname = input("pleas enter your name: ")
    manager_id.append(int(input("pleas enter your manager id: ")))
    manager_password.append(int(input("pleas enter your manager password: ")))
    for i in manager_password:
        passworde = i

    string = f"manager fullname is: {fullname} and password is: {passworde}"
    pickled = pickle.dumps(string)
    file = open("users.pk", "ab")
    file.write(pickled)
    file.close()