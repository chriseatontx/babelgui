# main_working.py - Working bot using keyboard library for input

import pyautogui
import keyboard
import time
import threading
import sys

from screen_analyzer import ScreenAnalyzer
from player_controller_keyboard import PlayerControllerKeyboard
from decision_maker import DecisionMaker
from utils import log_action

class GameBotWorking:
    def __init__(self):
        self.running = True
        self.screen_analyzer = ScreenAnalyzer()
        self.player_controller = PlayerControllerKeyboard()  # Using keyboard library version
        self.decision_maker = DecisionMaker()
        self.loop_count = 0
        
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
        """Main game loop with basic status output"""
        log_action("START", "Working bot starting...")
        print("🤖 Tower of Babel Bot (Working Version)")
        print("=" * 50)
        print("✅ Using keyboard library for input!")
        print("=" * 50)
        
        # Automatic countdown - no user input required!
        self.countdown_and_focus(5)
        
        try:
            while self.running:
                self.loop_count += 1
                
                try:
                    # Capture the game screen
                    game_screen = self.screen_analyzer.capture_game_screen()
                    
                    if game_screen is None:
                        log_action("ERROR", "Failed to capture screen")
                        time.sleep(1)
                        continue
                    
                    # Analyze the current game state
                    player, enemies = self.screen_analyzer.analyze_screen(game_screen)
                    
                    # Check for experience shards
                    experience_shards = self.screen_analyzer.detect_experience_shards(game_screen)
                    
                    # Make decisions (prioritize experience collection)
                    if experience_shards and player:
                        # Move towards closest experience shard
                        player_x, player_y, _, _ = player
                        closest_shard = min(experience_shards, 
                                          key=lambda shard: abs(shard[0] - player_x) + abs(shard[1] - player_y))
                        shard_x, shard_y, _, _ = closest_shard
                        
                        # Simple movement towards shard
                        if abs(shard_x - player_x) > abs(shard_y - player_y):
                            move_direction = 'right' if shard_x > player_x else 'left'
                        else:
                            move_direction = 'down' if shard_y > player_y else 'up'
                        
                        if self.loop_count % 50 == 1:  # Status every 50 loops
                            log_action("XP_COLLECTION", f"Moving {move_direction} towards experience shard")
                    else:
                        # Normal enemy avoidance
                        move_direction = self.decision_maker.decide_movement(player, enemies)
                        
                        if self.loop_count % 50 == 1:  # Status every 50 loops
                            status = f"Player: {'Found' if player else 'Lost'}, Enemies: {len(enemies) if enemies else 0}, XP: {len(experience_shards) if experience_shards else 0}"
                            log_action("STATUS", status)
                    
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
        print("🛑 Bot stopped successfully.")
        print(f"📈 Total loops executed: {self.loop_count}")

if __name__ == "__main__":
    print("🎮 TOWER OF BABEL: SURVIVORS BOT (WORKING VERSION)")
    print("=" * 60)
    print("✅ Uses keyboard library - should work with your game!")
    print("🎯 Features:")
    print("  • Automatic movement and enemy avoidance")
    print("  • Experience shard collection")
    print("  • Emergency stop with 'q' key")
    print("=" * 60)
    print("📋 Instructions:")
    print("1. Make sure the game is running and you're actively playing")
    print("2. Position this window where you can see it")
    print("3. The bot will start automatically after a 5-second countdown")
    print("4. When countdown starts, click on your game window to focus it")
    print("5. Press 'q' anytime to stop the bot")
    print("=" * 60)
    
    # No input() call - starts automatically!
    bot = GameBotWorking()
    bot.run()
