import sys
import random
from argparse import ArgumentParser
import pandas as pd

class Gameplay:
    def __init__(self, player):
        self.player = player
        self.score = {player: 0}
        self.type = None
        self.counter = 0

    
    def select_class(self):
        class_type = str(input(f"{self.player}, select a character class:"
                            " Tank, Warrior, Mage.  "))
        if class_type == "Tank" or "tank":
            self.type = Tank(self.player)
        elif class_type == "Warrior" or "warrior":
            self.type = Warrior(self.player)
        elif class_type == "Mage" or "mage":
            self.type = Mage(self.player)
        else:
            raise ValueError
        
    def action(self):
        if self.type == Tank:
            choice = input("Choose an action: Attack, Defend, or Taunt. "
                        "Stop to stop.  ")
            if choice == "Attack":
                self.attack()
                self.counter += 1
            elif choice == "Defend":
                self.defend()
                self.counter += 1
            elif choice == "Taunt":
                num = int(input("Select a number 0-4"))
                self.taunt(num)
                self.counter += 1
            elif choice == "Stop":
                print(f"The tutorial is over, go kick some butt!")
            else:
                raise ValueError
        elif self.type == Mage:
            choice = input("Choose an action: Fireball, Heal, or Taunt. "
                        "Stop to stop.  ")
            if choice == "Heal":
                self.heal()
                self.counter += 1
            elif choice == "Fireball":
                self.fireball()
                self.counter += 1
            elif choice == "Taunt":
                num = int(input("Select a number 0-4"))
                self.taunt(num)
                self.counter += 1
            elif choice == "Stop":
                print(f"The tutorial is over, go kick some butt!")
            else:
                raise ValueError
        elif self.type == Warrior:
            input("Choose an action: Attack, Guard, or Taunt. "
                        "Stop to stop.  ")
            if choice == "Attack":
                self.attack()
                self.counter += 1
            elif choice == "Guard":
                self.guard()
                self.counter += 1
            elif choice == "Taunt":
                num = int(input("Select a number 0-4"))
                self.taunt(num)
                self.counter += 1
            elif choice == "Stop":
                print(f"The tutorial is over, go kick some butt!")
            else:
                raise ValueError
            
                
    def scoreboard_creation(self):
        """Creates two dataframes, one containing player stats and one containing
        total actions preformed"""
        self.action()
        self.attack()
        self.defend()
        self.heal()
    
        self.score_board = pd.DataFrame({"Total Damage": [self.total_dmg],
                             "Total Defence": [self.total_def],
                             "Total Heal":[self.total_heal],})
        self.turns = pd.DataFrame({"": "","Turns":self.counter})
  
def scoreboard_visual(self):
    """Takes the two dataframes, and visualzes the player stats using a bar 
    graph, and using groupby, counts total player actions"""
    self.scoreboard_creation()
    turn_count = self.counter.groupby("")["Turns"].count()
    print("Total Player turns: ", turn_count)
    self.score_board.plot.bar(y = ["Total Damage",
                           "Total Defence", 
                           "Total Heal"], xlabel = "Player 1")

class BaseCharacter:
    """Standard character with default status and actions, is not used as a
    playable character but a template for character classes.
    
    Attributes:
        name (str): name of character.
        health (int): health of character.
        power (int): power level of character.
        defense (int): characters level of defense.
        total_dmg (int): total damage from the character.
        total_def (int): total defense from the character.
        total_heal (int): total heal from the character.
    """
    def __init__(self, name = "Character"):
        """Creates the character to be played on the traning ground.
        
        Args:
            name (str): name of character.
            
        Side effects:
            Sets the attributes of name, health, power, defense, total_dmg,
            total_def, and total_heal.
        """
        self.name = name
        self.health = 100
        self.power = 0
        self.defense = 0
        self.total_dmg = 0
        self.total_def = 0
        self.total_heal = 0
        
    def attack(self):
        """Action to deal damage to a dummy target. Deals damage according to 
        what the character's power is currently at.
            
        Side effects:
            Writes to stdout that the dummy target has taken damage, changes the 
            health of the opponent.
        """
        self.power = random.randint(20, 40)
        self.total_dmg += self.power
        print(f"{self.name} did {self.power} damage to the dummy!")

    def taunt(self, num):
        """Action to taunt the dummy target, displays taunt in text form. Has 
        multiple taunts that can be chosen or randomized by indicating the index
        of the taunts list.
         
        Args:
            num (int): position of taunt that is selected
            
        Side effects:
            Writes to stdout
        """
        taunts = [
            "You are no match for me!",
            "I'll end this here!",
            "Come on!",
            "This was too easy.",
            "Go back to the tutorial, noob."
        ]
        print(f"{self.name} taunts: {taunts[num]}")
    
    def status(self):
        """Returns the characters' name, health, power, and defense to
        the user.

        Side effects:
          Writes to stdout.
          
        Returns:
            message (str): the player's status, including their health, power
            and defense
        """
        message = str(
            f"{self.name}'s status:"
            f"Health: {self.health}"
            f"Power: {self.power}"
            f"Defense: {self.defense}"            
            )
        
        return message
        
