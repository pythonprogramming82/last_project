from termcolor import colored
import pickle

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


# #===========================(delettrip)==================================================


class User():
    list_user=[]

    def __init__(self,ID:int,name:str,password,gender:bool):
        self.ID=ID
        self.name= name
        self.password = password
        self.gender = gender
        User.list_user.append(self)

    def __str__(self):
        return self.ID
    
    
    @staticmethod
    def check(id,password):

        if len(User.list_user) == 0 :
            return False
        else:

            for x in User.list_user :

                if x.ID==id:
                    if x.password == password:

                        return x
                    else:

                        return False
                else:

                    return False



