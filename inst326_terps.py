import sys

class Gameplay:
    def __init__(self, playerlist):
        self.players = playerlist
    
    def select_class(self):
        self.contestants = []
        for playername in self.players:
            class_type = input(f"{playername}, select a character class:"
                               " Tank, Warrior, Mage.")
            if class_type == "Tank":
                self.type = Tank(playername)
                self.contestants.append((playername, str(self.type)))                
            elif class_type == "Warrior":
                self.type = Warrior(playername)
                self.contestants.append((playername, str(self.type)))
            elif class_type == "Mage":
                self.type = Mage(playername)
                self.contestants.append((playername, str(self.type)))
            else:
                raise ValueError
            return self.contestants
            
    def new_game(self):
        self.players.clear()
        self.contestants.clear()
        
    def play_game(self):
        self.new_game()
        

class Players:
    def __init__(self, playerlist):
        

class BaseCharacter:
    """Standard character with default status and actions, is not used as a
    playable character but a template for character classes.
    
    Attributes:
        name (str): name of character
        health (int): health of character
        power (int): power level of character
        defense (int): characters level of defense
    """
    def __init__(self, name):
        """Creates the character to be played on the field.
        
        Args:
            name (str): name of character
            
        Side effects:
            Sets the attributes of name, health, power, and defense.
        """
        self.name = name
        self.health = 100
        self.power = 20
        self.defense = 0
        
    def attack(self, opponent):
        """Action to deal damage to an opponent. Deals damage according to what
        the character's power is currently at.
        
        Args:
            opponent (BaseCharacter): other character
            
        Side effects:
            Writes to stdout that opponent has taken damage, changes the health
            of the opponent
        """
        if opponent.health != 0:
            remaining_health = opponent.health - self.power           
            return f"{self.name} attacked {opponent.name} and did {self.power} \
                    damage. {opponent.name} has {remaining_health}HP left."
        elif opponent.health ==0:
            return f"{opponent.name} has fallen and can no longer fight."
        
    def taunt(self, num,  other = None):
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
        return f"{self.name} taunts {other.name}: {taunts[num]}"
    
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
    def __init__(self, name):
        """Sets the status of the tank character, uses the base character stats
        but with more health and less power.
        
        Args:
            name (str): name of character
            
        Side effects:
            Sets the attributes of name, health, power, and defense.
        """
        
        self.name = name 
        self.health = 125
        self.power = 10
        self.defense = 0
        
    def defend(self):
        """Action to defend against possible incoming damage, lasts one turn,
        would add to the defense stat. Unique to the tank class.
           
        Side effects:
            Writes to stdout that character has defended for the round, and adds
            health to character
        """
        temp_health = 20
        remaining_health = self.health + temp_health
        return f"{self.name} used defend for the round!"
        
    
    def attack(self, opponent):
        """Action to deal damage to an opponent. Deals damage according to what
        the character's power is currently at. Weakened for the tank class
        
        Args:
            opponent (BaseCharacter): other character
            
        Side effects:
            Writes to stdout that opponent has taken damage, changes the health
            of the opponent
        """
        super().attack(self.name)
        return f"{self.opponent} took damage!"
         
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
    def __init__(self):
        """Sets the status of the mage character, uses the base character stats
        but with more power and less health.
        
        Args:
            name (str): name of character
            
        Side effects:
            Sets the attributes of name, health, power, and defense.
        """
        
    def attack(self):
        """Does nothing. Overrides the parent class method but makes it do
        nothing (pass). May right to stdout that mages cannot use the default
        attack?
        """
        
    def fireball(self, opponent):
        """Action to attack another character, has more power than the default
        attack action. Unique to the mage class.
        
        Args:
            opponent (BaseCharacter or Tank or Mage or Warrior): name of another
            character/player
            
        Side effects:
            Writes out to stdout that the opponent was attacked, changes the
            health of the opponent attacked
        """
        
    def heal(self):
        """Heals a small amount of the user's permanent health. Unique to the
        mage class
        
        Side effects:
            changes the characters health
        """
        
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
    def guard(self):
        """Action to defend an incoming attack. Will add to characters defense
        stat. Unique to the warrior class.
        
        Side effects:
            Writes action to stdout
        """
    def __str__(self):
        return "Class: Warrior"
        
def socreboard_creation(): 
    """
    This function will create dataframe that will act as a scorboard for the 
    game. It will have room for x amount of players and ranks 1-x, but will not 
    have any players within the dataframe yet, simply the format 
    Return: will return the data frame """ 
    
def socreboard_population(socreboard_df): 
    """
    This function will take in the socreboard created in scoreboard_creation,
    and after that, it will modify the dataframe and add x amount of
    players, ranking them first to last place 

    Returns: This will return the data frame 
         with the players and their ranks
    """



def main(p1_name, p2_name, p3_name):
    """ Allows user to create their character and begin the game. User-input 
    allows users to select their actions and conditional statements determines 
    how those actions affect the other players. Returns print statements that
    shows users which player is playing, theaction they chose, and the effect
    it caused.
    
    Args:
        p1_name (BaseCharacter): Character object of player 1.
        p2_name (BaseCharacter): Character object of player 2.
        p3_name (BaseCharacter): Character object of player 3.
        
    Side effects:
        Writes out to stdout the player that is playing, the action they chose,
        and the effect of those actions. 
    """
            
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
    play() 
    
    #have function that takes in both player1 and player2
    #input() function, storing a variable as the user input
    #input() function to prompt turn-based input
    #dataframe, don't worry too much about this
    #finish character classes first, don't focus so so much on the dataframes 
    #dataframe population should be a simple plug and chug of values and attributes
    #keep things simple, don't confuse ourselves too much
    #set operations ideas = getting rid of duplicate values
    