# Tower of Babel: Survivors of Chaos Smart Bot

An intelligent Python application that plays Tower of Babel: Survivors of Chaos using advanced computer vision, smart pathfinding, and automated controls.

## 🎯 Smart Features

- **🧠 Intelligent Pathfinding**: Smart navigation to experience shards with safety checks
- **🛡️ Dynamic Enemy Avoidance**: Real-time threat assessment and escape routes
- **💎 Safe Experience Collection**: Only collects items when the path is safe
- **🚨 Immediate Danger Response**: Emergency escape when enemies get too close
- **🔄 Stuck Detection & Recovery**: Automatically recovers when movement is blocked
- **⚖️ Threat Prioritization**: Weighs risks vs rewards for optimal decision making
- **🎮 Adaptive Movement**: Changes strategies based on game state
- **🛑 Emergency Stop**: Press 'q' anytime to stop safely

## Requirements

- Python 3.8+
- pyautogui
- opencv-python
- numpy
- keyboard
- Pillow

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/babel-survivors-bot.git
cd babel-survivors-bot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Calibration
1. Start Tower of Babel: Survivors of Chaos
2. Position the game window where it is fully visible
3. Run the calibration tool to set up the screen region:
```bash
python calibrate.py
```
4. Follow the on-screen instructions to define the game area.

### Running the Bot
1. With the game running and visible, execute:
```bash
python main.py
```
2. Press 'q' to stop the bot safely at any time.

### Testing
To verify the bot is working correctly:
```bash
python test_bot.py
```
This will test screen capture, movement controls, and basic bot functionality.

## Configuration

Edit `config.py` to adjust:
- Screen capture region
- Movement patterns
- Detection thresholds
- Color ranges for enemies and items

## Structure

- `main.py` - Entry point and main game loop
- `screen_analyzer.py` - Screen capture and computer vision
- `player_controller.py` - Character movement and actions
- `decision_maker.py` - AI logic for survival decisions
- `config.py` - Configuration settings
- `utils.py` - Utility functions

## Disclaimer

This bot is for educational purposes. Use responsibly and in accordance with the game's terms of service.
