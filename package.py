class User:
    full_name=""
    email=""
    __password=""
    mobile_number=""
    def update_name(self,new_name):
        self.full_name=new_name
    def get_name(self):
        return self.full_name
    def update_password(self,new_password):
        self.__password=new_password
    def update_mobile_number(self,new_number):
        self.mobile_number=new_number

