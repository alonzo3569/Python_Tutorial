# Chapter **5.**  Object Oriented Programming

## **Class :**  
```python
class Circle:
    # Class Object Attribute
    pi = 3.14

    # Class Circle Constructor (radius default is 1)
    def __init__(self, myradius=1):                   # Usually we'll just use 'radius' instead of 'myradius'
        self.radius = myradius 
        self.area = radius * radius * Circle.pi       # U can use both 'self.pi' or 'Circle.pi'

    # Method for resetting Radius
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi

    # Method for getting Circumference
    def getCircumference(self):
        return self.radius * self.pi * 2


c = Circle()

print('Radius is: ',c.radius)
print('Area is: ',c.area)
print('Circumference is: ',c.getCircumference())
```
Output => `Radius is:  1\n  Area is:  3.14\n Circumference is:  6.28`

## **Inheritance :**  

```python
class Animal:
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):              # <= this means class Dog is a sub class of Animal
    def __init__(self):
        #Animal.__init__(self)
        print("Dog created")

    def whoAmI(self):           # If methods have the same name, derived class will overwrite base class
        print("Dog")            # If they have different names, it will inherit

    def bark(self):
        print("Woof!")
        
d = Dog()                        # Overwrite
d.whoAmI()                       # Overwrite
d.eat()                          # inherit
```
Output => `Dog create\n  Dog\n  Eating\n`

## **Polymorphism :**  
```python
class Animal:
    def __init__(self, name):    # Constructor of the class
        self.name = name

    def speak(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")  # If someone create an Animal Object and call speak, a error will occur


class Dog(Animal):
    
    def speak(self):
        return self.name+' says Woof!'
    
class Cat(Animal):

    def speak(self):
        return self.name+' says Meow!'
    
fido = Dog('Fido')
isis = Cat('Isis')

print(fido.speak())
print(isis.speak())
```
Output => `Fido says Woof!\n  Isis says Meow!\n`

## **Special methods :**  
Special methods allow us to use Python specific functions on objects created through our class.

```python
class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):            #return the string representation of an object, print() will ask for str representation
        return "Title: %s, author: %s, pages: %s" %(self.title, self.author, self.pages)

    def __len__(self):            # for len() function
        return self.pages

    def __del__(self):            # for del() function, del() allows us to delete objects in memory
        print("A book is destroyed")
```

```python
book = Book("Python Rocks!", "Jose Portilla", 159)

#Special Methods
print(book)
print(len(book))
del book
```
Output => `A book is created\n  Title: Python Rocks!, author: Jose Portilla, pages: 159\n  159\n  A book is destroyed`
