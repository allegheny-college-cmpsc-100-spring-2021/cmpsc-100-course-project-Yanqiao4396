import random
from monsters import monsters
class Battle:
    def __init__(self, monster_a, monster_b):
        self.a = monster_a.pick
        self.b = monster_b.pick
        self.monster_a = monster_a.monsters[self.a]
        self.monster_b = monster_b.monsters[self.b]
        heal = True
        
    
        
           
                
    def demage(self):
        demage = random.randint(15,self.monster_a["attack"])
        self.monster_b["hp"] -= demage
        print(f"{self.a} attacks {self.b} with {demage} hp")
        
        
            
                
    def winner(self):
        if self.monster_a["hp"] > 0:
            winner = self.a
        else:
            winner = self.b
        print(f"{winner} wins!")
        
    def capture(self):
        capture = random.random()
        if capture <= self.monster_a["hp"] * 0.01:
            print(f"{self.a} tries to capture {self.b}, but it fails")
        else:
            print(f"{self.a} tries to capture {self.b}..... it succeeds. The battle ends")
            self.monster_b["hp"] -= 100
           
    
    def heal(self):
        if heal == True:
            self.monster_a["hp"] += 50
            print(f"{self.a} heals itself.")
            heal = False
        else:
            self.demage()
            print(f"{self.a} has healed once, so intead it attacks this time")
                  
    def enemy(self):
        demage = random.randint(15,self.monster_b["attack"])
        self.monster_a["hp"] -= demage
        print(f"{self.b} attacks {self.a} with {demage} hp")

        
    
    def escape(self):
        rate = random.random()
        if rate >0.5 :
            print(f"{self.a} tries to escape but it fails")
        else:
            print(f"{self.a} runs")
            self.monster_a["hp"] -= 100
         
        
    def fight(self):
        while self.monster_a["hp"] > 0 and self.monster_b["hp"] > 0:
            if self.monster_a["hp"] > 50 and self.monster_b["hp"] > 25:
                self.demage()
            elif self.monster_a["hp"] > 25 and self.monster_b["hp"] > 25:
                prob = random.random()
                if prob < 0.3:
                    self.heal()
                else:
                    self.demage()
            elif self.monster_a["hp"] > 0 and self.monster_b["hp"] > 25:
                prob = random.random()
                if prob < 0.3:
                    self.heal()
                elif prob < 0.6:
                    self.escape()
                else:
                    self.demage()
            elif self.monster_a["hp"] > 50 and self.monster_b["hp"] < 25:
                prob = random.random()
                if prob < 0.5:
                    self.capture()
                else:
                    self.demage()
            elif self.monster_a["hp"] > 25 and self.monster_b["hp"] < 25:
                prob = random.random()
                if prob < 0.4:
                    self.capture()
                elif prob < 0.8:
                    self.heal()
                else:
                    self.demage()
            elif self.monster_a["hp"] > 0 and self.monster_b["hp"] < 25:
                prob = random.random()
                if prob < 0.3:
                    self.capture()
                elif prob < 0.5:
                    self.heal()
                elif prob < 0.8:
                    self.escape()
                else:
                    self.demage()
            self.enemy()
        self.winner()