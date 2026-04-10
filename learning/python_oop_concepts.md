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