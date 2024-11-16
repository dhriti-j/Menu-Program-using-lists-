list1=[]
list2=[]
while True:
    x= input("Enter element to add to list: ")
    list1.append(x)
    list2.append(x)
    y_n= input("Do you want to enter more elements? (y/n): ")
    if y_n.lower()=="n":
        break

print("The list is", list1)

n= len(list1)

if n%2==0:
    for j in range(0,n-1,2):
        list1[j], list1[j+1] = list1[j+1], list1[j]

    print("The list after swapping the elements at odd position with even position : ", list1)

    for i in range(n//2):
        list2[i], list2[i+(n//2)]= list2[i+(n//2)], list2[i]
    print("The list after swaping the first and second half: ", list2)


else:
    for j in range(0,n-2,2):
        list1[j], list1[j+1] = list1[j+1], list1[j]
    print("The list after swapping the elements at odd position with even position : ", list1)

    for i in range(n//2):
        list2[i], list2[i+(n//2)+1]= list2[i+(n//2)+1], list2[i]
    print("The list after swaping the first and second half: ", list2)
        
    
