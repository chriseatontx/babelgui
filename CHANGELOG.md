# Changelog

All notable changes to the Tower of Babel: Survivors of Chaos Bot project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0] - 2025-07-01

### Added
- **2025-07-01 05:14:49** - Created initial changelog documentation
- **2025-07-01 05:12:20** - Added calibration tool (`calibrate.py`) for interactive screen region setup
- **2025-07-01 05:12:20** - Added test script (`test_bot.py`) for debugging bot functionality
- **2025-07-01 05:12:20** - Added setup guide (`SETUP_GUIDE.md`) with step-by-step instructions
- **2025-07-01 05:09:32** - Fixed kill switch and main loop issues in `main.py`
- **2025-07-01 05:09:32** - Restructured main script with proper class-based architecture
- **2025-07-01 05:09:32** - Added comprehensive error handling and cleanup mechanisms
- **2025-07-01 05:00:18** - Successfully installed all required Python packages
- **2025-07-01 04:52:38** - Created core project structure with modular design

### Initial Project Structure
- **`main.py`** - Entry point with GameBot class and main game loop
- **`screen_analyzer.py`** - Screen capture and computer vision analysis
- **`player_controller.py`** - Character movement and input control
- **`decision_maker.py`** - AI logic for survival decisions
- **`config.py`** - Configuration settings and detection parameters
- **`utils.py`** - Utility functions for distance calculation and logging
- **`requirements.txt`** - Python package dependencies
- **`README.md`** - Project documentation and usage instructions
- **`.gitignore`** - Git ignore patterns for Python projects

### Dependencies Added
- `pyautogui>=0.9.50` - Screen capture and keyboard/mouse automation
- `opencv-python>=4.8.0` - Computer vision and image processing
- `numpy>=1.24.0` - Numerical operations and array handling
- `keyboard>=0.13.5` - Global hotkey detection for kill switch
- `Pillow>=10.0.0` - Image processing support

### Features Implemented
- **Screen Analysis**: Real-time game screen capture and processing
- **Enemy Detection**: Color-based enemy identification using OpenCV
- **Player Detection**: Character location tracking on screen
- **Movement AI**: Intelligent movement patterns to avoid enemies
- **Kill Switch**: Emergency stop functionality (press 'q' to stop)
- **Circular Movement**: Default movement pattern for survival
- **Upgrade Selection**: Automated level-up upgrade selection
- **Configuration System**: Adjustable detection thresholds and color ranges

### Fixed
- **2025-07-01 05:09:32** - Fixed KeyError in emergency stop when releasing movement keys
- **2025-07-01 05:09:32** - Fixed kill switch triggering multiple times on startup
- **2025-07-01 05:09:32** - Fixed main loop stability and error handling
- **2025-07-01 05:00:18** - Resolved package installation issues with Python 3.13

### Technical Details
- **Architecture**: Modular design with separate concerns for analysis, control, and decision-making
- **Error Handling**: Comprehensive exception handling throughout the application
- **Resource Management**: Proper cleanup of keyboard hooks and movement keys
- **Logging**: Action logging with timestamps for debugging
- **Compatibility**: Windows-compatible with PowerShell support

### Configuration Defaults
- Game region: 1280x720 at position (100, 100)
- Movement keys: WASD standard configuration
- Loop speed: 0.1 seconds between iterations
- Detection thresholds: Configurable color ranges for different game elements

### Development Tools
- **Calibration Tool**: Interactive screen region setup assistant
- **Test Script**: Comprehensive functionality testing
- **Setup Guide**: Step-by-step installation and configuration instructions

### Known Issues
- Requires administrator privileges for keyboard/mouse control
- Game window must be active and visible for proper operation
- Color detection may need adjustment for different game themes/graphics settings

---

## Version History

### Version 1.0.0 (2025-07-01)
- Initial release with core bot functionality
- Complete automation system for Tower of Babel: Survivors of Chaos
- Screen analysis, enemy detection, and survival AI
- Interactive setup and calibration tools
