# debug_main.py - Debug version of main.py with verbose output

import pyautogui
import keyboard
import time
import threading
import sys

from screen_analyzer import ScreenAnalyzer
from player_controller import PlayerController
from decision_maker import DecisionMaker
from utils import log_action
from config import GAME_REGION

class GameBotDebug:
    def __init__(self):
        self.running = True
        self.screen_analyzer = ScreenAnalyzer()
        self.player_controller = PlayerController()
        self.decision_maker = DecisionMaker()
        self.loop_count = 0
        
        # Set up kill switch
        keyboard.add_hotkey('q', self.stop_bot)
        
    def stop_bot(self):
        """Stop the bot gracefully"""
        log_action("STOP", "Kill switch activated")
        self.running = False
        self.player_controller.emergency_stop()
        
    def debug_screen_capture(self):
        """Test screen capture and save a debug image"""
        try:
            game_screen = self.screen_analyzer.capture_game_screen()
            if game_screen is not None:
                # Save debug screenshot
                import cv2
                cv2.imwrite('debug_capture.png', game_screen)
                print(f"✅ Screen capture successful! Shape: {game_screen.shape}")
                print(f"📸 Debug screenshot saved as 'debug_capture.png'")
                return game_screen
            else:
                print("❌ Screen capture returned None")
                return None
        except Exception as e:
            print(f"❌ Screen capture failed: {e}")
            return None
    
    def debug_analysis(self, game_screen):
        """Debug the screen analysis"""
        try:
            player, enemies = self.screen_analyzer.analyze_screen(game_screen)
            print(f"🎮 Player detected: {player}")
            print(f"👾 Enemies detected: {len(enemies) if enemies else 0} enemies")
            if enemies:
                print(f"   Enemy positions: {enemies[:3]}...")  # Show first 3
            return player, enemies
        except Exception as e:
            print(f"❌ Screen analysis failed: {e}")
            return None, []
    
    def debug_decision_making(self, player, enemies):
        """Debug the decision making process"""
        try:
            move_direction = self.decision_maker.decide_movement(player, enemies)
            print(f"🧠 Decision: Move {move_direction}")
            return move_direction
        except Exception as e:
            print(f"❌ Decision making failed: {e}")
            return 'stop'
    
    def debug_collect_experience_shards(self, game_screen):
        """Debug the collection of experience shards"""
        # Detect green experience shards
        try:
            experience_positions = self.screen_analyzer.detect_experience_shards(game_screen)
            if experience_positions:
                first_experience = experience_positions[0]
                print(f"💎 Experience shard detected at: {first_experience}")
                # Pick up the first shard
                player_x, player_y, _, _ = self.screen_analyzer._detect_player(game_screen)
                shard_x, shard_y, _, _ = first_experience
                if shard_x > player_x:
                    print("👟 Moving right to collect shard")
                    self.player_controller.move_player('right')
                elif shard_x < player_x:
                    print("👟 Moving left to collect shard")
                    self.player_controller.move_player('left')
                elif shard_y > player_y:
                    print("👟 Moving down to collect shard")
                    self.player_controller.move_player('down')
                elif shard_y < player_y:
                    print("👟 Moving up to collect shard")
                    self.player_controller.move_player('up')
            else:
                print("🚫 No experience shards detected")
        except Exception as e:
            print(f"❌ Experience shard detection failed: {e}")

    def debug_movement(self, direction):
        """Debug the movement commands"""
        try:
            print(f"🎯 Executing movement: {direction}")
            self.player_controller.move_player(direction)
            keys_pressed = list(self.player_controller.current_keys_pressed)
            print(f"⌨️  Currently pressed keys: {keys_pressed}")
        except Exception as e:
            print(f"❌ Movement failed: {e}")
        
    def run(self):
        """Main game loop with debug output"""
        log_action("START", "Debug bot starting...")
        print("🤖 Debug Bot is running. Press 'q' to stop.")
        print(f"📍 Game region: {GAME_REGION}")
        print("=" * 60)
        
        # Initial screen capture test
        print("🔍 Testing initial screen capture...")
        initial_screen = self.debug_screen_capture()
        if initial_screen is None:
            print("❌ Cannot capture screen. Check GAME_REGION settings.")
            return
        
        print("✅ Screen capture working. Starting main loop...")
        print("=" * 60)
        
        try:
            while self.running:
                self.loop_count += 1
                print(f"\n🔄 Loop #{self.loop_count} - {time.strftime('%H:%M:%S')}")
                
                try:
                    # Step 1: Capture screen
                    print("1️⃣ Capturing screen...")
                    game_screen = self.screen_analyzer.capture_game_screen()
                    
                    if game_screen is None:
                        print("❌ Failed to capture screen")
                        time.sleep(1)
                        continue
                    
                    # Step 2: Analyze screen (every 10 loops to reduce spam)
                    if self.loop_count % 10 == 1:
                        print("2️⃣ Analyzing screen...")
                        player, enemies = self.debug_analysis(game_screen)
                        # Also check for experience shards
                        experience_shards = self.screen_analyzer.detect_experience_shards(game_screen)
                        print(f"💎 Experience shards detected: {len(experience_shards)}")
                        if experience_shards:
                            print(f"   Shard positions: {experience_shards[:3]}...")  # Show first 3
                    else:
                        player, enemies = self.screen_analyzer.analyze_screen(game_screen)
                        experience_shards = self.screen_analyzer.detect_experience_shards(game_screen)
                    
                    # Step 3: Make decision
                    if self.loop_count % 10 == 1:
                        print("3️⃣ Making movement decision...")
                        move_direction = self.debug_decision_making(player, enemies)
                    else:
                        move_direction = self.decision_maker.decide_movement(player, enemies)
                    
                    # Step 4: Execute movement
                    if self.loop_count % 10 == 1:
                        print("4️⃣ Executing movement...")
                        self.debug_movement(move_direction)
                    else:
                        self.player_controller.move_player(move_direction)
                    
                    # Brief status update every 10 loops
                    if self.loop_count % 10 == 0:
                        print(f"📊 Status: Loop {self.loop_count}, Player: {'Found' if player else 'Not found'}, Enemies: {len(enemies) if enemies else 0}")
                    
                    # Small delay
                    time.sleep(0.1)
                    
                except Exception as e:
                    log_action("ERROR", f"Error in main loop: {str(e)}")
                    print(f"❌ Loop error: {e}")
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
        print("🛑 Debug bot stopped successfully.")
        print(f"📈 Total loops executed: {self.loop_count}")

if __name__ == "__main__":
    print("🐛 TOWER OF BABEL DEBUG BOT")
    print("=" * 50)
    print("This debug version shows detailed information about what the bot is doing.")
    print("Make sure:")
    print("1. The game is running and you're actively playing (not on title screen)")
    print("2. The game window is visible and active")
    print("3. You've run the calibration tool (python calibrate.py)")
    print("=" * 50)
    input("Press Enter to start debug session...")
    
    bot = GameBotDebug()
    bot.run()
