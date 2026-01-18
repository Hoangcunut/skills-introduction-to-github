#!/usr/bin/env python3
"""
Screenshot Tool - A simple tool to capture screenshots
Công cụ chụp màn hình đơn giản
"""

import sys
import os
from datetime import datetime

try:
    import pyautogui
except ImportError:
    print("Error: Required dependencies are not installed.")
    print("Please install them using: pip install -r requirements.txt")
    sys.exit(1)


def take_screenshot(filename=None, region=None):
    """
    Take a screenshot and save it to a file.
    
    Args:
        filename (str): Output filename. If None, auto-generates a filename with timestamp
        region (tuple): Optional region to capture (x, y, width, height)
    
    Returns:
        str: Path to the saved screenshot
    """
    # Generate filename if not provided
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshot_{timestamp}.png"
    
    # Ensure the filename has .png extension
    if not filename.endswith('.png'):
        filename += '.png'
    
    try:
        # Take screenshot
        if region:
            screenshot = pyautogui.screenshot(region=region)
        else:
            screenshot = pyautogui.screenshot()
        
        # Save screenshot
        screenshot.save(filename)
        print(f"Screenshot saved successfully: {filename}")
        return os.path.abspath(filename)
    
    except Exception as e:
        print(f"Error taking screenshot: {e}")
        return None


def main():
    """Main function to handle command-line usage"""
    print("=== Screenshot Tool / Công cụ chụp màn hình ===")
    print()
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = None
    
    result = take_screenshot(filename)
    
    if result:
        print(f"Full path: {result}")
        print("\nUsage:")
        print("  python screenshot_tool.py                    # Auto-generate filename")
        print("  python screenshot_tool.py myscreen.png       # Custom filename")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
