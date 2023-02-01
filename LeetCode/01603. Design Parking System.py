class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.s = [ 0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        self.s[carType] -= 1 
        return self.s[carType] >= 0
        
