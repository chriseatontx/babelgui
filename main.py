# main.py - Tower of Babel: Survivors of Chaos Smart Bot

import pyautogui
import keyboard
import time
import threading
import sys

from screen_analyzer import ScreenAnalyzer
from player_controller_keyboard import PlayerControllerKeyboard
from decision_maker_enhanced import DecisionMakerEnhanced
from utils import log_action
from upgrade_manager import UpgradeManager
from combat_tracker import CombatTracker

class GameBot:
    def __init__(self):
        self.running = True
        self.screen_analyzer = ScreenAnalyzer()
        self.player_controller = PlayerControllerKeyboard()  # Using keyboard library
        self.decision_maker = DecisionMakerEnhanced()  # Using enhanced AI
        self.loop_count = 0
        self.upgrade_manager = UpgradeManager()
        self.combat_tracker = CombatTracker()
        
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
        
        print("🚀 SMART BOT STARTING NOW!")
        print("Press 'q' at any time to stop the bot")
        print("=" * 40)
        
    def run(self):
        """Main game loop with smart decision making"""
        log_action("START", "Smart bot starting...")
        print("🧠 Tower of Babel Smart Bot")
        print("=" * 50)
        print("✅ Enhanced with smart pathfinding and safety!")
        print("🎯 Features:")
        print("  • Safe experience shard collection")
        print("  • Intelligent enemy avoidance") 
        print("  • Stuck detection and recovery")
        print("  • Dynamic threat assessment")
        print("=" * 50)
        
        # Automatic countdown
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
                    experience_shards = self.screen_analyzer.detect_experience_shards(game_screen)
                    
                    # Check for level-up screen
                    if self.screen_analyzer.detect_level_up_screen(game_screen):
                        upgrade_options = self.screen_analyzer.detect_upgrade_options(game_screen)
                        best_upgrade, upgrade_index = self.upgrade_manager.evaluate_best_upgrade(upgrade_options)
                        
                        print(f"🆙 Selecting upgrade: {best_upgrade} (option {upgrade_index + 1})")
                        
                        # Actually select the upgrade using keyboard controls
                        self.player_controller.select_upgrade(upgrade_index, len(upgrade_options))
                        
                        # Calculate effectiveness and update database
                        effectiveness = self.combat_tracker.on_level_up()
                        self.upgrade_manager.update_upgrade_choice(best_upgrade, effectiveness)
                        
                        # Show current upgrade statistics
                        print(self.upgrade_manager.get_upgrade_stats())
                        
                        # Wait a bit for level-up screen to disappear
                        time.sleep(2)
                        continue  # Skip the rest of the loop while level-up screen is handled
                    
                    # Make smart decisions
                    move_direction = self.decision_maker.decide_movement(player, enemies, experience_shards)
                    
                    # Control the player character
                    self.player_controller.move_player(move_direction)
                    
                    # Detailed logging every 30 loops
                    if self.loop_count % 30 == 1:
                        debug_info = self.decision_maker.get_debug_info(player, enemies, experience_shards)
                        log_action("DEBUG", debug_info)
                    
                    # Brief status every 100 loops
                    if self.loop_count % 100 == 0:
                        status = f"Loop {self.loop_count} | Direction: {move_direction}"
                        log_action("STATUS", status)
                    
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
        print("🛑 Smart bot stopped successfully.")
        print(f"📈 Total loops executed: {self.loop_count}")

if __name__ == "__main__":
    print("🧠 TOWER OF BABEL: SMART SURVIVORS BOT")
    print("=" * 60)
    print("🎯 INTELLIGENT FEATURES:")
    print("  ✅ Smart pathfinding to experience shards")
    print("  ✅ Safety checks before moving toward items")
    print("  ✅ Dynamic enemy avoidance")
    print("  ✅ Escape routes when in danger")
    print("  ✅ Stuck detection and recovery")
    print("  ✅ Threat assessment and prioritization")
    print("=" * 60)
    print("📋 Instructions:")
    print("1. Make sure the game is running and you're actively playing")
    print("2. Position this window where you can see it")
    print("3. The bot will start automatically after a 5-second countdown")
    print("4. When countdown starts, click on your game window to focus it")
    print("5. Press 'q' anytime to stop the bot")
    print("6. Watch the console for intelligent decision making!")
    print("=" * 60)
    
    bot = GameBot()
    bot.run()
