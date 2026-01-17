"""
create a simple bicycle class

# Attributes
number of tires
type of of tires (road vs mountain bike)
model
color
number of speeds
brakes (front or back or both)
current speed.

# Methods
brake
pedal faster (should affect speed)
"""

class Bicycle:
    tires = 2
    tire_type = "road"
    model = "Hercules"
    color = "Green"
    speeds = 18
    brakes = "both"
    current_speed = 12
    
    def brake(self, amount):
        self.current_speed = max(0, self.current_speed - amount)
        return self.current_speed
    
    def pedal_faster(self, amount):
        self.current_speed += amount
        return self.current_speed
    
my_bike = Bicycle()
print("Initial speed:", my_bike.current_speed)
my_bike.pedal_faster(5)
print("Speed after pedaling faster:", my_bike.current_speed)
my_bike.brake(8)
print("Speed after braking:", my_bike.current_speed)
