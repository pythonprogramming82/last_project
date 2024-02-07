from cards import *
from deletetrip import *
from changetrip import change_trip
class Manager():
    def __init__(self, manager_id, fullname, password):
        self.manager_id = manager_id
        self.fullname = fullname
        self.password = password


    def delet_trip(self, manager_id, password):
        password_manager = 1234
        manager = 320012
        if manager_id == manager and password == password_manager:
            delet_trip()
            logging.basicConfig(filename="metro.log", level=logging.INFO)
            logging.info("trip a delet")


    def change_trip(self, manager_id, password):
        password_manager = 1234
        manager = 320012
        if manager_id == manager and password == password_manager:
            change_trip()
            logging.basicConfig(filename="metro.log", level=logging.INFO)
            logging.info("the trip change")
            
    
    def add_trip(self, manager_id, password):
        password_manager = 1234
        manager = 320012
        if manager_id == manager and password == password_manager:
            new_trip = dict(input("pleas enter your new trip: "))
            cost_matrix.update(new_trip)
            logging.basicConfig(filename="metro.log", level=logging.INFO)
            logging.info("a new trip add trips")
    

    def pickle_txt(self):
        pickled = pickle.dumps(self)
        file = open("users.pk", "ab")
        file.write(pickled)
        file.close()
        logging.basicConfig(filename="metro.log", level=logging.INFO)
        logging.info("trip information is pickle")


    def unpickle(file):
        with open("users.pk", "rb") as file:
            file = pickle.loads(file)
            file.read()
            file.close()
            logging.basicConfig(filename="metro.log", level=logging.INFO)
            logging.info("cards is unpickle")
