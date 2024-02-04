from trip import *
from os import system, name
import time

def delet_page():
        if name == "nt":
            system("cls")
        else:
            system("clear")


def delet_trip():
    for i in cost_matrix.items():
            print(i)


    print("You have 10 seconds to choose your trip")
    time.sleep(10)
    delet_page()


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

delet_trip()