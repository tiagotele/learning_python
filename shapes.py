class Shape:

    def __init__(self):
        print "Object Shape just created"

    def drawMe(self):
        print "I'm a simple Shape"

class Circle(Shape):

    def __init__(self):
        print "Object Circle just created"

    def drawMe(self):
        print "I'm a simple Circle"

class Square(Shape):
    def __init__(self):
        print "Object Square just created"

    def drawMe(self):
        print "I'm a simple Square"
