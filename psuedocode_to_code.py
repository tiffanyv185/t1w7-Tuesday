# # - Example 1: Calculate the sum of a list of numbers
# ```
#     [1, 2, 3, 4, 5]
#     Initialise the sum to 0
#     For each number in the list
#         ADD the number to sum
#     END FOR
#     Print sum

numbers = [1, 2, 3, 4, 5]

total_sum = 0

for number in numbers:
    total_sum += number
print(total_sum)


# - Example 2: Finding the maximum number in a list
# ```
#     Initialise max to the first number of the list
#     FOR each number in the list
#     IF number > than max THEN
#         Set max to number
#     END IF
# ```

numbers = [1, 2, 3, 4, 5]

max_number = numbers [0]
for number in numbers:
    if number > max_number:
        max_number = number
print(max_number)