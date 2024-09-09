marks = int(input("enter the num :"))
if marks >= 91 and marks <= 100:
    print("grade a")
elif marks >= 81 and marks <= 90:
    print("grade b")
elif marks >= 71 and marks <= 80:
    print("grade c")
elif marks >= 61 and marks <= 70:
    print("grade d")
elif marks >= 1 and marks <= 60:
    print("fail")
else:
    print("invalid marks")

num = int(input("enter the number:"))
if num % 5 == 0 and num % 3 == 0:
    print("foobar")
elif num % 3 == 0:
    print("foo")
elif num % 5 == 0:
    print("bar")
else:
    print("invalid")
