class BaseCharacter:
    """Standard character with default status and actions
    
    Attributes:
        name (str): name of character
        health (int): health of character
        power (int): power level of character
        defense (int): characters level of defense
        
    """
    def __init__(self, name):
        """Creates the character to be played on the field
        
        Args:
            name (str): name of character
            
        """
        
    def attack(self, opponent):
        """Move to deal damage to an opponent.
        
        Args:
            opponent (BaseCharacter): other character
            
        Side effects:
            Writes to stdout that opponent has taken damage
        """
        
        
class Tank(BaseCharacter):
    """Tank class variation of base character, has more health, less
    power. Has an additional defense ability.
    
    Attributes:

    """
    def __init__(self, name):
        """Sets the status of the tank character, uses the base character stats
        but with more health and less power.
        
        Args:
            name (str): name of character
        """
        
    def defend(self):
        """Action to defend against possible incoming damage, lasts one turn,
        would add temporary health to the character 
           
        Side effects:
            Writes to stdout that character has defended for the round, and adds
            health to character
        """
        
class Mage(BaseCharacter):
    """Magic caster variation of base character, but has more power, and less
    health. Has no standard attack action, but two casting actions.
    
    Attributes:

    """
    def __init__(self):
        """Sets the status of the tank character, uses the base character stats
        but with more power and less health.
        
        Args:
            name (str): name of character
        """
        
    def fireball(self, opponent):
        """Action to attack 
        """
        
def socreboard_creation(): 
    """This function will create dataframe that will act as a scorboard for the 
        game. It will have room for x amount of players and ranks 1-x, but will not 
        have any players within the dataframe yet, simply the format 
        Return: will return the data frame """ 
    
def socreboard_population(socreboard_df): 
    """This function will take in the socreboard created in scoreboard_creation,
        and after that, it will modify the dataframe and add x amount of players , 
        ranking them first to last place 
    
    Returns: This will return the data frame 
            with the players and their ranks"""