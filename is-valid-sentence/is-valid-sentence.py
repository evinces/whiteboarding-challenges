"""Is Valid Sentence

Given a dictionary of valid words. Validate that a sentence without
spaces or punctiation consists only of valid words.

Example:

    >>> dictionary = {
            "hello", "hi", "goodbye", "i", "you",
            "me", "we", "is", "am", "are",
            "uber", "ubers", "yes", "no", "maybe",
        }

    >>> is_valid_sentence("iamuber")
    True

    >>> is_valid_sentence("ixam")
    Flase

"""


def is_valid_sentence(sentence, dictionary):
    """Determine if sentence consists only of words from dictionary

    In:
        sentence -> str
        dictionary -> set(str)
    Out:
        bool

    """

    starting_index, validated_chars = 0

    for i in range(len(sentence)):
        search_string = sentence[starting_index:i + 1]

        if search_string in dictionary:
            validated_chars += len(search_string)
            starting_index = i + 1

    return validated_chars == len(sentence)
