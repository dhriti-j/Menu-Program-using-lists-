def reverse():
    new_n= 0
    n=int(input("Enter an integer: "))
    while n!=0:
        
      dig= n%10
      new_n= new_n*10+dig
      n=n//10

    print("The reversed number is:",new_n)

def palindrome():
    n=input("Enter an integer: ")
    if n==n[::-1]:
        print(int(n),"is a palindrome")

    else:
        print(int(n),"is not a palindrome")


def prime():

    n=int(input("Enter an integer: "))
    if n>1:
     for i in range(2,n):
        if n%i==0:
            print(n,"is not a prime number.")
            break
     else:
        print(n,"is a prime number")
        

    else:
        print(n,"is neither prime nor composite")

        


print("MENU DRIVEN PROGRAM")
print("1-Reverse a number")
print("2-Check if number is a palindrome")
print("3-Check if number is prime")
print("4-Exit")
ch=int(input("Enter your choice: "))
if ch==1:
    reverse()

elif ch==2:
    palindrome()

elif ch==3:
    prime()

elif ch==4:
    print("Goodbye!\nEXIT")

else:
    print("Wrong choice entered")


    
