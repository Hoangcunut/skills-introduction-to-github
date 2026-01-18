#!/usr/bin/env python3
"""
Example script showing how to use the screenshot tool
Ví dụ sử dụng công cụ chụp màn hình
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def show_examples():
    """Display usage examples"""
    print("=== Screenshot Tool Usage Examples ===")
    print("=== Ví dụ sử dụng Công cụ chụp màn hình ===\n")
    
    print("1. Basic screenshot with auto-generated filename:")
    print("   python screenshot_tool.py")
    print("   Output: screenshot_20240118_143000.png\n")
    
    print("2. Screenshot with custom filename:")
    print("   python screenshot_tool.py myscreen.png")
    print("   Output: myscreen.png\n")
    
    print("3. Screenshot with custom name (no extension):")
    print("   python screenshot_tool.py myscreen")
    print("   Output: myscreen.png\n")
    
    print("4. Programmatic usage:")
    print("   from screenshot_tool import take_screenshot")
    print("   take_screenshot('output.png')")
    print("   # or")
    print("   take_screenshot()  # auto-generate filename\n")
    
    print("5. Taking a screenshot of a specific region:")
    print("   from screenshot_tool import take_screenshot")
    print("   # Capture region: x=100, y=100, width=500, height=400")
    print("   take_screenshot('region.png', region=(100, 100, 500, 400))\n")
    
    print("\nNote: Make sure to install dependencies first:")
    print("pip install -r requirements.txt\n")

if __name__ == "__main__":
    show_examples()
