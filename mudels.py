from termcolor import colored
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
    "a": {"b": "tehran", "cost":5000, "star_time":10, "end_time":11},
    "b": {"a": "karaj", "cost": 10000, "star_time":10.30, "end_time":11.10},
    "c": {"b": "aslamshahr", "cost": 8000, "star_time":11, "end_time":11.30},
    "d": {"a": "pasdaran", "cost": 20000, "star_time":11.10, "end_time":12},
}

#===========================(changetrip)====================================================
class ChangeTrip():
    def change_trip():
        trip_chose = input("1)a to b\n2)b to a\n3)c to b\n4)d to a\npleas chose your trip: ")
        if trip_chose == "1":
            print("1)origin\n2)destination\n3)cost\n4)end_time")
            change = int(input("Which part of the trip do you want to change: "))
            if change == 1:
                origin = input("pleas enter the new origin: ")
                cost_matrix["a"] = origin

            elif change == 2:
                destination = input("pleas enter the new destination: ")
                cost_matrix["a"]["b"] = destination

            elif change == 3:
                cost = int(input("pleas enter the new cost: "))
                cost_matrix["a"]["cost"] = cost

            elif change == 4:
                end_time = input("pleas enter the new end_time: ")
                cost_matrix["a"]["end_time"] = end_time

            else:
                print("your chose is wrong...")


        elif trip_chose == "2":
            print("1)origin\n2)destination\n3)cost\n4)end_time")
            change = int(input("Which part of the trip do you want to change: "))
            if change == 1:
                origin = input("pleas enter the new origin: ")
                cost_matrix["b"] = origin

            elif change == 2:
                destination = input("pleas enter the new destination: ")
                cost_matrix["b"]["a"] = destination

            elif change == 3:
                cost = int(input("pleas enter the new cost: "))
                cost_matrix["b"]["cost"] = cost

            elif change == 4:
                end_time = input("pleas enter the new end_time: ")
                cost_matrix["b"]["end_time"] = end_time

            else:
                print("your chose is wrong...")


        elif trip_chose == "3":
            print("1)origin\n2)destination\n3)cost\n4)end_time")
            change = int(input("Which part of the trip do you want to change: "))
            if change == 1:
                origin = input("pleas enter the new origin: ")
                cost_matrix["c"] = origin

            elif change == 2:
                destination = input("pleas enter the new destination: ")
                cost_matrix["c"]["b"] = destination

            elif change == 3:
                cost = int(input("pleas enter the new cost: "))
                cost_matrix["c"]["cost"] = cost

            elif change == 4:
                end_time = input("pleas enter the new end_time: ")
                cost_matrix["c"]["end_time"] = end_time

            else:
                print("your chose is wrong...")

        elif trip_chose == "4":
            print("1)origin\n2)destination\n3)cost\n4)end_time")
            change = int(input("Which part of the trip do you want to change: "))
            if change == 1:
                origin = input("pleas enter the new origin: ")
                cost_matrix["d"] = origin

            elif change == 2:
                destination = input("pleas enter the new destination: ")
                cost_matrix["d"]["a"] = destination

            elif change == 3:
                cost = int(input("pleas enter the new cost: "))
                cost_matrix["d"][""] = cost

            elif change == 4:
                end_time = input("pleas enter the new end_time: ")
                cost_matrix["d"]["end_time"] = end_time

            else:
                print("your chose is wrong...")

# #===========================(delettrip)==================================================
class DeletTrip():
    def delet_trip():
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



