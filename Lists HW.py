# 1 Creating a List
fruits = ['Apple', 'Banana', 'Mango', 'Orange', 'Pineapple']
print(fruits)

# 2 Accessing Elements
colors = ['Red', 'Blue', 'Green', 'Yellow', 'Purple']
print(colors[0])
print(colors[2]) 
print(colors[-1])  

# 3 Modifying a List
numbers = [10, 20, 30, 40, 50]
numbers[1] = 25 
numbers.append(60) 
print(numbers)

# 4 List Slicing
names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma']
subset = names[:3]
print(subset)

# 5 Looping through a List
numbers = list(range(1, 11))
print("Squares of numbers 1-10:")
for number in numbers:
    print(number ** 2)

# 6 List Methods: Append and Extend
shopping_cart = []
shopping_cart.append('milk')
shopping_cart.append('bread')
shopping_cart.append('eggs')
shopping_cart.extend(['butter', 'cheese'])
print(shopping_cart)

# 7 Finding Maximum and Minimum in a List
numbers = [45, 22, 88, 56, 92, 33]
print("Max number: ", max(numbers))
print("Min number: ", min(numbers))

# 8 Counting Occurrences
letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
print("Count of 'a': ", letters.count('a'))

# 9 List Comprehension
squares_of_even = [x ** 2 for x in range(11) if x % 2 == 0]
print(squares_of_even)

# 10 Removing Duplicates
nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_nums = list(set(nums))
print(unique_nums)



