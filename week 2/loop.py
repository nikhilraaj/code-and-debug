# i = 1
# while i <= 10:
#     print(i, end=" ")
#     i += 1

# n = int(input())
# i = 1
# while i <= n:
#     print(i, end=" ")
#     i += 1
# print(i)

# n = int(input())
# i = int(input())
# while i <= n:
#     print(i, end=" ")
#     i += 1


# def fact(n):
#     if n == 1 or n == 0:
#         return 1
#     return fact(n - 1) * n


# print(fact(5))
# i = 5674
# j = 10983
# co = 0
# while i <= j:
#     if i % 7 == 0:
#         co += 1
#     i += 1
# print(co)


# def product_of_numbers(n):
#     i = 1
#     total = 1
#     while i <= n:
#         total = total * i
#         i += 1
#     return total


# print(product_of_numbers(5))


# def factors(n: int) -> None:
#     i = 1
#     while i <= n:
#         if n % i == 0:
#             print(i, end=" ")
#         i += 1


# factors(5)


# def distriibut(arr):
#     candy_len = int(len(arr) / 2)
#     unique_candy = len(set(arr))
#     return min(candy_len, unique_candy)


# arr = [3, 3, 3, 3, 3, 34, 3]
# distriibut(arr)
# print()


def pattern(n):
    i = 1
    while i <= n:
        a = i * 10
        print(a)
        i += 1


n = int(input())
print(pattern(n))
