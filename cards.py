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
                logging.basicConfig(filename="metro.log", level=logging.INFO)
                logging.info("The single card was selected and the amount of 3500 Tomans was added to it")
                return True
            else:
                if amount < MetroCard.cost:
                    print("your amount is low")
                    return False
            
    
    def credit(self, balance):
        if self.card_type == "credit":
            balance += money
            if balance > MetroCard.cost:
                balance -= MetroCard.cost
                logging.basicConfig(filename="metro.log", level=logging.INFO)
                logging.info(f"The credit card was selected and the amount of {money} Tomans was added to it")
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
                    logging.basicConfig(filename="metro.log", level=logging.INFO)
                    logging.info(f"The time_credit card was selected Its expiration date {expiration_date} and the amount of {money} Tomans was added to it")
                    return True
            else:
                return False
            
    
    def pickle_card(self):
        pickled = pickle.dumps(self)
        file = open("card.pk", "ab")
        file.write(pickled)
        file.close()
        logging.basicConfig(filename="metro.log", level=logging.INFO)
        logging.info("the card is pickle")

MetroCard.pickle_card()

