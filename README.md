# Lochana DN — Portfolio Website

## Run locally on macOS

1. Install Python 3.
2. Open this folder in Visual Studio Code.
3. Open Terminal in VS Code and run:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

4. Open http://127.0.0.1:5000 in your browser.

## Backend feature

The Contact Me form sends a POST request to Flask's `/contact` route. Flask checks the fields and saves each message in `messages.db` using SQLite.

## Before publishing

- Check that your details are correct.
- Add project details when you have projects to show.
- Set a secure `SECRET_KEY` environment variable on the hosting service.
- Do not run Flask in debug mode in production.
- Use persistent storage or a hosted database if you need messages to remain available after redeployments.
