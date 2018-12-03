import mysql.connector
import pickle
from mysql.connector import errorcode

cnx = mysql.connector.connect(user='root', password = 'password',
                            host = '127.0.0.1',
                            database='hackathan')
cursor = cnx.cursor()


def uploadonDB(name, email, password):
    #'signup' is the name of the table
    query = "INSERT INTO signup (username, email, pword) VALUES ('%s', '%s', '%s');" % (name, email, password)
    cursor.execute(query)
    cnx.commit()

    query1 = "select * from signup;"
    cursor.execute(query1)
    print(cursor.fetchall())

def check():
    query = "SELECT username FROM signup;"
    cursor.execute(query)
    lis_1=cursor.fetchall()
    query_2="SELECT pword FROM signup;"
    cursor.execute(query_2)
    lis_2=cursor.fetchall()
    check={}
    counter=0
    for i in lis_1:
        name=i[0]
        check[name]=lis_2[counter][0]
        counter=counter+1
    #output = open('data.pkl', 'wb')
    #pickle.dump(check, output)
    # print(cursor.fetchall())


check()
