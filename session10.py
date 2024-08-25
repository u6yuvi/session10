import math

class Polygon:
    def __init__(self, n, R):
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices.')
        self._n = n
        self._R = R
        
    def __repr__(self):
        return f'Polygon(n={self._n}, R={self._R})'
    
    @property
    def count_vertices(self):
        return self._n
    
    @property
    def count_edges(self):
        return self._n
    
    @property
    def circumradius(self):
        return self._R
    
    @property
    def interior_angle(self):
        return (self._n - 2) * 180 / self._n

    @property
    def side_length(self):
        return 2 * self._R * math.sin(math.pi / self._n)
    
    @property
    def apothem(self):
        return self._R * math.cos(math.pi / self._n)
    
    @property
    def area(self):
        return self._n / 2 * self.side_length * self.apothem
    
    @property
    def perimeter(self):
        return self._n * self.side_length
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.count_edges == other.count_edges 
                    and self.circumradius == other.circumradius)
        else:
            return NotImplemented
        
    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.count_vertices > other.count_vertices
        else:
            return NotImplemented


class Polygons:
    """
     A class representing a collection of polygons with varying numbers of sides.
    """
    def __init__(self, m, R):
        """
        Initializes a Polygons instance.
        """
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m = m
        self._R = R
        self._polygons = [Polygon(i, R) for i in range(3, m+1)]

    def __len__(self):
        """
        Returns the number of polygons in the collection.
        """
        return self._m - 2

    def __repr__(self):
        """
        Provides a string representation of the Polygons instance.
        """
        return f'Polygons(m={self._m}, R={self._R})'

    def __getitem__(self, s):
        """
         Returns the polygon at the specified index.
         """
        return self._polygons[s]

    @property
    def max_efficiency_polygon(self):
        """
        Returns the polygon with the highest area-to-perimeter ratio.
        """
        sorted_polygons = sorted(self._polygons, 
                                 key=lambda p: p.area / p.perimeter,
                                 reverse=True)
        return sorted_polygons[0]

    # Implement the __iter__ method to return an iterator
    def __iter__(self):
        """
        Returns an iterator for the polygons collection.
        """
        return PolygonsIterator(self._polygons)


class PolygonsIterator:
    """
    An iterator for the Polygons class.
    """
    def __init__(self, polygons):
        """
        Initializes a PolygonsIterator instance.
        """
        self._polygons = polygons
        self._index = 0

    def __iter__(self):
        """
        Returns the iterator object itself.
        """
        return self

    def __next__(self):
        """
        Returns the next polygon in the sequence.
        """
        if self._index < len(self._polygons):
            polygon = self._polygons[self._index]
            self._index += 1
            return polygon
        else:
            raise StopIteration

if __name__=="__main__":

    polygons = Polygons(5, 10)
    for polygon in polygons:
        print(polygon)