# Chapter **3.**  Methods and Functions

## **Functions :**

**1. Declare :**
```python
def name_of_function(arg1,arg2):
    '''
    This is where the function's Document String (docstring) goes
    '''
    # Do stuff here
    # Return desired result
```
Note : [ Built-in Function in Python][0]

[0]: https://docs.python.org/2/library/functions.html

**2. Map function :** allows you to "map" a function to an iterable object.
```python
def square(num):
    return num**2
    
my_nums = [1,2,3,4,5]
list(map(square,my_nums))
```
=> Output: `[1, 4, 9, 16, 25]`

**3. Filter function :**
```python
def check_even(num):
    return num % 2 == 0 
    
nums = [0,1,2,3,4,5,6,7,8,9,10]
list(filter(check_even,nums))
```
=> Output: `[0, 2, 4, 6, 8, 10]`

## **Lambda expression :** allow us to create "anonymous" functions.
```python
list(map(lambda num: num ** 2, my_nums))
```
=> Output: `[1, 4, 9, 16, 25]`

```python
list(filter(lambda n: n % 2 == 0,nums))
```
=> Output: `[0, 2, 4, 6, 8, 10]`

```python
s='abc'
a = lambda s: s[::-1]
print(a(s))
```
=> Output: `cba`

**Note : ** lambda expressions works very well with certain non-built-in libraries, such as pandas library for data analysis.

## Python Scope  
* A variable is only available from **inside** the function it is created and is **not** available **outside** the function
```python
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()
```
Output => `300`

* If you operate with the same variable name inside and outside of a function, Python will treat them as **two separate variables**
```python
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)
```
Output => `200\n 300\n`

* If you need to create a global variable, but are stuck in the local scope, you can use the **global** keyword.
```python 
x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)
```
Output => `200`
**Note :** [Reference][1]
[1]: https://www.w3schools.com/python/python_scope.asp
