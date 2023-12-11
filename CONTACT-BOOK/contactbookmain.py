from contactbookmenu import menu
from contactbookopration import insertcontact,viewcotact,searchcontact,updatecontact,deletecontact

while(True):
  menu()
  ch=int(input("enter ur choice:"))
  match(ch):
        case 1:
            print("======================")
            print("Add new contact")
            print("======================")
            insertcontact()
        case 2:
            print("======================")
            print("view all contact")
            print("=======================")
            viewcotact()
        case 3:
            print("======================")
            print("view search contact")
            print("=======================")
            searchcontact()
        case 4:
            print("======================")
            print("update contact")
            print("======================")
            updatecontact()
        case 5:
            print("=======================")
            print("delete contact")
            print("=======================")
            deletecontact()
        case 6:
            print("thanks for using program")
            break
        case _:
            print("exist")

