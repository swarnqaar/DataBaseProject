import mysql.connector

class DbHelper:
    def __init__(self):
       try:
           self.conn = mysql.connector.connect(host="localhost",user="root",password="",database="my_database")
           self.mycursor = self.conn.cursor()
       except:
           print("Error connecting to database")
       else:
           print("successfully connected to database")

    def register(self, name, password,email):
        try:
            query = "Insert into "
            self.mycursor.execute(""" INSERT INTO `users` (`id`, `name` , `email` , `password`) VALUES (NULL, '{}', '{}', '{}');""".format(name, email, password))
            self.conn.commit()
        except Exception as e:
            print("Registration error:", e)
            return -1
        else:
            return 1
    def search(self, email, password):
        try:
            self.mycursor.execute(""" SELECT * FROM `users` WHERE `email` = '{}' AND PASSWORD LIKE '{}'""".format(email, password))
            self.conn.commit()
        except Exception as e:
            print("Search error:", e)


