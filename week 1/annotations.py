a = 10
b = a // 3
print(b)
age = int(input("enter the age :"))
if age >= 18:
    print("eligible for vote")
else:
    print("not eligible for vote")

num = int(input("enter the num :"))
if num % 2 == 0:
    print("even")
else:
    print("odd")

age = int(input("enter the age :"))
if age >= 18:
    print("adult")
elif age >= 13 and age >= 17:
    print("teenagers")
else:
    print("child")
