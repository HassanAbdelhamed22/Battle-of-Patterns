from character.character import Character
from config import PLAYER_INITIAL_HEALTH, DODGE_SUCCESS_RATE

class Player(Character):
    def __init__(self):
        super().__init__(PLAYER_INITIAL_HEALTH)
        self.attack_boost = 0
        self.defense_boost = 0
        self.dodge_success_rate = DODGE_SUCCESS_RATE
        self.abilities = []
    
    def apply_ability(self, ability):
        self.abilities.append(ability)
        ability.apply(self)
        self.notify_observers(f"Player gained {ability.__class__.__name__} ability!")

    def handle_abilities(self):
        for ability in self.abilities:
            ability.reduce_turns()
            if ability.is_expired():
                ability.expire(self)
        
        self.abilities = [ability for ability in self.abilities if not ability.is_expired()]

    def end_turn(self):
        self.handle_abilities()
        super().end_turn()
