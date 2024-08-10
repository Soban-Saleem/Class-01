
#ASSIGNMENT 02 CALCULATOR 

# Taking input from the user

num1 = int(input ("Enter the number:" ))
num2 = int(input ("Enter the number:" ))

opr = input("Enter the operator( +, -, *, / ): ")

# Performing  operation

if opr == "+":
    print (num1 + num2)
elif opr == "-":
    print (num1 - num2)
elif opr == "*":
    print (num1 * num2)
elif opr == "/":
    print (num1 / num2)
    if num2 != 0:
        print (num1 / num2)
    else:
        print ("Error ! Division by zero")    

else:
    print ( "Invalid Operation")     
    


           

