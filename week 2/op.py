# def marks(s1, s2, s3, s4, s5) -> bool:
#     total = (s1 + s2 + s3 + s4 + s5) / 5
#     if total >= 33:
#         return True
#     else:
# return False


# x = marks(45, 66, 44, 77, 88)
# print(x)


# def marks(s1, s2, s3, s4, s5) -> bool:
#     total = (s1 + s2 + s3 + s4 + s5) / 5
#     return total >= 33


# x = marks(23, 2, 12, 34, 43)
# print(x)


# def average(n1, n2, n3):
#     avg = (n1 + n2 + n3) / 3
#     return avg


# n1 = int(input())
# n2 = int(input())
# n3 = int(input())
# x = average(n1, n2, n3)
# print(x)


# def compare(avg, n4):
#     if x >= n4:
#         return True
#     else:
#         return False


# n4 = int(input())
# y = compare(x, n4)
# print(y)


# def multiple(n):
#     i = 1
#     while i <= 10:
#         m = n * i
#         i += 1
#         print(m)


# n = int(input())
# print(multiple(n))

# my_list = [4, 8, 6, 5, 3, 12, 1, 7, 6, 2]
# n = len(my_list)
# for i in (n - 1, -1, -1):
#     if my_list[i] % 5 == 0:
#         print(my_list[i])


# def create_list(length):
#     list2 = []
#     for i in range(length):
#         x = int(input("enter no:"))
#         list2.append(x)
#     return list2


# y = create_list(6)
# print(y)


def create_list(length):
    my_list = []
    for i in range(length):
        n = int(input())
        my_list.append(n)
    return my_list


create_list(4)
print(my_list)
n = len(my_list)
other_list = []
for i in range(n - 1, -1, -1):
    other_list.append(my_list[i])
print(other_list)
