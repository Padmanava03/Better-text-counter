from text_counter import betterCounter
from pathlib import Path
from time import sleep

print("""
Analyzes a text file and reports:
- Letter count
- Word count
- Sentence count

Requires a valid file path.
""")


FILE_PATH = input("Enter the file path...\n")

ABS_PATH = Path(FILE_PATH).resolve()

print("Trying to access the file...\n")
sleep(2)

if Path(ABS_PATH).exists():
    print("File accessed, reading the file...\n")
    sleep(2)

    letters, words, sentences = betterCounter(ABS_PATH)

    print(f"Letters: {letters}")
    print(f"Words: {words}")
    print(f"Sentences: {sentences}")

else:
    print("No such file or directory!")