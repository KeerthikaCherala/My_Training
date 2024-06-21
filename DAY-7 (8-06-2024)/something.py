'''L = ['L2', 'R3', 'L2']

# Create a new list to store the integers
numbers = []

# Loop through the original list and extract the numbers
for item in L:
  numbers.append(int(item[1:]))  # Extract the number from the second character onwards

# Print the new list of integers
print(numbers)'''


'''L = ['sch', 'cho', 'hoo', 'ool']

# Create a new list to store the modified strings
L1 = []

# Loop through the original list
for item in L:
  # Perform a circular shift by appending the first character and then the remaining characters
  L1.append(item[1:] + item[0])

# Print the modified list
print(L1)'''

'''L = ['sch', 'cho', 'hoo', 'ool']

# Define a key function to sort by the second character
def sort_by_second_letter(word):
  return word[1]  # Return the second character of the string

# Sort the list using sorted() with the custom key
sorted_L = sorted(L, key=sort_by_second_letter)

# Print the sorted list
print(sorted_L)'''

s = 'hoc'

# Sort the characters and create a new string (more concise)
sorted_s = ''.join(sorted(s))

print(sorted_s)
