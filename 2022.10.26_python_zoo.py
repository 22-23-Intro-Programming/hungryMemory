#Python Zoo

class Animal:
    def __init__(self, name, animal_type, animal_species, habitat, age, popularity):
        self.name = name
        self.animal_type = animal_type
        self.habitat = habitat
        self.age = age
        self.popularity = popularity
    def get_name(self):
        return(self.name)
    def get_type(self):
        return(self.animal_type)
    def get_species(self):
        return(self.animal_species)
    def get_habitat(self):
        return(self.habitat)
    def get_age(self):
        return(self.age)
    def get_popularity(self):
        return(self.popularity)
    
class Zoo:
    def __init__(self, animal_list, admission_cost, maximum_capacity):
        self.animal_list = animal_list
        self.admission_cost = admission_cost
        self.maximum_capacity = maximum_capacity
    def get_animals(self):
        animals = []
        for i in self.animal_list:
            animals.append(i.get_name())
        return(animals)
    def get_habitats(self):
        habitats = []
        for i in self.animal_list:
            habitats.append(i.get_habitat())
        return habitats
    def get_animal_habitat(self, animal_name):
        animals = []
        for i in self.animal_list:
            animals.append(i.get_name())
        return(self.animal_list[animals.index(animal_name)].get_habitat())
    def get_habitat_animal(self, habitat_name):
        habitats = []
        for i in self.animal_list:
            habitats.append(i.get_habitat())
        return(self.animal_list[habitats.index(habitat_name)].get_name())
    def get_admission_cost(self):
        return(self.admission_cost)
    def get_maximum_capacity(self):
        return(self.maximum_capacity)
    def add_animal(self, new_animal):
        self.animal_list.append(new_animal)
    def set_admission_cost(self, new_cost):
        self.admission_cost = new_cost
    def set_maximum_capacity(self, new_capacity):
        self.maximum_capacity = new_capacity
            

def main():
    penguin = Animal("Penguin", "Mammal", "Some latin thing idk", "Ant Artcica", 2, 100)
    print(penguin.get_name())
    print(penguin.get_habitat())
    zoo_animals = [Animal("Bengal Tiger", "Mammal", "Panthera Tigris Tigris", "Forest", 5, 92), penguin]
    my_zoo = Zoo(zoo_animals, 90, 500)
    print(my_zoo.get_animals())
    print(my_zoo.get_habitats())
    print(my_zoo.get_animal_habitat("Bengal Tiger"))
    print(my_zoo.get_habitat_animal("Forest"))
    my_zoo.add_animal(Animal("Steven", "Mammal", "Homo Sapiens", "Couch", 22, 94))
    print(my_zoo.get_admission_cost())
    
if(__name__ == "__main__"):
    main()
    
    
        
    
        
