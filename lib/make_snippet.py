def make_snippet(string):
    word_array = string.split(" ")
    if len(word_array) > 5:
        return f"{" ".join(word_array[:5])}..."
    else:
        return string