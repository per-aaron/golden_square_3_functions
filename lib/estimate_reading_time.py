def estimate_reading_time(text, reading_speed = 200):
    sanitised_text = text.strip()
    if len(sanitised_text) > 0:
        text_array = sanitised_text.split()
        no_of_words = len(text_array)
        return no_of_words/reading_speed
    else:
        raise Exception("Empty string entered")
