# TrackStatus Visual Overlay

A lightweight Python desktop app that reacts to real-time Formula 1 track status by displaying fullscreen color overlays. These overlays are picked up by the Nanoleaf Desktop App’s screen mirroring feature to trigger ambient MAGRGB lighting reactions.

---

## 🧩 Purpose

This project is an alternative to API-driven smart home reactions. Instead of using Matter or Alexa routines, it leverages simple on-screen color to drive lighting scenes based on track flags.

---

## 🚦 Track Status → Visual Overlay

| Track Status | Code | Overlay Color | Description              |
| ------------ | ---- | ------------- | ------------------------ |
| All Clear    | 1    | Green         | Rainbow/calm lighting    |
| Yellow Flag  | 2    | Yellow        | Caution - flashing scene |
| Red Flag     | 4    | Red           | Panic - intense red      |

---

## 📁 Project Structure

```
f1-rgb-control/
├── main.py           # Polls Multiviewer for track status
├── overlay.py        # Displays color overlay windows
├── config.py         # Track status API settings
└── README.md
```

---

## 🛠️ Setup

### Requirements

* Python 3.8+
* Nanoleaf Desktop App with screen mirroring enabled

### Install dependencies

This app uses only Python standard libraries (`tkinter`, `threading`, `requests`). Just clone and run.

### Run it

```bash
python main.py
```

Make sure the Nanoleaf Desktop App is actively mirroring the monitor where the overlays will appear.

---

## 🔧 Configuration

Edit `config.py` to point to your Multiviewer local server:

```python
F1MV_HOST = "localhost"
F1MV_PORT = 10101
```

---

## 🧪 Future Enhancements

* Add fading/pulsing effects
* CLI triggers or hotkeys for testing
* Stream Deck integration
* Victory animation (multi-color blast)

---

## 🧑‍💻 Authors

* Kelly Morris — project lead and developer
* Sam — co-architect and future collaborator

This app is part of the larger \[F1 Command Center Project].

---

## 💡 Inspiration

Built to maximize race weekend immersion without relying on cloud APIs or proprietary smart home ecosystems. Everything happens locally, in real time.
