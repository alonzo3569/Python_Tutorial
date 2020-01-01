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
 * bool (for Boolean True/False)

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
