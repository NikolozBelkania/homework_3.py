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





# for i in range (0, 1000):
#     if i % 2 == 0:
#       continue
#     print(i)

   
# import random

# x = random.randint(0, 100)

# homework_3.py
# -----------------------------------
# Study Planner – Workshop 3
# This program helps you plan study tasks,
# estimate total and average time, and analyze workload.

print("Welcome to the Study Planner!")
print("You'll enter your study tasks, estimate times, and see your total plan.\n")

# Step 1: Collect study tasks from the user
tasks = []

while True:
    task = input("Enter a study task (leave blank to finish): ").strip()
    if task == "":
        break
    if task in tasks:
        print("You already added this task. Skipping...")
        continue
    tasks.append(task)

# Check if user entered any tasks
if not tasks:
    print("\nNo tasks were entered. Exiting program.")
    exit()

# Step 2: Print summary of collected tasks
print(f"\nYou added {len(tasks)} unique tasks:")
for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")

# Step 3: Ask how many tasks to do today
while True:
    try:
        num = int(input("\nHow many tasks will you complete today? "))
        if 1 <= num <= len(tasks):
            break
        else:
            print(f"Please enter a number between 1 and {len(tasks)}.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Step 4: Gather estimated minutes per selected task
today_tasks = tasks[:num]
total_minutes = 0

for task in today_tasks:
    while True:
        try:
            mins = int(input(f"Estimated minutes for '{task}': "))
            if mins < 0:
                print("Minutes cannot be negative. Try again.")
                continue
            total_minutes += mins
            break
        except ValueError:
            print("Please enter a valid number.")

# Step 5: Calculate and print summary
average = round(total_minutes / num, 1)
print("\n--------------------------")
print("Study Plan Summary")
print("--------------------------")
print(f"Total study time: {total_minutes} minutes")
print(f"Average per task: {average} minutes")

# Step 6: Analyze plan intensity
if total_minutes < 60:
    print("Plan type: Light session.")
elif total_minutes < 150:
    print("Plan type: Moderate session.")
else:
    print("Plan type: Intensive session.")

# Inline if example
if average >= 30:
    print("Great momentum!")

# Optional Bonus: shuffle suggested order
import random
random.shuffle(today_tasks)
print("\nSuggested study order for today:")
for i, task in enumerate(today_tasks, start=1):
    print(f"{i}. {task}")

print("\nGood luck with your studies! 💪")
