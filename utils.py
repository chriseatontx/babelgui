# utils.py - Utility functions for the Tower of Babel bot

import math
import time
import cv2
import numpy as np

def calculate_distance(point1, point2):
    """Calculate Euclidean distance between two points"""
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def get_center_point(bbox):
    """Get center point from bounding box (x, y, w, h)"""
    x, y, w, h = bbox
    return (x + w // 2, y + h // 2)

def is_point_in_circle(point, center, radius):
    """Check if a point is within a circular area"""
    return calculate_distance(point, center) <= radius

def detect_level_up_screen(image):
    """
    Detect if the level up screen is currently showing
    Returns True if level up screen is detected
    """
    # Convert to grayscale for easier detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Look for dark areas typical of level up overlay
    dark_areas = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)[1]
    
    # Count the number of dark pixels
    dark_pixel_count = cv2.countNonZero(dark_areas)
    total_pixels = gray.shape[0] * gray.shape[1]
    
    # If more than 40% of screen is dark, likely a level up screen
    return (dark_pixel_count / total_pixels) > 0.4

def wait_for_game_start(timeout=30):
    """
    Wait for the game to start (useful for initialization)
    Returns True if game appears to be ready, False if timeout
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        # Add game-specific detection logic here
        time.sleep(1)
        print("Waiting for game to start...")
    return True

def clamp_value(value, min_val, max_val):
    """Clamp a value between min and max"""
    return max(min_val, min(value, max_val))

def normalize_coordinates(x, y, screen_width, screen_height):
    """Normalize coordinates to 0-1 range"""
    return (x / screen_width, y / screen_height)

def log_action(action, details=""):
    """Simple logging function"""
    timestamp = time.strftime("%H:%M:%S")
    print(f"[{timestamp}] {action}: {details}")
