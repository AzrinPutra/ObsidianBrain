# Python OOP Primer

This primer is designed for individuals familiar with Python basics but new to Object-Oriented Programming (OOP). We'll cover fundamental OOP concepts with simple analogies and practical Python code examples.

## 1. Classes: The Blueprint

Imagine you want to build many houses. Instead of drawing up plans for each house from scratch, you create a general blueprint. In OOP, a **class** is like that blueprint. It's a template for creating objects, defining their common characteristics (data) and behaviors (functions).

```python
class Dog:
    # A blueprint for creating dog objects
    pass
```

## 2. Objects: The Instance

If a class is the blueprint, an **object** is the actual house built from that blueprint. It's an individual instance of a class, with its own unique data based on the blueprint's specifications.

```python
# Creating objects (instances) from the Dog class
dog1 = Dog()
dog2 = Dog()

print(dog1) # Output will show a unique object in memory
print(dog2) # Another unique object
```

## 3. `__init__()`: The Constructor

When you build a house, you often want to set some initial properties, like the number of rooms or its address. In Python, the `__init__` method is a special function called a **constructor**. It gets automatically called when you create a new object from a class, allowing you to initialize the object's attributes.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name    # instance variable
        self.breed = breed  # instance variable
        print(f"A new dog named {self.name} is born!")

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Lucy", "Beagle")

print(f"{dog1.name} is a {dog1.breed}")
```

## 4. Instance vs. Class Variables

### Instance Variables
These are like the unique features of each house built from the same blueprint (e.g., house A has a red door, house B has a blue door). Each object has its own copy of instance variables, defined using `self.variable_name`.

### Class Variables
These are shared by all objects of a class, like a common rule for all houses from a builder (e.g., all houses from "XYZ Builders" must have a certain type of roof). They are defined directly within the class but outside any methods.

```python
class Dog:
    species = "Canis familiaris" # Class variable: shared by all dogs

    def __init__(self, name, breed):
        self.name = name        # Instance variable: unique to each dog
        self.breed = breed      # Instance variable

dog1 = Dog("Max", "German Shepherd")
dog2 = Dog("Bella", "Poodle")

print(f"{dog1.name} species: {dog1.species}") # Both dogs share the same species
print(f"{dog2.name} species: {dog2.species}")

Dog.species = "Domestic Dog" # Changing the class variable affects all instances
print(f"{dog1.name} new species: {dog1.species}")
```

## 5. Methods: The Actions

A method is a function that belongs to an object. If the house blueprint includes instructions to "open door" or "turn on lights," these are like methods. They define what an object can do.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self): # Instance method
        return f"{self.name} says Woof!"

    def describe(self):
        return f"{self.name} is a {self.breed}."

dog1 = Dog("Charlie", "Labrador")
print(dog1.bark())
print(dog1.describe())
```

## 6. Inheritance: Building on Existing Plans

Imagine you have a basic house blueprint, but now you want to create a "luxury house" blueprint that includes everything from the basic plan, plus some extra features like a swimming pool and a bigger garage. **Inheritance** allows a new class (child/derived class) to take on the attributes and methods of an existing class (parent/base class), and then extend or modify them. This promotes code reusability.

```python
class Animal: # Parent class
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating."

class Dog(Animal): # Child class inheriting from Animal
    def __init__(self, name, breed):
        super().__init__(name) # Call parent's constructor
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"

my_dog = Dog("Rex", "Bulldog")
print(my_dog.eat())  # Inherited method
print(my_dog.bark()) # Dog's own method
```

## 7. Encapsulation: Keeping Things Tidy

Encapsulation is like putting all the building materials and tools for a house inside a secured workshop. You know what's inside and how to use it, but outsiders don't need to see the messy details or directly tamper with things. In OOP, encapsulation means bundling data (attributes) and the methods that operate on the data within a single unit (the class). It also involves restricting direct access to some of an object's components, which helps prevent accidental modification and makes the code more robust.

In Python, we typically indicate "private" attributes using a single underscore `_` (convention, not enforced) or double underscore `__` (name mangling for stronger protection).

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance # "Private" attribute (name-mangled)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        return "Deposit amount must be positive."

    def get_balance(self): # Public method to access balance
        return f"Current balance for {self.owner}: ${self.__balance}"

account = BankAccount("Alice", 100)
print(account.get_balance())
print(account.deposit(50))
# print(account.__balance) # This would raise an AttributeError!
# print(account._BankAccount__balance) # Technically accessible, but discouraged
```

By using encapsulation, we ensure that the internal state of an object (`__balance`) is managed through controlled methods (`deposit`, `get_balance`), making the code safer and easier to maintain.