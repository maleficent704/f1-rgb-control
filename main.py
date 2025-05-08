# main.py

import requests
import time
from config import F1MV_HOST, F1MV_PORT
from overlay import show_color

API_URL = f"http://{F1MV_HOST}:{F1MV_PORT}/api/graphql"

HEADERS = {
    "Content-Type": "application/json",
}

QUERY = {
    "query": """
    {
        f1LiveTimingState {
            TrackStatus
        }
    }
    """
}

def get_track_status():
    try:
        response = requests.post(API_URL, json=QUERY, headers=HEADERS)
        if response.status_code == 200:
            data = response.json()
            return data["data"]["f1LiveTimingState"]["TrackStatus"]
        else:
            print(f"Error {response.status_code}: {response.text[:100]}")
    except Exception as e:
        print("Request failed:", e)
    return None

def main():
    print("Starting HTTP polling for TrackStatus...")
    last_status = None

    while True:
        track_status = get_track_status()
        print("📦 Raw track_status:", track_status)
        if track_status:
            status = track_status.get("Status")
            message = track_status.get("Message", "Unknown")

            if status != last_status:
                print(f"⚠️ Track Status changed: {message} (Code: {status})")
                last_status = status

                # Trigger color overlay
                show_color(status)
            else:
                print(f"Track Status unchanged: {message} (Code: {status})")

        time.sleep(2)

if __name__ == "__main__":
    main()
