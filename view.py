import os
import logging
from os import name, system
import pickle
import datetime
import time
from mudels import *
from datetime import datetime
#=======================================================
def deletpage():
    if name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
#================================================
now = datetime.now()
#login check acount
def check_login():
    id = int(len(User.list_user)+1000)
    name = input("pleas enter your name: ")
    password=input("pleas enter the password: ")
    ml=input("if male = m\nif fmale = f: ")
    #pickle the users
    string = f"your id{id}, your name{name}, your password{password}"
    pickled = pickle.dumps(string)
    file = open("users.pk", "ab")
    file.write(pickled)
    file.close()
    #===========================================
    if ml.startswith("m"):
        gender=True
    else:
        gender=False
    x=User(id,name,password,gender)
    print(f"you are register your id is {id}")
    logging.basicConfig(filename="metro.log", level=logging.INFO)
    logging.info(f"the user login width password {password} and id {id}: at time {now}")
    return x
#==========================================================================
#managment_bank
def bank_sistm():
            password_bank = int(input("pleas enter the bank password: "))
            balance = int(input("pleas enter your account balance: ")) 
            deletpage()
            print("1)money_in\n2)money_out\n3)show_balance")
            choice = int(input("select any option:"))
            deletpage()
            if choice == 1:
                    money = int(input("Please deposit the amount you want: "))
                    balance += money
                    print(f"Deposit successfully completed Your balance is {balance}")
                    logging.basicConfig(filename="metro.log", level=logging.INFO)
                    logging.info(f"The user deposited {money} to account: at time {now}")
            
            elif choice == 2:
                money = int(input("Please picking up the amount you want: "))
                password = int(input("pleas enter the password: "))
                if password == password_bank:
                    if money > balance:
                        print(colored("insufficient funds => your balance is: ","blue"),balance)
                    else:
                        balance -= money
                        print(colored("account balance has been update: ","red"),balance)
                        logging.basicConfig(filename="metro.log", level=logging.INFO)
                        logging.info(f"The user widthdrew {money} to account: at time {now}")

                else:
                    logging.basicConfig(filename="metro.log", level=logging.INFO)
                    logging.info(f"The user could not deposit money into her account due to incorrect password: at time {now}")
                    print(colored("your password is wrong...","yellow"))

            elif choice == 3:
                password = int(input("pleas enter the password: "))
                if password == password_bank:
                    print(f"your balance is {balance}")
                    logging.basicConfig(filename="metro.log", level=logging.INFO)
                    logging.info(f"The user took a balance from his account on the time: {now}")

                else:
                    logging.basicConfig(filename="metro.log", level=logging.INFO)
                    logging.info(f"user could not check card balance due to incorrect password on the time: {now}")
                    print(colored("your password is wrong...","yellow"))

            else:
                print(colored("your chose is wrong...","yellow"))
#=================================================================================
def delet_trip():
    trip_chose = input("1)gholhak to bime\n2)azadi to gholhak\n3)vardavard to aslamshahr\n4)sadr to pasdaran\npleas chose your trip: ")
    if trip_chose == "1":
        del cost_matrix["gholhak"]
        logging.basicConfig(filename="metro.log", level=logging.INFO)
        logging.info("the manager delet the trip 1")

    elif trip_chose == "2":
        del cost_matrix["azadi"]
        logging.basicConfig(filename="metro.log", level=logging.INFO)
        logging.info("the manager delet the trip 2")

    elif trip_chose == "3":
        del cost_matrix["vardavard"]
        logging.basicConfig(filename="metro.log", level=logging.INFO)
        logging.info("the manager delet the trip 3")

    elif trip_chose == "4":
        del cost_matrix["sadr"]
        logging.basicConfig(filename="metro.log", level=logging.INFO)
        logging.info("the manager delet the trip 4")

    else:
        print("your chose is wrong!pleas try again...")
