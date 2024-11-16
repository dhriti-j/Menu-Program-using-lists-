def push(list1):
    while True:
       x= input("Enter element to add in list: ")
       list1.append(x)
       y_n= input("Do you want to enter more elements? (y/n): ")
       if y_n.lower() == "n":
          break

    print("The stack is : ")
    print(list1[len(list1)-1], "<-----TOP")
    for i in range(len(list1)-2,-1, -1):
        print(list1[i])

def stack_pop(list1):
    while True:
        if len(list1)<1:
            print("STACK UNDERFLOW")
            break

        elif len(list1)==1 :
            list1.pop()
            print("TASK COMPLETED! Stack is empty now.")
            break
        else :
            list1.pop()
            print("TASK COMPLETED")
            print("The stack is :")
            print(list1[len(list1)-1], "<-----TOP")
            for i in range(len(list1)-2, -1, -1):
                print(list1[i])
            
            y_n= input("Do you want to remove more elements? (y/n): ")
            if y_n.lower() == "n": break

#MENU         
list1= []
while True:
    x= input("Enter element to add in list: ")
    list1.append(x)
    y_n= input("Do you want to enter more elements? (y/n): ")
    if y_n.lower() == "n":
        break
print("The stack is : ")
print(list1[len(list1)-1], "<----TOP")
for i in range(len(list1)-2, -1, -1):
        print(list1[i])
while True:
 print("MENU PROGRAM")
 print("1- Push element in stack")
 print("2- Pop element from stack")
 print("3-Exit")
 n= int(input("Enter your choice: "))
 if n==1:
    push(list1)

 elif n==2:
    stack_pop(list1)

 elif n==3:
    print("Goodbye!", "\nEXIT")
    break
 else:
    print("Wrong choice entered")    
