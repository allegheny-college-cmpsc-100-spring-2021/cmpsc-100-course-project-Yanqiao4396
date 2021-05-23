import random
class monsters:
    def __init__(self):
        self.dictionary()
        self.generate()
    def dictionary(self):
        self.monsters = {
            "Squirtle":{
                "hp": 100,
                "attack": 30
                },
            "Charmander":{
                "hp": 120,
                "attack": 25
                },
            "Bulbasaur":{
                "hp":90,
                "attack": 35
            }
        }
    def generate(self):
        list = []
        for monster in self.monsters:
            list.append(monster)
        self.pick = random.choice(list)
        
