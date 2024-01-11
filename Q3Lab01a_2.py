previous_number = 0
for i in range(0, 10):
 current_number = i
 sum_of_previous_and_current = current_number + previous_number
 print(f"The sum of {previous_number} and {current_number} is: {sum_of_previous_and_current}")
 previous_number = current_number