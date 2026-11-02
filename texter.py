#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
"""Flask random sentence generator with project-relative resources."""
from pathlib import Path
import secrets

BASE_DIR = Path(__file__).resolve().parent

def load_sentences(path: Path | None = None) -> list[str]:
    source = path if path is not None else BASE_DIR / "fortunes.txt"
    with source.open("r", encoding="utf-8-sig") as handle:
        return [text.strip() for text in handle.read().split("%") if text.strip()]

def choose_sentence(sentences: list[str]) -> str:
    if not sentences:
        raise ValueError("No sentences are available")
    return secrets.choice(sentences)

def create_app(sentences_path: Path | None = None):
    from flask import Flask, render_template
    application = Flask(__name__, template_folder=str(BASE_DIR / "templates"), static_folder=str(BASE_DIR / "static"))
    application.config["SENTENCES_FILE"] = str(sentences_path or BASE_DIR / "fortunes.txt")

    @application.get("/")
    def index():
        try:
            sentence = choose_sentence(load_sentences(Path(application.config["SENTENCES_FILE"])))
        except (OSError, UnicodeError, ValueError):
            return "Sentences temporarily unavailable", 503
        return render_template("index.html", msg=sentence)

    return application

# Preserve the original WSGI import contract: from texter import app.
app = create_app()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
