# Chapter **10.**  Advanced Python Modules

## Advanced Python Modules
* __Collections Module :__
  * __Counter :__
  ```python
  # Import module
  from collections import Counter
  
  # Counter() with lists
  lst = [1,2,2,2,2,3,3,3,1,2,1,12,3,2,32,1,21,1,223,1]
  Counter(lst)
  # > Counter({1: 6, 2: 6, 3: 4, 12: 1, 21: 1, 32: 1, 223: 1})
  
  # Counter with strings
  Counter('aabsbsbsbhshhbbsbs')
  # > Counter({'a': 2, 'b': 7, 'h': 3, 's': 6})
  
  # Methods with Counter()
  c = Counter(lst)
  c.most_common(2)
  # > [(1, 6),(2, 6)]
  
  # More method in Counter
  help(Counter)
  dir(Counter)
  ```

  * __defaultdict :__  
  A defaultdict will never raise a KeyError. Any key that does not exist gets the value returned by the default factory.
  ```python
  # Import module
  from collections import defaultdict
  
  # Create defaultdict object
  # d  = defaultdict(factory_function)
  # factory_function可以是list, set, str 或 function
  # 當字典中的key不存在時，返回的是factory_function的預設值，
  # Ex. list返回[]，str返回空字串''，int返回0。
  d = defaultdict(lambda: 0)
  
  # Test
  d['one'] 
  # d 中無'one'這個 key, 所以用 factory_functiont 創造'one'這個key並給予初始值 0 (由 lamda function)
  # > 0
  
  # More method in Counter
  help(Counter)
  dir(Counter)
  ```
  
  * __OrderedDict :__  
  An OrderedDict is a dictionary subclass that remembers the order in which its contents are added.  
    * 一般 dictionary 輸出時"不一定"按照輸入順序, 但 OrderedDict 會
    ```python
    # Import module
    from collections import OrderedDict

    # Create OrderedDict object
    d = OrderedDict()

    d['a'] = 'A'
    d['b'] = 'B'
    d['c'] = 'C'
    d['d'] = 'D'
    d['e'] = 'E'

    for k, v in d.items():
        print(k, v)
    # > a A
    # > b B
    # > c C
    # > d D
    # > e E
    ```
    * Equality with an Ordered Dictionary
    ```python
    print('Dictionaries are equal?')

    d1 = {}
    d1['a'] = 'A'
    d1['b'] = 'B'

    d2 = {}
    d2['b'] = 'B'
    d2['a'] = 'A'

    print(d1==d2)
    # > True 
    # 若為一般 Ordered Dictionary, 則 False 
    ```
    
  * __namedtuple :__   
  A very quick way of creating a new object/class type with some attribute fields.
  ```python
  # Import module
  from collections import namedtuple
  
  # Create object
  sam = Dog(age=2,breed='Lab',name='Sammy')
  
  # Usage
  sam.age
  # > 2 
  sam.breed
  # > 'Lab'
  ```

* __datetime Module :__
```python
import datetime

# Setup a datetime object
t = datetime.time(4, 20, 1)

# Let's show the different components
print(t)
print('hour  :', t.hour)
print('minute:', t.minute)
print('second:', t.second)
print('microsecond:', t.microsecond)
# > 04:20:01
# > hour  : 4
# > minute: 20
# > second: 1
# > microsecond: 0

# Setup a datetime object
today = datetime.date.today()
print(today)
print('ctime:', today.ctime())
print('tuple:', today.timetuple())
print('ordinal:', today.toordinal())
print('Year :', today.year)
print('Month:', today.month)
print('Day  :', today.day)
# > 2018-02-05
# > ctime: Mon Feb  5 00:00:00 2018
# > tuple: time.struct_time(tm_year=2018, tm_mon=2, tm_mday=5, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=36, tm_isdst=-1)
# > ordinal: 736730
# > Year : 2018
# > Month: 2
# > Day  : 5

# Arithmetic
d1 = datetime.date(2015, 3, 11)
d2 = d1.replace(year=1990)

# Calculate time delta
d1-d2
# > datetime.timedelta(9131)
```

* __pbd Module :__
```python
# Import module
import pdb

x = [1,3,4]
y = 2
z = 3

result = y + z
print(result)

# Set a trace using Python Debugger
# The program will stop here and wait for user input 
# This is when user can test all the variables in the program
pdb.set_trace()

result2 = y+x
print(result2)

# Note : Don't to use pdb in an iPython Notebook.
```

* __timeit Module :__
```python
# Import module
import timeit

# For loop (number=10000 : run this code for 10000 times)
timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
# > 0.21865416520477374

# List comprehension
timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
# > 0.19484614421698643

# Map()
timeit.timeit('"-".join(map(str, range(100)))', number=10000)
# > 0.15291817337139246

# This only works in jupyter notebooks
%timeit "-".join(str(n) for n in range(100))
# > 20.4 µs ± 269 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
```


* __Regular expressions Module re:__  
  * One of the most common uses for the re module is for finding patterns in text.
