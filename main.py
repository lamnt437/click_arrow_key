import pyautogui
import time

def press_backward_arrow():
    """
    Simulates pressing the backward arrow key on the keyboard.
    """
    pyautogui.press('left')  # Left arrow key is typically the 'backward' key

def main():
    try:
        print("Backward Arrow Key Presser started. Press Ctrl+C to stop.")
        while True:
            press_backward_arrow()
            print("Pressed backward arrow key")
            time.sleep(2)  # Wait for 5 seconds between key presses
    except KeyboardInterrupt:
        print("\nProgram stopped by user.")

if __name__ == "__main__":
    main()