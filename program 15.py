l= []
n= int(input("Enter number of elements to add to list: "))
for i in range(n):
    x= int(input("Enter number to add in list: "))
    
    l.append(x)
print("The list is:",l)

print("MENU")
print("1-Insert a new element in beginning of sorted list.")
print("2- Remove duplicate values.")
n= int(input("Enter choice: "))

if n==1:
    l=sorted(l)
    x= int(input("Enter number to add: "))
    l.insert(0,x)
    print("Number added.\nThe list is now:", l)

elif n==2:
    new_l=[]
    for i in l:
        if i not in new_l:
            new_l.append(i)

    print("Task completed.\nThe new list is:", new_l)


else: print("Invalid choice entered.")
