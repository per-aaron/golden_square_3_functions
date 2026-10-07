# Estimate Reading Time Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

>As a user
>So that I can manage my time
>I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def estimate_reading_time(text, words_per_minute=200):
    """Estimates time taken to read a given text based on the number of words and reading speed

    Parameters: (list all parameters and their types)
        text: a string containing words (e.g. "hello world")
        (optional) words_per_minute: an integer that gives the reading speed in words per minute, defaults to 200 per the user story

    Returns: (state the return value and its type)
        returns float representing number of minutes it would take to read the given text
        e.g. 14.1

    Side effects: (state any side effects)
        (future?) prints a formatted string stating the number of hours and minutes it would take to read, to the closest minute
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE
"""
Given text of 200 words with default reading speed
It returns 1
"""
estimate_reading_time("...200 words...") => 1

"""
Given text of 2 words with default reading speed
It returns .001 (2/200)
"""
estimate_reading_time("hi everybody") => .01

"""
Given empty string
Exception raised for "Empty string entered"
"""
estimate_reading_time("")
# Raises error: "Empty string entered"

"""
Given the 9162 word bee movie script with default reading speed
It returns 45.785 minutes (9157/200)
"""
estimate_reading_time(bee_movie_script) => 45.785

"""
Given 3 words with a reading speed of 30
It returns 0.1
"""
estimate_reading_time("hello dr. nick", 20) => .1
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
