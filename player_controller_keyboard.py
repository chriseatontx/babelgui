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
    
    def select_upgrade(self, upgrade_index, total_options=3):
        """Select an upgrade option using A/D keys and Enter"""
        try:
            # Ensure upgrade_index is within valid range (0-2 for 3 main options)
            if upgrade_index < 0 or upgrade_index > 2:
                print(f"⚠️ Invalid upgrade index {upgrade_index}. Using option 1 instead.")
                upgrade_index = 0
            
            print(f"🎯 Selecting upgrade option {upgrade_index + 1} of 3 main options")
            
            # CRITICAL: Release all movement keys first to avoid conflicts
            print("  🛑 Releasing all movement keys...")
            self._release_all_keys()
            time.sleep(0.5)  # Give time for keys to be released
            
            # ALWAYS move to leftmost position first (press A 4 times to be safe)
            print("  ⬅️ Moving to leftmost position...")
            for i in range(4):
                print(f"    Pressing A (attempt {i+1}/4)")
                kb.press_and_release('a')
                time.sleep(0.3)  # Longer delay between presses
            
            # Now we're guaranteed to be at option 1 (leftmost)
            print("  ⏸️ Waiting for UI to settle...")
            time.sleep(0.5)  # Longer pause to let UI settle
            
            # Navigate to desired option (0=stay, 1=press D once, 2=press D twice)
            if upgrade_index == 0:
                print("  🎯 Staying at option 1 (leftmost)")
                # Already at option 1, no movement needed
            elif upgrade_index == 1:
                print("  ➡️ Moving to option 2 (middle)")
                print("    Pressing D once")
                kb.press_and_release('d')
                time.sleep(0.3)
            elif upgrade_index == 2:
                print("  ➡️➡️ Moving to option 3 (rightmost)")
                print("    Pressing D first time")
                kb.press_and_release('d')
                time.sleep(0.3)
                print("    Pressing D second time")
                kb.press_and_release('d')
                time.sleep(0.3)
            
            # Select the option
            print("  ⏸️ Final pause before selection...")
            time.sleep(0.5)  # Longer pause before selection
            print(f"  ✅ Confirming selection with Enter...")
            kb.press_and_release('enter')
            print(f"✅ Selected upgrade option {upgrade_index + 1}")
            
            # Wait for selection to process
            time.sleep(2.0)  # Longer wait for selection to process
            
        except Exception as e:
            print(f"❌ Error selecting upgrade: {e}")
            import traceback
            traceback.print_exc()
            
            # Fallback: move left and select first option
            print("  🔄 Fallback: selecting first option")
            try:
                self._release_all_keys()
                time.sleep(0.5)
                for i in range(4):
                    print(f"    Fallback A press {i+1}/4")
                    kb.press_and_release('a')
                    time.sleep(0.3)
                time.sleep(0.5)
                print("    Fallback Enter press")
                kb.press_and_release('enter')
                time.sleep(2.0)
            except Exception as fallback_error:
                print(f"❌ Fallback also failed: {fallback_error}")
    
    def emergency_stop(self):
        """Emergency stop - release all keys immediately"""
        self._release_all_keys()
        print("Emergency stop activated - all movement keys released")
