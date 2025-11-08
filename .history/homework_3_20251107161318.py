# # i = 0
# # while i < 5:
# #     print(f"Hello, World!{i}")
# #     i += 1



# user_input = input("please enter a pin code: ")

# stored_pin_code = "1234"
# # print(f"{len(user_input)== 4 = }")

# # print(f"{user_input.isdigit() = }")

# while len(user_input) != 4 or not user_input.isdigit():
#     print("Invalid pin code. Please try again.")
#     user_input = input("please enter a valid pin code: ")


#     while number != int(stored_pin_code):
#         print("Incorrect pin code. Please try again.")
#         user_input = input("please enter a valid pin code: ")
#         number = int(user_input)
# print("Pin code accepted.")



# # Alternative solution:


# while True:
#     user_input = input("Please enter a 4-digit PIN: ")
#     if len(user_input) == 4 and user_input.isdigit():
#         print("Pin code accepted.")
#         break
#     else:
#         print("Invalid pin code. Please try again.")


# for 


# for i in range(5,  10, 2):
#         print(f"Hello, Universe!{i}")

# print("Hello" in "Hello Universe!")


# for char in "Hello Universe!":
#     print(char)


# for i in range(100, 111):
#     print(i)



# continue and break


# import random

# count = 0
# x = random.randint(0, 100)
# while x != 56:
#     count += 1
#     x = random.randint(0, 100)

# print(x)
# print(f"we {x} in  {count} tries")

SEARCH_NUMBER = 56
tries = 0

# while True:
#     tries += 1
#     x = random.randint(0, 100)
#     if x == SEARCH_NUMBER:
#         break

# print(f"we found {x} in {tries} tries")

for i in range(0, 100): 
    if i == 97:
       break

    print(i)
     