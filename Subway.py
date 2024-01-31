import sys
import datetime
class MetroCard:
    def __init__(self ,card_type ,credit=0 ,expiration_date=None):
        self.card_type=card_type
        self.credit=credit
        self.expiration_date=expiration_date
    
    def deduct_credit(self,amount):
        self.credit=amount
    
    def is_expired(self,current_date):
        if self.expiration_date is None:
            return False
        return current_date > self.expiration_date
    


class BankAccount:
    def __init__(self,account_number, balance=0):
        self.account_number=account_number
        self.balance=balance
    def deposit(self,amount):
        self.balance += amount
    
    def withdraw(self,amount):
        if self.balance >= amount
            return True
        else:
            False

class User:
    def __init__(self, unique_id ,fullname ,password):
        self.unique_id=unique_id
        self.fullname=fullname
        self.password=password
        self.metro_card=None
        self.bank_account=None

    def create_bank_account(self,account_number,balance=0):
        self.bank_account=BankAccount(account_number, balance)
    
    def register_trip(self,origin,destination,cost,start_time,end_time):
        if self.metro_card is None:
            return False
        if self.metro_card.cardtype == "single table":
            if self.metro_card.is_expired(datetime.now()):
                return False
            self.metro_card =None
                return True
        elif self.metro_card.card_type == "credit":
            if self.metro_card.credit < cost or self.metro_card.is_expired(datetime.now()):
                return False
            
            self.metro_card.deduct_credit(cost)
                return True
        elif self.metro_card.card_type == "credit / time":
            if self.metro_card.credit < cost or self.metro_card.is_expired(datetime.now():)
                return False
            self.metro_card.deduct_credit(cost)
                return True
        
    
    def pay_for_metro_card(self,amount):
       if self.bank_account is None:
            return False
       
       if self.bank_accounta.withdraw(amount):
           return True
       else:
           return False



        if sys.argv[1] == "createsuperuser":
           print("enter fullname:")
           fullname = input()
           print("enter password:")
           password=input()
           commit
           


            
    

  
       