def right(list1):
    last= list1[-1]
    for i in range(len(list1)-1,0,-1):
        list1[i]= list1[i-1]

    list1[0]= last
    print("List after shifting all elements to right:", list1)

def left(list1):
    first= list1[0]
    for i in range(len(list1)-1):
        list1[i]= list1[i+1]

    list1[-1]= first
    print("List after shifting all elements to left:", list1)


#MENU


list1=[]
n= int(input("Enter number of elements to add to list: "))
for i in range(n):
    x= input("Enter element to be added to list: ")
    list1.append(x)

print("The list is:", list1)
print("MENU DRIVEN PROGRAM")
print("1- Right shift all the elements of the list.")
print("2- Left shift all the elements of the list.")

ch= int(input("Enter your choice: "))

if ch==1:
    right(list1)

elif ch==2:
    left(list1)

else:
    print("Wrong choice entered.")
