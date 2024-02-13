from termcolor import colored
import pickle
import datetime
#===========================(banksistem)======================================
class User:
    def __init__(self, ID, name, age, gender):
        self.ID = ID
        self.name = name
        self.age = age
        self.gender = gender
        

    def show(self):
        return f"name is: {self.name} age is: {self.age} and gender is: {self.gender}"
    

    def pickle_txt(self):
        pickled = pickle.dumps(self)
        file = open("users.pk", "ab")
        file.write(pickled)
        file.close()



class Bank():
    def __init__(self, ID, balance, password):
        self.ID = ID
        self.balance = balance
        self.password = password

    
    def money_out(self, password):
        money = int(input("pleas enter the money: "))
        if password == self.password:
            if money > self.balance:
                print(colored("insufficient funds => your balance is: ","blue"),self.balance)

            
            else:
                self.balance -= money
                print(colored("account balance has been update: ","red"),self.balance)


        else:
            print(colored("your password is wrong...","yellow"))

    
    def show_balance(self, password):
        bank_password = 3345
        if password == bank_password:
            print(colored("account balance is: ","green"),self.balance)


        else:
            print(colored("youe password is wrong...","yellow"))

#==========================(cards)==============================================
class MetroCard:
    cost = 3500
    def __init__(self ,card_type ,credit=0):
        self.card_type=card_type
        self.credit=credit

    
    def single(self, amount):
        if self.card_type == "single_table":
            if amount == MetroCard.cost:
                amount -= MetroCard.cost
                return True
            else:
                if amount < MetroCard.cost:
                    print("your amount is low")
                    return False
            
    
    def credit(self, balance):
        if self.card_type == "credit":
            balance += money
            if balance > MetroCard.cost:
                balance -= MetroCard.cost
                return True
            else:
                return False
            
    
    def time_credit(self, balance):
        current_date = datetime.now()
        expiration_date = 2044
        if self.card_type == "time-credit":
            if expiration_date < current_date:
                balance += money
                if balance > MetroCard.cost:
                    balance -= MetroCard.cost
                    return True
            else:
                return False
            
    
    def pickle_card(self):
        pickled = pickle.dumps(self)
        file = open("card.pk", "ab")
        file.write(pickled)
        file.close()

#==============================(trip)=======================================
class Trip:
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination
        self.end_time = None
        self.cost = None

    def calculate_cost(self, cost_matrix):
        if self.origin in cost_matrix and self.destination in cost_matrix[self.origin]:
            self.cost = cost_matrix[self.origin][self.destination]
        else:
            raise ValueError(f"No cost found for the trip from {self.origin} to {self.destination}")

    def deactivate(self, end_time):
        self.end_time = end_time


cost_matrix = {
    "a": {"b": 5000, "star_time":10, "end_time":11},
    "b": {"a": 10000, "star_time":10.30, "end_time":11.10},
    "c": {"b": 8000, "star_time":11, "end_time":11.30},
    "d": {"a":20000, "star_time":11.10, "end_time":12},
}

#===========================(changetrip)====================================================
class ChangeTrip():
    def change_trip():
        for i in cost_matrix.items():
                print(i)

        print("================================================")

        trip_chose = input("1)a to b\n2)b to a\n3)c to b\n4)d to a\npleas chose your trip: ")

        print("================================================")

        if trip_chose == "1":
            change = input("1)origin\n2)destination\n3)cost\n4)end_time\nWhich part of the trip do you want to change: ")
            if change == "1":
                origin = input("pleas enter the new origin: ")
                cost_matrix["a"] = origin

            elif change == "2":
                destination = input("pleas enter the new destination: ")
                cost_matrix["a"]["b"] = destination

            elif change == "3":
                cost = int(input("pleas enter the new cost: "))
                cost_matrix["a"]["cost"] = cost

            elif change == "4":
                end_time = input("pleas enter the new end_time: ")
                cost_matrix["a"]["end_time"] = end_time

            else:
                print("your chose is wrong...")


        elif trip_chose == "2":
            if change == "1":
                origin = input("pleas enter the new origin: ")
                cost_matrix["b"] = origin

            elif change == "2":
                destination = input("pleas enter the new destination: ")
                cost_matrix["b"]["a"] = destination

            elif change == "3":
                cost = int(input("pleas enter the new cost: "))
                cost_matrix["b"]["cost"] = cost

            elif change == "4":
                end_time = input("pleas enter the new end_time: ")
                cost_matrix["b"]["end_time"] = end_time

            else:
                print("your chose is wrong...")


        elif trip_chose == "3":
            if change == "1":
                origin = input("pleas enter the new origin: ")
                cost_matrix["c"] = origin

            elif change == "2":
                destination = input("pleas enter the new destination: ")
                cost_matrix["c"]["b"] = destination

            elif change == "3":
                cost = int(input("pleas enter the new cost: "))
                cost_matrix["c"]["cost"] = cost

            elif change == "4":
                end_time = input("pleas enter the new end_time: ")
                cost_matrix["c"]["end_time"] = end_time

            else:
                print("your chose is wrong...")

        elif trip_chose == "4":
            if change == "1":
                origin = input("pleas enter the new origin: ")
                cost_matrix["d"] = origin

            elif change == "2":
                destination = input("pleas enter the new destination: ")
                cost_matrix["d"]["a"] = destination

            elif change == "3":
                cost = int(input("pleas enter the new cost: "))
                cost_matrix["d"]["cost"] = cost

            elif change == "4":
                end_time = input("pleas enter the new end_time: ")
                cost_matrix["d"]["end_time"] = end_time

            else:
                print("your chose is wrong...")

#===========================(delettrip)==================================================
class DeletTrip():
    def delet_trip():
        for i in cost_matrix.items():
                print(i)


        print("You have 10 seconds to choose your trip")


        trip_chose = input("1)a to b\n2)b to a\n3)c to b\n4)d to a\npleas chose your trip: ")
        if trip_chose == "1":
            del cost_matrix["a"]

        elif trip_chose == "2":
            del cost_matrix["b"]

        elif trip_chose == "3":
            del cost_matrix["c"]

        elif trip_chose == "4":
            del cost_matrix["d"]

        else:
            print("your chose is wrong!pleas try again...")

#=============================(manager)=================================================
class Manager():
    def __init__(self, manager_id, fullname, password):
        self.manager_id = manager_id
        self.fullname = fullname
        self.password = password


    def delet_trip(self, manager_id, password):
        password_manager = 1234
        manager = 320012
        if manager_id == manager and password == password_manager:
            DeletTrip.delet_trip()


    def change_trip(self, manager_id, password):
        password_manager = 1234
        manager = 320012
        if manager_id == manager and password == password_manager:
            ChangeTrip.change_trip()

            
    
    def add_trip(self, manager_id, password):
        password_manager = 1234
        manager = 320012
        if manager_id == manager and password == password_manager:
            new_trip = dict(input("pleas enter your new trip: "))
            cost_matrix.update(new_trip)

    

    def pickle_txt(self):
        pickled = pickle.dumps(self)
        file = open("users.pk", "ab")
        file.write(pickled)
        file.close()



    def unpickle(file):
        with open("users.pk", "rb") as file:
            file = pickle.loads(file)
            file.read()
            file.close()            

