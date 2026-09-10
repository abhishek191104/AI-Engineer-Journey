numbers = [12, 7, 25, 8, 19, 30, 4, 15]

largest_number = max(numbers)
smallest_number = min(numbers)
sum_numbers = sum(numbers)

length_numbers = len(numbers)
average_numbers = sum_numbers / len(numbers)

"""count = 0

for number in numbers:
  if number % 2 == 0:
    count += 1

count_even_numbers = count"""

count_even_number = sum(1 for num in numbers if num %2 == 0)

'''reverse_number = list(reversed(numbers))'''
reverse_number = numbers[::-1]

print(f"Your Numbers: {numbers}")

print(f"Largest Number: {largest_number}")

print(f"Smallest Number: {smallest_number}")

print(f"Sum of Numbers: {sum_numbers}")

print(f"Average of Numbers: {average_numbers}")

print(f"Count of Even Numbers: {count_even_number}")

print(f"Reverse List: {reverse_number}")