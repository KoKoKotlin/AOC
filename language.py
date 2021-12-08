from random import choice
from sys import argv
import os

if len(argv) != 3:
    print(f"Usage: python3 language.py <year> <day>")

languages = ["python", "kotlin", "java", "rust", "c", "cpp", "perl", "haskell", "ruby", "js"]

_, year, day = argv

lang = choice(languages)
print(f"Next language will be: {lang}.")

os.system(f"mkdir -p aoc{year}/{day}")
os.system(f"cp -rf templates/{lang}/* aoc{year}/{day}/")
os.system(f"chmod +x aoc{year}/{day}/run.sh")