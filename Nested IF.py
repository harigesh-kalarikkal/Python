# age = int(input("Enter your age: "))
#
# if age >= 18:
#     if age>=60:
#         print('you are a senior citizen')
#     else:
#         print('you are an adult')
# else:
#     print('you are a minor')

username=input("enter your username:")
password=input("enter your password:")

if username=="admin":
    if password=="1234":
        print("Welcome admin")
    else:
        print("Wrong password")
else:
    print("Wrong username")

