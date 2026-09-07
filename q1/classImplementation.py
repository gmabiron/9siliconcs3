class Sport:

    def __init__(
        self,
        name: str,
        inventor: str,
        games: int,
        condition: bool,
        score: int = 0,
    ):
        # Public attributes
        self.name = name
        self.inventor = inventor
        self.games = games

        # Private attributes
        self.__condition = condition  # Game readiness state
        self.__score = score  # Score must be safely managed

    # Method that returns information about a private attribute
    def is_game_ready(self) -> bool:
        return self.__condition

    # Method that reads private attribute state
    def get_score(self) -> int:
        return self.__score

    # Method receiving a parameter and safely modifying a private attribute
    def add_point(self, points: int):
        if points > 0:
            self.__score += points
            print(f"[{self.name}] Added {points} point(s) to score.")
        else:
            print("Points to add must be positive.")

    # Method modifying private condition state safely
    def start_game(self):
        if self.__condition:
            print(f"[{self.name}] The game has officially started!")
        else:
            print(f"[{self.name}] Cannot start: Game condition is False.")

    def end_game(self):
        self.__condition = False
        print(f"[{self.name}] The game has ended.")


basketball = Sport(
    name="Basketball", inventor="James Naismith", games=82, condition=True
)
volleyball = Sport(
    name="Volleyball", inventor="William G. Morgan", games=30, condition=True
)

print("--- BEFORE ---")
print(f"Basketball ({basketball.name}) Score: {basketball.get_score()}")
print(f"Volleyball ({volleyball.name}) Score: {volleyball.get_score()}")

print("\nPerforming action on Basketball...")
basketball.add_point(3)

print("\n--- AFTER ---")
print(f"Basketball ({basketball.name}) Score: {basketball.get_score()}")
print(f"Volleyball ({volleyball.name}) Score: {volleyball.get_score()}")