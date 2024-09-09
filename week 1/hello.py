name = "nikhil"
age = 21
gender = "male"
print("my name is", name)
print("my age is", age)
print("my name is", name, "and gender is", gender)

# 2nd method

print(f"my name is{name}")
print(f"my gender is {gender}")

# 3rd method
# %S=String
# %d=integer
# %f=float

print("my name is %s" % name)
print("my gender is %s" % gender)
print("my age is %d" % age)

a: str = "nikhil"
print(a, type(a))
