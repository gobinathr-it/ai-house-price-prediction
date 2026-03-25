"""
for i in range(1,11):
    print(i,"x2=",i*2)

a=int(input())
if(a%2==0):
        print("even")

a=[]
print("enter 10 numbers:")
for i in range(10):
    num=int(input("enter num"+str(i+1)))
    a.append(num)  
print(a)

for i in range(1,3):
    print("week",i)
    for j in range(1,4):
        print("day:",j)

for i in range(1,5):
    print()
    for j in range(1,i+1):
        print("*",end="" )

i=0
while(i==0):
    print(i)
    i=i+1

a = [1,2,3,4,5,6]
a.append(True)
a.append("gobi")
a.append(5)

a = [1,2,3,4,5,6]
a[0]=11
a.pop(3)
print(a)

a = [1,2,3,4,5,6]
b = [7,8,9,0]
a.extend(b)
print(a)


a = {1,2,3} # can't change the values once created the tupple
b = list(a) # tuple into list is possible
b.pop(2) #after change u will do any modification

"""
a = (1,2,3,4) #unordered
 # 10 add in last
print(a)






