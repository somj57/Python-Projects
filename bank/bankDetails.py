class bank():
    def __init__(self):
        print("Bank Account Created")
        
    def _setDetails(self,BankName,Name,Id,Ac,Balance):
        self.BankName = BankName
        self.Name = Name
        self.Id = Id
        self.Ac = Ac
        self.Balance = Balance
        print("Bank data Initlized📈")

    def printDetails(self):
        print(f'Customer Name : {self.Name}\nBank : {self.BankName}\nID : {self.Id}\nAccNo : {self.Ac}\nBalance : {self.Balance}')
