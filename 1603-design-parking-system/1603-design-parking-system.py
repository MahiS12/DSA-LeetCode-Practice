class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.slot= {1:big,2:medium,3:small}

        

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if not self.slot.get(carType):
            return False
        self.slot[carType] -=1
        return True
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)