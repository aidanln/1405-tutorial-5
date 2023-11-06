# binary search, time optimised search algorithm
# by Aidan Lalonde-Novales

import random
import time

''' finds the index of the first instance of a value in a sorted list '''
def count(list, value):
    return findend(list, value) - findstart(list, value) + 1

''' finds the index of the first instance of a value in a sorted list '''
def findstart(list, value):
     # declare variables for the range of the list
    bottom = 0
    top = len(list) - 1
    range = top - bottom

    # sets index to the midpoint of the range (rounded down)
    index = int((top + bottom) / 2)

    # loops until the range is between two numbers
    while range != 1:
        range = top - bottom

        # set the top range to the midpoint if the value is lesser than or equal to the midpoint,
        # otherwise set the bottom range to the midpoint. then get a new midpoint using the new range
        if value <= list[index]:
            top = index
        else:
            bottom = index
        index = int((top + bottom) / 2)

    # return the index that matches the value
    if list[index] == value:
        return index
    else:
        return index + 1

''' finds the index of the last instance of a value in a sorted list '''
def findend(list, value):
    # declare variables for the range of the list
    bottom = 0
    top = len(list) - 1
    range = top - bottom

    # sets index to the midpoint of the range (rounded down)
    index = int((top + bottom) / 2)

    # loops until the range is between two numbers
    while range != 1:
        range = top - bottom

        # set the top range to the midpoint if the value is lesser than the midpoint,
        # otherwise set the bottom range to the midpoint. then get a new midpoint using the new range
        if value < list[index]:
            top = index
        else:
            bottom = index
        index = int((top + bottom) / 2)

    # return the index that matches the value
    if list[index + 1] == value:
        return index + 1
    else:
        return index

''' testing code '''
# randomly generate a sorted list (list X) of 2500 numbers from ranges 0 - 10000
values = []
for i in range(2500):
    values.append(random.randint(0, 10000))
values.sort()

# randomly generate a list (list Y) of 50000 numbers from ranges 0 - 10000
desired_values = []
for i in range(50000):
    desired_values.append(random.randint(0, 20000))

# perform the linear search
print("\nStaring linear search... ")
start = time.time()
for i in desired_values:
	values.count(i)
end = time.time()
print("Linear time: ", (end - start))

# perform ther binary search
print("\nStaring binary search... ")
start = time.time()
for i in desired_values:
	count(values, i)
end = time.time()
print("Binary time: ", (end - start))

print("\nDone.\n")

'''
Analysis Questions

1. Q: Is your binary search count faster than the built-in list count?

A: Yes, Considerably. The linear search typically takes 1.4 seconds, while the binary search typically takes 0.3 seconds.


2. Q: What happens if you change the size of X (i.e., how does the time difference change for smaller/longer lists)?

A: Lowering the size of X causes the time difference to decrease, while increasing the size of X causes the time difference to increase.
This is because at a lower X size, there are less values to iterate through and therefore less of a need for an optimized searching algorithm,
as the built in count function can simply iterate through the lower number of values at a comperable time to the binary search.

3. Q: What if you change the range of the numbers added to X so there are more/less duplicates?

A: Changing the range of numbers so there are more/less duplicates does not change runtime signficantly.

4. Q: What if a larger proportion of numbers in Y are not present in X?

A: Similar to question 3, having a large proportion of numbers in Y that are not present in X does not change runtime signficantly.

5. Q: Do these results make sense given what you know about the runtime complexity of both functions?

A: These results make sense based on what I know about the runtime complexity of both functions, as they are both influenced by the size
of lists X and Y. The linear search has a time complexity of O(n), while the binary search has a time complexity of O(log n), meaning that
the binary search will be faster than the linear search for larger lists.

'''