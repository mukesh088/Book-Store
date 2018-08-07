import sqlite3
import bk_store

#print(type(title))
tl=""
aut=""
def search(title):
    try:
        store=sqlite3.connect("bookstore.db")
        cursr=store.cursor()
        cursr.execute("SELECT * FROM store WHERE title==? ",[title,])
        data=cursr.fetchone()
        x=0
        for e in data:
                x=x+1
                if x==1:
                     titl=e
                elif x==2:
                    auth=e
                else:
                    pric=e
                #print(e,end=" ")
        print(" ")
        print(title,auth,pric)
       
        return title,auth,pric
    except:
        print("NOT AVAILABLE AT STORE !!!")
        return -0.5


#store.commit()

###search(ttl)
##bk_store.createDB()
##while 1:
##    ttl=str(input("BOOK TITLE : "))
##    prc=search(ttl)
##    
##    if prc<0:
##        print(" ")
##        p=input("ADD MORE BOOKS Y/N :")
##        if p=="Y":
##            title=input("ENTER TITLE :")
##            print(" ")
##            author=input("ENTER AUTHOR NAME :")
##            print(" ")
##            price=float(input("ENTER PRICE :"))
##            print(" ")
##            bk_store.insert(title,author,price)
##            continue
##    
##    print(" ")
##    ip=int(input("NO OF COPIES :"))
##    print(" ")
##    print("TOTAL COST : {}".format(float(ip*prc)))
##    
##    print(" ")
##    q=input("WANT TO QUIT Y/N: ")
##    if q=='Y':
##        break
        
    
