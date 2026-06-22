class ParkingSystem:

    def __init__(self, big, medium, small):
        self.slots = [big, medium, small]

    def addCar(self, carType):
        if self.slots[carType - 1] > 0:
            self.slots[carType - 1] -= 1
            return True

        return False