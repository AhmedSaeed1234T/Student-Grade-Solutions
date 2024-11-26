steps_input = input("Enter the number of steps taken each day in the month, separated by spaces: ")

steps = list(map(int, steps_input.split()))

highest_steps = max(steps)

lowest_steps = min(steps)

average_steps = sum(steps) / len(steps)

steps.sort()
steps.reverse()

print("\nStep Count Analysis: ")
print(f"Highest step count: {highest_steps}")
print(f"Lowest Step Count : {lowest_steps}")
print(f"Average number of daily steps: {average_steps:.3f}")
print(f"Steps in Desc order: {steps}")

























































# steps_input = input("Enter the number of steps taken each day in the month, separated by spaces: ")

# steps = list(map(int, steps_input.split()))
# if len(steps) not in [30, 31]:
#         print("Please enter exactly 30 or 31 numbers for the days of the month.")
#         return


# highest_steps = max(daily_steps)

# lowest_steps = min( )

# average_steps = sum(daily_steps) / len(daily_steps)

# daily_steps.sort()
# daily_steps.reverse()

# print("\n       Step Count Analysis: ")
# print(f"Highest step count: {highest_steps}")
# print(f"Lowes {lowest_steps}")
# print(f"Average number of daily steps: {average_steps:.3f}")
# print(f"Steps in Desc order: {daily_steps}")
