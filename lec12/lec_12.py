# file handling
# we can do 3 main things in file handing
# 1. create a file 
# 2. write to a file 
# 3. read from a file
# 4. close file

# type of files 
# 1. text files (.tx ,  .py , .csv , .json)
# 2. binary files (.jpg , .png , .pdf , .exe)


# syntax
# file_object = open("file_name" , "mode")
# modes
# r - read 
# w - write
# a - append
# b - create

# create a file
# f = open("new_file.txt" , "x") 

# write to a file
# f = open("new_file.txt" , "w")
# f.write("hello world from programing communities!\n")
# f.close()

#read from a file
# f = open("new_file.txt" , "r")
# print(f.read())
# f.close()

#append to a file
# f = open("new_file.txt" , "a")
# f.write("hello world\n")
# f.close()

# using with statement ot close a file
# with open("new_file.txt" , "a") as f:
    # f.write("hello world on line no 3\n")

# line by line reading of a file
# with open("new_file.txt" , "r") as f:
    # for line in f:
        # print(line)

# readlines() method
# with open("new_file.txt" , "r") as f:
    # lines = f.readlines()
    # print(lines)





