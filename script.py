import psycopg2
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=myPassword")
cur = conn.cursor()
cur.execute("""
CREATE TABLE mobiles(
id integer PRIMARY KEY,
email text,
name text,
address text)
""")
 
insert_query = "INSERT INTO mobiles VALUES {}".format("(1, 'hello@dataquest.io', 'Some Name', '123 Fake St.')") 
cur.execute(insert_query)
hh=cur.execute('SELECT * FROM users') 
conn.commit()

try:
   connection = psycopg2.connect(user="postgres",
                                  password="myPassword",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")
   cursor = connection.cursor()
   postgreSQL_select_Query = "select * from mobiles"

   cursor.execute(postgreSQL_select_Query)
   print("Selecting rows from mobile table using cursor.fetchall")
   mobile_records = cursor.fetchall() 
   
   print("Print each row and it's columns values")
   for row in mobile_records:
       print("Id = ", row[0], )

except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
