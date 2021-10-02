class GameStats:

    """Track statistics for alien invasion"""

    def __init__(self, ai_game):
        """Initialize Statistics"""

        self.settings = ai_game.settings
        self.reset_stats()
        # Start alien invasion in an active state
        self.game_active = False
        self.high_score = 0
        self.level = 1

    def reset_stats(self):
        """Initializing the statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0