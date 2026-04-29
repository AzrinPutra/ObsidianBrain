# Python OOP Primer: Understanding Object-Oriented Programming

This primer is for Azrin, who knows Python basics but is new to Object-Oriented Programming (OOP). We'll cover the core concepts with simple analogies and short code examples.

## What is Object-Oriented Programming (OOP)?

Imagine you're building with LEGOs instead of just drawing. In basic Python, you write instructions step-by-step. In OOP, you create "blueprints" (classes) for "things" (objects) that have their own characteristics and actions. This helps organize your code, make it reusable, and easier to manage as projects grow.

## Core Concepts

### 1. Classes: The Blueprints

A `class` is like a blueprint for creating objects. It defines the structure and behavior that all objects of that type will have.

**Analogy:** The blueprint for a car. It specifies that all cars have wheels, an engine, a steering wheel, and can accelerate or brake.

```python
class Car:
    pass # A simple, empty class
```

### 2. Objects: The Instances

An `object` (also called an instance) is a real-world entity created from a class. You can create many objects from a single class blueprint, and each object will be unique.

**Analogy:** An actual car built from the car blueprint. You can have a red car, a blue car, an old car, a new car – all from the same blueprint but with their own specific details.

```python
# Creating objects (instances) from the Car class
my_car = Car()
your_car = Car()

print(my_car)
print(your_car)
# Output will show different memory addresses, indicating they are separate objects
```

### 3. `__init__` Method: Setting Up Your Object

The `__init__` method (pronounced "dunder init") is a special method called automatically when you create a new object. It's used to initialize the object's attributes (its characteristics). `self` refers to the instance of the class (the object itself).

**Analogy:** When you build a car, `__init__` is like the factory attaching the specific wheels, engine, and painting it a certain color initially.

```python
class Car:
    def __init__(self, make, model, color):
        self.make = make      # instance variable
        self.model = model    # instance variable
        self.color = color    # instance variable
        self.speed = 0        # initial speed

my_car = Car("Toyota", "Camry", "Blue")
friends_car = Car("Honda", "Civic", "Red")

print(f"My car is a {my_car.color} {my_car.make} {my_car.model}.")
print(f"My friend's car is a {friends_car.color} {friends_car.make} {friends_car.model}.")
```

### 4. Instance Variables vs. Class Variables

*   **Instance Variables:** These belong to a specific object. Each object gets its own copy, and changes to one object's instance variable don't affect others. (e.g., `make`, `model`, `color` in the `Car` example).
*   **Class Variables:** These belong to the class itself, not to any specific object. All objects of that class share the same class variable.

**Analogy:**
*   Instance variable (e.g., `color`): Your car is red, my car is blue. The color is specific to each car.
*   Class variable (e.g., `wheels_per_car`): Every car, by default, has 4 wheels. This is common to all `Car` objects.

```python
class Car:
    wheels_per_car = 4 # Class variable

    def __init__(self, make, model):
        self.make = make
        self.model = model

car1 = Car("Ford", "Focus")
car2 = Car("Nissan", "Altima")

print(f"{car1.make} {car1.model} has {car1.wheels_per_car} wheels.")
print(f"{car2.make} {car2.model} has {car2.wheels_per_car} wheels.")

# You can access class variables via the class name as well
print(f"All Cars have {Car.wheels_per_car} wheels.")
```

### 5. Methods: The Actions

`Methods` are functions defined inside a class that perform actions on the object's data. They always take `self` as their first parameter.

**Analogy:** The car blueprint includes instructions on how to "accelerate" or "brake." These are actions the car can perform.

```python
class Car:
    def __init__(self, make, model, speed=0):
        self.make = make
        self.model = model
        self.speed = speed

    def accelerate(self, increment):
        self.speed += increment
        print(f"The {self.make} {self.model} is now going {self.speed} km/h.")

    def brake(self, decrement):
        self.speed -= decrement
        if self.speed < 0:
            self.speed = 0
        print(f"The {self.make} {self.model} is now going {self.speed} km/h.")

my_car = Car("Tesla", "Model 3")
my_car.accelerate(50)
my_car.brake(20)
```

### 6. Inheritance: Building on Existing Blueprints

`Inheritance` allows a new class (child/derived class) to inherit attributes and methods from an existing class (parent/base class). This promotes code reuse and creates a hierarchical relationship.

**Analogy:** A "SportsCar" blueprint can inherit all the basic features from the general "Car" blueprint, but then add its own specific features like "turbo boost" or "spoiler."

```python
class Vehicle: # Parent class
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        print(f"{self.brand} engine started.")

class Car(Vehicle): # Child class inherits from Vehicle
    def __init__(self, brand, model):
        super().__init__(brand) # Call parent's __init__
        self.model = model

    def drive(self):
        print(f"Driving the {self.brand} {self.model}.")

my_vehicle = Vehicle("Generic Motors")
my_vehicle.start_engine()

my_car = Car("BMW", "X5")
my_car.start_engine() # Inherited method
my_car.drive()        # Specific method for Car
```

### 7. Encapsulation: Keeping Things Tidy and Safe

`Encapsulation` is the bundling of data (attributes) and methods (functions) that operate on the data within a single unit (the class). It also often involves restricting direct access to some of an object's components, protecting them from unintended external modifications. In Python, this is usually done by convention using a single `_` (for protected) or double `__` (for private, though not strictly enforced like in some other languages) prefix for attribute names.

**Analogy:** A car's engine is encapsulated. Drivers interact with the steering wheel, pedals, and gear shift (public methods), not directly with the complex internal workings of the engine (private attributes/methods). This prevents accidental damage and keeps the interface simple.

```python
class BankAccount:
    def __init__(self, owner, initial_balance):
        self.owner = owner
        self.__balance = initial_balance # Private by convention using __

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self): # Public method to access private balance
        return self.__balance

my_account = BankAccount("Azrin", 1000)
my_account.deposit(500)
my_account.withdraw(200)
# print(my_account.__balance) # This would raise an AttributeError because it's "private"
print(f"Current balance: {my_account.get_balance()}")
my_account.withdraw(2000) # Insufficient funds
```

This primer should give you a solid foundation for understanding Python OOP!
