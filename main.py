# import calculator 
# print("add", calculator.add_number(10,11))
# import calculator as ca
# print("add",ca.add_number(10,11))
from calculator import *
print("add",add_number(9,12))
print("sub",sub_number(12,6))
print("multi",multiply_number(18,6))
print("div",divide_number(18,6))
print("addinglist",add_list([78,12,13,14]))



# fruits 
# add new fruits in list
# check if fruit present in a list or notand return True/False
# Index of the fruit in list
# reverse list items

import fruits
print(fruits.addfruit(["manngo","apple","gauva"],"banana"))
fruit = ['kiwi','grapes']
print(fruits.addfruit(fruit,"abc"))
print(fruit)

a = [1,2,2,3,4,5,6,6,67,7,7,7,7,7,7,7,11,7,7,7,45,7,7,51, 53,4,6,7,8,9,10]

print(fruits.checkfruits(fruit,"banana"))
print ("index",(fruits.getindex(a,51)))