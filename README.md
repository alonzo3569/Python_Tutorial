# Python
**My own Python tutorial files**

## Basic :
1. **help() :** `help(lst.count)`
2. **type() :** `type(a)`
3. **print() :**
4. **input() :** `a = input('PLZ guess: ')`

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
