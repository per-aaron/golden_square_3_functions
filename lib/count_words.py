def count_words(text):
    sanitised_string = text.strip()
    if len(sanitised_string) > 0:
        return sanitised_string.count(" ") + 1
    else:
        return 0