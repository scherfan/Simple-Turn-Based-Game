import random

class Player:
    def __init__(self):
        self.hp = 50
        self.computer_attack = False
        self.player_defense = False
    
    def heal(self):
        if self.player_defense:
            heal_amt = (random.randint(18, 25) + 5)
            self.player_defense = False
        else:
            heal_amt = random.randint(18, 25)
            
        if (heal_amt + self.hp) >= 100:
            print("You heal for " + str((100 - self.hp)) + " points.")
            self.hp = 100
        else:
            self.hp += heal_amt
            print("You heal for " + str(heal_amt) + " points.")

    def imp_def(self):
        self.player_defense = True
        print("You improve your next heal.")
