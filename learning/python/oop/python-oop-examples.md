# Python OOP: Abstract Class & *args/**kwargs

## Abstract Class Examples

### Example 1: Shape (Basic)
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

# Usage
r = Rectangle(5, 3)
print(r.area())  # 15

c = Circle(2)
print(c.area())  # 12.56
```

### Example 2: Animal (With Concrete Method)
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def speak(self):
        pass
    
    def info(self):  # Concrete method
        return f"{self.name} makes sound: {self.speak()}"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Usage
dog = Dog("Buddy")
print(dog.info())  # Buddy makes sound: Woof!
```

### Example 3: Payment System
```python
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process(self, amount):
        pass

class CreditCard(Payment):
    def process(self, amount):
        return f"Charging ${amount} to credit card"

class PayPal(Payment):
    def process(self, amount):
        return f"Processing ${amount} via PayPal"

class Crypto(Payment):
    def process(self amount):
        return f"Sending ${amount} in crypto"

# Usage
payments = [CreditCard(), PayPal(), Crypto()]
for p in payments:
    print(p.process(100))
```

---

## *args and **kwargs Examples

### *args (Variable Positional Arguments)
```python
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3))        # 6
print(sum_all(10, 20, 30, 40)) # 100
print(sum_all(5))              # 5
```

### **kwargs (Variable Keyword Arguments)
``` python
def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Azrin", course="CSIT 121", year=2026)
# name: Azrin
# course: CSIT 121
# year: 2026
```

### Combining *args and **kwargs
```python
def func(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

func(1, 2, 3, name="Azrin", age=20)
# Positional: (1, 2, 3)
# Keyword: {'name': 'Azrin', 'age': 20}
```

### Practical: Flexible Logger
```python
def log_message(level, *args, **kwargs):
    msg = " ".join(str(a) for a in args)
    print(f"[{level.upper()}] {msg}")
    
    if kwargs.get("save"):
        print(f"  Saved to {kwargs['save']}")
    if kwargs.get("notify"):
        print(f"  Notifying {kwargs['notify']}")

log_message("ERROR", "Database", "connection", "failed", save="error.log")
# [ERROR] Database connection failed
#   Saved to error.log
```

### Practical: Flexible Class
```python
class Robot:
    def __init__(self, name, *features):
        self.name = name
        self.features = features
    
    def __str__(self):
        return f"{self.name} with features: {', '.join(self.features)}"

r = Robot("R2D2", "laser", "flying", "translator")
print(r)  # R2D2 with features: laser, flying, translator
```

### With Abstract Classes
```python
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    def process(self, *args, **kwargs):
        return self._process_data(*args, **kwargs)
    
    @abstractmethod
    def _process_data(self, *args, **kwargs):
        pass

class Adder(DataProcessor):
    def _process_data(self, *args, **kwargs):
        return sum(args)

class Multiplier(DataProcessor):
    def _process_data(self, *args, **kwargs):
        result = 1
        for n in args:
            result *= n
        return result

print(Adder().process(1, 2, 3, 4))      # 10
print(Multiplier().process(2, 3, 4))    # 24
```

---

## Common Patterns for Assignments

### Factory Pattern with *args
```python
class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def __init__(self, *args):
        self.wheels = args[0] if args else 4
    
    def move(self):
        return "Driving"

class Boat(Vehicle):
    def __init__(self, *args):
        self.masts = args[0] if args else 1
    
    def move(self):
        return "Sailing"

def create_vehicle(vtype, *args):
    vehicles = {'car': Car, 'boat': Boat}
    return vehicles[vtype](*args)

v = create_vehicle('car', 4)
print(v.move())  # Driving
```

---

## Practice Exercises

1. Create abstract class `Employee` with concrete method `info()` and abstract `salary()`
2. Use `*args` to accept multiple numbers and return the average
3. Create a `Config` class that accepts any keyword arguments and stores them
4. Combine: Abstract class with `**kwargs` for flexible initialization