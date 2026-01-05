import re

def betterCounter(FILE_NAME):
    """
    The `betterCounter` function takes a file name as input, reads the file, and counts the total number
    of letters, words, and sentences in the file using regular expressions.
    
    :param FILE_NAME: The function `betterCounter` is designed to count the total number of letters,
    words, and sentences in a text file. It uses regular expressions to match patterns for letters,
    words, and sentences
    :return: The function `betterCounter` is returning a tuple containing the total count of letters,
    words, and sentences found in the file specified by the `FILE_NAME` parameter.
    """
    pattern_letter = re.compile(r"[a-zA-Z]")
    pattern_word = re.compile(r"\b[a-zA-Z-']+\b")
    pattern_sentence = re.compile(r"\w+(\.|\?|!)")

    total_letters = 0
    total_words = 0
    total_sentences = 0

    with open(FILE_NAME, "r") as f:
        for line in f.readlines():
            total_letters += len(list(pattern_letter.finditer(line)))
            total_words += len(list(pattern_word.finditer(line)))
            total_sentences += len(list(pattern_sentence.finditer(line)))


    return total_letters, total_words, total_sentences

def main():
    letters, words, senetences = betterCounter("test.txt")
    print(letters, words, senetences)

if __name__ == "__main__":
    main()
