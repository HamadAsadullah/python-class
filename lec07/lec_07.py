# new type
# list - mutable type
# in context of other languages: array

fruits = ["apple", "banana", "cherry"]

# exlmple of students
student1 = "hamad"
student2 = "ali"
student3 = "rashid"
student4 = "ahmed"
student5 = "fahad"
student6 = "asad"

# peint(f"student 1: {student1}")
# index       0    ,    1   ,   2   ,    3   ,   4   ,    5

students = ["hamad", "ali", "rashid", "ahmed", "fahad", "asad"]

print(students)
students.append("raheem")
# list after append ["hamad", "ali", "rashid", "ahmed", "fahad", "asad", "raheem"]
print(students)
students.extend(["kaka", "hassan"])
print(students)
# list after extend ["hamad", "ali", "rashid", "ahmed", "fahad", "asad", "raheem", "kaka", "hassan"]
students.insert(2, "naeem")
print(students)












# new type
# list - mutable type
# in context of other languages: array

fruits = ["apple", "banana", "cherry"]

# exlmple of students
student1 = "hamad"
student2 = "ali"
student3 = "rashid"
student4 = "ahmed"
student5 = "fahad"
student6 = "asad"

# peint(f"student 1: {student1}")
# index       0    ,    1   ,   2   ,    3   ,   4   ,    5

students = ["hamad", "ali", "rashid", "ahmed", "fahad", "asad"]
print(students, "original list")






# adding new student to the list
students.append("raheem")
# list after append ["hamad", "ali", "rashid", "ahmed", "fahad", "asad", "raheem"]
print(students,"list after append")
students.extend(["kaka", "hassan"])
print(students, "list after extend")
# list after extend ["hamad", "ali", "rashid", "ahmed", "fahad", "asad", "raheem", "kaka", "hassan"]
students.insert(2, "naeem")
print(students, "list after insert")

# removing student from the list
students.remove("kaka")
print(students, "list after remove")

students.pop()
print(students , "list after pop")

del students[3]
print(students , "list after del")

# updating student name
students[1] = "hassan"
print(students , "list after update")

# slicing
print(students[1:4] , "list after slicing ")
print(students[:4] , "list after slicin from start")
print(students[0:5:2] , "list after slicing with step 2")
