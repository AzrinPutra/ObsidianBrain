---
title: Python Object Oriented Programming
path: "SIM-UOW / Python Object Oriented Programming"
url: https://www.notion.so/Python-Object-Oriented-Programming-269bd926b4e48035924ed97b0aa82418
created_by: Azrin Putra
last_edited_by: Azrin Putra
last_edited_time: 2025-12-13T12:58:00.000Z
---

# Python Object Oriented Programming
### Class
```python
ie. class Point:
		    pass
```

Classes is a fundamental building block in Python Object oriented programming. Classes are an object constructor or simply put a blueprint to creating an object. Our next question is:

### What is an object?

Let’s say we have a point. A point has an x and a y. These are called attributes.
```python
ie. """To construct a point, we need the two attributes"""

		class Point:
		    """Represents a point in two-dimensional geometric coordinates"""
		    
		    def __init__(self, x, y):
		    """
        Initialize the position of a new point. the x and y
        coordinates can be specified. If they are not, the point
        defaults to the origin.
        """
			      self.x = x
			      self.y = y 
```

### **__init**__() method

The __**init__ **method is used to assign values to objects’ attributes as shown below.
i.e. for our object “point”,
- it has an x
- it has a y
These are its attributes. 
```python
class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

point = Point(5, 0)
```

With the above example,  we have defined the x and y are the attributes that forms the object “point”. By calling out the class, Python expects us to give “point” object a value for each attribute(x and y) to form the object. We can also give x and y a default value so that if the user does not provide said values, it will default to the values that is given in the init method instead of giving an error.
```python
class Point:
    
    def __init__(self, x=0, y=0):
	      self.x = x
	      self.y = y
	      
point = Point()
print(point)

# This will print 0 0.
```

### Case Study: Notebook

What is in a Notebook
- Notes which are short memos stored inside a Notebook
	- Each note should record the day it was written
	- and can have tags for easy querying
	- Able to modify notes
	- Able to search


### Object Container: Notebook
- Notes : list

Methods
- search(filter : str) : list
	- To return a list of filtered notes
	- User to provide the filter which is a str
	- Function will return a list
- new_note(memo, tag=’’)
	- a memo and a tag has to be passed in this function
- modify_memo(note_id, memo)
- modify_tags(note_id, tags)


### Object: Notes
Attributes
- memo
- tags
- creation_date
- id

Methods
- match(search_filter : str) : boolean
	- User to provide the search filter which is a str
	- This function will return a boolean (True or False)

Here is a UML diagram for easy visualization.

```python
UML

+-------------------------+
|        Notebook         |
+-------------------------+
| - notes: list[Note]     |
+-------------------------+
| + new_note(memo, tags)  |
| + modify_memo(id, memo) |
| + modify_tags(id, tags) |
| + search(filter): list  |
+-------------------------+
           |
   * list of Notes *
           ▼
+--------------------+
|      Note          |
+--------------------+
| - id: int          |
| - memo: str        |
| - tags: str        |
| - creation_date    |
+--------------------+
| + match(filter):   |
|   bool             |
+--------------------+
```

We can also create a simple folder structure with the files below

```python
parent_directory/
    notebook.py
    menu.py
    command_option.py ## for future use to add more user interfaces
```

Let’s start to put it together starting with objects Notebook and Note

```python
#!/usr/bin/env python3

# File Name: notebook.py

import datetime

class Notebook:
    """ Represent a collection of notes that can be tagged,
    modified and searched..
    """
    
    def __init__(self):
        """ Initialize a notebook with an empty list """
        self.notes = []
        
    def new_note(self, memo, tags=""):
        """ Create a new note and append it to the list """
        self.notes.append(Note(memo, tags=""))
    
    def _find_note(self, note_id):
        """ Locate note with the given id """
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None
        
    def modify_memo(self, note_id, memo):
        """ Find the note with the given id and change its 
        memo to the given value.
        """
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        else:
            return False
                
    def modify_tags(self, note_id, tags):
        """ Find the note with the given id and change its tags 
        to the given value
        """
        note = self._find_note(note_id)
        if note:
            note.tags = tags
            return True
        else:
            return False
                
    def search(self, filter):
        """ Find all notes that match the given filter """
        for note in self.notes:
            if note.match(filter):
                return note
        
    

# Store the next available id for all the new notes
last_id = 0

class Note:
    """ Represent a note in the notebook. Match against a string
    in searches and store tags for each notes
    """
    
    def __init__(self, memo, tags=""):
        """ Initialize a note with memo and optional space-separated
        tags. Automatically set the note's creation date and a unique
        id.
        """
        
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id
        
    def match(self, filter):
        """ Determine if this note matches the filter text. Return
        True if it matches. Return False if otherwise. Search is 
        case-sensitive and matches both text and tags via interation of strings
        """
        
        return filter in self.memo or filter in self.tags
```

This is our foundation code which is built based upon our UML diagram.

### Inheritance
Classes can inherit attributes from other classes via inheritance. This is a good way to have sub classes based on parent classes without writing duplicated code.
ie. Parent class
```python
class Contact:
    all_contacts = []
    
    def __init__(self, name, email):
	      self.name = name
	      self.email = email
	      Contact.all_contacts.append(self)
	      ## all_contacts list is shared to all instances of Contact class
	      ## Also means that there is only one list that we access via
	      ## Contact.all_contacts
```

💡 Creating a list via [ ] is actually shorthand for using list() method

[]  == list()

What if some of our contacts are suppliers that we need to order from via order()? We can add an order() method to Contact class but it means that it is possible to accidentally order from contacts that are not suppliers. Let’s create a supplier class that acts like the Contact class but has an order() method.

```python
class Supplier(contact):
    def order(self, order):
        print("If this were a real system, we would send {0} order to {1}"\
        .format(order, self.name))
```
