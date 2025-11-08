# i = 0
# while i < 5:
#     print(f"Hello, World!{i}")
#     i += 1



user_input = input("please enter a pin code: ")

stored_pin_code = "1234"
# print(f"{len(user_input)== 4 = }")

# print(f"{user_input.isdigit() = }")

while len(user_input) != 4 or not user_input.isdigit():
    print("Invalid pin code. Please try again.")
    user_input = input("please enter a valid pin code: ")

number = int(user_input)
    
print("Pin code accepted.")



# while True:
#     user_input = input("Please enter a 4-digit PIN: ")
#     if len(user_input) == 4 and user_input.isdigit():
#         print("Pin code accepted.")
#         break
#     else:
#         print("Invalid pin code. Please try again.")
