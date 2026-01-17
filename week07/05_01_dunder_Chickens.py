"""
Update your chicken class to include the following dunders

__str__  : make some nice str format for your chicken. 
When we print your chicken it should tell us: how heavy the chicken is, the gender and how many eggs it has laid (if has)

__add__ : what happens when you add two chickens together? If they are male and female, create a baby chicken! (a new chicken) Otherwise, nothing?

"""
import random

class Chicken:
    def __init__(self, weight: float, gender: str, eggs_laid = 0):
        self.weight = weight
        self.gender = gender
        self.eggs_laid = eggs_laid
        
    def __str__(self):
        info = f"Chicken - Weight: {self.weight}kg, Gender: {self.gender.capitalize()}"
        if self.gender == 'female':
            info += f", Eggs laid: {self.eggs_laid}"
        return info

    def __add__(self, other):
        # Check if the other object is a Chicken
        if not isinstance(other, Chicken):
            return NotImplemented
        
        # Only create a baby if one is male and the other is female
        if (self.gender == 'male' and other.gender == 'female') or \
           (self.gender == 'female' and other.gender == 'male'):

            baby_weight = round(random.uniform(0.2, 0.5), 2)
            baby_gender = random.choice(['male', 'female'])
            return Chicken(baby_weight, baby_gender)
        else:
            print("Nothing happens: same gender chickens cannot produce a baby.")
            return None
        
hen = Chicken(2.5, 'male')
rooster = Chicken(3.0, 'female', 5)

# --- Print them ---
print(hen)
print(rooster)

# --- Explicitly call __add__ ---
baby1 = hen.__add__(rooster)
if baby1:
    print("Congratulations! Here's your baby!")
    print(baby1)