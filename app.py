
from dbhelper import DbHelper
import sys
class Flipkart:
    def __init__ (self):
        self.db = DbHelper()
        self.menu()

    def menu(self):
        user_input = input("""
        1. enter r to register
        2. enter l to login
        3. enter q to quit
        """)

        if user_input == "r":
            self.register()
        elif user_input == "l":
            self.login()
        else:
            sys.exit(10000)


    def login_menu(self):
        input("""
        1. enter 1 to see profile
        2. enter 2 to edit profile
        3. enter 3 delete profile
        4. enter 4 to logout
        """)


    def register(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        responce = self.db.register(name, email, password)
        if responce:
            print("successfully registered")
        else:
            print("failed")
        self.menu()


    def login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        data = self.db.search(email, password)

        if len(data) == 0:
            print("incorrect password or email")
            self.login()
        else:
            print("logged in")

obj = Flipkart()