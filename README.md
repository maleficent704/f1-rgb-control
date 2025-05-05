# F1 RGB Control

🎨 Sync Nanoleaf RGB lighting with live Formula 1 race events using the F1 Multiviewer API.

## 🚀 Features

- Detect live race events: yellow/red/green flags
- Flash Nanoleaf lights based on event triggers
- Cycle colors for race highlights (e.g. green flag rainbow)
- Multi-device Nanoleaf support
- Modular, expandable Python project

## 🔧 Requirements

- Python 3.7+
- Nanoleaf light panels or strips
- F1 Multiviewer running locally
- Websocket access to F1MV GraphQL endpoint

## 📦 Installation

```bash
pip install requests websockets aiohttp
```

## 📁 File Structure

- `main.py`: Listens for F1MV events and triggers effects
- `nanoleaf.py`: Light control helpers
- `config.py`: Device IPs, tokens, and F1MV settings

## ⚙️ Usage

1. Update `config.py` with your Nanoleaf IP(s) and auth token(s)
2. Run the app:
```bash
python main.py
```

## 🛣️ Roadmap

- [ ] Add support for purple sectors and fastest laps
- [ ] Track pit stop events
- [ ] Display dashboard with driver stats
- [ ] Alexa/Stream Deck voice & button integrations
- [ ] Event replay assistant with highlight markers

## 🧠 Built With

- Python
- Nanoleaf OpenAPI
- F1 Multiviewer API

---

Enjoy race weekends with lightshow flair ✨