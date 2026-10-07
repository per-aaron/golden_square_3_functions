from lib.count_words import *

#Given a single word as a string
#Count words returns 1
def test_count_words_returns_1_for_single_word():
    result = count_words("hello")
    assert result == 1

#Given five word string seperated with spaces
#Count words returns 5
def test_count_words_returns_five_for_five_words():
    result = count_words("hello this is five words")
    assert result == 5

#Given an empty string
#Count words returns 0
def test_count_words_returns_zero_for_empty_string():
    result = count_words("")
    assert result == 0

#Given a two word string with a trailing space
#Count words returns two
def test_count_words_deals_with_trailing_space():
    result = count_words("Hello space ")
    assert result == 2
