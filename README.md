# Python
**My own Python tutorial files**

## Basic :
1. **help() :** `help(lst.count)`
2. **type() :** `type(a)`
3. **print() :**


There are three ways to perform string formatting:

 * %
 * .format().
 * Python 3.6, f-strings.

    1. **_print ( f ' ' )_**   
    `name = 'jose'`  
    `print(f'Hello, his name is {name}')` -> `Hello, his name is jose`  
    `num = 23.45`  
    `print(f"My 10 character, four decimal number is:{num:10.4f}")` -> `My 10 character, four decimal number is:   23.4500`  
    2. **_print ( " { r : width . precision } ". format ( r = result ) )_**<br/>
    `print("The result was {r:3.10}".format(r=result))` -> `The result was 0.1287001287`  
    `print("The result was {r:1.3f}".format(r=result))` -> `The result was 0.129`  
    `print("The result was {r:10.3f}".format(r=result))` -> `The result was      0.129`  
    `Width means the white space before the numbers`  
    3. **"%s" & "%r" , "str()" & "repr()"**  
    `print('I once caught a fish %s.' %'this \tbig')` -> `I once caught a fish this 	big.`  
    `print('I once caught a fish %r.' %'this \tbig')` -> `I once caught a fish 'this \tbig'.`   
    _**%r** and **repr()** deliver the string representation of the object, including quotation marks and any escape characters._  
    
    4. **For more String Formatting details, check out Ch0 03.ipynb or visit [**here**][0]!**
        
    [0]: https://docs.python.org/3/reference/lexical_analysis.html#f-strings
    
## Useful Operators
1. **range() :** **Generator**
```python
range(0,11)
```
=> Output: `range(0, 11)`

```python
list(range(0,11,2))
```
=> Output: `[0, 2, 4, 6, 8, 10]`

2. **enumerate() :**  Create a counter(starts from zero) for each object in a list.
```python
for i,letter in enumerate('abcde'):
    print("At index {} the letter is {}".format(i,letter))
```
=> Output: `At index 0 the letter is a\n At index 1 the letter is b\n...`

```python
list(enumerate('abcde'))
```
=> Output: `[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]`

3. **zip() :** **Generator**
```python
mylist1 = [1,2,3,4,5] #mylist1 = [1,2,3,4,5,6,7,8,9,10] also works
mylist2 = ['a','b','c','d','e']
print(list(zip(mylist1,mylist2)))
```
=> Output: `[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]`

4. **input() :** `a = input('PLZ input: ')` **Note : return type 'str'**

5. **in** :
```python
d = {'mykey':245}

'mykey' in d.keys()
```
=> Output: `True` **Note: Don't forget '' for mykey**

```python
'x' in [1,2,3]
```
=> Output: `False`

6. **min() & max()** :
```python 
mylist = [10,20,30,40,100]
min(mylist)
max(mylist)
```
=> Output: `10\n 100\n`

7. **random library**
    * **shuffle :** Will effect the list passed. Won't return anything.
    ```python
    from random import shuffle
    shuffle(mylist)
    print(mylist)
    ```
    => Output: `[40, 10, 100, 30, 20]`  
    </br>
    * **randint :** Return random integer in range [a, b], including both end points.
    ```python
    from random import randint
    print(randint(0,100))
    ```
    => Output: 91
    
8. **join()** : Allows you to join together **strings in a list** with some connector string.
```python
"--".join(['a','b','c'])
```
Output => `'a--b--c'`
    
