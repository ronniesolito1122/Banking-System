import time 
import sys
class account:
    def __init__(self,pin,balance):
        self.index = 0
        self.pin = pin 
        self.balance = balance
        self.history = [] 

class bank_system:
    def __init__(self):
        self.accounts = {}

    def add_account(self,acc,pin,balance):
        self.accounts[acc] = account(pin,balance)
    
    def transfer_money(self,acc1,acc2,amount):
        self.accounts[acc1].balance -= amount 
        self.accounts[acc2].balance += amount 
        self.accounts[acc1].history.append(f"Transaction {int(self.accounts[acc1].index)+1}: Transferred {amount} to {acc2}.") 
        self.accounts[acc2].history.append(f"Transaction {int(self.accounts[acc2].index)+1}: Received {amount} from {acc1}.")
        self.accounts[acc1].index +=1
        self.accounts[acc2].index +=1

bank_system = bank_system()
while True:
    print ("✦✧✦✧"*10)
    print(f"Welcome to Group 1's Banking System. \nPlease select a function")
    try:
        ans = str(input(f"0. Create an account \n1. Login \n2. Exit \nReponse:"))
        print("✦✧✦✧"*10)  
        if ans =="0":
            try:
                while True:
                    print("//Enter a letter to exit the program//")
                    acc = str(input("Please enter an 8 numbered account number: "))
                    if acc.isalpha():
                        raise ValueError
                        
                    elif len(acc) !=8:
                        print("Account number should range from 8 numbers. Please try again.")
                        continue 
                    elif int(acc)<0:
                        print("Invalid Response. Try again.")
                        continue
                    elif acc in bank_system.accounts:
                        print("Account Already exist.")
                        continue 
                    break
                while True:
                    pin = str(input("Please enter a 6 numbered pin: "))
                    if pin.isalpha():
                        raise ValueError
                    if int(pin)<0:
                        print("Invalid Response. Try again.")
                        continue
                    elif len(str(pin)) == 6:
                        while True:
                            con = str(input("Re-enter your pin: "))
                            if con.isalpha():
                            	raise ValueError
                            elif con == pin:
                                break
                            else:
                                print("PIN doesn't match.")
                                continue
                        break
                    print("Invalid PIN. Please enter a 6-digit PIN.")
                    continue
                while True:
                    balance = float(input("Enter the initial balance: "))
                    if balance <0:
                        print("Invalid Amount. Try again.")
                        continue
                    break
            except ValueError:
                print(f"Exiting",end="")
                for i in range(10):
                    sys.stdout.write(".")
                    sys.stdout.flush()
                    time.sleep(0.2)
                print()
                continue
            print(f"Creating account", end ="")
            for i in range(10):
                sys.stdout.write(".")
                sys.stdout.flush()
                time.sleep(0.2)
            print()
            bank_system.accounts[acc] = account(pin,balance)
            print("Account successfully created!")
        
        elif ans =="1":
            log_acc = str(input("Please enter your account number: "))
            if log_acc.isalpha():
            	raise ValueError	
            print(f"Looking for {log_acc}", end ="")
            for i in range(10):
                sys.stdout.write(".")
                sys.stdout.flush()
                time.sleep(0.2)
            print()
            if log_acc in bank_system.accounts:
                log_pin = str(input("Enter your PIN: "))
                print(f"Checking", end = "")
                for i in range(10):
                    sys.stdout.write(".")
                    sys.stdout.flush()
                    time.sleep(0.2)
                print()
                if log_pin.isalpha():
                            	raise ValueError
                if (bank_system.accounts[log_acc].pin == log_pin):
                    print("SUCCESSFULLY LOGGED IN!")
                    
                    while True:
                        print("Please select a function:")
                        log_ans = int(input(f"0.Deposit \n1.Withdraw \n2.Check Balance \n3.Transfer Money \n4.View Transaction History \n5.Log Out \nResponse: "))

                        if log_ans == 0:
                            print (f"\ncurrently working on the process")
                            user=input("enter anything to continue: ")
                            
                        elif log_ans == 1: 
                            print (f"\ncurrently working on the process")
                            user=input("enter anything to continue: ")

                        elif log_ans == 2: 
                            print (f"\ncurrently working on the process")
                            user=input("enter anything to continue: ")

                        elif log_ans ==3:
                            log_acc2 = str(input("Enter the recipient's account: "))
                            print(f"Verifying the account",end="")
                            for i in range(10):
                                sys.stdout.write(".")
                                sys.stdout.flush()
                                time.sleep(0.2)
                            print()
                            if log_acc2.isalpha():
                            	raise ValueError
                            if log_acc2 == log_acc:
                                print("Invalid Action.")
                                continue
                            if log_acc2 in bank_system.accounts:
                                transfer = float(input(f"Enter amount to transfer to {log_acc2}: "))
                                print(f"Checking balance",end="")
                                for i in range(10):
                                    sys.stdout.write(".")
                                    sys.stdout.flush()
                                    time.sleep(0.2)
                                print()
                                
                                if transfer > bank_system.accounts[log_acc].balance:
                                    print(f"Insufficient balance for transfer. You only have ₱{bank_system.accounts[log_acc].balance}.")
                                    continue 
                                
                                elif transfer <0:
                                    print("Invalid Amount.")
                                    continue
                                bank_system.transfer_money(log_acc,log_acc2,transfer)
                                print("Transaction Complete!")
                            else:
                                print(f"No {log_acc2} found.")

                        elif log_ans ==4:
                            print(f"Retrieving History",end="")
                            for i in range(10):
                                sys.stdout.write(".")
                                sys.stdout.flush()
                                time.sleep(0.2)
                            print()
                            print("History: ")
                            if not bank_system.accounts[log_acc].history:
                                print("No Transactions made yet.")
                                continue
                            for history in bank_system.accounts[log_acc].history:
                                print(history)
                        
                        elif log_ans ==5:
                            print(f"Logging out",end="")
                            for i in range(10):
                                sys.stdout.write(".")
                                sys.stdout.flush()
                                time.sleep(0.2)
                            print()
                            break
                else:
                    print("Incorrect PIN.")
            else:
                print(f"No {log_acc} found.")

        elif ans =="2":
            print("Thank you for using our System. Bye ^_^.")
            break
        else:
            print("Invalid Response.")
    except ValueError:
        print("Invalid answer.")
        continue