import sqlite3

def createDB():
    try:
        lb=sqlite3.connect("bookstore.db")
        cursor_lb=lb.cursor()
        cursor_lb.execute(''' CREATE TABLE store (
        title TEXT PRIMARY KEY ,
        author TEXT (20) NOT NULL,
        price REAL NOT NULL);''')
        lb.close()
        print("DATABASE BOOKSTORE IS CREATED !!!")
    except:
        print("DATABASE CREATED ALREADY!!!")
        lb.close()
def insert(title,author,price):
    try:
        st=sqlite3.connect("bookstore.db")
        cur=st.cursor()
        cur.execute("INSERT INTO store (title,author,price) VALUES (?,?,?)",(title,author,price))
        st.commit()
        print("BOOK ADDED !!!!")
    except:
        print("ERROR IN OPERATION !!!")
        st.rollback()
    st.close()
        
