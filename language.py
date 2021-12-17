from random import choice
from sys import argv
import os

if len(argv) not in [3, 4]:
    print(f"Usage: python3 language.py <year> <day> [<language>]")

languages = ["python", "kotlin", "java", "rust", "c", "cpp", "perl", "haskell", "ruby", "js"]

_, year, day, *argv = argv

lang = choice(languages)

if len(argv) == 1:
    lang, *argv = argv    

print(f"Next language will be: {lang}.")

os.system(f"mkdir -p aoc{year}/{day}")
os.system(f"cp -rf templates/{lang}/* aoc{year}/{day}/")
os.system(f"chmod +x aoc{year}/{day}/run.sh")
os.system(f"touch aoc{year}/{day}/data.txt")
os.system(f"touch aoc{year}/{day}/test.txt")
