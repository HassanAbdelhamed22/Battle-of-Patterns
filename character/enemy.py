from character.character import Character
from config import ENEMY_INITIAL_HEALTH

class Enemy(Character):
    def __init__(self):
        super().__init__(ENEMY_INITIAL_HEALTH)
        
