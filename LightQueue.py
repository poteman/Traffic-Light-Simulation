from Car import Car


class LightQueue:
    '''
    Represents the queue at each direction of a light
    '''

    def __init__(self, id, cars=[], time=0):
        self.id = id
        self.cars = cars[:]
        for i in range(len(self.cars)):
            self.cars[i].start_time = time

    def pushCar(self, car, time):
        ''' 
        Add a single car to the end of the queue and sets its start time
        '''
        initLength = len(self.cars)
        car.start_time = time
        self.cars.append(car)
        assert(len(self.cars) - initLength == 1)

    def peakCar(self):
        return self.cars[0]

    def popCar(self):
        ''' 
        Pop a single car off the beginning of the queue and return it 
        '''
        initNumCars = len(self.cars)
        car = self.cars.pop(0)
        assert(initNumCars - len(self.cars) == 1)
        return car

    def getNumCars(self):
        return len(self.cars)

    def getWaitTime(self, time):
        return sum([time - car.start_time for car in self.cars])
