# functions in python

# def sum():
#     num1 = int(input("enter first number: "))
#     num2 = int(input("enter second number:" ))
#     total = num1 + num2
#     print(f"{num1} + {num2} = {total}")

# sum()


# total_price = int(input("enter total price: "))

# if total_price <= 0:
#     print("invalid price entered.")
# elif total_price >= 1000 and total_price < 2000:
#     discount = total_price * 0.10
#     final_price = total_price - discount
#     print(f"you get a 10% discount! final price is: {final_price}")
# elif total_price >= 2000 and total_price < 3000:
#     discount = total_price * 0.20
#     final_price = total_price - discount
#     print(f"you get a 20% discount! final price is: {final_price}")
# elif total_price >= 3000 and total_price < 5000:
#     discount = total_price * 0.30
#     final_price = total_price - discount
#     print(f"you get a 30% discount! final price is: {final_price}")
# elif total_price >= 5000:
#      discount = total_price * 0.50
#      final_price = total_price - discount
#      print(f"you get a 50% discount! final price is: {final_price}")
# else:
#      print(f"no discount applied. final price is: {total_price}")

# sum()

# def subtract(num1, num2):
#     result = num1 - num2
#     print(f"{num1} - {num2} = {result}")

# subtract(10, 5)

# def subtract(num1, num2):
#     def multiply(num1, num2):
#         mul = num1 * num2
#         print(f"{num1} * {num2} = {mul}")
#     multiply (num1, num2)
    
#     minus = num1 - num2
#     print(f"{num1} - {num2} = {minus}")

# subtract(10, 5)

      
def battery_analyzer() :
    bettery = int(input("enter you currert battery percentage (0 -100): "))
    if battery <= 0 or batttery > 100:
        print("invalid battery percentage.")
    is_charging = input("is you phone/laptop is charging? (yes/no): ").lower()
    if battery <= 10 and is_charging == "no":
        print("battery critical plug in immediately!")
    elif battery <= 10 and is_charging =="yes":
        print("charging started just in time!")
    elif battery > 10 and battery <= 30 and is_charging == "no":
        print("battery low consider plugging soon.")
    elif battery > 10 and battery <= 30 and is_charging == "yes":
        print("battery low consider plugging soon.")
    elif battery > 30 and battery <= 60 and is_charging == "no":
        print("battery ok moderate usage allowed.")
    elif battery > 30 and battery <= 60 and is_charging == "yes":
        print("battery ok moderate usage allowed.")
    elif battery > 60 and battery <= 90 and is_charging == "no":
        print("battery good you can unplug soon.")
    elif battery > 60 and battery <= 90 and is_charging == "yes":
        print("battery good you can unplug soon.")
    elif battery > 90 and battery <= 100 and is_charging == "yes":
        print("battery full unplug charger to save energy.")
    else:
        print("battery sufficient all good!")

battery_analyzer()

    