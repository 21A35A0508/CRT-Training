row=3
col=3
arr1=[]
arr2=[]
for i in range(row):

    temp=input("enter elements in row:").split(' ')
    ele=list(map(int,temp))
    arr1.append(ele)
    print(arr1)
    for j in range(row):
        temp = input("enter elements in row:").split(' ')
        ele = list(map(int, temp))
        arr2.append(ele)
        print(arr2)
res=[[0 for j in range (col)] for i in range (row)]
for i in range (row):
 for j in range(col):
  res[i][j]=arr1[i][j]+arr2[i][j]
print(res)
