# FIBONACCI SEQUENCE WITHOUT RECURSION
# NAME:keshava k
# USN:1RUA25BCA0048

n = int(input("Enter limit: "))
a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
