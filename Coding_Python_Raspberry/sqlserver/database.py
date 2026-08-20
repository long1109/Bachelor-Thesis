import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="test",
    database="testdb",
    )

my_cursor = mydb.cursor()
#######create table
#my_cursor.execute("CREATE DATABASE testdb")

#my_cursor.execute("SHOW DATABASES")
#for db in my_cursor:
#    print(db)

#######them noi dung
#my_cursor.execute("CREATE TABLE users (name VARCHAR(255), id VARCHAR(255), c VARCHAR(255),n VARCHAR(255),user_id INTEGER AUTO_INCREMENT PRIMARY KEY  )")
#add_thing = ("INSERT INTO users "
#             "(name , id ,c ,n)"
#             "VALUES (%s,%s,%s,%s)")
#data_thing = ('long','1412103','1246788999888','234536858665')

#my_cursor.execute(add_thing,data_thing)
#emp_no=my_cursor.lastrowid
#mydb.commit()
#my_cursor.close()
#mydb.close()

########them column bi thieu
#key="idnhaxe"
#query="ALTER TABLE users ADD  %s VARCHAR(255)" % key
#my_cursor.execute(query)


########insert multiple
#sqlStuff = "INSERT INTO users (name, id, c , n, idnhaxe) VALUES(%s,%s,%s,%s,NULL)"
#record1 = ("CUONG","1412100","74545693683698","739465368576987698")

#my_cursor.execute(sqlStuff,record1)
#mydb.commit()
#sqlStuff = "INSERT INTO users (name,id ,c,n,idnhaxe) VALUES(%s,%s,%s,%s,NULL)"
#records = [("dai","1412101","754736503457638","37456973657835895"),
#    ("khiem","1412101","754736503457638","37456973657835895"),
#    ("phu","1412101","754736503457638","37456973657835895"),
#    ("phuoc","1412101","754736503457638","37456973657835895"),
#    ("messi","1412101","754736503457638","37456973657835895"),]
#my_cursor.executemany(sqlStuff, records)

#mydb.commit()
#########
#my_cursor.execute("SELECT name FROM users")
#result = my_cursor.fetchone()
#for row in result:
#    print(row)
#######
k='1412103'
p='14121034long'
#sql_select_query="""select * FROM users WHERE id = %s"""
#my_cursor.execute(sql_select_query,(k,))
#result = my_cursor.fetchall()
#for row in result:
#   print(row)

#l=row[2]
#l2=str(l)

#print(l2)
#print(type(l2))
###
my_sql = """UPDATE users SET idnhaxe = %s WHERE id = %s"""
my_cursor.execute(my_sql,(p,k,))
mydb.commit()


                  



    
    
    



