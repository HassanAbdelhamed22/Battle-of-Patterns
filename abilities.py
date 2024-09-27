from abc import ABC, abstractmethod

class Ability(ABC):
    @abstractmethod
    def apply(self, character):
        pass

    @abstractmethod
    def is_expired(self):
        pass
    
    @abstractmethod
    def reduce_turns(self):
        pass
    
    @abstractmethod
    def expire(self, character):
        pass
    
class AbilityDecorator(Ability):
    def __init__(self, ability):
        self._ability = ability

    def apply(self, character):
        self._ability.apply(character)

    def is_expired(self):
        return self._ability.is_expired()

    def reduce_turns(self):
        self._ability.reduce_turns()

    def expire(self, character):
        self._ability.expire(character)

class IncreasedAttackPower(Ability):
    def __init__(self, boost, duration):
        self.boost = boost
        self.duration = duration
        self.turns_left = duration

    def apply(self, character):
        character.attack_boost += self.boost
        character.notify_observers(f"{character.__class__.__name__} gained increased attack power for {self.turns_left} turns!")
        print(f"Applying {self.__class__.__name__} to {character.__class__.__name__}")

    def is_expired(self):
        return self.turns_left <= 0

    def reduce_turns(self):
        self.turns_left -= 1
        
    def expire(self, character):
        character.attack_boost -= self.boost
        character.notify_observers(f"{character.__class__.__name__}'s attack boost expired.")

class Shield(Ability):
    def __init__(self, duration):
        self.duration = duration
        self.turns_left = duration

    def apply(self, character):
        character.shielded = True
        character.notify_observers(f"{character.__class__.__name__} activated shield for {self.turns_left} turns!")
        print(f"Applying {self.__class__.__name__} to {character.__class__.__name__}")

    def is_expired(self):
        return self.turns_left <= 0

    def reduce_turns(self):
        self.turns_left -= 1
        
    def expire(self, character):
        character.shielded = False
        character.notify_observers(f"{character.__class__.__name__}'s shield expired.")

class Speed(Ability):
    def __init__(self, dodge_increase, duration):
        self.dodge_increase = dodge_increase
        self.duration = duration
        self.turns_left = duration
        self.original_dodge_rate = None

    def apply(self, character):
        self.original_dodge_rate = character.dodge_success_rate
        character.dodge_success_rate += self.dodge_increase
        character.notify_observers(f"{character.__class__.__name__} gained speed for {self.turns_left} turns!")
        print(f"Applying {self.__class__.__name__} to {character.__class__.__name__}")
        
    def is_expired(self):
        return self.turns_left <= 0

    def reduce_turns(self):
        self.turns_left -= 1

    def expire(self, character):
        character.dodge_success_rate = self.original_dodge_rate
        character.notify_observers(f"{character.__class__.__name__}'s speed boost expired.")
