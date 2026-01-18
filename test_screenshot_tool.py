#!/usr/bin/env python3
"""
Test script for screenshot tool
"""

import os
import sys

# Add the current directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from screenshot_tool import take_screenshot
    print("✓ Successfully imported screenshot_tool")
except ImportError as e:
    print(f"✗ Failed to import screenshot_tool: {e}")
    sys.exit(1)

def test_screenshot_tool():
    """Test the screenshot tool functionality"""
    print("\n=== Testing Screenshot Tool ===\n")
    
    # Test 1: Check if dependencies are installed
    print("Test 1: Checking dependencies...")
    try:
        import pyautogui
        import PIL
        print("✓ All dependencies are installed")
    except ImportError as e:
        print(f"✗ Missing dependency: {e}")
        print("Please run: pip install -r requirements.txt")
        return False
    
    # Test 2: Test auto-generated filename
    print("\nTest 2: Testing auto-generated filename...")
    try:
        result = take_screenshot()
        if result and os.path.exists(result):
            print(f"✓ Screenshot created: {result}")
            # Clean up
            os.remove(result)
            print("✓ Test file cleaned up")
        else:
            print("✗ Failed to create screenshot")
            return False
    except Exception as e:
        print(f"✗ Error during test: {e}")
        return False
    
    # Test 3: Test custom filename
    print("\nTest 3: Testing custom filename...")
    test_filename = "test_screenshot.png"
    try:
        result = take_screenshot(test_filename)
        if result and os.path.exists(test_filename):
            print(f"✓ Screenshot created with custom name: {test_filename}")
            # Clean up
            os.remove(test_filename)
            print("✓ Test file cleaned up")
        else:
            print("✗ Failed to create screenshot with custom name")
            return False
    except Exception as e:
        print(f"✗ Error during test: {e}")
        return False
    
    print("\n=== All tests passed! ===")
    return True

if __name__ == "__main__":
    success = test_screenshot_tool()
    sys.exit(0 if success else 1)
