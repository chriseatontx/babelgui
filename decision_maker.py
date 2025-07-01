# decision_maker.py - AI logic for making decisions based on game state

from config import SAFE_DISTANCE_FROM_ENEMIES
import random

class DecisionMaker:
    def decide_movement(self, player, enemies):
        """
        Decide what movement the player should take based on the player's position and enemies
        """
        if not player:
            return 'stop'  # Cannot find player

        # Use a simple strategy: move away from the quadrant with the most enemies
        player_x, player_y, player_w, player_h = player
        danger_zones = self._calculate_danger_zones(player, enemies)

        # Determine safe direction
        safe_dir = self._determine_safe_direction(danger_zones)
        return safe_dir

    def _calculate_danger_zones(self, player, enemies):
        """
        Calculate dangerous zones based on enemy positions
        """
        zones = {'up': 0, 'down': 0, 'left': 0, 'right': 0}
        player_x, player_y, _, _ = player

        for enemy_x, enemy_y, enemy_w, enemy_h in enemies:
            if enemy_x < player_x:
                zones['left'] += 1
            else:
                zones['right'] += 1

            if enemy_y < player_y:
                zones['up'] += 1
            else:
                zones['down'] += 1

        return zones

    def _determine_safe_direction(self, danger_zones):
        """
        Determine the safest direction based on calculated danger zones
        """
        # Sort zones to find the direction with the least danger
        safe_direction = min(danger_zones, key=danger_zones.get)
        return safe_direction

    def decide_upgrade(self):
        """
        Logic for deciding which upgrade to choose
        Currently selects randomly for simplicity
        """
        return random.choice(['option1', 'option2', 'option3'])  # Placeholder options
