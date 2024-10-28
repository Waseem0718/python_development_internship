
def Reverse_digit(n):
    temp = 0
    while n!=0:
        m = n%10
        temp = (temp*10) + m
        n = n // 10
    return temp
n = 12345
print("Reverse digits : %d" % (Reverse_digit(n)))

#return power of the number
x = int(input("Enter the number :"))
a = int(input("Enter the power of number :"))
def power_of_number(x,a):
    return x**a

print(power_of_number(x,a))

#GCD of number

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Example usage:
num1 = 48
num2 = 18

result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result}")

     