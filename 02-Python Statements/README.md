# Chapter **2.**  Python Statements

## if statement:
```python
if x:
    if y:
        code-statement
elif:
    code-statement
else:
    another-code-statement
```

## for statement:
* **list:**
```python
list1 = [1,2,3,4,5,6,7,8,9,10]
for num in list1:
    print(num)
```
=> Output: `1\n 2\n 3\n...`

```python
list2 = [(2,4),(6,8),(10,12)]
for num in list2:
    print(num)
```
=> Output: `(2,4)\n (6,8)\n (10,12)\n...`

* **String:**
```python
for letter in 'This is a string.':
    print(letter)
```
=> Output: `T\n h\n i\n...`

* **Tuple:**
```python
tup = (1,2,3,4,5)

for t in tup:
    print(t)
```
=> Output: `1\n 2\n 3\n...`

* **Dictionary:**
  * **Items = key + value**
```python
d = {'k1':1,'k2':2,'k3':3}

for things in d:
    print(things)
```
=> Output: `k1\n k2\n k3\n...`

```python
for k,v in d.items():
    print(k)
    print(v)
```
=> Output: `k1\n 1\n k2\n 2\n...`

**Note: Unpack dictionary into list**
```python
list(d.keys())
```
=> Output: `['k1', 'k2', 'k3']`

```python
sorted(d.values())
```
=> Output: `[1, 2, 3]`

## while statement:
```python
while condition:
    code statements
else:
    final code statements
```

```python
while test: 
    code statement
    if test: 
        break  #break out of hte loop
    if test: 
        continue # skip this round and continue while loop
else:
```
