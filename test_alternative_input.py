# test_alternative_input.py - Test alternative input methods

import time
import sys

def test_pynput_input():
    """Test using pynput library for input"""
    try:
        from pynput.keyboard import Key, Controller
        print("📦 Testing pynput library...")
        
        keyboard = Controller()
        
        print("🎯 Focus game window in 3 seconds...")
        for i in range(3, 0, -1):
            print(f"   {i}...")
            time.sleep(1)
        
        print("📤 Sending 'w' key via pynput...")
        keyboard.press('w')
        time.sleep(2)
        keyboard.release('w')
        
        print("✅ pynput test completed!")
        return True
        
    except ImportError:
        print("❌ pynput not installed. Installing...")
        import subprocess
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pynput"])
            print("✅ pynput installed! Please run this script again.")
            return False
        except Exception as e:
            print(f"❌ Failed to install pynput: {e}")
            return False
    except Exception as e:
        print(f"❌ pynput test failed: {e}")
        return False

def test_keyboard_library():
    """Test using keyboard library for input"""
    try:
        import keyboard as kb
        print("📦 Testing keyboard library...")
        
        print("🎯 Focus game window in 3 seconds...")
        for i in range(3, 0, -1):
            print(f"   {i}...")
            time.sleep(1)
        
        print("📤 Sending 'w' key via keyboard library...")
        kb.press('w')
        time.sleep(2)
        kb.release('w')
        
        print("✅ keyboard library test completed!")
        return True
        
    except Exception as e:
        print(f"❌ keyboard library test failed: {e}")
        return False

def test_win32api_input():
    """Test using Windows API directly"""
    try:
        import win32api
        import win32con
        print("📦 Testing Windows API (win32api)...")
        
        print("🎯 Focus game window in 3 seconds...")
        for i in range(3, 0, -1):
            print(f"   {i}...")
            time.sleep(1)
        
        print("📤 Sending 'w' key via Windows API...")
        # Virtual key code for 'W' is 0x57
        win32api.keybd_event(0x57, 0, 0, 0)  # Key down
        time.sleep(2)
        win32api.keybd_event(0x57, 0, win32con.KEYEVENTF_KEYUP, 0)  # Key up
        
        print("✅ Windows API test completed!")
        return True
        
    except ImportError:
        print("❌ pywin32 not installed. Installing...")
        import subprocess
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pywin32"])
            print("✅ pywin32 installed! Please run this script again.")
            return False
        except Exception as e:
            print(f"❌ Failed to install pywin32: {e}")
            return False
    except Exception as e:
        print(f"❌ Windows API test failed: {e}")
        return False

def test_ctypes_input():
    """Test using ctypes for direct Windows API calls"""
    try:
        import ctypes
        from ctypes import wintypes
        print("📦 Testing ctypes (direct Windows API)...")
        
        user32 = ctypes.windll.user32
        
        print("🎯 Focus game window in 3 seconds...")
        for i in range(3, 0, -1):
            print(f"   {i}...")
            time.sleep(1)
        
        print("📤 Sending 'w' key via ctypes...")
        
        # Define key codes
        VK_W = 0x57
        KEYEVENTF_KEYUP = 0x0002
        
        # Press key down
        user32.keybd_event(VK_W, 0, 0, 0)
        time.sleep(2)
        # Release key
        user32.keybd_event(VK_W, 0, KEYEVENTF_KEYUP, 0)
        
        print("✅ ctypes test completed!")
        return True
        
    except Exception as e:
        print(f"❌ ctypes test failed: {e}")
        return False

def test_sendkeys():
    """Test using SendKeys if available"""
    try:
        import win32com.client
        print("📦 Testing SendKeys (COM)...")
        
        shell = win32com.client.Dispatch("WScript.Shell")
        
        print("🎯 Focus game window in 3 seconds...")
        for i in range(3, 0, -1):
            print(f"   {i}...")
            time.sleep(1)
        
        print("📤 Sending 'w' key via SendKeys...")
        shell.SendKeys("w")
        time.sleep(2)
        
        print("✅ SendKeys test completed!")
        return True
        
    except Exception as e:
        print(f"❌ SendKeys test failed: {e}")
        return False

def check_game_compatibility():
    """Check what might be blocking input"""
    print("\n🔍 GAME COMPATIBILITY CHECK")
    print("=" * 40)
    print("Possible reasons input is blocked:")
    print("1. ✅ Game has anti-cheat/anti-automation protection")
    print("2. ✅ Game uses DirectInput instead of standard Windows input")
    print("3. ✅ Game is running in exclusive fullscreen mode")
    print("4. ✅ Game requires specific input timing")
    print("5. ✅ Game uses custom input handling")
    print()
    print("💡 Possible solutions:")
    print("• Try windowed or borderless windowed mode")
    print("• Look for input accessibility options in game settings")
    print("• Check if game has built-in automation/macro support")
    print("• Some games require physical input (won't work with bots)")
    print("• Try different timing between key presses")

def main():
    print("🎮 ALTERNATIVE INPUT METHOD TESTER")
    print("=" * 50)
    print("Testing different ways to send keyboard input...")
    print("=" * 50)
    
    methods = [
        ("pyautogui (current)", lambda: print("❌ Already tested - failed")),
        ("pynput", test_pynput_input),
        ("keyboard library", test_keyboard_library),
        ("Windows API (win32api)", test_win32api_input),
        ("ctypes (direct API)", test_ctypes_input),
        ("SendKeys (COM)", test_sendkeys)
    ]
    
    working_methods = []
    
    for name, test_func in methods:
        print(f"\n{'='*20} {name} {'='*20}")
        try:
            if test_func():
                working_methods.append(name)
                print(f"✅ {name} method works!")
            else:
                print(f"❌ {name} method failed")
        except Exception as e:
            print(f"❌ {name} method crashed: {e}")
        
        time.sleep(1)  # Pause between tests
    
    print("\n" + "=" * 50)
    print("📊 RESULTS SUMMARY")
    print("=" * 50)
    
    if working_methods:
        print("✅ Working input methods:")
        for method in working_methods:
            print(f"   • {method}")
        print("\n💡 We can modify the bot to use a working method!")
    else:
        print("❌ No input methods worked")
        print("This suggests the game blocks automated input")
        check_game_compatibility()
    
    print("\n🎯 NEXT STEPS:")
    if working_methods:
        print("• Tell me which method worked and I'll update the bot")
        print("• Test if the character actually moved during any test")
    else:
        print("• Try running the game in windowed mode")
        print("• Check game settings for input/accessibility options")
        print("• The game might have anti-automation protection")

if __name__ == "__main__":
    main()
