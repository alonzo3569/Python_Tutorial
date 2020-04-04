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
        #Animal.__init__(self)  # Add this line to inherit base class constructor
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

## **Multiple Inheritance :**

```python
class Hybrid(Gasoline, Electric):                # Inherit from Gasoline class and Electric class
    def __init__(self,engine='Hybrid',tank_cap=11,kWh_cap=5):
        Gasoline.__init__(self,engine,tank_cap)  # A more efficient way to inherit base class constructor
        Electric.__init__(self,engine,kWh_cap)
        
        
prius = Hybrid()
print(prius.tank)
print(prius.kWh)
```

## **Why do we use self?**
Python uses self to find the right set of attributes and methods to apply to an object.  
When we say:     `fido.speak()`  
1. Python first looks up the class belonging to fido (Dog)
2. Passes fido to the Dog.speak() method
3. `Dog.speak(self == fido)`  
* Thus, `fido.speak()`  ==   `Dog.speak(fido)` 
* It is shorter and more intuitive.

## **Method Resolution Order (MRO)**
Inheritance rules
```python
class A:
    num = 4
    
class B(A):
    pass

class C(A):
    num = 5
class D(B,C):
    pass
```
         A
       num=4
      /     \
     /       \
     B       C
    pass   num=5
     \       /
      \     /
         D
        pass
```python
D.num
# > 5  => Inherit from Class C
```

## **Super()**
* A shortcut for calling __base classes__
* Follows __Method Resolution Order__  
* __Simple Inheritance__
```python
class MyBaseClass:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
class MyDerivedClass(MyBaseClass):
    def __init__(self,x,y,z):
        super().__init__(x,y)   # super() represent base class "MyBaseClass"
        self.z = z
```
* __Multiple Inheritance__
```python
class A:
    def truth(self):
        return 'All numbers are even'
    
class B(A):
    pass

class C(A):
    def truth(self):
        return 'Some numbers are even'
        
class D(B,C):
    def truth(self,num):
        if num%2 == 0:
            return A.truth(self)
        else:
            return super().truth()  # super() follow MRO
                                    # super() represent Class C here
            
d = D()
d.truth(5)
# > 'Some numbers are even'
```
