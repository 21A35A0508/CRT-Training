n=int(input())
for i in range(n):
    password=input()
    pass_len =len(password)>=8 and len(password)<=16
    alp=password[0].isalpha()
    upper=False
    lower=False
    digit=False
    special=False
    for i in password:
        if i.isdigit():
            digit=True
        elif i.isupper():
            upper=True
        elif i.islower():
            lower=True
        else:
            special=True
    if pass_len and alp and upper and lower and digit and special:
        print(True)
    else:
        print(False)

