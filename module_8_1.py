# a=1
# b= 2
# if int(a) and str(b):
#     try:
#             a + b
#     except TypeError:
#         print("1234"+ "mdkdkdl")
# else:
#     print(a+b)

def add_everything_up(a,b):
    try:
        a+b
    except TypeError:
       return str(a)+ str(b)


    return a+b


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))