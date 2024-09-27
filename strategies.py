from abc import ABC, abstractmethod

from config import HEAVY_ATTACK_DAMAGE, LIGHT_ATTACK_DAMAGE

class AttackStrategyInterface(ABC):
    @abstractmethod
    def execute(self):
        pass

class AttackStrategy(AttackStrategyInterface):
    def execute(self):
        raise NotImplementedError("Execute method not implemented")

class LightAttack(AttackStrategy):
    def execute(self):
        return LIGHT_ATTACK_DAMAGE

class HeavyAttack(AttackStrategy):
    def execute(self):
        return HEAVY_ATTACK_DAMAGE