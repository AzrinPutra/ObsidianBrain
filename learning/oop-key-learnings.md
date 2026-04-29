# OOP Key Learnings (From Assignment)

## Name Mangling with Private Attributes

- `__attribute` gets mangled to `_ClassName__attribute`
- Subclass cannot access parent's private attribute directly
  - `self.__side` in Cube looks for `_Cube__side`, not `_Square__side`
- **Always access parent private data through inherited methods**

### Fixing Name Mangling in Subclasses
1. Use a getter method in the parent class
2. Use inherited methods that already have access (e.g. `self.area()` instead of `self.__side`)

---

## super() for Reusing Parent Logic

```python
# Good examples:
Cube.area() = super().area() * 6
Cube.perimeter() = super().perimeter() * 3
```

- Avoids duplicating logic
- Sidesteps name mangling cleanly

---

## Abstract Methods

- `@abstractmethod` forces every subclass to implement it
- Forgetting any abstract method makes the subclass uninstantiable
- Common abstract methods: `area()`, `perimeter()`, `__eq__()`

---

## __eq__ Best Practice

```python
def __eq__(self, other):
    # Always check isinstance first!
    if not isinstance(other, Shape):
        return False
    return self.area() == other.area()
```

- Check `isinstance(other, ClassName)` before comparing attributes
- Compare by behavior/methods when direct attribute access is blocked by name mangling

---

## __str__ Gotcha

```python
# Wrong:
return f"Area: {self.area}"  # Returns method object, not value!

# Correct:
return f"Area: {self.area()}"  # Call with ()
```

- `self.area` without `()` refers to the method object
- Always include `()` when calling methods inside f-strings

---

## Related Code Concepts
- `__init__`: Constructor
- `__str__`: String representation (for print)
- `__eq__`: Equality comparison
- `__repr__`: Developer representation