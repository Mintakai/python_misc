from dice import d6
from random import randint

class Creature:
    def __init__(self, name, max_hp):
        self.name = name
        self.max_hp = max_hp
        self.hp = self.max_hp
    
    def __str__(self):
        return f"Name: {self.name}\nHP: {self.hp} / {self.max_hp}"

    def damage(self, dmg):
        self.hp -= dmg

    def heal(self, heal):
        self.hp += heal
        if self.hp > self.max_hp:
            self.hp = self.max_hp

class MagicUser(Creature):
    def __init__(self, name, max_hp, mana):
        super().__init__(name, max_hp)
        self.mana = mana

    def __str__(self):
        return f"{self.name}"

    def cure_wounds(self):
        return d6() + 1

    def magic_missiles(self):
        return d6() + 1

def battle(wizards):
    attacker = wizards[randint(0,2)]
    attackee = wizards[randint(0,2)]
    while attacker == attackee:
        attackee = wizards[randint(0,2)]
    
    dmg = attacker.magic_missiles()
    attackee.damage(dmg)
    print(f"{attacker} attacks {attackee} doing {dmg} damage")

### BELOW NOT WORKING YET (HEALING) ###
    #for x in range(len(wizards)):
        #if (wizards[x].hp / wizards[x].max_hp) * 100 < 75:
            #heal = wizards[x].cure_wounds()
            #wizards[x].heal(heal)
            #print(f"{wizards[x]} heals for {heal} health")
    
def main():
    first_wizard = MagicUser("Blue wizard", randint(8, 12), randint(8, 12))
    second_wizard = MagicUser("Red wizard", randint(8, 12), randint(8, 12))
    third_wizard = MagicUser("Green wizard", randint(8, 12), randint(8, 12))

    wizards = [first_wizard, second_wizard, third_wizard]

    battle(wizards)

    print(f"{first_wizard.name}\t{first_wizard.hp}\n{second_wizard.name}\t{second_wizard.hp}\n{third_wizard.name}\t{third_wizard.hp}")

    for x in range(len(wizards)):
        wizards[x].heal(wizards[x].cure_wounds())

    print(f"{first_wizard.name}\t{first_wizard.hp}\n{second_wizard.name}\t{second_wizard.hp}\n{third_wizard.name}\t{third_wizard.hp}")

if __name__ == '__main__':
    main()
    