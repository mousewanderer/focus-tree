import pyautogui
import time

# Wait for user to position cursor and read instructions
print("Hover over the input box. Starting in 5 seconds...")
time.sleep(5)

# Get current mouse position (assume it's over the input box)
input_box_pos = pyautogui.position()
print(f"Locked input box at: {input_box_pos}")

# Loop through all 6-digit numbers
for i in range(1000000):  # 000000 to 999999
    number = f"{i:06d}"

    # Reclick the input box to ensure focus
    pyautogui.click(input_box_pos)

    # Type the number and hit Enter
    pyautogui.write(number)
    pyautogui.press('enter')
    time.sleep(0.05)

    # Backspace 6 digits and Enter key
    for _ in range(7):
        pyautogui.press('backspace')

    time.sleep(0.05)
