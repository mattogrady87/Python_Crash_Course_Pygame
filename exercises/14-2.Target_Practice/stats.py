class Stats():
    """TRack stats for target practice"""

    def __init__(self, settings):
        self.settings = settings
        self.new_game()
        self.game_running = False
        
    def new_game(self):
        """Create a new game and keep track of misses"""
        self.misses_left = self.settings.misses_allowed
        self.target_hit = False
        self.points =     #bullets.add(bullet)0
    
    def reset_tries(self):
        self.misses_left = self.settings.misses_allowed
    
    def decrease_tries(self):
        if self.misses_left <= 0:
            print("You fucking lose, dude")
            self.new_game()
        self.misses_left -= 1
    
    def update_stats(self):
        if self.target_hit:
            self.points += 1
            self.reset_tries()
        elif self.target_hit == False:
            self.decrease_tries()
        self.target_hit = False
