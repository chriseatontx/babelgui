# Tower of Babel: Survivors of Chaos Bot

An automated Python application that plays Tower of Babel: Survivors of Chaos using computer vision and automated controls.

## Features

- **Automated Survival**: Keeps the character moving to avoid enemies
- **Enemy Detection**: Uses OpenCV for identifying enemies on screen
- **Upgrade Selection**: Automatically selects upgrades during level-up
- **Loot Collection**: Identifies and collects experience gems and items
- **Kill Switch**: Emergency stop using keyboard hotkey

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

1. Start Tower of Babel: Survivors of Chaos
2. Position the game window appropriately
3. Run the bot:
```bash
python main.py
```

4. Press 'q' to stop the bot at any time

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
