# Troubleshooting Guide - Input Issues

## 🚨 Problem: Bot Not Moving Character

If the bot isn't moving your character, this guide will help you diagnose and fix the issue.

## 🔍 Step 1: Run Diagnostic Tests

### Test Alternative Input Methods
```bash
python test_alternative_input.py
```
This tests 6 different ways to send keyboard input to find one that works.

### Quick Keyboard Test
```bash
python test_keyboard_fixed.py
```
Simple test to verify basic keyboard input.

## 🎯 Step 2: Game Settings

### Display Mode
- **Try Windowed Mode**: Some games block input in fullscreen
- **Try Borderless Windowed**: Alternative to fullscreen that often works better
- **Avoid Exclusive Fullscreen**: This mode often blocks automated input

### Input Settings
- Look for "Input Method" or "Raw Input" settings
- Disable "Raw Input" if available
- Check for "Accessibility" or "Alternative Input" options
- Some games have "Allow External Input" settings

## 🛠️ Step 3: System Configuration

### Administrator Rights
1. Right-click PowerShell/Command Prompt
2. Select "Run as administrator"
3. Navigate to your project folder
4. Run the bot scripts

### Windows Settings
- **Game Mode**: Try disabling Windows Game Mode
- **Game Bar**: Disable Xbox Game Bar if enabled
- **Antivirus**: Temporarily disable real-time protection (re-enable after testing)

## 🎮 Step 4: Game-Specific Solutions

### Tower of Babel: Survivors of Chaos Specific
1. **Check Controls**: Verify game uses WASD for movement
2. **Pause Menu**: Make sure game isn't paused
3. **UI Overlays**: Close any in-game menus or dialogs
4. **Character State**: Ensure character is alive and can move

### Common Game Issues
- **Anti-Cheat Software**: Some games block all automated input
- **DirectInput Games**: May require different input methods
- **Unity/Unreal Engine**: Often have specific input handling

## 🔧 Step 5: Alternative Solutions

### If Standard Methods Don't Work:
1. **Virtual Input**: Try virtual keyboard software
2. **Hardware Emulation**: Use tools that emulate physical devices
3. **Game Mods**: Look for accessibility mods
4. **Different Games**: Test with other games to verify bot works

### Manual Testing:
1. Open Notepad
2. Run `python test_keyboard_fixed.py`
3. Focus Notepad during countdown
4. Check if 'w' character appears - this tests if input works at all

## 📊 Common Solutions by Error Type

### "No input methods worked"
- Game has anti-automation protection
- Try windowed mode
- Check for game-specific input settings

### "Some methods work but not in game"
- Game uses custom input handling
- Try different display modes
- Look for input accessibility options

### "Input works in other apps but not game"
- Game has input filtering
- Try running as administrator
- Check for game-specific solutions

## 🆘 Last Resort Options

### If Nothing Works:
1. **Check Game Forums**: Look for automation/accessibility discussions
2. **Game Documentation**: Check if game supports external input
3. **Alternative Games**: Test bot with similar games
4. **Contact Support**: Ask game developers about accessibility options

### Hardware Solutions:
- **Arduino/Raspberry Pi**: Physical device emulation
- **USB Input Devices**: Programmable keyboards/mice
- **Accessibility Hardware**: Specialized input devices

## 📝 Reporting Issues

If you continue having problems, please provide:
1. Results from `test_alternative_input.py`
2. Game version and settings
3. Windows version
4. Whether you're running as administrator
5. Any error messages

## ✅ Success Indicators

The bot is working correctly if:
- ✅ Character moves during keyboard tests
- ✅ Debug output shows player detection
- ✅ Debug output shows movement commands being sent
- ✅ No error messages in console

## 🎯 Next Steps

Once input is working:
1. Run `python main_fixed.py` for the full bot
2. Use `python calibrate.py` to adjust screen region if needed
3. Modify `config.py` for game-specific color detection
4. Use `python debug_main.py` for detailed debugging
