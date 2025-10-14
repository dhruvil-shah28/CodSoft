print("CALCULATOR")

x=float(input("Enter the first number: "))
y=float(input("Enter the second number: "))

print("\nSelect an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (1/2/3/4): ")

if choice=='1':
    result=x+y
    print(f"\nResult: {x} + {y} = {result}")

elif choice=='2':
    result=x-y
    print(f"\nResult: {x} - {y} = {result}")

elif choice=='3':
    result=x*y
    print(f"\nResult: {x} × {y} = {result}")

elif choice=='4':
    if y!=0:
        result=x/y
        print(f"\nResult: {x} ÷ {y} = {result}")
    else:
        print("\nError: Division by zero is not allowed!")

else:
    print("\nInvalid choice! Please select 1, 2, 3, or 4.")
