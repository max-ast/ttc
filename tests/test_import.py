import importlib

MODULES = ["app.main", "app.asr", "app.tts", "app.rag"]

def test_imports():
    for mod in MODULES:
        importlib.import_module(mod)