#===============================================================================
def change_trip():
    trip_chose = input("1)gholhak to bime\n2)azadi to gholhak\n3)vardavard to aslamshahr\n4)sadr to pasdaran\npleas chose your trip: ")
    deletpage()
    if trip_chose == "1":
        print("1)origin\n2)destination\n3)cost\n4)end_time")
        change = int(input("Which part of the trip do you want to change: "))
        deletpage()
        deletpage()
        if change == 1:
            origin = input("pleas enter the new origin: ")
            cost_matrix["gholhak"]= origin
            logging.basicConfig(filename="metro.log", level=logging.INFO)
            logging.info(f"the manager change the origin trip 1 on the time: {now}, and new origin is {origin}")


        elif change == 2:
            destination = input("pleas enter the new destination: ")
            cost_matrix["gholhak"]["b"] = destination
            logging.basicConfig(filename="metro.log", level=logging.INFO)
            logging.info(f"the manager change the destination trip 1 on the time: {now}, and new destination is {destination}")

        elif change == 3:
            cost = int(input("pleas enter the new cost: "))
            cost_matrix["gholhak"]["cost"] = cost
            logging.basicConfig(filename="metro.log", level=logging.INFO)
            logging.info(f"the manager change the cost trip 1 on the time: {now}, and new cost is {cost}")

        elif change == 4:
            end_time = input("pleas enter the new end_time: ")
            cost_matrix["gholhak"]["end_time"] = end_time
            logging.basicConfig(filename="metro.log", level=logging.INFO)
            logging.info(f"the manager change the end_time trip 1 on the time: {now}, and new end_time is {end_time}")

        else:
            print("your chose is wrong...")


    elif trip_chose == "2":
        print("1)origin\n2)destination\n3)cost\n4)end_time")
        change = int(input("Which part of the trip do you want to change: "))
        deletpage()
        if change == 1:
            origin = input("pleas enter the new origin: ")
            cost_matrix["azadi"] = origin
            logging.basicConfig(filename="metro.log", level=logging.INFO)
            logging.info(f"the manager change the origin trip 2 on the time: {now}, and new origin is {origin}")

        elif change == 2:
            destination = input("pleas enter the new destination: ")
            cost_matrix["azadi"]["a"] = destination
            logging.basicConfig(filename="metro.log", level=logging.INFO)
            logging.info(f"the manager change the destination trip 2 on the time: {now}, and new destination is {destination}")

        elif change == 3:
            cost = int(input("pleas enter the new cost: "))
            cost_matrix["azadi"]["cost"] = cost
            logging.basicConfig(filename="metro.log", level=logging.INFO)
            logging.info(f"the manager change the cost trip 2 on the time: {now}, and new cost is {cost}")

        elif change == 4:
            end_time = input("pleas enter the new end_time: ")
            cost_matrix["azadi"]["end_time"] = end_time
            logging.basicConfig(filename="metro.log", level=logging.INFO)
            logging.info(f"the manager change the end_time trip 2 on the time: {now}, and new end_time is {end_time}")

        else:
            print("your chose is wrong...")


    elif trip_chose == "3":
        print("1)origin\n2)destination\n3)cost\n4)end_time")
        change = int(input("Which part of the trip do you want to change: "))
        deletpage()
        if change == 1:
            origin = input("pleas enter the new origin: ")
            cost_matrix["vardavard"] = origin
            logging.basicConfig(filename="metro.log", level=logging.INFO)
            logging.info(f"the manager change the origin trip 3 on the time: {now}, and new origin is {origin}")

        elif change == 2:
            destination = input("pleas enter the new destination: ")
            cost_matrix["vardavard"]["b"] = destination
            logging.basicConfig(filename="metro.log", level=logging.INFO)
            logging.info(f"the manager change the destination trip 3 on the time: {now}, and new destination is {destination}")

        elif change == 3:
            cost = int(input("pleas enter the new cost: "))
            cost_matrix["vardavard"]["cost"] = cost
            logging.basicConfig(filename="metro.log", level=logging.INFO)
            logging.info(f"the manager change the cost trip 3 on the time: {now}, and new cost is {cost}")

        elif change == 4:
            end_time = input("pleas enter the new end_time: ")
            cost_matrix["vardavard"]["end_time"] = end_time
            logging.basicConfig(filename="metro.log", level=logging.INFO)
            logging.info(f"the manager change the end_time trip 3 on the time: {now}, and new end_time is {end_time}")

        else:
            print("your chose is wrong...")

    elif trip_chose == "4":
        print("1)origin\n2)destination\n3)cost\n4)end_time")
        change = int(input("Which part of the trip do you want to change: "))
        deletpage()
        if change == 1:
            origin = input("pleas enter the new origin: ")
            cost_matrix["sadr"] = origin
            logging.basicConfig(filename="metro.log", level=logging.INFO)
            logging.info(f"the manager change the origin trip 4 on the time: {now}, and new origin is {origin}")

        elif change == 2:
            destination = input("pleas enter the new destination: ")
            cost_matrix["sadr"]["a"] = destination
            logging.basicConfig(filename="metro.log", level=logging.INFO)
            logging.info(f"the manager change the destination trip 4 on the time: {now}, and new destination is {destination}")

        elif change == 3:
            cost = int(input("pleas enter the new cost: "))
            cost_matrix["sadr"]["cost"] = cost
            logging.basicConfig(filename="metro.log", level=logging.INFO)
            logging.info(f"the manager change the cost trip 4 on the time: {now}, and new cost is {cost}")

        elif change == 4:
            end_time = input("pleas enter the new end_time: ")
            cost_matrix["sadr"]["end_time"] = end_time
            logging.basicConfig(filename="metro.log", level=logging.INFO)
            logging.info(f"the manager change the end_time trip 4 on the time: {now}, and new end_time is {end_time}")

        else:
            print("your chose is wrong...")
