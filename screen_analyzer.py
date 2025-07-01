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
