# # homework_3.py
# # -----------------------------------
# # Study Planner – Workshop 3
# # This program helps you plan study tasks,
# # estimate total and average time, and analyze workload.

# print("Welcome to the Study Planner!")
# print("You'll enter your study tasks, estimate times, and see your total plan.\n")

# # Step 1: Collect study tasks from the user
# tasks = []

# while True:
#     task = input("Enter a study task (leave blank to finish): ").strip()
#     if task == "":
#         break
#     if task in tasks:
#         print("You already added this task. Skipping...")
#         continue
#     tasks.append(task)

# # Check if user entered any tasks
# if not tasks:
#     print("\nNo tasks were entered. Exiting program.")
#     exit()

# # Step 2: Print summary of collected tasks
# print(f"\nYou added {len(tasks)} unique tasks:")
# for i, task in enumerate(tasks, start=1):
#     print(f"{i}. {task}")

# # Step 3: Ask how many tasks to do today
# while True:
#     try:
#         num = int(input("\nHow many tasks will you complete today? "))
#         if 1 <= num <= len(tasks):
#             break
#         else:
#             print(f"Please enter a number between 1 and {len(tasks)}.")
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")

# # Step 4: Gather estimated minutes per selected task
# today_tasks = tasks[:num]
# total_minutes = 0

# for task in today_tasks:
#     while True:
#         try:
#             mins = int(input(f"Estimated minutes for '{task}': "))
#             if mins < 0:
#                 print("Minutes cannot be negative. Try again.")
#                 continue
#             total_minutes += mins
#             break
#         except ValueError:
#             print("Please enter a valid number.")

# # Step 5: Calculate and print summary
# average = round(total_minutes / num, 1)
# print("\n--------------------------")
# print("Study Plan Summary")
# print("--------------------------")
# print(f"Total study time: {total_minutes} minutes")
# print(f"Average per task: {average} minutes")

# # Step 6: Analyze plan intensity
# if total_minutes < 60:
#     print("Plan type: Light session.")
# elif total_minutes < 150:
#     print("Plan type: Moderate session.")
# else:
#     print("Plan type: Intensive session.")

# # Inline if example
# if average >= 30:
#     print("Great momentum!")

# # Optional Bonus: shuffle suggested order
# import random
# random.shuffle(today_tasks)
# print("\nSuggested study order for today:")
# for i, task in enumerate(today_tasks, start=1):
#     print(f"{i}. {task}")

# print("\nGood luck with your studies! 💪")