class Tank(BaseCharacter):
    """Tank class variation of base character, has more health, less
    power. Has an additional defense ability.
    
    Attributes:
        name (str): name of character
        health (int): health of character
        power (int): power level of character
        defense (int): characters level of defense
    """

    def defend(self):
        """Action to defend against possible incoming damage, lasts one turn,
        would add to the defense stat. Unique to the tank class.
           
        Side effects:
            Writes to stdout that character has defended for the round, and adds
            health to character
        """
        self.defense = 20
        if self.health < 150:
            new_health = self.health + self.defense
        elif self.health >= 150:
            self.health = 150
            return f"{self.name} is at max health."
        self.total_def += self.defense
     
        print(f"{self.name} used defend for the round and now has {new_health} \
              health.")
        
    
    def attack(self):
        """Action to deal damage to the dummy target. Deals damage according to 
        what the character's power is currently at. Weakened for the tank class.
        
        Returns: 
            tank_attack (str): outputs a message that describes the amount 
            of damage the character did to the dummy target

        """
        self.power = random.randint(10, 20)
        tank_attack = super().attack()
        return tank_attack
         
    def __str__(self):
        return "Class: Tank"
    
class Mage(BaseCharacter):
    """Magic caster variation of base character, but has more power, and less
    health. Has no standard attack action, but two casting actions.
    
    Attributes:
        name (str): name of character
        health (int): health of character
        power (int): power level of character
        defense (int): characters level of defense
    """
    
    def attack(self):
        """Does nothing. Overrides the parent class method but makes it do
        nothing (pass). 
        
        Side effects: 
            Write to stdout that mages cannot use the default attack.
        """
        print(f"{self.name} cannot use the default attack.")
        
    def fireball(self):
        """Action to attack the dummy target, has more power than the default
        attack action. Unique to the mage class.
            
        Returns:
            tank_attack (str): outputs a message that describes the amount 
            of damage the character did to the dummy target
        """
        self.power = random.randint(30, 60)
        mage_attack = super().attack()
        return mage_attack
         
    def heal(self):
        """Heals a small amount of the user's permanent health. Unique to the
        mage class
        
        Side effects:
            changes the characters health
        """
        heal_value = 20
        if self.health < 150:
            self.health += heal_value
        elif self.health >= 150: 
            self.health = 150
            return f"{self.name} is at max health."
        self.total_heal += heal_value
        
    def __str__(self):
        return "Class: Mage"
    
class Warrior(BaseCharacter):
    """Warrior class of the base character. Has standard status and
    uses the default attack but also has a guard action.

    Attributes:
        name (str): name of character
        health (int): health of character
        power (int): power level of character
        defense (int): characters level of defense
    """

    def guard(self, opponent):
        """Action to defend an incoming attack. Will add to characters defense
        stat and health to prevent possible damage from opponent. Unique to the 
        warrior class.

        Returns:
            str: states that the character will be defending this round
        """
        self.defense += 10

        base_health = BaseCharacter("random").health
        self.health = self.health + opponent.power
        if self.health > base_health + opponent.power:
            self.health = base_health + opponent.power

        return f"{self.name} is going to defend!"

    def __str__(self):
        return "Class: Warrior"    


def main(filepath, player1):
    """ Allows user to create their character and begin the game. User-input 
    allows users to select their actions and conditional statements determines 
    how those actions affect the other players. Returns print statements that
    shows users which player is playing, theaction they chose, and the effect
    it caused.
    
    Args:
        filepath (str): csv file of a character sheet class that gives details 
        of each character class
        player1 (BaseCharacter): Character object of player1
    """
    with open(filepath, "r", encoding = "utf-8") as f:
        for line in f:
            file = line.strip()
            print(file)
    player = Gameplay(player1)
    player.select_class()
    player.action()
            
def parse_args(args_list):
   """Parse command line arguments
  
   Expect three mandatory arguments:
       - str: player 1 name
       - str: player 2 name
       - str: player 3 name
  
   Args:
       arglist (list of str): arguments from the command line
  
   Returns:
       agrument vaules
   """
   parser = ArgumentParser()
   parser.add_argument('filename', type = str, help = "Please enter a file name")
   parser.add_argument('p1_name', type=str, help="Please enter a Player name")
   args = parser.parse_args(args_list)
   return args
   
 
if __name__ == '__main__':
    """
    main() function calling, the driver code to play the game
    """
    args = parse_args(sys.argv[1:])
    main(args.filename, args.p1_name)
    