import random
import datetime
import mysql.connector

b=input("user name:")
a=input("enter password for database:")
con=mysql.connector.connect(host="localhost",
                           password=a,
                           user=b)
if con.is_connected()==1:
    print("login succesfull")
cur=con.cursor()
try:
    cur.execute("create database hotel_try4")
    a=1
except:
    pass
if a==1:
    cur.execute("use hotel_try4")
    cur.execute("create table custom(customerid int(3) primary key,customername varchar(40),phoneno char(100),address varchar(100),aadharno int(20) unique,checkin char(13),checkout char(13),days_of_stay int(2),roomno int(20),room_type varchar(20),room_price int(20),extra int default 0)")
    cur.execute("create table me(item_no int(10) primary key,item_name varchar(40),price int(20))")
    l=[[1,"Regular Tea",20],[2,"Masala Tea",25],[3,"Coffee",25],[4,"Cold Drink",25],[5,"Bread Butter",30],[6,"Cheese Toast Sandwich",70],[7,"Tomato Soup",110],[8,"Hot & Sour",110],[9,"Veg. Munchow",110],[10,"Shahi Paneer",110],[11,"Kadai Paneer",110],[12,"Chilli Paneeer",140],[13,"Mix veg",140],[14,"Dal Fry",140],[15,"Dal Makhani",150],[16,"Plain Roti",15],[17,"Tandoori Roti",20],[18,"Plain Rice",90],[19,"Jeera Rice",90],[20,"Ice Cream",60]]
    for i in l:
        a,b,c=int(i[0]),i[1],int(i[2])
        cur.execute("insert into me values('{}','{}','{}')".format(a,b,c))
        con.commit()
    cur.execute("create table room_info(roomno int(20) primary key,customerid int(3) unique,room_type varchar(20),price int(3))")
    for i in range(1,21):
        if i<=5:
            a="STANDARD NON-AC"
            b=3500
            cur.execute("insert into room_info values('{}','{}','{}','{}')".format(300+i,100+i,a,b))
            con.commit()
        elif i>5 and i<=10:
            a="STANDARD AC"
            b=4000
            cur.execute("insert into room_info values('{}','{}','{}','{}')".format(300+i,100+i,a,b))
            con.commit()
        elif i>10 and i<=15:
            a="3 BED NON-AC"
            b=4000
            cur.execute("insert into room_info values('{}','{}','{}','{}')".format(300+i,100+i,a,b))
            con.commit()
        else:
            a="3 BED AC"
            b=4500
            cur.execute("insert into room_info values('{}','{}','{}','{}')".format(300+i,100+i,a,b))
            con.commit()
cur.execute("use hotel_try4")
 
# Global List Declaration
name = []
phno = []
add = []
aadhar=[]
checkin = []
checkout = []
room = []
price = []
rc = []
p = []
roomno = []
custid = []
day = []
i=0
# Home Function
def Home():
    
     
    print("\t\t\t\t\t\t WELCOME TO HOTEL ANCASA\n")
    print("\t\t\t 1 Booking\n")
    print("\t\t\t 2 Rooms Info\n")
    print("\t\t\t 3 Room Service(Menu Card)\n")
    print("\t\t\t 4 Payment\n")
    print("\t\t\t 5 Record\n")
    print("\t\t\t 0 Exit\n")
  
    ch=int(input("->"))
     
    if ch == 1:
        print(" ")
        Booking()
     
    elif ch == 2:
        print(" ")
        Rooms_Info()
     
    elif ch == 3:
        print(" ")
        restaurant()
     
    elif ch == 4:
        print(" ")
        Payment()
     
    elif ch == 5:
        print(" ")
        Record()
     
    else:
        exit()
 # program to check if date is correct
  
def date(c):
     
    if c[2] >= 2022 and c[2] <= 2023:
         
        if c[1] != 0 and c[1] <= 12:
             
            if c[1] == 2 and c[0] != 0 and c[0] <= 31:
                 
                if c[2]%4 == 0 and c[0] <= 29:
                    pass
                 
                elif c[0]<29:
                    pass
                 
                else:
                    print("Invalid date\n")
                
                    Booking()
             
             
            # if month is odd & less than equal
            # to 7th  month
            elif c[1] <= 7 and c[1]%2 != 0 and c[0] <= 31:
                pass
             
            # if month is even & less than equal to 7th
            # month and not 2nd month
            elif c[1] <= 7 and c[1]%2 == 0 and c[0] <= 30 and c[1] != 2:
                pass
             
            # if month is even & greater than equal
            # to 8th  month
            elif c[1] >= 8 and c[1]%2 == 0 and c[0] <= 31:
                pass
             
            # if month is odd & greater than equal
            # to 8th  month
            elif c[1]>=8 and c[1]%2!=0 and c[0]<=30: 
                pass
             
            else:
                print("Invalid date\n")
            
                Booking()
                 
        else:
            print("Invalid date\n")

            Booking()
             
    else:
        print("Invalid date\n")

        Booking()
  
  
