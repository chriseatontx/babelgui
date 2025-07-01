# test_keyboard_fixed.py - Fixed keyboard test with automatic countdown

import pyautogui
import time

def countdown_and_focus(seconds=5):
    """Countdown to allow user to focus the game window"""
    print(f"\n🎯 FOCUS THE GAME WINDOW NOW!")
    print("=" * 40)
    print("1. Click on your game window to make it active")
    print("2. Make sure your character is visible in-game")
    print("3. The keyboard test will start automatically after countdown")
    print("=" * 40)
    
    for i in range(seconds, 0, -1):
        print(f"⏰ Starting in {i} seconds... (Focus the game window!)")
        time.sleep(1)
    
    print("🚀 KEYBOARD TEST STARTING NOW!")
    print("=" * 40)

def test_keyboard_input():
    """Test if we can send keyboard input to the active window"""
    print("🎮 KEYBOARD INPUT TEST")
    print("=" * 40)
    print("This test will send keyboard inputs to whatever window is currently active.")
    print("✅ No user input required - automatic startup!")
    print()
    
    # Automatic countdown - no user input required!
    countdown_and_focus(5)
    
    # Test each movement key
    movement_keys = [
        ('W (Up)', 'w'),
        ('A (Left)', 'a'), 
        ('S (Down)', 's'),
        ('D (Right)', 'd')
    ]
    
    for direction, key in movement_keys:
        print(f"\n📤 Pressing {direction} key: '{key}'")
        print("   (Your character should move now)")
        
        # Press and hold the key
        pyautogui.keyDown(key)
        print(f"   ✅ Key '{key}' pressed down")
        
        # Hold for 2 seconds
        for second in range(2):
            print(f"   ⏱️  Holding for {second + 1}/2 seconds...")
            time.sleep(1)
        
        # Release the key
        pyautogui.keyUp(key)
        print(f"   ⬆️  Key '{key}' released")
        
        # Short pause between keys
        time.sleep(0.5)
    
    print("\n" + "=" * 40)
    print("✅ KEYBOARD TEST COMPLETED!")
    print()
    print("Results:")
    print("• If your character moved: Keyboard input is working! ✅")
    print("• If nothing happened: There's an input issue ❌")
    print()
    print("If the character didn't move, try:")
    print("1. Run this script as administrator")
    print("2. Make sure the game window was focused during countdown")
    print("3. Check if the game uses different movement keys")
    print("4. Try windowed mode instead of fullscreen")
    print("5. Some games have anti-automation protection")

def quick_single_key_test():
    """Quick test with just one key"""
    print("\n🔍 QUICK SINGLE KEY TEST")
    print("=" * 40)
    
    countdown_and_focus(3)
    
    print("Sending single 'W' key press for 2 seconds...")
    pyautogui.keyDown('w')
    time.sleep(2)
    pyautogui.keyUp('w')
    
    print("✅ Single key test completed!")
    print("Did your character move up? This tells us if input is working.")

if __name__ == "__main__":
    print("🎮 TOWER OF BABEL: KEYBOARD INPUT TEST")
    print("=" * 50)
    print("This will test if the bot can send keyboard input to your game.")
    print("✅ No user interaction required during test!")
    print("=" * 50)
    
    try:
        # Run the full test
        test_keyboard_input()
        
        # Also run a quick single key test
        quick_single_key_test()
        
    except KeyboardInterrupt:
        print("\n\n🛑 Test cancelled by user")
    except Exception as e:
        print(f"\n\n❌ Test failed with error: {e}")
    
    print("\n" + "=" * 50)
    print("🎯 NEXT STEPS:")
    print("If keyboard input worked: Run 'python main_fixed.py'")
    print("If keyboard input failed: Try running as administrator")
    print("=" * 50)
