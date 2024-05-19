
class Pet:
    all =[]
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type, owner = None):
        self.name = name
        self.owner = owner

        if pet_type in self.PET_TYPES: 
            self.pet_type = pet_type
        else:
            raise "Error"
        
        self.all.append(self)



class Owner:
    pets_list = []
    sorted_pets = []
    def __init__(self, name):
        
        self.name = name 
        
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if pet.pet_type in Pet.PET_TYPES and isinstance(pet, Pet):
            pet.owner = self
            self.pets_list.append(pet)

    def get_sorted_pets(self):
        owners_pet = [pet for pet in Pet.all if pet.owner == self]
        sorted_pets = sorted(owners_pet, key=lambda obj: obj.name)
        return sorted_pets
