# Android Auto Clicker (For Telegram Airdrops)

This Python script automates clicking on your Android device using ADB. It's designed to interact with apps that require repetitive tapping.

## Key Features

*   Connects to Android devices via ADB
*   Simulates random clicks within specified screen areas
*   Extracts text from screenshots using OCR (e.g., remaining energy, scores)
*   Monitors app status and energy levels
*   Customizable click frequency and sleep intervals
*   Config options to target specific phone sizes or resolutions

## Benefits

*   Ideal for games or apps requiring repetitive actions
*   Potential for automation of tasks
*   Customizable for different screen resolutions

# Preview:
To give you a quick overview of what this project does, here's a GIF preview showing the script in action. The GIF demonstrates the script interacting with the app, performing clicks, and pausing when necessary.

![Project Preview](vid.gif)

## Installation & Setup

### Prerequisites

*   Python 3.8+
*   ADB (Android Debug Bridge) installed and in your system's PATH
*   Libraries:
    *   Pillow (PIL): `pip install pillow`
    *   pytesseract: `pip install pytesseract`
*   (Optional) Tesseract OCR engine if not already installed

### Steps

1.  Clone this repository.
2.  Install the required libraries.
3.  (Optional) Set the path to your Tesseract executable in the `extract_text_from_image` function if needed.
4.  Update the `phone_sizes` dictionary with your device's resolution and click/data ranges.

## Usage

### Customization

*   Adjust the `_click_per_loop`, `_sleep_time`, and `_coin_threshhold` variables in the script to control the clicking behavior and energy monitoring.
*   Update the `phone_sizes` dictionary with your device's specifications (resolution, click ranges, data extraction ranges) if it's not already included.
*   Set `dynamic_sizes` to `True` for automatic scaling based on resolution, or `False` to use manual configuration.

### Example Command

```bash
python main.py
```
# Workflow
## Device Connection:
1. Ensure your Android device is connected to your computer via USB and that USB debugging is enabled.
2. Verify the connection using `adb devices` in your terminal.

## Script Configuration:
1. Open the script in a text editor.
2. Modify the following settings based on your requirements:
   - `_click_per_loop`: Number of clicks per loop.
   - `_sleep_time`: Time (in seconds) to sleep between click loops.
   - `_coin_threshhold`: Minimum energy required before the script pauses.
   - `phone_sizes`: Add or modify your device's specifications if it's not in the list.
   - `dynamic_sizes`: Set to `True` for automatic scaling to your device's resolution, or `False` to use manual coordinates.

## Run the Script:
1. Save your changes to the script.
2. Open your terminal and navigate to the directory where the script is saved.
3. Run the script using the command `python script_name.py`.

## Monitoring and Pausing:
1. The script will automatically detect if the specified app is running and if there is enough energy.
2. If either condition isn't met, the script will pause and display messages in the terminal.
   - If the app is closed, you need to reopen it manually.
   - If the energy is low, wait for it to replenish before resuming the script manually.

# Troubleshooting

## ADB not found:
- Make sure ADB is installed and added to your system's PATH environment variable.
- Test by typing `adb devices` in your terminal. If you see a list of devices, ADB is working correctly.

## OCR Errors:
- Ensure Tesseract OCR is installed on your system.
- Double-check that you've correctly set the path to the Tesseract executable (`tesseract_cmd`) in the `extract_text_from_image` function.
- If OCR results are inaccurate, you can try:
  - Adjusting the image preprocessing steps within the script (e.g., increase image contrast).
  - Experimenting with different Tesseract configurations.

## App Detection Issues:
- Verify that the `my_name` variable in the script matches your in-game name exactly (case-sensitive).
- If the app is not detected, the script will pause and you'll need to manually reopen it.





# Important
## Note:
    This project is created purely for educational and entertainment purposes.  It is not intended for malicious use or to gain unfair advantages in any applications. Please use this script responsibly.

## Disclaimer:
    This script is a fun experiment in Android automation.  I am not responsible for any consequences that may arise from its use. Please be aware that some apps or games might have terms of service that prohibit the use of automation tools.

### Note on Dynamic Sizing:
The dynamic sizing feature may not always work as expected due to variations in screen resolutions and layouts across different devices.

### Static Sizing Instructions:
For static sizing, follow these steps:

1. **Locate CEO Name, Remaining Energy, and Current Score on Screen**:
   - Find the coordinates (x, y) for the CEO name, remaining energy, and current score on your device's screen.
   - Use example images provided in the repository to assist you in identifying these elements.

2. **Update Script Configuration**:
   - Open the script in a text editor.
   - Locate the settings related to static sizing.
   - Update the script with the coordinates (x, y) for the CEO name, remaining energy, and current score.

### Example Images:
Example images illustrating the CEO name, remaining energy, and current score on the screen are available in the repository. Use these images as references when configuring static sizing.

By following these instructions and using the provided example images, you can effectively configure static sizing for the script to accurately identify and interact with the required elements on the screen.

### Example Static sized for a phone

```python
phone_sizes = {
    "poco-x3": {
        "click_range_x": (200, 800),
        "click_range_y": (1000, 1700),
        "energy_range": (110, 350, 1850, 1950), # (start_x, end_x, start_y, end_y)
        "name_range": (185, 460, 300, 360),  # (start_x, end_x, start_y, end_y)
        "resolution": (1080, 2400),  # phone resolution (Required for dynamic size)
        "scores-range": (430, 845, 700, 805), # (start_x, end_x, start_y, end_y)
    }
}
```