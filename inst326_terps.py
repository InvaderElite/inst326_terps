import sys


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
        
    def attack(self, opponent):
        """Action to deal damage to an opponent. Deals damage according to what
        the character's power is currently at.
        
        Args:
            opponent (BaseCharacter): other character
            
        Side effects:
            Writes to stdout that opponent has taken damage, changes the health
            of the opponent
        """
        
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
    
    def status(self):
            """Returns the characters' name, health, power, and defense to
        the user.

        Side effects:
          Writes to stdout
     """
        
        
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
        
    def defend(self):
        """Action to defend against possible incoming damage, lasts one turn,
        would add temporary health to the character. Unique to the tank class.
           
        Side effects:
            Writes to stdout that character has defended for the round, and adds
            health to character
        """
    
    def attack(self, opponent):
        """Action to deal damage to an opponent. Deals damage according to what
        the character's power is currently at. Weakened for the tank class
        
        Args:
            opponent (BaseCharacter): other character
            
        Side effects:
            Writes to stdout that opponent has taken damage, changes the health
            of the opponent
        """
        
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
        
class Warrior(BaseCharacter):
    """Warrior class of the base character. Has standard status and
    uses the default attack but also a roll action.
    
    Attributes:
        name (str): name of character
        health (int): health of character
        power (int): power level of character
        defense (int): characters level of defense
    """
    def roll(self):
        """Action to roll and have a chance to dodge any incoming attack. If
        there is no attack, 100% dodge rate. Unique to warrior class.
        
        Side effects:
            Writes action to stdout
        """

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
    shows users which player is playing, the action they chose, and the effect
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