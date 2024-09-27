from observers import GameSubject
from random import randint
from config import DODGE_SUCCESS_RATE
from strategies import AttackStrategyInterface

class Character(GameSubject):
    def __init__(self, health):
        super().__init__()
        self.health = health
        self.defense = False
        self.attack_boost = 0
        self.shielded = False
        self.dodge_success_rate = DODGE_SUCCESS_RATE
        
    def take_damage(self, damage):
        print(f"{self.__class__.__name__} is taking damage: {damage}")
        if self.shielded:
            damage *= 0.5
            self.shielded = False
        if self.defense:
            damage *= 0.5
        self.health -= damage
        print(f"{self.__class__.__name__} health after damage: {self.health:.2f}")
        self.health = max(self.health, 0)
        self.notify_observers(f"{self.__class__.__name__} took {damage:.2f} damage.")
        
    def attack(self, strategy: AttackStrategyInterface, opponent):
        # if opponent.dodge():
        #     self.notify_observers(f"{opponent.__class__.__name__} dodged the attack!")
        #     return         

        damage = strategy.execute() + self.attack_boost
        
        opponent.take_damage(damage)
        self.notify_observers(f"{self.__class__.__name__} attacked {opponent.__class__.__name__} for {damage:.2f} damage!")
            
    def defend(self):
        self.defense = True
        self.notify_observers(f"{self.__class__.__name__} is defending!")
        
    def end_turn(self):
        self.defense = False
        self.shielded = False
        
    def dodge(self):
        if randint(1, 100) <= self.dodge_success_rate:
            self.notify_observers(f"{self.__class__.__name__} successfully dodged the attack!")
            return True
        else:
            self.notify_observers(f"{self.__class__.__name__} failed to dodge the attack.")
            return False
        
    def is_alive(self):
        return self.health > 0
      
    def get_health(self):
        return self.health

