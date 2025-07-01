# Setup Guide for Tower of Babel Bot

## Prerequisites
1. **Game Must Be Running**: Start Tower of Babel: Survivors of Chaos before running the bot
2. **Game Window Position**: Position the game window where the bot can capture it
3. **Permissions**: Run the script as administrator (required for keyboard/mouse control)

## Step-by-Step Setup

### 1. Start the Game
- Launch Tower of Babel: Survivors of Chaos
- Start a new game or continue an existing one
- Make sure the character is visible on screen

### 2. Configure Screen Region
The bot needs to know where your game window is located. You have two options:

#### Option A: Use the calibration tool (recommended)
```bash
python calibrate.py
```

#### Option B: Manual configuration
1. Note your game window position and size
2. Edit `config.py` and update the `GAME_REGION` values:
   ```python
   GAME_REGION = {
       'left': 100,    # X position of game window
       'top': 100,     # Y position of game window  
       'width': 1280,  # Width of game area
       'height': 720   # Height of game area
   }
   ```

### 3. Run as Administrator
Right-click on PowerShell/Command Prompt and select "Run as administrator", then:
```bash
cd E:\babelgui
python main.py
```

### 4. Test the Bot
- The bot should start moving your character
- Press 'q' to stop the bot safely
- Check the console for any error messages

## Troubleshooting

### Nothing Happens in Game
- Ensure the game window is active and in focus
- Check that GAME_REGION coordinates are correct
- Verify the script is running as administrator
- Make sure the game uses WASD controls

### Bot Moves Erratically  
- The color detection might need adjustment
- Check if the player detection is working correctly
- Adjust color ranges in config.py

### Performance Issues
- Reduce the loop speed in main.py (increase sleep time)
- Lower the screen capture quality if needed
