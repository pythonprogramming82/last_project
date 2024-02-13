import time
from view import *

while True:
    option = print("1)login\n2)Bank account management\n3)Metro travel registration\n4)Management")
    choice = input("pleas enter the number your chose:")
    time.sleep(2)
    deletpage()

    if choice == "1":
        chose_1()

    elif choice == "2":
        chose_2()

    elif choice == "3":
        chose_3()

    elif choice == "4":
        chose_4()

    else:
        print("your chose is wrong!pleas try again...")
        time.sleep(3)
        deletpage()
