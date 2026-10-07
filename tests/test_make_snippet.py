from lib.make_snippet import *

#When given an empty string
#empty string is returned
def test_make_snippet_returns_empty_string_from_empty_string():
    result = make_snippet("")
    assert result == ""

#When a short string of five words is entered
#That string is returned
def test_make_snippet_returns_whole_short_string():
    result = make_snippet("hello this is five words")
    assert result == "hello this is five words"

#When a string longer than five words is entered
#only the first five are returned folowed by an elipsis
def test_make_snippet_returns_first_five():
    result = make_snippet("hello this message is cut off")
    assert result == "hello this message is cut..."