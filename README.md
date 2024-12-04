# PRODIGY_CS_04
Absolutely! Here’s a README that reflects your direct involvement:

---

# Simple Keylogger

**Author:** Shema Prince  

I created this project as a basic keylogger to demonstrate how keystrokes can be recorded and logged using Python. The program captures keyboard input and saves it to a specified log file. 
**Important:** This tool is for educational purposes only and must be used ethically and with permission.

---

## Features

- **Keystroke Logging:** Records all keystrokes, including spaces and special keys.  
- **Log File:** Saves recorded keys to `key_log.txt`.  
- **Simple and Lightweight:** Uses the `pynput` library for efficient key capture.

---

## Requirements

- Python 3.x  
- `pynput` library  

### Installation  
Install the required library with:  
```bash
pip install pynput
```

---

## How to Use

1. **Run the Script:**  
   Save the code as `keylogger.py`, open a terminal, navigate to the script’s location, and run:  
   ```bash
   python keylogger.py
   ```

2. **Logging:**  
   The keylogger will capture all keystrokes and save them in `key_log.txt`.  
   Press `Ctrl+C` to stop the keylogger.

3. **Check the Log:**  
   Open `key_log.txt` to view the recorded keystrokes.

---

## Screenshots

### Running the Keylogger:  
*Insert screenshot here*  

### Viewing the Log File:  
*Insert screenshot here*  

---

## How It Works

- **Key Press Handling:**  
  The `on_press` function captures each key and writes it to the log file:
  - Regular characters are logged directly.  
  - Special keys like `Space` and `Enter` are handled separately.  
  - Non-character keys (like arrow or function keys) are recorded in square brackets.

- **Listener:**  
  The `pynput.keyboard.Listener` listens for key events and triggers `on_press` for each keystroke.

---

## Ethical Considerations

This project is intended for learning purposes only. Always obtain consent before using keyloggers, as they involve sensitive information and privacy laws may apply.

---

## Disclaimer

This keylogger is a tool for educational purposes. I am not responsible for any misuse of the code.

---
