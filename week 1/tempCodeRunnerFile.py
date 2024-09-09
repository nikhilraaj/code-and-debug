# a = int(input("enter the number:"))
# if a < 0:
#     print(a * -1)
# else:
#     print(a)
def pattern(n):
    for i in range(n, 0, -1):
        for j in range(i, 0):
            print(j, end=" ")
        print()


n = int(input())
pattern(n)
