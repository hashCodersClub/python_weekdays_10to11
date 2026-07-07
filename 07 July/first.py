class Human:
    def __init__(self,name,age):
        self.name = name 
        self.age = age

class Account(Human):
    def __init__(self,name,age,password,acc_no):
        self.__password = password
        self.__balance = 0
        self.acc_no = acc_no
    
    def update_password(self,acc_no,new_password):
        if self.acc_no ==acc_no:
            self.__password = new_password
        
    def show_password(self,acc_no):
        if self.acc_no ==acc_no:
            print(self.__password)

            # show_balance
            # deposite
            # widthrawal

class Trainer(Human):
    def __init__(self,name,age):
        Human.__init__(self,name,age)
        self.trainer_id = 1

gaurav = Account("Gaurav",10,12345,12345678)
tr = Trainer("Hasib",555)
print("name" in dir(tr))
