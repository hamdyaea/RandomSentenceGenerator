# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("texter", Path(__file__).resolve().parents[1] / "texter.py")

class SentenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            import flask
        except ImportError:
            raise unittest.SkipTest("Install requirements.txt for Flask integration tests")
        cls.mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.mod)

    def test_load_actual_count(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "fortunes.txt"
            path.write_text(" one % two % % three ", encoding="utf-8")
            self.assertEqual(self.mod.load_sentences(path), ["one", "two", "three"])

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            self.mod.choose_sentence([])

    def test_http_route(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "fortunes.txt"
            path.write_text("only option", encoding="utf-8")
            app = self.mod.create_app(path)
            app.testing = True
            response = app.test_client().get("/")
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"only option", response.data)

if __name__ == "__main__":
    unittest.main()
