import random

class Computer:

    def __init__(self):
        self.hp = 100
        self.player_attack = False
        self.computer_defense = False

    def imp_player_atk(self):
        self.player_attack = True
    
    def atked_weak(self):
        if self.player_attack:
            dam_amt = (random.randint(18, 25) + 5)
            self.hp -= dam_amt
            self.player_attack = False
            print("You do " + str(dam_amt) + " damage!")
        else:
            dam_amt = random.randint(18, 25)
            self.hp -= dam_amt
            print("You do " + str(dam_amt) + " damage.")

    def atked_strong(self):
        if self.player_attack:
            dam_amt = (random.randint(10, 35) + 5)
            self.hp -= dam_amt
            self.player_attack = False
            print("You do " + str(dam_amt) + " damage!");
        else:
            dam_amt = random.randint(10, 35)
            self.hp -= dam_amt
            print("You do " + str(dam_amt) + " damage.");
    
    def imp_player_atk(self):
        self.player_attack = True
        print("You improve the damage of your next attack.")
