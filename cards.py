

class MetroCard:
    cost = 3500
    def __init__(self ,card_type ,credit=0 ,expiration_date=None):
        self.card_type=card_type
        self.credit=credit
        self.expiration_date=expiration_date

    
    def deduct_credit(self, amount):
        if self.card_type == "single_table":
            amount += money
            if amount == MetroCard.cost:
                amount -= MetroCard.cost
                return True
            else:
                return False
            
    
    def credit(self, balance):
        if self.card_type == "credit":
            balance += money
            if balance > MetroCard.cost:
                balance -= MetroCard.cost
                return True
            else:
                return False
            
    
    def time_credit(self,current_date, balance):
        if self.card_type == "time-credit":
            if self.expiration_date < current_date:
                balance += money
                if balance > MetroCard.cost:
                    balance -= MetroCard.cost
                    return True
            else:
                return False