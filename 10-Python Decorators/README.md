# Chapter **10.**  Python Decorators

## Python Decorators
```python
# Decorator function
def decorator(func):

    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func

# Test function
def test_function():
    print("This function is in need of a Decorator")
```
* __Wrap test_function using decorator function__
```python
# Reassign decorated test_function to a function variable 
func_after_decorated = decorator(test_function)

# Execute func_after_decorated
func_after_decorated()

# Output:
# > Code would be here, before executing the func
# > This function is in need of a Decorator
# > Code here will execute after the func()
```
* __Rewrite code above using "@" symbol__

```python
@decorator
def test_function():
    print("This function is in need of a Decorator")
```

* __Note :__
```python 
# Define function
def hello():
    return 'Hi Jose!'

if __name__ == "__main__":

    # Raw function. Can be used as variables
    hello           
    # > <function __main__.hello>

    # Execute variable 
    hello()   
    # > 'Hi Jose!'
```
