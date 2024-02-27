from view import *
def enter():
    while True:
        option = print("1)login & register\n2)Bank account management\n3)Metro travel registration\n4)Management")
        choice = input("pleas enter the number your chose:")
        time.sleep(2)
        deletpage()

        if choice == "1":
            back=chose_1()
            if back==False:
                print("wrong")
                continue
            else:
                enter2(back)

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


def enter2(user:User):
    print (f"hi{user.name}")
    while True:
        option = print("1)logout \n2)Bank account management\n3)Metro travel registration\n4)Management")
        choice = input("pleas enter the number your chose:")
        time.sleep(2)
        deletpage()

        if choice == "1":
            enter()

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


enter()