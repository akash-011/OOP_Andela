"""
This program store information of certain info on cars and can be used to display car info and condition 
"""

class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    
    def display_car(self):
        print "This is a %s %s with %s MPG."% (self.color,self.model,str(self.mpg))
    
    def drive_car(self):
        self.condition = "used"


# ElectricCar inherits from Car class , Car class is the parent class making ElectricCar the Child class
class ElectricCar(Car):                                     
    def __init__(self,model,color,mpg,battery_type):
        super(ElectricCar,self).__init__(model,color,mpg)   
        self.battery_type = battery_type
    
    def drive_car(self):            #ElectricCar has its own drive_car method 
        self.condition = "like new"
        