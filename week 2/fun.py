# def avg():
#     num1 = int(input())
#     num2 = int(input())
#     num3 = int(input())
#     average = (num1 + num2 + num3) / 3
#     print(average)
# avg()


# def num(n1: int, n2: int, n3: int):
#     total = n1 + n2 + n3
#     print(total)


# num(20, 32, 12)
# num("nik", "hil", " raj")


# def marks(n1, n2, n3, n4, n5):
#     total = n1 + n2 + n3 + n4 + n5
#     print(total)
#     perc = (total / 500) * 100
#     print(perc)


# marks(76, 57, 58, 89, 75)
# def check_even_odd(n: int):
#     if n % 2 == 0:
#         print("even")
#     else:
#         print("odd")


# check_even_odd(10)
# def simple_calculator(num1, num2, operation):
#     if operation == "+":
#         result = num1 + num2
#     elif operation == "-":
#         result = num1 - num2
#     else:
#         result = "Invalid operation"

#     print(f"The result is: {result}")


# Call the function with user input
# simple_calculator(num1, num2, operation)


# def add(n1, n2, n3):
#     total = n1 + n2 + n3
#     print(total)


# add(10, 20, 30)


def sum(a, b):
    if a > b:
        a, b = b, a
    total = 0
    while a <= b:
        total += a
        a += 1
    return total


a = int(input())
b = int(input())

print(sum(a, b))
