# using recursion
# NAME:keshava k
# USN:1RUA25BCA0048

def fact(n):
    return 1 if n <= 1 else n * fact(n-1)

n = int(input("Enter number: "))
print(fact(n))

