from abc import ABC,abstractmethod
class area(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    def calculate_circle(self):
        pass
class square(area):
    def calculate_area(self):
        print("in square method")
class rectangle(area):
    pass
obj=square()
obj.calculate_area()