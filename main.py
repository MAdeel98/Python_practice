from pathlib import Path
import json
import random
import string
class Bank :
    data =[]
    database='data.json'

    try:
        if Path(database).exists():
            with open(database) as fs:
                data=json.loads(fs.read())
        
        else:
            print("file not found")       
    except Exception as e:
        print("Error in loading the data from the file : ",e)

    
    def createaccount():

        info ={
            "name" : input("enter the name :"),
            "age" : int(input("enter the age :")),
            "email" : input("enter the email :"),
            "Pin" : int(input("enter the four digit pin :")),
            "accountNo" : Bank.accountgen(),
            "BankBalance" : 0
        }
        if info['age']< 18 or info['Pin'] !=4:
            print("you are not eligible for creating the account")
        else:
            print("account created successfully")

        for i in info:
            print(f"{i}  : {info[i]}")
        print("plx note down your account number and pin for future use")
        
        Bank.data.append(json.dumps(info))
        Bank.update()

    def depositmoney():
        accNo=input("enter the account number :")
        pin=int(input("enter the pin :"))
        userdata=[i for i in Bank.data if i['accountNo']==accNo and i['Pin']==pin]
        print(userdata , type(userdata))
        if not userdata:
            print("invalid account number or pin")
        else:
            amount=int(input(" enter the amount to deposit :"))
            if amount<=0:
                print("invalid amount")
            else:
                userdata [0]['BankBalance']+=amount
                print(f"your amount {amount} is deposited successfully")
                Bank.update()
                return userdata[0]['BankBalance']
            
            
    def withdrawamount() :
        accNo=input("enter the account number :")
        pin=int(input("enter the pin :"))
        userdata=[i for i in Bank.data if i['accountNo']==accNo and i['Pin']==pin]
        print(userdata , type(userdata))
        if not userdata:
            print("invalid account number or pin")
        else:
            amount=int(input(" enter the amount to withdraw :"))
            if amount<=0:
                print("invalid amount")
            else:
                userdata [0]['BankBalance']-=amount
                print(f"your amount {amount} is withdrawn successfully")
                Bank.update()
                return userdata[0]['BankBalance']



    @staticmethod
    def update():
        with open(Bank.database,'w')as fs:
            fs.write(json.dumps(Bank.data))
    @staticmethod
    def accountgen():
        alpha=random.choices(string.ascii_letters,k=4)
        dig=random.choices(string.digits,k=3)
        specChar=random.choices("@#$%&*",k=2)
        id = alpha + dig + specChar
        random.shuffle(id)
        return "".join(id)











print("Press 1 to create an account : ")
print("press 2 for updating the acount :")
print("press 3 for deposit the amooiunt :")
print("press 4 for withdraw an amount : ")
print("press 5 for delete the account :")

choice = input("enter the choice :")

if choice =="1":
    Bank.createaccount()
if choice =="3":
    Bank.depositmoney()

if choice =="4":
    Bank.withdrawamount()


