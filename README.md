# session10

Task:
Refactor the Polygons class to make it an iterable, you'll need to implement both an iterable and an iterator. In 

Refer old_polygons.py for the implementation using the sequence

Note:
Python, an iterable is an object that implements the __iter__ method, and an iterator is an object that implements both the __iter__ and __next__ methods.

Here's how we can refactor the Polygons class:

Add an __iter__ method to the Polygons class to return an iterator object.
Define an Iterator class that implements the __iter__ and __next__ methods.
Here's a refactored version of the Polygons class:

Polygons Class:

1. Polygons.__iter__():

This method returns an instance of the PolygonsIterator class, initialized with the list of polygons.

2. Polygons Iterator Class:

__init__(): Initializes the iterator with the list of polygons and sets the initial index to 0.
__iter__(): Returns self, making PolygonsIterator both an iterable and an iterator.
__next__(): Returns the next polygon in the sequence. If the end of the list is reached, it raises StopIteration to signal that iteration is complete.
With these changes, the Polygons class now supports iteration, allowing you to use it in loops or any other context that requires an iterable object. For example:

Colab Link  - https://colab.research.google.com/drive/1PrtCeyABG-fXTSo7btHk0kyn88ny_QH5?usp=drive_link