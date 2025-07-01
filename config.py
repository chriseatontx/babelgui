# config.py - Configuration settings for the Tower of Babel bot

import numpy as np

# Screen capture settings
GAME_REGION = {
    'left': 969,
    'top': 50,
    'width': 1574,
    'height': 877
}

# Player detection settings
PLAYER_COLOR_RANGE = {
    'lower': np.array([100, 150, 0]),    # Lower HSV bound for player color
    'upper': np.array([130, 255, 255])   # Upper HSV bound for player color
}

# Enemy detection settings
ENEMY_COLOR_RANGES = {
    'red_enemies': {
        'lower': np.array([0, 120, 70]),
        'upper': np.array([10, 255, 255])
    },
    'green_enemies': {
        'lower': np.array([40, 50, 50]),
        'upper': np.array([80, 255, 255])
    }
}

# Experience gem detection (typically yellow/gold)
XP_GEM_COLOR_RANGE = {
    'lower': np.array([20, 100, 100]),
    'upper': np.array([30, 255, 255])
}

# Movement settings
MOVEMENT_KEYS = {
    'up': 'w',
    'down': 's',
    'left': 'a',
    'right': 'd'
}

# Detection thresholds
MIN_CONTOUR_AREA = 100
PLAYER_DETECTION_THRESHOLD = 0.8
ENEMY_DETECTION_THRESHOLD = 0.7

# Movement patterns
CIRCLE_RADIUS = 200
MOVEMENT_SPEED = 0.1  # Time between movement commands

# Upgrade selection settings
LEVEL_UP_DETECTION_COLOR = {
    'lower': np.array([40, 40, 40]),  # Dark background of level up screen
    'upper': np.array([60, 60, 60])
}

# Safe distances
SAFE_DISTANCE_FROM_ENEMIES = 150
COLLECTION_DISTANCE = 100
