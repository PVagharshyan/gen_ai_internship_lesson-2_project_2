from array import array

class Int:
    
    """Checks whether the type matches and provides the assignment operation"""
    
    __max = 100
    __min = 0

    def __set_name__(self, owner, name):
        self.name = f"_{name}"
    
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        cls = type(self)
        if isinstance(value, int):
            if cls.__min <= value <= cls.__max:
                instance.__dict__[self.name] = float(value)
            else:
                raise ValueError('Out of limits!!')
        else:
            raise ValueError('Coordinate can only be a integral type!!')

class Point2D:

    """Is a two-dimensional vector representing a point in the Cardiac system"""

    x = Int()
    y = Int()

    def __init__(self, x, y):
        self.x = x
        self.y = y

def find_line_equation(p1: Point2D, p2: Point2D) -> (tuple,int):
    
    """Returns the coefficients of the line passing through the corresponding points"""

    try:
        k = (p1.y - p2.y)/(p1.x - p2.x)
        b = p1.y - k*p1.x
    except ZeroDivisionError:
        return p1.x 
    
    return (k, b)

class Point2DSequence:

    """Checks the corresponding points can create a polygonal image"""

    __min = 3
    __max = 4
    def __set_name__(self, owner, name):
        self.vertices = f"_{name}"
    
    def __get__(self, instance, owner):
        return instance.__dict__[self.vertices]

    def __set__(self, instance, value):

        """This function specifically ensures that duplicate points are removed from the list of polygon corners"""

        cls = type(self)
        
        if not (cls.__min <= len(value) <= cls.__max):
            raise ValueError("Out of limits(points)")
        
        mapValue = {}
        
        for i in value:
            mapValue[i] = 0
            mapValue[i] += 1
        
        value = []

        for i, j in mapValue.items():
            value.append(i)

        if len(mapValue) < 3:
            raise ValueError("These coordinates do not satisfy the polygon definition!!")
        elif len(mapValue) == 3:
            p1 = value[0]
            p2 = value[1]
            p3 = value[2]
            if find_line_equation(p1, p2) == find_line_equation(p2, p3):
                raise ValueError("These coordinates do not satisfy the polygon definition!!")
        instance.__dict__[self.vertices] = value
    
class Polygon:

    """Polygonal image"""

    vertices = Point2DSequence()

    def __init__(self, *vertices):
        self.vertices = vertices

    def append(self, *app: Point2D):

        """Enables adding vertices"""

        self.vertices = self.vertices + list(app)

#Testing

p1 = Point2D(1, 100)
p2 = Point2D(1, 2)
p3 = Point2D(0, 0)
p4 = Point2D(0, 0)
p5 = Point2D(0, 0)
p6 = Point2D(0, 0)

polygon = Polygon(p1, p2, p3)
polygon.append(p3)

print(polygon.vertices)


