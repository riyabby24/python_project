import mysql.connector
import random
import stdiomask

mydb = mysql.connector.connect(host='localhost',password='root@123',user='root',database='rachel')
mycursor = mydb.cursor()

#mycursor.execute("create table traindetail(tnum VARCHAR(10) PRIMARY KEY,tname CHAR(20),tsrc CHAR(20),tdest CHAR(20),tac1 INT,tac2 INT,tac3 INT,tsleeper INT)")
#mycursor.execute("insert into traindetail values(12301,'RAJDHANI EXPRESS','Howrah Jn','New Delhi',20,25,30,150),(12010,'SHATABDI EXPRESS','Ahmedabad','Mumbai Central',25,30,30,150),(12511,'KERALA EXPRESS','Thiruvananthapuram','New Delhi',20,20,30,250),(13301,'HUMSAFAR','Banglore','Patna',10,15,35,150),(14201,'GURUVAYUR EXPRESS','Thiruvananthapuram','Thrissur',5,10,10,250)")
#mydb.commit()

#mycursor.execute("create table passengers(pnr int PRIMARY KEY,pname CHAR(50),age int,phone varchar(20),tname char(20),seat varchar(5),amt int)")

print("                                                                     WELCOME")

def login():
    
    user = input("Enter username: ")
    pswd = stdiomask.getpass("Enter password: ", '*')

    if pswd == "123" and user == "123":
        print("Successful Login!!")
        print("")
        print("======================================================================================================================================================")
        print("                                                      WELCOME TO RAILWAY MANAGEMENT SYSTEM!!                            ")
        print("                                                           LIST OF AVAILABLE TRAINS:")

       
            
        def bookticket():
            
            print("\nTrain No.     Train Name           Source      Destination")
            print("")
            mycursor.execute("select tnum,tname,tsrc,tdest from traindetail")
            res = mycursor.fetchall()
            for i in res:
                print(i)
                
            p = []

            n = int(input("Enter number of passengers:"))

            for i in range (1,n+1):

                print("Passenger" ,i)
                pnr = random.randint(2000,3000)
                pname = input("Enter passenger name: ")
                age = int(input("Enter passenger age: "))
                phone = int(input("Enter passenger phone number: "))
                t = int(input("Choose train (1/2/3/4/5): "))
                if t==1:
                    tname = "SHATABDI EXPRESS"
                elif t==2:
                    tname = "RAJDHANI EXPRESS"
                elif t==3:
                    tname = "KERALA EXPRESS"
                elif t==4:
                    tname = "HUMSAFAR"
                elif t==5:
                    tname = "GURUVAYUR EXPRESS"
                else:
                    print("Invalid")
                    bookticket()
                
                print("")

                print("Available seats   Price(Rs.)")    
                print("1.AC 1               750")
                print("2.AC 2               400")
                print("3.AC 3               300")
                print("4.Sleeper            150 ")
                s = int(input("Enter choice of seat(1/2/3/4): "))
                if s==1:
                    seat = "AC1"
                    amt = 750
                elif s==2:
                    seat = "AC2"
                    amt = 400
                elif s==3:
                    seat = "AC3"
                    amt = 300
                elif s==4:
                    seat = "Sleeper"
                    amt = 150
                else:
                    print("Invalid")
                    bookticket()
                     
                mycursor.execute("insert into passengers values({},'{}',{},{},'{}','{}',{})".format(pnr,pname,age,phone,tname,seat,amt))
                mydb.commit()
                print("Booking was successful with PNR number ",pnr,"and ticket fare Rs.",amt,"\nPASSENGER DETAILS:")
                print("PNR Number                           :",pnr)
                print("Passenger Name                       :",pname)
                print("Passenger Age                        :",age)
                print("Phone Number                         :",phone)
                print("Train Name                           :",tname)
                print("Seat Type                            :",seat)
                print("Total Amount                         :",amt)

            print("=======================================================================================================================================")
                       
            menu()    

        def deleteticket():
            print("Bookings:")
            mycursor.execute("select pnr,pname,tname from passengers")
            res = mycursor.fetchall()
            for i in res:
                print(i)
                
            delpnr = int(input("Enter PNR of ticket to be deleted: "))
            mycursor.execute("delete from passengers where pnr = %s",(delpnr,))
            mydb.commit()
            print("Ticket deleted successfully!!")
            
            print("=================================================================================")
            
            menu()

        def display():
            
            pnr = int(input("Enter PNR number to get details: "))

            mycursor.execute("select * from passengers where pnr = %s",(pnr,))
            ans = mycursor.fetchall()
            for i in ans:
                print(*i," Status:Confirmed")
         
            print("=================================================================================")

            menu()

        def updateticket():

            def updatemenu():
                print("")

                print("Update:\n1.Passenger Name\n2.Passenger Age\n3.Phone Number\n4.Train Name\n5.Seat\n6.Go back to Main Menu\n")
                choice = int(input("Enter choice: "))
                
                if choice==1:
                    pnr = int(input("Enter PNR number of ticket to be updated: "))
                    name = input("Enter new name: ")
                    mycursor.execute("update passengers set pname = %s where pnr = %s",(name,pnr,))
                    mydb.commit()
                    
                elif choice==2:
                    pnr = int(input("Enter PNR number of ticket to be updated: "))
                    age = int(input("Enter updated age: "))
                    mycursor.execute("update passengers set age = %s where pnr = %s",(age,pnr,))
                    mydb.commit()
                    
                elif choice==3:
                    pnr = int(input("Enter PNR number of ticket to be updated: "))
                    phone = int(input("Enter new phone number: "))
                    mycursor.execute("update passengers set phone = %s where pnr = %s",(phone,pnr,))
                    mydb.commit()
                    
                elif choice==4:
                    pnr = int(input("Enter PNR number of ticket to be updated: "))
                    print("1.SHATABDI EXPRESS\n2.RAJDHANI EXPRESS\n3.KERALA EXPRESS\n4.HUMSAFAR\n5.GURUVAYUR EXPRESS\n")
                    t = input(("Enter choice for new train name: "))

                    if t==1:
                        tname = "SHATABDI EXPRESS"
                    elif t==2:
                        tname = "RAJDHANI EXPRESS"
                    elif t==3:
                        tname = "KERALA EXPRESS"
                    elif t==4:
                        tname = "HUMSAFAR"
                    elif t==5:
                        tname = "GURUVAYUR EXPRESS"
                    else:
                        print("Invalid")
                        updateticket()
                        
                    mycursor.execute("update passengers set tname = %s where pnr = %s",(tname,pnr,))
                    mydb.commit()
                    
                elif choice==5:
                    pnr = int(input("Enter PNR number of ticket to be updated: "))
                    print("Available seats   Price(Rs.)")    
                    print("1.AC 1               750")
                    print("2.AC 2               400")
                    print("3.AC 3               300")
                    print("4.Sleeper            150 ")
                    s = int(input("Enter choice of seat(1/2/3/4): "))
                    if s==1:
                        seat = "AC1"
                        amt = 750
                    elif s==2:
                        seat = "AC2"
                        amt = 400
                    elif s==3:
                        seat = "AC3"
                        amt = 300
                    elif s==4:
                        seat = "Sleeper"
                        amt = 150
                    else:
                        print("Invalid")
                        updateticket()
                        
                    mycursor.execute("update passengers set seat = %s,amt = %s where pnr = %s",(seat,amt,pnr,))
                    mydb.commit()
                    
                else:
                    menu()
                    
                print("Updated details:\n")
                mycursor.execute("select * from passengers where pnr = %s",(pnr,))
                res = mycursor.fetchall()
                print(*res[0])

                updatemenu()
                
            mycursor.execute("select * from passengers")
            ans = mycursor.fetchall()       
            for i in ans:
                print(*i)
            updatemenu()

        def menu():
            print("\nMenu:\n1.Ticket Booking\n2.Ticket Cancellation\n3.PNR Status\n4.Update Booking\n5.Quit\n")
            ch = int(input("Enter choice: "))

            if ch==1:
                bookticket()
            elif ch==2:
                deleteticket()
            elif ch==3:
                display()
            elif ch==4:
                updateticket()
            elif ch==5:
                exit()
            else:
                print("Invalid choice!!")
                menu()
        menu()          

    else:
        print("Invalid Login!!")
        login()
    
login()


    
    
    

