def high(list1):
    if len(list1)==1:
        print("Only one element in list.\nHighest and second highest number is",list1[0])
    else:
        list1= sorted(list1)
        print("The highest number is",list1[len(list1)-1], "and the second highest number is",list1[len(list1)-2])
  
#Assuming all numbers added are unique
list1 = []
n= int(input("Enter the number of integers to be added to list: "))
for i in range(n):
    x= int(input("Enter number: "))
    list1.append(x)
print("The list is:", list1)

high(list1)


    
