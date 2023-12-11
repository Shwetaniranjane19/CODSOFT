def menu():
    print("="*50)
    print("------Arithmetic Operation Calculator-------")
    print("="*50)
    print("\t1.Addition")
    print("\t2.subtraction")
    print("\t3.Multiplication")
    print("\t4.Division")
    print("\t5.Floor Division")
    print("\t6.Modulo Division")
    print("\t7.Exponentiation")
    print("\t8.exit")
    print("*"*50)

def readvalues(op):
    print("enter two value for {}".format(op))
    a,b=float(input("enter value of a:")),float(input("enter value of b:"))
    return a,b

addop=lambda a,b:a+b
subop=lambda a,b:a-b
mulop=lambda a,b:a*b
divop=lambda a,b:a/b
floordivop=lambda a,b:a//b
modulodiv=lambda a,b:a%b
Expop=lambda a,b:a**b


