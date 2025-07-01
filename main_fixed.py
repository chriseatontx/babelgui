# main_fixed.py - Fixed version with proper game window focusing

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
        
    def countdown_and_focus(self, seconds=5):
        """Countdown to allow user to focus the game window"""
        print(f"\n🎯 FOCUS THE GAME WINDOW NOW!")
        print("=" * 40)
        print("1. Click on your game window to make it active")
        print("2. Make sure your character is visible in-game")
        print("3. The bot will start automatically after countdown")
        print("=" * 40)
        
        for i in range(seconds, 0, -1):
            print(f"⏰ Starting in {i} seconds... (Focus the game window!)")
            time.sleep(1)
        
        print("🚀 BOT STARTING NOW!")
        print("Press 'q' at any time to stop the bot")
        print("=" * 40)
        
    def run(self):
        """Main game loop"""
        log_action("START", "Game bot starting...")
        print("🤖 Tower of Babel Bot")
        print("=" * 40)
        
        # Automatic countdown - no user input required!
        self.countdown_and_focus(5)
        
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
    print("🎮 TOWER OF BABEL: SURVIVORS BOT")
    print("=" * 50)
    print("✅ No user input required - automatic startup!")
    print("📋 Instructions:")
    print("1. Make sure the game is running and you're actively playing")
    print("2. Position this window where you can see it")
    print("3. The bot will start automatically after a 5-second countdown")
    print("4. When countdown starts, click on your game window to focus it")
    print("5. Press 'q' anytime to stop the bot")
    print("=" * 50)
    
    # No input() call - starts automatically!
    bot = GameBot()
    bot.run()
