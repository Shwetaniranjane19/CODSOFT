from anonymenu import menu,readvalues,addop,subop,mulop,divop,floordivop,modulodiv,Expop
while(True):
    menu()
    ch=int(input("enter ur choice:"))
    print("*"*50)
    match(ch):
        case 1:
            a,b=readvalues("Addition")
            res=addop(a,b)
            print("-"*50)
            print("sum of number({},{})={}".format(a,b,res))

        case 2:
            a,b=readvalues("Subtraction")
            res=subop(a,b)
            print("-"*50)
            print("Sub of number({},{})={}".format(a,b,res))

        case 3:
            a,b=readvalues("Multiplication")
            res=mulop(a,b)
            print("-"*50)
            print("Mul of number({},{})={}".format(a,b,res))

        case 4:
            a,b=readvalues("Division")
            res=divop(a,b)
            print("-"*50)
            print("Div of number({},{})={}".format(a,b,res))

        case 5:
            a,b=readvalues("Floor Division")
            res=floordivop(a,b)
            print("-"*50)
            print("Floor Div of number ({},{})={}".format(a,b,res))

        case 6:
            a,b=readvalues("modulo Division")
            res=modulodiv(a,b)
            print("-"*50)
            print("Modulo Div of number({},{})={}".format(a,b,res))

        case 7:
            a,b=float(input("enter power:")),float(input("enter base:"))
            res=Expop(a,b)
            print("-"*50)
            print("power of number ({},{})={}".format(a,b,res))

        case 8:
            print("thanks for using program")
        case _:
            print("exit")

