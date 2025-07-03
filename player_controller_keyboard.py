# player_controller_keyboard.py - Controls player movement using keyboard library

import keyboard as kb
import time
import random
import math
from config import MOVEMENT_KEYS, MOVEMENT_SPEED, CIRCLE_RADIUS, GAME_REGION

class PlayerControllerKeyboard:
    def __init__(self):
        self.current_keys_pressed = set()
        self.movement_angle = 0  # For circular movement pattern
        self.movement_pattern = "circle"  # Default movement pattern
        
    def move_player(self, direction):
        """
        Move the player in the specified direction.
        Direction can be: 'up', 'down', 'left', 'right', 'stop', or 'circle'
        """
        # Release all currently pressed keys
        self._release_all_keys()
        
        if direction == 'stop':
            return
        elif direction == 'circle':
            self._move_in_circle()
        elif direction in MOVEMENT_KEYS:
            self._press_key(MOVEMENT_KEYS[direction])
        else:
            # Handle diagonal movement
            if isinstance(direction, tuple) and len(direction) == 2:
                dx, dy = direction
                self._move_diagonal(dx, dy)
    
    def _press_key(self, key):
        """Press and hold a key"""
        if key not in self.current_keys_pressed:
            kb.press(key)
            self.current_keys_pressed.add(key)
    
    def _release_key(self, key):
        """Release a key"""
        if key in self.current_keys_pressed:
            kb.release(key)
            self.current_keys_pressed.remove(key)
    
    def _release_all_keys(self):
        """Release all currently pressed movement keys"""
        for key in self.current_keys_pressed.copy():
            kb.release(key)
        self.current_keys_pressed.clear()
    
    def _move_in_circle(self):
        """Move the player in a circular pattern"""
        # Calculate movement based on current angle
        x_movement = math.cos(self.movement_angle)
        y_movement = math.sin(self.movement_angle)
        
        # Determine which keys to press based on movement direction
        if x_movement > 0.5:
            self._press_key(MOVEMENT_KEYS['right'])
        elif x_movement < -0.5:
            self._press_key(MOVEMENT_KEYS['left'])
            
        if y_movement > 0.5:
            self._press_key(MOVEMENT_KEYS['down'])
        elif y_movement < -0.5:
            self._press_key(MOVEMENT_KEYS['up'])
        
        # Increment angle for next movement
        self.movement_angle += 0.1
        if self.movement_angle >= 2 * math.pi:
            self.movement_angle = 0
    
    def _move_diagonal(self, dx, dy):
        """Move diagonally based on dx, dy values"""
        if dx > 0:
            self._press_key(MOVEMENT_KEYS['right'])
        elif dx < 0:
            self._press_key(MOVEMENT_KEYS['left'])
            
        if dy > 0:
            self._press_key(MOVEMENT_KEYS['down'])
        elif dy < 0:
            self._press_key(MOVEMENT_KEYS['up'])
    
    def click_upgrade(self, x=None, y=None):
        """Click on an upgrade option. If no coordinates provided, clicks center of screen"""
        import pyautogui  # Still use pyautogui for mouse clicks
        if x is None or y is None:
            # Default to center of game region for upgrade selection
            x = GAME_REGION['left'] + GAME_REGION['width'] // 2
            y = GAME_REGION['top'] + GAME_REGION['height'] // 2
        
        pyautogui.click(x, y)
        time.sleep(0.5)  # Wait for click to register
    
    def select_upgrade(self):
        """Select the leftmost upgrade option."""
        try:
            print("🎯 Selecting leftmost upgrade option")
            
            # Release all movement keys to avoid conflicts
            self._release_all_keys()
            time.sleep(0.5)
            
            # Move to the leftmost position by pressing 'a' multiple times
            for _ in range(3):
                kb.press_and_release('a')
                time.sleep(0.3)
            
            # Wait for UI to settle
            time.sleep(0.5)
            
            # Confirm selection with Enter
            kb.press_and_release('enter')
            print("✅ Selected leftmost upgrade option.")
            
            # Wait for the selection to process
            time.sleep(2.0)
            
        except Exception as e:
            print(f"❌ Error selecting upgrade: {e}")
    
    def emergency_stop(self):
        """Emergency stop - release all keys immediately"""
        self._release_all_keys()
        print("Emergency stop activated - all movement keys released")