# Booking function
def Booking():
     
        # used global keyword to
        # use global variable 'i'
    print(" BOOKING ROOMS")
    print(" ")
         
    while 1:
        name=str(input("Name: "))
        phno=str(input("Phone No.: "))
        add=str(input("Address: "))
        aadhar=int(input("enter aadhar no")) 
            # checks if any field is not empty
        if name!="" and phno!="" and add!="" and aadhar!="":
            cur.execute("select phoneno,aadharno from custom")
            r=cur.fetchall()
            for i in r:
                if i[0]==phno or i[1]==aadhar:
                    print("already exists")
                    ch=input("do you want to book another?y/n")
                    if ch=="y" or ch=="Y":
                        Booking()
                    else:
                        Home()    
            break
                 
        else:
             print("\tName, Phone no. & Address cannot be empty..!!")
              
    checkin=str(input("Check-In: "))
    cii=checkin.split('/')
    ci=cii
    ci[0]=int(ci[0])
    ci[1]=int(ci[1])
    ci[2]=int(ci[2])
    date(ci)
          
    checkout=str(input("Check-Out: "))
    coo=checkout.split('/')
    co=coo
    co[0]=int(co[0])
    co[1]=int(co[1])
    co[2]=int(co[2])
    date(co)
         
        # checks if check-out date falls after
        # check-in date
    if co[1]<ci[1] and co[2]<ci[2]:
             
        print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n")
        Booking()
    elif co[1]==ci[1] and co[2]>=ci[2] and co[0]<=ci[0]:
             
        print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n")
        Booking()
    else:
        pass
        d1 = datetime.datetime(ci[2],ci[1],ci[0])
        d2 = datetime.datetime(co[2],co[1],co[0])
        day = (d2-d1).days
        cur.execute("select distinct room_type,price from room_info")
        r=cur.fetchall()
          
    print("----SELECT ROOM TYPE----")
    for i in range( len(r)):
            print (i+1,r[i])
         
        
    cur.execute("select customerid from custom")
    b=cur.fetchall()
    d=[]
    while 1:
        ch=int(input("->"))
        if ch==1:
            cur.execute("select roomno,customerid from room_info where room_type='STANDARD NON-AC'")
            c=cur.fetchall()
            for i in c:
                f=0
                for j in b:
                    j=int(j[0])
                    if j==i[1]:
                        f+=1
                if f==0:
                    d.append(i)
            if len(d)==0:
                print("this room is not available please choose another")
                continue
            else:
                rr=random.choice(d)
                print("Room Type- Standard Non-AC")
                room="STANDARD NON-AC"
                price=3500
                print("Price- 3500")
                break
            
        elif ch==2:
            cur.execute("select roomno,customerid from room_info where room_type='STANDARD AC'")
            c=cur.fetchall()
            for i in c:
                f=0
                for j in b:
                    j=int(j[0])
                    if j==i[1]:
                        f+=1
                if f==0:
                    d.append(i)
            if len(d)==0:
                print("this room is not available please choose another")
                continue
            else:
                rr=random.choice(d)
                room='Standard AC'
                print("Room Type- Standard AC")
                price=4000
                print("Price- 4000")
                break
            
        elif ch==3:
            cur.execute("select roomno,customerid from room_info where room_type='3 BED NON-AC'")
            c=cur.fetchall()
            for i in c:
                f=0
                for j in b:
                    j=int(j[0])
                    if j==i[1]:
                        f+=1
                if f==0:
                    d.append(i)
            print(d)
            if len(d)==0:
                print("this room is not available please choose another")
                continue
            else:
                rr=random.choice(d)
                room='3 BED NON-AC'
                print("Room Type- 3-Bed Non-AC")
                price=4000
                print("Price- 4000")
                break
            
        elif ch==4:
            cur.execute("select roomno,customerid from room_info where room_type='3 BED AC'")
            c=cur.fetchall()
            for i in c:
                f=0
                for j in b:
                    j=int(j[0])
                    if j==i[1]:
                        f+=1
                if f==0:
                    d.append(i)
            if len(d)==0:
                print("this room is not available please choose another")
                continue
            else:
                rr=random.choice(d)
        
                room='3 BED AC'
                print("Room Type- 3-Bed AC")
                price=4500
                print("Price- 4500")
                break
        else:
            print(" Wrong choice..!!")
  

    print("")
        
    print("Room No. - ",rr[0])
    print("Customer Id - ",rr[1])
    extra=0
    cur.execute("insert into custom values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(rr[1],name,phno,add,aadhar,checkin,checkout,day,rr[0],room,price,extra))
    con.commit()

    print("\t\t\t***ROOM BOOKED SUCCESSFULLY***\n")

    n=int(input("0-BACK\n ->"))
    if n==0:
        Home()
    else:
        exit()

# ROOMS INFO
def Rooms_Info():
    print("         ------ HOTEL ROOMS INFO ------")
    print("")
    print("STANDARD NON-AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed, Television, Telephone,")
    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
    print("an attached washroom with hot/cold water.\n")
    print("STANDARD AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed, Television, Telephone,")
    print("Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and")
    print("an attached washroom with hot/cold water + Window/Split AC.\n")
    print("3-Bed NON-AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1")
    print("Side table, Balcony with an Accent table with 2 Chair and an")
    print("attached washroom with hot/cold water.\n")
    print("3-Bed AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, ")
    print("1 Side table, Balcony with an Accent table with 2 Chair and an")
    print("attached washroom with hot/cold water + Window/Split AC.\n\n")
    print()
    n=int(input("0-BACK\n ->"))
    if n==0:
        Home()
    else:
        exit()
 
# RESTAURANT FUNCTION
def restaurant():
    ph=int(input("Customer Id: "))
    f=0
    cur.execute("select customerid from custom")
    r=cur.fetchall()
    billc=0
    for i in r:
        i=int(i[0])
        if i==ph:
            f=1
    if f==1:
        cur.execute("select * from me")
        d=cur.fetchall()
        cur.execute("select item_no from me")
        e=cur.fetchall()
        print("Item no\t\tName\t\t\tPrice")
        for i in d:
            if i[0]!=6 and i[0]!=12:
                a,b,c=i[0],i[1],i[2]
                print(a,"\t\t",b,"\t\t",c)
            elif i[0]==6:
                a,b,c=i[0],i[1],i[2]
                print(a,"\t\t",b," ",c)
            else:
                a,b,c=i[0],i[1],i[2]
                print(a,"\t\t",b,"\t",c)
                
        print("enter 0 to exit")
        cur.execute("select extra from custom where customerid='{}'".format(ph))
        b=cur.fetchall()
        billt=b[0]
        billt=int(billt[0])
        while f==1:
            ch=int(input("enter item no"))
            if ch!=0:
                char=int(input("enter the amount of items"))
                cur.execute("select price from me where item_no='{}'".format(ch))
                g=cur.fetchone()
                g=int(g[0])
                billc+=g*char
                continue
            else:
                
                break
        billt=billc+billt
        print("Current Bill:",billc,"Total Bill: ",billt)
        cur.execute("update custom set extra='{}' where customerid='{}'".format(billt,ph))
        con.commit()
    else:
        print("Invalid Customer Id")
    n=int(input("0-BACK\n ->"))
    if n==0:
        Home()
    else:
        exit()
      
                  
# PAYMENT FUNCTION            
def Payment():
     
    ph=int(input("Customer ID:"))
    f=0
    cur.execute("select customerid from custom")
    r=cur.fetchall()
    for i in r:
        i=int(i[0])
        if i==ph:
            f=1
    if f==1:
           cur.execute("select customername,phoneno,address,checkin,checkout,room_type,room_price,days_of_stay,extra from custom where customerid='{}'".format(ph))
           r=cur.fetchall()
           r=r[0]
           name,phno,add,checkin,checkout,room,price,day,rc=r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8]
           print(r)
           print(" Payment")
           print(" --------------------------------")
           print("  MODE OF PAYMENT")
           print("  1- Credit/Debit Card")
           print("  2- Paytm/PhonePe")
           print("  3- Using UPI")
           print("  4- Cash")
           x=int(input("-> "))
           print("\n  Amount: ",((price*day)+rc))
           print("\n            Pay For AnCasa")
           print("  (y/n)")
           ch=str(input("->"))
           if ch=='y' or ch=='Y':
               print("\n\n --------------------------------")
               print("           Hotel AnCasa")
               print(" --------------------------------")
               print("              Bill")
               print(" --------------------------------")
               print(" Name: ",name,"\t\n Phone No.: ",phno,"\t\n Address: ",add,"\t")
               print("\n Check-In: ",checkin,"\t\n Check-Out: ",checkout,"\t")
               print("\n Room Type: ",room,"\t\n Room Charges: ",price*day,"\t")
               print(" Restaurant Charges: \t",rc)
               print(" --------------------------------")
               print("\n Total Amount: ",((price*day)+rc),"\t")
               print(" --------------------------------")
               print("          Thank You")
               print("          Visit Again :)")
               print(" --------------------------------\n")
               cur.execute("delete from custom where customerid='{}'".format(ph))
               con.commit()
    else: 
        print("Invalid Customer Id")
         
    n = int(input("0-BACK\n ->"))
    if n == 0:
        Home()
    else:
        exit()
 
# RECORD FUNCTION
def Record():
    cur.execute("select customername,phoneno,address,checkin,checkout,room_type,room_price from custom")
    c=cur.fetchall()
    if len(c)!=0:
        print("        *** HOTEL RECORD ***\n")
        print("| Name        | Phone No.    | Address       | Check-In  | Check-Out     | Room Type     | Price      |")
        print("----------------------------------------------------------------------------------------------------------------------") 
        for r in c:
            name,phno,add,checkin,checkout,room,price=r[0],r[1],r[2],r[3],r[4],r[5],r[6]
            print("|",name,"\t |",phno,"\t|",add,"\t|",checkin,"\t|",checkout,"\t|",room,"\t|",price)
         
        print("----------------------------------------------------------------------------------------------------------------------")
     
    else:
        print("No Records Found")
    n = int(input("0-BACK\n ->"))
    if n == 0:
        Home()
         
    else:
        exit()
Home()
