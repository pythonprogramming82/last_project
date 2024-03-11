from view import *


def enter():
    while True:
        print("1)login & register\n2)Bank account management\n3)Metro travel registration")
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

        else:
            print("your chose is wrong!pleas try again...")
            time.sleep(3)
            deletpage()


def enter2(user:User):
    print (f"hi{user.name}")
    while True:
        option = print("1)logout \n2)Bank account management\n3)Metro travel registration")
        choice = input("pleas enter the number your chose:")
        time.sleep(2)
        deletpage()

        if choice == "1":
            enter()

        elif choice == "2":
            chose_2()

        elif choice == "3":
            chose_3()

        else:
            print("your chose is wrong!pleas try again...")
            time.sleep(3)
            deletpage()
            

password_managment = [1244]
id_managment = [130012]
def managment():
    while True:
        print("1)travel managment\n2)new managment\n3)Continue as a user")
        chose_1 = input("pleas chose your aption: ")
        if chose_1 == "1":
            password = int(input("pleas enter your password managment: "))
            id = int(input("pleas enter your id managment: "))
            if password in password_managment and id in id_managment:
                logging.basicConfig(filename="metro.log", level=logging.INFO)
                logging.info(f"the manager logged into the system on the: {now}")
                #pickle the managers
                string = f"id manager is {id} and password is {password}"
                pickled = pickle.dumps(string)
                file = open("users.pk", "ab")
                file.write(pickled)
                file.close()
                #===========================================================
                chose = input("1)add a trip\n2)change trip\n3)delet trip\n4)show the cards\npleas chose a number: ")
                if chose == "1":
                    for i in cost_matrix.items():
                        print(i)
                    new_trip = dict(input("pleas enter your new trip: "))
                    cost_matrix.update(new_trip)
                    logging.basicConfig(filename="metro.log", level=logging.INFO)
                    logging.info(f"the manager add a trip {new_trip} to the list of trip on the time: {now}")

                elif chose == "2":
                    for i in cost_matrix.items():
                        print(i)
                    change_trip()
                
                elif chose == "3":
                    for i in cost_matrix.items():
                        print(i)
                    delet_trip()

                elif chose == "4":
                    #read the file 
                    file = open("cards.pk", "rb")
                    file = pickle.load(file)
                    print(file)

                else:
                    print("your chose is wrong...")
            
            else:
                print("your id and pssword is wrong...pleas try again.")
            
        elif chose_1 == "2":
            password_managment.append(int(input("pleas enter the password new managment: ")))
            id_managment.append(int(input("pleas enter the id new managment: ")))
            logging.basicConfig(filename="metro.log", level=logging.INFO)
            logging.info(f"add the nwe manager on the: {now}")
            time.sleep(3)

        elif chose_1 == "3":
            deletpage()
            enter()
        
        else:
            print("your chose is wrong...")

managment()