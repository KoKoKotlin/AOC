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

FOLDER_NAME = f"aoc{year}/{day}"

if os.path.exists(FOLDER_NAME):
    answer = input(f"The folder for aoc {2021} day {day} already exits! Do you want to override it? [y/N]: ")
    if answer not in ["y", "Y", "yes", "Yes"]: 
        print("Exiting ...")
        exit(0)
    else:
        print("Overriding ...")

os.system(f"mkdir -p {FOLDER_NAME}")
os.system(f"cp -rf templates/{lang}/* {FOLDER_NAME}/")
os.system(f"chmod +x {FOLDER_NAME}/run.sh")
os.system(f"touch {FOLDER_NAME}/data.txt")
os.system(f"touch {FOLDER_NAME}/test.txt")
