 
#Simple Calculator in Python


#....Input from user .......
num1 = float(input("Enter first Number :"))
num2 = float(input("Enter second number :"))

print("Selection Operation ")
print("1. Addition '+'")
print("2. Subtraction '-'")
print("3. Multiplication '*'")
print("4. Division '/'")
#...USER CHOICE.....
choice= input("Enter Choice (1,2,3,4):")

if choice == '1':
    print(f"Result is{num1 +num2}")
elif choice =='2':
    print(f"the Result is :{num1 -num2} ")
elif choice =='3':
    print(f"Result is:{num1 *num2} ")
elif choice == '4': 
    if num2 != 0:
        print(f"Result= {num1/num2}")
    else:
        print("error! division by zero is not Allowed ")       



