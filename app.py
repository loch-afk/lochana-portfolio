from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from pathlib import Path

app = Flask(__name__)
app.secret_key = "change-this-to-a-random-secret"
DB_PATH = Path("messages.db")


def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                message TEXT NOT NULL
            )
        """)


# Create the database table when the app starts, including on hosted servers.
init_db()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        flash("Please fill in all three fields.")
        return redirect(url_for("home") + "#contact")

    if "@" not in email or "." not in email:
        flash("Please enter a valid email address.")
        return redirect(url_for("home") + "#contact")

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO messages (name, email, message) VALUES (?, ?, ?)",
            (name, email, message)
        )

    flash("Thank you! Your message has been received.")
    return redirect(url_for("home") + "#contact")


if __name__ == "__main__":
    app.run(debug=True)