#================================================================================
def chose_1():
        while True:
            id=int(input("pleas enter your ID: "))
            password=input("pleas enter your password bank: ")
            request=User.check(id,password)
            if request == False:
                print("wrong")
                time.sleep(2)
                deletpage()
                x= input("if you want to try again enter the 1\nif you want the register enter 2: ")
                if x == "1":
                    continue
                elif x == "2":
                    time.sleep(1)
                    deletpage()
                    id = int(len(User.list_user)+1000)
                    name = input("pleas enter your name: ")
                    password=input("pleas enter the password: ")
                    ml=input("if male = m\nif fmale = f: ")
                    #pickle the users
                    string = f"your id{id}, your name{name}, your password{password}"
                    pickled = pickle.dumps(string)
                    file = open("users.pk", "ab")
                    file.write(pickled)
                    file.close()
                    #===========================================
                    if ml.startswith("m"):
                        gender=True
                    else:
                        gender=False
                    x=User(id,name,password,gender)

                    print(f"you are register your id is {id}")
                    logging.basicConfig(filename="metro.log", level=logging.INFO)
                    logging.info(f"the user login width password {password} and id {id}: at time {now}")
                    return x
                else:
                    return False
            else:return request


def chose_2():
        if len(User.list_user) == 0:
            print("your not login pleas first login and try again...")
            logging.basicConfig(filename="metro.log", level=logging.INFO)
            logging.info("The user could not access her bank account because she was not logged in")
            time.sleep(2)
            deletpage()
            check_login()
            time.sleep(2)
            deletpage()
            bank_sistm()

        else:
            bank_sistm()

card_list = []  
def chose_3():
        amount_single = 0
        balance_credit = 0
        balance_time = 0
        cost = 3500
        if len(card_list) == 0:
            balance = int(input("pleas enter the balance: "))
            password_bank = int(input("pleas enter the bank password: "))
            deletpage()
            print("1)single\n2)credit\n3)time_credit")
            chose_card = input("pleas chose the card: ")
            deletpage()
            if chose_card == "1":
                password = int(input("pleas enter the bank password: "))
                if password == password_bank:
                    balance -= 3500
                    amount_single += 3500
                    print(colored("account balance has been update: ","red"),balance)
                    card_list.append("single card")
                    logging.basicConfig(filename="metro.log", level=logging.INFO)
                    logging.info(f"The user bought a single card on the: {now}")
                    time.sleep(3)
                    deletpage()

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
                if password == password_bank:
                    balance -= money_card
                    balance_credit += money_card
                    print(colored("account balance has been update: ","red"),balance)
                    print(colored("your balance card is: ", "blue"), balance_credit)
                    string = f"you have credit card and balance is {balance_credit}"
                    card_list.append(string)
                    logging.basicConfig(filename="metro.log", level=logging.INFO)
                    logging.info(f"The user bought a credit card width balance {balance_credit} on the: {now}")
                    time.sleep(3)
                    deletpage()

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
                if password == password_bank:
                    current_day = datetime.now()
                    expiration_date = 2044
                    balance -= money_card
                    balance_time += money_card
                    print(colored("account balance has been update: ","red"),balance)
                    print(colored("your balance card is: ", "blue"), balance_time)
                    print("your expiration catd is: ", expiration_date)
                    string = f"you have credit_time card and balance is {balance_credit} and expiratipn is {expiration_date}"
                    card_list.append(string)
                    logging.basicConfig(filename="metro.log", level=logging.INFO)
                    logging.info(f"The user bought a credit_time card width balance {balance_credit} and expiration {expiration_date} on the: {now}")
                    time.sleep(3)
                    deletpage()

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
            for i in card_list:
                print(f"you have a {i}")
                time.sleep(2)
                deletpage()
            for i in cost_matrix.items():
                print(i) 
            trip_chose = input("1)gholhak to bime\n2)azadi to gholhak\n3)vardavard to aslamshahr\n4)sadr to pasdaran\npleas chose your trip: ")
            deletpage()
            