class Account:
    def __init__(self,title=None,balance=0):
          self.title=title
          self.balance=balance
    def Account(self,title,balance):
           self.title=title
           self.balance=balance
    def Account_details(self):
              return (f'The title is: {self.title}\nThe balance amount is: {self.balance}')
class SavingsAccount():
     def __init__(self,title,balance,interestrate):
            self.title=title
            self.balance=balance
            self.interestrate=interestrate
     def Savings_Account_Details(self):
          return (f'The title is: {self.title}\nThe balance amount is: {self.balance}\nThe interest rate is: {self.interestrate}')
Account1=Account("Ashish",5000)
Account2=SavingsAccount("Ashish",5000,5)
print(Account1.Account_details())
print(Account2.Savings_Account_Details())