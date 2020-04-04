# Chapter **14.**  Advanced Python Objects and Data Structures

## Advanced Numbers
```python
# Hexadecimal 
hex(512)
# > '0xf6'

# Binary (for positive numbers)
bin(1234)
# > '0b10011010010'

# Binary (for negetive numbers)
bin((-7).to_bytes(1, 'big', signed=True)[0])
# > '0b11111001' => correct 2's complement for -7

# Absolute value
abs(-3.14)
# > 3.14

# Round 
round(3.1415926535,2)
# > 3.14
```

## Advanced Strings 

```python

# String for testing
s = 'hello world'

# Capitalize first word in string
s.capitalize()
# > 'Hello world'

# Capitalize every character in a string
s.upper()
'hello world'

# Returns the number of occurrences
s.count('o')
# > 2

# Returns the starting index position of the first occurence
s.find('o') 

# Formatting
s.center(20,'z')  
# > 'zzzzhello worldzzzzz'
# 20 => total length of the string 
'hello\thi'.expandtabs()
# > 'hello   hi'


# Is check methods (Returns True or False)
# Test string
s = 'hello'

# Is Method
s.isalnum()
s.isalpha()
s.islower()
s.isspace()
s.istitle()
s.isupper()
s.endswith('o')

# Split
s.split('e')
# > ['h', 'llo']

# Partition : divide string into 3 parts 
s.partition('l')
# > ('he', 'l', 'lo')
# (part before seperator, seperator, part after seperator)


```
* __Note :__
  * Strings are __immutable__
  * `s = s.upper()` to change original string

## Advanced Lists

```python

# Setup a list
list1 = [1,2,3]

# Append
list1.append(4)

# Count
# Returns the number of times an element occurs
list1.count(10)
# > 0

# Append more than one element at a time
x = [1, 2, 3]
x.extend([4, 5])
print(x)
# > [1, 2, 3, 4, 5]


# Index of the element 
list1.index(2)
# > 1

# Insert
list1.insert(2,'inserted')
# > [1, 2, 'inserted', 3, 4, 5]
# Place a letter at the index 2
# insert(index,object)

# Pop
ele = list1.pop(1)  
ele
# > 2
# pop the second element and give it to ele
# pop(index), default = last element


# Remove
list1.remove('inserted')
list1
# > [1, 3, 4, 5]
# Remove "the first" {value} in the list
# remove(value)

# Reverse
list2 = [1, 2, 4, 3]
list2.reverse()
list2
# > [3, 4, 2, 1]


# Sort
list2.sort(reverse=True)
list2
# > [4, 3, 2, 1]
``` 




## Advanced Sets 

```python
# Construct a set object
s = set()

# Add elements
s.add(1)

# Remove all element
s.clear()

# Copy
s = {1,2,3}
sc = s.copy()

# Difference
sc.add(4)
s.difference(sc)
# > {4}

# Difference update
# 把 s1 中有而 s2 裡沒有的 給s1
s1 = {1,2,3}
s2 = {1,4,5}
s1.difference_update(s2)
s1
# > {2, 3}


# Remove an element from set
s = {1, 2, 3}
s.discard(2)
# 2: "value" not index

# Common between two sets
s1 = {1,2,3}
s2 = {1,2,4}
s1.intersection(s2)
# > {1, 2}

# Intersection_update 
# Makes an set equals to intersection of two sets
s1.intersection_update(s2) 
s1
# > {1, 2}

# Return True when they have no intersection
s1.isdisjoint(s2)

# Subset
s1 = {1, 2}
s2 = {1, 2, 4}
s1.issubset(s2)
# > True

# Superset
s2.issuperset(s1)3
# > True


# The difference of two sets
# All elements that are in exactly one of the sets
s1.symmetric_difference(s2)
# > {4}

# Union (聯集)
s1.union(s2)
# > {1, 2, 4}

# Update (取聯集後 更新本身)
s1.update(s2)
# > {1, 2, 4}
```

## Advanced Dictionaries
```python

# Construct a dict object
d = {'k1':1,'k2':2}

# View object in dicts 
key_view = d.keys()

# Add new key:value pair in dicts
d['k3'] = 3

# Dict view object update keys automatically
key_view
# > dict_keys(['k1', 'k2', 'k3'])

```

