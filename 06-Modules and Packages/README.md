# Chapter **6.**  Modules and Packages

## Pip Install and PyPi
* __PyPi :__ A repository for open-source 3rd-party Python packages.
* __pip :__ A simple way to download packages **from Pypi** at your command line. 
* __Install command :__
  1. `pip install openpyxl(library name)` 
  2. `import openpyxl`
* __Google search :__ `python package for ... ex.(pdf, excel...)`

## Modules and Packages
* __Modules :__ Modules are just .py scripts which you import in another .py script.
* __Packages :__ Packages are collection of modules.
* __.py >> module >> package__
* To create a package(A folder full of modules), create a blank file "__ init __.py" (2 underscore) inside the folder.
* ```python
  # Import
  from mymodule import my_func  # You can just import one specific function or the intire script
  from MyMainPackage import some_main_scrpit  # some_main_scrpit.py module is inside the MyMainPackage folder(package)
  from MyMainPackage.SubPackage import mysubscrpit # mysubscrpit.py module path: MyMainPackage/SubPackage/mysubscrpit.py
  
  # Function call
  my_func()
  some_main_script.report_main() # call function in some_main_script.py module
  my_subscript.sub_report()
  ```
* __dir() :__ look for all the functions in the module. ex. `print(dir(math))`
* __help() :__ 
  ```python
  Help on built-in function ceil in module math:

    ceil(...)
    ceil(x)
    
    Return the ceiling of x as an Integral.
    This is the smallest integer >= x.
  ```
 
## Concept of __ name __ and "__ main __"
* If the .py file is executed directly, the so called `if __name__ == "__main__":` part will be executed, which means every line will be executed.
* If the .py file is **NOT** executed directly but imported, everything other than `if __name__ == "__main__":` part will be executed.
* Usage: 
  ```python 
  
      if __name__ == "__main__":
        # Do things here
    else:
        # Do things here
  ```
* Example:

```python
    # file one.py
    def func():
        print("func() in one.py")

    print("top-level in one.py")

    if __name__ == "__main__":
        print("one.py is being run directly")
    else:
        print("one.py is being imported into another module")
```

```python
    # file two.py
    import one

    print("top-level in two.py")
    one.func()

    if __name__ == "__main__":
        print("two.py is being run directly")
    else:
        print("two.py is being imported into another module")

```

* __Execute : python two.py__
```python
  top-level in one.py                               # The interpreter will execute line by line. Thus, the first line in two.py is "import one"
                                                    # Hence, print("top-level in one.py") will be executed first
  one.py is being imported into another module      # Else part of one.py
  top-level in two.py
  func() in one.py                                  # execute line by line
  two.py is being run directly
```
