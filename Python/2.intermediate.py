# List

# Lists are used to store multiple items in a single variable.

# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.


thislist = ["apple", "banana", "cherry"]
print(thislist)

# List Items
# List items are ordered, changeable, and allow duplicate values.

# List items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

# If you add new items to a list, the new items will be placed at the end of the list.

# Changeable
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

# Allow Duplicates
# Since lists are indexed, lists can have items with the same value:

carList = ["Ford", "BMW", "Volvo", "BMW"]
print(carList)

print(len(carList))  # Output: 4

# List items can be of any data type:


# list = ["apple", "mango", "banana", "strawberry", "kiwi", "orange"]
# print(len(list))  # Output: 6

print(type(list))  # Output: <class 'list'>

thislist = list(("apple", "banana", "cherry"))  # note the double round-brackets
print(thislist)  # Output: ['apple', 'banana', 'cherry']



print(thislist[1])


thislist[1] = "blackcurrant"
print(thislist)  # Output: ['apple', 'blackcurrant', 'cherry']

thislist.append("orange")
print(thislist)  # Output: ['apple', 'blackcurrant', 'cherry





