a = int(input("enter no.01:"))
b = int(input("enter no.02:"))
c = int(input("enter no.03:"))
d = int(input("enter no.04:"))
e = int(input("enter no.05:"))
average = (a + b + c + d + e) / 5
print(f"average is {average}")

a = 34
print(id(a))
a += 4
print(a, id(a))
a = 33
b = 32
print(id(a))
print(id(b))
