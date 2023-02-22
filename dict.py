
db=[{ 'a@mail.com','aba'},
    {'b@mail.com','Bac'},
    {'c@mail.com','21A'}
 ]
print(db)
username=input("enter username")
password=input("enter password")
temp={'username':'password'}
if temp in db:
    print("found")
else:
    print("invalid")
