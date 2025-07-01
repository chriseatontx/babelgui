# test_upgrade_keys.py - Test A/D/Enter keys for upgrade selection

import keyboard as kb
import time

def test_upgrade_navigation():
    """Test the A/D/Enter navigation for upgrade selection"""
    print("🧪 UPGRADE NAVIGATION TEST")
    print("=" * 40)
    print("This will test A, D, and Enter key presses for level-up navigation.")
    print()
    print("Instructions:")
    print("1. Get to a level-up screen in your game")
    print("2. Focus the game window")
    print("3. Watch the selection move as keys are pressed")
    print("=" * 40)
    
    input("Press Enter when you have the level-up screen visible and game focused...")
    
    print("\n🎯 Starting upgrade navigation test in 3 seconds...")
    for i in range(3, 0, -1):
        print(f"   {i}...")
        time.sleep(1)
    
    print("\n🔧 Testing A key (move left)...")
    for i in range(4):
        print(f"  A press {i+1}/4")
        kb.press_and_release('a')
        time.sleep(0.5)
    
    print("\n⏸️ Pausing for 2 seconds...")
    time.sleep(2)
    
    print("\n🔧 Testing D key (move right)...")
    for i in range(3):
        print(f"  D press {i+1}/3")
        kb.press_and_release('d')
        time.sleep(0.5)
    
    print("\n⏸️ Pausing for 2 seconds...")
    time.sleep(2)
    
    print("\n🔧 Moving back left...")
    for i in range(2):
        print(f"  A press {i+1}/2")
        kb.press_and_release('a')
        time.sleep(0.5)
    
    print("\n⏸️ Final pause before Enter...")
    time.sleep(1)
    
    print("\n🔧 Testing Enter key (should select current option)...")
    print("  WARNING: This will actually select an upgrade!")
    
    confirm = input("Press 'y' to test Enter key (will select upgrade): ").lower()
    if confirm == 'y':
        print("  Enter press!")
        kb.press_and_release('enter')
        print("✅ Enter key test completed!")
    else:
        print("⏭️ Skipped Enter key test")
    
    print("\n✅ Navigation test completed!")

def test_individual_keys():
    """Test individual key presses with manual confirmation"""
    print("\n🔍 INDIVIDUAL KEY TEST")
    print("=" * 30)
    print("This will test each key individually with your confirmation.")
    
    keys_to_test = ['a', 'd', 'enter']
    
    for key in keys_to_test:
        input(f"\nPress Enter to test '{key}' key...")
        print(f"🔧 Pressing '{key}' key...")
        
        if key == 'enter':
            print("⚠️ WARNING: This will select the current upgrade!")
            confirm = input("Type 'yes' to actually press Enter: ")
            if confirm.lower() == 'yes':
                kb.press_and_release(key)
                print(f"✅ Pressed '{key}' key")
            else:
                print("⏭️ Skipped Enter key")
        else:
            kb.press_and_release(key)
            print(f"✅ Pressed '{key}' key")
        
        time.sleep(0.5)

def main():
    print("🎮 UPGRADE KEY TESTING TOOL")
    print("=" * 50)
    print("Choose a test:")
    print("1. Full navigation test (A left, D right, Enter select)")
    print("2. Individual key test (step by step)")
    print("3. Both tests")
    
    choice = input("\nEnter choice (1/2/3): ").strip()
    
    if choice == "1":
        test_upgrade_navigation()
    elif choice == "2":
        test_individual_keys()
    elif choice == "3":
        test_upgrade_navigation()
        test_individual_keys()
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
