
class rectangle:

   def __init__(self, length, width):
      self.length = length
      self.width = width

   def area(self):
      print("\nArea of rectagle is ", self.length * self.width)

   def perimeter(self):
      print("Perimeter of rectangle is ", 2 * (self.length + self.width))

rectangle1 = rectangle(8, 6)
rectangle2 = rectangle(10, 5)

rectangle1.area()
rectangle1.perimeter()

rectangle2.area()
rectangle2.perimeter()