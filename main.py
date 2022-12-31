#~~~ IMPORT ~~~
import os
import time 
from getpass import getpass
from name import name1

#~~~ LISTS ~~~
list1 = 'Calculator' , 'Password-Make' , 'Datelist' , 'Mail-Send' 

#~~~ MAIN ~~~
#passwort1 = getpass("Password\n")
#if passwort1 == '2006':
while True:
     os.system('cls')
     print(f"hello {name1}")
     print("all tools")
     A1 = input(f"{list1}\n")
     A1 = A1.lower()
      if A1 == 'Calculator' or '1':
        #~~ a ~~
        os.system('cls')
        print("Calculator by AI")
        time.sleep(2)

      elif A1 == 'Password-Make' or '2':
        #~~ b ~~
        os.system('cls')
        print("Password-Make by AI")
        time.sleep(2)

      elif A1 == 'Datelist' or '3':
        #~~ c ~~
        os.system('cls')
        print("Datelist by AI")
        time.sleep(2)

      elif A1 == 'Mail-Send' or 'ms' or '4':
       #~~ d ~~
        os.system('cls')
        print("Mail-Send by AI")
        time.sleep(2)

      elif A1 == 'exit' or 'e':
        #~~ e ~~
        os.system('cls')
        print("Exit by AI")
        time.sleep(2)
        os.system('cls')
        exit()

      elif A1 == '5' or 'edit':
        #~~ f ~~
        os.system('cls')
        print("#")
        f1 = input("1)edit-name, 2)mail")
        if f1 == '1' or 'edit-name' or 'en':
            f2 = input("NEW Name")
            name2 = (f'name = {f2}')
            f = open('name.py', 'w')
            f.write(f"{name1}\n")
            f.close()
            time.sleep(2)

     else:
        os.system('cls')
        print("not found")
        time.sleep(2)
    

#elif passwort1 == 'e':
    #os.system('cls')
    #exit()

#else:
    #os.system('cls')
   # print("not found")