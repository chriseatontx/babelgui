# combat_tracker.py - Tracks combat effectiveness to evaluate upgrade choices

import time

class CombatTracker:
    def __init__(self):
        self.session_start = time.time()
        self.last_level_up = time.time()
        self.enemies_killed = 0
        self.experience_collected = 0
        self.damage_taken = 0
        self.time_survived = 0
        self.level_count = 0
        
    def on_level_up(self):
        """Called when player levels up"""
        current_time = time.time()
        time_since_last_level = current_time - self.last_level_up
        
        self.level_count += 1
        self.time_survived = current_time - self.session_start
        
        # Calculate effectiveness metrics
        effectiveness = self._calculate_effectiveness(time_since_last_level)
        
        print(f"📊 Level {self.level_count} reached!")
        print(f"⏱️ Time since last level: {time_since_last_level:.1f}s")
        print(f"🎯 Combat effectiveness: {effectiveness:.2f}")
        
        # Reset for next level
        self.last_level_up = current_time
        self.enemies_killed = 0
        self.experience_collected = 0
        
        return effectiveness
    
    def _calculate_effectiveness(self, time_period):
        """Calculate combat effectiveness based on multiple factors"""
        if time_period <= 0:
            return 0
        
        # Base score on survival time (longer = better)
        survival_score = min(time_period / 60.0, 5.0)  # Cap at 5 minutes
        
        # Add bonus for experience collection rate
        xp_rate = self.experience_collected / time_period
        xp_score = min(xp_rate / 10.0, 2.0)  # Cap bonus at 2.0
        
        # Add bonus for enemy elimination (if trackable)
        enemy_score = min(self.enemies_killed / 10.0, 1.0)  # Cap bonus at 1.0
        
        # Penalty for taking too much damage (if trackable)
        damage_penalty = min(self.damage_taken / 100.0, 1.0)
        
        total_effectiveness = survival_score + xp_score + enemy_score - damage_penalty
        return max(total_effectiveness, 0.1)  # Minimum score of 0.1
    
    def update_experience_collected(self, xp_gained):
        """Update experience collection counter"""
        self.experience_collected += xp_gained
    
    def update_enemies_killed(self, count=1):
        """Update enemy kill counter"""
        self.enemies_killed += count
    
    def update_damage_taken(self, damage):
        """Update damage taken counter"""
        self.damage_taken += damage
    
    def get_session_stats(self):
        """Get overall session statistics"""
        total_time = time.time() - self.session_start
        return {
            'total_time': total_time,
            'levels_gained': self.level_count,
            'avg_time_per_level': total_time / max(self.level_count, 1),
            'total_experience': self.experience_collected,
            'total_enemies_killed': self.enemies_killed
        }
