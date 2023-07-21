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

    def __str__(self):
        return f"({self.x}, {self.y})"

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
            if i not in mapValue.keys():
                mapValue[i] = 0
            mapValue[i] += 1
        
        value = []

        for i, j in mapValue.items():
            value.append(i)

        if len(mapValue) < 3:
            raise ValueError("these coordinates do not satisfy the polygon definition!!")
        mapCheckPoints = {}
        for i in range(len(value)):
            for j in range(i + 1, len(value)):
                line = find_line_equation(value[i], value[j])
                if line not in mapCheckPoints:
                    mapCheckPoints[line] = 0
                mapCheckPoints[line] += 1
        if len(mapCheckPoints) < 2:
            raise ValueError("these coordinates do not satisfy the polygon definition!!")

        instance.__dict__[self.vertices] = value
    
class Polygon:

    """Polygonal image"""

    vertices = Point2DSequence()

    def __init__(self, *vertices):
        self.vertices = vertices
    
    def __str__(self):
        text = [str(i) for i in self.vertices]
        text = ', '.join(text)
        return f"vertices: {text}"

    def append(self, *app: Point2D):

        """Enables adding vertices"""

        self.vertices = self.vertices + list(app)

#Testing

p1 = Point2D(1, 1)
p2 = Point2D(2, 2)
p3 = Point2D(4, 3)
p4 = Point2D(6, 4)
p5 = Point2D(5, 5)
p6 = Point2D(0, 0)

polygon = Polygon(p1, p2, p3)
print(polygon)


