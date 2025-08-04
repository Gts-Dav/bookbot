def get_num_words(text):
    return len(text.split())


def get_char_counts(text):
    lowercase_text = text.lower()
    char_counts = {}

    for char in lowercase_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts


def sort_char_counts(char_counts):
    def sort_on(char_counts):
        return char_counts["num"]

    chars_and_counts = []

    for char in char_counts:
        chars_and_counts.append({"char": char, "num": char_counts[char]})

    chars_and_counts.sort(reverse=True, key=sort_on)
    return chars_and_counts
