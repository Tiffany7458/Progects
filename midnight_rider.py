# Midnight Rider
import random
import sys
import textwrap
import time
import midnight_rider_text

# A text-based game of intrigue and illusion
MAX_FUEL = 50
MAX_TOFU = 3
MAX_HUNGER = 50

ENDGAME_REASON = {
    "LOSE_AGENTS": 1,
    "LOSE_FUEL": 2,
}

class Game:
    """Represent our game engine

    Attribute:
        done: describe if the game is finish or not - bool
        distance_traveled: describe the distance that we've traveled so far this game, in km
        amount_of_tofu: how much tofu we have left in our inventory
        agents_distance: described the distance between the player and the agents
        fuel: describes amount of fuel remaining, starts off at 50
        hunger: describes how hungry our player is, represented by a number between 0 - 50,
            if hunger goes beyond, game is over
        endgame_reason: shows the index of the games ending text from midnight_rider_text.py
    """
    def __init__(self):
        self.done = False
        self.distance_traveled = 0
        self. amount_of_tofu = MAX_TOFU
        self.agents_distance = -20
        self.fuel = MAX_FUEL
        self.hunger = 0
        self.endgame_reason = 0

    def introduction(self) -> None:
        """Print the introduction text"""
        self.typewriter_effect(midnight_rider_text.INTRODUCTION)

    def typewriter_effect(self, text: str) -> None:
        """Print out to console with a typewriter effect."""
        for char in textwrap.dedent(text):
            time.sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()

    def show_choices(self) -> None:
        """Show the user their choices"""
        print(midnight_rider_text.CHOICES)
        time.sleep(1)

    def get_choice(self) -> None:
        """Gets the user's choice and changes the environment"""
        # Get the user's response
        user_choice = input().strip(",.?!").lower()
        # Base on their choice, change the attributes of the class
        agents_distance_now = random.randrange(7, 15)
        if user_choice == "a":
            if self.amount_of_tofu > 0:
                self.amount_of_tofu -= 1
                self.hunger = 0
                print(midnight_rider_text.EAT_TOFU)
            else:
                print(midnight_rider_text.NO_TOFU)
        if user_choice == "b":
            slow_traveling = random.randrange(2, 7)
            self.distance_traveled += slow_traveling
            self.agents_distance += agents_distance_now - slow_traveling
            self.fuel -= random.randrange(1, 5)
            print(f"\n-----You drive conservation")
            print(f"-------YOU TRAVELED {self.distance_traveled} kms")
        if user_choice == "c":
            # Move the player
            player_distance_now = random.randrange(10, 16)
            self.distance_traveled += player_distance_now
            # Move the agents
            self.agents_distance += agents_distance_now - player_distance_now
            # Burn fuel
            self.fuel -= random.randrange(5, 11)
            # Give the player some feedback
            print(f"\n-------ZOOOOOOOOOOM.")
            print(f"-------YOU TRAVELED {self.distance_traveled} kms")
        elif user_choice == "d":
            self.fuel = MAX_FUEL
            self.agents_distance += agents_distance_now
            print(midnight_rider_text.REFUEL)
            time.sleep(2)
        if user_choice == "e":
            print("---Status Check---")
            print(f"Distance Traveled:{self.distance_traveled} kms")
            print(f"Fuel remaining: {self.fuel} L")
            print(f"Tofu Pieces Left {self.amount_of_tofu}")
            print(f"Agent's Distance {abs(self.agents_distance)} km behind")
            print("------")
            time.sleep(2)
        elif user_choice == "q":
            self.done = True

    def upkeep(self) -> None:
        """Give the user remainders of hunger"""
        if self.hunger > 40:
            print(midnight_rider_text.SEVERE_HUNGER)
        elif self.hunger > 25:
            print(midnight_rider_text.HUNGER)

    def check_endgame(self) -> None:
        """Check to see if win/lose conditions are met.
        If they're met, change the self.done flag."""
        if self.agents_distance >= 0:
            # Allows us to quit the while loop
            self.done = True
            # Help with printing the right ending
            self.endgame_reason = ENDGAME_REASON["LOSE_AGENTS"]
        if self.fuel <= 0:
            self.done = True
            self.endgame_reason = ENDGAME_REASON["LOSE_FUEL"]
def main() -> None:
    game = Game()  #starting a new game
    # game.introduction()


    # Main Loop:
    while not game.done:
        game.upkeep()
        game.show_choices()
        game.get_choice()
        game.check_endgame()

    time.sleep(3)
    # Print out the ending
    game.typewriter_effect(
        midnight_rider_text.ENDGAME_TEXT[game.endgame_reason]
    )
if __name__ == "__main__":
    main()
