loops in python
fon loop - waile loop
print(1)
print(2)
print(3)


# for loop
for i in "hamad":
      print("hello world", i)

example for loop
for users in ["hamad" , "ali" , "hassan" , "banned user"]:
     if users == "banned user":
          print("permission denied")
     else:
          print("permission granted")

example 2  for loop by using break keyword
for money in [10 , 20 , 50 , 100 , 500 , 1000 , 5000]:
     if money == 1000:
          print("i have 1000rs")
          break
     else:
          print("i dont have 1000rs")




by using continue keyword
for money in [10 , 20 , 50 , 100 , 500 , 1000 , 5000]:
     if money == 1000:
          print("i have 1000rs")
          continue
     else:
          print("i dont have 1000rs")

by using pass keyword

for i in "hamad":
     pass # it will do nothing and continue the loop


lncrement operator  -  decreament
number = 1
number += 1
number += 1
number += 1
number -= 1
number -= 1

print(number)




while loop
number = 1
while number <= 10:
     print("number is:", number)
     number += 1

example 1 while loop
number = 1
while number <= 10:
     print("5 x", number , "=", number * 5)
#      number += 1

numbar guessing game using while loop

     