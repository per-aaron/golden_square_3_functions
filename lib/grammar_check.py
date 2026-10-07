def grammar_check(text):
    terminal_punct = ".!?"
    if text[0].islower() or text[-1] not in terminal_punct:
        return False
    else:
        return True