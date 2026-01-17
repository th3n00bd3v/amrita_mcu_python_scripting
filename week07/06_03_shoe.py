'''
Wrie a superclass Shoe and 2 subclasses Ballet, Boot, of that superclass, listing 4 attributes that each subclass would have.

superclass shoe: 
Attributes: brand, size, material

subclass - Ballet- attributes:
brand, size, material, instock

subclass - Boot- attributes:
brand, size, material, instock

method in subclass:
display shoe info 

when user inputs a shoe type ballet or boot, output should print shoe info like brand, size, material, instock(True/False) using the method in subclass.

'''
class Shoe:
    def __init__(self, brand, size, material):
        self.brand = brand
        self.size = size
        self.material = material
        
class Ballet(Shoe):
    def __init__(self, brand, size, material, instock):
        super().__init__(brand, size, material)
        self.instock = instock

    def display_shoe_info(self):
        print(f"Ballet Shoe Info:\nBrand: {self.brand}\nSize: {self.size}\nMaterial: {self.material}\nIn Stock: {self.instock}")

class Boot(Shoe):
    def __init__(self, brand, size, material, instock):
        super().__init__(brand, size, material)
        self.instock = instock

    def display_shoe_info(self):
        print(f"Boots Info:\nBrand: {self.brand}\nSize: {self.size}\nMaterial: {self.material}\nIn Stock: {self.instock}")


shoe_type = input("Enter shoe type (ballet/boot): ").strip().lower()
shoe_brand = input("Enter shoe brand: ")
shoe_size = int(input("Enter shoe size: "))
shoe_material = input("Enter shoe material: ")

if shoe_type == "ballet":
    ballet_shoe = Ballet(shoe_brand, shoe_size, shoe_material, instock=True)
    ballet_shoe.display_shoe_info()

elif shoe_type == "boot":
    boot_shoe = Boot(shoe_brand, shoe_size, shoe_material, instock=False)
    boot_shoe.display_shoe_info()

else:
    print("Invalid shoe type entered!")