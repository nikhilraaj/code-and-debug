a = 5
b = 10
print(a > 5 and b >= 10)
print(a >= 5 or not b > 10)
print(not (a > 5 and b > 5))
print(a < 10 or not b < 10)

# 2
dis_km = eval(input("enter the distance:"))
miles = dis_km * 0.621
print(miles)

# 6
tour = int(input("enter the number of tournament:"))
won = int(input("enter the number of won tournament:"))
loss = int(input("enter the number of loss tournament:"))
t = won + loss
tie = tour - t
print(f"tie matches{tie}")
points = won * 4 + tie * 2
print(f"total point is {points}")

# 9
a = eval(input("length"))
b = eval(input("breadth"))
c = a == b
print(c)
