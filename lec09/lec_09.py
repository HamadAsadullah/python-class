# tuple
# non mutable tupe

names = "hamad" , "ahmed" , "ali" , 15 , 20 , 25 , True , False , False
names0 = "mohammed"  # this will raise an error 
# print(names)

# it can be used to store constant values
months = ["jan" , "feb" , "mar" , "apr" , "may" , "jun" , "jul" , "aug" , "sep" , "oct" , "nov" , "dec"]

# print(months)

cities = {
    (31.5204, 74.3587): "Lahore",
    (24.8607, 67.0011): "Karachi"

}
# print(cities)
# accessing values
myself = "hamad" ,  16  ,  True  ,  "developer"
# print(myself[2])
# del myself[3]  # this will raise an error
# print(myself[1 : 4])


# nested tuple
nested = (1, 2, 3, ("hamad") , ("ali", (8,7,6)))
print(nested)
print(nested[3])
print(nested[4][1][2])


tuple1 = (1, 2, 3, 5, 6, 7,"hamad",8, 9, 10,)
tuple2 = (4, 5, 6)
# print(tuple1 * 3)
# print(tuple1 + tuple2)

# if 4 in tuple1:
#     print("yes 4 is tuple1")
# else:
#     print("no 4 is not in tuple1")

# print(tuple1.count(7))
# print(tuple1.index("hamad"))


# unpacking tuple
myself1 = ("hamad" , 16 , True , "developer" ,
"pakistan" , "lahore" , "reading" , "traveling" ,
"coding" , "gaming")
name1 , age1 , is_student1 , profession1 ,
country1 , city1 , hobby1 , hobby2 , hobby3 , hobby4 = myself1

# print(hobby3)

myself2 = "hassan" , 16 , True , "developer" ,
"pakistan" , "lahore" , "reading" , "traveling" , "coding" , "gaming"
name1 , age1 , is_student1 , profession1 , country1 ,
city1 , *hobby2_1 , hobby3_1 , hobby4_1 = myself2
print(age1)
print(myself2)