# test_keyboard.py - Simple test to verify keyboard input is working

import pyautogui
import time
import keyboard

def test_keyboard_input():
    """Test if we can send keyboard input to the active window"""
    print("🎮 KEYBOARD INPUT TEST")
    print("=" * 40)
    print()
    print("This test will send keyboard inputs to whatever window is currently active.")
    print("Make sure your game window is focused and active!")
    print()
    print("The test will:")
    print("1. Wait 3 seconds for you to focus the game window")
    print("2. Send W, A, S, D keys for 2 seconds each")
    print("3. Show what keys are being pressed")
    print()
    
    # Countdown
    for i in range(3, 0, -1):
        print(f"Starting in {i}...")
        time.sleep(1)
    
    print("🚀 TEST STARTING NOW!")
    print("=" * 40)
    
    # Test each movement key
    movement_keys = [
        ('W (Up)', 'w'),
        ('A (Left)', 'a'), 
        ('S (Down)', 's'),
        ('D (Right)', 'd')
    ]
    
    for direction, key in movement_keys:
        print(f"\\n📤 Pressing {direction} key: '{key}'")
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
    
    print("\\n" + "=" * 40)
    print("✅ KEYBOARD TEST COMPLETED!")
    print()
    print("Did your character move during the test?")
    print("If YES: The bot should work fine")
    print("If NO: The game window might not be receiving input")
    print()
    print("Troubleshooting if character didn't move:")
    print("1. Make sure the game window was focused/active")
    print("2. Check if the game uses different movement keys")
    print("3. Try running this script as administrator")
    print("4. Some games block automated input")

def test_with_user_confirmation():
    """Test with user feedback"""
    print("\\n🔍 INTERACTIVE TEST")
    print("=" * 40)
    
    input("Focus your game window and press Enter when ready...")
    
    print("\\nSending single key press...")
    print("Watch your character - pressing 'w' for 1 second")
    
    pyautogui.keyDown('w')
    time.sleep(1)
    pyautogui.keyUp('w')
    
    response = input("\\nDid your character move? (y/n): ").lower().strip()
    
    if response == 'y':
        print("✅ Great! Keyboard input is working.")
        print("The bot should be able to control your character.")
    else:
        print("❌ Keyboard input is not reaching the game.")
        print("This explains why the bot isn't moving your character.")
        print("\\nPossible solutions:")
        print("1. Run the script as administrator")
        print("2. Make sure the game window is focused")
        print("3. Check if the game has input blocking")
        print("4. Try windowed mode instead of fullscreen")

if __name__ == "__main__":
    try:
        test_keyboard_input()
        test_with_user_confirmation()
    except KeyboardInterrupt:
        print("\\n\\n🛑 Test cancelled by user")
    except Exception as e:
        print(f"\\n\\n❌ Test failed with error: {e}")
