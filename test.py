# Yongdong Xi Mar 4

class Car:    
    def __car__(self, color, wheels = 0, axels= 0, doors = 0):
        self.color = color
        self._wheels = wheels
        self._axels = axels
        self._doors = doors

    def display(self):
        print(self.color)
        print(self._wheels)

build = Car('red', 1, 2, 3)
#accessing using class method
build.display()
#accessing directly from outside
print(build._wheels)