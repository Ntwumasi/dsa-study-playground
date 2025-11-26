# 🔁 ITERATION

# enumerate: get index and value when looping through a list
nums = [10, 20, 30]
for index, value in enumerate(nums):
    print(index, value)  # Useful for indexed loops in LeetCode

# zip: combine two (or more) lists into pairs
names = ["Alice", "Bob"]
scores = [85, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")  # Used in aligning related data

# 📊 EVALUATION

# eval: evaluate a string as a Python expression
expression = "2 * 3 + 4"
result = eval(expression)
print(result)  # 10 — used in calculator-style problems

# ✂️ FILTERING / TRANSFORMING

# filter: keep only items that match a condition
nums = [-2, 3, 0, 5]
positive = list(filter(lambda x: x > 0, nums))  # [3, 5]

# map: apply a function to each item in a list
squared = list(map(lambda x: x**2, [1, 2, 3]))  # [1, 4, 9]

# list comprehensions (better alternative to map/filter in most cases)
even = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# ✏️ SORTING

# sorted: sort list with custom key or reverse
words = ["apple", "banana", "kiwi"]
sorted_by_length = sorted(words, key=len)  # ['kiwi', 'apple', 'banana']

# list.sort(): same as sorted, but modifies the list in-place
nums = [3, 1, 2]
nums.sort()  # nums becomes [1, 2, 3]

# 📦 COLLECTION UTILITIES

from collections import Counter, defaultdict

# Counter: count frequency of elements
letters = "banana"
count = Counter(letters)  # {'a': 3, 'b': 1, 'n': 2}

# defaultdict: auto-create default values for keys
dd = defaultdict(list)
dd['x'].append(1)  # {'x': [1]}

# set: remove duplicates from a list
unique = list(set([1, 2, 2, 3]))  # [1, 2, 3]

# 🔢 MATH

# sum: add all numbers
print(sum([1, 2, 3]))  # 6

# max / min: get largest/smallest item
print(max([1, 9, 3]))  # 9
print(min([1, 9, 3]))  # 1

# abs: get absolute value
print(abs(-7))  # 7

# round: round to nearest int (or to given decimal places)
print(round(3.14159, 2))  # 3.14

# 🧵 STRING METHODS

s = "  hello world  "

# split: split string into words
print(s.split())  # ['hello', 'world']

# join: combine list of strings with a delimiter
words = ["fast", "ai"]
print(" ".join(words))  # "fast ai"

# strip: remove leading/trailing whitespace
print(s.strip())  # "hello world"

# replace: replace part of a string
print(s.replace("hello", "hi"))  # "  hi world  "

# 🔄 BOOLEAN CHECKS

# any: returns True if any item is truthy
print(any([False, 0, 3]))  # True

# all: returns True if all items are truthy
print(all([1, True, "yes"]))  # True

# 🔁 REVERSE + RANGE

# reversed: reverse an iterable
for val in reversed([1, 2, 3]):
    print(val)  # 3, 2, 1

# range: generate numbers
for i in range(3):  # 0, 1, 2
    print(i)

# 🧰 MISC UTILITIES

# isinstance: check type of object
print(isinstance("hi", str))  # True

# type: get type of object
print(type(123))  # <class 'int'>

# len: get length of string, list, dict, etc.
print(len("hello"))  # 5