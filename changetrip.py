from trip import *


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
