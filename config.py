from pathlib import Path

CURRENT_FILE = Path(__file__).resolve()
print(CURRENT_FILE)
ROOT_DIR = CURRENT_FILE.parent

NAMES_TXT = str(ROOT_DIR / "data/names.txt")
