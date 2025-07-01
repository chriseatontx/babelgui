# main.py

import pyautogui
import keyboard
import time

from screen_analyzer import ScreenAnalyzer
from player_controller import PlayerController
from decision_maker import DecisionMaker

# Initialize components
screen_analyzer = ScreenAnalyzer()
player_controller = PlayerController()
decision_maker = DecisionMaker()

# Define a kill switch
def kill_switch():
    print("Kill switch activated. Exiting the game bot.")
    exit(0)

keyboard.add_hotkey('q', kill_switch)

# Main game loop
if __name__ == "__main__":
    print("Starting the game bot. Press 'q' to stop.")
    try:
        while True:
            # Capture the game screen
            game_screen = screen_analyzer.capture_game_screen()

            # Analyze the current game state
            player, enemies = screen_analyzer.analyze_screen(game_screen)

            # Make decisions
            move_direction = decision_maker.decide_movement(player, enemies)

            # Control the player character
            player_controller.move_player(move_direction)

            time.sleep(0.1)  # Control the loop speed

    except KeyboardInterrupt:
        kill_switch()
