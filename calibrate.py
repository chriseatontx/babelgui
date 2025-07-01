# calibrate.py - Tool to help calibrate the screen region for the game

import pyautogui
import cv2
import numpy as np
import time

def show_mouse_position():
    """Show current mouse position for 10 seconds"""
    print("Move your mouse to help identify game window bounds...")
    print("Mouse position will be shown for 10 seconds:")
    
    for i in range(100):
        x, y = pyautogui.position()
        print(f"\rMouse position: X={x}, Y={y}   ", end="", flush=True)
        time.sleep(0.1)
    print()

def capture_and_show_region(left, top, width, height):
    """Capture and display a screen region"""
    try:
        screenshot = pyautogui.screenshot(region=(left, top, width, height))
        screenshot_np = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        
        # Save the screenshot for user to view
        screenshot.save('calibration_preview.png')
        print(f"\nCaptured region: left={left}, top={top}, width={width}, height={height}")
        print("📸 Screenshot saved as 'calibration_preview.png'")
        print("\n📋 Please check the saved image file to verify it shows your game area.")
        print("   - Open 'calibration_preview.png' in your file explorer")
        print("   - Verify it captures the game area correctly")
        
        # Simple text-based confirmation instead of OpenCV window
        while True:
            response = input("\nDoes the preview image look correct? (y/n/q to quit): ").lower().strip()
            if response == 'y':
                return True
            elif response == 'n':
                return False
            elif response == 'q':
                print("Calibration cancelled.")
                return False
            else:
                print("Please enter 'y' for yes, 'n' for no, or 'q' to quit.")
        
    except Exception as e:
        print(f"Error capturing region: {e}")
        return False

def interactive_calibration():
    """Interactive tool to find the correct game region"""
    print("=== Game Region Calibration Tool ===")
    print()
    
    # Step 1: Show mouse position
    show_mouse_position()
    print()
    
    # Step 2: Get game window bounds
    print("Now we'll set up the game capture region.")
    print("1. First, click on the TOP-LEFT corner of your game window")
    input("Position your mouse and press Enter...")
    top_left = pyautogui.position()
    print(f"Top-left corner set to: {top_left}")
    
    print("2. Now click on the BOTTOM-RIGHT corner of your game window")
    input("Position your mouse and press Enter...")
    bottom_right = pyautogui.position()
    print(f"Bottom-right corner set to: {bottom_right}")
    
    # Calculate region
    left = top_left[0]
    top = top_left[1]
    width = bottom_right[0] - top_left[0]
    height = bottom_right[1] - top_left[1]
    
    print(f"\\nCalculated game region:")
    print(f"Left: {left}")
    print(f"Top: {top}")
    print(f"Width: {width}")
    print(f"Height: {height}")
    
    # Step 3: Preview the region
    print("\\n3. Let's preview this region...")
    if not capture_and_show_region(left, top, width, height):
        print("Calibration cancelled.")
        return None
    
    # Step 4: Confirm
    confirm = input("\\nDoes this look correct? (y/n): ").lower().strip()
    if confirm == 'y':
        return {
            'left': left,
            'top': top,
            'width': width,
            'height': height
        }
    else:
        print("Let's try again...")
        return interactive_calibration()

def update_config_file(region):
    """Update the config.py file with new region"""
    try:
        # Read current config
        with open('config.py', 'r') as f:
            content = f.read()
        
        # Replace the GAME_REGION section
        new_region = f"""GAME_REGION = {{
    'left': {region['left']},
    'top': {region['top']},
    'width': {region['width']},
    'height': {region['height']}
}}"""
        
        # Find and replace the existing GAME_REGION
        import re
        pattern = r"GAME_REGION\s*=\s*\{[^}]+\}"
        new_content = re.sub(pattern, new_region, content)
        
        # Write back to file
        with open('config.py', 'w') as f:
            f.write(new_content)
        
        print(f"✅ Successfully updated config.py with new game region!")
        return True
        
    except Exception as e:
        print(f"❌ Error updating config.py: {e}")
        print("Please manually update the GAME_REGION in config.py with these values:")
        print(f"'left': {region['left']},")
        print(f"'top': {region['top']},")
        print(f"'width': {region['width']},")
        print(f"'height': {region['height']}")
        return False

def main():
    print("Tower of Babel Bot - Screen Calibration Tool")
    print("=" * 50)
    print()
    print("This tool will help you set up the correct screen region for the bot.")
    print("Make sure the game is running and visible before starting!")
    print()
    
    input("Press Enter when ready...")
    
    region = interactive_calibration()
    
    if region:
        print("\\n" + "=" * 50)
        print("Calibration completed successfully!")
        print("Region settings:")
        for key, value in region.items():
            print(f"  {key}: {value}")
        
        update_config_file(region)
        print("\\nYou can now run the bot with: python main.py")
    else:
        print("\\nCalibration was cancelled or failed.")

if __name__ == "__main__":
    main()
