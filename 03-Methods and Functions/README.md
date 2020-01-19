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

## **Lambda expression :**  
* Lambda expression allow us to create "anonymous" functions.
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

**Note :** lambda expressions works very well with certain non-built-in libraries, such as pandas library for data analysis.

## Python Scope  
* A variable created **outside** of a function is **global** and can be used by anyone.
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

Note : [Ref][1]

* Conclusion: 
    * In python, What all matters is whether the variable is **inside** or **outside** the **function**. 
    * In C++, we can tell the variable's scope by curly braces{}. However, in python, we can tell by 
    * Only **functions** will affect, statements such as `While, if, for...` won't affect. For example,
    ```python 
    def get_positive_int(prompt):
        While True:
            n = int(input("Get int: "))
            if n > 0:
                break
        return n            # C++ won't allow n be used outside while{}, but python can.
                            # Since n can be used inside get_positive_int() function.  
    ```

[1]: https://www.w3schools.com/python/python_scope.asp

## *args and **kwargs

* *args: it allows for an arbitrary number of inputs **(Tuples)**
```python

def myfunc(*args):
    #print(args)    # output => (40, 60, 20)
    return sum(args)*.05

myfunc(40,60,20)
myfunc(10,10,10,10)
```
Output => `6\n 2\n`  

* **kwargs: it handles arbitrary numbers of key/value pairs and  builds a dictionary **(Dictionary)**
```python
def myfunc(**kwargs):
    if 'fruit' in kwargs:
        #print(kwargs)    # output => {'fruit': 'pineapple'}
        print(f"My favorite fruit is {kwargs['fruit']}") 
    else:
        print("I don't like fruit")
        
myfunc(fruit='pineapple') # key = fruit, value = 'pineapple'
```
Output => `My favorite fruit is pineapple`  

* *args and **kwargs combined
```python
def myfunc(*args, **kwargs):
    if 'fruit' and 'juice' in kwargs:
        print()
        print(f"I like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
        print(f"May I have some {kwargs['juice']} juice?")
    else:
        pass
        
myfunc('eggs','spam',fruit='cherries',juice='orange')
```
**Note :** In this case, args = ('eggs', 'spam'), kwargs = {'fruit': 'cherries', 'juice': 'orange'}  
Output => `I like eggs and spam and my favorite fruit is cherries\n May I have some orange juice?`  

