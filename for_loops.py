# For loop that iterates over items in this list (simpler)
numbers = [1, 2, 3, 4, 5]
print(numbers)
for item in numbers:
    print(item)
print("done")
# Uses while loop to achieve same result (len = length of a list)
i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1
