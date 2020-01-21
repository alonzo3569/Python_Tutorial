# Chapter **7.**  Errors and Exception Handling

## Errors and Exception Handling

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
