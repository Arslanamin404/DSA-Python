# Define a class Circle with instance object variable radius. Provide a setter
# and getter methods for radius. Also define getArea() and getCircumference() methods

class Circle:
    def __init__(self, radius=None):
        self.__radius = radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def get_area(self):
        area = (22/7)*(self.__radius*self.__radius)
        return round(area, 2)

    def get_circumference(self):
        circumference = 2*(22/7)*(self.__radius)
        return round(circumference, 2)


if __name__ == "__main__":
    c1 = Circle()
    radius = float(input("Enter the radius of circle: "))
    c1.set_radius(radius)

    print(f"\nRadius: {c1.get_radius()} units")
    print(f"Area: {c1.get_area()} units")
    print(f"Circumference: {c1.get_circumference()} units\n")
