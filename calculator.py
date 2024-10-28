# Calculator for multiple numbers

def add(*args):
    return sum(args)

def subtract(*args):
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

def divide(*args):
    result = args[0]
    for num in args[1:]:
        if num == 0:
            return "Error! Division by zero is not allowed."
        result /= num
    return result

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num_count = int(input("Enter the number of values: "))
        values = []
        for i in range(num_count):
            values.append(float(input(f"Enter value {i + 1}: ")))

        if choice == '1':
            print("Result:", add(*values))
        elif choice == '2':
            print("Result:", subtract(*values))
        elif choice == '3':
            print("Result:", multiply(*values))
        elif choice == '4':
            print("Result:", divide(*values))
        break
    else:
        print("Invalid Input")
