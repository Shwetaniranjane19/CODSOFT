import mysql.connector

def insertcontact():

  while(True):
    try:
        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="root",
                                    database="4pmbatch")
        cur=con.cursor()
        name=input("enter name for inserting record:")
        pno=int(input("enter phone number for inserting record :"))
        email=input("enter email address for inserting record:")
        Address=input("enter Address for inserting record:")
        cur.execute("insert into contactbook values('%s',%d,'%s','%s')"%(name,pno,email,Address))
        con.commit()
        print("contact detail inserted successfully")
        print("----------------------------------------------------")
        ch=input("do u have another record inserted (yes/no) :")
        if(ch.lower()=="no"):
            break
        print("-----------------------------------------------------")

    except mysql.connector.DatabaseError as db:
        print("problem in mysql",db)


def viewcotact():
    try:
        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="root",
                                    database="4pmbatch")
        cur=con.cursor()
        cur.execute("select * from contactbook")
        for colname in [metadata[0] for metadata in cur.description]:
            print(colname,end=" ")
        print()
        #code for getting records
        records=cur.fetchall()
        for record in records:
            for val in record:
                print(val,end=" ")
            print()
        print("------------------------------------------")
        print("contact View successfully")
    except mysql.connector.DatabaseError as db:
        print("problem in mysql",db)


def searchcontact():
  while(True):
    try:
        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="root",
                                    database="4pmbatch")
        cur=con.cursor()
        cur.execute("select * from contactbook")
        op = int(input("enter number for searching record:"))
        for colname in [metadata[0] for metadata in cur.description]:
            print(colname,end=" ")
        print()
        records=cur.fetchmany(op)
        for record in records:
            for val in record:
                print(val,end=" ")
            print()
        print("---------------------------------------")
        ch=input("do u have search another contact (yes/no):")
        if(ch.lower()=="no"):
            break
        print("=================================")
    except mysql.connector.DatabaseError as db:
        print("program in mysql",db)



def updatecontact():
    while True:
        try:
            con = mysql.connector.connect(host="localhost",
                                          user="root",
                                          passwd="root",
                                          database="4pmbatch")
            cur = con.cursor()

            name = input("Enter name for updating records: ")
            pno = int(input("Enter phone number for updating records: "))
            email = input("Enter email Id for updating records: ")
            Address = input("Enter Address for updating records: ")

            cur.execute("UPDATE contactbook SET Pno=%s, email=%s, Address=%s WHERE name=%s", (pno, email, Address, name))
            con.commit()

            print("Successful")
            ch = input("Do you want to update another record (yes/no): ")
            if ch.lower() == "no":
                break
            print("====================================")
        except mysql.connector.DatabaseError as db:
            print("Problem in MySQL:", db)



def deletecontact():
  while(True):
    try:
        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="root",
                                    database="4pmbatch")
        cur=con.cursor()
        name=input("enter name for delete record:")
        cur.execute("delete from contactbook where name='%s'"%name)
        con.commit()
        if(cur.rowcount>0):
            print("record delete successfully")
        else:
            print("record does not exist")
        ch=input("do u want to another record delete (yes/no):")
        if(ch.lower()=="no"):
            break
        print("============================================")
    except mysql.connector.DatabaseError as db:
        print("problem in mysql",db)
