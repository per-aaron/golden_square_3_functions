# Grammar Check Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

>As a user
>So that I can improve my grammar
>I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

Assuming for single sentence only or that we'll only consider the start and end of the text and not intermediate ones.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def grammar_check(text):
    """Checks whether text starts with capital letter and ends with one of ['.','?','!']

    Parameters:
        text: a string containing english words, most likely a single sentence (e.g. "Please check this sentence for me.")

    Returns:
        Boolean (True if valid or False if not)

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given one uncapitalized word
It returns False
"""
grammar_check("hello") => False

"""
Given one capitalized word without punctuation
It returns False
"""
grammar_check("Hello") => False

"""
Given one uncapitalized word with a full stop at the end
It returns False
"""
grammar_check("hello.") => False

"""
Given one capitalized word with a full stop at the end
It returns True
"""
grammar_check("Hello.") => True

"""
Given a word starting lowercase but containing uppercase and ending with a full stop
It returns False
"""
grammar_check("hELLO.") => False

"""
Given multiple words, starting with a capital, but with full stops between them and none at the end
It returns False
"""
grammar_check("Box. Your Stuff. Out the front door. Parking lot. Car. Goodbye") => False

"""
Given a sentence starting with a capital and ending with an !
It returns True
"""
grammar_check("Stress doesn't ship lemonade!") => True

"""
Given a sentence starting with a capital, contains a comma and ends with an ?
It returns True
"""
grammar_check("I don't want your damn lemons, what am I supposed to do with these?") => True

"""
Given a sentence starting with a capital and ends with an :
It returns False
"""
grammar_check("Good news is we've got a much better test for you:") => False
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
