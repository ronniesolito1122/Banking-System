class bankSystem:
    def __init__(self):
        self.acc = {}

    def accCreation(self, acc, pin):
        self.acc[acc] = {pin : 0}


    def login(self,acc):
        for x in range(3):
            pin = input("enter pin: ")
            check = pin_checkerLog(pin)

            while check == False:
                pin = input("try again: ")
                check = pin_checkerLog(pin)

            if pin in self.acc[acc]:
                print("currently in working on the functions")
                user = input("enter anything to continue: ")
                return
            
            elif x == 3:
                print("you have exided the maximum retries")
                return
            else:
                print("Your pin code is incorrect ")



def acc_checkerCre(acc):
  for char in acc:
      if char.isalpha():
          print("acc shouldn't contain any letters")
          return False
      
  if len(acc) != 8:
      print("must be 8 digits")
      return False

  if acc in banksystem.acc:
      print("acc is already existed in the system")
      return False

  return True



def pin_checkerCre(pin):
  for char in pin:
      if char.isalpha():
          print("pin shouldn't contain any letters")
          return False
      
  if len(pin) != 4:
      print("must be 4 digits")
      return False

  return True



def acc_checkerLog(acc):
  if len(acc) != 8:
      print("must be 8 digits")
      return False

  for char in acc:
      if char.isalpha():
          print("acc shouldn't contain any letters")
          return False
      
  if acc not in banksystem.acc:
      print("acc does not exists in the system")
      return False

  return True



def pin_checkerLog(pin):
  if len(pin) != 4:
      print("must be 4 digits")
      return False

  for char in pin:
      if char.isalpha():
          print("pin shouldn't contain any letters")
          return False
  
  return True



banksystem = bankSystem()


def main():
    while True:
        print("---------JRE2 Bank System welcome---------")
        try:
            user = int(input("1. create acount \n2. login \n3. exit\nyour action: "))

            if user == 1:
                acc = input("enter your acc: ")
                check = acc_checkerCre(acc)

                while check == False:
                    acc = input("try again: ")
                    check = acc_checkerCre(acc)

                pin = input("enter your pin: ")
                check = pin_checkerCre(pin)

                while check == False:
                    pin = input("try again: ")
                    check = pin_checkerCre(pin)

                banksystem.accCreation(acc,pin)

            elif user == 2:
                acc = input("enter your account: ")
                check = acc_checkerLog(acc)

                while check == False:   
                    acc = input("try again: ")
                    check = acc_checkerLog(acc)

                banksystem.login(acc)

            elif user == 3:
                print("bye bye")
                break

            else:
                print("Input is not on the list try again: ")

        except ValueError:
            print("Must be interger")
main()