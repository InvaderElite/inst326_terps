import sys
import random

class Gameplay:
    def __init__(self, player):
        self.player = player
        self.score = {player: 0}
        self.type = None
        self.counter = 0

    
    def select_class(self):
        for playername in self.player:
            class_type = str(input(f"{playername}, select a character class:"
                               " Tank, Warrior, Mage."))
            if class_type == "Tank" or "tank":
                self.type = Tank(playername)
            elif class_type == "Warrior" or "warrior":
                self.type = Warrior(playername)
            elif class_type == "Mage" or "mage":
                self.type = Mage(playername)
            else:
                raise ValueError
        
    def action(self):
        if self.type == Tank:
            choice = input("Choose an action: Attack or Defend. Stop to stop.")
            if choice == "Attack":
                self.attack()
                self.counter += 1
            elif choice == "Defend":
                self.defend()
                self.counter += 1
            elif choice == "Stop":
                print(f"The tutorial is over, go kick some butt!")
            else:
                raise ValueError
        if self.type == Mage:
            choice = input("Choose an action: Heal or Fireball. Stop to stop.")
            if choice == "Heal":
                self.heal()
                self.counter += 1
            elif choice == "Fireball":
                self.fireball()
                self.counter += 1
            elif choice == "Stop":
                print(f"The tutorial is over, go kick some butt!")
            else:
                raise ValueError
        if self.type == Warrior:
            choice = input("Choose an action: Attack or Guard. Stop to stop.")
            if choice == "Attack":
                self.attack()
                self.counter += 1
            elif choice == "Fireball":
                self.guard()
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
    turn_count = self.turns.groupby("")["Turns"].count()
    print("Total Player turns: ", turn_count)
    self.score_board.plot.bar(y = ["Total Damage",
                           "Total Defence", 
                           "Total Heal"], xlabel = "Player 1")

class BaseCharacter:
    """Standard character with default status and actions, is not used as a
    playable character but a template for character classes.
    
    Attributes:
        name (str): name of character
        health (int): health of character
        power (int): power level of character
        defense (int): characters level of defense
    """
    def __init__(self, name = "Character"):
        """Creates the character to be played on the field.
        
        Args:
            name (str): name of character
            
        Side effects:
            Sets the attributes of name, health, power, and defense.
        """
        self.name = name
        self.health = 100
        self.power = 0
        self.defense = 0
        self.total_dmg = 0
        self.total_def = 0
        self.total_heal = 0
        
    def attack(self):
        """Action to deal damage to an opponent. Deals damage according to what
        the character's power is currently at.
            
        Side effects:
            Writes to stdout that opponent has taken damage, changes the health
            of the opponent
        """
        self.power = random.randint(20, 40)
        print(f"{self.name} did {self.power} damage to the dummy!")
        self.total_dmg += self.power
        
    def taunt(self, num):
        """Action to taunt other characters, displays taunt in text form, can
        take another character to specify the taunt. Has multiple taunts that
        can be chosen or randomized.
        
        Args:
            other (BaseCharacter or Tank or Mage or Warrior): name of another
            character/player
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
          Writes to stdout
        """
        return str(
            f"{self.name}'s status:"
            f"Health: {self.health}"
            f"Power: {self.power}"
            f"Defense: {self.defense}"            
            )
        
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
     
        print(f"{self.name} used defend for the round and now has {new_health} health.")
        
    
    def attack(self, opponent):
        """Action to deal damage to an opponent. Deals damage according to what
        the character's power is currently at. Weakened for the tank class
        
        Args:
            opponent (BaseCharacter): other character
            
        Side effects:
            Writes to stdout that opponent has taken damage, changes the health
            of the opponent
        """
        self.power = random.randint(10, 20)
        return super().attack()
         
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
        nothing (pass). May right to stdout that mages cannot use the default
        attack?
        """
        print(f"{self.name} cannot use the default attack.")
        
    def fireball(self):
        """Action to attack another character, has more power than the default
        attack action. Unique to the mage class.

            
        Side effects:
            Writes out to stdout that the opponent was attacked, changes the
            health of the opponent attacked
        """
        self.power = random.randint(30, 60)
        return super().attack()
         
        
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
        stat and health to prevent possible damage from opponent. Unique to the warrior class.

        Side effects:
            Writes action to stdout
        """
        self.defense += 1

        base_health = BaseCharacter("random").health
        self.health = self.health + opponent.power
        if self.health > base_health + opponent.power:
            self.health = base_health + opponent.power

        return f"{self.name} is going to defend!"

    def __str__(self):
        return "Class: Warrior"
 
def class_sheet(filepath):
    """Opens a csv file containing the different classes and their move set
    Args:
        Filepath: a path to a file"""
    with open(filepath, "r", encoding = "utf-8") as f:
        char_class = f.readlines()
        return char_class
       


def main(player1, player2):
    """ Allows user to create their character and begin the game. User-input 
    allows users to select their actions and conditional statements determines 
    how those actions affect the other players. Returns print statements that
    shows users which player is playing, theaction they chose, and the effect
    it caused.
    
    Args:
        p1_name (BaseCharacter): Character object of player 1.
        p2_name (BaseCharacter): Character object of player 2.
        
    Side effects:
        Writes out to stdout the player that is playing, the action they chose,
        and the effect of those actions. 
    """
    player1 = Gameplay()
    player1.select_class("Bob")
            
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
   parser = argparse.ArgumentParser()
   parser.add_argument('p1_name', type=str, help="Please enter Player 1 name")
   parser.add_argument('p2_name', type=str, help="Please enter Player 2 name")
   parser.add_argument('p3_name', type=str, help="Please enter Player 3 name")
   args = parser.parse_args(args_list)
   return args
   
 
if __name__ == '__main__':
    """
    play() function calling, the driver code to play the game
    """
    main()
    
    #have function that takes in both player1 and player2
    #input() function, storing a variable as the user input
    #input() function to prompt turn-based input
    #dataframe, don't worry too much about this
    #finish character classes first, don't focus so so much on the dataframes 
    #dataframe population should be a simple plug and chug of values and attributes
    #keep things simple, don't confuse ourselves too much
    #set operations ideas = getting rid of duplicate values
    