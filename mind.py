import time 
import random


num1 = random.randint(1,999)
num2 = random.randint(1,99)


print(f"Test: {num1} * {num2}")

start_time = time.time()
user_input = input("Enter result: ")


result = num1 * num2


while True:
    if int(user_input) == result:
        end_time = time.time()
        input_time = round(end_time - start_time)
        print(f"It took you {input_time}")
        break
    else:
        print("Try again")
        user_input = input("Enter result: ")

