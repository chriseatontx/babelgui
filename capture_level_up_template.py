# capture_level_up_template.py - Tool to capture level-up template for detection

import pyautogui
import cv2
import numpy as np
import time
from config import GAME_REGION

def capture_level_up_template():
    """Capture a template of the level-up text for template matching"""
    print("🎯 LEVEL-UP TEMPLATE CAPTURE TOOL")
    print("=" * 50)
    print("Instructions:")
    print("1. Get to a level-up screen in your game")
    print("2. Make sure the 'LEVEL UP' text is clearly visible")
    print("3. Position the game window so it's captured properly")
    print("4. This tool will capture the top-middle area where 'LEVEL UP' appears")
    print("=" * 50)
    
    input("Press Enter when you have the level-up screen visible...")
    
    print("📸 Capturing screen in 3 seconds...")
    for i in range(3, 0, -1):
        print(f"   {i}...")
        time.sleep(1)
    
    # Capture the full game screen
    full_screenshot = pyautogui.screenshot(region=(
        GAME_REGION['left'], 
        GAME_REGION['top'], 
        GAME_REGION['width'], 
        GAME_REGION['height']
    ))
    full_screenshot = cv2.cvtColor(np.array(full_screenshot), cv2.COLOR_RGB2BGR)
    
    # Define the top-middle area where "LEVEL UP" typically appears
    # Adjust these values based on your game's UI layout
    template_height = 100  # Height of the template area
    template_width = 300   # Width of the template area
    
    # Calculate position (top-middle of game area)
    start_x = (GAME_REGION['width'] - template_width) // 2
    start_y = 50  # 50 pixels from top
    
    end_x = start_x + template_width
    end_y = start_y + template_height
    
    # Extract the template area
    template = full_screenshot[start_y:end_y, start_x:end_x]
    
    # Save the template
    cv2.imwrite('level_up_template.png', template)
    
    # Also save the full screenshot for reference
    cv2.imwrite('full_level_up_screen.png', full_screenshot)
    
    print("✅ Template captured!")
    print(f"📁 Saved as 'level_up_template.png' ({template_width}x{template_height})")
    print(f"📁 Full screen saved as 'full_level_up_screen.png' for reference")
    print(f"📐 Template region: ({start_x}, {start_y}) to ({end_x}, {end_y})")
    
    # Display template info
    print(f"🔍 Template dimensions: {template.shape[1]}x{template.shape[0]}")
    print("\n💡 The template will now be used for accurate level-up detection!")
    
    return template

def test_template_matching():
    """Test the captured template against current screen"""
    try:
        # Load the template
        template = cv2.imread('level_up_template.png', cv2.IMREAD_COLOR)
        if template is None:
            print("❌ No template found. Run capture first!")
            return
        
        print("\n🧪 TESTING TEMPLATE MATCHING")
        print("=" * 30)
        
        input("Position game screen (level-up or normal) and press Enter to test...")
        
        # Capture current screen
        current_screenshot = pyautogui.screenshot(region=(
            GAME_REGION['left'], 
            GAME_REGION['top'], 
            GAME_REGION['width'], 
            GAME_REGION['height']
        ))
        current_screenshot = cv2.cvtColor(np.array(current_screenshot), cv2.COLOR_RGB2BGR)
        
        # Perform template matching
        result = cv2.matchTemplate(current_screenshot, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        
        print(f"🎯 Template match confidence: {max_val:.3f}")
        
        # Threshold for detection (adjust as needed)
        threshold = 0.7
        
        if max_val >= threshold:
            print(f"✅ LEVEL-UP DETECTED! (confidence: {max_val:.3f})")
            print(f"📍 Match location: {max_loc}")
        else:
            print(f"❌ No level-up detected (confidence: {max_val:.3f} < {threshold})")
        
        # Save result for inspection
        h, w = template.shape[:2]
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        
        # Draw rectangle around best match
        result_image = current_screenshot.copy()
        cv2.rectangle(result_image, top_left, bottom_right, (0, 255, 0), 2)
        cv2.imwrite('template_match_result.png', result_image)
        
        print("📁 Match result saved as 'template_match_result.png'")
        
    except Exception as e:
        print(f"❌ Error testing template: {e}")

def main():
    print("🎮 LEVEL-UP TEMPLATE TOOLS")
    print("=" * 50)
    print("Choose an option:")
    print("1. Capture new level-up template")
    print("2. Test existing template")
    print("3. Both (capture then test)")
    
    choice = input("\nEnter choice (1/2/3): ").strip()
    
    if choice == "1":
        capture_level_up_template()
    elif choice == "2":
        test_template_matching()
    elif choice == "3":
        capture_level_up_template()
        test_template_matching()
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
