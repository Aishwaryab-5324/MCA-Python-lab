class Customer:
    def getdata(self,name,acno,actype,balance):
        self.name=name
        self.acno=acno
        self.actype=actype
        self.balance=balance
    def displayCustomer(self):
        print("Customer Name:",self.name)
        print("Account Number:",self.acno)
        print("Account Type:",self.actype)
        print("Balance Amount:",self.balance)
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(self.balance,".Rs Successully Deposited")
    def withdrawal(self,amount):
        if self.balance<amount:print("Insuficient Balance")
        else: self.balance=self.balance-amount

#main program
ch=0
while ch!=5:
    print("1.New Customer")
    print("2.Deposit")
    print("3.Withdrawal")
    print("4.Display")
    print("5.Exit")
    ch=int(input("enter your choice"))
    if ch==1:
        obj=Customer()
        n=input("Enter name:")
        no=int(input("Enter Account Number:"))
        t=input("Enter Account Type(SB/C):")
        b=int(input("Enter the Amount:"))
        obj.getdata(n,no,t,b)
    if ch==2:
        b=int(input("Enter the amount to be dposited:"))
        obj.deposit(b)
    if ch==3:
        b=int(input("enter he amount to be withdrawal:"))
        obj.withdrawal(b)
    if ch==4:
        obj.displayCustomer()
    else:print("program terminated")
    
