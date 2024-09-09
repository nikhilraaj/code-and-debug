# a = int(input("enter first number:"))
# b = int(input("enter the second number"))
# if a % b == 0:
#     print("it is divisble")
# else:
#     print("not divisible")

# a = int(input("number of classes held:"))
# b = int(input("number of classes attended:"))
# c = (b / a) * 100
# print(f"{c} %")
# if c >= 75:
#     print("allowed")
# else:
#     print("not allowed")

# a = int(input("enter the number:"))
# if a % 2 == 0 and a % 3 == 0 and a % 8 != 0:
#     print("checked satisfied the statment")
# else:
#     print("not satisfied the statment")

# 5
# a = eval(input("enter the bill amount:"))
# if a >= 5000:
#     print("final bill", a - a * 30 / 100)
# elif a >= 4000 and a < 5000:
#     print("final bill", a - a * 25 / 100)
# elif a >= 3000 and a < 4000:
#     print("final bill", a - a * 20 / 100)
# elif a >= 1000 and a < 3000:
#     print("final bill", a - a * 10 / 100)
# else:
#     print(f"final bill {a}")

# a = int(input("enter the year:"))
# if a % 4 == 0 and a % 400 == 0:
#     print("leap year")
# elif a % 4 == 0 and a % 100 != 0:
#     print("leap year")
# else:
#     print("non leap year")


# a = int(input("enter the number:"))
# if a < 0:
#     print(a * -1)
# else:
#     print(a)

# a = int(input("enter the number:"))
# print(abs(a))


# Check if the sides can form a valid triangle
# a = int(input())
# b = int(input())
# c = int(input())
# if a + b > c and a + c > b and b + c > a:
#     if a == b == c:
#         print("equilateral")
#     elif a == b or b == c or a == c:
#         print("isosceles")
#     else:
#         print("scalene")
# else:
#     print("invalid")
def pattern(n):
    for i in range(1, n // 2 + 1 + 1):
        for j in range(1, n // 2 + 1 - i + 1):
            print(" ", end=" ")
        for k in range(1, i * 2):
            print(k, end=" ")
        print()
    for i in range(n // 2, 0, -1):
        for j in range(1, n // 2 + 1 - i + 1):
            print(" ", end=" ")
        for k in range(1, i * 2):
            print(k, end=" ")
        print()


n = int(input())
pattern(n)
