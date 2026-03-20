# Python OOP Primer

Object-Oriented Programming (OOP) is a programming paradigm that organizes code around "objects" rather than functions and logic. If you know Python basics (variables, loops, functions), this primer will help you understand OOP using simple analogies and short code examples.

## 1. Classes & Objects (Blueprint Analogy)

**Class** = A blueprint for creating objects.
**Object** = An actual instance created from that blueprint.

Think of a class like a cookie cutter: it defines the shape (properties and behaviors). Each cookie made from that cutter is an object.

Example:
```python
# Class definition (blueprint)
class Cookie:
    def __init__(self, shape, flavor):
        self.shape = shape
        self.flavor = flavor

# Creating objects (actual cookies)
cookie1 = Cookie("star", "chocolate")
cookie2 = Cookie("circle", "vanilla")

print(cookie1.shape)  # Output: star
print(cookie2.flavor) # Output: vanilla
```

## 2. The __init__ Method (Constructor)

`__init__` is a special method that runs automatically when you create a new object. It's where you set up the object's initial state.

Think of it as the setup crew that prepares a new house (object) with furniture (attributes) before you move in.

Example:
```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0  # Default value

my_car = Car("Toyota", "Corolla", 2023)
print(f"{my_car.brand} {my_car.model}")  # Toyota Corolla
```

## 3. Instance Variables vs Class Variables

**Instance variables** = Unique to each object (like each person's name)
**Class variables** = Shared by all objects of that class (like the species "human")

Example:
```python
class Dog:
    # Class variable (same for all dogs)
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        # Instance variables (different for each dog)
        self.name = name
        self.age = age

dog1 = Dog("Rex", 3)
dog2 = Dog("Bella", 5)

print(dog1.name)      # Rex (instance-specific)
print(dog2.name)      # Bella (instance-specific)
print(dog1.species)   # Canis familiaris (shared)
print(dog2.species)   # Canis familiaris (shared)
```

## 4. Methods (Actions Objects Can Do)

Methods are functions defined inside a class that describe what objects of that class can do.

Think of methods as skills: a "Dog" class might have "bark()" and "eat()" methods.

Example:
```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds!")

account = BankAccount("Alice", 100)
account.deposit(50)    # Deposited $50. New balance: $150
account.withdraw(30)   # Withdrew $30. New balance: $120
```

## 5. Inheritance (Parent-Child Relationship)

Inheritance allows a new class (child) to take on the properties and methods of an existing class (parent).

Think of it like genetics: a "Child" class inherits traits from a "Parent" class but can also have its own unique traits.

Example:
```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

# Child class inherits from Animal
class Cat(Animal):
    def speak(self):  # Override parent method
        print(f"{self.name} says meow")
    
    def purr(self):   # New method specific to Cat
        print(f"{self.name} is purring")

# Another child class
class Dog(Animal):
    def speak(self):  # Override parent method
        print(f"{self.name} says woof")

animal = Animal("Generic")
cat = Cat("Whiskers")
dog = Dog("Buddy")

animal.speak()  # Generic makes a sound
cat.speak()     # Whiskers says meow
cat.purr()      # Whiskers is purring
dog.speak()     # Buddy says woof
```

## 6. Encapsulation (Information Hiding)

Encapsulation means keeping some details private inside the object. In Python, we use a single underscore `_` (convention) or double underscore `__` (name mangling) to indicate private attributes.

Think of it like a vending machine: you use the public interface (buttons) to interact with it, but you don't need to know the internal workings.

Example:
```python
class TemperatureSensor:
    def __init__(self):
        self._temperature = 25  # "Protected" attribute (convention)
        self.__calibration = 0  # "Private" attribute (name mangling)
    
    def get_temperature(self):
        # Public method to access private data
        return self._temperature + self.__calibration
    
    def calibrate(self, adjustment):
        # Control how the private attribute is modified
        if -5 <= adjustment <= 5:
            self.__calibration = adjustment
        else:
            print("Calibration adjustment out of range")

sensor = TemperatureSensor()
print(sensor.get_temperature())  # 25
sensor.calibrate(2)
print(sensor.get_temperature())  # 27

# Can still access (Python doesn't enforce strict privacy)
print(sensor._temperature)       # 25 (but you shouldn't)
# print(sensor.__calibration)    # Would cause AttributeError
```

## 7. Putting It All Together

Example: A simple e-commerce system demonstrating multiple OOP concepts:

```python
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def apply_discount(self, percent):
        discount = self.price * (percent / 100)
        return self.price - discount

class Electronics(Product):
    def __init__(self, name, price, stock, warranty_years):
        super().__init__(name, price, stock)  # Call parent __init__
        self.warranty_years = warranty_years
    
    def display_info(self):
        return f"{self.name} - ${self.price} ({self.warranty_years}yr warranty)"

class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, product, quantity=1):
        if product.stock >= quantity:
            self.items.append((product, quantity))
            product.stock -= quantity
            print(f"Added {quantity} {product.name}(s) to cart")
        else:
            print(f"Insufficient stock for {product.name}")
    
    def total_cost(self):
        return sum(product.price * quantity for product, quantity in self.items)

# Usage
laptop = Electronics("Gaming Laptop", 1200, 10, 2)
phone = Electronics("Smartphone", 800, 15, 1)

cart = ShoppingCart()
cart.add_item(laptop, 1)
cart.add_item(phone, 2)

print(f"Total: ${cart.total_cost()}")
print(f"Laptop stock remaining: {laptop.stock}")
```

## Quick Reference

| Concept | Analogy | Python Syntax |
|---------|---------|---------------|
| **Class** | Blueprint | `class ClassName:` |
| **Object** | Actual thing | `obj = ClassName()` |
| **__init__** | Setup crew | `def __init__(self, ...):` |
| **Instance variable** | Personal trait | `self.variable = value` |
| **Class variable** | Shared trait | Inside class: `variable = value` |
| **Method** | Skill/action | `def method(self, ...):` |
| **Inheritance** | Parent-child | `class Child(Parent):` |
| **Encapsulation** | Private box | `_variable` or `__variable` |

## Common Pitfalls to Avoid

1. **Forgetting `self`**: Instance methods must have `self` as first parameter
2. **Confusing class vs instance**: Class variables are shared, instance variables are unique
3. **Overcomplicating**: Start simple, add complexity only when needed
4. **Inheritance abuse**: Don't use inheritance just to reuse code if there's no "is-a" relationship

## Next Steps

After mastering these basics:
1. Practice by creating your own classes for real-world concepts (Book, Student, Restaurant, etc.)
2. Learn about **polymorphism** (different objects responding to the same method)
3. Explore **magic methods** like `__str__`, `__len__`, etc.
4. Study **composition** (building complex objects from simpler ones) as an alternative to inheritance

Remember: OOP is a tool to organize code. Use it when it makes your code clearer, not just because it's "the right way."