from lib.grammar_check import *

def test_grammar_check_returns_false_for_one_uncap_word():
    result = grammar_check("hello")
    assert result == False

def test_grammar_check_returns_false_one_cap_word_no_punctuation():
    result = grammar_check("Hello")
    assert result == False

def test_grammar_check_returns_false_uncap_word_with_punctuation():
    result = grammar_check("hello.")
    assert result == False

def test_grammar_check_returns_true_cap_word_with_punctuation():
    result = grammar_check("Hello.")
    assert result == True

def test_grammar_check_returns_false_mixed_case_word_starting_uncap():
    result = grammar_check("hEllO.")
    assert result == False

def test_grammar_check_returns_false_contains_fullstop_but_not_last():
    result = grammar_check("Box. Your Stuff. Out the front door. Parking lot. Car. Goodbye")
    assert result == False

def test_grammar_check_accepts_exclamation_as_valid():
    result = grammar_check("Stress doesn't ship lemonade!")
    assert result == True

def test_grammar_check_returns_true_contains_comma_ends_question_mark():
    result = grammar_check("I don't want your damn lemons, what am I supposed to do with these?")
    assert result == True

def test_grammar_check_returns_false_ends_semi_colon():
    result = grammar_check("Good news is we've got a much better test for you:")
    assert result == False


