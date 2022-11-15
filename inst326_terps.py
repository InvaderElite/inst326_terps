class BaseCharacter:
    """Standard character with default status
    
    Attributes:
        name (str): name of character
        health (int): health of character
        power (int): power level of character
        defense (int): characters level of defense
        
    """
    def __init__(self,):
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
        
    
    def defend(self):
        """Move to defend against possible incoming damage, lasts one turn
        
        Side effects:
            Writes to stdout that character has defended for the round
        """
        
class Tank(BaseCharacter):
    """Tank class variation of base character, has more health and defense, less
    power
    """
    def __init__(self, ):
        """Sets the status of the tank character
        """