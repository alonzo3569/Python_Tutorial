# Chapter **0.**  Python Data Structure Basics

## **Number Basic Arithmetic :**  
 * Floor Division : `7//4 = 1`
 * Modulo :  `7%4 = 3`
 * Powers : `2**3 = 8`
 
## Data Type in Python :
 * int (for integer)
 * float
 * str (for string)
 * list
 * tuple
 * dict (for dictionary)
 * set
 * bool (for Boolean True/False/None)

## Data Structure in Python
* **Strings**
* **Lists :**
    + Objects retrieved by location.  
    + Ordered sequence can be indexed or sliced.  
* **Dictionaries :**
    + Objects retrieved by key.
    + Unordered and cannot be sorted.
* **Tuples :**
    + Similar to list, but **immutable**.
    + Cannot append items in tuple!
* **Sets :**
    + **Unordered** collection of **Unique** elements
    + 'set' object **does not support indexing**

## Strings :
 * Declare : `'hello'` **or** `"String built with double quotes"`
 * Method  : 
     + len() -> Counts all of the characters in the string, including spaces and punctuation.
     + upper()
     + split() ex. `s.split() -> ['Hello', 'World']   s.split('W') ->  ['Hello', 'orld']`
     + len()
 * Access  :  assume s = 'Hello World'
     + `s[0]` -> `H`
     + `s[-1]` -> `d`
     + `s[1:]` -> `ello World`
     + `s[:3]` -> `Hel`
     + `s[::2]` -> `HloWrd`
     + `s[::-1]` -> `dlroW olleH`  

## Lists :
 * Declare : `my_list = ['A string',23,100.232,'o']`  
 * Method  : 
     + len() ex. `len(my_list)` -> `4`
     + append()
     + pop() ex. `popped_item = my_list.pop()` 
     + sort() -> numbers it will go ascending or alphabetical order
     + reverse()
 * Access  :
     + `my_list[0]` -> `'A string'`
     + `my_list[:3]` -> `'A string',23,100.232`
     + `my_list = my_list + ['new item']` -> `['A string',23,100.232,'o','new item']`
     + `my_list * 2` -> `['A string',23,100.232,'o','new item','A string',23,100.232,'o','new item']`
     
## Dictionaries :
 * Declare : 
     + `my_dict = {'key1':'value1','key2':'value2'}`  
     + `my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}`  
     + `d = {}`
 * Method  : 
     + keys() -> return a list of all keys
     + values() -> return a list of all values
     + items() -> return tuples of all items  ex. `my_dict.items()` -> `dict_items([('key1', 1), ('key2', 2)])`
 * Access  :
     + `my_dict['key2']`
     + `my_dict['key1'] = my_dict['key1'] - 123`
     + `my_dict['key1'] -= 123`
     + `d['animal'] = 'Dog'`
     
## Tuples :
 * Declare :
     + `t = (1,2,3)`
     + `t = ('one',2)`
 * Method  :
     + len()
     + index() -> enter a value and return the index  ex. `t.index('one')` -> `0`
     + count() -> count the number of times a value appears
 * Access  :
     + `t[0]`
     + `t[-1]`
 
 ## Sets :
 * Declare : Construct them by using the set() function.
     + `x = set()`
     + `x = {1,2,3}` -> `type(x)` -> `set`
 * Method  :
     + add()
     + set() ex. `list1 = [1,1,2,2]` -> `set(list1)` -> `{1,2}`
 * Access  :
     + Use _**for** a **in** x_ access items in set
 
  ## Files :
