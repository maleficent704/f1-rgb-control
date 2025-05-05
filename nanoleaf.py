# nanoleaf.py

import requests
from config import LIGHT_DEVICES
import time

def set_color_all(hue, sat=100, brightness=100):
    for device in LIGHT_DEVICES:
        url = f"http://{device['ip']}:16021/api/v1/{device['token']}/state"
        try:
            requests.put(url, json={
                "on": {"value": True},
                "hue": {"value": hue},
                "sat": {"value": sat},
                "brightness": {"value": brightness}
            })
        except Exception as e:
            print(f"Error setting light: {e}")

def cycle_rainbow():
    for hue in range(0, 360, 45):
        set_color_all(hue)
        time.sleep(0.2)

def flash_color(hue, cycles=3, delay=0.3):
    for _ in range(cycles):
        set_color_all(hue, 100, 100)
        time.sleep(delay)
        set_color_all(hue, 0, 0)
        time.sleep(delay)