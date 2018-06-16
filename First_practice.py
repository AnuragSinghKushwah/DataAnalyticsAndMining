# """
# Something here
# """
# a = 10 #something about 3
# b = 10.01
# c = [10]
# d = {"value":10}
# e = (10, 11)
# f = "hello"
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))

# import csv
class ClassName():
    def __init__(self, input_x, input_y):
        print("value of input_x ",type(input_x))
        print("value of input_y ",type(input_y))
        self.x = input_x
        self.y = input_y
        print("output : ",self.add())

    def add(self,):
        return self.x+self.y


# ClassName(1,2)
# ClassName("1","2")
# ClassName([1],[2])
# if __name__ == '__main__':
#     ClassName(1, 2)
    # ClassName(1, 2).y

def addition(x,y):
    # Return Sum of two variables
    return x+y

def subtraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    return x/y

# print("add : ",addition(20,10))
# print("sub : ",subtraction(20,10))
# print("mul : ",multiplication(20,10))
# print("div : ",division(20,10))

some_string = "hello world at TechSimPlus"
# Strip, Length, Split, slicing, indexing, format
# print(some_string.split())
# print(some_string.split("l"))
# print(some_string.replace("world","universe"))
# print(len(some_string))
# print(len(some_string.replace(" ","")))
# print(some_string.strip())
# print(some_string[5:-6])
# new_string = " bhopal"
# some_string =some_string +new_string
# print(some_string)
#
# some_list = ["hello", "world", "at", "TechSimPlus"]
# # print(len(some_list))
# # some_list.append("bhopal")
# print(some_list)
#
# # output = "\t".join(some_list)
# # print("output new: ",output)
#
# print(some_list[:3])
# for i in range(0, 12):
#     try:
#         print("item ; ",some_list[i])
#     except Exception as e:
#         print("Exception in indexing : ",e)
#         # pass

# some_tuple  = ("hello","world","at","TechSimPlus")
# print("some_tuple ",some_tuple)
# print(len(some_tuple))
# print(some_tuple[0:3])
from pprint import pprint
some_dict = {"name":"Raj",
             "sur name":"Malhotra",
             "country":"india",
             "age":"22",
             "salary":22000000.000324,
             "movies":["DDLJ","KKHH","KHNH"],
             "competitor":{"name":"sallu","sur name":"khan"},
             }

# pprint(some_dict)
# print(len(some_dict))
# print(" ".join(some_dict["movies"]))
# print(some_dict["movies"][0])
# print(some_dict["competitor"]["name"])
#
# print(type(some_dict.keys()))
# print(some_dict.values())

# print(some_dict[list(some_dict.keys())[2]])
# outfile = open("output.txt")
# for key in some_dict:
#     output = "Key : "+key+" , Value : "+str(some_dict[key])
#     print(output)
#     print("Key : {} , Value : {}".format(key, some_dict[key]))

if int(some_dict["age"])<=int(25):
    print("Yes he is underage")

# if some_dict["age"]==22 or some_dict["age"]=="22":
#     print("Yes he is underage")
# elif some_dict["age"]=="22":
#     print("Yes he is underage")
# else:
#     print("he is not underage")

# for i in some_dict:
#     if some_dict[i]=="age":
#         if int(some_dict[i]["age"])<=25:
#             print("yes he is underage")
#             break
#
# output = [i for i in some_dict if i=="age" and int(some_dict[i]) <=25]