```python
import re

# List of patterns to search for
pattern = 'term1'

# Text to parse
text = 'This is a string with term1, but it does not have the other term.'

match = re.search(pattern,text)

type(match)
# > _sre.SRE_Match  => return a "Match" object

# Show start of match
# help(match.start) =>  Return index of the start of the matched string.
match.start()  
# > 22
# Show end
match.end()
# > 27 
# 'term1' has 5 character, thus 27-22 = 5 

# Split
re.split('@', phrase) # help(re.split)

# Returns a list of all matches
re.findall('match','test phrase match is in middle')
# > ['match'] 
# help(re.findall) 
# re.search only find the first matched pattern
```
  * __re pattern syntax :__
  1. __* :__ " * " 前的字元可出現0次(沒有*前這個字元)或多次
  2. __+ :__ " + " 前的字元要至少出現1次或多次
  3. __? :__ " ? " 前只能出現0次或1次
  4. __{} :__ " {} " 內可決定 "{}" 前一個字元的出現次數 ex.{2}
  5. __{,} :__  " {} " 內可決定 "{}" 前一個字元的出現次數範圍 ex. {2,3} or {3,}
  6. __[] :__ " [] " 內可決定字元範圍 ex. [a-zA-Z]
  7. __^ :__ 
    * "^" 在 " [] " 內: 代表否定 ex. [^z] 代表字元Z不取,其他都取  
    * "^" 在 " [] " 外: 代表取以 "^" 後字元為開頭的字串  
  * __escape code :__  
  <table>
  <colgroup>
  <col width="14%" />
  <col width="86%" />
  </colgroup>
  <thead>
  <tr>
  <th>Code</th>
  <th>Meaning</th>
  </tr>
  </thead>
  <tbody valign="top">
  <tr class="row-even"><td><tt class="docutils literal"><span class="pre">\d</span></tt></td>
  <td>a digit</td>
  </tr>
  <tr class="row-odd"><td><tt class="docutils literal"><span class="pre">\D</span></tt></td>
  <td>a non-digit</td>
  </tr>
  <tr class="row-even"><td><tt class="docutils literal"><span class="pre">\s</span></tt></td>
  <td>whitespace (tab, space, newline, etc.)</td>
  </tr>
  <tr class="row-odd"><td><tt class="docutils literal"><span class="pre">\S</span></tt></td>
  <td>non-whitespace</td>
  </tr>
  <tr class="row-even"><td><tt class="docutils literal"><span class="pre">\w</span></tt></td>
  <td>alphanumeric</td>
  </tr>
  <tr class="row-odd"><td><tt class="docutils literal"><span class="pre">\W</span></tt></td>
  <td>non-alphanumeric</td>
  </tr>
  </tbody>
  </table>
  
  * __Examples :__
  ```python
  # Function for testing regular expression patterns
  def multi_re_find(patterns,phrase):
    '''
    Takes in a list of regex patterns
    Prints a list of all matches
    '''
    for pattern in patterns:
        print('Searching the phrase using the re check: %r' %(pattern))
        print(re.findall(pattern,phrase))
        print('\n')
        
  # Testing re pattern syntax    
  test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

  test_patterns = [ 'sd*' ]
  multi_re_find(test_patterns,test_phrase)
  # > Searching the phrase using the re check: 'sd*'
  # > ['sd', 'sd', 's', 's', 'sddd', 'sddd', 'sddd', 'sd', 's', 's', 's', 's', 's', 's', 'sdddd']
  
  # Testing exclusion "[^]"
  test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
  re.findall('[^!.? ]+',test_phrase)
  # > ['This',
  # > 'is',
  # > 'a',
  # > 'string',
  # > 'But',
  # > 'it', ....
  
  # Testing escape code
  test_phrase = 'This is a string with some numbers 1233 and a symbol #hashtag'

  # 'r' 標明這是這則表達式, 而非print中的 '/n'
  test_patterns=[ r'\d+', # sequence of digits ]

  multi_re_find(test_patterns,test_phrase)
  # > Searching the phrase using the re check: '\\d+'
  # > ['1233']
  ```
  * __For more information, please checkout jupyter notebook!__
  * __Reference :__
    * [__Python documentation__][0]
    * [__Vbird Regular Expression__][0]

[0]: https://docs.python.org/3/library/re.html#regular-expression-syntax
[1]: http://linux.vbird.org/linux_basic/0330regularex.php

* __StringIO Module :__ 
Create a in-memory file-like objects within your program that Python treats the same way.  
Mostly used in reading web content.
```python
# Import module
import io

# Arbitrary String
message = 'This is just a normal string.'

# Use StringIO method to set as file object
f = io.StringIO(message)

f.read()
# > 'This is just a normal string.'
f.write(' Second line written to file like object')

# Reset cursor just like you would a file
f.seek(0)

# Read again
f.read()
# > 'This is just a normal string. Second line written to file like object'

# Close the object when contents are no longer needed
f.close()
```
