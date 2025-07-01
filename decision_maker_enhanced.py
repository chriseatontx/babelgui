# decision_maker_enhanced.py - Enhanced AI logic with smart pathfinding and safety

from config import SAFE_DISTANCE_FROM_ENEMIES, COLLECTION_DISTANCE
import random
import math

class DecisionMakerEnhanced:
    def __init__(self):
        self.last_direction = None
        self.stuck_counter = 0
        self.last_position = None
        
    def decide_movement(self, player, enemies, experience_shards=None):
        """
        Enhanced decision making with safety checks and smart pathfinding
        """
        if not player:
            return 'stop'  # Cannot find player
        
        player_x, player_y, player_w, player_h = player
        player_center = (player_x + player_w // 2, player_y + player_h // 2)
        
        # Check if we're stuck (same position)
        if self.last_position:
            distance_moved = self._calculate_distance(player_center, self.last_position)
            if distance_moved < 10:  # Haven't moved much
                self.stuck_counter += 1
            else:
                self.stuck_counter = 0
        
        self.last_position = player_center
        
        # If stuck, try random movement
        if self.stuck_counter > 20:
            self.stuck_counter = 0
            return random.choice(['up', 'down', 'left', 'right'])
        
        # Priority 1: Check for immediate danger
        immediate_danger = self._check_immediate_danger(player_center, enemies)
        if immediate_danger:
            escape_direction = self._find_escape_direction(player_center, enemies)
            print(f"🚨 DANGER! Escaping {escape_direction}")
            return escape_direction
        
        # Priority 2: Collect safe experience shards
        if experience_shards:
            safe_shard = self._find_safe_experience_shard(player_center, experience_shards, enemies)
            if safe_shard:
                direction = self._calculate_direction_to_target(player_center, safe_shard)
                print(f"💎 Moving {direction} to collect safe experience shard")
                return direction
        
        # Priority 3: General survival movement
        survival_direction = self._calculate_survival_movement(player_center, enemies)
        return survival_direction
    
    def _check_immediate_danger(self, player_pos, enemies):
        """Check if player is in immediate danger"""
        if not enemies:
            return False
        
        danger_distance = SAFE_DISTANCE_FROM_ENEMIES // 2  # Half safe distance for immediate danger
        
        for enemy in enemies:
            enemy_x, enemy_y, enemy_w, enemy_h = enemy
            enemy_center = (enemy_x + enemy_w // 2, enemy_y + enemy_h // 2)
            distance = self._calculate_distance(player_pos, enemy_center)
            
            if distance < danger_distance:
                return True
        
        return False
    
    def _find_escape_direction(self, player_pos, enemies):
        """Find the best direction to escape from enemies"""
        directions = {
            'up': (0, -50),
            'down': (0, 50),
            'left': (-50, 0),
            'right': (50, 0)
        }
        
        best_direction = 'up'
        max_distance_to_enemies = 0
        
        for direction, (dx, dy) in directions.items():
            # Calculate potential new position
            new_pos = (player_pos[0] + dx, player_pos[1] + dy)
            
            # Calculate minimum distance to any enemy from this new position
            min_enemy_distance = float('inf')
            for enemy in enemies:
                enemy_x, enemy_y, enemy_w, enemy_h = enemy
                enemy_center = (enemy_x + enemy_w // 2, enemy_y + enemy_h // 2)
                distance = self._calculate_distance(new_pos, enemy_center)
                min_enemy_distance = min(min_enemy_distance, distance)
            
            # Choose direction that maximizes distance from nearest enemy
            if min_enemy_distance > max_distance_to_enemies:
                max_distance_to_enemies = min_enemy_distance
                best_direction = direction
        
        return best_direction
    
    def _find_safe_experience_shard(self, player_pos, experience_shards, enemies):
        """Find the closest experience shard that's safe to collect"""
        safe_shards = []
        
        for shard in experience_shards:
            shard_x, shard_y, shard_w, shard_h = shard
            shard_center = (shard_x + shard_w // 2, shard_y + shard_h // 2)
            
            # Check if shard is within collection distance
            shard_distance = self._calculate_distance(player_pos, shard_center)
            if shard_distance > COLLECTION_DISTANCE * 2:  # Too far
                continue
            
            # Check if path to shard is safe
            if self._is_path_safe(player_pos, shard_center, enemies):
                safe_shards.append((shard, shard_distance))
        
        if not safe_shards:
            return None
        
        # Return closest safe shard
        closest_shard = min(safe_shards, key=lambda x: x[1])
        shard_x, shard_y, shard_w, shard_h = closest_shard[0]
        return (shard_x + shard_w // 2, shard_y + shard_h // 2)
    
    def _is_path_safe(self, start_pos, target_pos, enemies):
        """Check if the path from start to target is safe from enemies"""
        if not enemies:
            return True
        
        # Check several points along the path
        steps = 5
        for i in range(steps + 1):
            t = i / steps
            check_x = start_pos[0] + t * (target_pos[0] - start_pos[0])
            check_y = start_pos[1] + t * (target_pos[1] - start_pos[1])
            check_pos = (check_x, check_y)
            
            # Check if this point is too close to any enemy
            for enemy in enemies:
                enemy_x, enemy_y, enemy_w, enemy_h = enemy
                enemy_center = (enemy_x + enemy_w // 2, enemy_y + enemy_h // 2)
                distance = self._calculate_distance(check_pos, enemy_center)
                
                if distance < SAFE_DISTANCE_FROM_ENEMIES:
                    return False
        
        return True
    
    def _calculate_direction_to_target(self, player_pos, target_pos):
        """Calculate the best direction to move toward a target"""
        dx = target_pos[0] - player_pos[0]
        dy = target_pos[1] - player_pos[1]
        
        # Determine primary direction based on larger distance
        if abs(dx) > abs(dy):
            return 'right' if dx > 0 else 'left'
        else:
            return 'down' if dy > 0 else 'up'
    
    def _calculate_survival_movement(self, player_pos, enemies):
        """Calculate movement for general survival when no specific target"""
        if not enemies:
            # No enemies visible - move in a gentle circle
            return 'circle'
        
        # Calculate danger zones
        danger_zones = {'up': 0, 'down': 0, 'left': 0, 'right': 0}
        
        for enemy in enemies:
            enemy_x, enemy_y, enemy_w, enemy_h = enemy
            enemy_center = (enemy_x + enemy_w // 2, enemy_y + enemy_h // 2)
            distance = self._calculate_distance(player_pos, enemy_center)
            
            # Weight danger by distance (closer enemies are more dangerous)
            danger_weight = max(0, SAFE_DISTANCE_FROM_ENEMIES - distance)
            
            # Determine which zones this enemy affects
            if enemy_center[0] < player_pos[0]:
                danger_zones['left'] += danger_weight
            else:
                danger_zones['right'] += danger_weight
                
            if enemy_center[1] < player_pos[1]:
                danger_zones['up'] += danger_weight
            else:
                danger_zones['down'] += danger_weight
        
        # Find the safest direction
        safest_direction = min(danger_zones, key=danger_zones.get)
        
        # Add some randomness to avoid predictable patterns
        if danger_zones[safest_direction] == 0:
            # All directions equally safe, add some variation
            safe_directions = [d for d, danger in danger_zones.items() if danger == 0]
            if len(safe_directions) > 1:
                return random.choice(safe_directions)
        
        return safest_direction
    
    def _calculate_distance(self, pos1, pos2):
        """Calculate Euclidean distance between two points"""
        return math.sqrt((pos2[0] - pos1[0])**2 + (pos2[1] - pos1[1])**2)
    
    def get_debug_info(self, player, enemies, experience_shards=None):
        """Get debug information about current decision making"""
        if not player:
            return "No player detected"
        
        player_x, player_y, player_w, player_h = player
        player_center = (player_x + player_w // 2, player_y + player_h // 2)
        
        info = []
        info.append(f"Player at: {player_center}")
        info.append(f"Enemies nearby: {len(enemies) if enemies else 0}")
        info.append(f"Experience shards: {len(experience_shards) if experience_shards else 0}")
        
        if enemies:
            closest_enemy_dist = min([
                self._calculate_distance(player_center, (e[0] + e[2]//2, e[1] + e[3]//2))
                for e in enemies
            ])
            info.append(f"Closest enemy: {closest_enemy_dist:.1f} pixels")
        
        if experience_shards:
            safe_shards = len([s for s in experience_shards if self._is_path_safe(
                player_center, (s[0] + s[2]//2, s[1] + s[3]//2), enemies
            )])
            info.append(f"Safe shards: {safe_shards}")
        
        return " | ".join(info)
