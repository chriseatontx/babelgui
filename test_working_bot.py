# test_working_bot.py - Quick test for the keyboard library version

import time
from player_controller_keyboard import PlayerControllerKeyboard

def test_keyboard_controller():
    """Test the keyboard version of the player controller"""
    print("🎮 TESTING KEYBOARD CONTROLLER")
    print("=" * 40)
    print("This will test the keyboard library version of movement.")
    print("✅ This should work since keyboard library moved your character!")
    
    controller = PlayerControllerKeyboard()
    
    print("\n🎯 Focus game window in 3 seconds...")
    for i in range(3, 0, -1):
        print(f"   {i}...")
        time.sleep(1)
    
    print("\n📤 Testing movement with keyboard library...")
    
    movements = [
        ('up', 1),
        ('right', 1), 
        ('down', 1),
        ('left', 1)
    ]
    
    for direction, duration in movements:
        print(f"🎯 Moving {direction} for {duration} second(s)")
        controller.move_player(direction)
        time.sleep(duration)
        controller.move_player('stop')  # Stop movement
        time.sleep(0.5)  # Pause between movements
    
    print("\n✅ Movement test completed!")
    print("If your character moved, the working bot should function properly!")
    
    # Test circular movement
    print("\n🔄 Testing circular movement for 3 seconds...")
    start_time = time.time()
    while time.time() - start_time < 3:
        controller.move_player('circle')
        time.sleep(0.1)
    
    controller.move_player('stop')
    print("✅ Circular movement test completed!")
    
    print("\n🎯 NEXT STEP: Run 'python main_working.py' for the full bot!")

if __name__ == "__main__":
    test_keyboard_controller()
