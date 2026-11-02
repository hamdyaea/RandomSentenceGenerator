# Random Sentence Generator

**Developer:** Hamdy Abou El Anein  
**Contact:** info@daylightlinux.ch  
**License:** Check the repository's license before redistribution.

A Flask web application that selects one sentence from the project-local `fortunes.txt`. Empty entries are ignored; the number of sentences is determined dynamically.

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python texter.py
python -m unittest discover -s tests -v
```

Open `http://127.0.0.1:5000/`. For WSGI servers, import `app` from `texter`. The development server is not intended for public production use. The historical version is preserved on the [old branch](https://github.com/hamdyaea/RandomSentenceGenerator/tree/old).
