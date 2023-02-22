def invert(string):
    res=" "
    for i in string:
        if i=='0':
            res+='1'
        else:
            res+='0'
    return res
a=5
b=7
op='^'
new_a=bin(a)[2:]
new_b=bin(b)[2:]
new_a=invert(new_a)
new_b=invert(new_b)
print(new_a,new_b)
print(int(new_a,2))
x=int(new_a,2)
y=int(new_b,2)
print(x^y)