from character.player import Player
from character.enemy import Enemy
from observers import GameLogObserver, GameSubject
from strategies import LightAttack, HeavyAttack
from random import randint
from utilities import random_ability

class Game(GameSubject):
    def __init__(self):
        super().__init__()
        self.player = Player()
        self.enemy = Enemy()
        self.turn_count = 0

    def player_turn(self):
        self.notify_observers("Player's Turn:")
        print("\nChoose your action:")
        print("1: Attack")
        print("2: Defend")
        print("3: Dodge")

        choice = input("Enter the number of your choice: ")
    
        if choice == "1":
            print("\nChoose your attack strategy:")
            print("1: Light Attack")
            print("2: Heavy Attack")

            attack_choice = input("Enter the number of your choice: ")

            if attack_choice == "1":
                selected_strategy = LightAttack()
                self.notify_observers("Player chose Light Attack.")
            elif attack_choice == "2":
                selected_strategy = HeavyAttack()
                self.notify_observers("Player chose Heavy Attack.")
            else:
                self.notify_observers("Invalid attack choice! You lose your turn.")
                return False  
        
            self.player.attack(selected_strategy, self.enemy)
            print(f"{self.enemy.__class__.__name__} health is now {self.enemy.get_health():.2f}.")

        elif choice == "2":
            self.player.defend()
            self.notify_observers("Player chose to defend.")

        elif choice == "3": 
            if self.player.dodge():  
                self.notify_observers("Player successfully dodged the attack!")
            else:
                self.notify_observers("Player failed to dodge the attack!")

        else:
            self.notify_observers("Invalid choice! You lose your turn.")
            return False

        granted_ability = random_ability(self.turn_count, self.player)
        if granted_ability:
            self.notify_observers(f"Player received a new ability: {granted_ability.__class__.__name__}")
            self.player.apply_ability(granted_ability)
        
        self.player.handle_abilities()
        self.player.end_turn()

        return True 

    def enemy_turn(self):
        self.notify_observers("Enemy's Turn:")
        action = randint(0, 3)
        
        if action == 0:  
            attack_type = HeavyAttack()
            self.enemy.attack(attack_type, self.player)
            self.notify_observers(f"Enemy attacked the player with {attack_type.__class__.__name__}. Player health is now {self.player.get_health():.2f}.")
        elif action == 1:
            attack_type = LightAttack()
            self.enemy.attack(attack_type, self.player)
            self.notify_observers(f"Enemy attacked the player with {attack_type.__class__.__name__}. Player health is now {self.player.get_health():.2f}.")        
        
        elif action == 2:
            self.enemy.defend()
            self.notify_observers("Enemy chose to defend.")

        elif action == 3:
            if self.enemy.dodge():
                self.notify_observers("Enemy successfully dodged the attack!")
            else:
                self.notify_observers("Enemy failed to dodge the attack!")

        self.enemy.end_turn()
        
    def game_loop(self):
        while self.player.is_alive() and self.enemy.is_alive():
            self.turn_count += 1
            print(f"\n=== Turn {self.turn_count} ===")
            
            valid_turn = self.player_turn()  
            if not valid_turn: 
                continue
        
            if not self.enemy.is_alive(): 
                break
        
            self.enemy_turn() 
            if not self.player.is_alive(): 
                break    

            print(f"\n{self.player.__class__.__name__} Health: {self.player.get_health():.2f}")
            print(f"{self.enemy.__class__.__name__} Health: {self.enemy.get_health():.2f}")

        if self.player.is_alive():
            print("\n🎉 Congratulations! You win! 🎉")
        else:
            print("\n💔 Game over! You lose. 💔")
            
if __name__ == "__main__":
    game = Game()
    logger = GameLogObserver()
    game.attach(logger)
    game.game_loop()
