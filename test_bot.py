# test_bot.py - Simple test script to verify bot functionality

import pyautogui
import time
import keyboard
from config import GAME_REGION, MOVEMENT_KEYS

def test_screen_capture():
    """Test if we can capture the game screen"""
    print("Testing screen capture...")
    try:
        screenshot = pyautogui.screenshot(region=(
            GAME_REGION['left'], 
            GAME_REGION['top'], 
            GAME_REGION['width'], 
            GAME_REGION['height']
        ))
        print(f"✅ Successfully captured {GAME_REGION['width']}x{GAME_REGION['height']} region")
        
        # Save screenshot for inspection
        screenshot.save('test_capture.png')
        print("✅ Saved test screenshot as 'test_capture.png'")
        return True
    except Exception as e:
        print(f"❌ Failed to capture screen: {e}")
        return False

def test_movement_keys():
    """Test if we can send movement keys to the game"""
    print("\\nTesting movement keys...")
    print("Make sure the game window is active and focused!")
    print("The character should move for 2 seconds in each direction.")
    
    input("Press Enter to start movement test...")
    
    directions = [
        ('up', MOVEMENT_KEYS['up']),
        ('right', MOVEMENT_KEYS['right']),
        ('down', MOVEMENT_KEYS['down']),
        ('left', MOVEMENT_KEYS['left'])
    ]
    
    for direction, key in directions:
        print(f"Moving {direction} (key: {key})")
        pyautogui.keyDown(key)
        time.sleep(1)
        pyautogui.keyUp(key)
        time.sleep(0.5)
    
    print("✅ Movement test completed")

def test_basic_bot_loop():
    """Test a basic version of the bot loop"""
    print("\\nTesting basic bot functionality...")
    print("Bot will move in a simple pattern for 10 seconds")
    print("Press 'q' at any time to stop")
    
    input("Press Enter to start bot test...")
    
    # Set up kill switch
    stop_bot = False
    def stop():
        nonlocal stop_bot
        stop_bot = True
        print("\\nStopping bot...")
    
    keyboard.add_hotkey('q', stop)
    
    start_time = time.time()
    move_counter = 0
    
    try:
        while not stop_bot and (time.time() - start_time) < 10:
            # Simple movement pattern
            if move_counter % 4 == 0:
                key = MOVEMENT_KEYS['up']
            elif move_counter % 4 == 1:
                key = MOVEMENT_KEYS['right']
            elif move_counter % 4 == 2:
                key = MOVEMENT_KEYS['down']
            else:
                key = MOVEMENT_KEYS['left']
            
            print(f"Moving with key: {key}")
            pyautogui.keyDown(key)
            time.sleep(0.5)
            pyautogui.keyUp(key)
            time.sleep(0.1)
            
            move_counter += 1
            
    except Exception as e:
        print(f"Error in bot loop: {e}")
    finally:
        # Release all keys
        for key in MOVEMENT_KEYS.values():
            pyautogui.keyUp(key)
        keyboard.unhook_all()
        print("✅ Bot test completed")

def main():
    print("Tower of Babel Bot - Test Script")
    print("=" * 40)
    print("This script will test various bot functions.")
    print("Make sure the game is running before starting!")
    print()
    
    # Test 1: Screen capture
    if not test_screen_capture():
        print("\\n❌ Screen capture failed. Please check GAME_REGION in config.py")
        return
    
    # Test 2: Movement keys
    try:
        test_movement_keys()
    except Exception as e:
        print(f"❌ Movement test failed: {e}")
        return
    
    # Test 3: Basic bot loop
    try:
        test_basic_bot_loop()
    except Exception as e:
        print(f"❌ Bot loop test failed: {e}")
        return
    
    print("\\n" + "=" * 40)
    print("✅ All tests completed!")
    print("If the character moved during the tests, the bot should work.")
    print("If not, check:")
    print("1. Game window is active and focused")
    print("2. GAME_REGION settings in config.py")
    print("3. Script is running as administrator")

if __name__ == "__main__":
    main()
