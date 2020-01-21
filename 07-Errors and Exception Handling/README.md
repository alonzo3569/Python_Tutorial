# Chapter **7.**  Errors and Exception Handling

## Errors and Exception Handling
```python
def askint():
    while True:
        try:
            val = int(input("Please enter an integer: "))
        except:
            print("Looks like you did not enter an integer!")
            continue
        except IOError: # Python built-in error type
            # This will only check for an IOError exception and then execute this print statement
            print("Error: Could not find file or read data")
        else:
            # If no error occurs, this will be implemented
            print("Yep that's an integer!")
            break
        finally:
            # Finally will be implemented whether there is an error or not
            print("Finally, I executed!")
```

## Pylint
* __Installation :__ `python pip install pylint`
* __Execution :__ `pylint simple.py`
* __Common styling issues :__
  * __Final newline missing (missing-final-newline) :__ It would like to see an extra newline at the end.
  * __Missing module docstring (missing-docstring) :__ Modules and function definitions should have descriptive docstrings.
  * __Invalid constant name "a" (invalid-name) :__ Single characters are a poor choice for variable names.
  * __Undefined variable 'B' (undefined-variable) :__ A variable called before assignment.
  * __Found indentation woth tabs instead of spaces (mixed-indenatation) :__ Change tab to four spaces.
* __Standard Styling Example :__  
  simple.py
  ```python
  """
  A very simple script.                    # Docstrings for module
  """

  def myfunc():
      """
      An extremely simple function.       # Docstrings for function
      """
      first = 1
      second = 2
      print(first)
      print(second)
    
  myfunc()
                                         # Extra newline at the end
  ```
  
## Unittest
Unittest lets you write your own test programs. The goal is to send a specific set of data to your program, and analyze the returned results against an expected result.

* __cap.py__
 ```python
 def cap_text(text):
     return text.capitalize()                     # Only capitalize the first character of the sentence
                                                  # Use title() if you want to capitalize 1st char in every word
 ```
* __test_cap.py__
 ```python
 import unittest
 import cap

 class TestCap(unittest.TestCase):
    
     def test_one_word(self):
         text = 'python'
         result = cap.cap_text(text)
         self.assertEqual(result, 'Python')
         
     def test_multiple_words(self):
         text = 'monty python'
         result = cap.cap_text(text)                # Return Monty python
         self.assertEqual(result, 'Monty Python')
         
 if __name__ == '__main__':
     unittest.main()
 ```
* __Output__  
  * **Failed cuz Monty python != Monty Python**
  ```
  F.
  ======================================================================
  FAIL: test_multiple_words (__main__.TestCap)
  ----------------------------------------------------------------------
  Traceback (most recent call last):
    File "test_cap.py", line 14, in test_multiple_words
      self.assertEqual(result, 'Monty Python')
  AssertionError: 'Monty python' != 'Monty Python'
  - Monty python
  ?       ^
  + Monty Python
  ?       ^


  ----------------------------------------------------------------------
  Ran 2 tests in 0.000s

  FAILED (failures=1)
  ```
* __cap.py__
  * __Change cpitalize() to title()__
  * **Success cuz Monty Python = Monty Python**
  ```python
  def cap_text(text):
      return text.title()  # replace .capitalize() with .title()
  ```
* __Output__  
  ```
  ..
  ----------------------------------------------------------------------
  Ran 2 tests in 0.000s

  OK
  ```
