"""
Write 3 classes which are related to each other
1) a monster class
2) a night-monster class (they only come out at night)
3) a full moon monster class (they only come out at night and on the full moon)

Make use of inheritance to save your code!

## Monster class
# class attribute
time_of_day (will need to activate night monsters)
day_of_month
full_moon (boolean)

# attributes
name
number of limbs
attack mode (magic, physical, mental hypnosis etc)
scare factor
weakness
life points

# methods
basic attack (attack something)
sleep (get life points back)
defend (something attacks it!)

## Night monster
same as above, but also special powers that activate at night
vulnerable in daylight


## full moon monster
only active in the full moon
"""

class Monster:    
    times=["Morning","Afternoon","Night"]
    time_of_day="Night"
    day_of_month=15
    full_moon=True
    
    def __init__(self,name:str,number_of_limbs:int,attack_mode:str,scare_factor:int,weakness:str,life_points:int):
        self.name=name
        self.number_of_limbs=number_of_limbs
        self.attack_mode=attack_mode
        self.scare_factor=scare_factor
        self.weakness=weakness
        self.life_points=life_points
        
    def basic_attack(self):
        print(f"{self.name} attacks with {self.attack_mode}")
    def sleep(self):
        self.life_points+=10
        print(f"{self.name} sleeps and gains life points. Current life points: {self.life_points}")
    def defend(self,attack_power:int):
        self.life_points-=attack_power
        print(f"{self.name} defends and loses {attack_power} life points. Current life points: {self.life_points}")
        
class NightMonster(Monster):
    def __init__(self,name:str,number_of_limbs:int,attack_mode:str,scare_factor:int,weakness:str,life_points:int,special_power:str):
        super().__init__(name,number_of_limbs,attack_mode,scare_factor,weakness,life_points)
        self.special_power=special_power
        
    def night_attack(self):
        if Monster.time_of_day=="Night":
            print(f"{self.name} uses special power: {self.special_power}")
        else:
            print(f"{self.name} is vulnerable in daylight and cannot use special powers.")
            
class FullMoonMonster(NightMonster):
    def __init__(self,name:str,number_of_limbs:int,attack_mode:str,scare_factor:int,weakness:str,life_points:int,special_power:str):
        super().__init__(name,number_of_limbs,attack_mode,scare_factor,weakness,life_points,special_power)
        
    def full_moon_attack(self):
        if Monster.time_of_day=="Night" and Monster.full_moon==True:
            print(f"{self.name} uses full moon special power: {self.special_power}")
        else:
            print(f"{self.name} can only attack during a full moon night.")
            

# First monster
monster =Monster(name="Goblin",number_of_limbs=4,attack_mode="Physical",scare_factor=5,weakness="Fire",life_points=100)
monster.basic_attack()
monster.sleep()
monster.defend(20)

# Second monster - Night Monster
night_monster=NightMonster(name="Vampire",number_of_limbs=2,attack_mode="Mental Hypnosis",scare_factor=8,weakness="Sunlight",life_points=150,special_power="Hypnotic Gaze")
night_monster.night_attack()
night_monster.defend(30)

# Third monster - Full Moon Monster
fullmoon_monster=FullMoonMonster(name="Werewolf",number_of_limbs=4,attack_mode="Physical",scare_factor=10,weakness="Silver",life_points=200,special_power="Lunar Fury")
fullmoon_monster.full_moon_attack()
fullmoon_monster.sleep()
fullmoon_monster.defend(50)

