# Lists
# 1
my_list = list() # empty_list = []
my_list = [1, 2, 3, 4, 5]
my_list = [1, "Hello", 3.14]
print(my_list[1]) # Accessing elements by index

# 2
some_iterable = ["a", "b", "c"] # List of strings
first_letter = some_iterable[0] # Accessing first element
middle_one = some_iterable[1] # Accessing middle element
last_letter = some_iterable[2] # Accessing last element
print(first_letter, middle_one, last_letter)

# 3
some_iterable = [1, 2, 3] # змнює значення елемента за індексом 1
some_iterable[1] = -2
print(some_iterable)

# 4
chars = ['a', 'b', 'c']
last = chars.pop(1) # видаляє елемент за індексом 1 і повертає його
print(chars)

# 5
chars = ['a', 'b', 'c']
numbers = [1, 2]
chars.extend(numbers) # розширює список chars, додаючи елементи зі списку numbers
print(chars)

# 6
chars = ["a", "c"]
chars.insert(1, "b") # вставляє 'b' на індекс 1
print(chars)

# 7
chars = ['a', 'b']
chars.clear() # видаляє всі елементи зі списку
print(chars)

# 8
chars = ['a', 'b', 'c', 'd']
c_ind = chars.index('c') # шукає індекс елемента 'c'
print(c_ind)

# 9
my_list = [1, 2, 3, 4, 2, 2, 5, 2]
count_2 = my_list.count(2)
print(count_2)  # Виведе 4, оскільки число 2 зустрічається 4 рази

# 10
my_list = [1, 2, 3, 4, 5]
print(len(my_list))

# 11
nums = [3, 1, 4, 1, 5, 9, 2]
nums.sort() # Сортування списку за зростанням
print(nums)  # Виведе [1, 1, 2, 3, 4, 5, 9]

# 12
nums.sort(reverse=True) # Сортування списку за спаданням
print(nums)  # Виведе [9, 5, 4, 3, 2, 1, 1]

# 13 
words = ["banana", "apple", "cherry"]
words.sort(key=len) # Сортування списку за довжиною рядків
print(words)  # Виведе ['apple', 'banana', 'cherry']

# 14 (sorted)
nums = [3, 1, 4, 1, 5, 9, 2]
sorted_nums = sorted(nums) # Повертає новий відсортований список
print(sorted_nums)  # Виведе [1, 1, 2, 3, 4, 5, 9]

# 15 (reversed)
sorted_nums_desc = sorted(nums, reverse=True) # Повертає новий відсортований список у зворотньому порядку
print(sorted_nums_desc)  # Виведе [9, 5, 4, 3, 2, 1, 1]

#16 (sorting by length)
words = ["banana", "apple", "cherry"]
sorted_words = sorted(words, key=len) # Повертає новий список, відсортований за довжиною рядків
print(sorted_words)  # Виведе ['apple', 'banana', 'cherry']

#17 (copying a list)
chars =  ['a', 'b']
chars_copy = chars.copy() # створює поверхневу копію списку chars
print(chars_copy)

#18 (reverse a list)
chars = ["banana", "apple", "cherry"]
chars.reverse() # змінює порядок елементів списку на зворотній
print(chars)  # Виведе ['cherry', 'apple', 'banana']

# Dictionaries
#1 Creating and Modifying Dictionaries
my_dict = {"name": "Alice", "age": 25, "city": "Konchezaspa"} # створює словник з трьома парами ключ-значення
my_dict["age"] = 26 # змінює значення ключа "age" на 26
my_dict["country"] = "USA" # додає нову пару ключ-значення "country": "USA"
print(my_dict["name"], my_dict["age"], my_dict["city"], my_dict["country"]) # виводить значення ключів "name", "age", "city" і "country"
del my_dict["country"] # видаляє пару ключ-значення з ключем "country"
print(my_dict["name"], my_dict["age"], my_dict["city"]) # виводить значення ключів "name", "age" і "city"

#2 Methods of Dictionaries

#2.1 pop()
my_dict = {"name": "Alice", "age": 25, "city": "Konchezaspa"}
age = my_dict.pop("age") # видаляє пару ключ-значення з ключем "age" і повертає її значення
print(age)  # Виведе 25
print(my_dict)  # Виведе {'name': 'Alice', 'city': 'Konchezaspa'}

#2.2 update()
my_dict = {"name": "Alice", "age": 25}
my_dict.update({"email": "alice@example.com"}, {"age": 26}) # додає нову пару ключ-значення "email": "alice@example.com" і оновлює значення ключа "age" на 26
print(my_dict)  # Виведе {'name': 'Alice', 'age': 26, 'email': 'alice@example.com'}

#2.3 clear()
my_dict.clear() # видаляє всі пари ключ-значення зі словника
print(my_dict)  # Виведе {}

#2.4 copy()
new_dict = my_dict.copy() # створює поверхневу копію словника my_dict
print(new_dict)  # Виведе той самий вміст, що й my_dict але як окремий об'єкт

#2.5 get()
my_dict = {"name": "Alice", "age": 25} 
age = my_dict.get("age")  # Поверне 25
gender = my_dict.get("gender")  # Поверне None, оскільки "gender" немає в словнику 
print(age)
print(gender)

# якщо використовувати [] для доступу до неіснуючого ключа, виникне помилка KeyError
my_dict = {"name": "Alice", "age": 25}  
name = my_dict["name"]  # Поверне 'Alice'
gender = my_dict["gender"]  # Викличе KeyError, оскільки "gender" немає в словнику
print(name)
print(gender)

# Sets and Frozensets 
empty_set = set() # створює порожню множину
a = set("hello") # створює множину з унікальних символів рядка "hello"
b = {1,2,3,4,5} # створює множину з чисел від 1 до 5

a = frozenset([1,2,3]) # створює незмінювану множину з чисел 1, 2 і 3
b = frozenset([3,4,5]) # створює незмінювану множину з чисел 3, 4 і 5

union = a | b # об'єднання множин a і b
intersection = a & b # перетин множин a і b
difference = a - b # різниця множин a і b
symmetric_difference = a ^ b # симетрична різниця множин a і b

print(union)
print(intersection)
print(difference)
print(symmetric_difference)

# Tuples
my_tuple = (10, "Hello", 3.14, 40, 50)  # створює кортеж з п'яти елементів
first_item = my_tuple[1] # доступ до другого елемента кортежу
print(first_item)

# Coordinates in a dictionary
points = {
    (0,0): "O",
    (1,1): "A",
    (2,2): "B"
}

#Зрізи (slicing)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = numbers[0:10:2] # [start:stop:step] [::2] 
even_numbers = numbers[1:10:2] # [start:stop:step] [1::2]
three_numbers = numbers[2:10:3] # [start:stop:step] [2::3] 
reverse_numbers = numbers[::-1] # reverse the list 
copy_numbers = numbers[:] # copy the list

print(odd_numbers)
print(even_numbers)
print(three_numbers)
print(reverse_numbers)
print(copy_numbers)
