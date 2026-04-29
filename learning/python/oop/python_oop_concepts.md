---
tags: [python, oop, fundamentals]
created: 2026-04-09
---

# Python OOP Key Concepts

## Access Specifiers (Variables)

- **Public**: `self.radius` - accessible anywhere
- **Private (convention)**: `self._radius` - internal use, don't touch
- **Name mangling**: `self.__radius` - harder to access from outside
- **Dunder**: `self.__variable__` - built-in magic methods

## @classmethod
- Accesses **class variables** (shared across all instances)
- Called on class, not instance: `Circle.get_count()`
- Takes `cls` as first parameter

## @property
- Makes method look like an attribute
- No parentheses when accessing: `circle.radius` not `circle.radius()`
- Enables getter/setter pattern

## Getter/Setter
- Use `@property` for controlled access to private variables
- Validate data before setting

## Comparison Methods (Dunder)
- `__eq__(self, other)` - equality (`==`)
- `__lt__(self, other)` - less than (`<`)
- `__str__(self)` - string representation
- `__init__(self, ...)` - constructor

---

# Inheritance & super()

## Basic Inheritance
```python
class Parent:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, {self.name}"

class Child(Parent):
    pass

c = Child("Azrin")
print(c.greet())  # Hello, Azrin
```

## Overriding Methods
```python
class Parent:
    def greet(self):
        return "Hello from Parent"

class Child(Parent):
    def greet(self):  # Overrides parent
        return "Hello from Child"

# Child greet() takes priority
```

## super() — Calling Parent Methods
```python
class Shape:
    def __init__(self, name):
        self.name = name

class Square(Shape):
    def __init__(self, side):
        super().__init__("Square")  # Call parent __init__
        self.side = side
    
    def area(self):
        return self.side ** 2
```

### Why super()?
1. **Avoids duplicating parent logic**
2. **Sidesteps name mangling** (private `__attr` issues)
3. **Maintains inheritance chain** (multiple levels)

## super() in Multi-Level Inheritance
```python
class A:
    def process(self):
        return "A"

class B(A):
    def process(self):
        return f"{super().process()} + B"

class C(B):
    def process(self):
        return f"{super().process()} + C"

print(C().process())  # A + B + C
```

---

# *args and **kwargs

## *args — Variable Positional Arguments
```python
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3))        # 6
print(sum_all(10, 20, 30, 40)) # 100
```

- `*args` captures extra positional arguments as a **tuple**
- Allows flexible number of inputs

## **kwargs — Variable Keyword Arguments
```python
def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Azrin", course="CSIT 121")
# name: Azrin
# course: CSIT 121
```

- `**kwargs` captures extra keyword arguments as a **dictionary**
- Allows named parameters without defining each one

## Combining *args and **kwargs
```python
def func(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

func(1, 2, 3, name="Azrin", age=20)
# Positional: (1, 2, 3)
# Keyword: {'name': 'Azrin', 'age': 20}
```

## *args/**kwargs in Classes
```python
class Robot:
    def __init__(self, name, *features):
        self.name = name
        self.features = features
    
    def __str__(self):
        return f"{self.name}: {', '.join(self.features)}"

r = Robot("R2D2", "laser", "flying", "translator")
print(r)  # R2D2: laser, flying, translator
```

## *args/**kwargs with Abstract Classes
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

print(Adder().process(1, 2, 3, 4))  # 10
```

---

# Key Takeaways

1. **Inheritance** = Child class gets Parent's methods automatically
2. **super()** = Clean way to call parent methods, avoids name mangling
3. ***args** = Tuple of extra positional arguments
4. ***kwargs** = Dictionary of extra keyword arguments
5. **Combine them** for flexible, reusable code