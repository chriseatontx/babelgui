# screen_analyzer.py - Screen capture and analysis using OpenCV and numpy

import cv2
import numpy as np
import pyautogui
from config import GAME_REGION, PLAYER_COLOR_RANGE, ENEMY_COLOR_RANGES, XP_GEM_COLOR_RANGE, MIN_CONTOUR_AREA

class ScreenAnalyzer:

    def capture_game_screen(self):
        # Capture the screen region defined in the configuration
        screenshot = pyautogui.screenshot(region=(GAME_REGION['left'], GAME_REGION['top'], GAME_REGION['width'], GAME_REGION['height']))
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        return screenshot

    def analyze_screen(self, image):
        # Identify player and enemies on screen
        player = self._detect_player(image)
        enemies = self._detect_enemies(image)
        return player, enemies

    def _detect_player(self, image):
        # Convert image to HSV
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        player_mask = cv2.inRange(hsv, PLAYER_COLOR_RANGE['lower'], PLAYER_COLOR_RANGE['upper'])
        contours, _ = cv2.findContours(player_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) > MIN_CONTOUR_AREA:
                x, y, w, h = cv2.boundingRect(contour)
                return (x, y, w, h)
        return None

    def _detect_enemies(self, image):
        # Convert image to HSV
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        enemies = []

        for color_name, color_range in ENEMY_COLOR_RANGES.items():
            mask = cv2.inRange(hsv, color_range['lower'], color_range['upper'])
            contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            for contour in contours:
                if cv2.contourArea(contour) > MIN_CONTOUR_AREA:
                    x, y, w, h = cv2.boundingRect(contour)
                    enemies.append((x, y, w, h))
        return enemies
    
    def detect_experience_shards(self, image):
        """Detect green experience shards on screen"""
        # Convert image to HSV
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
        # Create mask for green experience shards
        xp_mask = cv2.inRange(hsv, XP_GEM_COLOR_RANGE['lower'], XP_GEM_COLOR_RANGE['upper'])
        contours, _ = cv2.findContours(xp_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        experience_shards = []
        for contour in contours:
            # Use smaller area threshold for experience shards
            if cv2.contourArea(contour) > MIN_CONTOUR_AREA // 4:
                x, y, w, h = cv2.boundingRect(contour)
                experience_shards.append((x, y, w, h))
        
        return experience_shards
    
    def detect_level_up_screen(self, image):
        """Detect if the level-up screen is currently showing using template matching"""
        try:
            # Load the level-up template
            import os
            template_path = 'level_up_template.png'
            
            if not os.path.exists(template_path):
                # Fallback to old method if no template exists
                print("⚠️ No level-up template found. Use 'python capture_level_up_template.py' to create one.")
                return self._detect_level_up_fallback(image)
            
            template = cv2.imread(template_path, cv2.IMREAD_COLOR)
            if template is None:
                print("❌ Failed to load level-up template.")
                return self._detect_level_up_fallback(image)
            
            # Perform template matching
            result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            
            # Threshold for detection (adjust as needed)
            threshold = 0.7
            level_up_detected = max_val >= threshold
            
            if level_up_detected:
                print(f"📈 LEVEL UP SCREEN DETECTED! (confidence: {max_val:.3f})")
            
            return level_up_detected
            
        except Exception as e:
            print(f"❌ Error in template matching: {e}")
            return self._detect_level_up_fallback(image)
    
    def _detect_level_up_fallback(self, image):
        """Fallback level-up detection method (less reliable)"""
        # Convert to grayscale for easier detection
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Look for dark areas typical of level up overlay (more than 40% dark pixels)
        dark_areas = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)[1]
        dark_pixel_count = cv2.countNonZero(dark_areas)
        total_pixels = gray.shape[0] * gray.shape[1]
        
        level_up_detected = (dark_pixel_count / total_pixels) > 0.4
        
        if level_up_detected:
            print("📈 LEVEL UP SCREEN DETECTED! (fallback method - may be inaccurate)")
        
        return level_up_detected
    
    def detect_upgrade_options(self, image):
        """Detect and extract upgrade option text from level-up screen"""
        try:
            import pytesseract
            
            # Convert to grayscale
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            # Enhance text contrast
            enhanced = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
            
            # Extract text from the image
            text = pytesseract.image_to_string(enhanced, config='--psm 6')
            
            # Parse upgrade options (simple approach)
            lines = [line.strip() for line in text.split('\n') if line.strip()]
            
            # Filter for likely upgrade names (basic heuristic)
            upgrade_options = []
            for line in lines:
                # Look for lines that might be upgrade names
                if len(line) > 3 and len(line) < 50:  # Reasonable length
                    if any(keyword in line.lower() for keyword in 
                           ['damage', 'speed', 'health', 'attack', 'defense', 'magic', 'pierce', 'fire', 'ice']):
                        upgrade_options.append(line)
            
            if not upgrade_options:
                # Fallback: use simple placeholder names based on position
                upgrade_options = ["Option 1", "Option 2", "Option 3"]
            
            print(f"🔍 Detected upgrades: {upgrade_options}")
            return upgrade_options
            
        except ImportError:
            print("⚠️ pytesseract not installed. Using position-based upgrade selection.")
            # Fallback to position-based selection
            return ["Option 1", "Option 2", "Option 3"]
        except Exception as e:
            print(f"❌ Error reading upgrade text: {e}")
            return ["Option 1", "Option 2", "Option 3"]
