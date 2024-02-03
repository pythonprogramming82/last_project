from banksistem import *
import datetime
class MetroCard:
    cost = 3500
    def __init__(self ,card_type ,credit=0):
        self.card_type=card_type
        self.credit=credit

    
    def single(self, amount):
        if self.card_type == "single_table":
            amount += money
            if amount == MetroCard.cost:
                amount -= MetroCard.cost
                return True
            else:
                if amount < MetroCard.cost:
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