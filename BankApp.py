

class Customer:
    #pass in  first last and social 
    #initialize self and variables self referse to the object inwhich the variable invoked
    def __init__(self,firstName, lastName, social):
        self.firstName = firstName 
        self.lastName = lastName 
        self.social = social 
    #set the name
    def setfirstName(self,firstName):
        self.firstName = firstName
    #set the last name
    def setlastName(self,lastName):
        self.lastName = lastName
    #when customer is created pass in string 
    def __str__(self):
        self.name = "{},{} (SSN:{})".format(self.firstName, self.lastName,self.social)
        return self.name 
        
#super class which is why object is there 
class BankAccount(object):
    from random import randint
    n = 10
    range_start = 10**(n-1)
    range_end = (10**n)-1
    accountNumber = randint(range_start, range_end)
    #initialze variables from customer and new variable balance
    def __init__(self, firstName, lastName, social, balance = 0):
        self.balance = balance 
        
    #set customer get from customer class 
    def setCustomer(self,customer,accountNumber):
        self.customer = customer
        self.accountNumber = accountNumber 
    #get customer 
    def getCustomer(self,customer,accountNumber):
        return self.customer, self.accountNumber
    #depoist method
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("insufficent funds")
        else:
            self.balance = self.balance - amount
        return self.balance

    def __str__(self):
        customer = "{} account number: {}, balance: ${}".format(self.customer,self.accountNumber,self.balance)
        return customer 
    
#checking account inherets from bank account class will get all methods from this class 
class CheckingAccount(BankAccount):
    #initialize in customer class(which includes its atributes) and balance 
    def __init__(self, customer, balance = 0):
        super().__init__(self, customer, balance)
        self.customer = customer
        self.balance = balance
      
        print("created")
        
    def annualInterest(self):
        excess = self.balance - 10000
        if excess > 0:
            interest = (excess * .02)
            self.balance = self.balance + interest
            return self.balance
        else:
            return self.balance
        
    
class SavingAccount(BankAccount):
    def __init__(self, customer, balance = 0):
        super().__init__(self, customer, balance)
        self.customer = customer
        self.balance = balance
        
        
    def applyAnnualInterest(self):
        interest = (self.balance * .05)
        self.balance = self.balance + interest
        return self.balance

    print("created")
    
def main():
    #create customer objects in the customer class 
    alin = Customer('Alin', 'Smith', '111-11-1111')
    mary = Customer('Mary', 'Lee', '222-22-2222')
    #create checking account object in the checking account 
    alinAccnt = CheckingAccount(alin)
    maryAccnt = SavingAccount(mary)
    
    alinAccnt.deposit(20000)
    print(alinAccnt)
    alinAccnt.withdraw(5000)
    print(alinAccnt)
    alinAccnt.annualInterest()
    print(alinAccnt)


    maryAccnt.deposit(10000)
    print(maryAccnt) 
    maryAccnt.withdraw(15000)
    print(maryAccnt)
    maryAccnt.applyAnnualInterest()
    print(maryAccnt) 

 
    
main()



