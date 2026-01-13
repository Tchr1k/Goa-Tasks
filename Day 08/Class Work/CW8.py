# type() გვიბრუნებს ობიექტის (ცვლადის, მნიშვნელობის) მონაცემთა ტიპს
# მაგალითად:

# print(type(5))           # <class 'int'>
# print(type(3.14))        # <class 'float'>
# print(type("გამარჯობა")) # <class 'str'>
# print(type(True))        # <class 'bool'>

age = input("შეიყვანე თქვენი ასაკი")

print("შეოყვანე მნიშვნელობა:",age)
print("მონაცემთა ტიპი:", type(age))

# ⁡⁢⁣⁣-------------------------------------------⁡

num1 = input("შეიყვანე მთელი რიცხვი:")
num1 = int(num1)

num2 = input("შეიყვანე წილადი რიცხვი")
num2 = float(num2)

name = input("შეიყვანე თქვენი სახელი:")

value = input("შეიყვანე True or False:")
value = value.lower() == "true"

print("num1:", num1,type(num1))
print("num2:", num2,type(num2))
print("name:", name,type(name))
print("value:", value, type(value))



#⁡⁢⁣⁣ -------------------------------------------⁡

