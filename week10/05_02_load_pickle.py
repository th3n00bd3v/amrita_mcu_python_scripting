"""
Load your pickled files from 05_01 and use them here!

"""


from pickle_this import Car
import pickle

with open('car_class.pkl', 'rb') as file:
    CarLoaded = pickle.load(file)
my_car = CarLoaded(4, "blue", True)
print(my_car.can_drive())