# main.py

import pyautogui
import keyboard
import time
import threading
import sys

from screen_analyzer import ScreenAnalyzer
from player_controller import PlayerController
from decision_maker import DecisionMaker
from utils import log_action

class GameBot:
    def __init__(self):
        self.running = True
        self.screen_analyzer = ScreenAnalyzer()
        self.player_controller = PlayerController()
        self.decision_maker = DecisionMaker()
        
        # Set up kill switch
        keyboard.add_hotkey('q', self.stop_bot)
        
    def stop_bot(self):
        """Stop the bot gracefully"""
        log_action("STOP", "Kill switch activated")
        self.running = False
        self.player_controller.emergency_stop()
        
    def run(self):
        """Main game loop"""
        log_action("START", "Game bot starting...")
        print("Bot is running. Press 'q' to stop.")
        
        try:
            while self.running:
                try:
                    # Capture the game screen
                    game_screen = self.screen_analyzer.capture_game_screen()
                    
                    if game_screen is None:
                        log_action("ERROR", "Failed to capture screen")
                        time.sleep(1)
                        continue
                    
                    # Analyze the current game state
                    player, enemies = self.screen_analyzer.analyze_screen(game_screen)
                    
                    # Make decisions
                    move_direction = self.decision_maker.decide_movement(player, enemies)
                    
                    # Control the player character
                    self.player_controller.move_player(move_direction)
                    
                    # Small delay to prevent excessive CPU usage
                    time.sleep(0.1)
                    
                except Exception as e:
                    log_action("ERROR", f"Error in main loop: {str(e)}")
                    time.sleep(0.5)
                    
        except KeyboardInterrupt:
            log_action("INTERRUPT", "Keyboard interrupt received")
        finally:
            self.cleanup()
            
    def cleanup(self):
        """Clean up resources before exit"""
        log_action("CLEANUP", "Cleaning up...")
        self.player_controller.emergency_stop()
        keyboard.unhook_all()
        print("Bot stopped successfully.")

if __name__ == "__main__":
    bot = GameBot()
    bot.run()
