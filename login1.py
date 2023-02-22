from login import User
class login:
    __db=[]
    def __init__(self):
        self.print_menu()
    def print_menu(self):
        print("welcome user")
        print("1.register")
        print("2.login")
        print("3.exit")
    def create_user(self,name,email,password):
        new_user=User(name,email,password)
        self.__db.append(new_user)
        print(self.__db)
        return True
    def validate_user(self,email,password):
        temp=self.__db.copy()
        for user_obj in temp:
            if email==user_obj.email:
                if password==user_obj.get_user_password():
                    return "login success"
                else:
                    return "failed"
        return False
obj=login()
while True:
    option=input("enter option:")
    if option=='1':
         name=input("enter your name:")
         mail = input("enter your mail:")
         password = input("enter your password:")
         res=obj.create_user(name,mail,password)
         if res==True:
            print("user created")
    elif option=='2':
        email=input("enter email:")
        password=input("enter a password")
        if obj.validate_user(email,password):
            print("login success")
        else:
            print("fail")
    elif option=='3':
        break
    else:
      print("invalid process")

