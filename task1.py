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
