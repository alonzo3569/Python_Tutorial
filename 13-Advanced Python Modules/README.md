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
