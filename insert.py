l= []
n= int(input("Enter number of elements to add to list: "))
for i in range(n):
    x= int(input("Enter number to add in list: "))
    
    l.append(x)

print("The list is", l)

print("MENU")
print("1-Insert a new element in the beginning of the list")
print("2-Insert a new element at specific position of the list")
ch= int(input("Enter your choice: "))

if ch==1:
    x= int(input("Enter number to add in list: "))
    l.insert(0,x)
    print("The list is:",l)

elif ch==2:
    x= int(input("Enter number to add in list: "))
    pos= int(input("Enter the position at which element to be added in list(in number): "))
    l.insert(pos-1,x)
    print("The list is:",l)


else:
    print("Wrong choice entered")
    
