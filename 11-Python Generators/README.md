# Chapter **11.**  Python Generators

## Python Generators

* __Yield or Return ?__  
If the output has the potential of taking up a large amount of memory and you only intend to iterate through it, you would want to use a generator. 

```python
# Generator function for the cube of numbers (power of 3)
def gencubes(n):
    for num in range(n):
        yield num**3

if __name__ == "__main__":
    for x in gencubes(10):
        print(x)
```

* __Built-in functions next() & iter() :__ <br></br>
  * __Next() :__
  ```python
  # Generator
  def simple_gen():
      for x in range(3):
          yield x

  # Assign simple_gen 
  g = simple_gen()  # g is a "generator object"        

  # Usage
  print(next(g))
  # > 0
  print(next(g))
  # > 1
  print(next(g))
  # > 2
  ```
  
  * __Iter() :__
  ```python
  # Create string
  s = 'hello'

  #Iterate over string
  for let in s:   
      print(let)    
  # > h   
  # > e
  # > l
  # > l
  # > o

  # Test
  next(s)
  # > TypeError! >> String are "iterable" but not "iterator" !!

  # Use iter() function to let string become "iterator"
  s = iter(s)  # let string to be an iterator

  # Test
  next(s)
  # > h
  next(s)
  # > e

  print(type(s))
  # > <class 'str_iterator'>
  ```
