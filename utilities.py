import random
from abilities import IncreasedAttackPower, Shield, Speed
from config import RANDOM_ABILITIES_TURNS


def random_ability(turn_count, player):
        if turn_count % RANDOM_ABILITIES_TURNS == 0:
            ability = random.choice([
                IncreasedAttackPower(boost=5, duration=1),
                Shield(duration=1),
                Speed(duration=1, dodge_increase=75)
            ])
            player.apply_ability(ability)
            return ability
        return None