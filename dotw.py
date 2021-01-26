from dice import d6
from random import randint

class Creature:
    def __init__(self, name, max_hp):
        self.name = name
        self.max_hp = max_hp
        self.hp = self.max_hp
        self.dead = False
        self.mana_starved = False

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
        heal_amount = d6() + 1
        print(f"{self.name} healed for {heal_amount} health")
        Creature.heal(self, heal_amount)

    def magic_missiles(self, attackee):
        dmg_amount = d6() + 1
        print(f"{self.name} attacks {attackee} doing {dmg_amount} damage")
        return dmg_amount

def determine_action(wizards):
    if wizards.hp < 3:
        action = 1
    else:
        action = 0
    return action

def battle(wizards):
    battle_round = 1

    print(f"Round {battle_round}!")
    while True:
        for x in range(len(wizards)):
            action = determine_action(wizards[x])
            wizards[x].mana -= 1

            if action == 0 and wizards[x].mana_starved != True and wizards[x].dead != True:
                attackee = choose_attackee(wizards, wizards[x])
            
                dmg = wizards[x].magic_missiles(attackee)
                attackee.damage(dmg)
            elif action == 1 and wizards[x].mana_starved != True and wizards[x].dead != True:
                wizards[x].cure_wounds()

            death_check(wizards)

            if x == 2:
                if battle_round > 9:
                    quit()
                battle_round += 1
                print(f"Round {battle_round}!")

            

def choose_attackee(wizards, attacker):
    attackee = wizards[randint(0,2)]
    while attacker == attackee or attackee.dead == True:
        attackee = wizards[randint(0,2)]
    return attackee

def death_check(wizards):
    counter = 0
    for x in range(len(wizards)):
        if wizards[x].hp <= 0:
            if wizards[x].dead != True:
                print(f"{wizards[x].name} died!")
            wizards[x].dead = True
        if wizards[x].mana <= 0:
            if wizards[x].dead != True and wizards[x].mana_starved != True:
                print(f"{wizards[x].name} is mana starved!")
            wizards[x].mana_starved = True

    for x in range(len(wizards)):
        if wizards[x].dead == True:
            counter += 1
        if counter >= 2:
            for i in range(len(wizards)):
                if wizards[i].dead == False:
                    winner = wizards[i]
            print(f"Game over! {winner} won with Stats: HP = {winner.hp}/{winner.max_hp}"
                f" Mana = {winner.mana}")
            quit()
                

    ### BELOW NOT WORKING YET (HEALING) ###
        #for x in range(len(wizards)):
            #if (wizards[x].hp / wizards[x].max_hp) * 100 < 75:
                #heal = wizards[x].cure_wounds()
                #wizards[x].heal(heal)
                #print(f"{wizards[x]} heals for {heal} health")
    
def main():
    first_wizard = MagicUser("Blue wizard", randint(8, 12), randint(4, 10))
    second_wizard = MagicUser("Red wizard", randint(8, 12), randint(4, 10))
    third_wizard = MagicUser("Green wizard", randint(8, 12), randint(4, 10))

    wizards = [first_wizard, second_wizard, third_wizard]

    battle(wizards)

if __name__ == '__main__':
    main()
    